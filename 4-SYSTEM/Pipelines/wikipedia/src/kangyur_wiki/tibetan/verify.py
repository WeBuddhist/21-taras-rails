"""The verbatim-quotation checker — stage 7's blocking rule V1.

The paper's central claim is that a generated article is checkable by
construction: every quotation in it appears character-for-character in the file
it cites.  This module is the mechanism that claim rests on.  It is
deterministic, offline, and it fails closed.

Three tiers, deliberately unequal:

``exact``      the quote is a substring of the source.  A pass.
``collapsed``  a substring once whitespace is removed from both.  A pass —
               line wrapping is not part of the text.
``fuzzy``      a substring once shads, tshegs, head marks and markup are also
               removed.  **Not** a pass.  The letters agree but the
               punctuation does not, which means the article is not quoting
               what the file says; a human decides whether the source has an
               orthographic variant or the model paraphrased.
``missing``    a failure.

Reporting a fuzzy hit as success would quietly reintroduce exactly the class of
error this gate exists to catch, so ``found`` is not the gate: ``passed`` is.

Generalised from ``verify_wiki_citations.py`` in the Bodhicaryāvatāra vault,
which caught a real bad citation in production.  Its semantics are preserved —
whitespace-collapsed comparison, a short-quote warning at ten characters — with
two additions: an offset mapped back to the original file, and the fuzzy tier,
which that script lacked and which turns "not verbatim" into a diagnosis.
"""

from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Callable, Final, Sequence

from kangyur_wiki.tibetan.normalize import (
    collapse,
    collapse_with_map,
    fuzzy_key,
    fuzzy_key_with_map,
    nfc,
)

__all__ = [
    "METHOD_EXACT",
    "METHOD_COLLAPSED",
    "METHOD_FUZZY",
    "METHOD_MISSING",
    "PASSING_METHODS",
    "MIN_FUZZY_KEY_LEN",
    "SHORT_QUOTE_CHARS",
    "QuoteCheck",
    "SourceLoader",
    "check_quote",
    "check_quotes",
]

METHOD_EXACT: Final = "exact"
METHOD_COLLAPSED: Final = "collapsed"
METHOD_FUZZY: Final = "fuzzy"
METHOD_MISSING: Final = "missing"

#: The only two outcomes that satisfy V1.
PASSING_METHODS: Final = frozenset({METHOD_EXACT, METHOD_COLLAPSED})

#: Below this many characters a fuzzy key is not evidence of anything — with
#: punctuation stripped, three or four syllables of Tibetan recur constantly.
#: Shorter quotes that fail the two exact tiers are reported ``missing``, which
#: is the safe direction: a human looks at it.
MIN_FUZZY_KEY_LEN: Final = 8

#: Inherited from the vault verifier: a hit this short is weak evidence even
#: when exact, so it is noted.  Non-blocking.
SHORT_QUOTE_CHARS: Final = 10

#: Similarity for a miss is computed on a window, but ``SequenceMatcher`` is
#: quadratic; past this quote length the diagnostic is not worth the seconds.
_RATIO_MAX_LEN: Final = 4000

#: Loads a source's full text given the path recorded in the citation.
SourceLoader = Callable[[str], str]


@dataclass(frozen=True)
class QuoteCheck:
    """The verdict on one quotation.

    ``char_offset`` indexes into ``nfc(source_text)``.  Stage 1 stores every
    source NFC-normalised, so for pipeline data that is the byte-for-byte file
    offset; for a source that arrives in some other normal form the offset is
    into its NFC form, which is the only string the comparison ever saw.

    ``ratio`` is 1.0 for the two passing tiers.  For ``fuzzy`` it is the
    similarity between the quote and the source span that matched it, so a
    reviewer can tell a one-shad difference (0.99) from a rewrite (0.6).  For
    ``missing`` it is the best similarity found near the longest matching
    prefix or suffix — 0.0 means the quote is not in this file at all, 0.9
    means it is nearly there and worth looking at.  A ``missing`` ratio is
    computed on fuzzy keys, so it never flatters punctuation differences.
    """

    quote: str
    source_path: str
    found: bool
    method: str
    ratio: float
    char_offset: int | None
    note: str = ""

    @property
    def passed(self) -> bool:
        """True only for ``exact`` and ``collapsed``.

        The V1 gate must branch on this, never on ``found`` — a fuzzy hit is
        found and still fails.
        """
        return self.method in PASSING_METHODS

    @property
    def warning(self) -> bool:
        """A fuzzy hit: real text, wrong punctuation, needs a human."""
        return self.method == METHOD_FUZZY


