"""Statistical key-term selection — pipeline step 1.2.

Stage 3 proposes the terms a corpus is *about*, and does it twice: once with
Gemini (forum prompt 289-v3) and once here, statistically.  The intersection is
what a human reviews.  Two independent signals is the point — a term the model
likes and the counts do not is a term worth arguing about.

The statistic is Rayson & Garside's log-likelihood (G²), the corpus-linguistics
standard for "occurs more here than chance would predict", plus Hardie's
log-ratio as the effect size, because G² alone confuses *significant* with
*large*: in a big corpus a trivially commoner function word can outrank the
doctrinal term the article is named after.

Two Tibetan-specific complications shape the API:

**Words are not syllables.** Tibetan is written without word spaces; the tsheg
separates syllables, not words.  botok does real word segmentation and is used
when importable, but it is optional and this module must import without it, so
there is a documented syllable-level fallback.

**Key terms are 3–4 ཚེག་བར long** (prompt 289's own rule), which no unigram
count can find.  ``ngram_candidates`` therefore builds the multi-syllable
candidates the statistic then ranks.  N-gram windows never cross a shad: a
phrase spanning a sentence boundary is an artefact, not a term.

No reference corpus of Tibetan is known to exist for this purpose — PLAN.md §3
flags building one from the rest of the Kangyur/Tengyur as an open question —
so ``keyness`` also runs without one, in frequency-only mode.
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from typing import Final, Iterable, Sequence

from kangyur_wiki.tibetan.normalize import SHAD, TSHEG, TSHEG_NB, nfc, strip_markup

try:  # botok is optional: this module must import on a machine without it.
    import botok  # noqa: F401

    BOTOK_AVAILABLE = True
except ImportError:  # pragma: no cover - depends on the environment
    BOTOK_AVAILABLE = False

__all__ = [
    "BOTOK_AVAILABLE",
    "BOUNDARY",
    "KeyTerm",
    "frequencies",
    "keyness",
    "log_likelihood",
    "log_ratio",
    "ngram_candidates",
    "tokenize",
]

#: Sentence-boundary sentinel in a token stream.  It *is* the shad, which is
#: unambiguous: a content token contains only syllabic characters, so no real
#: token can ever equal it.
BOUNDARY: Final = SHAD

#: Separators inside a word — they end a syllable without ending a phrase.
_SOFT_BREAKS: Final = frozenset({TSHEG, TSHEG_NB})


def _is_letter(ch: str) -> bool:
    """A Tibetan letter, subjoined consonant or vowel sign."""
    return ch == "ༀ" or "ཀ" <= ch <= "ྼ"


def _is_syllabic(ch: str) -> bool:
    """A character that can sit inside a ཚེག་བར.

    Letters and vowel signs, Tibetan digits, and the handful of combining marks
    (``༷`` and friends) that annotated commentaries sprinkle through words.
    Everything else — shad, head marks, Latin script, Arabic digits — ends the
    syllable *and* the phrase.
    """
    return (
        _is_letter(ch)
        or "༠" <= ch <= "༳"
        or ch in "༹༘༙༵༷༾༿"
    )


def is_term_token(token: str) -> bool:
    """True for tokens eligible to be (part of) a key term.

    Excludes the boundary sentinel, anything holding punctuation or Latin
    script, and digit-only tokens — a number is never a doctrinal term.
    """
    if not token or token == BOUNDARY:
        return False
    if not any(_is_letter(ch) for ch in token):
        return False
    return all(_is_syllabic(ch) or ch in _SOFT_BREAKS for ch in token)


@lru_cache(maxsize=1)
def _word_tokenizer():  # pragma: no cover - requires botok installed
    """botok's ``WordTokenizer``, built once.

    Constructing it loads a multi-megabyte trie from disk, which takes seconds;
    a run tokenises many files.  The instance is read-only and stateless with
    respect to us, so memoising it is not shared mutable state.
    """
    if not BOTOK_AVAILABLE:
        raise RuntimeError("botok is not installed")
    from botok import WordTokenizer

    return WordTokenizer()


def _clean_botok_unit(raw: str) -> str | None:
    """Turn one botok token into a content token, or ``None`` for a boundary.

    botok emits words with their trailing tsheg attached (``བྱང་ཆུབ་``).  The
    trailing separator is dropped and internal ones kept, so a token is exactly
    the word and ``ngram_candidates`` can rejoin units with a single tsheg
    without doubling it.
    """
    unit = nfc(raw).strip().strip(TSHEG + TSHEG_NB)
    if not unit or not is_term_token(unit):
        return None
    return unit


def _tokenize_botok(text: str) -> list[str]:
    tokens: list[str] = []
    for token in _word_tokenizer().tokenize(strip_markup(text)):
        raw = getattr(token, "text", None)
        unit = _clean_botok_unit(raw if isinstance(raw, str) else str(token))
        if unit is None:
            _push_boundary(tokens)
        else:
            tokens.append(unit)
    return _trim_boundaries(tokens)


def _push_boundary(tokens: list[str]) -> None:
    if tokens and tokens[-1] != BOUNDARY:
        tokens.append(BOUNDARY)


def _trim_boundaries(tokens: list[str]) -> list[str]:
    start = 1 if tokens and tokens[0] == BOUNDARY else 0
    end = len(tokens) - 1 if tokens and tokens[-1] == BOUNDARY else len(tokens)
    return tokens[start:end]


def _tokenize_fallback(text: str) -> list[str]:
    """Syllable tokenisation, used when botok is unavailable.

    Markup is stripped, then the text is scanned character by character: a
    tsheg closes the current syllable, and anything non-syllabic closes it and
    emits a boundary.  The result is ཚེག་བར units, **not** words — a two-syllable
    word arrives as two tokens.  ``ngram_candidates`` is what makes that
    survivable, since it reassembles multi-syllable candidates anyway; the cost
    is a noisier candidate set, not a wrong one.
    """
    tokens: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            unit = "".join(buffer)
            buffer.clear()
            if is_term_token(unit):
                tokens.append(unit)
            else:
                _push_boundary(tokens)

    for ch in strip_markup(text):
        if _is_syllabic(ch):
            buffer.append(ch)
        elif ch in _SOFT_BREAKS:
            flush()
        else:
            flush()
            _push_boundary(tokens)
    flush()
    return _trim_boundaries(tokens)


def tokenize(text: str, *, use_botok: bool | None = None) -> list[str]:
    """Tokenise Tibetan text into content tokens separated by ``BOUNDARY``.

    Uses botok when it is importable and the syllable fallback otherwise; pass
    ``use_botok`` to force either path (tests pin it so results do not depend
    on what happens to be installed).  Requesting botok when it is absent
    raises rather than degrading silently — the two tokenisers produce
    different statistics, and a run must not switch between them unnoticed.
    """
    if use_botok is None:
        use_botok = BOTOK_AVAILABLE
    if use_botok:
        if not BOTOK_AVAILABLE:
            raise RuntimeError("botok tokenisation requested but botok is not installed")
        return _tokenize_botok(text)
    return _tokenize_fallback(text)


def frequencies(tokens: Iterable[str]) -> Counter[str]:
    """Count tokens exactly as given, boundary sentinels included.

    Kept literal so it can count n-gram candidates, raw tokens or anything
    else; ``keyness`` does the filtering it needs.
    """
    return Counter(tokens)


def ngram_candidates(
    tokens: Sequence[str],
    n_range: tuple[int, int] = (1, 4),
) -> list[str]:
    """All tsheg-joined n-grams of ``tokens`` for n in ``n_range``, inclusive.

    Repeats are kept — the output is meant to be fed straight to
    ``frequencies``.  Windows break at boundary sentinels and at any
    non-eligible token, so no candidate ever spans a shad.

    N-grams carry no trailing tsheg: ``བྱང་ཆུབ་སེམས``, not ``བྱང་ཆུབ་སེམས་``.
    The trailing tsheg belongs to whatever renders the term — a wikilink target
    takes one (wikitext-spec §3), a ``<ref>`` may not.
    """
    low, high = n_range
    if low < 1 or high < low:
        raise ValueError(f"n_range must be (low, high) with 1 <= low <= high, got {n_range!r}")

    out: list[str] = []
    run: list[str] = []

    def emit() -> None:
        for n in range(low, high + 1):
            for i in range(len(run) - n + 1):
                out.append(TSHEG.join(run[i : i + n]))
        run.clear()

    for token in tokens:
        if is_term_token(token):
            run.append(token)
        else:
            emit()
    emit()
    return out


def log_likelihood(a: float, b: float, c: float, d: float) -> float:
    """Rayson & Garside's G² for one term.

    ``a`` its frequency in the study corpus, ``b`` in the reference corpus,
    ``c`` and ``d`` the corpora's total token counts::

        E1 = c(a+b)/(c+d)     E2 = d(a+b)/(c+d)
        G² = 2( a·ln(a/E1) + b·ln(b/E2) )

    with a zero count contributing zero.  G² is non-negative and says only that
    the observed split is unlikely — it does not say in which direction, which
    is what ``log_ratio`` is for.  Degenerate inputs (an empty corpus) return
    0.0 rather than raising: a corpus with no tokens has no evidence, and the
    caller ranking a thousand terms should not have to guard every one.
    """
    total = c + d
    if total <= 0:
        return 0.0
    e1 = c * (a + b) / total
    e2 = d * (a + b) / total
    g2 = 0.0
    if a > 0:
        if e1 <= 0:
            return 0.0
        g2 += a * math.log(a / e1)
    if b > 0:
        if e2 <= 0:
            return 0.0
        g2 += b * math.log(b / e2)
    return 2.0 * g2


def log_ratio(a: float, b: float, c: float, d: float) -> float:
    """Hardie's log-ratio effect size: log2 of the relative-frequency ratio.

    Positive means over-represented in the study corpus.  A term absent from
    the reference corpus would give infinity, so ``b`` is floored at 0.5 — the
    standard continuity correction, and the honest reading is "at least this
    large", since the true value depends on a count we do not have.
    """
    if c <= 0 or d <= 0:
        return 0.0
    b_adj = b if b > 0 else 0.5
    return math.log2((a / c) / (b_adj / d))


@dataclass(frozen=True)
class KeyTerm:
    """One ranked candidate.

    ``g2`` is significance, ``effect`` is size.  Both are 0.0 in frequency-only
    mode, where neither is defined.
    """

    term: str
    freq_study: int
    freq_ref: int
    g2: float
    effect: float


def keyness(
    study_tokens: Iterable[str],
    reference_tokens: Iterable[str] | None = None,
    min_freq: int = 3,
    *,
    positive_only: bool = True,
) -> list[KeyTerm]:
    """Rank the study corpus's candidate terms by keyness, highest first.

    Feed it whatever population you want ranked — raw tokens for unigrams, or
    ``ngram_candidates(tokens)`` for the multi-syllable terms prompt 289 asks
    for.  ``c`` and ``d`` are the totals of the populations actually passed, so
    both corpora must be prepared the same way or the comparison is meaningless.

    ``min_freq`` applies to the study frequency only: a term seen twice is not
    a key term regardless of how absent it is from the reference corpus.
    ``positive_only`` drops terms the study corpus *under*-uses, which are
    statistically interesting and useless for choosing what to write about.

    **Frequency-only mode.** With ``reference_tokens=None`` there is nothing to
    compare against, so the result is ranked by raw frequency with ``g2`` and
    ``effect`` set to 0.0.  Do not report those zeros as statistics — they mean
    "not computed".  PLAN.md §3 records that no Tibetan reference corpus exists
    yet; until one is built this is the mode that runs.
    """
    study = Counter(t for t in study_tokens if is_term_token(t))
    total_study = sum(study.values())
    if total_study <= 0:
        return []

    if reference_tokens is None:
        ranked = sorted(
            ((term, freq) for term, freq in study.items() if freq >= min_freq),
            key=lambda item: (-item[1], item[0]),
        )
        return [KeyTerm(term, freq, 0, 0.0, 0.0) for term, freq in ranked]

    reference = Counter(t for t in reference_tokens if is_term_token(t))
    total_ref = sum(reference.values())

    terms: list[KeyTerm] = []
    for term, freq in study.items():
        if freq < min_freq:
            continue
        freq_ref = reference.get(term, 0)
        if positive_only and total_ref > 0:
            if freq / total_study <= freq_ref / total_ref:
                continue
        terms.append(
            KeyTerm(
                term=term,
                freq_study=freq,
                freq_ref=freq_ref,
                g2=log_likelihood(freq, freq_ref, total_study, total_ref),
                effect=log_ratio(freq, freq_ref, total_study, total_ref),
            )
        )

    # Ties broken by frequency then by the term itself: golden-file tests and
    # a human review list both need the order to be reproducible.
    terms.sort(key=lambda k: (-k.g2, -k.freq_study, k.term))
    return terms
