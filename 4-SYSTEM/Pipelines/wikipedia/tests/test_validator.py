"""Golden-fixture tests for the blocking wikitext gate.

The method is one known-good article, asserted clean, then one mutation per
rule asserted to fire *that rule and no other*.  Mutating one rule at a time is
what makes the suite a regression net rather than a smoke test: a change that
makes V9 swallow a V12 failure shows up as a test that now reports two rules
where it reported one.

Several mutations cannot be produced by the emitter at all (it drops uncited
sections, and it never writes ``{{Reflist}}``).  They are applied to the
rendered text directly, because the gate also runs over merged and
hand-corrected articles on the update path, where those states are reachable.

Offline: no network, no API key, no source files on disk.  The quote checker is
stubbed through ``sys.modules`` so V1's delegation is tested in both directions
without depending on another module's build order.
"""

from __future__ import annotations

import sys
import types
from dataclasses import dataclass, replace

import pytest

from kangyur_wiki.wiki.validator import (
    Finding,
    SEED_CATEGORIES,
    format_report,
    has_errors,
    validate,
)
from kangyur_wiki.wiki.wikitext import (
    HEADING_BIBLIOGRAPHY,
    HEADING_REFERENCES,
    HEADING_SEE_ALSO,
    REFERENCES_TAG,
    Article,
    Citation,
    Section,
    format_bibliography_entry,
    render_article,
    render_ref,
    render_ref_reuse,
)

# --------------------------------------------------------------------------
# Fixture
# --------------------------------------------------------------------------

BCA_QUOTE = "བྱང་ཆུབ་ཀྱི་སེམས་ནི་སྨོན་པ་དང་འཇུག་པ་གཉིས་སུ་ཤེས་པར་བྱ།"
KP_QUOTE = "སྨོན་པ་ནི་འགྲོ་བར་འདོད་པ་ལྟ་བུ་སྟེ།"

BCA = Citation(
    source_id="bca",
    author="ཞི་བ་ལྷ",
    title="སྤྱོད་འཇུག",
    year="༡༩༩༠",
    page="༡༢",
    url="https://wikisource.org/wiki/BCA",
    quote=BCA_QUOTE,
)
KUNPAL = Citation(
    source_id="kunpal",
    author="མཁན་པོ་ཀུན་དཔལ",
    title="ཚིག་འགྲེལ",
    year="༢༠༠༧",
    page="༥༥",
    url="https://wikisource.org/wiki/KP",
    quote=KP_QUOTE,
)

SOURCES = {
    "bca": "སྔོན་གྱི་གཞུང་།" + BCA_QUOTE + "ཞེས་གསུངས་སོ།",
    "kunpal": "འགྲེལ་པ་ལས།" + KP_QUOTE + "ཞེས་བཤད།",
}


def source_loader(source_id: str) -> str | None:
    return SOURCES.get(source_id)


def build_wikitext(bca: Citation = BCA, kunpal: Citation = KUNPAL) -> str:
    """The known-good article, rendered by the emitter under test."""
    return render_article(
        Article(
            term="བྱང་ཆུབ་སེམས",
            lead=["ནི་ཐེག་པ་ཆེན་པོའི་གནད་ཀྱི་ཐ་སྙད་ཅིག་ཡིན།" + render_ref(bca)],
            sections=[
                Section(
                    heading="ངེས་ཚིག",
                    paragraphs=[
                        "ངེས་ཚིག་གི་སྒོ་ནས་བཤད་ན།" + render_ref(kunpal, name="kp")
                    ],
                ),
                Section(
                    heading="དབྱེ་བ།",
                    paragraphs=["དབྱེ་ན་གཉིས་ཡོད་དེ།" + render_ref_reuse("kp")],
                ),
            ],
            see_also=["སེམས་བསྐྱེད་"],
            citations=[bca, kunpal],
            bibliography=[format_bibliography_entry(bca)],
            categories=["ནང་བསྟན།"],
        )
    )


GOLDEN = build_wikitext()
CITATIONS = (BCA, KUNPAL)


def run(text: str, *, citations=CITATIONS, allowed=SEED_CATEGORIES, loader=None):
    return validate(
        text,
        citations=citations,
        allowed_categories=allowed,
        source_loader=loader,
    )


def rules(findings, severity: str = "error") -> list[str]:
    """The distinct rule ids that fired at ``severity``, sorted."""
    return sorted({f.rule for f in findings if f.severity == severity})


