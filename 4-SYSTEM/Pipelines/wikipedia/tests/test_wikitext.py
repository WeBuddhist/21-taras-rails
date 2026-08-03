"""Golden-file tests for the canonical wikitext emitter.

Offline by construction: the emitter is a pure function of its arguments, so
every test here is an equality assertion against a literal expected string.
That is deliberate — the point of moving markup decisions out of the model and
into code is that they become diffable.
"""

from __future__ import annotations

import unicodedata
from urllib.parse import unquote

import pytest

from kangyur_wiki.wiki.wikitext import (
    CATEGORY_NAMESPACE,
    HEADING_BIBLIOGRAPHY,
    HEADING_REFERENCES,
    HEADING_SEE_ALSO,
    REFERENCES_TAG,
    SHAD,
    TAIL_HEADINGS,
    TSHEG,
    Article,
    Citation,
    Section,
    citation_url,
    format_bibliography_entry,
    join_boundary,
    render_article,
    render_bold,
    render_category,
    render_heading,
    render_lead,
    render_ref,
    render_ref_body,
    render_ref_reuse,
    render_section,
    render_wikilink,
    syllable_count,
    syllable_spans,
    syllables,
    text_fragment,
    wikilink_target,
)

# --------------------------------------------------------------------------
# Fixture material
# --------------------------------------------------------------------------

BCA = Citation(
    source_id="bca",
    author="ཞི་བ་ལྷ",
    title="སྤྱོད་འཇུག",
    year="༡༩༩༠",
    page="༡༢",
    url="https://wikisource.org/wiki/BCA",
)

KUNPAL = Citation(
    source_id="kunpal",
    author="མཁན་པོ་ཀུན་དཔལ",
    title="ཚིག་འགྲེལ",
    year="༢༠༠༧",
    page="༥༥",
    url="https://wikisource.org/wiki/KP",
)

UNLINKED = Citation(
    source_id="oral",
    author="མཁས་དབང་ཚུལ་ཁྲིམས",
    title="ཞལ་ལུང",
)

SECONDARY = Citation(
    source_id="williams",
    author="Williams, Paul",
    title="Mahayana Buddhism",
    year="2008",
    isbn="9780415356534",
)

GOLDEN_ARTICLE = "\n".join(
    [
        "'''བྱང་ཆུབ་སེམས་'''ནི་ཐེག་པ་ཆེན་པོའི་གནད་ཀྱི་ཐ་སྙད་ཅིག་ཡིན།"
        "<ref>[https://wikisource.org/wiki/BCA ཞི་བ་ལྷ། སྤྱོད་འཇུག། ཤོག་གྲངས་༡༢]</ref>",
        "",
        "== ངེས་ཚིག ==",
        "ངེས་ཚིག་གི་སྒོ་ནས་བཤད་ན།"
        '<ref name="kp">[https://wikisource.org/wiki/KP མཁན་པོ་ཀུན་དཔལ། ཚིག་འགྲེལ། ཤོག་གྲངས་༥༥]</ref>',
        "",
        "== དབྱེ་བ། ==",
        'དབྱེ་ན་གཉིས་ཡོད་དེ།<ref name="kp" />',
        "",
        "== འབྲེལ་ཡོད་ཤོག་ངོས། ==",
        "* [[སེམས་བསྐྱེད་]]",
        "",
        "== ལུང་ཁུངས། ==",
        "<references />",
        "",
        "== དཔྱད་གཞིའི་ཡིག་ཆ། ==",
        "* ཞི་བ་ལྷ། སྤྱོད་འཇུག། ༡༩༩༠།",
        "",
        "[[རིགས་དབྱེ།:ནང་བསྟན།]]",
    ]
)


def build_article() -> Article:
    """The known-good article, assembled the way the draft stage assembles it."""
    return Article(
        term="བྱང་ཆུབ་སེམས",
        lead=[
            "ནི་ཐེག་པ་ཆེན་པོའི་གནད་ཀྱི་ཐ་སྙད་ཅིག་ཡིན།" + render_ref(BCA),
        ],
        sections=[
            Section(
                heading="ངེས་ཚིག",
                paragraphs=["ངེས་ཚིག་གི་སྒོ་ནས་བཤད་ན།" + render_ref(KUNPAL, name="kp")],
            ),
            Section(
                heading="དབྱེ་བ།",
                paragraphs=["དབྱེ་ན་གཉིས་ཡོད་དེ།" + render_ref_reuse("kp")],
            ),
        ],
        see_also=["སེམས་བསྐྱེད་"],
        citations=[BCA, KUNPAL],
        bibliography=[format_bibliography_entry(BCA)],
        categories=["ནང་བསྟན།"],
    )


# --------------------------------------------------------------------------
# Value objects
# --------------------------------------------------------------------------


