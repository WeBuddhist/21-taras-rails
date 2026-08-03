"""The update path: classify-then-apply merging into an existing article.

Same safety story as the create path, extended to updates: the model classifies, code
applies, conflicts reach a human unmerged, and a new quotation that is not
character-for-character in its source fails the gate. Plus the update-specific policy:
the pre-existing state of a community-written page (foreign refs, off-allowlist
categories) is advisory, never blocking — otherwise the majority case is unusable.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from kangyur_wiki.registry import Registry, Source, TermRecord
from kangyur_wiki.stages.pipeline import (
    Passage,
    TermArtifacts,
    run_update,
    update_citation_builder,
)
from kangyur_wiki.wiki.merge import (
    MergeOperation,
    apply_operations,
    ensure_references_section,
    find_section,
    parse_operations,
    parse_sections,
    section_anchor,
    unified_diff,
    verify_merged,
)
from kangyur_wiki.wiki.wikitext import Citation, render_ref

TERM = "བྱང་ཆུབ་ཀྱི་སེམས།"

QUOTE_REAL = "བྱང་ཆུབ་ཀྱི་སེམས་ནི་གཞན་གྱི་དོན་དུ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འདོད་པའི་སེམས་སོ།།"
QUOTE_FAKE = QUOTE_REAL + "བསླད་པ།"

COMMENTARY = f"༄༅། །འདིར་བཤད་པ།\n{QUOTE_REAL}\nཞེས་གསུངས་སོ།།\n"

EXISTING_SENTENCE = "བྱང་ཆུབ་ཀྱི་སེམས་ནི་སེམས་བསྐྱེད་ཅེས་ཀྱང་བརྗོད།"

# A community-written article: a lead, two sections, a human ref that is NOT in our
# citation inventory, an off-allowlist category, and no <references /> display —
# the documented state of ~600 live bo.wikipedia pages.
EXISTING_ARTICLE = f"""'''{TERM}'''ནི་ཐེག་ཆེན་གྱི་གཞུང་ལ་གྲགས་པའི་ཐ་སྙད་ཅིག་ཡིན།

== མཚན་ཉིད། ==
{EXISTING_SENTENCE}<ref>མི་ཤེས་པའི་ཡིག་ཆ།</ref>

== དབྱེ་བ། ==
སྨོན་འཇུག་གཉིས་སུ་དབྱེ།

== འབྲེལ་ཡོད་ཤོག་ངོས། ==
* [[སྨོན་པའི་སེམས་]]