def first(findings, rule: str):
    """The first finding for ``rule`` — never findings[0], which is whichever
    rule happens to run first."""
    return next(f for f in findings if f.rule == rule)


# --------------------------------------------------------------------------
# The known-good article
# --------------------------------------------------------------------------


def test_golden_article_raises_no_errors():
    assert rules(run(GOLDEN)) == []
    assert not has_errors(run(GOLDEN))


def test_golden_article_warns_about_the_unchecked_quotations():
    """Without a source_loader, V1 downgrades — it never silently passes."""
    v1 = [f for f in run(GOLDEN) if f.rule == "V1"]
    assert [f.severity for f in v1] == ["warning"]
    assert "not checked" in v1[0].message


# --------------------------------------------------------------------------
# V1 — quotations verbatim
# --------------------------------------------------------------------------


@dataclass
class _StubCheck:
    found: bool
    method: str


@pytest.fixture
def stub_verify(monkeypatch):
    """Install a fake ``kangyur_wiki.tibetan.verify`` with the agreed interface."""

    def install(found: bool, method: str = "exact"):
        module = types.ModuleType("kangyur_wiki.tibetan.verify")
        module.check_quote = lambda quote, source_text: _StubCheck(found, method)
        monkeypatch.setitem(sys.modules, "kangyur_wiki.tibetan.verify", module)

    return install


def test_v1_passes_when_every_quote_is_found(stub_verify):
    stub_verify(True)
    assert rules(run(GOLDEN, loader=source_loader)) == []


def test_v1_fires_when_a_quote_is_not_verbatim(stub_verify):
    stub_verify(False, method="missing")
    findings = run(GOLDEN, loader=source_loader)
    assert rules(findings) == ["V1"]
    assert "method=missing" in first(findings, "V1").message


def test_v1_reports_an_undeclared_source_without_blaming_the_quote(stub_verify):
    stub_verify(True)
    findings = run(GOLDEN, loader=lambda source_id: None)
    # Both V1 (cannot verify) and V2 (not declared) are true statements here.
    assert rules(findings) == ["V1", "V2"]


def test_v1_degrades_to_a_warning_when_the_checker_is_missing(monkeypatch):
    """A None entry in sys.modules is exactly what a not-yet-built module
    looks like to the import system."""
    monkeypatch.setitem(sys.modules, "kangyur_wiki.tibetan.verify", None)
    findings = run(GOLDEN, loader=source_loader)
    assert rules(findings) == []
    assert [f.rule for f in findings if f.severity == "warning"].count("V1") == 1


def test_v1_survives_a_source_loader_that_explodes(stub_verify):
    stub_verify(True)

    def angry_loader(source_id: str) -> str:
        raise OSError("disk on fire")

    findings = run(GOLDEN, loader=angry_loader)
    assert rules(findings) == ["V1", "V2"]
    assert "disk on fire" in " ".join(f.message for f in findings)


def test_v1_uses_the_real_checker_when_it_is_available():
    """Integration with kangyur_wiki.tibetan.verify, skipped if unbuilt."""
    pytest.importorskip("kangyur_wiki.tibetan.verify")
    assert rules(run(GOLDEN, loader=source_loader)) == []


# --------------------------------------------------------------------------
# V2 — every ref resolves to a declared source
# --------------------------------------------------------------------------


def test_v2_fires_on_a_ref_that_matches_no_declared_citation():
    mutated = GOLDEN.replace("ཞི་བ་ལྷ།", "སློབ་དཔོན་མིང་མེད།")
    findings = run(mutated)
    assert rules(findings) == ["V2"]
    assert "does not match any declared citation" in first(findings, "V2").message


def test_v2_fires_when_the_source_id_is_not_declared():
    findings = run(GOLDEN, loader=lambda source_id: None)
    assert "V2" in rules(findings)


# --------------------------------------------------------------------------
# V3 / V4 — the reference display
# --------------------------------------------------------------------------


def test_v3_fires_when_refs_have_nowhere_to_render():
    mutated = GOLDEN.replace("\n" + REFERENCES_TAG, "")
    assert rules(run(mutated)) == ["V3"]


