"""Stage 1b — finish a segmented commentary so its passages are addressable.

``commentary-segmentation`` leaves a file that is correctly *broken up* and
otherwise unmarked: no headings, no block IDs, no anchors back to the root text.
That is enough to align against, badly — the cluster matcher in
:mod:`~kangyur_wiki.stages.align` will find roughly where a verse is discussed
and hand the extractor everything from there to the next anchor, which on a
prose bstod-'grel is thousands of characters of undifferentiated text.  It is not
enough to *cite* against: a footnote can name the commentary but not the passage,
so a reader who wants to check a quotation is told which book to read.

This module adds the three layers that make a commentary citable, in the order
they have to happen:

1. **Headings** (``tag-inline-toc``) — the sa-bcad outline the commentator wrote
   becomes ``## <title> ^N-…-0``.  Finding them is meaning work and belongs to
   the model (:func:`build_toc_annotation`); assigning the IDs and proving no
   prose changed is the vendored Phase-2 renderer's job.
2. **Block IDs** (:func:`stamp_block_ids`) — every content block under a heading
   gets ``^<heading>-<n>``, so each paragraph has a name.
3. **Transclusion anchors** — ``![[root#^1-4]]`` before the passage that
   discusses root verse 1-4, which :func:`~kangyur_wiki.stages.align.align_commentary`
   trusts absolutely and which a human can check by eye.

Nothing here rewrites Tibetan.  Every function either inserts scaffolding on its
own line, appends an ID after a trailing space, or wraps an existing substring —
and :func:`reading_view` exists to take all of it back off again, because the
verification gate must compare a quotation against what the commentary *says*,
not against what ingest wrote in the margin.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

from ..config import repo_root
from ..tibetan.normalize import collapse

__all__ = [
    "BLOCK_ID_RE",
    "HEADING_RE",
    "TRANSCLUSION_LINE_RE",
    "INTRO_PREFIX",
    "TOC_SCHEMA",
    "Block",
    "StampReport",
    "split_front_matter",
    "parse_blocks",
    "stamp_block_ids",
    "reading_view",
    "blocks_containing",
    "number_lines",
    "sanitise_sections",
    "build_toc_annotation",
    "load_annotation",
    "skill_script",
    "run_script",
]

#: A block ID at the end of a line: a space, a caret, then word characters and
#: hyphens.  The leading whitespace is part of the match so stripping an ID
#: leaves no trailing space behind.
BLOCK_ID_RE = re.compile(r"[ \t]+\^([\w-]+)[ \t]*$")

#: ``## <title> ^1-2-0`` — the heading form ``tag_inline_toc.py`` emits.  The ID
#: group is optional because a file's own title line usually has none yet.
HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})[ \t]+(?P<title>.*?)(?:[ \t]+\^(?P<id>[\w-]+))?[ \t]*$")

#: A line that is nothing but a transclusion.  These are navigation, never
#: content: they take no block ID of their own and they never open a block.
TRANSCLUSION_LINE_RE = re.compile(r"^[ \t]*!\[\[[^\]]*\]\][ \t]*$")

#: A heading line that ``tag_inline_toc.py`` *inserted* — ``##``–``######`` plus a
#: depth-derived numeric ID ending in ``-0``.  Copied from that script's own
#: ``_HEADING_RE`` on purpose: its title is text the pipeline wrote, not the
#: commentator's words, and the two files must agree on which lines those are.
#: A heading without such an ID came in with the source and its text is the
#: commentary's own (a title line, or a sa-bcad promoted to a heading in a
#: sibling vault), so it is kept.
INSERTED_HEADING_RE = re.compile(r"^#{2,6}[ \t].*[ \t]\^[0-9]+(?:-[0-9]+)*-0[ \t]*$")

#: Where content that precedes the first heading is filed.  Matches the root
#: text's front-matter slot in ``docs/reference/conventions.md`` §1 — a
#: commentary's homage and title-gloss are the same kind of material.
INTRO_PREFIX = "I"

_FRONT_MATTER_RE = re.compile(r"\A---\r?\n(?P<body>.*?)\r?\n(?:---|\.\.\.)[ \t]*\r?\n", re.DOTALL)


# ---------------------------------------------------------------------------
# Reading the file
# ---------------------------------------------------------------------------


def split_front_matter(text: str) -> tuple[str, str]:
    """``(front matter including its fences, the rest)``.

    Front matter is metadata (``docs/reference/conventions.md`` §4) and every
    function here leaves it untouched, so it is split off once rather than
    special-cased in each walk.
    """
    match = _FRONT_MATTER_RE.match(text.lstrip("﻿"))
    if not match:
        return "", text
    return match.group(0), text[match.end() :]


@dataclass
class Block:
    """One blank-line-delimited unit of a commentary.

    ``lines`` are the raw source lines.  ``start_line`` and ``end_line`` are
    1-based and inclusive over the *whole* file (front matter included), so they
    can be compared directly against :class:`~kangyur_wiki.stages.align.AlignedSpan`
    line numbers.
    """

    lines: list[str]
    start_line: int
    end_line: int
    #: ``heading`` | ``content``.  A block whose first line is a markdown
    #: heading is structure; everything else is content, including a block that
    #: merely *contains* a transclusion line.
    kind: str = "content"
    #: The ID already present on the block's last content line, if any.
    block_id: str = ""
    #: For a heading: the number of ``#`` characters.
    level: int = 0
    #: For a heading: the title with the ID stripped.
    title: str = ""

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @property
    def is_heading(self) -> bool:
        return self.kind == "heading"

    @property
    def transclusions(self) -> list[str]:
        """Verse IDs anchored inside this block, in order."""
        return re.findall(r"!\[\[[^\]]*?#\^([\w-]+)\]\]", self.text)


def _last_content_index(lines: Sequence[str]) -> int:
    """Index of the last line that can carry a block ID.

    A block ID goes on the block's last line of *text*.  A transclusion is not
    text, so a block ending in one puts its ID on the line above; a block that is
    only transclusions gets none at all (``-1``).
    """
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i]
        if line.strip() and not TRANSCLUSION_LINE_RE.match(line):
            return i
    return -1


def parse_blocks(text: str) -> list[Block]:
    """Split a commentary body into blocks, classifying and reading each one.

    Blocks are separated by one or more blank lines — the layout every stage of
    ``commentary-segmentation`` emits.  A heading line always begins its own
    block even when no blank line precedes it, because the vault's transclusion
    spacing pass (Stage 3) deliberately glues a heading to the transclusion and
    stanza below it.
    """
    front, body = split_front_matter(text)
    offset = front.count("\n")

    blocks: list[Block] = []
    current: list[str] = []
    start = 0  # body index of the block's first line

    def flush(stop: int) -> None:
        """Close the open block, whose last line is body index ``stop - 1``."""
        nonlocal current
        if not current:
            return
        blocks.append(_build_block(current, offset + start + 1, offset + stop))
        current = []

    body_lines = body.splitlines()
    for index, line in enumerate(body_lines):
        if not line.strip():
            flush(index)
            continue
        if HEADING_RE.match(line):
            # A heading is always its own one-line block: it closes whatever came
            # before it and does not absorb what follows.  Both matter, because
            # the transclusion spacing pass deliberately glues a heading to the
            # anchor and stanza below it with no blank line between — and that
            # stanza is content that needs an ID of its own.
            flush(index)
            blocks.append(_build_block([line], offset + index + 1, offset + index + 1))
            continue
        if not current:
            start = index
        current.append(line)
    flush(len(body_lines))
    return blocks


def _build_block(lines: list[str], start_line: int, end_line: int) -> Block:
    heading = HEADING_RE.match(lines[0])
    if heading:
        return Block(
            lines=list(lines),
            start_line=start_line,
            end_line=end_line,
            kind="heading",
            block_id=heading.group("id") or "",
            level=len(heading.group("hashes")),
            title=heading.group("title").strip(),
        )
    last = _last_content_index(lines)
    existing = BLOCK_ID_RE.search(lines[last]) if last >= 0 else None
    return Block(
        lines=list(lines),
        start_line=start_line,
        end_line=end_line,
        kind="content",
        block_id=existing.group(1) if existing else "",
    )


# ---------------------------------------------------------------------------
# Stamping block IDs
# ---------------------------------------------------------------------------


@dataclass
class StampReport:
    """What one :func:`stamp_block_ids` run did, for the ingest report."""

    stamped: int = 0
    already_had_ids: int = 0
    headings: int = 0
    untagged_headings: list[str] = field(default_factory=list)
    intro_blocks: int = 0

    def format_summary(self) -> str:
        parts = [f"{self.stamped} stamped", f"{self.headings} headings"]
        if self.already_had_ids:
            parts.append(f"{self.already_had_ids} already had IDs")
        if self.intro_blocks:
            parts.append(f"{self.intro_blocks} before the first heading (^{INTRO_PREFIX}-*)")
        if self.untagged_headings:
            parts.append(f"{len(self.untagged_headings)} untagged headings")
        return ", ".join(parts)


def _heading_prefix(heading_id: str) -> str:
    """``1-2-0`` -> ``1-2``.  A heading ID always ends in the ``-0`` slot."""
    return heading_id[:-2] if heading_id.endswith("-0") else heading_id


def stamp_block_ids(text: str) -> tuple[str, StampReport]:
    """Give every content block an ID derived from the heading above it.

    Under ``## ཕྲིན་ལས། ^3-0`` the blocks become ``^3-1``, ``^3-2``, …; under a
    depth-2 heading ``^3-1-0`` they become ``^3-1-1``, ``^3-1-2``, …  Content
    that precedes the first heading is filed under ``^I-*``.  The ``-0`` suffix
    continues to mean "this is a heading", exactly as it does in a root text, so
    a reader of an ID can always tell structure from content.

    Idempotent: a block that already carries an ID keeps it, so this can be
    re-run over a partly-stamped file without renumbering anything.  Headings are
    never given IDs here — those come from ``tag_inline_toc.py``, which derives
    them from the sa-bcad depth and is the only thing entitled to.
    """
    front, body = split_front_matter(text)
    lines = body.splitlines()
    blocks = parse_blocks(text)
    offset = front.count("\n")

    report = StampReport()
    prefix = INTRO_PREFIX
    counter = 0
    edits: dict[int, str] = {}

    for block in blocks:
        if block.is_heading:
            report.headings += 1
            if block.block_id:
                prefix = _heading_prefix(block.block_id)
                counter = 0
            else:
                report.untagged_headings.append(block.title[:60])
            continue

        if block.block_id:
            report.already_had_ids += 1
            # Keep the numbering honest: a re-run must not reuse an ID that a
            # previous run already handed out under this heading.
            tail = block.block_id.rsplit("-", 1)[-1]
            if tail.isdigit():
                counter = max(counter, int(tail))
            continue

        last = _last_content_index(block.lines)
        if last < 0:
            continue  # a transclusion-only block is navigation, not content
        counter += 1
        block_id = f"{prefix}-{counter}"
        line_index = block.start_line - 1 - offset + last
        edits[line_index] = f"{lines[line_index].rstrip()} ^{block_id}"
        report.stamped += 1
        if prefix == INTRO_PREFIX:
            report.intro_blocks += 1

    for index, replacement in edits.items():
        lines[index] = replacement

    trailing = "\n" if body.endswith("\n") else ""
    return front + "\n".join(lines) + trailing, report


# ---------------------------------------------------------------------------
# Taking the scaffolding back off
# ---------------------------------------------------------------------------


def reading_view(text: str) -> str:
    """The commentary as text: every layer this module added, removed.

    The verification gate compares a quotation character-for-character against
    its source (``tibetan.verify``).  Once a file carries block IDs, transclusion
    lines and wikilink-wrapped sa-bcad terms, the bytes on disk are no longer the
    bytes the commentator wrote, and a perfectly faithful quotation spanning a
    block boundary would fail the gate on a caret we put there ourselves.

    So the loader reads *through* the scaffolding.  What is removed is exactly
    what ingest is allowed to add — IDs, transclusion lines, inserted headings,
    wikilink wrappers.  Not one Tibetan character is touched, and the line
    structure is preserved so reported offsets still land in the right place.

    An **inserted** heading goes entirely: its title is a short name the model
    wrote for the sa-bcad node, not something the commentator said, and an
    article must not be able to quote it as though it were.  A heading that came
    in with the source keeps its text and loses only the ``#`` marker.
    """
    front, body = split_front_matter(text)
    out: list[str] = [""] * front.count("\n")

    for line in body.splitlines():
        if TRANSCLUSION_LINE_RE.match(line) or INSERTED_HEADING_RE.match(line):
            out.append("")  # hold the line so offsets do not shift
            continue
        cleaned = BLOCK_ID_RE.sub("", line)
        heading = HEADING_RE.match(cleaned)
        if heading:
            cleaned = heading.group("title")
        cleaned = _unwrap_wikilinks(cleaned)
        out.append(cleaned)

    return "\n".join(out) + ("\n" if body.endswith("\n") else "")


_WIKILINK_RE = re.compile(r"\[\[(?:[^\]|\n]*\|)?([^\]\n]*)\]\]")


def _unwrap_wikilinks(line: str) -> str:
    """``[[#^1-2-0|བཤད་པ་]]`` -> ``བཤད་པ་``; the display text is the source's own."""
    return _WIKILINK_RE.sub(lambda m: m.group(1), line)


def blocks_containing(text: str, needle_key: str, key_of: Callable[[str], str]) -> list[Block]:
    """Every content block whose text matches ``needle_key`` under ``key_of``.

    ``key_of`` is injected rather than imported so this module stays free of the
    Tibetan comparison stack; callers pass ``tibetan.normalize.fuzzy_key``.
    """
    if not needle_key:
        return []
    return [
        block
        for block in parse_blocks(text)
        if not block.is_heading and needle_key in key_of(block.text)
    ]


# ---------------------------------------------------------------------------
# The sa-bcad outline (tag-inline-toc Phase 1)
# ---------------------------------------------------------------------------
#
# Finding the sa-bcad is meaning work and the skill forbids doing it with rules.
# What the model returns, though, is not prose: it is a list of line numbers,
# depths and short titles.  Everything that touches the commentary's own bytes
# stays in ``tag_inline_toc.py``, which copies them and then proves it changed
# nothing.

TOC_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "sections": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "body_start_line": {"type": "integer"},
                    "depth": {"type": "integer"},
                    "heading_title": {"type": "string"},
                },
                "required": ["body_start_line", "depth", "heading_title"],
            },
        }
    },
    "required": ["sections"],
}


