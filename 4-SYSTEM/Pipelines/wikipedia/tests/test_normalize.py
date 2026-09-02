"""Tests for the shared normalisation layer.

Every string here is real material from ``corpora/spyodjug/source`` — root
verse 1-1 and the commentary lines that quote it — because the failure modes
this module exists for (bold-wrapped quotations, interleaved block ids,
single-versus-double shad) are things those files actually do.

Offline: no network, no API key, no fixtures on disk except the optional
corpus check at the end of ``test_verify.py``.
"""

from __future__ import annotations

import re
import unicodedata

import pytest

from kangyur_wiki.tibetan import normalize as n

# --------------------------------------------------------------------------
# Real corpus material
# --------------------------------------------------------------------------

#: root.md, verse ^1-1 line 1.
ROOT_L1 = "བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །"
#: root.md, verse ^1-1 line 2 — note ``གུས་པར``.
ROOT_L2 = "ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །"
#: root.md, verse ^1-1 line 4, with its block id.
ROOT_L4 = "ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། ། ^1-1"
#: BCAC14_GDR_bo_segmented.md:87 — the same verse quoted in bold, on one line,
#: with ``གུས་པས``.
GDR_QUOTE = (
    "**བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། ། "
    "ཕྱག་འོས་ཀུན་ལའང་གུས་པས་ཕྱག་འཚལ་ཏེ། །**"
)
#: root.md, the transclusion line that precedes verse ^1-1.
TRANSCLUSION = "![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]"
#: root.md, ^I-1 — head marks and a non-Tibetan-script transliteration.
ROOT_I1 = "༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་སཏྭ་ཙརྱ་ཨ་བ་ཏཱ་ར། ^I-1"

CORPUS_LINES = [ROOT_L1, ROOT_L2, ROOT_L4, GDR_QUOTE, TRANSCLUSION, ROOT_I1]


def _legacy_norm(s: str) -> str:
    """``norm()`` from the vault's ``01_transclude_verses.py``, verbatim.

    Kept here as the oracle: ``fuzzy_key`` is only allowed to differ from the
    implementation that has already been run over ten commentaries in ways we
    can point at.  Applied to single-line inputs, where the original's
    space-only removal and our whitespace removal coincide.
    """
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"!\[\[.*?\]\]", "", s)
    s = re.sub(r"\^[\w-]+", "", s)
    s = s.replace("**", "")
    for ch in ["།", "༎", "་", " ", "༅", "༄", "༈"]:
        s = s.replace(ch, "")
    return s.strip()


# --------------------------------------------------------------------------
# nfc
# --------------------------------------------------------------------------


def test_nfc_is_idempotent_on_corpus_lines():
    for line in CORPUS_LINES:
        assert n.nfc(line) == n.nfc(n.nfc(line))


def test_nfc_reconciles_the_two_spellings_of_a_precomposed_stack():
    """U+0F43 and U+0F42+U+0FB7 are the same syllable, differently encoded.

    Tibetan e-texts mix the two freely.  Without NFC a quotation using one
    spelling fails against a source using the other, which would look exactly
    like a fabricated citation.
    """
    precomposed = "གྷ"
    decomposed = "གྷ"
    assert n.nfc(precomposed) == n.nfc(decomposed)
    assert len(n.nfc(precomposed)) == 2


# --------------------------------------------------------------------------
# collapse
# --------------------------------------------------------------------------


def test_collapse_removes_every_kind_of_whitespace():
    text = f"{ROOT_L1}\n\t {ROOT_L2} "
    out = n.collapse(text)
    assert not any(ch.isspace() for ch in out)
    assert out == n.collapse(ROOT_L1) + n.collapse(ROOT_L2)


def test_collapse_keeps_tibetan_punctuation():
    """The tsheg and shad are orthography, not spacing — dropping them here
    would make ``collapse`` a fuzzy key and destroy the verbatim guarantee."""
    out = n.collapse(ROOT_L1)
    assert n.TSHEG in out
    assert n.SHAD in out
    assert out.count(n.SHAD) == ROOT_L1.count(n.SHAD)


def test_collapse_leaves_markup_alone():
    assert "![[" in n.collapse(TRANSCLUSION)
    assert "**" in n.collapse(GDR_QUOTE)


# --------------------------------------------------------------------------
# strip_markup
# --------------------------------------------------------------------------


def test_strip_markup_removes_transclusions_block_ids_and_bold():
    assert n.strip_markup(TRANSCLUSION) == ""
    assert n.strip_markup(ROOT_L4) == "ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། ། "
    assert "**" not in n.strip_markup(GDR_QUOTE)
    assert "'''" not in n.strip_markup(f"'''{ROOT_L1}'''")


def test_strip_markup_removes_refs_including_attributes_and_self_closing():
    body = f"{ROOT_L1}<ref>ཞི་བ་ལྷ། སྤྱོད་འཇུག</ref>{ROOT_L2}"
    assert n.strip_markup(body) == ROOT_L1 + ROOT_L2

    named = f'{ROOT_L1}<ref name="a">ཁུངས།</ref>{ROOT_L2}<ref name="a" />'
    assert n.strip_markup(named) == ROOT_L1 + ROOT_L2


