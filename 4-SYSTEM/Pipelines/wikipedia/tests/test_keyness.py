"""Tests for statistical key-term selection.

The fallback tokeniser is tested directly because that is what runs wherever
botok is not installed — including this environment.  The botok adapter is
tested through an injected fake, so the token-shape assumptions it makes
(trailing tsheg attached, punctuation arriving as its own token) are pinned
without needing botok present or the network up.

G² values are checked against hand-computed numbers rather than a golden file,
so a refactor that changes the statistic cannot be blessed by regenerating the
fixture.
"""

from __future__ import annotations

import math

import pytest

from kangyur_wiki.tibetan import keyness as k

# root.md ^I-3, and a phrase from the same verse used throughout.
HOMAGE = "སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །"


# --------------------------------------------------------------------------
# tokenize — fallback path
# --------------------------------------------------------------------------


def test_fallback_splits_on_tsheg_and_drops_terminal_punctuation():
    assert k.tokenize("བྱང་ཆུབ་སེམས་དཔའ།", use_botok=False) == [
        "བྱང",
        "ཆུབ",
        "སེམས",
        "དཔའ",
    ]


def test_fallback_marks_sentence_boundaries_with_a_shad_token():
    assert k.tokenize("ཆོས།ཆོས།", use_botok=False) == ["ཆོས", k.BOUNDARY, "ཆོས"]


def test_fallback_collapses_runs_of_punctuation_into_one_boundary():
    assert k.tokenize("ཆོས། །༄༅། །ཉིད", use_botok=False) == [
        "ཆོས",
        k.BOUNDARY,
        "ཉིད",
    ]


def test_fallback_never_emits_a_leading_or_trailing_boundary():
    tokens = k.tokenize("། །ཆོས། །", use_botok=False)
    assert tokens == ["ཆོས"]


def test_fallback_strips_markup_before_tokenising():
    """Block ids and bold markers are file furniture; counting them as terms
    would put ``^1-1`` near the top of the keyness table."""
    assert k.tokenize("**བདེ་གཤེགས་** ^1-1", use_botok=False) == ["བདེ", "གཤེགས"]


def test_fallback_drops_latin_script_and_arabic_digits():
    assert k.tokenize("abc བྱང་ཆུབ 123", use_botok=False) == ["བྱང", "ཆུབ"]


def test_fallback_drops_tibetan_digit_only_tokens():
    assert k.tokenize("༡༢་ཆོས", use_botok=False) == ["ཆོས"]


def test_fallback_keeps_combining_marks_inside_a_syllable():
    """The annotated commentaries (BCAC19_KKP) mark words with U+0F37; the mark
    belongs to the syllable, not between syllables."""
    assert k.tokenize("དགེ༷་བ༷", use_botok=False) == ["དགེ༷", "བ༷"]


def test_fallback_on_a_real_line():
    assert k.tokenize(HOMAGE, use_botok=False) == [
        "སངས", "རྒྱས", "དང", "བྱང", "ཆུབ", "སེམས", "དཔའ", "ཐམས", "ཅད", "ལ", "ཕྱག", "འཚལ", "ལོ",
    ]


def test_empty_input_tokenises_to_nothing():
    assert k.tokenize("", use_botok=False) == []
    assert k.tokenize("   \n", use_botok=False) == []


# --------------------------------------------------------------------------
# tokenize — botok adapter, exercised through a fake
# --------------------------------------------------------------------------


class _FakeToken:
    def __init__(self, text: str) -> None:
        self.text = text


class _FakeTokenizer:
    """Stands in for ``botok.WordTokenizer``: words carry their trailing tsheg,
    punctuation and whitespace arrive as their own tokens."""

    def __init__(self, pieces: list[str]) -> None:
        self._pieces = pieces

    def tokenize(self, text: str) -> list[_FakeToken]:
        return [_FakeToken(piece) for piece in self._pieces]


def _install_fake(monkeypatch, pieces: list[str]) -> None:
    monkeypatch.setattr(k, "BOTOK_AVAILABLE", True)
    monkeypatch.setattr(k, "_word_tokenizer", lambda: _FakeTokenizer(pieces))


def test_botok_words_keep_their_internal_tsheg_and_lose_the_trailing_one(monkeypatch):
    """A botok word is a multi-syllable unit and must stay one token —
    otherwise the whole reason for preferring botok is thrown away."""
    _install_fake(monkeypatch, ["བྱང་ཆུབ་", "སེམས་དཔའ་", "།", " ", "ཆོས་"])
    assert k.tokenize("ignored", use_botok=True) == [
        "བྱང་ཆུབ",
        "སེམས་དཔའ",
        k.BOUNDARY,
        "ཆོས",
    ]