def number_lines(text: str) -> str:
    """The body with 1-based *file* line numbers, blank lines dropped.

    Numbers count from the top of the file, front matter included, because that
    is the coordinate system ``tag_inline_toc.py`` resolves against.  Blank lines
    are not shown — they cost tokens and the model must never anchor to one — but
    they still consume a number, so the sequence has gaps and that is correct.
    """
    front, body = split_front_matter(text)
    offset = front.count("\n")
    return "\n".join(
        f"{offset + i + 1}\t{line}"
        for i, line in enumerate(body.splitlines())
        if line.strip()
    )


def sanitise_sections(sections: Sequence[dict], text: str) -> tuple[list[dict], list[str]]:
    """Drop or repair sections the renderer would reject, and say what changed.

    The renderer fails the whole file on the first bad section, which on a
    sixteen-commentary run means one hallucinated line number costs a
    commentary.  Everything checkable is therefore checked here, against the
    actual file, and the survivors are what get rendered:

    * a line number outside the file, or landing on a blank line, or on a line
      that is already a heading — dropped;
    * a line number that goes *backwards* — dropped, since sections are
      document-ordered by definition.  Repeating a line is allowed and normal:
      a parent node and its first child routinely open on the same sa-bcad line
      (``དེ་ལ་གསུམ། དང་པོ་ནི།``), and the renderer stacks both headings there.  What
      is rejected is a repeat that does not go *deeper*, which is a duplicate
      rather than a nesting;
    * a depth that skips a level — pulled back to one deeper than its parent,
      which is what the skill says to do when the intermediate level is unclear.

    Returns ``(kept, notes)``.  The notes go in the ingest report: a file that
    lost a third of its sections here needs a human, not a silent pass.
    """
    lines = text.splitlines()
    kept: list[dict] = []
    notes: list[str] = []
    previous_line = 0
    previous_depth = 0

    for raw in sections:
        try:
            line_no = int(raw.get("body_start_line", 0))
            depth = int(raw.get("depth", 0))
        except (TypeError, ValueError):
            notes.append(f"dropped a section with a non-numeric line or depth: {raw!r}")
            continue
        title = str(raw.get("heading_title", "")).strip()

        if not title:
            notes.append(f"line {line_no}: dropped, no heading_title")
            continue
        if not 1 <= line_no <= len(lines):
            notes.append(f"line {line_no}: dropped, outside the file (1-{len(lines)})")
            continue
        if not lines[line_no - 1].strip():
            notes.append(f"line {line_no}: dropped, anchors to a blank line")
            continue
        if HEADING_RE.match(lines[line_no - 1]):
            notes.append(f"line {line_no}: dropped, that line is already a heading")
            continue
        if line_no < previous_line:
            notes.append(f"line {line_no}: dropped, runs backwards past line {previous_line}")
            continue
        if line_no == previous_line and depth <= previous_depth:
            notes.append(
                f"line {line_no}: dropped, repeats that line at depth {depth} "
                f"without nesting under depth {previous_depth}"
            )
            continue

        if depth < 1:
            notes.append(f"line {line_no}: depth {depth} raised to 1")
            depth = 1
        if depth > previous_depth + 1:
            notes.append(
                f"line {line_no}: depth {depth} skips a level after depth "
                f"{previous_depth}, pulled back to {previous_depth + 1}"
            )
            depth = previous_depth + 1

        kept.append(
            {
                "body_start_line": line_no,
                "body_start_context": lines[line_no - 1].strip(),
                "depth": depth,
                "heading_title": title,
            }
        )
        previous_line = line_no
        previous_depth = depth

    return kept, notes


