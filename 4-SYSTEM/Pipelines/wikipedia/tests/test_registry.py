"""Offline tests for the source/term registry.

The fixtures below are miniatures of the real སྤྱོད་འཇུག tab and reproduce its
four hazards deliberately: ragged rows, URLs that exist only in the hyperlink
relation, a header repeated mid-sheet, and hyperlink refs that drift out of step
with the exported row list because blank rows were dropped.  Every one of those
was found in the live export, and each has its own test — a fixture that is
tidier than the real sheet would prove nothing.
"""

from __future__ import annotations

import json
import sys
import types

import pytest

from kangyur_wiki.registry import (
    Registry,
    Source,
    TermRecord,
    align_link_rows,
    bdrc_show_url,
    classify_url,
    find_split_index,
    find_term,
    iter_terms,
    load,
    load_from_xlsx_export,
    resolve_citation_url,
    save,
    term_key,
    unwrap_google_redirect,
)

# --------------------------------------------------------------------------
# Fixtures — a miniature of the real sheet
# --------------------------------------------------------------------------

WIKISOURCE_INDEX = "https://wikisource.org/wiki/Index:%E0%BD%A6%E0%BE%A4.pdf"
WIKISOURCE_TEXT = "https://wikisource.org/wiki/%E0%BD%A6%E0%BE%A4%E0%BE%B1"
COMMONS_FILE = "https://commons.wikimedia.org/wiki/File:Spyod.pdf"
DRIVE_SCAN = "https://drive.google.com/file/d/1iC60RA33/view?usp=drive_link"
WIKIDATA = "https://www.wikidata.org/wiki/Q2735624"

#: Google Sheets wraps external links in its own redirector and encodes the
#: target a second time.  This is a real value from the export, shortened.
WRAPPED_BDE = (
    "https://www.google.com/url?q=https://bo.wikipedia.org/wiki/"
    "%25E0%25BD%2596%25E0%25BD%2591%25E0%25BD%25BA%25E0%25BC%258B"
    "&sa=D&source=editors&ust=1754009172364777&usg=AOvVaw3"
)
UNWRAPPED_BDE = "https://bo.wikipedia.org/wiki/%E0%BD%96%E0%BD%91%E0%BD%BA%E0%BC%8B"

REDLINK = "https://bo.wikipedia.org/w/index.php?title=%E0%BD%A6%E0%BE%B2%E0%BD%A6%E0%BC%8B&action=edit&redlink=1"


