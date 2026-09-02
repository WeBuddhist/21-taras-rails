"""Stage 2 — align a root text with its commentaries at verse level.

Deterministic first, LLM only for the remainder. The reason for that ordering is that
alignment errors are silent: a verse anchored to the wrong commentary span produces a
citation that looks perfectly well-formed and is simply wrong. Deterministic matching can
fail to find a verse, but it cannot invent a location, so it goes first and the LLM only
sees what is left.

Measured behaviour (Bodhicaryāvatāra chapter 1, 37 verses, transclusion anchors as ground
truth, ``min_score=3.0``), on commentaries with their existing anchors stripped:

===========================================  =========  =========  =======
commentary                                   precision  recall     kind
===========================================  =========  =========  =======
Khenpo Zhenga (BCAC19_KS)                          96%        59%  prose
Ngulchu Thogmed (BCAC14_NTS)                       95%        51%  prose
Gyaltsab (BCAC14_GDR)                              77%        46%  prose
Khenpo Kunpal (BCAC19_KKP)                         58%        19%  word
===========================================  =========  =========  =======

The split is structural, not a tuning problem. A prose commentary quotes the stanza and
then expounds it, so fragments of the verse really are present to be found. A word
commentary (ཚིག་འགྲེལ / མཆན་འགྲེལ) dissolves the verse into its glosses — of the four lines of
BCA 1-1, exactly one survives intact anywhere in Kunpal's text — so there is often nothing
left to match on. **Deterministic alignment cannot carry a word-commentary; that is what
the LLM pass and the human checkpoint are for.** Recall here is a budget for how much LLM
work stage 2 needs, not a quality target to be tuned upward: raising it by lowering the
threshold trades away the precision that makes the deterministic anchors worth having.

Where a corpus already carries transclusion anchors from a sibling rails vault (as the
Bodhicaryāvatāra does), those are human-checked and are used directly — coverage is then
effectively complete and none of the above applies.

Ported from the proven implementation at
``4-SYSTEM/Skills/Transclusion-rootext-into-commentaries/scripts/01_transclude_verses.py``.
"""

from __future__ import annotations

import json
import re
from bisect import bisect_right
from dataclasses import dataclass, asdict, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Callable, Final

from ..tibetan.normalize import fuzzy_key, fuzzy_key_with_map, nfc

# A stanza quoted in a commentary rarely matches the root byte-for-byte: editions differ in
# orthography and scribes abbreviate. 0.80 on the fuzzy key is the threshold the vendored
# script has used in production; below it, false positives start appearing.
MATCH_THRESHOLD = 0.80

# Below this many characters a "match" is not evidence of anything — short strings collide.
MIN_MATCH_CHARS = 8

BLOCK_ID_RE = re.compile(r"\^([\w-]+)\s*$")
TRANSCLUSION_RE = re.compile(r"!\[\[[^\]]*?#\^([\w-]+)\]\]")


@dataclass
class Verse:
    """One root-text stanza, addressed by its block ID."""

    verse_id: str
    text: str
    line_no: int


@dataclass
class AlignedSpan:
    """A stretch of one commentary that comments on one root verse."""

    verse_id: str
    source_id: str
    start_line: int
    end_line: int
    text: str
    method: str  # 'transclusion' | 'verbatim' | 'fuzzy' | 'llm'
    confidence: float

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AlignmentReport:
    """Coverage summary — the artifact a human reads at the stage-2 checkpoint."""

    corpus: str
    total_verses: int
    spans: list[AlignedSpan] = field(default_factory=list)
    unanchored: dict[str, list[str]] = field(default_factory=dict)  # source_id -> [verse_id]

    def coverage(self) -> dict[str, float]:
        """Fraction of root verses anchored, per commentary."""
        per_source: dict[str, set[str]] = {}
        for s in self.spans:
            per_source.setdefault(s.source_id, set()).add(s.verse_id)
        return {
            src: len(vids) / self.total_verses if self.total_verses else 0.0
            for src, vids in sorted(per_source.items())
        }

    def to_dict(self) -> dict:
        return {
            "corpus": self.corpus,
            "total_verses": self.total_verses,
            "coverage": self.coverage(),
            "spans": [s.to_dict() for s in self.spans],
            "unanchored": self.unanchored,
        }

    def format_summary(self) -> str:
        lines = [f"Alignment coverage — {self.corpus} ({self.total_verses} root verses)", ""]
        for src, frac in self.coverage().items():
            n_missing = len(self.unanchored.get(src, []))
            lines.append(f"  {frac:6.1%}  {src}" + (f"   ({n_missing} unanchored)" if n_missing else ""))
        by_method: dict[str, int] = {}
        for s in self.spans:
            by_method[s.method] = by_method.get(s.method, 0) + 1
        lines += ["", "  spans by method: " + ", ".join(f"{k}={v}" for k, v in sorted(by_method.items()))]
        return "\n".join(lines)


