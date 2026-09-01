"""The canonical wikitext emitter for bo.wikipedia articles.

Why an emitter at all, rather than letting the drafting model write wikitext:
every failure mode catalogued in ``docs/reference/wikitext-spec.md`` is a
*formatting* decision — the ``{{Reflist}}`` double heading, the tsheg dropped at
a bold boundary, the orphaned ``<ref>`` with no ``<references />``.  A model
asked for wikitext reproduces the English-Wikipedia idiom because that is what
it saw most of; on bo.wikipedia that idiom is broken.  So the model returns
structured content and this module owns the markup, which makes every one of
those decisions testable offline.

Everything here is a pure function of its arguments.  No I/O, no network, no
configuration; ``kangyur_wiki.wiki.validator`` is the gate that checks the
result, and the two modules share the regexes defined here so they cannot drift
apart.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Sequence
from urllib.parse import quote as _percent_encode

__all__ = [
    "TSHEG",
    "SHAD",
    "DOUBLE_SHAD",
    "CATEGORY_NAMESPACE",
    "CATEGORY_NAMESPACE_ALIAS",
    "HEADING_SEE_ALSO",
    "HEADING_REFERENCES",
    "HEADING_BIBLIOGRAPHY",
    "TAIL_HEADINGS",
    "REFERENCES_TAG",
    "PAGE_LABEL",
    "HEADING_RE",
    "REF_TAG_RE",
    "REF_BLOCK_RE",
    "REFERENCES_TAG_RE",
    "SINGULAR_REFERENCE_TAG_RE",
    "REFLIST_RE",
    "TEMPLATE_RE",
    "CATEGORY_RE",
    "WIKILINK_RE",
    "HTML_TAG_RE",
    "Citation",
    "Section",
    "Article",
    "ref_name",
    "syllable_spans",
    "syllables",
    "syllable_count",
    "text_fragment",
    "citation_url",
    "join_boundary",
    "render_bold",
    "render_wikilink",
    "wikilink_target",
    "render_ref",
    "render_ref_body",
    "render_ref_reuse",
    "render_lead",
    "render_heading",
    "render_section",
    "render_category",
    "format_bibliography_entry",
    "render_article",
]

# --------------------------------------------------------------------------
# Tibetan orthography and bo.wikipedia furniture
# --------------------------------------------------------------------------

#: U+0F0B, the intersyllabic separator.  It is orthography, not whitespace: a
#: missing tsheg is a spelling error *and* removes the only legal line-break
#: opportunity (Unicode line-break class BA).
TSHEG = "་"
#: U+0F0D shad, the sentence terminator.
SHAD = "།"
#: U+0F0E nyis shad.
DOUBLE_SHAD = "༎"

#: Characters that end a ཚེག་བར unit.  Whitespace is included because a line
#: break stands in for a tsheg in practice, and the shads because they close a
#: syllable as surely as a tsheg does.
_SYLLABLE_DELIMITERS = frozenset(
    TSHEG
    + "༌"  # tsheg bstar, the non-breaking tsheg
    + SHAD
    + DOUBLE_SHAD
    + "༄༅༆༇༈༉༊"  # yig mgo and friends
    + "༏༐༑༒༔"  # rin chen spungs shad, etc.
    + "༺༻༼༽"  # brackets
    + " \t\r\n "
)

#: Tibetan characters that *continue* a syllable.  Used by the tsheg-boundary
#: check: markup followed by one of these with no tsheg in between is the
#: spelling error the linter exists to catch.
_TIBETAN_SYLLABLE_RANGE = ("ཀ", "ྼ")

CATEGORY_NAMESPACE = "རིགས་དབྱེ།"
#: The English namespace alias is what the team's already-published articles
#: use (``[[Category:ནང་བསྟན།]]``).  We never emit it, but the validator has to
#: recognise it or it would report a categorised article as uncategorised.
CATEGORY_NAMESPACE_ALIAS = "Category"

HEADING_SEE_ALSO = "འབྲེལ་ཡོད་ཤོག་ངོས།"
HEADING_REFERENCES = "ལུང་ཁུངས།"
HEADING_BIBLIOGRAPHY = "དཔྱད་གཞིའི་ཡིག་ཆ།"
#: The fixed tail, in order (wikitext-spec.md §1, topic 324 rule ༧).
TAIL_HEADINGS = (HEADING_SEE_ALSO, HEADING_REFERENCES, HEADING_BIBLIOGRAPHY)

#: Never ``{{Reflist}}``: bo.wikipedia's Reflist template opens with its own
#: ``== ཡོང་ཁུངས། ==`` heading, so the enwiki idiom renders two stacked
#: headings.  Verified by live ``action=parse`` on 2026-07-29.
REFERENCES_TAG = "<references />"

#: Page-number label inside a hand-formatted primary-source ref.
PAGE_LABEL = "ཤོག་གྲངས་"

# --------------------------------------------------------------------------
# Shared markup regexes
#
# The validator imports these rather than re-deriving them, so "what the
# emitter writes" and "what the linter looks for" cannot drift apart.
# --------------------------------------------------------------------------

#: A wikitext heading line: ``== text ==`` through ``====== text ======``.
HEADING_RE = re.compile(r"^(={2,6})[ \t]*(.*?)[ \t]*\1[ \t]*$", re.MULTILINE)

#: Any ``<ref>``-family tag: opening, closing or self-closing.  Deliberately
#: does *not* match ``<references />`` — ``attrs`` must start with whitespace,
#: and ``<references`` offers ``e`` at that position.
REF_TAG_RE = re.compile(
    r"<\s*(?P<close>/)?\s*ref(?P<attrs>\s[^>]*?)?\s*(?P<selfclose>/)?\s*>",
    re.IGNORECASE,
)

#: A complete ``<ref ...>body</ref>``.
REF_BLOCK_RE = re.compile(
    r"<\s*ref(?P<attrs>\s[^>]*?)?\s*>(?P<body>.*?)<\s*/\s*ref\s*>",
    re.IGNORECASE | re.DOTALL,
)

REFERENCES_TAG_RE = re.compile(r"<\s*references\b[^>]*>", re.IGNORECASE)
#: Topic 309 writes ``<reference>``/``</reference>``.  That is a typo, not
#: MediaWiki syntax, and it renders nothing at all.
SINGULAR_REFERENCE_TAG_RE = re.compile(
    r"<\s*/?\s*reference(?!s)\b[^>]*>", re.IGNORECASE
)

#: ``{{Reflist}}`` in any case, with any spacing or parameters.
REFLIST_RE = re.compile(r"\{\{\s*reflist\b[^{}]*\}\}", re.IGNORECASE)

TEMPLATE_RE = re.compile(r"\{\{.*?\}\}", re.DOTALL)

CATEGORY_RE = re.compile(
    r"\[\[\s*(?:"
    + re.escape(CATEGORY_NAMESPACE)
    + r"|"
    + CATEGORY_NAMESPACE_ALIAS
    + r")\s*:\s*(?P<name>[^\]|]*?)\s*(?:\|[^\]]*)?\]\]",
    re.IGNORECASE,
)

WIKILINK_RE = re.compile(r"\[\[(?P<inner>[^\[\]]*)\]\]")

HTML_TAG_RE = re.compile(r"<[^<>]*>")

_REF_NAME_RE = re.compile(
    r"""\bname\s*=\s*(?:"(?P<dq>[^"]*)"|'(?P<sq>[^']*)'|(?P<bare>[^\s"'<>/]+))""",
    re.IGNORECASE,
)