def test_botok_tokens_without_a_text_attribute_still_work(monkeypatch):
    monkeypatch.setattr(k, "BOTOK_AVAILABLE", True)

    class _StringTokenizer:
        def tokenize(self, text: str) -> list[str]:
            return ["ཆོས་", "ཉིད་"]

    monkeypatch.setattr(k, "_word_tokenizer", lambda: _StringTokenizer())
    assert k.tokenize("ignored", use_botok=True) == ["ཆོས", "ཉིད"]


def test_requesting_botok_without_botok_raises_rather_than_degrading(monkeypatch):
    monkeypatch.setattr(k, "BOTOK_AVAILABLE", False)
    with pytest.raises(RuntimeError, match="botok"):
        k.tokenize(HOMAGE, use_botok=True)


def test_botok_available_is_a_bool_and_the_module_imported_regardless():
    assert isinstance(k.BOTOK_AVAILABLE, bool)


# --------------------------------------------------------------------------
# is_term_token
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "token,expected",
    [
        ("ཆོས", True),
        ("བྱང་ཆུབ", True),
        (k.BOUNDARY, False),
        ("", False),
        ("༡༢", False),
        ("abc", False),
        ("ཆོས།", False),
        ("ཆོས ", False),
    ],
)
def test_is_term_token(token, expected):
    assert k.is_term_token(token) is expected


# --------------------------------------------------------------------------
# frequencies
# --------------------------------------------------------------------------


def test_frequencies_counts_exactly_what_it_is_given():
    counts = k.frequencies(["ཆོས", "ཆོས", k.BOUNDARY])
    assert counts["ཆོས"] == 2
    assert counts[k.BOUNDARY] == 1


# --------------------------------------------------------------------------
# ngram_candidates
# --------------------------------------------------------------------------


def test_ngrams_are_joined_by_a_single_tsheg_and_carry_no_trailing_one():
    tokens = ["བྱང", "ཆུབ", "སེམས"]
    assert k.ngram_candidates(tokens, (2, 2)) == ["བྱང་ཆུབ", "ཆུབ་སེམས"]


def test_ngram_windows_never_cross_a_sentence_boundary():
    tokens = ["བྱང", "ཆུབ", "སེམས", k.BOUNDARY, "དཔའ"]
    out = k.ngram_candidates(tokens, (1, 2))
    assert out == ["བྱང", "ཆུབ", "སེམས", "བྱང་ཆུབ", "ཆུབ་སེམས", "དཔའ"]
    assert "སེམས་དཔའ" not in out


def test_ngrams_reach_the_three_and_four_syllable_terms_prompt_289_asks_for():
    tokens = k.tokenize("བྱང་ཆུབ་སེམས་དཔའ", use_botok=False)
    out = k.ngram_candidates(tokens, (3, 4))
    assert "བྱང་ཆུབ་སེམས" in out
    assert "བྱང་ཆུབ་སེམས་དཔའ" in out


def test_ngram_output_keeps_repeats_so_it_can_be_counted():
    tokens = ["ཆོས", k.BOUNDARY, "ཆོས"]
    assert k.ngram_candidates(tokens, (1, 1)) == ["ཆོས", "ཆོས"]


@pytest.mark.parametrize("bad", [(0, 3), (2, 1), (-1, 2)])
def test_invalid_n_range_raises(bad):
    with pytest.raises(ValueError):
        k.ngram_candidates(["ཆོས"], bad)


def test_ngrams_of_nothing():
    assert k.ngram_candidates([], (1, 4)) == []


# --------------------------------------------------------------------------
# log_likelihood / log_ratio
# --------------------------------------------------------------------------


def test_g2_is_zero_when_the_two_corpora_agree():
    assert k.log_likelihood(10, 10, 100, 100) == pytest.approx(0.0)


def test_g2_matches_the_hand_computed_value():
    # E1 = E2 = 5; G2 = 2 * 10 * ln(10/5)
    assert k.log_likelihood(10, 0, 100, 100) == pytest.approx(2 * 10 * math.log(2))
    # E1 = E2 = 75; G2 = 2 * (100*ln(100/75) + 50*ln(50/75))
    assert k.log_likelihood(100, 50, 10_000, 10_000) == pytest.approx(16.98990366, abs=1e-6)


def test_g2_is_non_negative_and_direction_free():
    """Under-representation is just as significant as over-representation —
    which is why ``keyness`` needs the effect size to tell them apart."""
    assert k.log_likelihood(1, 50, 1000, 1000) > 0


def test_g2_on_degenerate_corpora_returns_zero_instead_of_raising():
    assert k.log_likelihood(0, 0, 0, 0) == 0.0
    assert k.log_likelihood(0, 0, 100, 100) == 0.0
    assert k.log_likelihood(10, 0, 100, 0) == 0.0