def parse_root(path: Path) -> list[Verse]:
    """Read a root text, returning every block-ID'd stanza.

    Headings (IDs ending in ``-0``) are editorial structure, not content, so they are skipped.
    """
    verses: list[Verse] = []
    buf: list[str] = []
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines()):
        line = raw.rstrip()
        is_heading = line.lstrip().startswith("#")
        m = BLOCK_ID_RE.search(line)
        if not m:
            if line.strip() and not is_heading and not line.lstrip().startswith(("---", "![[")):
                buf.append(line)
            elif not line.strip():
                buf = []
            continue
        vid = m.group(1)
        # Headings carry block IDs too (the `-0` slot, plus the bare `^0` on the title line),
        # but they are editorial structure rather than root-text content.
        if is_heading or vid.endswith("-0") or vid == "0":
            buf = []
            continue
        body = BLOCK_ID_RE.sub("", line).rstrip()
        if body.strip():
            buf.append(body)
        text = "\n".join(buf).strip()
        buf = []
        if not text:
            continue
        verses.append(Verse(verse_id=vid, text=text, line_no=i + 1))
    return verses


def _existing_transclusions(lines: list[str]) -> dict[str, int]:
    """Verse IDs already transcluded in a commentary, mapped to their line index.

    Commentaries in the sibling rails vaults are already aligned this way; reusing those
    anchors means we inherit work that has already been human-checked.
    """
    found: dict[str, int] = {}
    for i, line in enumerate(lines):
        for m in TRANSCLUSION_RE.finditer(line):
            found.setdefault(m.group(1), i)
    return found