def test_v3_fires_on_an_empty_reference_section():
    lonely = "\n\n".join(
        [
            "'''སེམས་'''ནི་ཡིན།",
            f"== {HEADING_REFERENCES} ==",
            REFERENCES_TAG,
            "[[རིགས་དབྱེ།:ནང་བསྟན།]]",
        ]
    )
    assert rules(run(lonely, citations=())) == ["V3"]


def test_v3_rejects_the_singular_reference_typo():
    mutated = GOLDEN.replace(REFERENCES_TAG, "<reference />")
    assert rules(run(mutated)) == ["V3"]


def test_v4_fires_on_reflist_under_a_heading():
    """The single most likely failure mode: correct on enwiki, broken here."""
    mutated = GOLDEN.replace(REFERENCES_TAG, "{{Reflist}}")
    assert rules(run(mutated)) == ["V4"]


def test_v4_ignores_case_and_spacing():
    for variant in ("{{reflist}}", "{{ Reflist }}", "{{REFLIST|2}}"):
        mutated = GOLDEN.replace(REFERENCES_TAG, variant)
        assert rules(run(mutated)) == ["V4"], variant


def test_reflist_fires_v4_where_references_tag_does_not():
    """The explicit contrast the spec calls out."""
    body = "'''སེམས་'''ནི་ཡིན།<ref>[https://wikisource.org/wiki/BCA ཞི་བ་ལྷ།]</ref>"
    category = "[[རིགས་དབྱེ།:ནང་བསྟན།]]"
    citation = Citation(source_id="bca", author="ཞི་བ་ལྷ", url="https://wikisource.org/wiki/BCA")

    broken = f"{body}\n\n== {HEADING_REFERENCES} ==\n{{{{Reflist}}}}\n\n{category}"
    fixed = f"{body}\n\n== {HEADING_REFERENCES} ==\n{REFERENCES_TAG}\n\n{category}"

    assert "V4" in rules(run(broken, citations=(citation,)))
    assert "V4" not in rules(run(fixed, citations=(citation,)))
    assert rules(run(fixed, citations=(citation,))) == []


# --------------------------------------------------------------------------
# V5 — ref structure
# --------------------------------------------------------------------------


def test_v5_fires_on_a_named_ref_that_is_never_defined():
    mutated = GOLDEN.replace('<ref name="kp" />', '<ref name="ghost" />')
    findings = run(mutated)
    assert rules(findings) == ["V5"]
    assert "never defined" in first(findings, "V5").message


def test_v5_fires_on_a_stray_closing_tag():
    mutated = GOLDEN.replace(REFERENCES_TAG, "</ref>\n" + REFERENCES_TAG)
    assert rules(run(mutated)) == ["V5"]


def test_v5_fires_on_a_ref_that_is_never_closed():
    mutated = GOLDEN.replace("ཤོག་གྲངས་༡༢]</ref>", "ཤོག་གྲངས་༡༢]")
    assert "V5" in rules(run(mutated))


def test_v5_fires_when_a_named_ref_is_defined_twice():
    mutated = GOLDEN.replace(
        '<ref name="kp" />', render_ref(KUNPAL, name="kp")
    )
    findings = run(mutated)
    assert rules(findings) == ["V5"]
    assert "defined 2 times" in first(findings, "V5").message


# --------------------------------------------------------------------------
# V6 / V7 — headings and categories
# --------------------------------------------------------------------------


def test_v6_fires_on_an_article_with_no_headings():
    """A raw model dump: prose, one category, no structure at all."""
    dump = "བྱང་ཆུབ་སེམས་ནི་ཐེག་པ་ཆེན་པོའི་གནད་ཡིན།\n\n[[རིགས་དབྱེ།:ནང་བསྟན།]]"
    assert rules(run(dump, citations=())) == ["V6"]


def test_v7_fires_on_a_category_outside_the_allowlist():
    mutated = GOLDEN.replace("ནང་བསྟན།]]", "ནང་པ་སངས་རྒྱས།།]]")
    findings = run(mutated)
    assert rules(findings) == ["V7"]
    assert "allowlist" in first(findings, "V7").message


def test_v7_fires_when_there_is_no_category_at_all():
    mutated = GOLDEN.replace("\n\n[[རིགས་དབྱེ།:ནང་བསྟན།]]", "")
    assert rules(run(mutated)) == ["V7"]


