"""The update path — merge new cited material into an existing bo.wikipedia article.

520 of the 545 སྤྱོད་འཇུག terms already have an article, so *this* is the majority case,
not creation. The forum spec's stage 4 has no published prompt (PLAN.md §4), which makes the
division of labour here even more important than in the create path: the model **classifies**
each piece of new material against the existing article — ``duplicate`` / ``new`` /
``conflict`` — and points at a section anchor; this module does every string operation. The
model never rewrites the page. What it judges, code applies; what it cannot judge safely
(a conflict), nobody applies — it is flagged ⚑ for the human, both readings preserved
(the Railroad divergence rule, open-questions.md Q10).

Three properties are load-bearing:

**Existing text is never modified.** An applied operation only *inserts* — a ``<ref>`` after
a sentence that already says the same thing, or a new cited paragraph at the end of an
existing section. Anything else is a diff a reviewer cannot trust.

**Sections are addressed by anchor, never by string-matching headings** (PLAN.md §4).
Tibetan headings differ by a shad or tsheg between two renderings of the same section;
:func:`section_anchor` normalises exactly the way MediaWiki does (whitespace → underscore)
and lookup additionally tolerates the terminal tsheg/shad the way ``registry.term_key`` does.
A ``new`` operation may not target a section that does not exist — never invent a section
(wikitext-spec.md §1) — nor the fixed tail sections, whose content the spec owns.

**An operation that cannot be applied exactly is skipped and reported, never repaired.**
A ``duplicate`` whose ``existing_text`` is not found verbatim in the target section is
dropped with a reason. Guessing at "what the model probably meant" is how a citation ends
up attached to the wrong sentence — well-formed and wrong, the failure mode this whole
pipeline exists to prevent.

Verification of a merged article is a *documented subset* of the create-path gate
(:func:`verify_merged`): the full rule set assumes we wrote the whole page, and an existing
article written by human editors legitimately fails house rules (V2: their refs are not in
our citation inventory; V7: their categories are off-allowlist; V11: their section order).
Blocking a legitimate update on the pre-existing state of the page would make the majority
case unusable. What stays blocking is what the merge itself could have broken or introduced:
every **new** quotation character-for-character in its source (V1), reference display
integrity (V3/V4/V5). Everything else is surfaced as advisory findings in the report.
"""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Sequence

from ..tibetan.normalize import nfc
from ..tibetan.verify import check_quote
from .validator import Finding, validate
from .wikitext import Citation, render_ref

__all__ = [
    "BLOCKING_RULES",
    "TERMINAL_SECTION_HEADINGS",
    "MergeError",
    "MergeOperation",
    "MergeResult",
    "WikiSection",
    "apply_operations",
    "ensure_references_section",
    "find_section",
    "parse_operations",
    "parse_sections",
    "section_anchor",
    "unified_diff",
    "verify_merged",
]

#: The fixed tail of every article (wikitext-spec.md §1 rule: "the last three sections are
#: fixed and ordered"). A ``new`` operation may not insert prose into them.
TERMINAL_SECTION_HEADINGS = ("འབྲེལ་ཡོད་ཤོག་ངོས།", "ལུང་ཁུངས།", "དཔྱད་གཞིའི་ཡིག་ཆ།")

#: Rules whose *errors* block a merged article. See the module docstring for why this is a
#: subset of the create-path gate.
BLOCKING_RULES = frozenset({"V1", "V3", "V4", "V5"})

_HEADING_RE = re.compile(r"^(={2,6})\s*(.*?)\s*\1\s*$", re.MULTILINE)
_CATEGORY_LINE_RE = re.compile(r"^\[\[རིགས་དབྱེ།:", re.MULTILINE)
_REF_AFTER_RE = re.compile(r"\s*<ref(?:\s[^>]*)?(?:/>|>.*?</ref>)", re.DOTALL)
_REF_ANY_RE = re.compile(r"<ref[\s>]", re.IGNORECASE)
_REFERENCES_TAG_RE = re.compile(r"<references\s*/?>", re.IGNORECASE)