def build_toc_annotation(
    source_id: str,
    text: str,
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
) -> tuple[dict[str, Any], list[str]]:
    """Ask the model for the sa-bcad outline; return a renderer-ready annotation.

    ``generate`` and ``prompt_render`` are injected exactly as they are for
    stages 4–6, so this is testable with a stub and runs on whatever model the
    caller built.
    """
    prompt = prompt_render(stage="01-toc", source_id=source_id, numbered_text=number_lines(text))
    result = generate(prompt, schema=TOC_SCHEMA)
    data = result.parsed if hasattr(result, "parsed") else result
    sections, notes = sanitise_sections((data or {}).get("sections", []), text)
    return {"source_file": source_id, "sections": sections}, notes


# ---------------------------------------------------------------------------
# Driving the vendored skill scripts
# ---------------------------------------------------------------------------
#
# The ported skills are CLI scripts that have been run in production in the
# sibling vaults.  They are invoked as subprocesses rather than imported: their
# no-loss assertions call ``sys.exit`` and their module scope is not import-safe,
# and — more to the point — a script that has processed ten commentaries
# unmodified is worth more than a tidier reimplementation of it (CLAUDE.md).


def skill_script(skill: str, script: str) -> Path:
    """Absolute path to a script inside a ported skill's ``scripts/``.

    The skills now live in the vault proper — ``4-SYSTEM/Skills/<skill>/`` —
    two levels above this pipeline's root, where the rest of the vault invokes
    them too.  The old in-repo ``vendor/skills/`` layout is still accepted so a
    standalone checkout of the pipeline keeps working.
    """
    candidates = (
        repo_root().parents[1] / "Skills" / skill / "scripts" / script,
        repo_root() / "vendor" / "skills" / skill / "scripts" / script,
    )
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"ported skill script missing: {candidates[0]}")