def test_v7_accepts_the_english_namespace_alias():
    """The team's published articles use [[Category:…]]; recognising it stops
    the gate from reporting a categorised article as uncategorised."""
    mutated = GOLDEN.replace("[[རིགས་དབྱེ།:ནང་བསྟན།]]", "[[Category:ནང་བསྟན།]]")
    assert rules(run(mutated)) == []


# --------------------------------------------------------------------------
# V8 — no unsourced sections
# --------------------------------------------------------------------------


def test_v8_fires_on_a_section_with_no_citation():
    mutated = GOLDEN.replace(
        f"== {HEADING_SEE_ALSO} ==",
        f"== མཚན་ཉིད། ==\nལུང་ཁུངས་མེད་པའི་ས་བཅད།\n\n== {HEADING_SEE_ALSO} ==",
    )
    findings = run(mutated)
    assert rules(findings) == ["V8"]
    assert "མཚན་ཉིད།" in first(findings, "V8").message


def test_v8_exempts_the_three_tail_sections():
    """They carry links, footnotes and a bibliography, never inline refs."""
    assert not [f for f in run(GOLDEN) if f.rule == "V8"]


def test_v8_lets_a_subsection_carry_the_parents_citation():
    mutated = GOLDEN.replace(
        "== དབྱེ་བ། ==\nདབྱེ་ན་གཉིས་ཡོད་དེ།",
        "== དབྱེ་བ། ==\n=== དང་པོ། ===\nདབྱེ་ན་གཉིས་ཡོད་དེ།",
    )
    assert rules(run(mutated)) == []


# --------------------------------------------------------------------------
# V9 — Tibetan script only
# --------------------------------------------------------------------------


def test_v9_fires_on_latin_text_in_the_body():
    mutated = GOLDEN.replace("ནི་ཐེག་པ་", "ནི་bodhicitta་ཐེག་པ་")
    findings = run(mutated)
    assert rules(findings) == ["V9"]
    assert "'bodhicitta'" in first(findings, "V9").message


def test_v9_fires_on_ascii_digits_in_the_body():
    mutated = GOLDEN.replace("དབྱེ་ན་གཉིས་", "དབྱེ་ན་2་")
    assert rules(run(mutated)) == ["V9"]


def test_v9_ignores_urls_inside_refs_and_template_parameters():
    """The golden article is full of Latin — all of it inside <ref> and
    <references />, which is exactly where the spec allows it."""
    assert not [f for f in run(GOLDEN) if f.rule == "V9"]


def test_v9_accepts_tibetan_numerals():
    assert not [
        f for f in run(GOLDEN.replace("གཉིས་ཡོད་", "༢་ཡོད་")) if f.rule == "V9"
    ]


# --------------------------------------------------------------------------
# V10 — the tsheg boundary
# --------------------------------------------------------------------------


def test_v10_fires_when_the_tsheg_is_lost_at_a_bold_boundary():
    mutated = GOLDEN.replace("'''བྱང་ཆུབ་སེམས་'''ནི་", "'''བྱང་ཆུབ་སེམས'''ནི་")
    findings = run(mutated)
    assert rules(findings) == ["V10"]
    assert "U+0F0B" in first(findings, "V10").message


def test_v10_accepts_the_tsheg_on_either_side():
    inside = GOLDEN
    outside = GOLDEN.replace("'''བྱང་ཆུབ་སེམས་'''ནི་", "'''བྱང་ཆུབ་སེམས'''་ནི་")
    assert not [f for f in run(inside) if f.rule == "V10"]
    assert not [f for f in run(outside) if f.rule == "V10"]


def test_v10_fires_at_a_wikilink_boundary():
    mutated = GOLDEN.replace(
        "* [[སེམས་བསྐྱེད་]]", "* [[སེམས་བསྐྱེད]]ནི་གནད་ཡིན།"
    )
    findings = run(mutated)
    assert rules(findings) == ["V10"]
    assert "[[…]]" in first(findings, "V10").message


def test_v10_ignores_a_boundary_followed_by_punctuation_or_end_of_line():
    mutated = GOLDEN.replace("* [[སེམས་བསྐྱེད་]]", "* [[སེམས་བསྐྱེད]]།")
    assert not [f for f in run(mutated) if f.rule == "V10"]


# --------------------------------------------------------------------------
# V11 — the fixed tail
# --------------------------------------------------------------------------