class _SourceView:
    """One source text plus its comparison keys, built on demand.

    Most quotations pass at ``exact``, so the collapsed and fuzzy views — each
    a full copy of the text plus an index map — are only built for the sources
    that actually need them.
    """

    __slots__ = ("text", "_collapsed", "_cmap", "_fuzzy", "_fmap")

    def __init__(self, raw: str) -> None:
        self.text = nfc(raw)
        self._collapsed: str | None = None
        self._cmap: Sequence[int] | None = None
        self._fuzzy: str | None = None
        self._fmap: Sequence[int] | None = None

    def _build_collapsed(self) -> None:
        self._collapsed, self._cmap = collapse_with_map(self.text)

    def _build_fuzzy(self) -> None:
        self._fuzzy, self._fmap = fuzzy_key_with_map(self.text)

    @property
    def collapsed(self) -> str:
        if self._collapsed is None:
            self._build_collapsed()
        assert self._collapsed is not None
        return self._collapsed

    @property
    def cmap(self) -> Sequence[int]:
        if self._cmap is None:
            self._build_collapsed()
        assert self._cmap is not None
        return self._cmap

    @property
    def fuzzy(self) -> str:
        if self._fuzzy is None:
            self._build_fuzzy()
        assert self._fuzzy is not None
        return self._fuzzy

    @property
    def fmap(self) -> Sequence[int]:
        if self._fmap is None:
            self._build_fuzzy()
        assert self._fmap is not None
        return self._fmap


def _longest_prefix_hit(needle: str, hay: str) -> tuple[int, int]:
    """Longest prefix of ``needle`` occurring in ``hay``: (length, position).

    Binary search is valid because the property is monotone — if a prefix is
    absent, every longer one is too.  Roughly a dozen C-level ``str.find``
    calls even on a three-megabyte commentary.
    """
    if not needle or not hay:
        return 0, -1
    lo, hi, pos = 0, len(needle), -1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        at = hay.find(needle[:mid])
        if at >= 0:
            lo, pos = mid, at
        else:
            hi = mid - 1
    return lo, pos


def _longest_suffix_hit(needle: str, hay: str) -> tuple[int, int]:
    """Longest suffix of ``needle`` occurring in ``hay``: (length, position)."""
    if not needle or not hay:
        return 0, -1
    lo, hi, pos = 0, len(needle), -1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        at = hay.find(needle[len(needle) - mid :])
        if at >= 0:
            lo, pos = mid, at
        else:
            hi = mid - 1
    return lo, pos


def _window_ratio(needle: str, hay: str, start: int) -> float:
    """Similarity of ``needle`` against the stretch of ``hay`` beginning at ``start``."""
    if start < 0:
        return 0.0
    pad = len(needle) // 2 + 8
    window = hay[max(0, start) : start + len(needle) + pad]
    if not window:
        return 0.0
    return SequenceMatcher(None, needle, window, autojunk=False).ratio()


def _miss_ratio(fuzzy_quote: str, fuzzy_source: str) -> float:
    """How close a failed quote came, on fuzzy keys.

    Anchored on the longest matching prefix and suffix rather than diffed
    globally: a whole-file diff is quadratic in the commentary length, and the
    answer a reviewer needs is local anyway — where does the quote stop
    agreeing with the source?
    """
    if not fuzzy_quote or not fuzzy_source:
        return 0.0
    if len(fuzzy_quote) > _RATIO_MAX_LEN:
        matched, _ = _longest_prefix_hit(fuzzy_quote, fuzzy_source)
        return matched / len(fuzzy_quote)

    best = 0.0
    prefix_len, prefix_at = _longest_prefix_hit(fuzzy_quote, fuzzy_source)
    if prefix_len:
        best = max(best, _window_ratio(fuzzy_quote, fuzzy_source, prefix_at))
    suffix_len, suffix_at = _longest_suffix_hit(fuzzy_quote, fuzzy_source)
    if suffix_len:
        start = suffix_at - (len(fuzzy_quote) - suffix_len)
        best = max(best, _window_ratio(fuzzy_quote, fuzzy_source, max(0, start)))
    return best