def run_script(path: Path, args: Iterable[str]) -> subprocess.CompletedProcess[str]:
    """Run a vendored script, capturing output for the ingest report.

    Never raises on a non-zero exit — the no-loss gates in those scripts signal
    "I refused to write anything" that way, which is a result to report per file,
    not a reason to abandon a sixteen-file run.
    """
    return subprocess.run(
        [sys.executable, str(path), *[str(a) for a in args]],
        capture_output=True,
        text=True,
        check=False,
    )


# ---------------------------------------------------------------------------
# The chain
# ---------------------------------------------------------------------------


@dataclass
class PrepareResult:
    """What happened to one commentary, step by step."""

    name: str
    source: Path
    final: Path | None = None
    steps: list[tuple[str, str]] = field(default_factory=list)  # (step, one-line result)
    notes: list[str] = field(default_factory=list)
    failure: str = ""
    headings: int = 0
    anchors: int = 0
    stamped: int = 0

    @property
    def ok(self) -> bool:
        return not self.failure and self.final is not None

    def format_lines(self) -> list[str]:
        lines = [f"{step:<12s} {detail}" for step, detail in self.steps]
        lines += [f"{'note':<12s} {note}" for note in self.notes[:4]]
        if len(self.notes) > 4:
            lines.append(f"{'note':<12s} … {len(self.notes) - 4} more (see the report)")
        if self.failure:
            lines.append(f"{'FAILED':<12s} {self.failure}")
        return lines

    def promote(self) -> None:
        """Copy the finished file over the corpus source, keeping one backup.

        ``source/`` is meant to be immutable after ingest (CLAUDE.md). Re-running
        ingest *is* the exception that rule allows for, but only once the file
        has survived every check — and the previous state is kept so the change
        is reversible without a git operation.

        The backup goes in ``work/``, not beside the source: ``source/`` holds
        source and nothing else, and a stray copy there is one careless glob away
        from being ingested as a seventeenth commentary.
        """
        if self.final is None:
            raise RuntimeError(f"{self.name}: nothing to promote")
        backup = self.final.with_name(f"{self.name}.pre-toc.md")
        if not backup.exists():
            backup.write_text(self.source.read_text(encoding="utf-8"), encoding="utf-8")
        self.source.write_text(self.final.read_text(encoding="utf-8"), encoding="utf-8")