@pytest.fixture()
def tab_rows() -> list[dict[str, str]]:
    """Exported cell text: ragged rows, a mid-sheet header, no blank rows.

    Row 4 of the real sheet is blank and therefore absent here, which is what
    makes the hyperlink refs in ``tab_links`` drift by one from row 5 onward.
    """
    return [
        # 1 — source header
        {
            "A": "ཨང་།",
            "B": "མཚན་བྱང་།",
            "C": "མཛད་པ་པོ།",
            "D": "གཞུང་ཁོངས།",
            "E": "པར་རིགས། Version",
            "F": "ཡིག་རྐྱང་དྲ་ཐག",
            "G": "Wikisource Link",
            "N": "WikiDataཝི་ཀི་གནས་མཛོད།",
            "O": "Wikipedia",
            "P": "Status",
        },
        # 2 — five cells, no links at all
        {
            "A": "1.0",
            "B": "སྤྱོད་འཇུག་གི་རྣམ་བཤད་རྒྱལ་སྲས་འཇུག་ངོགས།",
            "C": "རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།",
            "D": "བོད་གཞུང་།",
            "E": "ཤིང་དཔར།",
        },
        # 3 — URLs live in the relation; the cells just say "Link"
        {
            "A": "2.0",
            "B": "སྤྱོད་འཇུག་གི་འགྲེལ་པ་ལེགས་བཤད་རྒྱ་མཚོ།",
            "C": "རྒྱལ་སྲས་ཐོགས་མེད་བཟང་པོ།",
            "D": "བོད་གཞུང་།",
            "F": "Link",
            "G": "Link",
            "P": "ཤོག་ངོས་འདི་ཉར་རྒྱུ་ཡིན།",
        },
        # 4 (sheet row 5) — thirteen cells, URLs as visible text, BDRC id
        {
            "A": "3.0",
            "B": "བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།",
            "C": "རྒྱལ་སྲས་ཞི་བ་ལྷ།",
            "D": "WA0RK0529",
            "E": "བཟོས་ཟིན།",
            "F": WIKISOURCE_INDEX,
            "G": WIKISOURCE_TEXT,
            "H": COMMONS_FILE,
            "N": WIKIDATA,
        },
        # 5 (sheet row 6) — the term header, repeated mid-sheet
        {
            "A": "ཨང་།",
            "B": "སྤྱོད་འཇུག་རྩ་འགྲེལ་ནས་བཏོན་པའི་གནད་ཚིག་གཤམ་གསལ།",
            "C": "རྩོམ་སྒྲིག་མཁན།",
            "D": "རྩོམ་སྒྲིག་གནས་བབ།",
            "E": "ཝེ་ཁེ་རིག་མཛོད་ཀྱི་དྲ་ཐག Link",
        },
        # 6 (sheet row 7) — a term, blue link
        {
            "A": "1.0",
            "B": "བདེ་གཤེགས་",
            "C": "བྱང་ཆུབ་རྡོ་རྗེ།",
            "D": "བསྒྲིགས་ཟིན།",
            "E": "Link",
        },
        # 7 (sheet row 8) — a term, red link, plus a stray extra column
        {
            "A": "2.0",
            "B": "སྲས་",
            "C": "བྱང་ཆུབ་རྡོ་རྗེ།",
            "D": "བསྒྲིགས་ཟིན།",
            "E": "link",
            "G": "མཐུན།",
        },
        # 8 (sheet row 9) — a term with no link at all, and a chapter marker
        {"A": "3.0", "B": "ཆོས་ཀྱི་སྐུ་", "C": "ཚེ་ཐར་སྒྲོལ་མ།", "D": "བསྒྲིགས་ཟིན།", "F": "༧༽"},
    ]


@pytest.fixture()
def tab_links() -> dict[str, str]:
    """Hyperlink relations, keyed by *true* spreadsheet cell ref.

    Rows 1–3 line up with the export; from row 5 on they are one ahead,
    because sheet row 4 is blank and the cell-text export omitted it.
    """
    return {
        "F3": DRIVE_SCAN,
        "G3": WIKISOURCE_INDEX,
        "F5": WIKISOURCE_INDEX,
        "G5": WIKISOURCE_TEXT,
        "H5": COMMONS_FILE,
        "N5": WIKIDATA,
        "E7": WRAPPED_BDE,
        "E8": REDLINK,
    }


@pytest.fixture()
def registry(tab_rows, tab_links) -> Registry:
    return load_from_xlsx_export(
        {"སྤྱོད་འཇུག": tab_rows}, {"སྤྱོད་འཇུག": tab_links}, "སྤྱོད་འཇུག", corpus_id="spyodjug"
    )


# --------------------------------------------------------------------------
# URL handling
# --------------------------------------------------------------------------


def test_unwrap_google_redirect_undoes_the_double_encoding():
    assert unwrap_google_redirect(WRAPPED_BDE) == UNWRAPPED_BDE


def test_unwrap_google_redirect_leaves_a_plain_url_alone():
    assert unwrap_google_redirect(WIKISOURCE_TEXT) == WIKISOURCE_TEXT


def test_unwrap_google_redirect_terminates_on_a_self_referential_wrapper():
    loop = "https://www.google.com/url?q=https://www.google.com/url?q=https://x.test/"
    assert unwrap_google_redirect(loop).startswith("https://")