#: Punctuation that may end a heading or anchor without changing its identity — the same
#: set ``registry.term_key`` strips, for the same reason.
_TERMINAL_PUNCT = "་༌།༎"

_VALID_KINDS = ("duplicate", "new", "conflict")


class MergeError(ValueError):
    """The model's operations payload is structurally unusable."""


# --------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class WikiSection:
    """One ``== heading ==`` of the existing article, with its text span.

    ``start`` is the offset of the heading line; ``body_start`` the offset just past it;
    ``end`` where the section's content stops (the next heading of the same or shallower
    level, or end of text). Offsets index the NFC-normalised wikitext that
    :func:`parse_sections` was given — every downstream operation works on that string.
    """

    heading: str
    anchor: str
    level: int
    start: int
    body_start: int
    end: int


def section_anchor(heading: str) -> str:
    """The MediaWiki-style anchor of a heading: markup stripped, whitespace → ``_``.

    This is deliberately the *matching* form, not the percent-encoded URL form — both
    sides of a comparison go through this function, so encoding would only add a way for
    two spellings of the same anchor to miss each other.
    """
    text = nfc(heading)
    text = re.sub(r"'''|''", "", text)
    text = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", text)
    text = " ".join(text.split())
    return text.replace(" ", "_")


def _anchor_key(anchor: str) -> str:
    """Anchor identity tolerant of the terminal tsheg/shad, like ``term_key``."""
    text = nfc(anchor).strip().replace("_", " ").strip()
    while text and text[-1] in _TERMINAL_PUNCT:
        text = text[:-1].rstrip()
    return text.replace(" ", "_")


def parse_sections(wikitext: str) -> list[WikiSection]:
    """Every heading of the article, in order, with its content span.

    The lead (text before the first heading) is not a section here — operations address
    it with an empty anchor, and :func:`apply_operations` handles that case directly.
    """
    text = nfc(wikitext)
    headings = [
        (match.start(), match.end(), len(match.group(1)), match.group(2))
        for match in _HEADING_RE.finditer(text)
    ]
    sections: list[WikiSection] = []
    for index, (start, heading_end, level, heading_text) in enumerate(headings):
        end = len(text)
        for later_start, _, later_level, _ in headings[index + 1 :]:
            if later_level <= level:
                end = later_start
                break
        sections.append(
            WikiSection(
                heading=heading_text,
                anchor=section_anchor(heading_text),
                level=level,
                start=start,
                body_start=heading_end,
                end=end,
            )
        )
    return sections


def find_section(sections: Sequence[WikiSection], anchor: str) -> WikiSection | None:
    """Look up a section by anchor — exact first, then tsheg/shad-tolerant.

    Tolerant matching exists because the page may write ``མཚན་ཉིད།`` where the model's
    anchor says ``མཚན་ཉིད`` (or vice versa); those are one section. Interior differences
    are never bridged — a tolerant hit on the wrong section is worse than a miss.
    """
    wanted = section_anchor(anchor.replace("_", " "))
    for section in sections:
        if section.anchor == wanted:
            return section
    wanted_key = _anchor_key(wanted)
    if not wanted_key:
        return None
    for section in sections:
        if _anchor_key(section.anchor) == wanted_key:
            return section
    return None


def _is_terminal_heading(heading: str) -> bool:
    key = _anchor_key(section_anchor(heading))
    return any(key == _anchor_key(section_anchor(t)) for t in TERMINAL_SECTION_HEADINGS)


# --------------------------------------------------------------------------
# Operations
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class MergeOperation:
    """One classified change, exactly as the update prompt's schema defines it."""

    kind: str  # 'duplicate' | 'new' | 'conflict'
    section_anchor: str = ""
    existing_text: str = ""
    new_text: str = ""
    citation: Citation | None = None
    rationale: str = ""

    def describe(self) -> str:
        target = self.section_anchor or "(lead)"
        if self.kind == "duplicate":
            return f"duplicate in {target}: …{self.existing_text[:40]}"
        if self.kind == "new":
            return f"new in {target}: {self.new_text[:40]}…"
        return f"conflict in {target}: {self.rationale[:60]}"


