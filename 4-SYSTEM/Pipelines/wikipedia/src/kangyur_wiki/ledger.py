"""Per-corpus run state — the file that makes a run resumable.

One ``corpora/<corpus-id>/ledger.json`` records where every term got to.  A
Gemini batch over 500 terms costs real money and real wall-clock time; a crash,
a rate limit or a ``^C`` at term 380 must not mean starting over, and the only
way to guarantee that is to write the status down as it happens.

Two rules make this file trustworthy:

**Writes are atomic.**  ``os.replace`` onto the real path after the temp file is
fully written and fsynced.  A ledger truncated mid-write would be worse than no
ledger at all — it would silently claim terms were never processed and re-bill
the whole batch.

**Timestamps are injected, never taken.**  Nothing here calls
``datetime.now()``.  The caller passes ``updated_at``; the stage that knows it
did work is the one that knows when.  That keeps every function here pure and
every test deterministic.

The ledger stores *terms as given*.  It does no Tibetan normalisation beyond
NFC, because term identity is the registry's job
(``kangyur_wiki.registry.find_term``): if two modules both guessed at
orthographic equivalence they would eventually disagree, and the ledger would
lose track of a term mid-run.  Canonicalise through the registry first, then
talk to the ledger.
"""

from __future__ import annotations

import json
import os
import tempfile
import unicodedata
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Iterable, Mapping

__all__ = [
    "LEDGER_FILENAME",
    "LEDGER_VERSION",
    "TermStatus",
    "LedgerEntry",
    "Ledger",
    "atomic_write_text",
    "ledger_path",
]

#: Name of the per-corpus ledger file (PLAN.md §2).
LEDGER_FILENAME = "ledger.json"

#: Schema version written into the file.  Bumped only on a breaking change, so
#: an old ledger can be recognised rather than silently misread.
LEDGER_VERSION = 1

#: Mode for a file ``atomic_write_text`` creates.  These files are committed
#: and read by a human; 0600 (what ``mkstemp`` gives) is not what they expect.
DEFAULT_FILE_MODE = 0o644


class TermStatus(str, Enum):
    """Where a term is in the pipeline (create path: extract → claims → outline →
    draft [→ polish] → audit → verify → approve → publish).

    Declaration order is pipeline order, and ``summary()`` reports in that
    order, so a glance at the summary reads as progress rather than as an
    alphabetical jumble.  ``FAILED`` is terminal and deliberately last: a term
    can fail out of any stage.
    """

    PENDING = "pending"
    EXTRACTED = "extracted"
    CLAIMED = "claimed"
    ORGANIZED = "organized"
    DRAFTED = "drafted"
    AUDITED = "audited"
    VERIFIED = "verified"
    APPROVED = "approved"
    PUBLISHED = "published"
    FAILED = "failed"

    @classmethod
    def parse(cls, value: "TermStatus | str") -> "TermStatus":
        """Accept the stored value, the member name, or the member itself.

        Ledgers get hand-edited during a review session; ``"PUBLISHED"`` and
        ``"published"`` must not mean different things.
        """
        if isinstance(value, cls):
            return value
        text = str(value).strip()
        try:
            return cls(text.lower())
        except ValueError:
            pass
        try:
            return cls[text.upper()]
        except KeyError:
            raise ValueError(f"unknown term status: {value!r}") from None


def _entry_key(term: str) -> str:
    """Dict key for a term: NFC, outer whitespace gone, nothing else touched.

    Tibetan punctuation is orthography and stays in the key — see the module
    docstring on why the ledger refuses to guess about equivalence.
    """
    return unicodedata.normalize("NFC", term).strip()