@pytest.mark.parametrize(
    ("url", "kind"),
    [
        (WIKISOURCE_INDEX, "wikisource_index"),
        (WIKISOURCE_TEXT, "wikisource_text"),
        ("https://wikisource.org/w/index.php?title=Page:x.pdf/1&action=edit", "wikisource_text"),
        (COMMONS_FILE, "commons"),
        # A to-do marker, not a file: must not become a citation target.
        ("https://commons.wikimedia.org/wiki/Special:UploadWizard", "other"),
        (WIKIDATA, "wikidata"),
        (UNWRAPPED_BDE, "wikipedia"),
        (REDLINK, "wikipedia_redlink"),
        (DRIVE_SCAN, "drive"),
        ("https://docs.google.com/document/d/abc/edit", "drive"),
        ("https://library.bdrc.io/show/bdr:WA0RK0529", "bdrc"),
        ("https://example.test/thing", "other"),
    ],
)
def test_classify_url(url, kind):
    assert classify_url(url) == kind


def test_classify_url_sees_through_the_google_wrapper():
    assert classify_url(WRAPPED_BDE) == "wikipedia"


def test_bdrc_show_url():
    assert bdrc_show_url("WA0RK0529") == "https://library.bdrc.io/show/bdr:WA0RK0529"


# --------------------------------------------------------------------------
# Row alignment
# --------------------------------------------------------------------------


def test_align_link_rows_recovers_the_dropped_blank_row(tab_rows, tab_links):
    # Export rows 1-3 are sheet rows 1-3; from export row 4 on, add one.
    assert align_link_rows(tab_rows, tab_links) == [1, 2, 3, 5, 6, 7, 8, 9]


def test_align_link_rows_is_the_identity_without_evidence_of_drift(tab_rows):
    assert align_link_rows(tab_rows, {}) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_align_link_rows_handles_an_empty_sheet():
    assert align_link_rows([], {"A1": WIKISOURCE_TEXT}) == []


def test_misalignment_would_attach_the_wrong_article_to_a_term(tab_rows, tab_links):
    """The failure this pass exists to prevent, made explicit.

    Joining on ``rows[n-1]`` puts row 7's link on row 6's term.  Both look
    perfectly plausible in the output, which is exactly why it needs a test.
    """
    naive = load_from_xlsx_export(
        {"t": tab_rows},
        {"t": {"E6": WRAPPED_BDE}},  # as if the sheet had no blank row
        "t",
        corpus_id="c",
    )
    aligned = load_from_xlsx_export(
        {"t": tab_rows}, {"t": tab_links}, "t", corpus_id="c"
    )
    assert find_term(naive, "བདེ་གཤེགས་").wikipedia_url == UNWRAPPED_BDE
    assert find_term(aligned, "བདེ་གཤེགས་").wikipedia_url == UNWRAPPED_BDE


# --------------------------------------------------------------------------
# Splitting the source block from the term block
# --------------------------------------------------------------------------


def test_find_split_index_puts_the_boundary_at_the_term_header(tab_rows, tab_links):
    assert find_split_index(tab_rows, tab_links) == 4


def test_registry_split(registry):
    assert registry.split_index == 4
    assert len(registry.sources) == 3
    assert len(registry.terms) == 3


def test_split_index_can_be_overridden(tab_rows, tab_links):
    forced = load_from_xlsx_export(
        {"t": tab_rows}, {"t": tab_links}, "t", corpus_id="c", split_index=2
    )
    assert forced.split_index == 2
    assert len(forced.sources) == 1
    # The rows the heuristic called sources are now read as terms instead.
    assert len(forced.terms) == 5


def test_a_junk_tab_yields_a_registry_rather_than_an_exception():
    """The real sheet has a scratch tab named ``gaga`` — a stray note and a
    list of uploads under no header.  It must parse to *something*, not raise;
    which side of the split its rows land on is not meaningful for a tab with
    no structure, so this asserts only that nothing is lost or invented."""
    junk = {
        "gaga": [
            {"C": "UPloaded"},
            {"A": "མཛོད་ཊཱིཀ་ཐར་ལམ་གསལ་བྱེད།", "B": WIKISOURCE_INDEX},
            {"A": "ཆོས་མངོན་མཛོད་ཀྱི་ཚིག་ལེའུར་བྱས་པའི་འགྲེལ་པ།", "B": WIKISOURCE_INDEX},
        ]
    }
    result = load_from_xlsx_export(junk, {"gaga": {}}, "gaga")
    assert result.corpus_name == "gaga"
    # Both real rows survive; the stray English note becomes nothing rather
    # than a phantom source with an empty title.
    titles = [s.title for s in result.sources] + [t.term for t in result.terms]
    assert titles == ["མཛོད་ཊཱིཀ་ཐར་ལམ་གསལ་བྱེད།", "ཆོས་མངོན་མཛོད་ཀྱི་ཚིག་ལེའུར་བྱས་པའི་འགྲེལ་པ།"]