_BLANK_LINE_RE = re.compile(r"\n[ \t]*\n")


# --------------------------------------------------------------------------
# Small pure helpers
# --------------------------------------------------------------------------


def _nfc(value: str) -> str:
    """NFC everywhere, always — mixed normalisation forms make two identical
    Tibetan strings compare unequal, which would silently break quote
    verification and title probing alike."""
    return unicodedata.normalize("NFC", value)


def _clean(value: object) -> str:
    """Coerce to a stripped, NFC-normalised string (``None`` becomes empty)."""
    if value is None:
        return ""
    return _nfc(value if isinstance(value, str) else str(value)).strip()


def _is_tibetan_syllable_char(char: str) -> bool:
    """True for a character that continues a Tibetan syllable."""
    return bool(char) and _TIBETAN_SYLLABLE_RANGE[0] <= char <= _TIBETAN_SYLLABLE_RANGE[1]


def _as_paragraphs(value: object) -> tuple[str, ...]:
    """Normalise paragraph input to a tuple of non-empty NFC strings.

    A single string is split on blank lines (that is what a blank line means in
    wikitext); a sequence is taken at its word, one element per paragraph.
    """
    if value is None:
        return ()
    if isinstance(value, str):
        chunks: list[str] = _BLANK_LINE_RE.split(value)
    else:
        chunks = [chunk if isinstance(chunk, str) else str(chunk) for chunk in value]
    return tuple(text for text in (_nfc(chunk).strip() for chunk in chunks) if text)


