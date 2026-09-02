"""Tests for the verbatim-quotation checker.

The three tiers are tested against the situations that actually produce them in
this corpus: a commentary that wraps its root quotation in ``**bold**``, a root
file that interleaves ``^1-1`` block ids, editions that write one shad where
another writes two, and the ``གུས་པར``/``གུས་པས`` split in Bodhicaryāvatāra 1.1
that separates the root text from three of its commentaries.

Offline throughout.  The last test reads two files from ``corpora/`` and skips
when they are absent.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from kangyur_wiki.tibetan import normalize as n
from kangyur_wiki.tibetan import verify as v

# --------------------------------------------------------------------------
# Real corpus material
# --------------------------------------------------------------------------

ROOT_L1 = "བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །"
ROOT_L2 = "ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །"
ROOT_VERSE = f"{ROOT_L1}\n{ROOT_L2}"

#: BCAC14_GDR_bo_segmented.md:87 — bold, one line, and ``གུས་པས``.
GDR_QUOTE = (
    "**བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། ། "
    "ཕྱག་འོས་ཀུན་ལའང་གུས་པས་ཕྱག་འཚལ་ཏེ། །**"
)

#: A root-file shape: transclusion line, verse, block id.
ROOT_FILE = (
    "## 1. ལེའུ་དང་པོ། ^1-0\n\n"
    "![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]\n\n"
    f"{ROOT_L1}\n{ROOT_L2} ^1-1\n"
)

CORPUS = Path(__file__).resolve().parents[1] / "corpora" / "spyodjug" / "source"


# --------------------------------------------------------------------------
# exact
# --------------------------------------------------------------------------


def test_exact_hit_reports_a_usable_offset():
    check = v.check_quote(ROOT_L1, ROOT_FILE, "root.md")
    assert check.method == v.METHOD_EXACT
    assert check.found and check.passed and not check.warning
    assert check.ratio == 1.0
    assert ROOT_FILE[check.char_offset : check.char_offset + len(ROOT_L1)] == ROOT_L1


def test_exact_hit_inside_bold_markup():
    """The commentary's ``**`` wrapper sits outside the quoted span, so a
    single-line quotation is still literally verbatim."""
    check = v.check_quote(ROOT_L1, GDR_QUOTE, "gdr.md")
    assert check.method == v.METHOD_EXACT
    assert check.char_offset == 2


def test_short_quote_is_noted_but_still_passes():
    check = v.check_quote("ཆོས་", ROOT_FILE, "root.md")
    assert check.passed
    assert "short quote" in check.note


# --------------------------------------------------------------------------
# collapsed
# --------------------------------------------------------------------------


def test_line_break_difference_is_a_pass_with_a_mapped_offset():
    """The article quotes the verse as one run; the file wraps it at the shad.
    Same text — and the offset must still land on it in the *original*."""
    quote = f"{ROOT_L1}{ROOT_L2}"
    check = v.check_quote(quote, ROOT_FILE, "root.md")
    assert check.method == v.METHOD_COLLAPSED
    assert check.passed
    assert check.ratio == 1.0
    assert n.collapse(ROOT_FILE[check.char_offset :]).startswith(n.collapse(quote))


def test_collapsed_offset_is_exact_not_approximate():
    check = v.check_quote(f"{ROOT_L1} {ROOT_L2}", ROOT_FILE, "root.md")
    assert ROOT_FILE.index(ROOT_L1) == check.char_offset


# --------------------------------------------------------------------------
# fuzzy — a warning, never a pass
# --------------------------------------------------------------------------


def test_block_id_inside_the_quoted_span_downgrades_to_fuzzy():
    """A root file interleaves ``^1-1`` markers.  The letters are all there,
    but the article is not quoting the file byte for byte, so a human looks."""
    source = "ཞེས་ བྱང་ཆུབ་སེམས་དཔའི་ ^1-1\nསྤྱོད་པ། གསུངས།"
    check = v.check_quote("བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ།", source, "root.md")
    assert check.method == v.METHOD_FUZZY
    assert check.found is True
    assert check.passed is False, "a fuzzy hit must never satisfy V1"
    assert check.warning is True
    assert 0.8 < check.ratio < 1.0
    assert check.char_offset == source.index("བྱང")


def test_single_versus_double_shad_downgrades_to_fuzzy():
    check = v.check_quote("ཕྱག་འོས་ཀུན་ལའང་གུས་པས་ཕྱག་འཚལ་ཏེ། །", "ཕྱག་འོས་ཀུན་ལའང་གུས་པས་ཕྱག་འཚལ་ཏེ།", "c.md")
    assert check.method == v.METHOD_FUZZY
    assert check.ratio > 0.9


def test_a_quote_too_short_to_judge_is_not_fuzzy_matched():
    """Below ``MIN_FUZZY_KEY_LEN`` a punctuation-free key matches half the
    Kangyur; reporting that as a near-miss would be worse than useless."""
    check = v.check_quote("ཆོས།", "ཆོས་ཉིད་ཀྱི་དབྱིངས།", "c.md")
    assert check.method == v.METHOD_MISSING


# --------------------------------------------------------------------------
# missing
# --------------------------------------------------------------------------


def test_a_one_letter_variant_fails_and_says_how_close_it_came():
    """Bodhicaryāvatāra 1.1: the root reads ``གུས་པར``, GDR reads ``གུས་པས``.
    One letter, so no tier may pass it — and the ratio has to be high enough
    that a reviewer sees it is an edition difference, not a fabrication."""
    check = v.check_quote(ROOT_VERSE, GDR_QUOTE, "gdr.md")
    assert check.method == v.METHOD_MISSING
    assert not check.found and not check.passed
    assert check.char_offset is None
    assert 0.5 < check.ratio < 1.0


def test_unrelated_text_scores_near_zero():
    check = v.check_quote("སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །", "ཀུན་མཁྱེན་འཚོ་སྣ་བས་མཛད་པར་གྲགས།", "c.md")
    assert check.method == v.METHOD_MISSING
    assert check.ratio < 0.5


def test_empty_quote_is_a_failure_not_a_free_pass():
    """``"" in text`` is True; a checker that trusts substring semantics
    blindly reports every empty extraction as verified."""
    for quote in ("", "   ", "\n\t"):
        check = v.check_quote(quote, ROOT_FILE, "root.md")
        assert check.method == v.METHOD_MISSING
        assert not check.found
        assert "empty" in check.note


def test_empty_source_fails_every_quote():
    check = v.check_quote(ROOT_L1, "", "empty.md")
    assert check.method == v.METHOD_MISSING
    assert check.ratio == 0.0


# --------------------------------------------------------------------------
# Normalisation-form independence
# --------------------------------------------------------------------------


def test_a_precomposed_stack_matches_its_decomposed_spelling():
    """The source writes ``གྷ`` as U+0F43, the article as U+0F42 U+0FB7.  Same
    syllable; only NFC makes them comparable — and the reported offset indexes
    the NFC form, which is one character longer than the raw file here."""
    source = "ཞེས་གྷ་ན་" + ROOT_L1
    check = v.check_quote("གྷ་ན་", source, "c.md")
    assert check.method == v.METHOD_EXACT
    normalised = n.nfc(source)
    assert normalised[check.char_offset : check.char_offset + 2] == "གྷ"
    assert len(normalised) == len(source) + 1


# --------------------------------------------------------------------------
# check_quotes
# --------------------------------------------------------------------------


def test_check_quotes_preserves_order_and_loads_each_source_once():
    loaded: list[str] = []

    def loader(path: str) -> str:
        loaded.append(path)
        return {"root.md": ROOT_FILE, "gdr.md": GDR_QUOTE}[path]

    checks = v.check_quotes(
        [
            (ROOT_L1, "root.md"),
            (ROOT_VERSE, "gdr.md"),
            (f"{ROOT_L1}{ROOT_L2}", "root.md"),
        ],
        loader,
    )

    assert loaded == ["root.md", "gdr.md"]
    assert [c.method for c in checks] == [
        v.METHOD_EXACT,
        v.METHOD_MISSING,
        v.METHOD_COLLAPSED,
    ]
    assert [c.source_path for c in checks] == ["root.md", "gdr.md", "root.md"]


def test_an_unreadable_source_fails_that_citation_and_not_the_run():
    attempts: list[str] = []

    def loader(path: str) -> str:
        attempts.append(path)
        if path == "gone.md":
            raise FileNotFoundError(path)
        return ROOT_FILE

    checks = v.check_quotes(
        [(ROOT_L1, "gone.md"), (ROOT_L2, "gone.md"), (ROOT_L1, "root.md")], loader
    )

    assert attempts == ["gone.md", "root.md"], "the failure must be cached too"
    assert [c.method for c in checks[:2]] == [v.METHOD_MISSING, v.METHOD_MISSING]
    assert all("gone.md" in c.note for c in checks[:2])
    assert checks[2].passed


def test_check_quotes_on_an_empty_batch():
    assert v.check_quotes([], lambda path: "") == []


# --------------------------------------------------------------------------
# Against the real corpus
# --------------------------------------------------------------------------


@pytest.mark.skipif(
    not (CORPUS / "commentaries" / "BCAC14_GDR_bo_segmented.md").exists(),
    reason="corpora/spyodjug not present",
)
def test_real_verse_against_two_real_commentaries():
    """The production case, end to end on multi-megabyte files.

    Verse 1.1 is verbatim in the Thogs med bzang po commentary and one letter
    away in the Gyaltsab commentary.  A verifier that passed the second would
    be certifying a quotation the reader cannot find.
    """
    tg = (CORPUS / "commentaries" / "BCAC20_TG_bo.toc.md").read_text(encoding="utf-8")
    gdr = (CORPUS / "commentaries" / "BCAC14_GDR_bo_segmented.md").read_text(encoding="utf-8")

    hit = v.check_quote(ROOT_VERSE, tg, "BCAC20_TG_bo.toc.md")
    assert hit.passed
    assert tg[hit.char_offset : hit.char_offset + len(ROOT_L1)] == ROOT_L1

    miss = v.check_quote(ROOT_VERSE, gdr, "BCAC14_GDR_bo_segmented.md")
    assert not miss.passed
    assert miss.ratio > 0.5

    # The same line without the variant syllable *is* in the Gyaltsab file.
    assert v.check_quote(ROOT_L1, gdr, "BCAC14_GDR_bo_segmented.md").passed