def test_citation_normalises_to_nfc_and_strips():
    decomposed = unicodedata.normalize("NFD", "ཞི་བ་ལྷ")
    citation = Citation(source_id=" bca ", author=decomposed, year=1990)
    assert citation.source_id == "bca"
    assert citation.author == unicodedata.normalize("NFC", decomposed)
    assert citation.year == "1990"


def test_citation_requires_a_source_id():
    with pytest.raises(ValueError, match="source_id"):
        Citation(source_id="")


def test_citation_routing_flags():
    assert not BCA.is_secondary
    assert BCA.is_linked
    assert BCA.has_full_metadata
    assert SECONDARY.is_secondary
    assert not UNLINKED.is_linked
    assert not UNLINKED.has_full_metadata


def test_section_detects_its_own_citations():
    assert Section("དབྱེ་བ།", ["ཡོད།<ref>x</ref>"]).has_citation
    assert not Section("དབྱེ་བ།", ["ཡོད།"]).has_citation
    # <references /> is not a citation, and must not be mistaken for one.
    assert not Section("དབྱེ་བ།", [REFERENCES_TAG]).has_citation


def test_section_accepts_heading_with_or_without_markers():
    assert Section("== དབྱེ་བ། ==").heading == "དབྱེ་བ།"
    assert Section("དབྱེ་བ།").heading == "དབྱེ་བ།"


def test_section_rejects_impossible_levels():
    with pytest.raises(ValueError):
        Section("དབྱེ་བ།", level=1)


def test_article_splits_a_string_lead_on_blank_lines():
    article = Article(term="སེམས", lead="དང་པོ།\n\nགཉིས་པ།")
    assert article.lead == ("དང་པོ།", "གཉིས་པ།")


# --------------------------------------------------------------------------
# ཚེག་བར segmentation
# --------------------------------------------------------------------------


def test_syllable_count_counts_tsheg_bar():
    assert syllable_count("བྱང་ཆུབ་སེམས་དཔའ།") == 4
    assert syllable_count("") == 0


def test_syllable_spans_are_literal_substrings_in_order():
    text = "༄༅། བྱང་ཆུབ་སེམས་དཔའ། །གཞན།"
    spans = syllable_spans(text)
    # Every span is a literal slice, and slicing across spans reconstructs a
    # contiguous run — the property text fragments depend on.
    assert "".join(text[start:end] for start, end in spans) == text[spans[0][0] :]
    assert text[spans[0][0] : spans[1][1]] == "བྱང་ཆུབ་"


def test_syllables_carry_their_delimiter():
    assert syllables("བྱང་ཆུབ་") == ["བྱང་", "ཆུབ་"]


# --------------------------------------------------------------------------
# Text fragments
# --------------------------------------------------------------------------


def test_text_fragment_encodes_a_short_quote_whole():
    fragment = text_fragment("བྱང་ཆུབ་སེམས་")
    assert fragment.startswith("#:~:text=")
    assert "," not in fragment
    assert unquote(fragment[len("#:~:text=") :]) == "བྱང་ཆུབ་སེམས་"


def test_text_fragment_splits_a_long_quote_into_start_and_end():
    quote = TSHEG.join(f"ས{index}" for index in range(20)) + TSHEG
    fragment = text_fragment(quote, syllables_n=6)
    head, tail = fragment[len("#:~:text=") :].split(",")
    assert unquote(head).count(TSHEG) == 6
    assert unquote(tail).count(TSHEG) == 6
    assert quote.startswith(unquote(head))
    assert quote.endswith(unquote(tail))


def test_text_fragment_boundary_is_twice_n():
    twelve = TSHEG.join(f"ས{index}" for index in range(12)) + TSHEG
    thirteen = TSHEG.join(f"ས{index}" for index in range(13)) + TSHEG
    assert "," not in text_fragment(twelve)
    assert "," in text_fragment(thirteen)


def test_text_fragment_escapes_the_hyphen():
    """An unescaped '-' is the fragment syntax's prefix/suffix marker."""
    assert "%2D" in text_fragment("a-b")
    assert "-" not in text_fragment("a-b")[len("#:~:text=") :]


def test_text_fragment_collapses_internal_whitespace():
    assert text_fragment("བྱང་\n  ཆུབ་") == text_fragment("བྱང་ ཆུབ་")


def test_text_fragment_rejects_an_unanchorable_quote():
    with pytest.raises(ValueError):
        text_fragment("   ")


def test_citation_url_appends_the_anchor_only_once():
    quoted = Citation(source_id="x", url="https://example.org/a", quote="བྱང་ཆུབ་")
    assert citation_url(quoted).startswith("https://example.org/a#:~:text=")
    assert citation_url(quoted, anchor=False) == "https://example.org/a"

    prefragmented = Citation(
        source_id="x", url="https://example.org/a#already", quote="བྱང་ཆུབ་"
    )
    assert citation_url(prefragmented) == "https://example.org/a#already"