@dataclass
class LedgerEntry:
    """One term's row in the ledger.

    ``artifacts`` maps a stage name to a path *relative to the corpus
    directory* — relative so the corpus can be moved, zipped or shared without
    invalidating every recorded path.  ``metrics`` carries the numbers the
    paper's evaluation needs (``tokens``, ``cost_usd``, ``review_seconds``);
    it is an open dict because a stage that learns to measure something new
    should not require a schema change to record it.
    """

    term: str
    status: TermStatus
    updated_at: str
    error: str | None = None
    artifacts: dict[str, str] = field(default_factory=dict)
    wiki_title: str | None = None
    wiki_revid: int | None = None
    metrics: dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.term = unicodedata.normalize("NFC", self.term).strip()
        self.status = TermStatus.parse(self.status)

    @property
    def key(self) -> str:
        """The dict key this entry is filed under."""
        return _entry_key(self.term)

    def to_dict(self) -> dict[str, Any]:
        """JSON-ready form.  Empty optional fields are omitted, so a ledger of
        mostly-pending terms stays readable in a diff."""
        data: dict[str, Any] = {
            "term": self.term,
            "status": self.status.value,
            "updated_at": self.updated_at,
        }
        if self.error is not None:
            data["error"] = self.error
        if self.artifacts:
            data["artifacts"] = dict(self.artifacts)
        if self.wiki_title is not None:
            data["wiki_title"] = self.wiki_title
        if self.wiki_revid is not None:
            data["wiki_revid"] = self.wiki_revid
        if self.metrics:
            data["metrics"] = dict(self.metrics)
        return data

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "LedgerEntry":
        """Rebuild from stored JSON, tolerating a hand-edited file.

        Unknown keys are dropped rather than raising: a human who added a note
        column to the ledger should lose the note, not the run.
        """
        term = str(data.get("term", "")).strip()
        if not term:
            raise ValueError("ledger entry has no term")
        revid = data.get("wiki_revid")
        return cls(
            term=term,
            status=TermStatus.parse(data.get("status", TermStatus.PENDING)),
            updated_at=str(data.get("updated_at", "")),
            error=_optional_str(data.get("error")),
            artifacts={str(k): str(v) for k, v in dict(data.get("artifacts") or {}).items()},
            wiki_title=_optional_str(data.get("wiki_title")),
            wiki_revid=int(revid) if revid is not None else None,
            metrics={str(k): v for k, v in dict(data.get("metrics") or {}).items()},
        )


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value)
    return text or None


@dataclass
class Ledger:
    """The whole ledger, in memory.

    ``entries`` is insertion-ordered, and ``save`` writes a JSON *list*, so the
    file's diff shows the terms that changed rather than reshuffling on every
    write.
    """

    corpus_id: str = ""
    entries: dict[str, LedgerEntry] = field(default_factory=dict)
    path: Path | None = None

    # -- persistence -------------------------------------------------------

    @classmethod
    def load(cls, path: str | os.PathLike[str], *, corpus_id: str = "") -> "Ledger":
        """Read a ledger, or return an empty one if the file does not exist.

        A missing ledger is the normal state of a first run, not an error;
        making the caller handle ``FileNotFoundError`` would push that
        distinction into every stage.

        ``corpus_id`` fills in the name only when the file does not supply one,
        so the first save of a fresh run is already labelled and a later save
        can never overwrite the id an existing ledger carries.
        """
        resolved = Path(path)
        if not resolved.exists():
            return cls(corpus_id=corpus_id, entries={}, path=resolved)
        raw = json.loads(resolved.read_text(encoding="utf-8"))
        ledger = cls.from_dict(raw, path=resolved)
        if not ledger.corpus_id:
            ledger.corpus_id = corpus_id
        return ledger

    @classmethod
    def from_dict(
        cls, data: Mapping[str, Any], *, path: str | os.PathLike[str] | None = None
    ) -> "Ledger":
        """Rebuild from a parsed ledger document."""
        entries: dict[str, LedgerEntry] = {}
        for item in data.get("entries") or ():
            entry = LedgerEntry.from_dict(item)
            entries[entry.key] = entry
        return cls(
            corpus_id=str(data.get("corpus_id", "")),
            entries=entries,
            path=Path(path) if path is not None else None,
        )

    def to_dict(self) -> dict[str, Any]:
        """JSON-ready form of the whole ledger."""
        return {
            "version": LEDGER_VERSION,
            "corpus_id": self.corpus_id,
            "entries": [entry.to_dict() for entry in self.entries.values()],
        }

    def save(self, path: str | os.PathLike[str] | None = None) -> Path:
        """Write atomically and remember where.

        Returns the path written so a caller can log it.  ``path`` may be
        omitted once the ledger knows its own location (after ``load``).
        """
        target = Path(path) if path is not None else self.path
        if target is None:
            raise ValueError("Ledger.save needs a path: this ledger has no path set")
        text = json.dumps(self.to_dict(), ensure_ascii=False, indent=2) + "\n"
        atomic_write_text(target, text)
        self.path = target
        return target

    # -- queries -----------------------------------------------------------

    def get(self, term: str) -> LedgerEntry | None:
        """Look up a term.  Exact match on the NFC-normalised string."""
        return self.entries.get(_entry_key(term))

    def entries_by_status(self, status: TermStatus | str) -> list[LedgerEntry]:
        """Every entry at ``status``, in insertion order.

        This is how a stage picks up its work: ``entries_by_status(EXTRACTED)``
        is exactly the queue for the organize stage.
        """
        wanted = TermStatus.parse(status)
        return [entry for entry in self.entries.values() if entry.status is wanted]

    def summary(self) -> dict[str, int]:
        """Count per status in pipeline order, plus ``total``.

        Every status appears even at zero, so a progress line has a stable
        shape across a run instead of growing columns as terms advance.
        """
        counts = {status.value: 0 for status in TermStatus}
        for entry in self.entries.values():
            counts[entry.status.value] += 1
        counts["total"] = len(self.entries)
        return counts

    # -- mutation ----------------------------------------------------------

    def upsert(self, entry: LedgerEntry) -> LedgerEntry:
        """Insert or wholly replace one entry.  Returns the stored entry."""
        self.entries[entry.key] = entry
        return entry

    def set_status(
        self,
        term: str,
        status: TermStatus | str,
        updated_at: str,
        *,
        error: str | None = None,
        artifacts: Mapping[str, str] | None = None,
        wiki_title: str | None = None,
        wiki_revid: int | None = None,
        metrics: Mapping[str, float] | None = None,
    ) -> LedgerEntry:
        """Advance one term, creating its entry if this is the first stage to touch it.

        ``artifacts`` and ``metrics`` are **merged**, not replaced: stage 6
        recording ``draft.md`` must not erase stage 4's ``extracts.json``, and
        the review-time cost must not erase the drafting cost.  ``error`` is
        cleared on any non-``FAILED`` status, so a term that fails and is then
        retried successfully does not keep a stale error next to a green
        status.

        ``updated_at`` is required and caller-supplied — see the module
        docstring.
        """
        resolved = TermStatus.parse(status)
        existing = self.get(term)
        if existing is None:
            entry = LedgerEntry(term=term, status=resolved, updated_at=updated_at)
            self.entries[entry.key] = entry
        else:
            entry = existing
            entry.status = resolved
            entry.updated_at = updated_at

        # Assigned unconditionally: passing no error means there is no error,
        # which is what clears the message left by an earlier failed attempt.
        entry.error = error
        if artifacts:
            entry.artifacts.update({str(k): str(v) for k, v in artifacts.items()})
        if wiki_title is not None:
            entry.wiki_title = wiki_title
        if wiki_revid is not None:
            entry.wiki_revid = wiki_revid
        if metrics:
            entry.metrics.update({str(k): v for k, v in metrics.items()})
        return entry

    def seed(self, terms: Iterable[str], updated_at: str) -> list[LedgerEntry]:
        """Add any missing term at ``PENDING``; leave existing entries alone.

        Run after the term stage approves a list.  Idempotent, so re-running it
        after the human adds three more terms costs nothing and loses nothing.
        """
        added: list[LedgerEntry] = []
        for term in terms:
            key = _entry_key(term)
            if not key or key in self.entries:
                continue
            entry = LedgerEntry(term=term, status=TermStatus.PENDING, updated_at=updated_at)
            self.entries[key] = entry
            added.append(entry)
        return added