def _strip_heading_marks(heading: str) -> str:
    """Accept ``== X ==`` or ``X`` and return ``X``."""
    text = _clean(heading)
    match = HEADING_RE.match(text)
    if match:
        return _clean(match.group(2))
    return text.strip("=").strip()


def ref_name(attrs: str | None) -> str:
    """Extract the ``name="..."`` value from a ref tag's attribute text."""
    if not attrs:
        return ""
    match = _REF_NAME_RE.search(attrs)
    if not match:
        return ""
    return _clean(match.group("dq") or match.group("sq") or match.group("bare") or "")


# --------------------------------------------------------------------------
# ཚེག་བར segmentation
# --------------------------------------------------------------------------


def syllable_spans(text: str) -> list[tuple[int, int]]:
    """Character spans of the ཚེག་བར units in ``text``, delimiters included.

    Each span runs from the first character of a syllable up to and including
    the delimiter run that closes it, so ``text[spans[0][0]:spans[k][1]]`` is
    always a *literal* substring of ``text`` that starts and ends on a syllable
    boundary.  Text fragments need exactly that property: the browser matches
    the fragment against the rendered page character for character.

    This is a deliberately dependency-free segmentation.  botok segments
    *words*; a text fragment and a syllable count both want ཚེག་བར, which is
    decidable from the tsheg alone.
    """
    normalized = _nfc(text)
    spans: list[tuple[int, int]] = []
    index = 0
    length = len(normalized)
    while index < length:
        if normalized[index] in _SYLLABLE_DELIMITERS:
            index += 1
            continue
        start = index
        while index < length and normalized[index] not in _SYLLABLE_DELIMITERS:
            index += 1
        while index < length and normalized[index] in _SYLLABLE_DELIMITERS:
            index += 1
        spans.append((start, index))
    return spans


def syllables(text: str) -> list[str]:
    """The ཚེག་བར units of ``text``, each carrying its trailing delimiter."""
    normalized = _nfc(text)
    return [normalized[start:end] for start, end in syllable_spans(normalized)]


def syllable_count(text: str) -> int:
    """How many ཚེག་བར ``text`` contains."""
    return len(syllable_spans(text))


# --------------------------------------------------------------------------
# Text fragments — what makes a citation independently checkable
# --------------------------------------------------------------------------


def text_fragment(quote: str, syllables_n: int = 6) -> str:
    """Build a ``#:~:text=`` deep link anchor for ``quote``.

    A reader who follows a ref should land on the quoted passage, not on the
    top of a 400-page eText; the team's published ``སཏྭ་`` article does this by
    hand and this function is the automation of that step
    (wikitext-spec.md §2, "Source-link resolution").

    Long quotes become a ``textStart,textEnd`` range — the first and last
    ``syllables_n`` ཚེག་བར — because the WICG spec caps neither side but a
    whole-paragraph fragment is fragile against a single typographic
    difference.  A quote of ``2 * syllables_n`` syllables or fewer is encoded
    whole, with no comma.

    ``-`` is percent-encoded even though it is URL-safe: an unescaped hyphen is
    the fragment syntax's prefix/suffix marker and would be parsed as one.
    """
    if syllables_n < 1:
        raise ValueError("syllables_n must be at least 1")
    normalized = _nfc(quote)
    spans = syllable_spans(normalized)
    if not spans:
        raise ValueError("quote contains no Tibetan syllables to anchor on")

    if len(spans) <= 2 * syllables_n:
        whole = normalized[spans[0][0] : spans[-1][1]]
        return "#:~:text=" + _encode_fragment(whole)

    head = normalized[spans[0][0] : spans[syllables_n - 1][1]]
    tail = normalized[spans[-syllables_n][0] : spans[-1][1]]
    return f"#:~:text={_encode_fragment(head)},{_encode_fragment(tail)}"


