"""The source and key-term registry — typed, queryable, version-controlled.

The OpenPecha Wiki Working Group maintains its authoritative list of texts and
key terms in a Google Sheet with one tab per text project.  That sheet is the
ground truth for two things the pipeline cannot invent: **which edition of a
source a citation must point at**, and **which terms a human editor has already
claimed, drafted or published**.  This module turns an export of that sheet
into dataclasses, and writes it back out as YAML that lives in the repo at
``corpora/<id>/sources.yaml`` and ``corpora/<id>/terms.yaml`` — so the pipeline
reads a reviewed file under version control, never a live spreadsheet.

Three properties of the real sheet drive the design:

**URLs live in hyperlink relations, not cell text.**  A cell reading ``Link``
carries the URL in the XLSX relationship table.  Nothing can be parsed from the
visible values alone, so the loader takes two artifacts — cell text and a
``cell-ref -> URL`` map — and merges them.  Google Sheets also rewrites external
links through ``https://www.google.com/url?q=...``; those are unwrapped.

**Columns mean different things in different bands of the same tab.**  The
སྤྱོད་འཇུག tab lists its sources twice under one header — once with Drive
scans, once with Wikisource uploads — and column ``F`` is a Drive URL in the
first band and a Wikisource *index* URL in the second.  So link fields are
resolved by **classifying the URL**, not by trusting the column, while the
prose fields (title, author) are resolved from the header row with a positional
fallback.

**The source block and the term block are stacked in one sheet, with repeated
headers between them.**  Where they divide is inferred (see
``find_split_index``) and the result is recorded on the ``Registry`` so a human
who disagrees can pin it with ``split_index=``.

And one hazard that is invisible until you look for it: the cell-text export
**omits blank rows** while the hyperlink refs keep true spreadsheet numbering.
In the སྤྱོད་འཇུག tab the two drift apart by 0, then 2, then 6 rows, so a naive
``rows[n-1]`` join files 489 of the 546 terms' articles under the wrong term —
silently, and in a way that looks entirely plausible.  ``align_link_rows``
recovers the mapping before anything is read.  See its docstring.

Nothing here touches the network, and nothing edits Tibetan punctuation in
stored values: a tsheg or shad in a title is orthography, and the emitter
downstream needs it exactly as the editors wrote it.
"""

from __future__ import annotations

import json
import os
import re
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import yaml

from kangyur_wiki.ledger import atomic_write_text
from kangyur_wiki.tibetan.normalize import DOUBLE_SHAD, SHAD, TSHEG, TSHEG_NB, nfc, syllables

__all__ = [
    "SOURCES_FILENAME",
    "TERMS_FILENAME",
    "REGISTRY_VERSION",
    "Source",
    "TermRecord",
    "Registry",
    "align_link_rows",
    "bdrc_show_url",
    "classify_url",
    "find_split_index",
    "find_term",
    "iter_terms",
    "load",
    "load_from_xlsx_export",
    "resolve_citation_url",
    "save",
    "term_key",
    "unwrap_google_redirect",
]

#: The two human-editable files that make up a corpus registry (PLAN.md §2).
SOURCES_FILENAME = "sources.yaml"
TERMS_FILENAME = "terms.yaml"

#: Schema version stamped into both YAML files.
REGISTRY_VERSION = 1

_TERMINAL_PUNCTUATION = (TSHEG, TSHEG_NB, SHAD, DOUBLE_SHAD)

#: Tibetan *letters* — U+0F40..U+0FBC.  Deliberately excludes the Tibetan
#: digits (U+0F20..U+0F29) and marks, so a chapter-number cell like ``༧༽``
#: is not mistaken for a term.
_TIBETAN_LETTER_RE = re.compile(r"[ཀ-ྼ]")

#: A bare spreadsheet ordinal.  The export renders integers as floats, so
#: ``1`` arrives as ``"1.0"``.
_ORDINAL_RE = re.compile(r"^\d+(?:\.\d+)?$")

#: BDRC work identifiers as they appear in the sheet: ``WA0RK0529``,
#: ``WA0XL1DFCB8785C27``, ``W1KG24246``, ``MW22276``.  Derge/Tohoku numbers
#: (``D3871``) deliberately do **not** match — they are catalogue numbers, not
#: BDRC resources, and ``bdr:D3871`` resolves to nothing.
_BDRC_ID_RE = re.compile(r"\b(?:MW|W)[A-Z0-9]{4,}\b")

#: Cell values that are link *labels* rather than data.
_LINK_LABELS = frozenset({"link", "links", "url", "wikilink"})

#: Where a work title stops being a key term, measured in ཚེག་བར — the unit
#: the team's own prompts use (forum topic 289-v3 asks for terms of 3–4).  Six
#: is comfortably above the longest observed term and below the shortest
#: observed multi-word title.  One threshold, not two, so the source test and
#: the term test are exact complements and no row can score as both.
_SOURCE_TITLE_MIN_SYLLABLES = 6
#: A term row is narrow (number, term, editor, status, link); a source row is
#: wide (up to 18 columns of edition metadata).
_TERM_MAX_CELLS = 8

#: Header-row vocabulary, role -> substrings matched case-insensitively against
#: a cell's text.  Drawn from every tab of the real sheet; the Tibetan and the
#: English labels are both live, sometimes in the same cell
#: (``"གནས་བབ། Status"``).
_HEADER_KEYWORDS: dict[str, tuple[str, ...]] = {
    "ordinal": ("ཨང་།", "sr.no", "sr no", "s.no"),
    "title": ("མཚན་བྱང", "title"),
    "author": ("མཛད་པ་པོ", "author"),
    "collection": ("གཞུང་ཁོངས",),
    "version": ("པར་རིགས", "པར་མ", "version"),
    "catalog": ("ནང་བསྟན་དཔེ་ཚོགས་ཨང",),
    "term": ("གནད་ཚིག",),
    "editor": ("རྩོམ་སྒྲིག་མཁན", "ལས་ཀ་བྱེད་མཁན", "editor"),
    "status": ("གནས་བབ", "status"),
    "link": ("དྲ་ཐག", "དྲྭ་ཐག", "link", "url"),
    "proofreading": ("proofreading",),
}