# --------------------------------------------------------------------------
# Inline markup and the tsheg boundary
# --------------------------------------------------------------------------


def test_join_boundary_inserts_a_tsheg_only_when_missing():
    assert join_boundary("'''སེམས་'''", "ནི་") == "'''སེམས་'''ནི་"
    assert join_boundary("'''སེམས'''", "་ནི་") == "'''སེམས'''་ནི་"
    assert join_boundary("'''སེམས'''", "ནི་") == "'''སེམས'''་ནི་"


def test_join_boundary_leaves_non_tibetan_continuations_alone():
    assert join_boundary("'''སེམས'''", " ཞེས།") == "'''སེམས''' ཞེས།"
    assert join_boundary("'''སེམས'''", SHAD) == "'''སེམས'''" + SHAD


def test_render_bold_does_not_edit_punctuation():
    assert render_bold("སེམས") == "'''སེམས'''"
    with pytest.raises(ValueError):
        render_bold("'''སེམས'''")


def test_wikilink_target_takes_a_tsheg_and_drops_the_shad():
    assert wikilink_target("རྡོ་རྗེ།") == "རྡོ་རྗེ་"
    assert wikilink_target("རྡོ་རྗེ") == "རྡོ་རྗེ་"
    assert wikilink_target("རྡོ་རྗེ་") == "རྡོ་རྗེ་"


def test_render_wikilink_pipes_only_when_the_display_differs():
    assert render_wikilink("རྡོ་རྗེ།") == "[[རྡོ་རྗེ་]]"
    assert render_wikilink("རྡོ་རྗེ་", "རྡོ་རྗེ་") == "[[རྡོ་རྗེ་]]"
    assert render_wikilink("རྡོ་རྗེ།", "རྡོ་རྗེ།") == "[[རྡོ་རྗེ་|རྡོ་རྗེ།]]"


def test_render_lead_keeps_the_tsheg_inside_the_bold():
    assert (
        render_lead("བྱང་ཆུབ་སེམས", "ནི་ཡིན།") == "'''བྱང་ཆུབ་སེམས་'''ནི་ཡིན།"
    )
    assert (
        render_lead("བྱང་ཆུབ་སེམས", "་ནི་ཡིན།") == "'''བྱང་ཆུབ་སེམས'''་ནི་ཡིན།"
    )
    assert render_lead("བྱང་ཆུབ་སེམས་", "ནི་ཡིན།") == "'''བྱང་ཆུབ་སེམས་'''ནི་ཡིན།"


def test_render_lead_respects_a_lead_that_is_already_bolded():
    assert render_lead("སེམས", "'''སེམས་'''ནི་ཡིན།") == "'''སེམས་'''ནི་ཡིན།"


def test_render_lead_does_not_duplicate_a_body_that_opens_with_the_term():
    # A natural lead sentence opens with the term; bolding must wrap that
    # occurrence, not prepend a second copy (observed on every tara21 draft:
    # `'''སྒྲོལ་མ་'''སྒྲོལ་མ་ཞེས་པའི་...`).
    assert (
        render_lead("སྒྲོལ་མ", "སྒྲོལ་མ་ཞེས་པའི་མིང་གི་ངེས་ཚིག་ནི།")
        == "'''སྒྲོལ་མ་'''ཞེས་པའི་མིང་གི་ངེས་ཚིག་ནི།"
    )
    # Any following particle stays grammatical: the bold replaces the copy.
    assert render_lead("སྡུག་བསྔལ", "སྡུག་བསྔལ་ནི་ཡིན།") == "'''སྡུག་བསྔལ་'''ནི་ཡིན།"
    # A body that IS the bare term must not be stripped to nothing.
    assert render_lead("སེམས", "སེམས") == "'''སེམས་'''སེམས"
    # A body opening with a *different* word keeps the prepend behavior.
    assert render_lead("སེམས", "ནི་ཡིན།") == "'''སེམས་'''ནི་ཡིན།"


# --------------------------------------------------------------------------
# References
# --------------------------------------------------------------------------


def test_render_ref_primary_is_hand_formatted():
    assert render_ref(BCA) == (
        "<ref>[https://wikisource.org/wiki/BCA ཞི་བ་ལྷ། སྤྱོད་འཇུག། ཤོག་གྲངས་༡༢]</ref>"
    )


def test_render_ref_without_a_url_drops_the_link_but_keeps_the_source():
    assert render_ref(UNLINKED) == "<ref>མཁས་དབང་ཚུལ་ཁྲིམས། ཞལ་ལུང།</ref>"