def _encode_fragment(value: str) -> str:
    """Percent-encode one side of a text fragment.

    Internal whitespace collapses to a single space first: browsers match text
    fragments against whitespace-normalised rendered text, so a newline carried
    over from the source file would simply fail to match.
    """
    collapsed = " ".join(value.split())
    return _percent_encode(collapsed, safe="").replace("-", "%2D")


def citation_url(citation: "Citation", *, anchor: bool = True) -> str:
    """The URL a ref should carry: the source URL plus its passage anchor.

    A URL that already has a fragment is left alone — the resolver may have
    produced a better anchor (a Wikisource subpage, say) than we could.
    """
    url = citation.url
    if not url or not anchor or not citation.quote or "#" in url:
        return url
    try:
        return url + text_fragment(citation.quote)
    except ValueError:
        # A quote with no Tibetan syllables cannot be anchored; the bare URL is
        # still better than no ref at all, and V12 catches genuine placeholders.
        return url


# --------------------------------------------------------------------------
# Value objects
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Citation:
    """One source behind one claim.

    ``isbn`` is what routes the ref: a source with an ISBN is a modern
    secondary and gets CS1 (``{{Cite book}}``); everything else is Kangyur,
    Tengyur or a Tibetan commentary and gets a hand-formatted ``<ref>``,
    because CS1 renders English furniture (``2 ed.``, ``pp.``, ``Retrieved``)
    inside Tibetan prose (wikitext-spec.md §2).

    ``quote`` is the verbatim passage.  It is stored untouched apart from NFC
    normalisation — the verify stage compares it character for character
    against the source file, so any "tidying" here would break the gate.
    """

    source_id: str
    author: str = ""
    title: str = ""
    year: str = ""
    page: str = ""
    url: str = ""
    quote: str = ""
    isbn: str = ""
    #: The commentary block this quotation came from (``^1-1-2-1``), when the
    #: source has been through stage 1b.  Recorded in ``citations.json`` and the
    #: review report, **not** rendered into the ``<ref>`` — the ref format is
    #: fixed by ``docs/reference/wikitext-spec.md`` §2 and an Obsidian block ID
    #: means nothing to a Wikipedia reader.  Its job is internal: it tells the
    #: verify stage which paragraph to check the quotation against, and it tells
    #: a human reviewer where to look.
    segment_id: str = ""

    _TEXT_FIELDS = (
        "source_id",
        "author",
        "title",
        "year",
        "page",
        "url",
        "quote",
        "isbn",
        "segment_id",
    )

    def __post_init__(self) -> None:
        for name in self._TEXT_FIELDS:
            object.__setattr__(self, name, _clean(getattr(self, name)))
        if not self.source_id:
            raise ValueError(
                "Citation.source_id is required — a ref with no source id "
                "cannot be resolved against sources.yaml (rule V2)"
            )

    @property
    def is_secondary(self) -> bool:
        """True when this is a modern secondary source, i.e. CS1 applies."""
        return bool(self.isbn)

    @property
    def is_linked(self) -> bool:
        """False when the ref will ship unlinked and must be flagged."""
        return bool(self.url)

    @property
    def has_full_metadata(self) -> bool:
        """All four of topic 324 rule ༦: author, title, year, page."""
        return all((self.author, self.title, self.year, self.page))

    @property
    def locator(self) -> str:
        """``TARAC02_DGT#^1-1-2-1`` — the source plus the block, for reports."""
        return f"{self.source_id}#^{self.segment_id}" if self.segment_id else self.source_id


