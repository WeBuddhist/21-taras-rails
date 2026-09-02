"""The blocking wikitext lint gate (rules V1–V12 of ``wikitext-spec.md`` §7).

Why this is deterministic code and not a model call: it is the mechanism the
paper's central claim rests on.  "The pipeline does not publish an unverifiable
citation" is only worth saying if the check that enforces it cannot itself
hallucinate.  Every rule here is decidable from the text plus the citation
records, and every rule is a ``FAIL`` that stops a publish.

The empirical case for each rule is in ``research/reports/r-bo-wiki-conventions.md``:
of 677 sampled bo.wikipedia articles, 15% are raw model dumps with no markup at
all, 75% have no citations, 80% have no categories, and ~126 carry ``<ref>``
tags with nothing to display them.  These are not hypothetical failure modes.

Import cost is stdlib only, so the gate runs with no API key and no network.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Literal, Sequence

from kangyur_wiki.wiki.wikitext import (
    CATEGORY_RE,
    HEADING_RE,
    HTML_TAG_RE,
    REFERENCES_TAG_RE,
    REF_BLOCK_RE,
    REF_TAG_RE,
    REFLIST_RE,
    SINGULAR_REFERENCE_TAG_RE,
    TAIL_HEADINGS,
    TEMPLATE_RE,
    WIKILINK_RE,
    Citation,
    HEADING_REFERENCES,
    TSHEG,
    ref_name,
    render_ref_body,
    syllable_count,
)

__all__ = [
    "Finding",
    "Severity",
    "SourceLoader",
    "SEED_CATEGORIES",
    "MIN_ARTICLE_SYLLABLES",
    "RULE_TITLES",
    "validate",
    "format_report",
    "has_errors",
]

Severity = Literal["error", "warning"]

#: ``source_id -> source text``.  Returns ``None`` when the id is not declared
#: in ``sources.yaml``, which is itself a V2 failure.
SourceLoader = Callable[[str], "str | None"]

#: wikitext-spec.md §5.  Curated because the live category namespace contains
#: misspellings (``ནང་པ་སངས་རྒྱངས་ཀྱི་ལྷ།``) and shad typos (``ནང་པ་སངས་རྒྱས།།``)
#: that a model will happily imitate.
SEED_CATEGORIES = frozenset(
    {
        "ནང་ཆོས།",
        "ནང་བསྟན།",
        "ནང་པ་སངས་རྒྱས་ཆོས་ལུགས།",
        "བསྟན་བཅོས།",
        "ཤེར་ཕྱིན།",
        "ཆོས་ལུགས།",
    }
)

#: wikitext-spec.md §7, warnings: an article below this length is a stub in
#: substance whatever its markup says.
MIN_ARTICLE_SYLLABLES = 1500

RULE_TITLES: dict[str, str] = {
    "V1": "quotations verbatim in the cited source",
    "V2": "every <ref> resolves to a declared source",
    "V3": "<references /> present iff <ref> present",
    "V4": "no {{Reflist}} preceded by a heading",
    "V5": "<ref> tags balanced; named refs defined once",
    "V6": "at least one == heading ==",
    "V7": "at least one category, all allowlisted",
    "V8": "every section carries a citation",
    "V9": "Tibetan script only outside refs and templates",
    "V10": "tsheg survives every ''' and [[ boundary",
    "V11": "the three tail sections, in order",
    "V12": "no placeholders or leftover model chatter",
    "W1": "ref missing year or page",
    "W2": "unlinked ref",
    "W3": "section with only one citation",
    "W4": "article shorter than the stub threshold",
}


@dataclass(frozen=True)
class Finding:
    """One rule result.

    ``line`` is 1-based and refers to the NFC-normalised text with ``\\r\\n``
    folded to ``\\n`` — the same normalisation the publisher applies — so line
    numbers stay usable after a round trip through the wiki.
    """

    rule: str
    severity: Severity
    message: str
    line: int | None = None


# --------------------------------------------------------------------------
# Internal document model
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class _Heading:
    level: int
    text: str
    line: int
    start: int
    end: int


@dataclass(frozen=True)
class _RefTag:
    kind: str  # "open" | "close" | "self"
    name: str
    start: int
    end: int
    line: int


@dataclass(frozen=True)
class _RefDefinition:
    name: str
    body: str
    line: int


class _Document:
    """One parse of the wikitext, shared by every rule.

    Built once because several rules need the same three views of the text —
    the heading index, the ref-tag stream, and the "prose only" masked copy —
    and re-deriving them per rule is how two rules end up disagreeing about
    what a section is.
    """

    def __init__(self, wikitext: str) -> None:
        self.text = unicodedata.normalize("NFC", wikitext).replace("\r\n", "\n").replace(
            "\r", "\n"
        )
        self.headings = _parse_headings(self.text)
        self.ref_tags = _parse_ref_tags(self.text)
        self.definitions, self.structural_findings = _pair_ref_tags(self.text, self.ref_tags)
        self.masked = _mask_markup(self.text)

    def line_of(self, offset: int) -> int:
        return self.text.count("\n", 0, offset) + 1

    @property
    def has_refs(self) -> bool:
        return bool(self.ref_tags)

    def section_span(self, index: int) -> tuple[int, int]:
        """Content span of ``self.headings[index]``, subsections included.

        A ``==`` section owns its ``===`` subsections, which is what MediaWiki
        means by a section.  Ending the span at the next heading of *any* level
        would report a parent as uncited whenever its citations sit one level
        down.
        """
        heading = self.headings[index]
        for candidate in self.headings[index + 1 :]:
            if candidate.level <= heading.level:
                return heading.end, candidate.start
        return heading.end, len(self.text)


def _parse_headings(text: str) -> list[_Heading]:
    headings: list[_Heading] = []
    for match in HEADING_RE.finditer(text):
        marks = match.group(1)
        headings.append(
            _Heading(
                level=len(marks),
                text=unicodedata.normalize("NFC", match.group(2)).strip(),
                line=text.count("\n", 0, match.start()) + 1,
                start=match.start(),
                end=match.end(),
            )
        )
    return headings


def _parse_ref_tags(text: str) -> list[_RefTag]:
    tags: list[_RefTag] = []
    for match in REF_TAG_RE.finditer(text):
        if match.group("close"):
            kind = "close"
        elif match.group("selfclose"):
            kind = "self"
        else:
            kind = "open"
        tags.append(
            _RefTag(
                kind=kind,
                name=ref_name(match.group("attrs")),
                start=match.start(),
                end=match.end(),
                line=text.count("\n", 0, match.start()) + 1,
            )
        )
    return tags


def _pair_ref_tags(
    text: str, tags: Sequence[_RefTag]
) -> tuple[list[_RefDefinition], list[Finding]]:
    """Match ``<ref>`` openings to closings; report V5 structural failures.

    MediaWiki does not nest refs, so an opening tag seen while another is still
    open is an unclosed ref, not a nested one.
    """
    definitions: list[_RefDefinition] = []
    findings: list[Finding] = []
    pending: _RefTag | None = None

    for tag in tags:
        if tag.kind == "close":
            if pending is None:
                findings.append(
                    Finding(
                        "V5",
                        "error",
                        "stray </ref> with no matching opening tag",
                        tag.line,
                    )
                )
                continue
            body = text[pending.end : tag.start].strip()
            if not body:
                findings.append(
                    Finding(
                        "V5",
                        "error",
                        "empty <ref></ref> — an empty footnote is a cite error",
                        pending.line,
                    )
                )
            definitions.append(_RefDefinition(pending.name, body, pending.line))
            pending = None
        elif tag.kind == "self":
            if not tag.name:
                findings.append(
                    Finding(
                        "V5",
                        "error",
                        "self-closing <ref /> without a name displays nothing",
                        tag.line,
                    )
                )
        else:
            if pending is not None:
                findings.append(
                    Finding(
                        "V5",
                        "error",
                        f"<ref> opened on line {pending.line} was never closed",
                        pending.line,
                    )
                )
            pending = tag

    if pending is not None:
        findings.append(
            Finding("V5", "error", "<ref> is never closed", pending.line)
        )
    return definitions, findings


def _blank_out(match: "re.Match[str]") -> str:
    """Replace a span with spaces, keeping newlines so line numbers survive."""
    return "".join("\n" if char == "\n" else " " for char in match.group(0))


def _mask_markup(text: str) -> str:
    """Blank out everything that is legitimately not Tibetan prose.

    Order matters: ref blocks go first so that a template or a bare URL *inside*
    a ref is already gone by the time the later patterns run.
    """
    masked = text
    for pattern in (
        REF_BLOCK_RE,
        REF_TAG_RE,
        TEMPLATE_RE,
        CATEGORY_RE,
        HTML_TAG_RE,
    ):
        masked = pattern.sub(_blank_out, masked)
    return masked


def _normalize_ws(value: str) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split())


# --------------------------------------------------------------------------
# V1 — quotations verbatim
# --------------------------------------------------------------------------


def _load_check_quote() -> Callable[[str, str], Any] | None:
    """Import the quote checker, tolerating its absence.

    ``kangyur_wiki.tibetan.verify`` is a separate module with its own build
    order; the gate degrades to a warning rather than an ImportError so the
    other eleven rules still run.
    """
    try:
        from kangyur_wiki.tibetan.verify import check_quote
    except ImportError:
        return None
    return check_quote


def _rule_v1(
    citations: Sequence[Citation], source_loader: SourceLoader | None
) -> list[Finding]:
    quoted = [citation for citation in citations if citation.quote]
    if not quoted:
        return []
    if source_loader is None:
        return [
            Finding(
                "V1",
                "warning",
                f"skipped: no source_loader given, so {len(quoted)} quotation(s) "
                "were not checked against their sources",
            )
        ]
    check_quote = _load_check_quote()
    if check_quote is None:
        return [
            Finding(
                "V1",
                "warning",
                "skipped: kangyur_wiki.tibetan.verify.check_quote is not "
                f"available, so {len(quoted)} quotation(s) were not checked",
            )
        ]

    findings: list[Finding] = []
    for citation in quoted:
        try:
            source_text = source_loader(citation.source_id)
        except Exception as exc:  # foreign callable: never let it kill the gate
            findings.append(
                Finding(
                    "V1",
                    "error",
                    f"source {citation.source_id!r} could not be loaded: {exc}",
                )
            )
            continue
        if not source_text:
            findings.append(
                Finding(
                    "V1",
                    "error",
                    f"source {citation.source_id!r} is empty or undeclared, so "
                    "its quotation cannot be verified",
                )
            )
            continue
        try:
            result = check_quote(citation.quote, source_text)
        except Exception as exc:  # ditto
            findings.append(
                Finding(
                    "V1",
                    "error",
                    f"quote check for {citation.source_id!r} raised {exc!r}",
                )
            )
            continue
        found = getattr(result, "found", None)
        if found is None:
            findings.append(
                Finding(
                    "V1",
                    "warning",
                    f"check_quote returned {result!r} with no .found attribute; "
                    f"quotation from {citation.source_id!r} left unverified",
                )
            )
            continue
        if not found:
            method = getattr(result, "method", "unknown")
            findings.append(
                Finding(
                    "V1",
                    "error",
                    f"quotation not found verbatim in {citation.source_id!r} "
                    f"(method={method}): {_excerpt(citation.quote)}",
                )
            )
    return findings


def _excerpt(value: str, limit: int = 40) -> str:
    text = _normalize_ws(value)
    return text if len(text) <= limit else text[:limit] + "…"


# --------------------------------------------------------------------------
# V2 — every ref resolves to a declared source
# --------------------------------------------------------------------------


def _rule_v2(
    document: _Document,
    citations: Sequence[Citation],
    source_loader: SourceLoader | None,
) -> list[Finding]:
    findings: list[Finding] = []

    known_bodies: set[str] = set()
    for citation in citations:
        for anchor in (True, False):
            try:
                known_bodies.add(_normalize_ws(render_ref_body(citation, anchor=anchor)))
            except ValueError:
                continue

    for definition in document.definitions:
        if not definition.body:
            continue  # already reported by V5
        if _normalize_ws(definition.body) not in known_bodies:
            findings.append(
                Finding(
                    "V2",
                    "error",
                    "<ref> does not match any declared citation: "
                    f"{_excerpt(definition.body, 60)}",
                    definition.line,
                )
            )

    if source_loader is not None:
        for citation in citations:
            try:
                if source_loader(citation.source_id):
                    continue
            except Exception as exc:
                findings.append(
                    Finding(
                        "V2",
                        "error",
                        f"source {citation.source_id!r} could not be loaded: {exc}",
                    )
                )
                continue
            findings.append(
                Finding(
                    "V2",
                    "error",
                    f"source {citation.source_id!r} is not declared in sources.yaml",
                )
            )
    return findings


# --------------------------------------------------------------------------
# V3 / V4 — the reference display
# --------------------------------------------------------------------------


def _rule_v3(document: _Document) -> list[Finding]:
    findings: list[Finding] = []
    references_tags = list(REFERENCES_TAG_RE.finditer(document.text))
    reflists = list(REFLIST_RE.finditer(document.text))
    has_display = bool(references_tags) or bool(reflists)

    if document.has_refs and not has_display:
        findings.append(
            Finding(
                "V3",
                "error",
                "the article has <ref> tags but no <references /> — the "
                "footnotes render headless at the page bottom, which is the "
                "state ~600 bo.wikipedia articles are already in",
            )
        )
    if references_tags and not document.has_refs:
        findings.append(
            Finding(
                "V3",
                "error",
                "<references /> with no <ref> anywhere — an empty reference "
                "section",
                document.line_of(references_tags[0].start()),
            )
        )
    for match in SINGULAR_REFERENCE_TAG_RE.finditer(document.text):
        findings.append(
            Finding(
                "V3",
                "error",
                f"{match.group(0)!r} is not MediaWiki syntax and renders "
                "nothing; the tag is <references />",
                document.line_of(match.start()),
            )
        )
    return findings


def _rule_v4(document: _Document) -> list[Finding]:
    """The single most likely failure mode.

    ``== ལུང་ཁུངས། ==`` + ``{{Reflist}}`` is correct on English Wikipedia and
    broken here, because bo.wikipedia's Reflist opens with its own
    ``== ཡོང་ཁུངས། ==`` heading and the reader sees two stacked headings.
    Verified by live ``action=parse`` render on 2026-07-29.
    """
    findings: list[Finding] = []
    first_heading = document.headings[0].start if document.headings else None
    for match in REFLIST_RE.finditer(document.text):
        line = document.line_of(match.start())
        if first_heading is not None and first_heading < match.start():
            findings.append(
                Finding(
                    "V4",
                    "error",
                    "{{Reflist}} preceded by a heading — bo.wikipedia's Reflist "
                    "injects its own == ཡོང་ཁུངས། == heading, so this renders "
                    "two stacked headings; use <references /> instead",
                    line,
                )
            )
        else:
            findings.append(
                Finding(
                    "V4",
                    "warning",
                    "{{Reflist}} used instead of <references />; it carries its "
                    "own heading, so the article's reference heading is not "
                    "under our control",
                    line,
                )
            )
    return findings


# --------------------------------------------------------------------------
# V5 — named refs
# --------------------------------------------------------------------------


def _rule_v5(document: _Document) -> list[Finding]:
    findings = list(document.structural_findings)

    defined: dict[str, list[int]] = {}
    for definition in document.definitions:
        if definition.name and definition.body:
            defined.setdefault(definition.name, []).append(definition.line)
    for name, lines in defined.items():
        if len(lines) > 1:
            findings.append(
                Finding(
                    "V5",
                    "error",
                    f'ref name="{name}" is fully defined {len(lines)} times '
                    f"(lines {', '.join(str(line) for line in lines)}); only the "
                    "first use carries content",
                    lines[1],
                )
            )
    for tag in document.ref_tags:
        if tag.kind == "self" and tag.name and tag.name not in defined:
            findings.append(
                Finding(
                    "V5",
                    "error",
                    f'ref name="{tag.name}" is reused but never defined',
                    tag.line,
                )
            )
    return findings


# --------------------------------------------------------------------------
# V6 / V7 — headings and categories
# --------------------------------------------------------------------------


def _rule_v6(document: _Document) -> list[Finding]:
    if document.headings:
        return []
    return [
        Finding(
            "V6",
            "error",
            "no == heading == anywhere — 15% of sampled bo.wikipedia articles "
            "are unstructured model dumps and this is how they read",
        )
    ]


def _rule_v7(document: _Document, allowed_categories: Iterable[str]) -> list[Finding]:
    allowed = {
        unicodedata.normalize("NFC", name).strip()
        for name in allowed_categories
        if str(name).strip()
    }
    findings: list[Finding] = []
    found = list(CATEGORY_RE.finditer(document.text))
    if not found:
        return [
            Finding(
                "V7",
                "error",
                "no category — 80% of bo.wikipedia articles have none and are "
                "unreachable by browsing; at least one is required",
            )
        ]
    for match in found:
        name = unicodedata.normalize("NFC", match.group("name")).strip()
        if name not in allowed:
            findings.append(
                Finding(
                    "V7",
                    "error",
                    f"category {name!r} is not on the allowlist; the live "
                    "namespace contains misspellings and shad typos, so "
                    "categories are curated, never invented",
                    document.line_of(match.start()),
                )
            )
    return findings


# --------------------------------------------------------------------------
# V8 — no unsourced sections
# --------------------------------------------------------------------------


def _body_sections(document: _Document) -> list[tuple[int, _Heading, str]]:
    """Every section that carries article prose, i.e. not the fixed tail."""
    sections: list[tuple[int, _Heading, str]] = []
    for index, heading in enumerate(document.headings):
        if heading.text in TAIL_HEADINGS:
            continue
        start, end = document.section_span(index)
        sections.append((index, heading, document.text[start:end]))
    return sections


def _rule_v8(document: _Document) -> list[Finding]:
    findings: list[Finding] = []
    for _, heading, body in _body_sections(document):
        if not REF_TAG_RE.search(body):
            findings.append(
                Finding(
                    "V8",
                    "error",
                    f"section {heading.text!r} has no citation — a section the "
                    "sources do not support must not be written at all",
                    heading.line,
                )
            )
    return findings


# --------------------------------------------------------------------------
# V9 — Tibetan script only
# --------------------------------------------------------------------------

_LATIN_OR_ASCII_DIGIT_RE = re.compile(r"[A-Za-z0-9]+")


def _rule_v9(document: _Document) -> list[Finding]:
    findings: list[Finding] = []
    for line_number, line in enumerate(document.masked.split("\n"), start=1):
        offenders = _LATIN_OR_ASCII_DIGIT_RE.findall(line)
        if not offenders:
            continue
        findings.append(
            Finding(
                "V9",
                "error",
                "non-Tibetan text in the article body: "
                + ", ".join(repr(item) for item in offenders[:5])
                + (" …" if len(offenders) > 5 else "")
                + " — Latin letters and ASCII digits belong only inside <ref> "
                "URLs and template parameters (Tibetan numerals ༠–༩ in prose)",
                line_number,
            )
        )
    return findings


# --------------------------------------------------------------------------
# V10 — the tsheg boundary
# --------------------------------------------------------------------------

_TIBETAN_SYLLABLE_START = "ཀ"
_TIBETAN_SYLLABLE_END = "ྼ"


def _continues_syllable(char: str) -> bool:
    return bool(char) and _TIBETAN_SYLLABLE_START <= char <= _TIBETAN_SYLLABLE_END


def _rule_v10(document: _Document) -> list[Finding]:
    """``'''X'''Y`` and ``[[X]]Y`` fuse two syllables into one.

    bo.wikipedia's parser treats ``'''X་'''Y``, ``'''X'''་Y`` and ``'''X'''Y``
    identically, so the third — which is a Tibetan spelling error and destroys
    the line's only legal break opportunity — will never surface as a wiki
    error.  Only the linter sees it.
    """
    text = document.text
    findings: list[Finding] = []

    def check(inner: str, after_offset: int, markup: str) -> None:
        after = text[after_offset] if after_offset < len(text) else ""
        if not after or after == TSHEG or not _continues_syllable(after):
            return
        if inner and inner[-1] == TSHEG:
            return
        findings.append(
            Finding(
                "V10",
                "error",
                f"no tsheg (U+0F0B) at the {markup} boundary — "
                f"{_excerpt(text[max(0, after_offset - 24) : after_offset + 8], 60)}",
                document.line_of(after_offset),
            )
        )

    bold_positions = [match.start() for match in re.finditer(r"'''", text)]
    if len(bold_positions) % 2:
        findings.append(
            Finding(
                "V10",
                "error",
                "unbalanced ''' bold markup, so the bold boundaries cannot be "
                "checked",
                document.line_of(bold_positions[-1]),
            )
        )
    for opening, closing in zip(bold_positions[0::2], bold_positions[1::2]):
        check(text[opening + 3 : closing], closing + 3, "'''")

    for match in WIKILINK_RE.finditer(text):
        display = match.group("inner").split("|")[-1]
        check(display, match.end(), "[[…]]")

    return findings