def prepare_file(
    path: Path,
    *,
    root: Path,
    work_dir: Path,
    toc: tuple[Callable[..., Any], Callable[..., str]] | None,
    refine: bool = True,
) -> PrepareResult:
    """Run the whole chain over one commentary, into ``work_dir``.

    Steps run in this order for a reason:

    ``refine``     splits the over-cap blocks stage 1 could not, so the headings
                   land between blocks rather than inside one.
    ``toc``        inserts the sa-bcad headings.  Before transclusion, because
                   the anchors are placed relative to the *quotation* and a
                   heading inserted afterwards would land between an anchor and
                   the stanza it points at.
    ``transclude`` Stage 1 of the vendored skill only.  Stages 2 and 3 exist to
                   make the sa-bcad outline read correctly in Obsidian, and they
                   work by deleting the blank line above an anchor — which fuses
                   the anchor into the preceding prose block.  Here a block is
                   the unit a citation names, so that fusion is exactly what must
                   not happen.
    ``blockids``   last, over the final block structure, so no ID is stranded in
                   the middle of a block by a later insertion.

    Every step writes a numbered intermediate and every step is checked against
    the reading-view invariant before the next one runs.
    """
    result = PrepareResult(name=path.stem, source=path)
    original = path.read_text(encoding="utf-8")
    # The no-loss rule the vendored scripts enforce on themselves: text minus
    # whitespace.  Line breaking is not part of the text — stage-2 refinement
    # re-breaks it by design, and inserting a heading or an anchor adds lines —
    # so the invariant is over the *characters*, with the scaffolding taken back
    # off first.  Anything stronger fails on a legitimate step; anything weaker
    # would let a step quietly edit Tibetan.
    baseline = collapse(reading_view(original))
    current = original
    stem = path.stem

    def checkpoint(step: str, text: str) -> bool:
        if collapse(reading_view(text)) != baseline:
            result.failure = f"{step} changed the text, not just the scaffolding — nothing written"
            return False
        return True

    # -- stage-2 refinement -------------------------------------------------
    if refine:
        raw = work_dir / f"{stem}.0-input.md"
        refined = work_dir / f"{stem}.1-refined.md"
        raw.write_text(current, encoding="utf-8")
        proc = run_script(
            skill_script("commentary-segmentation", "stage2_refine.py"),
            [raw, refined, "--max-syllables", 40, "--source", raw,
             "--report", work_dir / f"{stem}.1-refined.tsv"],
        )
        if proc.returncode != 0 or not refined.exists():
            result.steps.append(("refine", f"declined ({_first_error(proc)}) — kept stage-1 blocks"))
        else:
            candidate = refined.read_text(encoding="utf-8")
            before = len(parse_blocks(current))
            after = len(parse_blocks(candidate))
            current = candidate
            result.steps.append(("refine", f"{before} → {after} blocks"))
            if not checkpoint("refine", current):
                return result

    # -- sa-bcad headings ---------------------------------------------------
    if toc is not None:
        generate, prompt_render = toc
        annotation_path = work_dir / f"{stem}.2-toc.annotation.json"
        tagged = work_dir / f"{stem}.2-toc.md"
        staged = work_dir / f"{stem}.2-toc.input.md"
        staged.write_text(current, encoding="utf-8")
        try:
            annotation, notes = build_toc_annotation(stem, current, generate, prompt_render)
        except Exception as exc:  # noqa: BLE001 - a model failure is one file's problem
            result.steps.append(("toc", f"model call failed: {type(exc).__name__}: {exc}"))
            annotation, notes = {"sections": []}, []
        result.notes.extend(notes)

        if annotation["sections"]:
            annotation_path.write_text(
                json.dumps(annotation, ensure_ascii=False, indent=1), encoding="utf-8"
            )
            proc = run_script(
                skill_script("tag-inline-toc", "tag_inline_toc.py"),
                ["render", "--input", staged, "--annot", annotation_path, "--output", tagged],
            )
            if proc.returncode != 0 or not tagged.exists():
                result.steps.append(("toc", f"renderer refused: {_first_error(proc)}"))
            else:
                current = tagged.read_text(encoding="utf-8")
                result.headings = len(annotation["sections"])
                result.steps.append(
                    (
                        "toc",
                        f"{result.headings} headings, max depth "
                        f"{max(s['depth'] for s in annotation['sections'])}",
                    )
                )
                if not checkpoint("toc", current):
                    return result
        elif not result.steps or result.steps[-1][0] != "toc":
            result.steps.append(("toc", "no sa-bcad sections found"))

    # -- transclusion anchors ----------------------------------------------
    anchored = work_dir / f"{stem}.3-anchored.md"
    anchored.write_text(current, encoding="utf-8")
    proc = run_script(
        skill_script("Transclusion-rootext-into-commentaries", "01_transclude_verses.py"),
        [
            "--root", root,
            "--commentary", anchored,
            "--link-base", root.stem,
            # A བསྟོད་འགྲེལ cites its verse by the opening pada inside a ཞེས frame far
            # more often than it quotes the whole stanza; without --incipit six of
            # these sixteen commentaries anchor nothing at all.  --in-order refuses
            # a placement above the previous verse's, which is free precision.
            "--incipit",
            "--in-order",
            "--apply",
        ],
    )
    (work_dir / f"{stem}.3-anchored.log").write_text(
        proc.stdout + proc.stderr, encoding="utf-8"
    )
    if proc.returncode != 0:
        result.steps.append(("transclude", f"failed: {_first_error(proc)}"))
    else:
        current = anchored.read_text(encoding="utf-8")
        placed, unplaced = _placement_counts(proc.stdout)
        result.anchors = placed
        result.steps.append(("transclude", f"{placed} verses anchored, {unplaced} unplaced"))
        if not checkpoint("transclude", current):
            return result

    # -- block IDs ----------------------------------------------------------
    final = work_dir / f"{stem}.4-final.md"
    current, stamp = stamp_block_ids(current)
    result.stamped = stamp.stamped
    result.steps.append(("blockids", stamp.format_summary()))
    result.notes.extend(f"untagged heading: {h}" for h in stamp.untagged_headings)
    if not checkpoint("blockids", current):
        return result

    final.write_text(current, encoding="utf-8")
    result.final = final
    return result