def test_log_ratio_sign_and_magnitude():
    assert k.log_ratio(10, 10, 100, 100) == pytest.approx(0.0)
    # 10/100 against a corrected 0.5/100 → twentyfold.
    assert k.log_ratio(10, 0, 100, 100) == pytest.approx(math.log2(20))
    assert k.log_ratio(1, 50, 100, 100) < 0
    assert k.log_ratio(10, 10, 0, 100) == 0.0


# --------------------------------------------------------------------------
# keyness
# --------------------------------------------------------------------------

STUDY = ["བྱང་ཆུབ་སེམས"] * 12 + ["ཆོས"] * 8 + ["ཞིང"] * 2
REFERENCE = ["ཆོས"] * 40 + ["ཞིང"] * 1 + ["རྒྱལ་པོ"] * 160


def test_keyness_ranks_the_term_the_reference_corpus_lacks_first():
    terms = k.keyness(STUDY, REFERENCE, min_freq=3)
    assert terms[0].term == "བྱང་ཆུབ་སེམས"
    assert terms[0].freq_study == 12
    assert terms[0].freq_ref == 0
    assert terms[0].g2 > 0
    assert terms[0].effect > 0


def test_keyness_is_sorted_by_g2_descending():
    terms = k.keyness(STUDY, REFERENCE, min_freq=1)
    assert [t.g2 for t in terms] == sorted((t.g2 for t in terms), reverse=True)


def test_min_freq_applies_to_the_study_corpus_only():
    terms = k.keyness(STUDY, REFERENCE, min_freq=3)
    assert "ཞིང" not in {t.term for t in terms}
    assert "ཞིང" in {t.term for t in k.keyness(STUDY, REFERENCE, min_freq=2)}


def test_positive_only_drops_terms_the_study_corpus_underuses():
    under = ["ཆོས"] * 3 + ["བྱང་ཆུབ་སེམས"] * 97
    reference = ["ཆོས"] * 500 + ["བྱང་ཆུབ་སེམས"] * 1
    assert "ཆོས" not in {t.term for t in k.keyness(under, reference, min_freq=3)}
    kept = k.keyness(under, reference, min_freq=3, positive_only=False)
    assert "ཆོས" in {t.term for t in kept}


def test_boundary_sentinels_and_punctuation_never_reach_the_ranking():
    tokens = k.tokenize("ཆོས།ཆོས།ཆོས།", use_botok=False)
    terms = k.keyness(tokens, min_freq=1)
    assert [t.term for t in terms] == ["ཆོས"]


def test_frequency_only_mode_ranks_by_count_and_reports_no_statistics():
    """With no reference corpus there is no G² to report.  The zeros mean
    'not computed' and the docstring says so; the ordering is still useful."""
    terms = k.keyness(STUDY, None, min_freq=3)
    assert [t.term for t in terms] == ["བྱང་ཆུབ་སེམས", "ཆོས"]
    assert all(t.g2 == 0.0 and t.effect == 0.0 and t.freq_ref == 0 for t in terms)


def test_keyness_of_an_empty_corpus_is_empty():
    assert k.keyness([], REFERENCE) == []
    assert k.keyness([k.BOUNDARY], REFERENCE) == []


def test_keyness_with_an_empty_reference_still_ranks():
    terms = k.keyness(STUDY, [], min_freq=3)
    assert {t.term for t in terms} == {"བྱང་ཆུབ་སེམས", "ཆོས"}
    assert all(t.freq_ref == 0 for t in terms)


def test_ordering_is_deterministic_when_scores_tie():
    study = ["ཀ་ཁ"] * 5 + ["ག་ང"] * 5
    reference = ["ཅ་ཆ"] * 100
    first = [t.term for t in k.keyness(study, reference, min_freq=3)]
    second = [t.term for t in k.keyness(list(reversed(study)), reference, min_freq=3)]
    assert first == second


def test_the_documented_stage_three_pipeline_runs_end_to_end():
    """tokenize → ngram_candidates → keyness, the shape stage 3 actually uses."""
    study_text = (
        "བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། "
        "བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ནི། "
        "བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་སོ། །"
    )
    reference_text = "རྒྱལ་པོ་ཆེན་པོའི་ཕོ་བྲང་དུ། རྒྱལ་པོ་ཆེན་པོའི་བཀའ་ལུང་ངོ་། །"

    study = k.ngram_candidates(k.tokenize(study_text, use_botok=False), (1, 4))
    reference = k.ngram_candidates(k.tokenize(reference_text, use_botok=False), (1, 4))
    terms = k.keyness(study, reference, min_freq=3)

    assert terms, "the repeated phrase should surface as a key term"
    assert "བྱང་ཆུབ་སེམས་དཔའི" in {t.term for t in terms}
    assert all(k.BOUNDARY not in t.term for t in terms)