def ledger_path(corpora_dir: str | os.PathLike[str], corpus_id: str) -> Path:
    """``<corpora_dir>/<corpus_id>/ledger.json`` — the one place a ledger lives."""
    return Path(corpora_dir) / corpus_id / LEDGER_FILENAME


def atomic_write_text(
    path: str | os.PathLike[str], text: str, *, encoding: str = "utf-8"
) -> Path:
    """Write ``text`` to ``path`` so that readers only ever see old or new, never half.

    Temp file in the *same directory* (``os.replace`` is only atomic within a
    filesystem), fsync before the rename (otherwise a power loss can leave the
    rename durable and the contents not), then replace.  The temp file is
    removed if anything fails, so a crashed run does not litter the corpus
    directory with partial ledgers.

    The replacement keeps the mode the file already had, or takes
    ``DEFAULT_FILE_MODE`` when there was none — ``mkstemp`` creates at 0600,
    and silently making a version-controlled corpus file owner-only on every
    save would be a surprising side effect of writing to it.

    Shared with ``kangyur_wiki.registry``: the corpus YAML deserves the same
    guarantee, and one implementation is one thing to get right.
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        mode = target.stat().st_mode & 0o777
    except OSError:
        mode = DEFAULT_FILE_MODE
    fd, temp_name = tempfile.mkstemp(
        dir=str(target.parent), prefix=f".{target.name}.", suffix=".tmp"
    )
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp_path, mode)
        os.replace(temp_path, target)
    except BaseException:
        temp_path.unlink(missing_ok=True)
        raise
    return target