def _short_note(quote: str) -> str:
    n = len(collapse(quote))
    if n < SHORT_QUOTE_CHARS:
        return f"short quote ({n} chars): a substring hit this short is weak evidence"
    return ""


def _check(quote: str, view: _SourceView, source_path: str) -> QuoteCheck:
    normalised = nfc(quote)
    if not normalised.strip():
        return QuoteCheck(
            quote=quote,
            source_path=source_path,
            found=False,
            method=METHOD_MISSING,
            ratio=0.0,
            char_offset=None,
            note="empty quote: nothing to verify",
        )

    at = view.text.find(normalised)
    if at >= 0:
        return QuoteCheck(
            quote=quote,
            source_path=source_path,
            found=True,
            method=METHOD_EXACT,
            ratio=1.0,
            char_offset=at,
            note=_short_note(quote),
        )

    collapsed_quote = collapse(quote)
    if collapsed_quote:
        at = view.collapsed.find(collapsed_quote)
        if at >= 0:
            return QuoteCheck(
                quote=quote,
                source_path=source_path,
                found=True,
                method=METHOD_COLLAPSED,
                ratio=1.0,
                char_offset=view.cmap[at],
                note=_short_note(quote) or "matched across a line break",
            )

    fuzzy_quote = fuzzy_key(quote)
    if len(fuzzy_quote) >= MIN_FUZZY_KEY_LEN:
        at = view.fuzzy.find(fuzzy_quote)
        if at >= 0:
            start = view.fmap[at]
            end = view.fmap[at + len(fuzzy_quote) - 1] + 1
            span = view.text[start:end]
            ratio = SequenceMatcher(
                None, collapse(quote), collapse(span), autojunk=False
            ).ratio()
            return QuoteCheck(
                quote=quote,
                source_path=source_path,
                found=True,
                method=METHOD_FUZZY,
                ratio=ratio,
                char_offset=start,
                note=(
                    "letters match but punctuation or markup differs; "
                    "not verbatim — review against the source span"
                ),
            )

    return QuoteCheck(
        quote=quote,
        source_path=source_path,
        found=False,
        method=METHOD_MISSING,
        ratio=_miss_ratio(fuzzy_quote, view.fuzzy),
        char_offset=None,
        note="not present in this source",
    )


def check_quote(quote: str, source_text: str, source_path: str = "") -> QuoteCheck:
    """Check one quotation against one source text.

    ``source_path`` is recorded on the result for reporting only; it is never
    read from disk here, which keeps this function pure and the module
    importable with no filesystem at all.
    """
    return _check(quote, _SourceView(source_text), source_path)


def check_quotes(
    quotes: Sequence[tuple[str, str]],
    loader: SourceLoader,
) -> list[QuoteCheck]:
    """Check ``(quote, source_path)`` pairs, loading each source at most once.

    Results come back in input order.  An article cites the same commentary
    dozens of times and those commentaries run to megabytes, so the cache is
    the difference between one read and dozens.  A source that will not load is
    reported as ``missing`` with the reason in ``note`` rather than raised: one
    unreadable file should produce one failed citation in the report, not an
    aborted verification run.
    """
    cache: dict[str, _SourceView | str] = {}
    results: list[QuoteCheck] = []

    for quote, source_path in quotes:
        view = cache.get(source_path)
        if view is None:
            try:
                view = _SourceView(loader(source_path))
            except Exception as exc:  # noqa: BLE001 - loader is caller-supplied
                view = f"source could not be loaded: {exc!r}"
            cache[source_path] = view

        if isinstance(view, str):
            results.append(
                QuoteCheck(
                    quote=quote,
                    source_path=source_path,
                    found=False,
                    method=METHOD_MISSING,
                    ratio=0.0,
                    char_offset=None,
                    note=view,
                )
            )
            continue

        results.append(_check(quote, view, source_path))

    return results