@dataclass(frozen=True)
class Section:
    """One ``== heading ==`` section and its paragraphs.

    ``paragraphs`` hold wikitext already carrying their ``<ref>`` markup: the
    citation belongs to the sentence it supports, so splicing refs in here —
    after the sentence has been written — would put them in the wrong place.
    """

    heading: str
    paragraphs: Sequence[str] = ()
    level: int = 2

    def __post_init__(self) -> None:
        heading = _strip_heading_marks(self.heading)
        if not heading:
            raise ValueError("Section.heading must be non-empty")
        object.__setattr__(self, "heading", heading)
        object.__setattr__(self, "paragraphs", _as_paragraphs(self.paragraphs))
        level = int(self.level)
        if not 2 <= level <= 6:
            raise ValueError(f"Section.level must be between 2 and 6, got {level}")
        object.__setattr__(self, "level", level)

    @property
    def body(self) -> str:
        return "\n\n".join(self.paragraphs)

    @property
    def has_citation(self) -> bool:
        """Whether the section carries at least one ``<ref>`` (rule V8)."""
        return bool(REF_TAG_RE.search(self.body))


@dataclass(frozen=True)
class Article:
    """A complete doctrinal-term article, ready to render.

    ``citations`` is the article's citation inventory — the refs are already
    embedded in the section text, but the validator needs the structured
    records to check that every rendered ref resolves to a declared source and
    to report the ones missing a year, a page or a URL.
    """

    term: str
    lead: Sequence[str] | str = ()
    sections: Sequence[Section] = ()
    see_also: Sequence[str] = ()
    citations: Sequence[Citation] = ()
    bibliography: Sequence[str] = ()
    categories: Sequence[str] = ()

    def __post_init__(self) -> None:
        term = _clean(self.term)
        if not term:
            raise ValueError("Article.term must be non-empty")
        object.__setattr__(self, "term", term)
        object.__setattr__(self, "lead", _as_paragraphs(self.lead))
        object.__setattr__(self, "sections", tuple(self.sections))
        object.__setattr__(
            self, "see_also", tuple(_clean(item) for item in self.see_also if _clean(item))
        )
        object.__setattr__(self, "citations", tuple(self.citations))
        object.__setattr__(
            self,
            "bibliography",
            tuple(_clean(item) for item in self.bibliography if _clean(item)),
        )
        object.__setattr__(
            self,
            "categories",
            tuple(_clean(item) for item in self.categories if _clean(item)),
        )
        for section in self.sections:
            if not isinstance(section, Section):
                raise TypeError("Article.sections must contain Section instances")
        for citation in self.citations:
            if not isinstance(citation, Citation):
                raise TypeError("Article.citations must contain Citation instances")


# --------------------------------------------------------------------------
# Inline markup
# --------------------------------------------------------------------------

_CLOSING_MARKUP = ("'''", "''", "]]", "}}")


def _inner_last_char(text: str) -> str:
    """The last *content* character of ``text``, looking through closing markup.

    ``'''བྱང་ཆུབ་སེམས་'''`` ends in ``'``, but the character that matters for
    the tsheg-boundary rule is the tsheg inside the bold.
    """
    stripped = text
    while stripped:
        for closer in _CLOSING_MARKUP:
            if stripped.endswith(closer):
                stripped = stripped[: -len(closer)]
                break
        else:
            break
    return stripped[-1] if stripped else ""


def join_boundary(left: str, right: str) -> str:
    """Concatenate two wikitext fragments, keeping a tsheg at the boundary.

    ``'''X'''Y`` fuses two syllables into one and destroys the line-break
    opportunity — a spelling error bo.wikipedia's parser will never complain
    about (wikitext-spec.md §4).  A tsheg is *inserted* when one is missing on
    both sides; nothing is ever removed, because deleting punctuation from
    Tibetan text is the other way to corrupt it.
    """
    if not left:
        return right
    if not right:
        return left
    if right[0] == TSHEG or not _is_tibetan_syllable_char(right[0]):
        return left + right
    if _inner_last_char(left) == TSHEG:
        return left + right
    return left + TSHEG + right