def test_an_unknown_tab_raises_with_the_available_names():
    with pytest.raises(KeyError, match="other"):
        load_from_xlsx_export({"other": []}, {}, "missing")


def test_loader_accepts_paths_as_well_as_parsed_documents(tmp_path, tab_rows, tab_links):
    registry_file = tmp_path / "registry.json"
    links_file = tmp_path / "hyperlinks.json"
    registry_file.write_text(json.dumps({"t": tab_rows}), encoding="utf-8")
    links_file.write_text(json.dumps({"t": tab_links}), encoding="utf-8")
    result = load_from_xlsx_export(registry_file, links_file, "t", corpus_id="c")
    assert len(result.terms) == 3


# --------------------------------------------------------------------------
# Field extraction
# --------------------------------------------------------------------------


def test_source_reads_prose_fields_from_the_header_roles(registry):
    source = registry.sources[0]
    assert source.source_id == "spyodjug-s002"
    assert source.title == "སྤྱོད་འཇུག་གི་རྣམ་བཤད་རྒྱལ་སྲས་འཇུག་ངོགས།"
    assert source.author == "རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།"
    assert source.collection == "བོད་གཞུང་།"
    assert source.version == "ཤིང་དཔར།"


def test_source_id_records_the_true_spreadsheet_row(registry):
    """s005, not s004: the id must point at the row a human can open."""
    assert [source.source_id for source in registry.sources] == [
        "spyodjug-s002",
        "spyodjug-s003",
        "spyodjug-s005",
    ]


def test_source_urls_come_from_the_hyperlink_relation(registry):
    """Row 3's cells say only "Link"; everything real is in the relation."""
    source = registry.sources[1]
    assert source.wikisource_index_url == WIKISOURCE_INDEX
    assert source.status == "ཤོག་ངོས་འདི་ཉར་རྒྱུ་ཡིན།"


def test_source_urls_are_classified_not_taken_by_column(registry):
    source = registry.sources[2]
    assert source.wikisource_index_url == WIKISOURCE_INDEX
    assert source.wikisource_text_url == WIKISOURCE_TEXT
    assert source.commons_url == COMMONS_FILE
    assert source.wikidata_id == "Q2735624"
    assert source.bdrc_id == "WA0RK0529"
    assert source.local_path is None


def test_terms_read_term_editor_and_status(registry):
    first = registry.terms[0]
    assert first.term == "བདེ་གཤེགས་"
    assert first.editor == "བྱང་ཆུབ་རྡོ་རྗེ།"
    assert first.status == "བསྒྲིགས་ཟིན།"


def test_a_blue_link_means_the_article_exists(registry):
    assert registry.terms[0].wikipedia_url == UNWRAPPED_BDE
    assert registry.terms[0].exists_on_wiki is True


def test_a_red_link_means_the_article_does_not_exist(registry):
    """``&redlink=1`` is the sheet saying "still missing" — 26 real terms say it."""
    assert registry.terms[1].term == "སྲས་"
    assert registry.terms[1].wikipedia_url is None
    assert registry.terms[1].exists_on_wiki is False


def test_a_term_with_no_link_at_all(registry):
    assert registry.terms[2].term == "ཆོས་ཀྱི་སྐུ་"
    assert registry.terms[2].exists_on_wiki is False


def test_a_tibetan_numeral_marker_is_not_mistaken_for_a_field(registry):
    """``༧༽`` is a chapter marker; it has digits but no letters."""
    assert registry.terms[2].status == "བསྒྲིགས་ཟིན།"