def _ratio(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


# --------------------------------------------------------------------------
# Probe-cluster matching
# --------------------------------------------------------------------------
#
# A prose commentary (འགྲེལ་པ) quotes the stanza and then expounds it, so the stanza
# appears contiguously and a whole-stanza search finds it. A word-commentary
# (ཚིག་འགྲེལ / མཆན་འགྲེལ) does not: it dissolves the verse, glossing a phrase at a time,
# so the stanza *never* appears as a contiguous string. Measured on Khenpo Kunpal's
# commentary, whole-stanza search anchors 0 of 37 chapter-1 verses; only one of the four
# lines of verse 1-1 survives intact anywhere in the file.
#
# So instead of asking "where does this stanza appear", we ask "where do fragments of this
# stanza cluster". Each verse contributes probes — its lines (specific, heavily weighted)
# and short character n-grams (fragile individually, but telling in aggregate). Wherever a
# dense cluster of a verse's probes lands, that is where the commentary is discussing it.

PROBE_NGRAM: Final = 9
PROBE_STRIDE: Final = 3
PROBE_MIN_LINE: Final = 12
CLUSTER_WINDOW: Final = 4000  # characters of fuzzy_key space
MIN_CLUSTER_SCORE: Final = 3.0  # precision-first; see the table in the module docstring
MAX_HITS_PER_PROBE: Final = 40  # a probe matching everywhere is noise, not signal


@dataclass
class _Probe:
    text: str
    weight: float


def _build_probes(verse: Verse) -> list[_Probe]:
    """Fragments whose co-occurrence identifies a verse's commentary."""
    probes: list[_Probe] = []
    seen: set[str] = set()
    for line in verse.text.splitlines():
        key = fuzzy_key(line)
        if len(key) >= PROBE_MIN_LINE and key not in seen:
            seen.add(key)
            probes.append(_Probe(key, 3.0))
    flat = fuzzy_key(verse.text)
    for i in range(0, max(0, len(flat) - PROBE_NGRAM + 1), PROBE_STRIDE):
        g = flat[i : i + PROBE_NGRAM]
        if g not in seen:
            seen.add(g)
            probes.append(_Probe(g, 1.0))
    return probes


def _probe_hits(flat: str, probes: list[_Probe]) -> list[tuple[int, int, float]]:
    """Every occurrence of every probe, as (position, probe_index, weight)."""
    hits: list[tuple[int, int, float]] = []
    for pi, p in enumerate(probes):
        if not p.text:
            continue
        start = 0
        n = 0
        while n < MAX_HITS_PER_PROBE:
            j = flat.find(p.text, start)
            if j < 0:
                break
            hits.append((j, pi, p.weight))
            start = j + 1
            n += 1
    hits.sort()
    return hits


def _best_clusters(hits: list[tuple[int, int, float]], top_k: int = 5) -> list[tuple[float, int]]:
    """Densest windows of distinct probes, as (score, start_position).

    Score counts each probe once per window however often it recurs there — a single
    phrase repeated ten times is weaker evidence than ten different phrases appearing once.
    """
    if not hits:
        return []
    out: list[tuple[float, int]] = []
    lo = 0
    counts: dict[int, int] = {}
    score = 0.0
    for hi in range(len(hits)):
        pos, pi, w = hits[hi]
        counts[pi] = counts.get(pi, 0) + 1
        if counts[pi] == 1:
            score += w
        while hits[hi][0] - hits[lo][0] > CLUSTER_WINDOW:
            _, lpi, lw = hits[lo]
            counts[lpi] -= 1
            if counts[lpi] == 0:
                del counts[lpi]
                score -= lw
            lo += 1
        out.append((score, hits[lo][0]))
    out.sort(key=lambda t: (-t[0], t[1]))
    deduped: list[tuple[float, int]] = []
    for s, p in out:
        if all(abs(p - q) > CLUSTER_WINDOW // 2 for _, q in deduped):
            deduped.append((s, p))
        if len(deduped) >= top_k:
            break
    return deduped


def _monotonic_assign(
    candidates: list[list[tuple[float, int]]],
) -> list[int | None]:
    """Choose one cluster per verse so positions increase down the text.

    Commentaries follow their root text in order. Treating that as a constraint rather
    than a coincidence resolves the ambiguity that sinks naive matching: a phrase recurring
    in chapters 1 and 9 is pinned to the right one by its neighbours. This is a longest
    increasing subsequence weighted by cluster score, solved exactly by O(n^2) DP — n is
    the number of verses in a chapter, so the quadratic cost is irrelevant.
    """
    n = len(candidates)
    chosen: list[int | None] = [None] * n
    if not n:
        return chosen

    # Flatten to one node per (verse, candidate position). A verse contributes no node when
    # it has no candidate, which is how "this commentary never discusses this verse" is
    # represented — skipping is free, so a silent commentary costs the chain nothing.
    nodes: list[tuple[int, int, float]] = []  # (verse_index, position, score)
    for i, opts in enumerate(candidates):
        for score, pos in opts:
            nodes.append((i, pos, score))
    if not nodes:
        return chosen
    nodes.sort(key=lambda t: (t[0], t[1]))

    # dp[k] = best achievable total for a chain ending at node k.
    dp = [0.0] * len(nodes)
    back = [-1] * len(nodes)
    for k, (vi, pos, score) in enumerate(nodes):
        dp[k] = score
        for m in range(k):
            vm, pm, _ = nodes[m]
            if vm < vi and pm < pos and dp[m] + score > dp[k]:
                dp[k] = dp[m] + score
                back[k] = m

    k = max(range(len(nodes)), key=lambda idx: dp[idx])
    while k >= 0:
        vi, pos, _ = nodes[k]
        chosen[vi] = pos
        k = back[k]
    return chosen


def _span_end(start: int, lines: list[str], next_anchor: int | None) -> int:
    """Where a verse's commentary ends: at the next anchored verse, or the next heading."""
    limit = next_anchor if next_anchor is not None else len(lines)
    for i in range(start + 1, limit):
        if lines[i].lstrip().startswith("#"):
            return i
    return limit


def align_commentary(
    verses: list[Verse],
    commentary_path: Path,
    source_id: str,
    *,
    min_score: float = MIN_CLUSTER_SCORE,
) -> tuple[list[AlignedSpan], list[str]]:
    """Align every root verse against one commentary.

    Returns the spans found and the verse IDs that could not be anchored — the latter are
    what a later LLM pass would be asked about, and what the human checkpoint reports.
    """
    text = commentary_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    transcluded = _existing_transclusions(lines)
    anchors: dict[str, tuple[int, str, float]] = {}

    # An existing transclusion is a human-checked anchor from a sibling rails vault; it
    # always wins over anything we could infer.
    remaining = []
    for v in verses:
        if v.verse_id in transcluded:
            anchors[v.verse_id] = (transcluded[v.verse_id], "transclusion", 1.0)
        else:
            remaining.append(v)

    if remaining:
        # Work in one flat fuzzy_key string so probe lookup is a C-level substring search,
        # and keep a map back to line numbers for reporting.
        flat, index = fuzzy_key_with_map(text)
        line_starts = [0]
        for ln in lines[:-1]:
            line_starts.append(line_starts[-1] + len(ln) + 1)

        def flat_pos_to_line(p: int) -> int:
            if not index or p >= len(index):
                return 0
            return max(0, bisect_right(line_starts, index[p]) - 1)

        candidates = [_best_clusters(_probe_hits(flat, _build_probes(v))) for v in remaining]
        chosen = _monotonic_assign(candidates)

        for v, pos, cands in zip(remaining, chosen, candidates):
            if pos is None:
                continue
            score = next((s for s, p in cands if p == pos), 0.0)
            if score < min_score:
                continue
            # Confidence is the share of the verse's own probe weight recovered at this
            # site, capped below 1.0: a cluster is corroboration, never proof of a quotation.
            total_w = sum(p.weight for p in _build_probes(v)) or 1.0
            anchors[v.verse_id] = (flat_pos_to_line(pos), "cluster", min(0.95, score / total_w))

    ordered = sorted(anchors.items(), key=lambda kv: kv[1][0])
    spans: list[AlignedSpan] = []
    for idx, (vid, (start, method, conf)) in enumerate(ordered):
        next_start = ordered[idx + 1][1][0] if idx + 1 < len(ordered) else None
        end = _span_end(start, lines, next_start)
        body = "\n".join(lines[start:end]).strip()
        if not body:
            continue
        spans.append(
            AlignedSpan(
                verse_id=vid,
                source_id=source_id,
                start_line=start + 1,
                end_line=end,
                text=body,
                method=method,
                confidence=conf,
            )
        )

    anchored = {vid for vid, _ in ordered}
    unanchored = [v.verse_id for v in verses if v.verse_id not in anchored]
    return spans, unanchored


def verify_spans(spans: list[AlignedSpan], loader) -> list[str]:
    """Confirm every span is a real, contiguous stretch of its commentary file.

    An LLM asked to align will happily return a plausible span that does not exist. This
    check is what makes the LLM pass safe to use at all: we accept its *judgement* about
    which passage is relevant, never its *reproduction* of the text.
    """
    problems: list[str] = []
    cache: dict[str, list[str]] = {}
    for s in spans:
        if s.source_id not in cache:
            cache[s.source_id] = loader(s.source_id).splitlines()
        lines = cache[s.source_id]
        if not (1 <= s.start_line <= s.end_line <= len(lines)):
            problems.append(f"{s.source_id}#{s.verse_id}: line range {s.start_line}-{s.end_line} out of bounds")
            continue
        actual = fuzzy_key("\n".join(lines[s.start_line - 1 : s.end_line]))
        if fuzzy_key(s.text) not in actual:
            problems.append(f"{s.source_id}#{s.verse_id}: span text is not a contiguous span of the source")
    return problems


def align_corpus(
    root_path: Path,
    commentary_paths: dict[str, Path],
    corpus: str,
    *,
    min_score: float = MIN_CLUSTER_SCORE,
) -> AlignmentReport:
    """Align a root text against every commentary in a corpus."""
    verses = parse_root(root_path)
    report = AlignmentReport(corpus=corpus, total_verses=len(verses))
    for source_id, path in sorted(commentary_paths.items()):
        spans, unanchored = align_commentary(verses, path, source_id, min_score=min_score)
        report.spans.extend(spans)
        if unanchored:
            report.unanchored[source_id] = unanchored
    return report


def save_alignment(report: AlignmentReport, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(report.to_dict(), ensure_ascii=False, indent=1), encoding="utf-8"
    )


def load_alignment(path: Path) -> AlignmentReport:
    data = json.loads(path.read_text(encoding="utf-8"))
    rep = AlignmentReport(corpus=data["corpus"], total_verses=data["total_verses"])
    rep.spans = [AlignedSpan(**s) for s in data["spans"]]
    rep.unanchored = data.get("unanchored", {})
    return rep


def spans_for_term(report: AlignmentReport, term: str, source_texts: dict[str, str] | None = None) -> list[AlignedSpan]:
    """Every aligned span whose commentary text mentions the term.

    This is what keeps per-term extraction affordable: instead of sending 16 MB of commentary
    to the model for each term, we send only the spans that actually contain it.
    """
    key = fuzzy_key(nfc(term))
    return [s for s in report.spans if key and key in fuzzy_key(s.text)]


@dataclass
class TermSegment:
    """One addressable commentary block that mentions a term.

    A span runs from a verse's anchor to the next one and can be thousands of
    characters; a segment is one block inside it. This is the unit a citation
    should name — ``TARAC02_DGT#^1-1-2-1`` tells a reader which paragraph to
    read, where the span alone only tells them which book.
    """

    source_id: str
    #: The commentary's own block ID (``stages.commentary.stamp_block_ids``).
    #: Empty for a corpus whose commentaries have not been through stage 1b.
    block_id: str
    #: The root verse this block's span is anchored to.
    verse_id: str
    start_line: int
    end_line: int
    text: str
    confidence: float

    @property
    def locator(self) -> str:
        """``TARAC02_DGT#^1-1-2-1`` — what a citation records."""
        return f"{self.source_id}#^{self.block_id}" if self.block_id else self.source_id

    def to_dict(self) -> dict:
        return asdict(self)


def segments_for_term(
    report: AlignmentReport,
    term: str,
    load_source: Callable[[str], str] | None = None,
) -> list[TermSegment]:
    """The individual commentary blocks that mention ``term``, with their IDs.

    Two filters, not one. The alignment says which stretches of which commentary
    discuss which root verse; this narrows that to the blocks inside those
    stretches that actually contain the term. A 2,000-character span in which
    the term appears once becomes the one paragraph it appears in — which is
    both what the model should be reading and what the footnote should point at.

    ``load_source`` reads a commentary's full text by ``source_id``. Without it
    (or for a commentary carrying no block IDs) each span is returned whole, so
    this degrades to :func:`spans_for_term` rather than returning nothing.
    """
    from .commentary import parse_blocks  # local: keeps align.py importable alone

    key = fuzzy_key(nfc(term))
    if not key:
        return []

    segments: list[TermSegment] = []
    cache: dict[str, list] = {}

    for span in report.spans:
        if key not in fuzzy_key(span.text):
            continue

        blocks = None
        if load_source is not None:
            if span.source_id not in cache:
                try:
                    cache[span.source_id] = parse_blocks(load_source(span.source_id))
                except Exception:  # noqa: BLE001 - an unreadable source is one lost locator
                    cache[span.source_id] = []
            blocks = [
                b
                for b in cache[span.source_id]
                if not b.is_heading
                and span.start_line <= b.start_line
                and b.end_line <= span.end_line
                and key in fuzzy_key(b.text)
            ]

        if not blocks:
            segments.append(
                TermSegment(
                    source_id=span.source_id,
                    block_id="",
                    verse_id=span.verse_id,
                    start_line=span.start_line,
                    end_line=span.end_line,
                    text=span.text,
                    confidence=span.confidence,
                )
            )
            continue

        for block in blocks:
            segments.append(
                TermSegment(
                    source_id=span.source_id,
                    block_id=block.block_id,
                    verse_id=span.verse_id,
                    start_line=block.start_line,
                    end_line=block.end_line,
                    text=block.text,
                    confidence=span.confidence,
                )
            )
    return segments