#: Any of these in a row makes it a header, if the row also carries no URL.
_HEADER_HINT_COUNT = 2


# --------------------------------------------------------------------------
# Tibetan-aware term identity
# --------------------------------------------------------------------------


def term_key(text: str) -> str:
    """Matching key for a Tibetan term: NFC, trimmed, terminal tsheg/shad removed.

    The sheet writes the same term as ``བྱང་ཆུབ་སེམས་`` in the term list and
    ``བྱང་ཆུབ་སེམས།`` in an article title, because a citation form takes a shad
    and a bare lemma takes a tsheg.  They are one term and must resolve to one
    ledger row.

    Deliberately *not* ``tibetan.normalize.fuzzy_key``, which drops every tsheg
    and shad everywhere: that would fold ``ཆོས་སྐུ`` and ``ཆོསསྐུ`` together and
    make distinct terms collide.  Only the trailing delimiter is ambiguous, so
    only the trailing delimiter is dropped.
    """
    stripped = nfc(text).strip()
    while stripped and stripped[-1] in _TERMINAL_PUNCTUATION:
        stripped = stripped[:-1].rstrip()
    return stripped


def _tibetan_syllable_count(text: str) -> int:
    """ཚེག་བར count, ignoring units that carry no Tibetan letter."""
    return sum(1 for unit in syllables(text) if _TIBETAN_LETTER_RE.search(unit))


def _has_tibetan_letter(text: str) -> bool:
    return _TIBETAN_LETTER_RE.search(text) is not None


# --------------------------------------------------------------------------
# URLs
# --------------------------------------------------------------------------


def unwrap_google_redirect(url: str, *, max_hops: int = 3) -> str:
    """Strip the ``https://www.google.com/url?q=...`` wrapper Sheets adds.

    Google Sheets rewrites every external hyperlink through its own redirector
    and percent-encodes the target a second time on the way.  Left wrapped,
    558 of the 613 links in the སྤྱོད་འཇུག tab would be recorded as
    ``www.google.com`` URLs and every citation built from them would be dead
    the day Google retires the redirector.  Query parsing undoes the extra
    encoding layer for free.

    Bounded loop rather than plain recursion: a hand-pasted double wrap is
    real, an infinite one is not, and this must not hang on malformed input.
    """
    current = url.strip()
    for _ in range(max_hops):
        parsed = urllib.parse.urlsplit(current)
        if parsed.netloc.lower() not in {"www.google.com", "google.com"}:
            return current
        if not parsed.path.rstrip("/").endswith("/url"):
            return current
        query = urllib.parse.parse_qs(parsed.query)
        target = (query.get("q") or query.get("url") or [""])[0]
        if not target:
            return current
        current = target
    return current


def classify_url(url: str) -> str:
    """Bucket a URL by what it is, ignoring which column it came from.

    Returns one of ``wikisource_index``, ``wikisource_text``, ``commons``,
    ``wikidata``, ``wikipedia``, ``wikipedia_redlink``, ``drive``, ``bdrc``,
    ``other``.

    ``wikipedia_redlink`` is its own kind and it matters: 26 of the སྤྱོད་འཇུག
    term links are ``/w/index.php?title=...&action=edit&redlink=1``, which is
    what a *red* link resolves to — the article does **not** exist.  Filed as a
    plain ``wikipedia`` URL it would set ``exists_on_wiki`` on 26 terms that
    have never been written, and send each of them down the update path instead
    of the create path.

    Column position is unreliable in this sheet — the same column holds a Drive
    scan in one band of rows and a Wikisource index in the next — so the URL
    itself is the only trustworthy signal.  ``Index:`` in the path is what
    separates a Wikisource *index* (the scanned-page container, which is what a
    reader wants for provenance) from the transcribed *text*.

    Commons and Wikisource ``Special:`` pages classify as ``other``: the sheet
    uses ``Special:UploadWizard`` as a to-do marker, and a citation pointing at
    an upload form is worse than no link at all.
    """
    resolved = unwrap_google_redirect(url)
    parsed = urllib.parse.urlsplit(resolved)
    host = parsed.netloc.lower()
    path = urllib.parse.unquote(parsed.path)
    query = urllib.parse.parse_qs(parsed.query)
    title = query.get("title", [""])[0]
    target = title or path

    if host.endswith("wikisource.org"):
        if "Special:" in target:
            return "other"
        if "Index:" in target:
            return "wikisource_index"
        if not target.strip("/"):
            return "other"
        return "wikisource_text"
    if host.endswith("commons.wikimedia.org"):
        return "commons" if "File:" in target else "other"
    if host.endswith("wikidata.org"):
        return "wikidata"
    if host.endswith("wikipedia.org"):
        if target.strip("/") in {"", "wiki"}:
            return "other"
        if "1" in query.get("redlink", []) or "edit" in query.get("action", []):
            return "wikipedia_redlink"
        return "wikipedia"
    if host in {"drive.google.com", "docs.google.com"}:
        return "drive"
    if host.endswith("bdrc.io"):
        return "bdrc"
    return "other"


def _wikidata_id(url: str) -> str | None:
    """Pull ``Q12345`` out of a Wikidata URL."""
    match = re.search(r"\b(Q\d+)\b", unwrap_google_redirect(url))
    return match.group(1) if match else None


def bdrc_show_url(bdrc_id: str) -> str:
    """The public BDRC viewer URL for a work id.

    Used as a citation fallback when a source has reached BDRC but not
    Wikisource — which is most of the Tengyur commentaries today.
    """
    return f"https://library.bdrc.io/show/bdr:{bdrc_id.strip()}"