def test_iter_terms_only_missing(registry):
    missing = [record.term for record in iter_terms(registry, only_missing=True)]
    assert missing == ["སྲས་", "ཆོས་ཀྱི་སྐུ་"]


# --------------------------------------------------------------------------
# Tibetan-aware lookup
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("left", "right"),
    [
        ("བྱང་ཆུབ་སེམས་", "བྱང་ཆུབ་སེམས།"),
        ("བྱང་ཆུབ་སེམས", "བྱང་ཆུབ་སེམས་"),
        ("  བྱང་ཆུབ་སེམས།  ", "བྱང་ཆུབ་སེམས"),
        ("བྱང་ཆུབ་སེམས༎", "བྱང་ཆུབ་སེམས"),
    ],
)
def test_term_key_ignores_only_the_terminal_delimiter(left, right):
    assert term_key(left) == term_key(right)


def test_term_key_keeps_interior_punctuation():
    """``fuzzy_key`` would fold these together; term identity must not."""
    assert term_key("ཆོས་སྐུ") != term_key("ཆོསསྐུ")


def test_term_key_normalises_to_nfc():
    decomposed = "གཱ"  # ག + vowel sign AA, decomposable pair
    assert term_key(decomposed) == term_key("གཱ")


def test_find_term_matches_across_the_shad_tsheg_difference(registry):
    assert find_term(registry, "བདེ་གཤེགས།").term == "བདེ་གཤེགས་"
    assert find_term(registry, "བདེ་གཤེགས").term == "བདེ་གཤེགས་"


def test_find_term_returns_none_for_an_absent_or_empty_term(registry):
    assert find_term(registry, "མེད་པ་") is None
    assert find_term(registry, "།") is None


# --------------------------------------------------------------------------
# Citation URLs
# --------------------------------------------------------------------------


def _registry_with(source: Source) -> Registry:
    return Registry(sources=[source], terms=[], corpus_name="test")


def test_resolve_citation_url_prefers_the_transcribed_text():
    registry = _registry_with(
        Source(
            source_id="s1",
            title="t",
            wikisource_index_url=WIKISOURCE_INDEX,
            wikisource_text_url=WIKISOURCE_TEXT,
            commons_url=COMMONS_FILE,
            bdrc_id="WA0RK0529",
        )
    )
    assert resolve_citation_url(registry, "s1") == WIKISOURCE_TEXT


def test_resolve_citation_url_falls_back_down_the_chain():
    index_only = _registry_with(
        Source(source_id="s1", title="t", wikisource_index_url=WIKISOURCE_INDEX)
    )
    bdrc_only = _registry_with(Source(source_id="s1", title="t", bdrc_id="WA0RK0529"))
    commons_only = _registry_with(Source(source_id="s1", title="t", commons_url=COMMONS_FILE))
    nothing = _registry_with(Source(source_id="s1", title="t"))

    assert resolve_citation_url(index_only, "s1") == WIKISOURCE_INDEX
    assert resolve_citation_url(bdrc_only, "s1") == bdrc_show_url("WA0RK0529")
    assert resolve_citation_url(commons_only, "s1") == COMMONS_FILE
    assert resolve_citation_url(nothing, "s1") is None


def test_resolve_citation_url_for_an_unknown_source():
    assert resolve_citation_url(_registry_with(Source("s1", "t")), "nope") is None


def test_resolve_citation_url_appends_a_text_fragment(monkeypatch):
    """The fragment builder is a sibling deliverable; stand one in."""
    module = types.ModuleType("kangyur_wiki.wiki.wikitext")
    module.text_fragment = lambda quote: "#:~:text=" + quote  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "kangyur_wiki.wiki.wikitext", module)

    registry = _registry_with(
        Source(source_id="s1", title="t", wikisource_text_url=WIKISOURCE_TEXT)
    )
    assert resolve_citation_url(registry, "s1", quote="བདེ") == f"{WIKISOURCE_TEXT}#:~:text=བདེ"