# --------------------------------------------------------------------------
# V11 — the fixed tail
# --------------------------------------------------------------------------


def _rule_v11(document: _Document) -> list[Finding]:
    findings: list[Finding] = []
    top_level = [heading for heading in document.headings if heading.level == 2]
    names = [heading.text for heading in top_level]

    positions: dict[str, list[int]] = {}
    for index, name in enumerate(names):
        if name in TAIL_HEADINGS:
            positions.setdefault(name, []).append(index)

    for name, indexes in positions.items():
        if len(indexes) > 1:
            findings.append(
                Finding(
                    "V11",
                    "error",
                    f"tail section {name!r} appears {len(indexes)} times",
                    top_level[indexes[1]].line,
                )
            )

    if document.has_refs and HEADING_REFERENCES not in positions:
        findings.append(
            Finding(
                "V11",
                "error",
                f"the article has footnotes but no == {HEADING_REFERENCES} == "
                "section",
            )
        )

    present = [name for name in TAIL_HEADINGS if name in positions]
    if not present:
        return findings

    found_order = [name for name in names if name in TAIL_HEADINGS]
    expected_order = [name for name in TAIL_HEADINGS if name in positions]
    if _dedupe(found_order) != expected_order:
        findings.append(
            Finding(
                "V11",
                "error",
                "the tail sections are out of order: expected "
                + " → ".join(expected_order)
                + ", found "
                + " → ".join(_dedupe(found_order)),
                top_level[positions[found_order[0]][0]].line,
            )
        )

    tail_start = len(names) - len(present)
    for index, name in enumerate(names):
        if index >= tail_start and name not in TAIL_HEADINGS:
            findings.append(
                Finding(
                    "V11",
                    "error",
                    f"section {name!r} comes after the fixed tail sections; the "
                    "last sections must be "
                    + " → ".join(TAIL_HEADINGS),
                    top_level[index].line,
                )
            )
    return findings


