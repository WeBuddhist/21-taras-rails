"""``emit_local_wiki`` — rendering a verified article's grounding into 2-RAILS/Local-Wiki/.

Builds a minimal fixture corpus (the four JSON artifacts one verified term actually has,
plus a registry with `registered_id`/`local_path` set) and checks the renderer against
it, the same style `test_gemini_polish_script.py` and `test_pipeline_e2e.py` use rather
than depending on a real corpus on disk.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from kangyur_wiki.registry import Registry, Source
from kangyur_wiki.stages.localwiki import emit_local_wiki
from kangyur_wiki.stages.pipeline import TermArtifacts

TERM = "སྒྲོལ་མ"
QUOTE_A = "སྒྲོལ་མ་ནི་སྡུག་བསྔལ་ལས་སྒྲོལ་བའོ།།"
QUOTE_B = "གཞན་ཡང་སྙིང་རྗེ་ཆེན་པོའི་རྣམ་པར་གྱུར་པའོ།།"
LEAD_TEXT = "སྒྲོལ་མ་ཞེས་པའི་མིང་གི་ངེས་ཚིག་ལ་མཁས་པ་མི་འདྲ་བ་གསུམ་གྱིས་མཐུན་པར་བཤད་དོ།"


def _write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


@pytest.fixture
def artifacts(tmp_path: Path) -> TermArtifacts:
    art = TermArtifacts(tmp_path / "articles" / TERM)
    art.ensure()
    _write_json(
        art.extract,
        {
            "term": TERM,
            "passages": [
                {"source_id": "S1", "quote": QUOTE_A, "segment_id": "I-1"},
                {"source_id": "S2", "quote": QUOTE_B, "segment_id": "I-2"},
            ],
        },
    )
    _write_json(
        art.claims,
        {
            "term": TERM,
            "claims": [
                {"id": "C1", "claim_bo": "དོན་དང་པོ།", "passage_indices": [0], "claim_type": "consensus", "contested": False},
                {"id": "C2", "claim_bo": "དོན་འགལ་བ།", "passage_indices": [1], "claim_type": "school-position",
                 "school": "དགེ་ལུགས།", "reception": "contested by X", "contested": True},
            ],
        },
    )
    _write_json(
        art.citations,
        [
            {"source_id": "S1", "author": "A1", "title": "T1", "quote": QUOTE_A, "segment_id": "I-1"},
            {"source_id": "S2", "author": "A2", "title": "T2", "quote": QUOTE_B, "segment_id": "I-2"},
            {"source_id": "S1", "author": "A1", "title": "T1", "quote": QUOTE_A, "segment_id": "I-1"},
        ],
    )
    _write_json(
        art.draft,
        {"lead": [{"text": LEAD_TEXT, "citations": [0]}], "sections": [], "see_also": []},
    )
    _write_json(art.model, {"model": "test-model-x", "run_at": "2026-01-01T00:00:00+00:00"})
    return art


@pytest.fixture
def registry() -> Registry:
    return Registry(
        sources=[
            Source(source_id="S1", title="Commentary One", registered_id="commentary-one",
                   local_path="1-SOURCES/Commentaries/commentary-one.md"),
            Source(source_id="S2", title="Commentary Two", registered_id="commentary-two",
                   local_path="1-SOURCES/Commentaries/commentary-two.md"),
            Source(source_id="S3", title="No registered_id", local_path="1-SOURCES/Commentaries/orphan.md"),
        ]
    )


def test_frontmatter_and_body_shape(tmp_path, artifacts, registry):
    result = emit_local_wiki(TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki")

    assert result.path == tmp_path / "Local-Wiki" / f"{TERM}.md"
    assert result.commentaries_cited == 2
    assert result.attestations == 3  # S1 cited twice, S2 once
    assert result.divergences == 1

    text = result.path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    assert "term: " + TERM in text
    assert "language: bo" in text
    assert "text: smoke" in text
    assert "commentary-one" in text and "commentary-two" in text
    assert "attested_blocks:" in text
    assert "commentary-one:^I-1" in text
    assert "commentary-two:^I-2" in text
    assert "status: draft" in text
    assert "## " + TERM in text
    assert "### Contextual definition" in text
    assert LEAD_TEXT in text
    assert "### Attestations" in text
    assert "#### commentary-one" in text
    assert "#### commentary-two" in text
    assert f"> {QUOTE_A}" in text
    assert f"> {QUOTE_B}" in text
    assert "(1-SOURCES/Commentaries/commentary-one.md#^I-1)" in text


def test_provenance_falls_back_to_model_json(tmp_path, artifacts, registry):
    result = emit_local_wiki(TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki")
    text = result.path.read_text(encoding="utf-8")
    assert "model: test-model-x" in text
    assert "run_at: '2026-01-01T00:00:00+00:00'" in text


def test_explicit_provenance_overrides_model_json(tmp_path, artifacts, registry):
    result = emit_local_wiki(
        TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki",
        model="override-model", run_at="2099-01-01T00:00:00+00:00",
    )
    text = result.path.read_text(encoding="utf-8")
    assert "model: override-model" in text


def test_citation_with_no_registered_id_is_dropped_with_a_warning(tmp_path, artifacts, registry):
    art = artifacts
    data = json.loads(art.citations.read_text(encoding="utf-8"))
    data.append({"source_id": "S3", "author": "Orphan", "title": "O", "quote": "unresolvable", "segment_id": "I-9"})
    art.citations.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    result = emit_local_wiki(TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki")
    assert any("S3" in w for w in result.warnings)
    text = result.path.read_text(encoding="utf-8")
    assert "unresolvable" not in text  # the orphan citation never made it into the file


def test_no_contested_claims_yields_none_observed(tmp_path, artifacts, registry):
    data = json.loads(artifacts.claims.read_text(encoding="utf-8"))
    for c in data["claims"]:
        c["contested"] = False
    artifacts.claims.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    result = emit_local_wiki(TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki")
    assert result.divergences == 0
    text = result.path.read_text(encoding="utf-8")
    assert "None observed in this article's claims." in text


def test_missing_lead_warns_and_uses_placeholder(tmp_path, artifacts, registry):
    artifacts.draft.write_text(json.dumps({"lead": [], "sections": [], "see_also": []}), encoding="utf-8")
    result = emit_local_wiki(TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki")
    assert any("no lead" in w for w in result.warnings)
    assert "no lead paragraph found" in result.path.read_text(encoding="utf-8")


def test_prefers_polished_draft_when_present(tmp_path, artifacts, registry):
    polished_text = "སྒྲོལ་མའི་ཞིབ་བཤད་གསར་བ།"
    artifacts.polished.write_text(
        json.dumps({"lead": [{"text": polished_text, "citations": [0]}], "sections": [], "see_also": []}),
        encoding="utf-8",
    )
    result = emit_local_wiki(TERM, "smoke", artifacts, registry, tmp_path / "Local-Wiki")
    text = result.path.read_text(encoding="utf-8")
    assert polished_text in text
    assert LEAD_TEXT not in text


def test_rerun_preserves_prior_version_in_history(tmp_path, artifacts, registry):
    out_dir = tmp_path / "Local-Wiki"
    first = emit_local_wiki(TERM, "smoke", artifacts, registry, out_dir)
    first_text = first.path.read_text(encoding="utf-8")

    # Change the lead so the second run produces genuinely different content.
    artifacts.draft.write_text(
        json.dumps({"lead": [{"text": "གསར་པའི་ངེས་ཚིག", "citations": [0]}], "sections": [], "see_also": []}),
        encoding="utf-8",
    )
    second = emit_local_wiki(TERM, "smoke", artifacts, registry, out_dir)

    history_dir = out_dir / "history"
    assert history_dir.is_dir()
    preserved = list(history_dir.glob(f"{TERM}.*.md"))
    assert len(preserved) == 1
    assert preserved[0].read_text(encoding="utf-8") == first_text
    assert "གསར་པའི་ངེས་ཚིག" in second.path.read_text(encoding="utf-8")