def test_resolve_citation_url_survives_a_missing_wikitext_module(monkeypatch):
    """``wikitext.py`` may not exist yet.  A bare URL beats an import error."""
    monkeypatch.setitem(sys.modules, "kangyur_wiki.wiki.wikitext", None)
    registry = _registry_with(
        Source(source_id="s1", title="t", wikisource_text_url=WIKISOURCE_TEXT)
    )
    assert resolve_citation_url(registry, "s1", quote="བདེ") == WIKISOURCE_TEXT


def test_resolve_citation_url_composes_with_the_real_fragment_builder():
    """Integration: the two deliverables actually fit together.

    Skipped rather than failed if ``wikitext.py`` is not in the checkout —
    ``registry.py`` is required to stand alone.
    """
    pytest.importorskip("kangyur_wiki.wiki.wikitext")
    registry = _registry_with(
        Source(source_id="s1", title="t", wikisource_text_url=WIKISOURCE_TEXT)
    )
    url = resolve_citation_url(registry, "s1", quote="བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།")
    assert url.startswith(f"{WIKISOURCE_TEXT}#:~:text=")


def test_resolve_citation_url_tolerates_a_quote_the_builder_rejects():
    """The real builder raises on a quote with no Tibetan syllables.  A link to
    the right page beats no link at all — that gap is reported as a warning by
    the verify stage, not by losing the URL here."""
    pytest.importorskip("kangyur_wiki.wiki.wikitext")
    registry = _registry_with(
        Source(source_id="s1", title="t", wikisource_text_url=WIKISOURCE_TEXT)
    )
    assert resolve_citation_url(registry, "s1", quote="   ") == WIKISOURCE_TEXT


def test_resolve_citation_url_survives_a_raising_fragment_builder(monkeypatch):
    module = types.ModuleType("kangyur_wiki.wiki.wikitext")

    def boom(quote):
        raise ValueError("quote too short")

    module.text_fragment = boom  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "kangyur_wiki.wiki.wikitext", module)

    registry = _registry_with(
        Source(source_id="s1", title="t", wikisource_text_url=WIKISOURCE_TEXT)
    )
    assert resolve_citation_url(registry, "s1", quote="བདེ") == WIKISOURCE_TEXT


# --------------------------------------------------------------------------
# YAML round trip
# --------------------------------------------------------------------------


def test_save_then_load_is_lossless(tmp_path, registry):
    sources_path, terms_path = save(registry, tmp_path / "spyodjug")
    assert sources_path.name == "sources.yaml"
    assert terms_path.name == "terms.yaml"

    restored = load(tmp_path / "spyodjug")
    assert restored.corpus_name == registry.corpus_name
    assert restored.corpus_id == registry.corpus_id
    assert restored.split_index == registry.split_index
    assert [s.to_dict() for s in restored.sources] == [s.to_dict() for s in registry.sources]
    assert [t.to_dict() for t in restored.terms] == [t.to_dict() for t in registry.terms]


def test_save_accepts_the_sources_file_path_and_finds_its_sibling(tmp_path, registry):
    sources_path, terms_path = save(registry, tmp_path / "c" / "sources.yaml")
    assert terms_path == tmp_path / "c" / "terms.yaml"
    assert load(sources_path).terms


def test_yaml_keeps_tibetan_readable(tmp_path, registry):
    sources_path, _ = save(registry, tmp_path / "c")
    assert "རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།" in sources_path.read_text(encoding="utf-8")


def test_load_tolerates_a_missing_terms_file(tmp_path, registry):
    save(registry, tmp_path / "c")
    (tmp_path / "c" / "terms.yaml").unlink()
    restored = load(tmp_path / "c")
    assert restored.sources and restored.terms == []


def test_load_raises_when_nothing_is_there(tmp_path):
    with pytest.raises(FileNotFoundError):
        load(tmp_path / "nowhere")


def test_local_path_round_trips_as_a_path(tmp_path):
    registry = Registry(
        sources=[Source(source_id="s1", title="t", local_path=tmp_path / "root.md")],
        terms=[TermRecord(term="བདེ་གཤེགས་")],
        corpus_name="c",
        corpus_id="c",
    )
    save(registry, tmp_path / "c")
    restored = load(tmp_path / "c")
    assert restored.sources[0].local_path == tmp_path / "root.md"