def parse_operations(
    data: Mapping[str, Any],
    *,
    citation_builder: Callable[[Mapping[str, Any]], Citation | None],
) -> tuple[list[MergeOperation], list[str]]:
    """Turn the model's JSON into typed operations, rejecting what cannot be used.

    ``citation_builder`` maps the payload's ``{source_id, quote, page}`` to a full
    :class:`Citation` — the URL and author come from the registry, never from the model
    (the ``dummy.com`` rule). A rejected operation becomes a message, not an exception:
    one malformed entry must not throw away the model's other judgements.
    """
    operations: list[MergeOperation] = []
    problems: list[str] = []
    raw_ops = data.get("operations")
    if not isinstance(raw_ops, Sequence) or isinstance(raw_ops, (str, bytes)):
        raise MergeError("operations payload is not a list")

    for index, raw in enumerate(raw_ops):
        if not isinstance(raw, Mapping):
            problems.append(f"op[{index}]: not an object, dropped")
            continue
        kind = str(raw.get("kind") or "").strip().lower()
        if kind not in _VALID_KINDS:
            problems.append(f"op[{index}]: unknown kind {raw.get('kind')!r}, dropped")
            continue

        citation: Citation | None = None
        raw_citation = raw.get("citation")
        if isinstance(raw_citation, Mapping):
            citation = citation_builder(raw_citation)
            if citation is None:
                problems.append(
                    f"op[{index}] ({kind}): citation source "
                    f"{raw_citation.get('source_id')!r} not in the registry, dropped"
                )
                continue

        operation = MergeOperation(
            kind=kind,
            section_anchor=str(raw.get("section_anchor") or "").strip(),
            existing_text=nfc(str(raw.get("existing_text") or "")).strip(),
            new_text=nfc(str(raw.get("new_text") or "")).strip(),
            citation=citation,
            rationale=nfc(str(raw.get("rationale") or "")).strip(),
        )

        if kind == "duplicate" and not operation.existing_text:
            problems.append(f"op[{index}]: duplicate with no existing_text, dropped")
            continue
        if kind == "duplicate" and citation is None:
            problems.append(f"op[{index}]: duplicate with no citation, dropped")
            continue
        if kind == "new" and not operation.new_text:
            problems.append(f"op[{index}]: new with no new_text, dropped")
            continue
        if kind == "new" and citation is None:
            # An uncited addition is exactly what this pipeline must never make.
            problems.append(f"op[{index}]: new with no citation, dropped")
            continue
        operations.append(operation)
    return operations, problems


# --------------------------------------------------------------------------
# Applying
# --------------------------------------------------------------------------


@dataclass
class MergeResult:
    """What happened when the operations met the page."""

    merged: str
    applied: list[MergeOperation] = field(default_factory=list)
    skipped: list[tuple[MergeOperation, str]] = field(default_factory=list)
    conflicts: list[MergeOperation] = field(default_factory=list)
    new_citations: list[Citation] = field(default_factory=list)
    repairs: list[str] = field(default_factory=list)
    parse_problems: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.applied or self.repairs)

    def format_report(self, original: str) -> str:
        lines = ["# Update merge report", ""]
        lines.append(
            f"{len(self.applied)} applied · {len(self.skipped)} skipped · "
            f"{len(self.conflicts)} conflicts for human review"
        )
        lines.append("")
        if self.conflicts:
            lines += ["## ⚑ Conflicts — decide these yourself", ""]
            for op in self.conflicts:
                lines.append(f"- ⚑ **{op.section_anchor or '(lead)'}**: {op.rationale or 'no rationale given'}")
                if op.existing_text:
                    lines.append(f"  - existing: {op.existing_text}")
                if op.new_text:
                    lines.append(f"  - new: {op.new_text}")
                if op.citation is not None and op.citation.quote:
                    lines.append(f"  - source {op.citation.source_id}: {op.citation.quote}")
            lines.append("")
        if self.applied:
            lines += ["## Applied", ""]
            lines += [f"- {op.describe()}" for op in self.applied] + [""]
        if self.repairs:
            lines += ["## Structural repairs", ""]
            lines += [f"- {r}" for r in self.repairs] + [""]
        if self.skipped:
            lines += ["## Skipped — not applied, look at why", ""]
            lines += [f"- {op.describe()} — {reason}" for op, reason in self.skipped] + [""]
        if self.parse_problems:
            lines += ["## Dropped at parse time", ""]
            lines += [f"- {p}" for p in self.parse_problems] + [""]
        lines += ["## Diff", "", "```diff", unified_diff(original, self.merged), "```", ""]
        return "\n".join(lines)