def render_bold(text: str) -> str:
    """``'''text'''`` — verbatim, with no punctuation surgery.

    Use :func:`join_boundary` for whatever follows it.
    """
    cleaned = _clean(text)
    if not cleaned:
        raise ValueError("cannot bold an empty string")
    if "'''" in cleaned:
        raise ValueError(f"text already contains bold markup: {cleaned!r}")
    return f"'''{cleaned}'''"


def wikilink_target(term: str) -> str:
    """The page title a ``[[link]]`` should point at: trailing tsheg, no shad.

    Topic 324 rule ༨.  The shad is sentence punctuation, not part of the title,
    and ``[[རྡོ་རྗེ།]]`` is a different page from ``[[རྡོ་རྗེ་]]`` — bo.wikipedia
    genuinely has both, for several terms, one of each pair usually broken.
    """
    target = _clean(term)
    if not target:
        raise ValueError("wikilink target must be non-empty")
    while target and target[-1] in (SHAD, DOUBLE_SHAD, TSHEG):
        target = target[:-1].rstrip()
    if not target:
        raise ValueError(f"wikilink target {term!r} is nothing but punctuation")
    if _is_tibetan_syllable_char(target[-1]):
        target += TSHEG
    return target


def render_wikilink(term: str, display: str | None = None) -> str:
    """``[[རྡོ་རྗེ་]]``, or ``[[རྡོ་རྗེ་|རྡོ་རྗེ།]]`` when ``display`` differs.

    Red links are expected output, not a defect: they mark terms the pipeline
    has not written yet, and the team already uses blue-vs-red as its manual
    existence check (wikitext-spec.md §3).
    """
    target = wikilink_target(term)
    for forbidden in ("[[", "]]", "|"):
        if forbidden in target:
            raise ValueError(f"wikilink target contains {forbidden!r}: {target!r}")
    shown = _clean(display) if display is not None else ""
    if not shown or shown == target:
        return f"[[{target}]]"
    for forbidden in ("[[", "]]", "|"):
        if forbidden in shown:
            raise ValueError(f"wikilink display contains {forbidden!r}: {shown!r}")
    return f"[[{target}|{shown}]]"


# --------------------------------------------------------------------------
# References
# --------------------------------------------------------------------------


def _with_shad(value: str) -> str:
    """Append a shad unless the field already ends in Tibetan terminal
    punctuation — doubling a shad is a visible typo."""
    if not value:
        return ""
    if value[-1] in (SHAD, DOUBLE_SHAD):
        return value
    return value + SHAD


def _split_author(author: str) -> tuple[str, str]:
    """Split ``"Last, First"`` for CS1; a Tibetan name has no such split, so it
    goes wholesale into ``last`` and ``first`` stays empty."""
    if "," in author:
        last, first = author.split(",", 1)
        return last.strip(), first.strip()
    return author, ""


def render_ref_body(citation: Citation, *, anchor: bool = True) -> str:
    """The inside of a ``<ref>`` for ``citation``.

    Split out from :func:`render_ref` so the validator can check that every ref
    in a page resolves to a declared citation (rule V2) without re-implementing
    the format.
    """
    if citation.is_secondary:
        return _render_cs1(citation)
    return _render_primary(citation, anchor=anchor)


def _render_primary(citation: Citation, *, anchor: bool) -> str:
    """Hand-formatted canonical-source ref: ``[URL AUTHOR། TITLE། ཤོག་གྲངས་PAGE]``."""
    caption_parts = [
        part
        for part in (_with_shad(citation.author), _with_shad(citation.title))
        if part
    ]
    if citation.page:
        caption_parts.append(f"{PAGE_LABEL}{citation.page}")
    caption = " ".join(caption_parts)

    url = citation_url(citation, anchor=anchor)
    if not url:
        # No link available.  Emitted anyway, and the caller flags the gap in
        # the review report, so a missing source URL is visible rather than
        # silently dropped (PLAN.md §5).
        return caption
    if "]" in url or " " in url:
        raise ValueError(f"citation url is not a usable external link: {url!r}")
    return f"[{url} {caption}]" if caption else f"[{url}]"