def _first_error(proc: subprocess.CompletedProcess[str]) -> str:
    """The most informative single line of a failed subprocess run."""
    for stream in (proc.stderr, proc.stdout):
        for line in reversed((stream or "").strip().splitlines()):
            if line.strip():
                return line.strip()[:160]
    return f"exit {proc.returncode}"


_PLACEMENT_RE = re.compile(r"verses=(\d+)\s+placed=(\d+)\s+unplaced=(\d+)")


def _placement_counts(stdout: str) -> tuple[int, int]:
    match = _PLACEMENT_RE.search(stdout or "")
    return (int(match.group(2)), int(match.group(3))) if match else (0, 0)


def format_corpus_report(corpus: str, results: Sequence[PrepareResult], *, promoted: bool) -> str:
    """The artifact a human reads before trusting the run."""
    lines = [
        f"# Commentary preparation — {corpus}",
        "",
        f"{sum(1 for r in results if r.ok)} of {len(results)} files completed"
        + (" and were promoted over `source/commentaries/`." if promoted else "; nothing promoted."),
        "",
        "| commentary | headings | anchors | block IDs | status |",
        "|---|---:|---:|---:|---|",
    ]
    for r in results:
        status = "ok" if r.ok else f"**FAILED** — {r.failure or 'incomplete'}"
        lines.append(f"| `{r.name}` | {r.headings} | {r.anchors} | {r.stamped} | {status} |")

    flagged = [r for r in results if r.notes]
    if flagged:
        lines += ["", "## Wants a human", ""]
        for r in flagged:
            lines.append(f"### `{r.name}`")
            lines += [f"- {note}" for note in r.notes]
            lines.append("")

    lines += [
        "## Per-file steps",
        "",
    ]
    for r in results:
        lines.append(f"### `{r.name}`")
        lines += [f"- **{step}** — {detail}" for step, detail in r.steps]
        lines.append("")
    return "\n".join(lines)


def load_annotation(path: Path) -> dict[str, Any]:
    """Read a ``tag-inline-toc`` Phase-1 annotation, with a shape check.

    The renderer's error messages are good, but they arrive after it has read a
    megabyte of commentary; a malformed annotation is worth catching here.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    sections = data.get("sections")
    if not isinstance(sections, list):
        raise ValueError(f"{path}: annotation has no 'sections' list")
    for i, section in enumerate(sections):
        missing = [k for k in ("depth", "heading_title", "body_start_context") if not section.get(k)]
        if missing:
            raise ValueError(f"{path}: section {i} is missing {', '.join(missing)}")
    return data
