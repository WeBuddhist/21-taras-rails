"""Shared text normalisation for Tibetan pipeline data.

Four normalisations, one module.  Every guarantee this pipeline makes about a
quotation is really a claim about *which* normalisation was compared, so the
verifier, the aligner and the term selector must not each grow their own — that
drift is exactly how a citation ends up looking checked when it is not.

The ladder, loosest last:

``nfc``           canonical form only.  The storage format for everything on
                  disk (PLAN.md stage 1 normalises on ingest).
``collapse``      NFC minus whitespace.  Line wrapping legitimately differs
                  between a commentary file and the article quoting it;
                  nothing else may.  This is the verbatim-comparison key.
``strip_markup``  NFC minus the editorial furniture that sits *inside* source
                  files — Obsidian transclusions, block IDs, wikilink wrappers,
                  bold, ``<ref>``.
``fuzzy_key``     all of the above plus every shad, tsheg and head mark.
                  Tolerates orthographic variation between editions; a match at
                  this level is a warning, never a pass (see ``verify.py``).

``fuzzy_key`` deliberately reproduces the ``norm()`` used by the
Bodhicaryāvatāra vault's ``01_transclude_verses.py``, which has been run across
ten commentaries: the dropped-character set is copied from there rather than
re-derived, because that set is what makes the alignment pass work.

Nothing here edits stored data.  These functions build *comparison keys* and
return new strings; the Tibetan punctuation in the corpus is never touched.
"""

from __future__ import annotations

import re
import unicodedata
from array import array
from typing import Final, Sequence

__all__ = [
    "TSHEG",
    "TSHEG_NB",
    "SHAD",
    "DOUBLE_SHAD",
    "FUZZY_DROP",
    "nfc",
    "collapse",
    "collapse_with_map",
    "strip_markup",
    "fuzzy_key",
    "fuzzy_key_with_map",
    "syllables",
]

# --------------------------------------------------------------------------
# Punctuation
# --------------------------------------------------------------------------

#: U+0F0B, the intersyllabic separator.  A letter for our purposes, not a
#: space: it may only be dropped when building a deliberately lossy key.
TSHEG: Final = "་"
#: U+0F0C, the *non-breaking* delimiter tsheg.  Never a split point — marking a
#: junction as unbreakable is its entire job — so ``syllables`` keeps it.
TSHEG_NB: Final = "༌"
#: U+0F0D, the shad (sentence terminator).
SHAD: Final = "།"
#: U+0F0E, the nyis shad.
DOUBLE_SHAD: Final = "༎"

#: Characters ``fuzzy_key`` removes, copied verbatim from the vault's
#: ``norm()``: shad U+0F0D, nyis shad U+0F0E, tsheg U+0F0B, and the head marks
#: U+0F05, U+0F04, U+0F08.  Editions disagree about all six far more often than
#: they disagree about letters, which is why dropping them recovers real
#: matches instead of manufacturing false ones.
FUZZY_DROP: Final = frozenset("།༎་༅༄༈")

# --------------------------------------------------------------------------
# Markup
# --------------------------------------------------------------------------

#: Obsidian transclusion, e.g. ``![[1-SOURCES/Text/root.md#^1-1]]``.
_TRANSCLUSION_RE: Final = re.compile(r"!\[\[.*?\]\]")
#: Obsidian block id, e.g. ``^1-1`` or ``^I-3``.  ``\w`` is Unicode-aware and
#: therefore also swallows a caret followed by Tibetan letters — kept because
#: the proven ``norm()`` behaves that way and the corpus depends on it.
_BLOCK_ID_RE: Final = re.compile(r"\^[\w-]+")
#: The wrapper around an Obsidian wikilink, e.g. the ``[[#^1-2-0|`` and ``]]``
#: of ``[[#^1-2-0|བཤད་པ་]]``.  ``tag-inline-toc`` wraps sa-bcad terms this way,
#: so the wrapper sits *inside* a sentence: dropping the whole link would delete
#: Tibetan the commentary actually says.  Two patterns rather than one because
#: the keep-mask drops whole matches, and only the furniture may be dropped —
#: the display text between them has to survive.
_WIKILINK_OPEN_RE: Final = re.compile(r"\[\[(?:[^\]|\n]*\|)?")
_WIKILINK_CLOSE_RE: Final = re.compile(r"\]\]")
#: Markdown bold, as used by the segmented commentaries to mark root quotations.
_MD_BOLD_RE: Final = re.compile(r"\*\*")
#: Wiki bold (docs/reference/wikitext-spec.md §4).
_WIKI_BOLD_RE: Final = re.compile(r"'''")
#: A footnote and its content.  The self-closing form is tried first so that
#: ``<ref name="x" />`` cannot be mistaken for an opening tag and swallow
#: everything up to some later ``</ref>``.  ``\b`` keeps ``<references />``
#: intact, which is structural and must survive into the validator.
_REF_RE: Final = re.compile(r"<ref\b[^>]*/>|<ref\b[^>]*>.*?</ref>", re.DOTALL | re.IGNORECASE)