def _render_cs1(citation: Citation) -> str:
    """``{{Cite book}}`` for a modern secondary with a real ISBN.

    Parameters are emitted even when empty, matching wikitext-spec.md §2; CS1
    ignores an empty parameter.  ``|pages=`` is added only when a page is
    known, because topic 324 rule ༦ wants the page and dropping it here would
    lose data the ref record actually has.
    """
    last, first = _split_author(citation.author)
    params = [
        ("last", last),
        ("first", first),
        ("title", citation.title),
        ("year", citation.year),
        ("isbn", citation.isbn),
    ]
    if citation.page:
        params.append(("pages", citation.page))
    for name, value in params:
        if "|" in value or "}}" in value:
            raise ValueError(
                f"citation field {name}={value!r} would break the template call"
            )
    rendered = " ".join(f"|{name}={value}" for name, value in params)
    return f"{{{{Cite book {rendered} }}}}"


def render_ref(
    citation: Citation,
    name: str | None = None,
    *,
    first_use: bool = True,
    anchor: bool = True,
) -> str:
    """Render one footnote.

    ``name`` turns the ref into a named ref.  The *first* use carries the full
    content (``<ref name="x">…</ref>``); every later use is the self-closing
    form, which is what ``first_use=False`` — or :func:`render_ref_reuse` —
    emits.  Getting that backwards is a MediaWiki cite error, and topic 309's
    ``<reference>`` spelling is a typo that renders nothing at all.
    """
    cleaned_name = _clean(name) if name else ""
    if name is not None and not cleaned_name:
        raise ValueError("ref name must be non-empty when given")
    if cleaned_name and re.search(r"""["'<>/\s]""", cleaned_name):
        raise ValueError(f"ref name {cleaned_name!r} contains illegal characters")

    if not first_use:
        if not cleaned_name:
            raise ValueError("a reused ref must have a name")
        return render_ref_reuse(cleaned_name)

    body = render_ref_body(citation, anchor=anchor)
    if not body:
        raise ValueError(
            f"citation {citation.source_id!r} has no author, title, page or url "
            "to render — an empty <ref> is a cite error"
        )
    open_tag = f'<ref name="{cleaned_name}">' if cleaned_name else "<ref>"
    return f"{open_tag}{body}</ref>"


def render_ref_reuse(name: str) -> str:
    """``<ref name="x" />`` — the second and later use of a named ref."""
    cleaned = _clean(name)
    if not cleaned:
        raise ValueError("ref name must be non-empty")
    return f'<ref name="{cleaned}" />'


# --------------------------------------------------------------------------
# Blocks
# --------------------------------------------------------------------------


def render_lead(term: str, body: str = "") -> str:
    """The opening sentence: bolded term, no heading (topic 324 rule ༣).

    The tsheg goes *inside* the bold when the body does not already start with
    one, which is the form attested in the live ``སྟོང་པ་ཉིད།`` article; both
    positions are correct, having none is not.
    """
    cleaned_term = _clean(term)
    if not cleaned_term:
        raise ValueError("Article term must be non-empty")
    text = _nfc(body).strip()
    if text.startswith("'''"):
        # The caller already bolded the opening; respect it rather than
        # producing '''''double''''' markup.
        return text

    # A drafting model writing a natural lead tends to open with the term
    # itself (`སྒྲོལ་མ་ཞེས་པའི་...`); prepending the bolded term verbatim would
    # then read `'''སྒྲོལ་མ་'''སྒྲོལ་མ་ཞེས་པའི་...`. Strip that one redundant
    # copy — but only when something follows it, so a body that IS the term
    # still renders.
    bare = cleaned_term.rstrip(TSHEG + SHAD + DOUBLE_SHAD)
    if bare and text.startswith(bare):
        rest = text[len(bare):].lstrip(TSHEG)
        if rest.strip():
            text = rest

    bold_text = cleaned_term
    if (
        text
        and not text.startswith(TSHEG)
        and _is_tibetan_syllable_char(bold_text[-1])
    ):
        bold_text += TSHEG
    return join_boundary(render_bold(bold_text), text)