def test_render_ref_appends_the_passage_anchor_when_a_quote_is_present():
    quoted = Citation(
        source_id="bca",
        author="ཞི་བ་ལྷ",
        title="སྤྱོད་འཇུག",
        url="https://wikisource.org/wiki/BCA",
        quote="བྱང་ཆུབ་སེམས་",
    )
    assert "#:~:text=" in render_ref(quoted)
    assert "#:~:text=" not in render_ref(quoted, anchor=False)


def test_render_ref_uses_cs1_only_for_a_source_with_an_isbn():
    assert render_ref(SECONDARY) == (
        "<ref>{{Cite book |last=Williams |first=Paul |title=Mahayana Buddhism "
        "|year=2008 |isbn=9780415356534 }}</ref>"
    )


def test_render_ref_cs1_carries_the_page_when_known():
    with_page = Citation(
        source_id="w", author="Williams, Paul", isbn="9780415356534", page="41"
    )
    assert "|pages=41" in render_ref_body(with_page)


def test_named_ref_first_use_carries_content_and_later_uses_do_not():
    assert render_ref(BCA, name="bca").startswith('<ref name="bca">')
    assert render_ref(BCA, name="bca", first_use=False) == '<ref name="bca" />'
    assert render_ref_reuse("bca") == '<ref name="bca" />'


def test_reused_ref_must_be_named():
    with pytest.raises(ValueError):
        render_ref(BCA, first_use=False)


def test_ref_name_rejects_characters_that_break_the_tag():
    with pytest.raises(ValueError):
        render_ref(BCA, name='bad"name')


def test_format_bibliography_entry():
    assert format_bibliography_entry(BCA) == "ཞི་བ་ལྷ། སྤྱོད་འཇུག། ༡༩༩༠།"


# --------------------------------------------------------------------------
# Blocks
# --------------------------------------------------------------------------


def test_render_heading_leaves_heading_punctuation_alone():
    # ངེས་ཚིག carries no shad; every other canonical heading does.  Adding one
    # would create a section title that matches no exemplar.
    assert render_heading("ངེས་ཚིག") == "== ངེས་ཚིག =="
    assert render_heading("མཚན་ཉིད།") == "== མཚན་ཉིད། =="
    assert render_heading("དབྱེ་བ།", 3) == "=== དབྱེ་བ། ==="


def test_render_section():
    section = Section("དབྱེ་བ།", ["དང་པོ།", "གཉིས་པ།"])
    assert render_section(section) == "== དབྱེ་བ། ==\nདང་པོ།\n\nགཉིས་པ།"


def test_render_category_strips_a_redundant_namespace():
    assert render_category("ནང་བསྟན།") == f"[[{CATEGORY_NAMESPACE}:ནང་བསྟན།]]"
    assert render_category("Category:ནང་བསྟན།") == f"[[{CATEGORY_NAMESPACE}:ནང་བསྟན།]]"


# --------------------------------------------------------------------------
# The whole article
# --------------------------------------------------------------------------


def test_render_article_matches_the_golden_skeleton():
    assert render_article(build_article()) == GOLDEN_ARTICLE


def test_render_article_emits_references_never_reflist():
    """bo.wikipedia's {{Reflist}} injects its own == ཡོང་ཁུངས། == heading."""
    rendered = render_article(build_article())
    assert f"== {HEADING_REFERENCES} ==\n{REFERENCES_TAG}" in rendered
    assert "Reflist" not in rendered


def test_render_article_puts_the_three_tail_sections_last_and_in_order():
    rendered = render_article(build_article())
    positions = [rendered.index(f"== {heading} ==") for heading in TAIL_HEADINGS]
    assert positions == sorted(positions)
    assert rendered.index("== ངེས་ཚིག ==") < positions[0]
    assert HEADING_BIBLIOGRAPHY in rendered
    assert HEADING_SEE_ALSO in rendered


def test_render_article_drops_a_section_with_no_citation():
    """Rule 10 of the 27-rule prompt: never invent a section."""
    article = build_article()
    padded = Article(
        term=article.term,
        lead=article.lead,
        sections=list(article.sections) + [Section("མཚན་ཉིད།", ["ལུང་ཁུངས་མེད་པ།"])],
        see_also=article.see_also,
        citations=article.citations,
        bibliography=article.bibliography,
        categories=article.categories,
    )
    assert "མཚན་ཉིད།" not in render_article(padded)


def test_render_article_omits_the_reference_section_when_there_are_no_refs():
    """Rule V3 is an 'iff': no <ref> means no empty reference section either."""
    article = Article(
        term="སེམས",
        lead=["ནི་ཡིན།"],
        categories=["ནང་བསྟན།"],
    )
    rendered = render_article(article)
    assert REFERENCES_TAG not in rendered
    assert HEADING_REFERENCES not in rendered


def test_render_article_output_is_nfc():
    rendered = render_article(build_article())
    assert rendered == unicodedata.normalize("NFC", rendered)