[[རིགས་དབྱེ།:ཆོས་ལུགས།]]
"""


@pytest.fixture
def registry() -> Registry:
    return Registry(
        corpus_id="test",
        corpus_name="test",
        sources=[
            Source(
                source_id="TESTCOMM",
                title="ཚིག་འགྲེལ།",
                author="མཁན་པོ།",
                wikisource_text_url="https://wikisource.org/wiki/TEST",
            )
        ],
        terms=[TermRecord(term=TERM)],
    )


@pytest.fixture
def citation() -> Citation:
    return Citation(
        source_id="TESTCOMM",
        author="མཁན་པོ།",
        title="ཚིག་འགྲེལ།",
        url="https://wikisource.org/wiki/TEST",
        quote=QUOTE_REAL,
    )


def _loader(source_id: str) -> str:
    if source_id == "TESTCOMM":
        return COMMENTARY
    raise FileNotFoundError(source_id)


# --------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------


def test_section_anchor_strips_markup_and_underscores_spaces():
    assert section_anchor("མཚན་ཉིད།") == "མཚན་ཉིད།"
    assert section_anchor("'''མཚན་ཉིད།'''") == "མཚན་ཉིད།"
    assert section_anchor("[[སྨོན་པ་|སྨོན་པ།]] དང་") == "སྨོན་པ།_དང་"


def test_parse_sections_spans_cover_their_content():
    sections = parse_sections(EXISTING_ARTICLE)
    assert [s.heading for s in sections] == ["མཚན་ཉིད།", "དབྱེ་བ།", "འབྲེལ་ཡོད་ཤོག་ངོས།"]
    body = EXISTING_ARTICLE[sections[0].body_start : sections[0].end]
    assert EXISTING_SENTENCE in body
    assert "དབྱེ་བ" not in body


def test_find_section_is_terminal_punctuation_tolerant():
    sections = parse_sections(EXISTING_ARTICLE)
    assert find_section(sections, "མཚན་ཉིད།").heading == "མཚན་ཉིད།"
    assert find_section(sections, "མཚན་ཉིད").heading == "མཚན་ཉིད།"  # shad dropped
    assert find_section(sections, "མེད་པའི་ས་བཅད།") is None


# --------------------------------------------------------------------------
# Operation parsing
# --------------------------------------------------------------------------


def test_parse_operations_drops_the_unusable_and_keeps_the_valid(registry):
    build = update_citation_builder(registry)
    data = {
        "operations": [
            {"kind": "new", "section_anchor": "མཚན་ཉིད།", "new_text": "ཚིག་གསར།",
             "citation": {"source_id": "TESTCOMM", "quote": QUOTE_REAL}},
            {"kind": "new", "section_anchor": "མཚན་ཉིད།", "new_text": "ལུང་མེད་ཚིག"},  # uncited
            {"kind": "duplicate", "section_anchor": "མཚན་ཉིད།",
             "citation": {"source_id": "TESTCOMM", "quote": QUOTE_REAL}},  # no existing_text
            {"kind": "rewrite", "section_anchor": "x"},  # unknown kind
            {"kind": "new", "section_anchor": "x", "new_text": "y",
             "citation": {"source_id": "GHOST", "quote": "z"}},  # unknown source
        ]
    }
    operations, problems = parse_operations(data, citation_builder=build)
    assert len(operations) == 1
    assert operations[0].kind == "new"
    assert operations[0].citation.url.startswith("https://wikisource.org/wiki/TEST")
    assert len(problems) == 4


# --------------------------------------------------------------------------
# Applying
# --------------------------------------------------------------------------


def test_duplicate_attaches_ref_after_the_sentence_and_its_existing_refs(citation):
    op = MergeOperation(
        kind="duplicate", section_anchor="མཚན་ཉིད།",
        existing_text=EXISTING_SENTENCE, citation=citation,
    )
    result = apply_operations(EXISTING_ARTICLE, [op])
    assert result.applied == [op]
    # New ref lands after the human ref, not between the sentence and it.
    expected = EXISTING_SENTENCE + "<ref>མི་ཤེས་པའི་ཡིག་ཆ།</ref>" + render_ref(citation)
    assert expected in result.merged
    # Nothing existing was altered.
    assert EXISTING_SENTENCE in result.merged
    assert "མི་ཤེས་པའི་ཡིག་ཆ།" in result.merged


def test_duplicate_with_unfindable_text_is_skipped_not_repaired(citation):
    op = MergeOperation(
        kind="duplicate", section_anchor="མཚན་ཉིད།",
        existing_text="འདི་ནི་ཤོག་ངོས་སུ་མེད་པའི་ཚིག་ཡིན།", citation=citation,
    )
    result = apply_operations(EXISTING_ARTICLE, [op])
    assert result.applied == []
    assert len(result.skipped) == 1
    assert "not found verbatim" in result.skipped[0][1]


def test_duplicate_already_cited_is_skipped(citation):
    once = apply_operations(
        EXISTING_ARTICLE,
        [MergeOperation(kind="duplicate", section_anchor="མཚན་ཉིད།",
                        existing_text=EXISTING_SENTENCE, citation=citation)],
    )
    again = apply_operations(
        once.merged,
        [MergeOperation(kind="duplicate", section_anchor="མཚན་ཉིད།",
                        existing_text=EXISTING_SENTENCE, citation=citation)],
    )
    assert again.applied == []
    assert "already attached" in again.skipped[0][1]


def test_new_paragraph_lands_at_the_end_of_its_section(citation):
    op = MergeOperation(
        kind="new", section_anchor="དབྱེ་བ།",
        new_text="གཞུང་གཞན་ལས་དབྱེ་ཚུལ་གསུམ་དུ་གསུངས།", citation=citation,
    )
    result = apply_operations(EXISTING_ARTICLE, [op])
    merged = result.merged
    assert result.applied == [op]
    inserted_at = merged.find("གཞུང་གཞན་ལས་དབྱེ་ཚུལ་")
    assert merged.find("སྨོན་འཇུག་གཉིས་སུ་དབྱེ།") < inserted_at < merged.find("== འབྲེལ་ཡོད་ཤོག་ངོས། ==")
    assert render_ref(citation) in merged


def test_new_refuses_invented_and_terminal_sections(citation):
    invented = MergeOperation(kind="new", section_anchor="གསར་བཟོའི་ས་བཅད།",
                              new_text="ཚིག", citation=citation)
    terminal = MergeOperation(kind="new", section_anchor="འབྲེལ་ཡོད་ཤོག་ངོས།",
                              new_text="ཚིག", citation=citation)
    result = apply_operations(EXISTING_ARTICLE, [invented, terminal])
    assert result.applied == []
    assert "never invent a section" in result.skipped[0][1]
    assert "fixed tail section" in result.skipped[1][1]


def test_conflict_changes_nothing_and_is_flagged(citation):
    op = MergeOperation(
        kind="conflict", section_anchor="དབྱེ་བ།",
        existing_text="སྨོན་འཇུག་གཉིས་སུ་དབྱེ།", new_text="དབྱེ་བ་གསུམ་དུ་གསུངས།",
        citation=citation, rationale="གྲངས་མི་མཐུན།",
    )
    result = apply_operations(EXISTING_ARTICLE, [op])
    assert result.conflicts == [op]
    assert result.applied == []
    # The only change apply may make on a conflict-only run is the <references /> repair.
    without_repair = result.merged.replace("== ལུང་ཁུངས། ==\n<references />\n", "")
    assert without_repair.replace("\n", "") == EXISTING_ARTICLE.replace("\n", "")
    report = result.format_report(EXISTING_ARTICLE)
    assert "⚑" in report and "གྲངས་མི་མཐུན།" in report


def test_orphaned_footnotes_get_a_references_section():
    repairs: list[str] = []
    fixed = ensure_references_section(EXISTING_ARTICLE, repairs)
    assert "<references />" in fixed
    assert "== ལུང་ཁུངས། ==" in fixed
    assert fixed.find("<references />") < fixed.find("[[རིགས་དབྱེ།:")
    assert repairs
    # Idempotent, and a no-op for a page with no refs at all.
    assert ensure_references_section(fixed) == fixed
    assert ensure_references_section("ཚིག་ཙམ།") == "ཚིག་ཙམ།"


def test_unified_diff_shows_only_the_insertion(citation):
    op = MergeOperation(kind="duplicate", section_anchor="མཚན་ཉིད།",
                        existing_text=EXISTING_SENTENCE, citation=citation)
    result = apply_operations(EXISTING_ARTICLE, [op])
    diff = unified_diff(EXISTING_ARTICLE, result.merged)
    assert "+" in diff
    removals = [l for l in diff.splitlines()
                if l.startswith("-") and not l.startswith("---")]
    # The sentence line is replaced by itself-plus-ref; nothing disappears outright.
    assert all(EXISTING_SENTENCE in l or l.strip() == "-" for l in removals)


# --------------------------------------------------------------------------
# The merge gate
# --------------------------------------------------------------------------


def test_gate_blocks_a_fabricated_new_quotation(registry):
    fake = Citation(source_id="TESTCOMM", author="མཁན་པོ།", title="ཚིག་འགྲེལ།",
                    quote=QUOTE_FAKE)
    op = MergeOperation(kind="duplicate", section_anchor="མཚན་ཉིད།",
                        existing_text=EXISTING_SENTENCE, citation=fake)
    result = apply_operations(EXISTING_ARTICLE, [op])
    verification = verify_merged(result.merged, result.new_citations, ["ནང་བསྟན།"], _loader)
    assert not verification.passed
    assert verification.quote_failures


def test_gate_does_not_block_on_the_preexisting_page_state(citation):
    op = MergeOperation(kind="duplicate", section_anchor="མཚན་ཉིད།",
                        existing_text=EXISTING_SENTENCE, citation=citation)
    result = apply_operations(EXISTING_ARTICLE, [op])
    verification = verify_merged(result.merged, result.new_citations, ["ནང་བསྟན།"], _loader)
    # The page has a foreign ref (V2) and an off-allowlist category (V7): advisory only.
    assert verification.passed, verification.format_report()
    advisory_rules = {f.rule for f in verification.advisory}
    assert "V2" in advisory_rules and "V7" in advisory_rules
    assert "Advisory" in verification.format_report()


# --------------------------------------------------------------------------
# run_update — the full stage with a stubbed model
# --------------------------------------------------------------------------


class StubResult:
    def __init__(self, parsed):
        self.parsed = parsed
        self.text = json.dumps(parsed, ensure_ascii=False)


class StubUpdateModel:
    def __init__(self, *, corrupt: bool = False):
        self.corrupt = corrupt
        self.calls: list[str] = []

    def generate(self, prompt: str, *, schema=None, **kwargs):
        assert "operations" in (schema or {}).get("properties", {})
        self.calls.append("update")
        quote = QUOTE_FAKE if self.corrupt else QUOTE_REAL
        return StubResult(
            {
                "term": TERM,
                "operations": [
                    {"kind": "duplicate", "section_anchor": "མཚན་ཉིད།",
                     "existing_text": EXISTING_SENTENCE,
                     "citation": {"source_id": "TESTCOMM", "quote": quote},
                     "rationale": "དོན་གཅིག"},
                    {"kind": "new", "section_anchor": "དབྱེ་བ།",
                     "new_text": "མཁན་པོའི་ཚིག་འགྲེལ་ལས་ཀྱང་དབྱེ་ཚུལ་གསུངས།",
                     "citation": {"source_id": "TESTCOMM", "quote": quote},
                     "rationale": "གནས་ཚུལ་གསར་པ།"},
                    {"kind": "conflict", "section_anchor": "དབྱེ་བ།",
                     "existing_text": "སྨོན་འཇུག་གཉིས་སུ་དབྱེ།",
                     "new_text": "དབྱེ་བ་གསུམ།",
                     "rationale": "གྲངས་མི་མཐུན།"},
                ],
                "conflicts_for_human": ["གྲངས་མི་མཐུན།"],
            }
        )


def _prompt_render(stage: str, **kwargs) -> str:
    assert stage == "07-update"
    assert "existing_wikitext" in kwargs and "new_passages_json" in kwargs
    return f"[{stage}]"


def test_run_update_merges_verifies_and_writes_the_audit_trail(tmp_path: Path, registry):
    art = TermArtifacts(tmp_path / "articles" / "test")
    model = StubUpdateModel()
    passages = [Passage(source_id="TESTCOMM", quote=QUOTE_REAL, kind="མཚན་ཉིད།")]

    merge_result, verification = run_update(
        TERM, EXISTING_ARTICLE, passages, registry,
        model.generate, _prompt_render, art, source_loader=_loader,
    )

    assert model.calls == ["update"]
    assert len(merge_result.applied) == 2
    assert len(merge_result.conflicts) == 1
    assert verification.passed, verification.format_report()

    merged = art.wikitext.read_text("utf-8")
    assert "མཁན་པོའི་ཚིག་འགྲེལ་ལས་ཀྱང་" in merged
    assert "wikisource.org/wiki/TEST" in merged
    assert "<references />" in merged  # the orphaned-footnote repair
    assert "{{Reflist}}" not in merged

    for path in (art.existing_wiki, art.update_ops, art.wikitext,
                 art.citations, art.update_report, art.report):
        assert path.exists(), path
    assert art.existing_wiki.read_text("utf-8") == EXISTING_ARTICLE
    report = art.update_report.read_text("utf-8")
    assert "⚑" in report and "```diff" in report


def test_run_update_gate_rejects_a_fabricated_quotation(tmp_path: Path, registry):
    art = TermArtifacts(tmp_path / "articles" / "test")
    model = StubUpdateModel(corrupt=True)
    passages = [Passage(source_id="TESTCOMM", quote=QUOTE_REAL, kind="མཚན་ཉིད།")]

    merge_result, verification = run_update(
        TERM, EXISTING_ARTICLE, passages, registry,
        model.generate, _prompt_render, art, source_loader=_loader,
    )

    assert not verification.passed
    assert verification.quote_failures
    # The merged text is still written, so the failure is diagnosable.
    assert art.wikitext.exists() and art.report.exists()
    assert "FAIL" in verification.format_report()