def unified_diff(old: str, new: str) -> str:
    """The reviewable artifact: what the update would actually change."""
    return "".join(
        difflib.unified_diff(
            old.splitlines(keepends=True),
            new.splitlines(keepends=True),
            fromfile="existing",
            tofile="merged",
        )
    ).rstrip("\n")


def _insertion_point_after(text: str, match_end: int) -> int:
    """Where a new ref goes: after the matched sentence *and* its existing refs.

    ``…sentence<ref>a</ref><ref>b</ref>`` + our ref must yield ``…<ref>b</ref><ref>new</ref>``,
    not a ref wedged between the sentence and its first footnote.
    """
    position = match_end
    while True:
        match = _REF_AFTER_RE.match(text, position)
        if match is None:
            return position
        position = match.end()


def apply_operations(
    wikitext: str, operations: Sequence[MergeOperation]
) -> MergeResult:
    """Apply classified operations to the page. Insert-only; skip on any doubt."""
    text = nfc(wikitext)
    result = MergeResult(merged=text)

    for op in operations:
        if op.kind == "conflict":
            result.conflicts.append(op)
            continue

        sections = parse_sections(result.merged)
        if op.section_anchor:
            section = find_section(sections, op.section_anchor)
        else:
            section = None  # the lead

        if op.kind == "new":
            if op.section_anchor and section is None:
                result.skipped.append(
                    (op, f"section {op.section_anchor!r} does not exist — never invent a section")
                )
                continue
            if section is not None and _is_terminal_heading(section.heading):
                result.skipped.append(
                    (op, f"{section.heading!r} is a fixed tail section; prose may not be added there")
                )
                continue
            assert op.citation is not None  # parse_operations guarantees it
            paragraph = f"{op.new_text}{render_ref(op.citation)}"
            if section is not None:
                insert_at = section.end
                body = result.merged[section.body_start : section.end]
            else:
                first_heading = sections[0].start if sections else len(result.merged)
                insert_at = first_heading
                body = result.merged[:first_heading]
            chunk = paragraph + "\n\n" if body.endswith("\n\n") else (
                "\n" + paragraph + "\n" if body.endswith("\n") else "\n\n" + paragraph + "\n"
            )
            result.merged = result.merged[:insert_at] + chunk + result.merged[insert_at:]
            result.applied.append(op)
            result.new_citations.append(op.citation)
            continue

        # duplicate — attach a corroborating ref to a sentence that already says it.
        if op.section_anchor and section is None:
            result.skipped.append((op, f"section {op.section_anchor!r} does not exist"))
            continue
        lo = section.body_start if section is not None else 0
        hi = section.end if section is not None else len(result.merged)
        found = result.merged.find(op.existing_text, lo, hi)
        if found < 0:
            # Widen to the whole page once: the model may have mis-filed the anchor while
            # copying the sentence correctly, and the sentence is the stronger signal.
            found = result.merged.find(op.existing_text)
            if found < 0:
                result.skipped.append(
                    (op, "existing_text not found verbatim on the page — not repaired, by design")
                )
                continue
        assert op.citation is not None
        ref = render_ref(op.citation)
        insert_at = _insertion_point_after(result.merged, found + len(op.existing_text))
        already_there = result.merged[found : insert_at + len(ref)]
        if ref in already_there:
            result.skipped.append((op, "this exact ref is already attached to that sentence"))
            continue
        result.merged = result.merged[:insert_at] + ref + result.merged[insert_at:]
        result.applied.append(op)
        result.new_citations.append(op.citation)

    result.merged = ensure_references_section(result.merged, result.repairs)
    return result