def _looks_like_url(value: str) -> bool:
    return value.strip().lower().startswith(("http://", "https://"))


# --------------------------------------------------------------------------
# Dataclasses
# --------------------------------------------------------------------------


@dataclass
class Source:
    """One text the pipeline may cite.

    ``source_id`` encodes the spreadsheet row it came from (``spyodjug-s003``
    = row 3), so a value a human questions can be traced back to the cell that
    produced it.  ``local_path`` is the ingested file under
    ``corpora/<id>/source/`` and is filled in by the ingest stage, not by the
    sheet — the sheet knows nothing about this machine.
    """

    source_id: str
    title: str
    author: str | None = None
    collection: str | None = None
    version: str | None = None
    bdrc_id: str | None = None
    wikisource_index_url: str | None = None
    wikisource_text_url: str | None = None
    commons_url: str | None = None
    wikidata_id: str | None = None
    wikipedia_url: str | None = None
    status: str | None = None
    local_path: Path | None = None
    # Canonical-pipeline metadata (docs/reference/cowork-pipeline.md step 1). ``copyright``
    # is a router, not a gate: it decides where a reader verifies the text (Wikisource vs a
    # BDRC/WeBuddhist link), never whether it may be cited. ``school`` feeds the claims
    # stage's attribution rules; leave it empty rather than guessing.
    school: str | None = None
    copyright: str | None = None
    author_dates: str | None = None
    webuddhist_url: str | None = None
    # The vault's 2-RAILS/Claims/ short id for this same source (e.g. "karma-maitri"),
    # so a source can be traced to its claims files and its 1-SOURCES/ frontmatter
    # without re-deriving the id from local_path. Optional: a corpus that predates the
    # vault-native registry (or has no rails-side claims work yet) leaves this unset.
    registered_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """YAML-ready form; ``None`` fields are kept so the file doubles as a
        template showing an editor which slots are still empty."""
        return {
            "source_id": self.source_id,
            "title": self.title,
            "author": self.author,
            "collection": self.collection,
            "version": self.version,
            "bdrc_id": self.bdrc_id,
            "wikisource_index_url": self.wikisource_index_url,
            "wikisource_text_url": self.wikisource_text_url,
            "commons_url": self.commons_url,
            "wikidata_id": self.wikidata_id,
            "wikipedia_url": self.wikipedia_url,
            "status": self.status,
            "local_path": str(self.local_path) if self.local_path is not None else None,
            "school": self.school,
            "copyright": self.copyright,
            "author_dates": self.author_dates,
            "webuddhist_url": self.webuddhist_url,
            "registered_id": self.registered_id,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Source":
        local = data.get("local_path")
        return cls(
            source_id=str(data["source_id"]),
            title=str(data.get("title") or ""),
            author=_clean_optional(data.get("author")),
            collection=_clean_optional(data.get("collection")),
            version=_clean_optional(data.get("version")),
            bdrc_id=_clean_optional(data.get("bdrc_id")),
            wikisource_index_url=_clean_optional(data.get("wikisource_index_url")),
            wikisource_text_url=_clean_optional(data.get("wikisource_text_url")),
            commons_url=_clean_optional(data.get("commons_url")),
            wikidata_id=_clean_optional(data.get("wikidata_id")),
            wikipedia_url=_clean_optional(data.get("wikipedia_url")),
            status=_clean_optional(data.get("status")),
            local_path=Path(str(local)) if local else None,
            school=_clean_optional(data.get("school")),
            copyright=_clean_optional(data.get("copyright")),
            author_dates=_clean_optional(data.get("author_dates")),
            webuddhist_url=_clean_optional(data.get("webuddhist_url")),
            registered_id=_clean_optional(data.get("registered_id")),
        )


@dataclass
class TermRecord:
    """One key term as the editors track it.

    ``wikipedia_url`` present means an editor has already published or claimed
    an article: the pipeline's update path applies, not the create path.  The
    team uses blue-vs-red links as its own existence check, and this field is
    the machine-readable form of that check — which is why a *red* link
    (``&redlink=1``) leaves it ``None``.  A red link is the sheet saying the
    article is still missing.
    """

    term: str
    editor: str | None = None
    status: str | None = None
    wikipedia_url: str | None = None

    @property
    def exists_on_wiki(self) -> bool:
        """Whether the sheet records a bo.wikipedia article for this term.

        Derived, never stored: a stale boolean next to a live URL is a bug
        waiting to be believed.
        """
        return bool(self.wikipedia_url)

    @property
    def key(self) -> str:
        """Tsheg/shad-insensitive identity — see ``term_key``."""
        return term_key(self.term)

    def to_dict(self) -> dict[str, Any]:
        return {
            "term": self.term,
            "editor": self.editor,
            "status": self.status,
            "wikipedia_url": self.wikipedia_url,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TermRecord":
        return cls(
            term=nfc(str(data.get("term") or "")).strip(),
            editor=_clean_optional(data.get("editor")),
            status=_clean_optional(data.get("status")),
            wikipedia_url=_clean_optional(data.get("wikipedia_url")),
        )


@dataclass
class Registry:
    """Everything one corpus knows about its sources and its key terms.

    ``split_index`` records where the loader decided the source block ended, in
    0-based row-list terms.  It is carried on the registry rather than thrown
    away because the decision is a heuristic on human-maintained data, and the
    person reviewing ``sources.yaml`` needs to see the number they may have to
    override.
    """

    sources: list[Source] = field(default_factory=list)
    terms: list[TermRecord] = field(default_factory=list)
    corpus_name: str = ""
    corpus_id: str | None = None
    split_index: int | None = None

    def source(self, source_id: str) -> Source | None:
        """Look up one source by id."""
        for candidate in self.sources:
            if candidate.source_id == source_id:
                return candidate
        return None

    def term_index(self) -> dict[str, TermRecord]:
        """``term_key`` -> record.  First occurrence wins on a duplicated term."""
        index: dict[str, TermRecord] = {}
        for record in self.terms:
            index.setdefault(record.key, record)
        return index


def _clean_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = nfc(str(value)).strip()
    return text or None


# --------------------------------------------------------------------------
# Spreadsheet parsing
# --------------------------------------------------------------------------


def _column_index(letter: str) -> int:
    """``A`` -> 0, ``Z`` -> 25, ``AA`` -> 26.  Sorts cells into visual order."""
    index = 0
    for char in letter.strip().upper():
        if not "A" <= char <= "Z":
            return index
        index = index * 26 + (ord(char) - ord("A") + 1)
    return index - 1


def _sorted_cells(row: Mapping[str, str]) -> list[tuple[str, str]]:
    """Row cells as ``(column letter, text)`` in left-to-right order."""
    return sorted(
        ((str(col), (value or "").strip()) for col, value in row.items() if (value or "").strip()),
        key=lambda pair: _column_index(pair[0]),
    )


def _is_header_label(value: str) -> bool:
    """Whether a cell reads like a column heading.

    A cell whose *whole* text is ``Link`` does not count, however much the
    header vocabulary mentions links: bare ``Link`` is the clickable label on a
    data row, and counting it would turn every source row whose URLs live
    entirely in hyperlink relations into a header — silently deleting it.
    Real heading cells say ``Wikisource Link`` or ``ཝེ་ཁེ་རིག་མཛོད་ཀྱི་དྲ་ཐག
    Link``, never ``Link`` alone.
    """
    lowered = value.strip().lower()
    if lowered in _LINK_LABELS:
        return False
    for keywords in _HEADER_KEYWORDS.values():
        if any(keyword.lower() in lowered for keyword in keywords):
            return True
    return False


def _is_header_row(row: Mapping[str, str]) -> bool:
    """Whether a row is a column-heading row rather than data.

    Headers repeat mid-sheet — the སྤྱོད་འཇུག tab has one at row 1 for the
    sources and another at row 17 for the terms — so this cannot be
    "row 1 only".  Two independent label hits and no URL anywhere is the test:
    data rows carry links, and a data row that happens to contain one label-ish
    word will not contain two.
    """
    cells = _sorted_cells(row)
    if not cells:
        return False
    if any(_looks_like_url(value) for _, value in cells):
        return False
    hits = sum(1 for _, value in cells if _is_header_label(value))
    return hits >= _HEADER_HINT_COUNT


def _roles_from_header(row: Mapping[str, str]) -> dict[str, str]:
    """Map role name -> column letter from a header row.

    Longest keyword first so ``ནང་བསྟན་དཔེ་ཚོགས་ཨང་།`` (a BDRC catalogue
    column) is not claimed by ``ཨང་།`` (the row-number column), and first
    column wins for a role the sheet repeats — the སྤྱོད་འཇུག source header
    has two ``Status`` columns and the left one is the article's.
    """
    roles: dict[str, str] = {}
    for column, value in _sorted_cells(row):
        lowered = value.lower()
        matches = [
            (len(keyword), role)
            for role, keywords in _HEADER_KEYWORDS.items()
            for keyword in keywords
            if keyword.lower() in lowered
        ]
        if not matches:
            continue
        matches.sort(reverse=True)
        role = matches[0][1]
        roles.setdefault(role, column)
    return roles


def _row_urls(
    row: Mapping[str, str], links: Mapping[str, str], row_number: int
) -> dict[str, str]:
    """Column letter -> URL for one row, merging hyperlink relations and cell text.

    The relation wins where both exist: a cell reading ``Link`` has its real
    target only in the relation, and a cell that shows a URL as text sometimes
    *also* carries a different, live hyperlink.
    """
    urls: dict[str, str] = {}
    for column, value in _sorted_cells(row):
        if _looks_like_url(value):
            urls[column] = unwrap_google_redirect(value)
    # Sweeping the link table by row number, rather than probing `f"{col}{n}"`
    # for the columns present in `row`, also catches a hyperlink on a cell with
    # no visible text — an empty-looking cell that is in fact a link, which the
    # cell-text export omits entirely.
    for ref, target in links.items():
        column, number = _split_cell_ref(ref)
        if column and number == row_number and target:
            urls[column] = unwrap_google_redirect(target)
    return dict(sorted(urls.items(), key=lambda pair: _column_index(pair[0])))


def _split_cell_ref(ref: str) -> tuple[str, int]:
    """``"E24"`` -> ``("E", 24)``.  Returns ``("", 0)`` on a malformed ref."""
    match = re.fullmatch(r"\$?([A-Za-z]+)\$?(\d+)", ref.strip())
    if not match:
        return ("", 0)
    return (match.group(1).upper(), int(match.group(2)))


def _links_by_row(links: Mapping[str, str]) -> dict[int, dict[str, str]]:
    """``{"E24": url}`` -> ``{24: {"E": url}}``, redirect wrappers already stripped."""
    grouped: dict[int, dict[str, str]] = {}
    for ref, target in links.items():
        column, number = _split_cell_ref(ref)
        if column and number and target:
            grouped.setdefault(number, {})[column] = unwrap_google_redirect(target)
    return grouped


def _wiki_title(url: str) -> str | None:
    """The article title a Wikipedia URL names, percent-decoded.

    Handles both the pretty form (``/wiki/<title>``) and the red-link form
    (``/w/index.php?title=<title>&redlink=1``).  Red links anchor row
    alignment just as well as blue ones — the title is right there either way,
    and excluding them would throw away 26 of the term block's anchors.
    """
    parsed = urllib.parse.urlsplit(url)
    if not parsed.netloc.lower().endswith("wikipedia.org"):
        return None
    path = urllib.parse.unquote(parsed.path)
    if path.startswith("/wiki/"):
        return path[len("/wiki/") :].strip() or None
    title = urllib.parse.parse_qs(parsed.query).get("title", [""])[0].strip()
    return title or None


#: Weight of an anchor whose evidence is an exact URL match — near-certain.
_ANCHOR_WEIGHT_URL = 3
#: Weight of an anchor whose evidence is "this link's article title is one of
#: this row's cell values" — individually weak (two rows can name the same
#: article) but decisive in bulk.
_ANCHOR_WEIGHT_TITLE = 1
#: Largest drift the aligner will consider, in rows.  Bounds the search and
#: stops a coincidental match hundreds of rows away from being believed.
_MAX_ROW_DRIFT = 64


def _collect_anchors(
    rows: Sequence[Mapping[str, str]], by_row: Mapping[int, Mapping[str, str]]
) -> dict[int, dict[int, int]]:
    """``{data index: {offset: total weight}}`` — evidence for how far each row drifted."""
    anchors: dict[int, dict[int, int]] = {}

    def add(index: int, sheet_row: int, weight: int) -> None:
        offset = sheet_row - (index + 1)
        if 0 <= offset <= _MAX_ROW_DRIFT:
            anchors.setdefault(index, {}).setdefault(offset, 0)
            anchors[index][offset] += weight

    url_owners: dict[tuple[str, str], list[int]] = {}
    title_owners: dict[str, list[int]] = {}
    for sheet_row, columns in by_row.items():
        for column, url in columns.items():
            url_owners.setdefault((column, url), []).append(sheet_row)
            title = _wiki_title(url)
            if title:
                title_owners.setdefault(term_key(title), []).append(sheet_row)

    for index, row in enumerate(rows):
        for column, value in _sorted_cells(row):
            if _looks_like_url(value):
                for sheet_row in url_owners.get((column, unwrap_google_redirect(value)), ()):
                    add(index, sheet_row, _ANCHOR_WEIGHT_URL)
            key = term_key(value)
            if key:
                for sheet_row in title_owners.get(key, ()):
                    add(index, sheet_row, _ANCHOR_WEIGHT_TITLE)
    return anchors


def align_link_rows(
    rows: Sequence[Mapping[str, str]], links: Mapping[str, str]
) -> list[int]:
    """Spreadsheet row number for each exported row — undoing the blank-row drift.

    **Why this is needed.**  The cell-text export lists only non-empty rows,
    while hyperlink refs (``E24``) carry the *true* spreadsheet row number.
    Every blank row in the sheet therefore pushes the two apart, permanently
    and cumulatively.  In the སྤྱོད་འཇུག tab the drift is 0 for the first
    sources, 2 for the rest, and 6 for the whole term block — so joining on
    ``rows[n - 1]`` gives 489 terms a link belonging to a term six rows away.
    The result looks perfectly reasonable and is wrong, which is the worst
    kind of wrong for a citation registry.

    **How it is recovered.**  Two kinds of evidence tie an exported row to a
    sheet row: a cell whose *text* is a URL that also appears as a hyperlink in
    the same column (near-certain), and a cell value that equals the article
    title of some hyperlink in the row (individually weak — two rows can point
    at the same article — but there are 489 of them in a row for the term
    block).

    Drift can only ever grow, because rows are dropped and never inserted.  So
    the answer is the non-decreasing offset sequence that explains the most
    anchor weight, which a linear-time dynamic program finds exactly.  A
    handful of spurious title matches near the top of the sheet cannot
    outvote seven exact URL anchors, and one weak-but-unanimous run of 489
    cannot be outvoted by anything.

    Returns ``[1, 2, 3, ...]`` when there is no drift or no evidence of any,
    which is the correct answer for a well-formed export.
    """
    by_row = _links_by_row(links)
    if not by_row or not rows:
        return [index + 1 for index in range(len(rows))]

    anchors = _collect_anchors(rows, by_row)
    candidates = sorted({0} | {offset for row in anchors.values() for offset in row})
    if candidates == [0]:
        return [index + 1 for index in range(len(rows))]

    # best[j] = most anchor weight explainable by a non-decreasing offset
    # sequence over rows[:i+1] that ends at candidates[j].
    best = [0] * len(candidates)
    choices: list[list[int]] = []
    for index in range(len(rows)):
        weights = anchors.get(index, {})
        updated = [0] * len(candidates)
        picks = [0] * len(candidates)
        running_best = -1
        running_arg = 0
        for j, offset in enumerate(candidates):
            if best[j] > running_best:
                running_best = best[j]
                running_arg = j
            updated[j] = running_best + weights.get(offset, 0)
            picks[j] = running_arg
        best = updated
        choices.append(picks)

    end = max(range(len(candidates)), key=lambda j: best[j])
    trail = [0] * len(rows)
    for index in range(len(rows) - 1, -1, -1):
        trail[index] = candidates[end]
        end = choices[index][end]
    return [index + 1 + offset for index, offset in enumerate(trail)]


def _urls_by_kind(urls: Mapping[str, str]) -> dict[str, list[str]]:
    """Group a row's URLs by ``classify_url``, preserving column order."""
    grouped: dict[str, list[str]] = {}
    for _, url in sorted(urls.items(), key=lambda pair: _column_index(pair[0])):
        grouped.setdefault(classify_url(url), []).append(url)
    return grouped


def _lead_field_syllables(row: Mapping[str, str]) -> int | None:
    """ཚེག་བར count of the row's *first* prose cell, or ``None`` if it has none.

    The first prose cell is the discriminating one: a source row leads with a
    long work title, a term row leads with a short lemma.  Later cells are not
    — a source row's ``གཞུང་ཁོངས།`` is as short as any term.
    """
    for _, value in _sorted_cells(row):
        if _is_field_text(value):
            return _tibetan_syllable_count(value)
    return None


def _source_score(row: Mapping[str, str], grouped: Mapping[str, list[str]]) -> int:
    """How much this row looks like a source row.  See ``find_split_index``."""
    score = 0
    if {"wikisource_index", "wikisource_text", "commons", "drive", "bdrc"} & set(grouped):
        score += 2
    if any(_BDRC_ID_RE.search(value) for _, value in _sorted_cells(row)):
        score += 1
    lead = _lead_field_syllables(row)
    if lead is not None and lead >= _SOURCE_TITLE_MIN_SYLLABLES:
        score += 2
    return score


def _term_score(row: Mapping[str, str], grouped: Mapping[str, list[str]]) -> int:
    """How much this row looks like a key-term row.  See ``find_split_index``."""
    cells = _sorted_cells(row)
    score = 0
    lead = _lead_field_syllables(row)
    if lead is not None and 1 <= lead < _SOURCE_TITLE_MIN_SYLLABLES:
        score += 2
    if any(value.strip().lower() in _LINK_LABELS for _, value in cells):
        score += 1
    if {"wikipedia", "wikipedia_redlink"} & set(grouped):
        score += 1
    if len(cells) <= _TERM_MAX_CELLS:
        score += 1
    return score


def find_split_index(
    rows: Sequence[Mapping[str, str]],
    links: Mapping[str, str] | None = None,
    *,
    sheet_rows: Sequence[int] | None = None,
) -> int:
    """Index of the first term row — where the source block ends.

    **The heuristic.**  Each row gets a *lean*: how much it looks like a source
    row minus how much it looks like a term row.

    ``source`` +2 for carrying a Wikisource / Commons / Drive / BDRC link, +1
    for a BDRC work id anywhere in the row, +2 for leading with a prose cell of
    at least six ཚེག་བར.

    ``term`` +2 for leading with a prose cell shorter than that, +1 for a cell
    whose whole text is the word ``Link``, +1 for a bo.wikipedia link, +1 for
    being a narrow row (≤8 cells).

    The *leading* prose cell is what separates the two: a source row opens with
    a work title, a term row with a lemma, while both are full of short cells
    further right (``བོད་གཞུང་།``, ``ཤིང་དཔར།``) — a bare "has a short cell"
    test fires on everything.

    Header rows lean 0 — they are not evidence either way, which is what lets
    the repeated mid-sheet header sit harmlessly on the boundary.

    The split is then the changepoint that maximises ``sum(lean before) -
    sum(lean after)``: the single cut that puts as much source-leaning weight
    as possible above it and term-leaning weight below.  A changepoint, rather
    than "first row that looks like a term", because the bands are ragged —
    row 16 of the སྤྱོད་འཇུག tab has four cells and no ordinal, and a
    first-match rule would cut there.

    Ties resolve to the earliest index, which puts a boundary header row in
    the term block where it is skipped anyway.

    ``sheet_rows`` is the output of ``align_link_rows``; pass it to avoid
    recomputing the alignment, or leave it out and this computes its own.
    """
    links = links or {}
    numbering = list(sheet_rows) if sheet_rows is not None else align_link_rows(rows, links)
    leans: list[int] = []
    for offset, row in enumerate(rows):
        if _is_header_row(row):
            leans.append(0)
            continue
        grouped = _urls_by_kind(_row_urls(row, links, numbering[offset]))
        leans.append(_source_score(row, grouped) - _term_score(row, grouped))

    total = sum(leans)
    best_index = 0
    best_value = -total  # prefix empty: 0 - total
    running = 0
    for index, lean in enumerate(leans, start=1):
        running += lean
        value = running - (total - running)
        if value > best_value:
            best_value = value
            best_index = index
    return best_index


def _is_field_text(value: str) -> bool:
    """Whether a cell holds a prose field (title, author, term) rather than furniture.

    Excludes URLs, bare ordinals like ``"1.0"``, the literal label ``Link``,
    and anything with no Tibetan letter — which is what keeps a chapter marker
    ``༧༽`` or an edition code ``S6`` out of the author slot.
    """
    text = value.strip()
    if not text or _looks_like_url(text):
        return False
    if _ORDINAL_RE.fullmatch(text):
        return False
    if text.lower() in _LINK_LABELS:
        return False
    return _has_tibetan_letter(text)


def _pick_fields(
    row: Mapping[str, str], roles: Mapping[str, str], wanted: Sequence[Sequence[str]]
) -> list[str | None]:
    """Resolve prose fields by header role, falling back to left-to-right position.

    ``wanted`` is one tuple of acceptable role names per output field, in
    preference order — ``("term", "title")`` means "the column the header calls
    a key term, or failing that the one it calls a title".  The fallback exists
    because several tabs have no header over their term block at all, and
    because the same header sits above two bands of rows with different
    meanings; a role that resolves to an empty cell must not shadow the value
    that is plainly there.
    """
    used: set[str] = set()
    values: list[str | None] = []
    for role_names in wanted:
        found: str | None = None
        for role in role_names:
            column = roles.get(role)
            if not column or column in used:
                continue
            text = (row.get(column) or "").strip()
            if _is_field_text(text):
                found = nfc(text)
                used.add(column)
                break
        values.append(found)

    remaining = iter(
        [(col, val) for col, val in _sorted_cells(row) if col not in used and _is_field_text(val)]
    )
    for position, value in enumerate(values):
        if value is not None:
            continue
        for column, text in remaining:
            values[position] = nfc(text)
            used.add(column)
            break
    return values


def _build_source(
    row: Mapping[str, str],
    urls: Mapping[str, str],
    roles: Mapping[str, str],
    *,
    corpus_id: str,
    row_number: int,
) -> Source | None:
    """One source row -> ``Source``, or ``None`` if the row has no title."""
    title, author, collection, version = _pick_fields(
        row, roles, [("title",), ("author",), ("collection",), ("version",)]
    )
    if not title:
        return None

    grouped = _urls_by_kind(urls)
    bdrc_id: str | None = None
    catalog_column = roles.get("catalog")
    if catalog_column:
        match = _BDRC_ID_RE.search(row.get(catalog_column) or "")
        if match:
            bdrc_id = match.group(0)
    if bdrc_id is None:
        for _, value in _sorted_cells(row):
            match = _BDRC_ID_RE.search(value)
            if match:
                bdrc_id = match.group(0)
                break
    if bdrc_id is None:
        for url in grouped.get("bdrc", []):
            match = _BDRC_ID_RE.search(urllib.parse.unquote(url))
            if match:
                bdrc_id = match.group(0)
                break

    wikidata_id: str | None = None
    for url in grouped.get("wikidata", []):
        wikidata_id = _wikidata_id(url)
        if wikidata_id:
            break

    status: str | None = None
    status_column = roles.get("status")
    if status_column:
        candidate = (row.get(status_column) or "").strip()
        if candidate and not _looks_like_url(candidate):
            status = nfc(candidate)

    return Source(
        source_id=f"{corpus_id}-s{row_number:03d}",
        title=title,
        author=author,
        collection=collection,
        version=version,
        bdrc_id=bdrc_id,
        wikisource_index_url=_first(grouped.get("wikisource_index")),
        wikisource_text_url=_first(grouped.get("wikisource_text")),
        commons_url=_first(grouped.get("commons")),
        wikidata_id=wikidata_id,
        wikipedia_url=_first(grouped.get("wikipedia")),
        status=status,
        local_path=None,
    )


def _build_term(
    row: Mapping[str, str], urls: Mapping[str, str], roles: Mapping[str, str]
) -> TermRecord | None:
    """One term row -> ``TermRecord``, or ``None`` if the row has no term."""
    term, editor, status = _pick_fields(
        row, roles, [("term", "title"), ("editor", "author"), ("status",)]
    )
    if not term:
        return None
    grouped = _urls_by_kind(urls)
    return TermRecord(
        term=term,
        editor=editor,
        status=status,
        wikipedia_url=_first(grouped.get("wikipedia")),
    )


def _first(values: Sequence[str] | None) -> str | None:
    return values[0] if values else None


def _as_mapping(value: Any, *, what: str) -> Mapping[str, Any]:
    """Accept an already-parsed JSON document or a path to one."""
    if isinstance(value, Mapping):
        return value
    if isinstance(value, (str, os.PathLike)):
        return json.loads(Path(value).read_text(encoding="utf-8"))
    raise TypeError(f"{what} must be a mapping or a path to a JSON file, got {type(value)!r}")


def load_from_xlsx_export(
    registry_json: Mapping[str, Any] | str | os.PathLike[str],
    hyperlinks_json: Mapping[str, Any] | str | os.PathLike[str],
    tab: str,
    *,
    corpus_id: str | None = None,
    split_index: int | None = None,
) -> Registry:
    """Build a ``Registry`` from an XLSX export of one tab of the team's sheet.

    ``registry_json`` maps tab name -> list of rows, each row a ``{column
    letter: cell text}`` dict with **absent keys for empty cells** — rows are
    ragged by construction.  ``hyperlinks_json`` maps tab name -> ``{"E24":
    "https://..."}``.  Both may be given as parsed dicts or as paths.

    Row *n* of the spreadsheet is ``rows[n - 1]``; hyperlink refs are 1-based
    and may point past the last non-empty row, which is ignored.

    ``split_index`` overrides the inferred source/term boundary — pass the
    0-based index of the first term row when the heuristic guesses wrong.  The
    value actually used is recorded on the returned registry.

    Raises ``KeyError`` if the tab is not in the export; returns an empty
    registry for a tab with no parseable rows (the sheet has a scratch tab
    named ``gaga``, and a junk tab must not be a crash).
    """
    tables = _as_mapping(registry_json, what="registry_json")
    link_tables = _as_mapping(hyperlinks_json, what="hyperlinks_json")
    if tab not in tables:
        raise KeyError(f"tab {tab!r} not in export; available: {sorted(tables)}")

    rows: list[Mapping[str, str]] = [
        {str(k): "" if v is None else str(v) for k, v in dict(row).items()}
        for row in tables[tab] or []
    ]
    links: Mapping[str, str] = {
        str(k): str(v) for k, v in dict(link_tables.get(tab) or {}).items()
    }
    resolved_id = corpus_id or tab

    numbering = align_link_rows(rows, links)
    boundary = (
        find_split_index(rows, links, sheet_rows=numbering)
        if split_index is None
        else int(split_index)
    )
    boundary = max(0, min(boundary, len(rows)))

    sources: list[Source] = []
    terms: list[TermRecord] = []
    roles: dict[str, str] = {}

    for offset, row in enumerate(rows):
        row_number = numbering[offset]
        if _is_header_row(row):
            # Roles accumulate rather than reset: the term header of several
            # tabs names only the term and the editor, and the source header
            # above it still describes the columns it does not mention.
            roles.update(_roles_from_header(row))
            continue
        urls = _row_urls(row, links, row_number)
        if offset < boundary:
            source = _build_source(
                row, urls, roles, corpus_id=resolved_id, row_number=row_number
            )
            if source is not None:
                sources.append(source)
        else:
            record = _build_term(row, urls, roles)
            if record is not None:
                terms.append(record)

    return Registry(
        sources=sources,
        terms=terms,
        corpus_name=tab,
        corpus_id=resolved_id,
        split_index=boundary,
    )


# --------------------------------------------------------------------------
# YAML round trip
# --------------------------------------------------------------------------


def _resolve_pair(path: str | os.PathLike[str]) -> tuple[Path, Path]:
    """``(sources.yaml, terms.yaml)`` for a corpus directory or either file path.

    The registry is two files because they have different review rhythms —
    fifteen sources a human curates once, five hundred terms that change every
    week — but they are one object, so every entry point accepts either the
    directory or ``sources.yaml`` and finds the other.
    """
    target = Path(path)
    if target.suffix.lower() in {".yaml", ".yml"}:
        return (target, target.with_name(TERMS_FILENAME))
    return (target / SOURCES_FILENAME, target / TERMS_FILENAME)


def _dump_yaml(payload: Mapping[str, Any]) -> str:
    """Serialise with Tibetan left as Tibetan and URLs left on one line.

    ``allow_unicode`` matters: without it every Tibetan title becomes a wall of
    ``\\u0F56`` escapes and the file stops being human-editable, which is the
    only reason it is YAML instead of JSON.
    """
    return yaml.safe_dump(
        dict(payload),
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=4096,
    )


def save(registry: Registry, path: str | os.PathLike[str]) -> tuple[Path, Path]:
    """Write ``sources.yaml`` and ``terms.yaml``.  Returns both paths.

    Atomic, via the ledger's writer: a corpus registry clobbered halfway
    through would take a curated source list with it.
    """
    sources_path, terms_path = _resolve_pair(path)
    header = {
        "version": REGISTRY_VERSION,
        "corpus_id": registry.corpus_id,
        "corpus_name": registry.corpus_name,
    }
    atomic_write_text(
        sources_path,
        _dump_yaml(
            {
                **header,
                "split_index": registry.split_index,
                "sources": [source.to_dict() for source in registry.sources],
            }
        ),
    )
    atomic_write_text(
        terms_path,
        _dump_yaml({**header, "terms": [record.to_dict() for record in registry.terms]}),
    )
    return (sources_path, terms_path)


def load(path: str | os.PathLike[str]) -> Registry:
    """Read a registry back from ``sources.yaml`` + ``terms.yaml``.

    A missing ``terms.yaml`` is not an error: a corpus can have curated sources
    before its term list exists, which is exactly the state after ingest and
    before the term stage runs.
    """
    sources_path, terms_path = _resolve_pair(path)
    sources_doc: Mapping[str, Any] = {}
    terms_doc: Mapping[str, Any] = {}
    if sources_path.exists():
        sources_doc = yaml.safe_load(sources_path.read_text(encoding="utf-8")) or {}
    if terms_path.exists():
        terms_doc = yaml.safe_load(terms_path.read_text(encoding="utf-8")) or {}
    if not sources_doc and not terms_doc:
        raise FileNotFoundError(f"no registry at {sources_path} or {terms_path}")

    split = sources_doc.get("split_index")
    return Registry(
        sources=[Source.from_dict(item) for item in sources_doc.get("sources") or []],
        terms=[TermRecord.from_dict(item) for item in terms_doc.get("terms") or []],
        corpus_name=str(sources_doc.get("corpus_name") or terms_doc.get("corpus_name") or ""),
        corpus_id=_clean_optional(sources_doc.get("corpus_id") or terms_doc.get("corpus_id")),
        split_index=int(split) if split is not None else None,
    )


# --------------------------------------------------------------------------
# Queries
# --------------------------------------------------------------------------


def find_term(registry: Registry, term: str) -> TermRecord | None:
    """Look up a key term, tolerating the trailing tsheg/shad difference.

    ``བྱང་ཆུབ་སེམས་`` finds ``བྱང་ཆུབ་སེམས།`` and vice versa — see ``term_key``
    for why only the terminal delimiter is ignored.
    """
    wanted = term_key(term)
    if not wanted:
        return None
    for record in registry.terms:
        if record.key == wanted:
            return record
    return None


def resolve_citation_url(
    registry: Registry, source_id: str, quote: str | None = None
) -> str | None:
    """The best public URL for citing a source, or ``None`` if it has no home yet.

    Preference order, from most to least useful to a reader checking the
    quotation: **Wikisource transcribed text** (searchable, so a text fragment
    can actually land on the passage) → **Wikisource index** (the scan) →
    **BDRC** → **Commons file**.  ``docs/reference/wikitext-spec.md`` §2 makes
    "no URL available" a visible gap in the review report rather than a silent
    one, so returning ``None`` is a real answer, not a failure.

    With ``quote``, a ``#:~:text=`` fragment is appended so the link opens at
    the quoted passage — the same thing the team's published སཏྭ་ article does
    by hand.  The fragment builder lives in
    ``kangyur_wiki.wiki.wikitext.text_fragment``; if it is not present yet, or
    cannot handle this quote, the bare URL is returned rather than a broken
    one.  A citation that lands on the right page is worth more than no
    citation at all.
    """
    source = registry.source(source_id)
    if source is None:
        return None

    base = (
        source.wikisource_text_url
        or source.wikisource_index_url
        or (bdrc_show_url(source.bdrc_id) if source.bdrc_id else None)
        or source.webuddhist_url
        or source.commons_url
    )
    if not base or not quote:
        return base

    fragment = _text_fragment(quote)
    if not fragment:
        return base
    if "#" in base:
        return base
    return f"{base}{fragment}"


def _text_fragment(quote: str) -> str | None:
    """Build a ``#:~:text=`` fragment, guarding the cross-module import.

    ``wikitext.py`` is a sibling deliverable and may not exist in a given
    checkout; importing it lazily and tolerating its absence keeps this module
    importable — and its tests runnable — on its own.
    """
    try:
        from kangyur_wiki.wiki.wikitext import text_fragment  # noqa: PLC0415
    except Exception:
        return None
    try:
        fragment = text_fragment(quote)
    except Exception:
        return None
    if not fragment:
        return None
    text = str(fragment)
    return text if text.startswith("#") else f"#{text.lstrip('#')}"


def iter_terms(registry: Registry, *, only_missing: bool = False) -> Iterable[TermRecord]:
    """Terms in sheet order; with ``only_missing``, just those with no article yet.

    The pipeline's create path and update path take different prompts, and this
    is the split between them.
    """
    for record in registry.terms:
        if only_missing and record.exists_on_wiki:
            continue
        yield record