_MARKUP_PATTERNS: Final = (
    _TRANSCLUSION_RE,
    _BLOCK_ID_RE,
    _WIKILINK_OPEN_RE,
    _WIKILINK_CLOSE_RE,
    _MD_BOLD_RE,
    _WIKI_BOLD_RE,
    _REF_RE,
)


def nfc(s: str) -> str:
    """Canonical composition.  Applied by every other function in this module."""
    return unicodedata.normalize("NFC", s)


def _markup_keep_mask(s: str) -> list[bool]:
    """Per-character keep flags for ``s`` with all markup spans marked dropped.

    Every pattern is matched against the *same* string and the spans unioned,
    rather than applying the regexes in sequence.  Sequential application would
    let one removal create a match for the next, so the offset map and the
    plain string result could disagree; a union cannot.
    """
    keep = [True] * len(s)
    for pattern in _MARKUP_PATTERNS:
        for match in pattern.finditer(s):
            start, end = match.span()
            for i in range(start, end):
                keep[i] = False
    return keep


def _reduce(
    text: str,
    *,
    strip: bool,
    drop_whitespace: bool,
    drop: frozenset[str] = frozenset(),
) -> tuple[str, Sequence[int]]:
    """Return the reduced text and a map from reduced index to index in ``nfc(text)``.

    The map is an ``array('i')`` rather than a list: a 3 MB commentary produces
    a few million entries, and a list of boxed ints costs roughly thirty bytes
    each — enough to matter once ``verify.check_quotes`` caches ten of them.
    """
    source = nfc(text)
    keep = _markup_keep_mask(source) if strip else None
    out: list[str] = []
    index: array[int] = array("i")
    for i, ch in enumerate(source):
        if keep is not None and not keep[i]:
            continue
        if drop_whitespace and ch.isspace():
            continue
        if ch in drop:
            continue
        out.append(ch)
        index.append(i)
    return "".join(out), index


def collapse(s: str) -> str:
    """NFC with all whitespace removed — the verbatim-comparison key.

    Two texts that differ only in line breaking are the same quotation; two
    texts that differ by one letter are not, and this key keeps that
    distinction sharp.
    """
    return _reduce(s, strip=False, drop_whitespace=True)[0]


def collapse_with_map(s: str) -> tuple[str, Sequence[int]]:
    """``collapse(s)`` plus ``map[i]`` = the index of that character in ``nfc(s)``.

    Lets a match found in collapsed space be reported at a character offset a
    human can actually use to open the file at the right place.
    """
    return _reduce(s, strip=False, drop_whitespace=True)


def strip_markup(s: str) -> str:
    """NFC with editorial markup removed, whitespace and punctuation untouched.

    Removes Obsidian transclusions ``![[...]]``, block ids ``^1-2``, markdown
    bold ``**``, wiki bold ``'''`` and ``<ref>...</ref>``, and unwraps wikilinks
    (``[[#^1-2-0|བཤད་པ་]]`` -> ``བཤད་པ་``) — the wrapper is annotation, the
    display text is the commentary's own words.  ``<references />`` survives: it
    is article structure, not annotation, and the validator needs to see it.
    """
    return _reduce(s, strip=True, drop_whitespace=False)[0]


def fuzzy_key(s: str) -> str:
    """Aggressive key for variant-tolerant matching.

    NFC, markup stripped, all whitespace gone, and every character in
    ``FUZZY_DROP`` gone.  What survives is letters — so two witnesses of the
    same line that punctuate it differently produce the same key.  Reproduces
    ``norm()`` from the vault's ``01_transclude_verses.py``.

    A match on this key proves the letters agree, and nothing more.  Treat it
    as evidence to be reviewed, never as verification.
    """
    return _reduce(s, strip=True, drop_whitespace=True, drop=FUZZY_DROP)[0]


def fuzzy_key_with_map(s: str) -> tuple[str, Sequence[int]]:
    """``fuzzy_key(s)`` plus ``map[i]`` = the index of that character in ``nfc(s)``."""
    return _reduce(s, strip=True, drop_whitespace=True, drop=FUZZY_DROP)


def syllables(s: str) -> list[str]:
    """Split into ཚེག་བར units on U+0F0B, dropping empties.

    The unit of length in Tibetan — gloss-length rules, article-length
    warnings and the ``#:~:text=`` fragments in citation URLs are all counted
    in these, not in characters or words.

    The split is exactly on the tsheg, with nothing else inferred, so
    punctuation lands wherever the text puts it: ``ཏེ། །`` is one unit (no
    tsheg intervenes) but ``དང་། །`` is two — ``དང`` and ``། །`` — because
    the scribe wrote a tsheg before the shad.  A caller counting syllables or
    slicing a URL fragment should therefore drop units with no letters in
    them; guessing here instead would make the function lossy for the caller
    that needs the substring exactly as it appears in the source.
    """
    return [unit for unit in (part.strip() for part in nfc(s).split(TSHEG)) if unit]