def _dedupe(values: Sequence[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


# --------------------------------------------------------------------------
# V12 — placeholders and model chatter
# --------------------------------------------------------------------------

_PLACEHOLDER_PATTERNS: tuple[tuple["re.Pattern[str]", str], ...] = (
    (re.compile(r"dummy\.(?:com|org|net)", re.IGNORECASE), "dummy placeholder URL"),
    (
        re.compile(r"example\.(?:com|org|net)", re.IGNORECASE),
        "example.com placeholder URL",
    ),
    (
        re.compile(r"wikisource\.com", re.IGNORECASE),
        "wikisource.com is not a real domain (the site is wikisource.org)",
    ),
    (re.compile(r"\b(?:TODO|FIXME|TBD|XXX)\b"), "editing placeholder"),
    (re.compile(r"<[A-Z][A-Z0-9_ -]*>"), "unfilled <PLACEHOLDER> slot"),
    (re.compile(r"\bplaceholder\b", re.IGNORECASE), "the word 'placeholder'"),
    (re.compile(r"\blorem ipsum\b", re.IGNORECASE), "lorem ipsum filler"),
    (re.compile(r"```"), "markdown code fence left in the wikitext"),
    (
        re.compile(
            r"(?im)^\s*(?:here (?:is|are)\b|here's\b|sure[,!]|certainly[,!]|"
            r"of course[,!]|i hope this helps|as an ai\b|i cannot\b|note:)"
        ),
        "leftover assistant chatter",
    ),
    (
        re.compile(r'"(?:lead|sections|citations|paragraphs)"\s*:'),
        "leftover JSON from the drafting stage",
    ),
)


def _rule_v12(document: _Document) -> list[Finding]:
    findings: list[Finding] = []
    for pattern, description in _PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(document.text):
            findings.append(
                Finding(
                    "V12",
                    "error",
                    f"{description}: {match.group(0)!r}",
                    document.line_of(match.start()),
                )
            )
    return findings


# --------------------------------------------------------------------------
# Warnings (wikitext-spec.md §7, non-blocking)
# --------------------------------------------------------------------------


def _warnings(document: _Document, citations: Sequence[Citation]) -> list[Finding]:
    findings: list[Finding] = []

    for citation in citations:
        missing = [
            label
            for label, value in (("year", citation.year), ("page", citation.page))
            if not value
        ]
        if missing:
            findings.append(
                Finding(
                    "W1",
                    "warning",
                    f"citation {citation.source_id!r} is missing "
                    + " and ".join(missing),
                )
            )
        if not citation.is_linked:
            findings.append(
                Finding(
                    "W2",
                    "warning",
                    f"citation {citation.source_id!r} has no URL, so a reader "
                    "cannot check it without the physical book",
                )
            )

    for _, heading, body in _body_sections(document):
        if len(REF_TAG_RE.findall(body)) == 1:
            findings.append(
                Finding(
                    "W3",
                    "warning",
                    f"section {heading.text!r} rests on a single citation",
                    heading.line,
                )
            )

    length = syllable_count(document.masked)
    if length < MIN_ARTICLE_SYLLABLES:
        findings.append(
            Finding(
                "W4",
                "warning",
                f"article is {length} ཚེག་བར long, below the "
                f"{MIN_ARTICLE_SYLLABLES}-syllable threshold",
            )
        )
    return findings


# --------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------


def validate(
    wikitext: str,
    *,
    citations: Sequence[Citation],
    allowed_categories: Iterable[str],
    source_loader: SourceLoader | None = None,
) -> list[Finding]:
    """Run V1–V12 (plus the spec's four warnings) over one article.

    ``citations`` is the article's declared citation inventory: V2 checks that
    every ``<ref>`` in the text was rendered from one of these, which is what
    "resolves to a source declared in ``sources.yaml``" means once the emitter
    has done its work.  ``source_loader`` is optional only so the gate can run
    before the corpus is on disk — without it V1 downgrades to a warning and
    the article is *not* cleared for publication.

    Findings come back ordered by rule, errors and warnings interleaved;
    :func:`format_report` groups them and :func:`has_errors` is the gate.
    """
    document = _Document(wikitext)
    findings: list[Finding] = []
    findings.extend(_rule_v1(citations, source_loader))
    findings.extend(_rule_v2(document, citations, source_loader))
    findings.extend(_rule_v3(document))
    findings.extend(_rule_v4(document))
    findings.extend(_rule_v5(document))
    findings.extend(_rule_v6(document))
    findings.extend(_rule_v7(document, allowed_categories))
    findings.extend(_rule_v8(document))
    findings.extend(_rule_v9(document))
    findings.extend(_rule_v10(document))
    findings.extend(_rule_v11(document))
    findings.extend(_rule_v12(document))
    findings.extend(_warnings(document, citations))
    return findings


def has_errors(findings: Iterable[Finding]) -> bool:
    """The gate: True means do not publish."""
    return any(finding.severity == "error" for finding in findings)


def format_report(findings: Sequence[Finding]) -> str:
    """A human-readable report, grouped by severity.

    Written for the reviewer sitting at the ``review/pending/`` queue, so every
    line carries the rule id, the line number and the reason — a reviewer who
    has to open the spec to interpret the report will stop reading it.
    """
    errors = [finding for finding in findings if finding.severity == "error"]
    warnings = [finding for finding in findings if finding.severity != "error"]

    lines: list[str] = []
    for heading, group in (("ERRORS", errors), ("WARNINGS", warnings)):
        if not group:
            continue
        lines.append(f"{heading} ({len(group)})")
        by_rule: dict[str, list[Finding]] = {}
        for finding in group:
            by_rule.setdefault(finding.rule, []).append(finding)
        for rule, rule_findings in by_rule.items():
            title = RULE_TITLES.get(rule, "")
            lines.append(f"  {rule}" + (f" — {title}" if title else ""))
            for finding in rule_findings:
                location = f"line {finding.line}: " if finding.line else ""
                lines.append(f"    {location}{finding.message}")
        lines.append("")

    if errors:
        lines.append(
            f"FAIL — {len(errors)} error(s), {len(warnings)} warning(s). "
            "Not cleared for publication."
        )
    else:
        lines.append(f"PASS — 0 errors, {len(warnings)} warning(s).")
    return "\n".join(lines)