def test_strip_markup_does_not_eat_the_references_tag():
    """``<references />`` is article structure; the validator's V3 rule has to
    still be able to see it after normalisation."""
    assert "<references />" in n.strip_markup("== ལུང་ཁུངས། ==\n<references />")


def test_strip_markup_preserves_whitespace_and_tibetan_punctuation():
    out = n.strip_markup(f"{ROOT_L1}\n{ROOT_L2}")
    assert "\n" in out
    assert out.count(n.SHAD) == (ROOT_L1 + ROOT_L2).count(n.SHAD)


def test_self_closing_ref_does_not_swallow_a_later_footnote():
    """Regression: an unanchored ``<ref ...>`` pattern matched the self-closing
    form as an opening tag and deleted everything up to the next ``</ref>``."""
    text = f'ཀ<ref name="a" />ཁ<ref>ག</ref>ང'
    assert n.strip_markup(text) == "ཀཁང"


# --------------------------------------------------------------------------
# fuzzy_key
# --------------------------------------------------------------------------


@pytest.mark.parametrize("line", CORPUS_LINES)
def test_fuzzy_key_matches_the_proven_legacy_norm(line):
    assert n.fuzzy_key(line) == _legacy_norm(line)


def test_fuzzy_key_collapses_a_bold_single_line_quotation_onto_the_root():
    """The GDR commentary quotes the verse in bold on one line; the root has it
    on two.  Only ``གུས་པར``/``གུས་པས`` should still separate them."""
    root = f"{ROOT_L1}\n{ROOT_L2}"
    assert n.fuzzy_key(root) != n.fuzzy_key(GDR_QUOTE)
    assert n.fuzzy_key(root.replace("གུས་པར", "གུས་པས")) == n.fuzzy_key(GDR_QUOTE)


def test_fuzzy_key_ignores_shad_count_and_head_marks():
    assert n.fuzzy_key("ཏེ།") == n.fuzzy_key("ཏེ། །")
    assert n.fuzzy_key("༄༅། །ཆོས།") == n.fuzzy_key("ཆོས")


# --------------------------------------------------------------------------
# Offset maps
# --------------------------------------------------------------------------


def _assert_map_is_sound(source: str, reduced: str, index, plain: str) -> None:
    normalised = n.nfc(source)
    assert reduced == plain
    assert len(index) == len(reduced)
    assert list(index) == sorted(set(index))
    for position, ch in zip(index, reduced):
        assert normalised[position] == ch


def test_collapse_with_map_points_back_at_the_original_characters():
    source = f"{TRANSCLUSION}\n\n{ROOT_L1}\n{ROOT_L2} ^1-1\n"
    reduced, index = n.collapse_with_map(source)
    _assert_map_is_sound(source, reduced, index, n.collapse(source))


def test_fuzzy_key_with_map_points_back_at_the_original_characters():
    source = f"{TRANSCLUSION}\n\n{GDR_QUOTE}\n{ROOT_I1}\n"
    reduced, index = n.fuzzy_key_with_map(source)
    _assert_map_is_sound(source, reduced, index, n.fuzzy_key(source))


def test_map_indexes_the_nfc_form_when_the_source_is_not_normalised():
    """A precomposed stack becomes two characters under NFC, so offsets shift.
    They must track the string the comparison actually ran against."""
    source = "གྷ" + ROOT_L1
    reduced, index = n.collapse_with_map(source)
    assert n.nfc(source)[index[0]] == reduced[0]
    assert index[2] == 2  # the stack occupies indices 0 and 1 after NFC


def test_maps_are_empty_for_empty_input():
    reduced, index = n.collapse_with_map("")
    assert reduced == ""
    assert len(index) == 0


# --------------------------------------------------------------------------
# syllables
# --------------------------------------------------------------------------


def test_syllables_splits_on_tsheg_and_keeps_terminal_punctuation():
    assert n.syllables("བྱང་ཆུབ་སེམས་དཔའ།") == ["བྱང", "ཆུབ", "སེམས", "དཔའ།"]


def test_syllables_drops_empties_from_doubled_and_trailing_tsheg():
    assert n.syllables("ཆོས་་ཉིད་") == ["ཆོས", "ཉིད"]
    assert n.syllables("་") == []
    assert n.syllables("") == []


def test_syllables_does_not_split_the_non_breaking_tsheg():
    """U+0F0C exists to mark a junction that must *not* break; splitting on it
    would defeat its only purpose."""
    assert n.syllables("དང༌ཆོས") == ["དང༌ཆོས"]


def test_syllables_counts_a_real_verse_line():
    """Nine syllables plus a punctuation-only unit: the scribe wrote a tsheg
    before the closing shads, so they split off.  Documented behaviour — the
    split is on the tsheg and nothing is inferred."""
    units = n.syllables(ROOT_L1)
    assert units[:9] == [
        "བདེ", "གཤེགས", "ཆོས", "ཀྱི", "སྐུ", "མངའ", "སྲས", "བཅས", "དང",
    ]
    assert units[9] == "། །"