def ensure_references_section(wikitext: str, repairs: list[str] | None = None) -> str:
    """Add ``== ལུང་ཁུངས། ==`` + ``<references />`` when refs exist with no display.

    About 600 live bo.wikipedia articles have orphaned footnotes (PLAN.md §1 finding 4).
    When the update path touches one, leaving it broken would put our new citation among
    the invisible; the deterministic fix is one heading and one tag, inserted before the
    category lines. Recorded as a repair so the reviewer sees it in the diff *and* the
    report.
    """
    text = nfc(wikitext)
    if not _REF_ANY_RE.search(text) or _REFERENCES_TAG_RE.search(text):
        return text
    block = "== ལུང་ཁུངས། ==\n<references />\n"
    category = _CATEGORY_LINE_RE.search(text)
    if category is not None:
        insert_at = category.start()
        prefix = text[:insert_at]
        if not prefix.endswith("\n\n"):
            block = block if prefix.endswith("\n") else "\n" + block
        text = text[:insert_at] + block + "\n" + text[insert_at:]
    else:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n" + block
    if repairs is not None:
        repairs.append(
            "page had <ref> tags but no <references /> display; added == ལུང་ཁུངས། == + <references />"
        )
    return text


# --------------------------------------------------------------------------
# Verifying
# --------------------------------------------------------------------------


@dataclass
class MergeVerification:
    """The gate's verdict on a merged article. Blocking subset — see module docstring."""

    findings: list[Finding] = field(default_factory=list)
    quote_failures: list[str] = field(default_factory=list)
    advisory: list[Finding] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        blocking = any(
            f.severity == "error" and f.rule in BLOCKING_RULES for f in self.findings
        )
        return not blocking and not self.quote_failures

    def format_report(self) -> str:
        lines = ["# Merged-article verification", ""]
        lines.append("**PASS**" if self.passed else "**FAIL**")
        lines.append("")
        if self.quote_failures:
            lines += ["## New quotations not found in source", ""]
            lines += [f"- {q}" for q in self.quote_failures] + [""]
        blocking = [
            f for f in self.findings if f.severity == "error" and f.rule in BLOCKING_RULES
        ]
        if blocking:
            lines += ["## Blocking", ""] + [f"- `{f.rule}` {f.message}" for f in blocking] + [""]
        if self.advisory:
            lines += [
                "## Advisory — pre-existing page state, not blocked",
                "",
                "These would block a *created* article. On an update they describe the page "
                "as the community wrote it; fix them only deliberately.",
                "",
            ]
            lines += [f"- `{f.rule}` {f.message}" for f in self.advisory] + [""]
        return "\n".join(lines)


def verify_merged(
    merged: str,
    new_citations: Sequence[Citation],
    allowed_categories: Sequence[str],
    source_loader: Callable[[str], str] | None,
) -> MergeVerification:
    """Verify a merged article: full quote gate on new citations, structural rules on the page.

    Runs the whole validator so nothing is silently unchecked, then splits findings into
    blocking (:data:`BLOCKING_RULES`) and advisory. The quotation check does not rely on
    the validator's V1 alone — it re-reads every new quotation from its claimed source file
    exactly the way the create path's stage 7 does, because that check is the paper's
    central mechanism and this module must not weaken it.
    """
    verification = MergeVerification()
    findings = validate(
        merged,
        citations=list(new_citations),
        allowed_categories=list(allowed_categories),
        source_loader=source_loader,
    )
    for finding in findings:
        if finding.severity == "error" and finding.rule not in BLOCKING_RULES:
            verification.advisory.append(finding)
        else:
            verification.findings.append(finding)

    if source_loader is not None:
        cache: dict[str, str] = {}
        for citation in new_citations:
            if not citation.quote:
                continue
            if citation.source_id not in cache:
                try:
                    cache[citation.source_id] = source_loader(citation.source_id)
                except Exception as exc:
                    verification.quote_failures.append(
                        f"{citation.source_id}: source unreadable ({exc})"
                    )
                    cache[citation.source_id] = ""
            check = check_quote(citation.quote, cache[citation.source_id], citation.source_id)
            if not check.passed:
                verification.quote_failures.append(
                    f"{citation.source_id}: [{check.method}] {citation.quote[:60]}…"
                )
    return verification
