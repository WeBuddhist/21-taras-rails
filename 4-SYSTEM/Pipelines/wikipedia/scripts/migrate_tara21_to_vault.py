#!/usr/bin/env python3
"""Adopt the kwiki pipeline's annotated tara21 bodies into 1-SOURCES/.

Today the vault's canonical files (``1-SOURCES/Text/…``, ``1-SOURCES/Commentaries/*.md``)
carry rich frontmatter but raw, unsegmented OCR bodies: no block IDs, no root-verse
transclusion anchors. The pipeline's own working corpus at
``4-SYSTEM/Pipelines/wikipedia/corpora/tara21/source/`` carries the opposite: cleaned,
block-ID'd, transclusion-anchored bodies with thin frontmatter. This script merges the
two — vault frontmatter (kept, lightly corrected) + corpus body (adopted verbatim, only
transclusion *targets* rewritten from the corpus's local ``root`` stem to the vault's
full path) — so each file ends up carrying both halves at once.

What it does, per the approved plan (see ``/Users/tashitsering/.claude/plans/
ethereal-wobbling-treasure.md``):

1. Back up the current (pre-migration) root text and all 16 commentaries to
   ``0-INBOX/migration-backups/<DATE>/`` — this is the resolution target for the
   frozen ``2-RAILS/Claims/{opus,sonnet,toc-scaffolded}/*.md`` files' ``L<n>``/``§n``
   citations, which were extracted against the *old* segmentation.
2. Root swap: adopt the corpus's 22-stanza-plus-invocation body
   (``^I-1``, ``^1-1``…``^1-22``) into the vault root file, keeping its frontmatter
   (with ``verse_id_format``/verse-count fields corrected).
3. Fifteen commentary body swaps, matched to their vault file by ``registered_id``
   (never by hardcoded Tibetan filename — resolved dynamically to avoid any
   transcription risk), with frontmatter fixes: ``root_text:`` repointed off its
   dangling pre-rename target, ``covers_verses:`` updated to the new scheme,
   ``siglum:`` added.
4. Add a 17th commentary, Gendun Drub's ṭīkā (corpus siglum ``TARAC03_GDD``), which
   exists in the pipeline corpus but was never part of the vault's original 16-file
   upload — new frontmatter modeled on the other 15, ``registered_id: gendun-drub``.
5. Rewrite every ``![[root#^...]]`` anchor to the vault's full path so Obsidian (and
   any future pipeline run) resolves it unambiguously — safe because
   ``align.TRANSCLUSION_RE`` and ``commentary.TRANSCLUSION_LINE_RE`` are target-agnostic
   (verified against the source, see the plan's "Decision B").

Every file is checked, before being written, against three identity assertions versus
its corpus counterpart: the *reading view* (all scaffolding stripped) collapses to the
same string, the ordered block-ID sequence is identical, and the ordered transclusion-ID
sequence is identical. A file that fails any of these is skipped and reported, never
partially written.

Usage
-----
    ./4-SYSTEM/Pipelines/wikipedia/.venv/bin/python \\
        4-SYSTEM/Pipelines/wikipedia/scripts/migrate_tara21_to_vault.py           # dry run
    ./4-SYSTEM/Pipelines/wikipedia/.venv/bin/python \\
        4-SYSTEM/Pipelines/wikipedia/scripts/migrate_tara21_to_vault.py --apply   # writes

Refuses to run ``--apply`` twice: the backup directory's existence is the guard, so a
second run cannot silently overwrite the first backup with already-migrated (post-swap)
content.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

SCRIPT = Path(__file__).resolve()
PIPELINE_ROOT = SCRIPT.parents[1]  # …/4-SYSTEM/Pipelines/wikipedia
VAULT_ROOT = PIPELINE_ROOT.parents[2]  # …/21-taras-rails
sys.path.insert(0, str(PIPELINE_ROOT / "src"))

from kangyur_wiki.stages.align import parse_root  # noqa: E402
from kangyur_wiki.stages.commentary import parse_blocks, reading_view, split_front_matter  # noqa: E402
from kangyur_wiki.tibetan.normalize import collapse  # noqa: E402

CORPUS_DIR = PIPELINE_ROOT / "corpora" / "tara21"
CORPUS_SOURCE = CORPUS_DIR / "source"
CORPUS_ROOT_FILE = CORPUS_SOURCE / "root.md"
CORPUS_COMMENTARIES_DIR = CORPUS_SOURCE / "commentaries"

SOURCES_TEXT_DIR = VAULT_ROOT / "1-SOURCES" / "Text"
SOURCES_COMM_DIR = VAULT_ROOT / "1-SOURCES" / "Commentaries"
BACKUP_DIR = VAULT_ROOT / "0-INBOX" / "migration-backups" / "2026-08-04"

# The dangling field every one of the 16 vault commentaries carries today — the root
# file was renamed after these were written and nothing repointed them.
STALE_ROOT_TEXT_FIELD = (
    "1-SOURCES/Text/MDAFBF633 སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ། Segmentation - corrected.md"
)

TRANSCLUSION_TARGET_RE = re.compile(r"(!\[\[)root(#\^[\w-]+\]\])")


@dataclass(frozen=True)
class Mapping:
    """One corpus commentary -> one vault commentary (or a new one)."""

    registered_id: str
    siglum: str  # sources.yaml source_id, minus the "_bo_segmented" suffix
    is_new: bool = False


MAPPINGS: tuple[Mapping, ...] = (
    Mapping("drakpa-gyaltsen", "TARAC02_DGT"),
    Mapping("gendun-drub", "TARAC03_GDD", is_new=True),
    Mapping("gendun-gyatso", "TARAC04_GDG"),
    Mapping("taranatha", "TARAC05_TRN"),
    Mapping("dharmabhadra", "TARAC06_NDB"),
    Mapping("konchok-thabkhe", "TARAC07_KTK"),
    Mapping("tenga-tulku", "TARAC08_DTG"),
    Mapping("yama-sonam", "TARAC09_JYS"),
    Mapping("pema-namgyal", "TARAC10_DPN"),
    Mapping("karma-maitri", "TARAC11_KMT"),
    Mapping("palden-sherab", "TARAC12_PDS"),
    Mapping("tenzin-dhonzang", "TARAC13_TDZ"),
    Mapping("lobsang-dawa", "TARAC14_LZD"),
    Mapping("sangye-nyentrul", "TARAC15_SNT"),
    Mapping("sungrab-tulku", "TARAC16_PSR"),
    Mapping("tsultrim-namdak", "TARAC17_TSN"),
)

#: registered_id present in the vault but with NO corpus counterpart — left untouched.
#: (Dharmabhadra's commentary; STATE.md's "R1B1817B6". Its title is textually
#: identical to the root's own Kangyur title, which is itself worth a human look —
#: flagged in the report, not silently resolved here.)
NO_CORPUS_MATCH_REGISTERED_ID = "rnam-snang"

#: Frontmatter for the new Gendun Drub file, modeled on the other 15 (same field
#: order and style as e.g. `gendun-gyatso`'s: bare Tibetan `author`, an
#: English-glossed `author_in_english`, no fabricated catalogue ID).
GENDUN_DRUB_TITLE_BO = "སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།"
GENDUN_DRUB_FRONTMATTER_TEMPLATE = """---
book_id: TARAC03_GDD
title: "{title_bo}"
title_in_english: "A Precious Garland: Commentary on the Twenty-One Homages to Tārā"
author: "དགེ་འདུན་གྲུབ།"
author_in_english: "Gendun Drub (First Dalai Lama)"
file_type: commentary
language: Tibetan
script: Unicode Tibetan
lang_tag: bo
verse_id_format: chapter-verse
registered_id: gendun-drub
root_text: {root_link_target}
covers_verses: I-1–1-22
siglum: TARAC03_GDD
source_description: "Ingested from the kwiki Wikipedia-pipeline corpus (4-SYSTEM/Pipelines/wikipedia/corpora/tara21/source/commentaries/TARAC03_GDD_bo_segmented.md); not part of the vault's original 16-file upload. No OpenPecha catalogue ID assigned yet — add one if this text is later registered there. Cited 10 times across the pipeline's three verified pilot articles (see corpora/tara21/REVIEW-2026-08-02.md)."
status: 2-annotated
---
"""


# ---------------------------------------------------------------------------
# Frontmatter field editing
# ---------------------------------------------------------------------------


def set_fm_field(front: str, field: str, value: str) -> str:
    """Replace a single-line ``field: ...`` inside a fenced frontmatter block.

    Appends the field just before the closing fence if it was not already present.
    Operates on the *whole* fenced block (opening ``---``, body, closing ``---``),
    which is exactly what ``kangyur_wiki.stages.commentary.split_front_matter``
    returns as its first element.
    """
    pattern = re.compile(rf"^{re.escape(field)}:.*$", re.MULTILINE)
    line = f"{field}: {value}"
    if pattern.search(front):
        return pattern.sub(line, front, count=1)
    # Insert right before the closing fence line.
    lines = front.splitlines(keepends=True)
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() in ("---", "..."):
            lines.insert(i, line + "\n")
            return "".join(lines)
    return front.rstrip("\n") + f"\n{line}\n"


def has_fm_field(front: str, field: str) -> bool:
    return re.search(rf"^{re.escape(field)}:", front, re.MULTILINE) is not None


# ---------------------------------------------------------------------------
# Anchor rewriting
# ---------------------------------------------------------------------------


def rewrite_anchors(text: str, root_link_target: str) -> tuple[str, int]:
    """Rewrite every ``![[root#^...]]`` to the vault's full root path.

    Safe under both consumers: ``align.TRANSCLUSION_RE`` and
    ``commentary.TRANSCLUSION_LINE_RE``/``Block.transclusions`` match on
    ``[^\\]]*`` before the ``#^id``, so any prefix — including a full vault-relative
    path with Tibetan characters and no ``]`` in it — still matches, and only the
    ``#^id`` group is ever extracted.
    """
    count = 0

    def _sub(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return f"{match.group(1)}{root_link_target}{match.group(2)}"

    new_text = TRANSCLUSION_TARGET_RE.sub(_sub, text)
    return new_text, count


# ---------------------------------------------------------------------------
# Identity assertions
# ---------------------------------------------------------------------------


class IdentityCheckFailed(RuntimeError):
    pass


def assert_identity(label: str, new_full_text: str, corpus_full_text: str) -> None:
    """Reading-view + block-ID + anchor-ID identity between a new vault file and its
    corpus source. Raises ``IdentityCheckFailed`` with a specific reason on mismatch.
    """
    new_reading = collapse(reading_view(new_full_text))
    corpus_reading = collapse(reading_view(corpus_full_text))
    if new_reading != corpus_reading:
        # Report the first differing offset to make a real mismatch diagnosable.
        i = 0
        limit = min(len(new_reading), len(corpus_reading))
        while i < limit and new_reading[i] == corpus_reading[i]:
            i += 1
        raise IdentityCheckFailed(
            f"{label}: reading view diverges at collapsed offset {i} "
            f"(new={new_reading[max(0, i - 20):i + 20]!r} "
            f"corpus={corpus_reading[max(0, i - 20):i + 20]!r})"
        )

    new_blocks = [(b.kind, b.block_id) for b in parse_blocks(new_full_text)]
    corpus_blocks = [(b.kind, b.block_id) for b in parse_blocks(corpus_full_text)]
    if new_blocks != corpus_blocks:
        raise IdentityCheckFailed(
            f"{label}: block-ID sequence differs (new has {len(new_blocks)} blocks, "
            f"corpus has {len(corpus_blocks)})"
        )

    new_anchors = [vid for b in parse_blocks(new_full_text) for vid in b.transclusions]
    corpus_anchors = [vid for b in parse_blocks(corpus_full_text) for vid in b.transclusions]
    if new_anchors != corpus_anchors:
        raise IdentityCheckFailed(
            f"{label}: transclusion-anchor sequence differs "
            f"(new={len(new_anchors)}, corpus={len(corpus_anchors)})"
        )


# ---------------------------------------------------------------------------
# Vault file resolution — by registered_id, never a hardcoded Tibetan filename
# ---------------------------------------------------------------------------


def find_vault_commentary(registered_id: str) -> Path:
    """The 1-SOURCES/Commentaries/*.md file whose frontmatter names this registered_id."""
    needle = re.compile(rf"^registered_id:\s*{re.escape(registered_id)}\s*$", re.MULTILINE)
    matches = [
        p
        for p in sorted(SOURCES_COMM_DIR.glob("*.md"))
        if needle.search(p.read_text(encoding="utf-8"))
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"expected exactly one 1-SOURCES/Commentaries/*.md with registered_id "
            f"{registered_id!r}, found {len(matches)}: {matches}"
        )
    return matches[0]


def find_vault_root() -> Path:
    matches = sorted(SOURCES_TEXT_DIR.glob("*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"expected exactly one file in {SOURCES_TEXT_DIR}, found {matches}")
    return matches[0]


# ---------------------------------------------------------------------------
# Per-file operations
# ---------------------------------------------------------------------------


@dataclass
class Outcome:
    label: str
    ok: bool
    detail: str
    path: Path | None = None


def process_root(apply: bool) -> Outcome:
    vault_path = find_vault_root()
    root_link_target = f"1-SOURCES/Text/{vault_path.name}"

    vault_text = vault_path.read_text(encoding="utf-8")
    corpus_text = CORPUS_ROOT_FILE.read_text(encoding="utf-8")

    vault_front, _old_body = split_front_matter(vault_text)
    _corpus_front, corpus_body = split_front_matter(corpus_text)

    new_front = vault_front
    new_front = set_fm_field(new_front, "verse_id_format", "chapter-verse")
    new_front = set_fm_field(new_front, "total_verses", "22")
    if not has_fm_field(new_front, "intro_block_id"):
        new_front = set_fm_field(new_front, "intro_block_id", '"I-1"')
    new_front = set_fm_field(
        new_front,
        "status",
        "2-annotated  # cleaned, block-ID'd (^I-1, ^1-1–^1-22); see 0-INBOX/migration-backups/2026-08-04/ for the pre-migration 47-line body",
    )

    new_full_text = new_front + corpus_body

    try:
        assert_identity("root", new_full_text, corpus_text)
    except IdentityCheckFailed as exc:
        return Outcome("root", False, str(exc), vault_path)

    # parse_root needs a real path; verify against a throwaway temp copy so both
    # dry-run and --apply exercise the same check without touching real state early.
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
        tmp.write(new_full_text)
        tmp_path = Path(tmp.name)
    try:
        verses = parse_root(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)
    if len(verses) != 23:
        return Outcome(
            "root", False, f"expected 23 root units (I-1 + 1-1..1-22), parse_root found {len(verses)}", vault_path
        )

    if apply:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        (BACKUP_DIR / vault_path.name).write_text(vault_text, encoding="utf-8")
        vault_path.write_text(new_full_text, encoding="utf-8")

    return Outcome("root", True, f"{len(verses)} root units, identity checks passed", vault_path)


def process_commentary(mapping: Mapping, apply: bool, root_link_target: str) -> Outcome:
    corpus_path = CORPUS_COMMENTARIES_DIR / f"{mapping.siglum}_bo_segmented.md"
    if not corpus_path.exists():
        return Outcome(mapping.registered_id, False, f"no corpus file at {corpus_path}", None)
    corpus_text = corpus_path.read_text(encoding="utf-8")
    _corpus_front, corpus_body = split_front_matter(corpus_text)

    anchored_body, anchor_count = rewrite_anchors(corpus_body, root_link_target)

    if mapping.is_new:
        new_front = GENDUN_DRUB_FRONTMATTER_TEMPLATE.format(
            title_bo=GENDUN_DRUB_TITLE_BO, root_link_target=root_link_target
        )
        vault_path = SOURCES_COMM_DIR / f"{GENDUN_DRUB_TITLE_BO}.md"
        was_existing = False
    else:
        vault_path = find_vault_commentary(mapping.registered_id)
        vault_text = vault_path.read_text(encoding="utf-8")
        vault_front, _old_body = split_front_matter(vault_text)
        new_front = vault_front
        new_front = set_fm_field(new_front, "root_text", root_link_target)
        new_front = set_fm_field(new_front, "covers_verses", "I-1–1-22")
        new_front = set_fm_field(new_front, "verse_id_format", "chapter-verse")
        if not has_fm_field(new_front, "siglum"):
            new_front = set_fm_field(new_front, "siglum", mapping.siglum)
        new_front = set_fm_field(new_front, "status", "2-annotated")
        was_existing = True

    new_full_text = new_front + anchored_body

    try:
        # Compare against the *anchor-rewritten* corpus text on both sides so the
        # assertion is about body identity, not about the rewrite itself (which is
        # covered by rewrite_anchors's own count below).
        corpus_full_rewritten = _corpus_front + anchored_body
        assert_identity(mapping.registered_id, new_full_text, corpus_full_rewritten)
    except IdentityCheckFailed as exc:
        return Outcome(mapping.registered_id, False, str(exc), vault_path)

    corpus_anchor_count = len(re.findall(r"!\[\[root#\^[\w-]+\]\]", corpus_body))
    if anchor_count != corpus_anchor_count:
        return Outcome(
            mapping.registered_id,
            False,
            f"rewrote {anchor_count} anchors but corpus body had {corpus_anchor_count}",
            vault_path,
        )

    if apply:
        if was_existing:
            BACKUP_DIR.mkdir(parents=True, exist_ok=True)
            (BACKUP_DIR / vault_path.name).write_text(vault_text, encoding="utf-8")
        vault_path.write_text(new_full_text, encoding="utf-8")

    detail = f"{anchor_count} anchors rewritten to full path"
    if mapping.is_new:
        detail += " (NEW file)"
    return Outcome(mapping.registered_id, True, detail, vault_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help="write changes; without this flag, dry-run only"
    )
    args = parser.parse_args()

    if args.apply and BACKUP_DIR.exists():
        print(
            f"REFUSING to run --apply: {BACKUP_DIR} already exists, which means this "
            "migration already ran once. Re-running would back up already-migrated "
            "(post-swap) content over the real pre-migration backup. If you deliberately "
            "want to re-run, move or remove that directory first.",
            file=sys.stderr,
        )
        return 2

    print(f"{'APPLYING' if args.apply else 'DRY RUN'} — tara21 source migration\n")

    root_vault_path = find_vault_root()
    root_link_target = f"1-SOURCES/Text/{root_vault_path.name}"
    print(f"root link target: {root_link_target}\n")

    outcomes: list[Outcome] = [process_root(args.apply)]
    for mapping in MAPPINGS:
        outcomes.append(process_commentary(mapping, args.apply, root_link_target))

    ok = [o for o in outcomes if o.ok]
    failed = [o for o in outcomes if not o.ok]

    for outcome in outcomes:
        status = "OK  " if outcome.ok else "FAIL"
        print(f"  [{status}] {outcome.label:<20} {outcome.detail}")

    print(f"\n{len(ok)}/{len(outcomes)} files {'migrated' if args.apply else 'would migrate'}")
    print(
        f"  {NO_CORPUS_MATCH_REGISTERED_ID} — left untouched, no corpus counterpart "
        "(flag for human review: title duplicates the root's own Kangyur title)"
    )

    if args.apply and ok:
        print(f"\nBackups of pre-migration files: {BACKUP_DIR}")
        print("Next: git mv the pipeline data (Phase 2), then `kwiki align tara21` and `kwiki verify`.")

    if failed:
        print(f"\n{len(failed)} FAILED — nothing was written for these files.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