def render_heading(heading: str, level: int = 2) -> str:
    """``== heading ==``.

    Heading text is emitted exactly as given: ``ངེས་ཚིག`` carries no shad while
    every other canonical heading does, and "helpfully" adding one would create
    a section title that does not match the exemplars.
    """
    text = _strip_heading_marks(heading)
    if not text:
        raise ValueError("heading must be non-empty")
    if not 2 <= level <= 6:
        raise ValueError(f"heading level must be between 2 and 6, got {level}")
    marks = "=" * level
    return f"{marks} {text} {marks}"


def render_section(section: Section) -> str:
    """One heading plus its paragraphs, blank-line separated."""
    block = render_heading(section.heading, section.level)
    if section.paragraphs:
        block += "\n" + "\n\n".join(section.paragraphs)
    return block


def render_category(name: str) -> str:
    """``[[རིགས་དབྱེ།:X]]`` from a bare category name.

    A name that already carries a namespace prefix is de-prefixed first, so a
    caller passing ``Category:ནང་བསྟན།`` cannot produce
    ``[[རིགས་དབྱེ།:Category:ནང་བསྟན།]]``.
    """
    cleaned = _clean(name).strip("[]").strip()
    for prefix in (CATEGORY_NAMESPACE + ":", CATEGORY_NAMESPACE_ALIAS + ":"):
        if cleaned.lower().startswith(prefix.lower()):
            cleaned = cleaned[len(prefix) :].strip()
    if not cleaned:
        raise ValueError("category name must be non-empty")
    return f"[[{CATEGORY_NAMESPACE}:{cleaned}]]"


def format_bibliography_entry(citation: Citation) -> str:
    """``AUTHOR། TITLE། YEAR།`` — the ``དཔྱད་གཞིའི་ཡིག་ཆ།`` line for a source.

    The year lives here rather than in the ref itself: the canonical ref form
    in wikitext-spec.md §2 has no year slot, but topic 324 rule ༦ still wants
    the year recorded, and the bibliography is where the reader finds it.
    """
    parts = [
        part
        for part in (
            _with_shad(citation.author),
            _with_shad(citation.title),
            _with_shad(citation.year),
        )
        if part
    ]
    if not parts:
        raise ValueError(
            f"citation {citation.source_id!r} has no author, title or year to list"
        )
    return " ".join(parts)


def _bullet(entry: str) -> str:
    text = _clean(entry)
    return text if text.startswith("*") else f"* {text}"


def render_article(article: Article) -> str:
    """Render a complete article in the canonical skeleton.

    Three emission rules are load-bearing, all from wikitext-spec.md:

    * a section with no citation is dropped, never invented (§1, rule 10 of the
      27-rule prompt) — the drafting model over-produces empty ``དབྱེ་བ།``
      sections and this is where they die;
    * the reference display is ``<references />``, never ``{{Reflist}}`` (§2);
    * it is emitted *iff* the article actually has a ``<ref>`` (rule V3), so we
      never add the ~600th orphaned-footnote article to bo.wikipedia — nor an
      empty reference section.
    """
    blocks: list[str] = []

    lead_paragraphs = tuple(article.lead)
    blocks.append(render_lead(article.term, lead_paragraphs[0] if lead_paragraphs else ""))
    blocks.extend(lead_paragraphs[1:])

    for section in article.sections:
        if not section.has_citation:
            continue
        blocks.append(render_section(section))

    if article.see_also:
        links = [
            entry if entry.startswith("[[") else render_wikilink(entry)
            for entry in article.see_also
        ]
        blocks.append(
            render_heading(HEADING_SEE_ALSO)
            + "\n"
            + "\n".join(_bullet(link) for link in links)
        )

    if REF_TAG_RE.search("\n\n".join(blocks)):
        blocks.append(render_heading(HEADING_REFERENCES) + "\n" + REFERENCES_TAG)

    if article.bibliography:
        blocks.append(
            render_heading(HEADING_BIBLIOGRAPHY)
            + "\n"
            + "\n".join(_bullet(entry) for entry in article.bibliography)
        )

    if article.categories:
        blocks.append("\n".join(render_category(name) for name in article.categories))

    return _nfc("\n\n".join(blocks))