def test_v11_fires_when_the_tail_sections_are_out_of_order():
    blocks = GOLDEN.split("\n\n")
    references = next(
        i for i, b in enumerate(blocks) if b.startswith(f"== {HEADING_REFERENCES} ==")
    )
    bibliography = next(
        i for i, b in enumerate(blocks) if b.startswith(f"== {HEADING_BIBLIOGRAPHY} ==")
    )
    blocks[references], blocks[bibliography] = (
        blocks[bibliography],
        blocks[references],
    )
    findings = run("\n\n".join(blocks))
    assert rules(findings) == ["V11"]
    assert "out of order" in first(findings, "V11").message


def test_v11_fires_when_a_body_section_comes_after_the_tail():
    mutated = GOLDEN.replace(
        "\n\n[[རིགས་དབྱེ།:ནང་བསྟན།]]",
        "\n\n== བསྡུས་དོན། ==\nམཇུག་བསྡུ།<ref name=\"kp\" />\n\n[[རིགས་དབྱེ།:ནང་བསྟན།]]",
    )
    findings = run(mutated)
    assert rules(findings) == ["V11"]


def test_v11_fires_when_the_reference_heading_is_missing():
    mutated = GOLDEN.replace(f"== {HEADING_REFERENCES} ==\n", "")
    assert "V11" in rules(run(mutated))


# --------------------------------------------------------------------------
# V12 — placeholders and chatter
# --------------------------------------------------------------------------


def test_v12_fires_on_a_dummy_source_url():
    """Topic 324's prompt emits https://dummy.com by design; shipping one is
    the resolver failing silently."""
    dummy = replace(BCA, url="https://dummy.com")
    mutated = build_wikitext(bca=dummy)
    findings = run(mutated, citations=(dummy, KUNPAL))
    assert rules(findings) == ["V12"]
    assert "dummy" in first(findings, "V12").message


def test_v12_fires_on_leftover_assistant_chatter():
    mutated = "Here is the article you asked for:\n\n" + GOLDEN
    assert "V12" in rules(run(mutated))


def test_v12_fires_on_an_unfilled_placeholder_slot():
    mutated = GOLDEN.replace("ཤོག་གྲངས་༡༢", "ཤོག་གྲངས་<PAGE>")
    assert "V12" in rules(run(mutated))


def test_v12_fires_on_a_markdown_code_fence():
    assert "V12" in rules(run("```\n" + GOLDEN + "\n```"))


# --------------------------------------------------------------------------
# Warnings
# --------------------------------------------------------------------------


def test_warnings_flag_incomplete_and_unlinked_refs():
    thin = Citation(source_id="oral", author="མཁས་དབང་", title="ཞལ་ལུང")
    findings = run(GOLDEN, citations=(thin,))
    warned = rules(findings, severity="warning")
    assert "W1" in warned  # missing year and page
    assert "W2" in warned  # no URL


def test_warning_flags_a_single_citation_section():
    assert "W3" in rules(run(GOLDEN), severity="warning")


def test_warning_flags_a_stub_length_article():
    assert "W4" in rules(run(GOLDEN), severity="warning")


def test_warnings_never_block():
    findings = run(GOLDEN)
    assert not has_errors(findings)
    assert rules(findings, severity="warning")


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


def test_format_report_groups_by_severity_and_states_the_verdict():
    report = format_report(run(GOLDEN.replace(REFERENCES_TAG, "{{Reflist}}")))
    assert "ERRORS (" in report
    assert "WARNINGS (" in report
    assert report.index("ERRORS (") < report.index("WARNINGS (")
    assert report.strip().endswith("Not cleared for publication.")
    assert "V4" in report


def test_format_report_passes_a_clean_article():
    report = format_report(run(GOLDEN))
    assert report.startswith("WARNINGS (")
    assert "PASS — 0 errors" in report


def test_format_report_handles_no_findings_at_all():
    assert format_report([]) == "PASS — 0 errors, 0 warning(s)."


def test_format_report_shows_line_numbers():
    finding = Finding("V4", "error", "boom", 7)
    assert "line 7:" in format_report([finding])


def test_format_report_groups_findings_under_their_rule():
    report = format_report(
        [Finding("V4", "error", "first", 1), Finding("V4", "error", "second", 2)]
    )
    lines = report.splitlines()
    assert lines[0] == "ERRORS (2)"
    assert lines[1].startswith("  V4 — ")
    assert lines[2] == "    line 1: first"
    assert lines[3] == "    line 2: second"
