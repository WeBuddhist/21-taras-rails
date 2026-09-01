"""End-to-end wiring test for stages 4–7 with a stubbed model.

Proves the chain extract → claims → outline → draft → audit → verify holds together and
that both gates actually bite, without needing an API key or the network. The stub returns
quotations taken verbatim from the real commentary fixture, so a passing run means the
citation checker is finding real text — the deliberately-corrupted variant proves the
deterministic gate fails when the text is not real, and the blocking-audit variant proves
the claims audit fails when the model reports drift.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from kangyur_wiki.registry import Registry, Source, TermRecord
from kangyur_wiki.stages.align import AlignedSpan, AlignmentReport
from kangyur_wiki.stages.pipeline import (
    Claim,
    Passage,
    TermArtifacts,
    run_audit,
    run_claims,
    run_draft,
    run_extract,
    run_organize,
    run_polish,
    run_verify,
)

TERM = "བྱང་ཆུབ་ཀྱི་སེམས།"

# A real sentence shape from the Bodhicaryāvatāra commentary tradition.
QUOTE_A = "བྱང་ཆུབ་ཀྱི་སེམས་ནི་གཞན་གྱི་དོན་དུ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འདོད་པའི་སེམས་སོ།།"
QUOTE_B = "སེམས་བསྐྱེད་པ་ནི་གཞན་དོན་ཕྱིར། །ཡང་དག་རྫོགས་པའི་བྱང་ཆུབ་འདོད།།"

COMMENTARY = (
    "༄༅། །འདིར་བཤད་པ།\n"
    f"{QUOTE_A}\n"
    "དེ་ལྟར་ན་སེམས་བསྐྱེད་ཀྱི་མཚན་ཉིད་བསྟན་པའོ།།\n"
    f"{QUOTE_B}\n"
    "ཞེས་གསུངས་སོ།།\n"
)


class StubResult:
    def __init__(self, parsed):
        self.parsed = parsed
        self.text = json.dumps(parsed, ensure_ascii=False)


class StubModel:
    """Returns a canned structured response per stage, keyed by schema shape."""

    def __init__(self, *, corrupt: bool = False, audit_blocking: bool = False):
        self.corrupt = corrupt
        self.audit_blocking = audit_blocking
        self.calls: list[str] = []

    def generate(self, prompt: str, *, schema=None, **kwargs):
        props = set((schema or {}).get("properties", {}))
        if "passages" in props:
            self.calls.append("extract")
            quote_b = QUOTE_B + "བསླད་པ།" if self.corrupt else QUOTE_B
            return StubResult(
                {
                    "term": TERM,
                    "passages": [
                        {"source_id": "TESTCOMM", "segment_id": "1-15", "quote": QUOTE_A,
                         "kind": "མཚན་ཉིད།", "note": "ངོ་བོ་སྟོན།"},
                        {"source_id": "TESTCOMM", "segment_id": "1-16", "quote": quote_b,
                         "kind": "ལུང་།", "note": "ལུང་དྲངས།"},
                    ],
                    "no_explanation_in": [],
                }
            )
        if "claims" in props:
            self.calls.append("claims")
            return StubResult(
                {
                    "term": TERM,
                    "claims": [
                        {"id": "C1",
                         "claim_bo": "བྱང་ཆུབ་ཀྱི་སེམས་ནི་གཞན་དོན་དུ་བྱང་ཆུབ་འདོད་པའི་སེམས་ཡིན།",
                         "passage_indices": [0], "claim_type": "consensus",
                         "school": "", "reception": "unengaged", "contested": False},
                        {"id": "C2",
                         "claim_bo": "ལུང་ལས་སེམས་བསྐྱེད་གཞན་དོན་ཕྱིར་ཞེས་གསུངས།",
                         "passage_indices": [1], "claim_type": "school-position",
                         "school": "dge lugs", "reception": "cited by later manuals",
                         "contested": False},
                        # No valid passages behind it — must be dropped, never drafted from.
                        {"id": "C3", "claim_bo": "རྒྱུ་ཆ་མེད་པའི་གྲུབ་དོན།",
                         "passage_indices": [99], "claim_type": "consensus"},
                    ],
                    "forbidden_syntheses": [],
                }
            )
        if "sections" in props and "lead" in props and "claim_indices" in json.dumps(schema):
            self.calls.append("organize")
            return StubResult(
                {
                    "term": TERM,
                    "lead": [0],
                    "sections": [{"heading": "མཚན་ཉིད།", "claim_indices": [0, 1],
                                  "divergence": False, "attribution_required": True}],
                    "unused": [],
                    "gap_report": [],
                }
            )
        if "findings" in props:
            self.calls.append("audit")
            if self.audit_blocking:
                return StubResult(
                    {
                        "term": TERM,
                        "findings": [
                            {"sentence": "གསར་བཟོའི་བརྗོད་པ།", "claim_indices": [],
                             "finding": "added-fact", "severity": "blocking",
                             "note": "no claim covers this"},
                        ],
                        "verdict": "fix",
                    }
                )
            return StubResult({"term": TERM, "findings": [], "verdict": "publish"})
        self.calls.append("draft")
        return StubResult(
            {
                "lead": [{"text": "ནི་གཞན་དོན་དུ་བྱང་ཆུབ་འདོད་པའི་སེམས་ཡིན།", "citations": [0]}],
                "sections": [
                    {
                        "heading": "མཚན་ཉིད།",
                        "paragraphs": [
                            {"text": "མཚན་ཉིད་ནི་འདི་ལྟར་ཏེ།", "citations": [0]},
                            {"text": "ལུང་ལས་ཀྱང་གསུངས་སོ།", "citations": [1]},
                        ],
                    }
                ],
                "see_also": ["སྨོན་པའི་སེམས་"],
            }
        )


@pytest.fixture
def corpus(tmp_path: Path) -> Path:
    comm = tmp_path / "source" / "commentaries"
    comm.mkdir(parents=True)
    (comm / "TESTCOMM.md").write_text(COMMENTARY, encoding="utf-8")
    return tmp_path


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
def alignment() -> AlignmentReport:
    rep = AlignmentReport(corpus="test", total_verses=2)
    rep.spans = [
        AlignedSpan(
            verse_id="1-15",
            source_id="TESTCOMM",
            start_line=1,
            end_line=5,
            text=COMMENTARY,
            method="transclusion",
            confidence=1.0,
        )
    ]
    return rep


def _loader(corpus: Path):
    def load(source_id: str) -> str:
        return (corpus / "source" / "commentaries" / f"{source_id}.md").read_text("utf-8")

    return load


def _prompt_render(stage: str, **kwargs) -> str:
    return f"[{stage}] " + " ".join(f"{k}={str(v)[:40]}" for k, v in kwargs.items())


def _run_chain(corpus: Path, registry: Registry, alignment: AlignmentReport, model: StubModel):
    art = TermArtifacts(corpus / "articles" / "test")
    passages = run_extract(TERM, alignment, model.generate, _prompt_render, art)
    claims = run_claims(TERM, passages, registry, model.generate, _prompt_render, art)
    organization = run_organize(TERM, claims, model.generate, _prompt_render, art)
    wikitext, citations = run_draft(
        TERM, passages, claims, organization, registry, model.generate, _prompt_render, art
    )
    draft_data = json.loads(art.draft.read_text("utf-8"))
    audit = run_audit(TERM, draft_data, claims, model.generate, _prompt_render, art)
    result = run_verify(TERM, wikitext, citations, ["ནང་བསྟན།"], _loader(corpus), art)
    return art, passages, claims, wikitext, citations, audit, result


def test_chain_produces_a_verified_article(corpus, registry, alignment):
    model = StubModel()
    art, passages, claims, wikitext, citations, audit, result = _run_chain(
        corpus, registry, alignment, model
    )

    assert model.calls == ["extract", "claims", "organize", "draft", "audit"]
    assert len(passages) == 2
    # The unsupported claim C3 was dropped at parse time — the claims table is the only
    # drafting input, so an unciteable claim must not exist in it.
    assert [c.id for c in claims] == ["C1", "C2"]
    assert json.loads(art.claims.read_text("utf-8"))["dropped"]
    assert len(citations) == 2

    # The canonical skeleton, per docs/reference/wikitext-spec.md §1.
    assert wikitext.startswith(f"'''{TERM}'''")
    assert "== མཚན་ཉིད། ==" in wikitext
    assert "== ལུང་ཁུངས། ==" in wikitext
    assert "<references />" in wikitext
    assert "{{Reflist}}" not in wikitext
    assert "[[རིགས་དབྱེ།:ནང་བསྟན།]]" in wikitext

    # Citation URLs come from the registry, never from the model — and the quotations come
    # from extract.json, never from the drafting model, which only ever saw claims.
    assert "wikisource.org/wiki/TEST" in wikitext
    assert "dummy.com" not in wikitext
    assert citations[0].quote == QUOTE_A

    assert audit.passed
    assert result.passed, result.format_report()
    assert not result.quote_failures

    for path in (art.extract, art.claims, art.sections, art.draft, art.audit,
                 art.audit_report, art.wikitext, art.citations, art.report):
        assert path.exists(), path


def test_gate_rejects_a_quotation_not_in_the_source(corpus, registry, alignment):
    """The whole safety argument in one test: invented text cannot reach publication.

    The audit stub says "publish" here — the deterministic gate must bite on its own.
    """
    model = StubModel(corrupt=True)
    *_, audit, result = _run_chain(corpus, registry, alignment, model)

    assert audit.passed  # the LLM audit saw nothing wrong…
    assert not result.passed  # …and the character-for-character gate still failed the build
    assert result.quote_failures
    assert any("TESTCOMM" in f for f in result.quote_failures)
    assert "FAIL" in result.format_report()


def test_audit_blocks_on_added_fact(corpus, registry, alignment):
    """Invariant 2: a blocking audit finding fails the build even when quotes verify."""
    model = StubModel(audit_blocking=True)
    *_, audit, result = _run_chain(corpus, registry, alignment, model)

    assert result.passed  # quotations are genuine…
    assert not audit.passed  # …but the audit's added-fact finding blocks publication
    assert audit.blocking
    assert "does not pass" in audit.format_report()


def test_polish_rejected_when_structure_changes(corpus, registry, alignment, tmp_path):
    """The stylist is never trusted with structure: a changed citations array is refused."""
    model = StubModel()
    art, passages, claims, *_ = _run_chain(corpus, registry, alignment, model)

    class RestructuringStylist:
        def generate(self, prompt: str, *, schema=None, **kwargs):
            data = json.loads(art.draft.read_text("utf-8"))
            data["lead"][0]["citations"] = []  # drops the lead's sourcing
            return StubResult(data)

    before = art.wikitext.read_text("utf-8")
    result = run_polish(
        TERM, passages, claims, registry, RestructuringStylist().generate,
        _prompt_render, art,
    )
    assert not result.accepted
    assert result.structure_problems
    assert not art.polished.exists()
    assert art.wikitext.read_text("utf-8") == before  # nothing on disk changed


def test_polish_accepted_rerenders_same_citations(corpus, registry, alignment):
    model = StubModel()
    art, passages, claims, _, citations, *_ = _run_chain(corpus, registry, alignment, model)

    class FaithfulStylist:
        def generate(self, prompt: str, *, schema=None, **kwargs):
            data = json.loads(art.draft.read_text("utf-8"))
            data["lead"][0]["text"] = "བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་བྱ་བ་ནི་གཞན་དོན་དུ་བྱང་ཆུབ་འདོད་པའི་སེམས་ཏེ་ལེགས་པར་བཤད།"
            return StubResult(data)

    result = run_polish(
        TERM, passages, claims, registry, FaithfulStylist().generate, _prompt_render, art
    )
    assert result.accepted
    assert art.polished.exists()
    assert len(result.citations) == len(citations)
    assert "ལེགས་པར་བཤད" in art.wikitext.read_text("utf-8")

    # A re-run of the draft stage invalidates the old polish — otherwise a later
    # standalone audit would prefer stale text.
    organization = json.loads(art.sections.read_text("utf-8"))
    run_draft(
        TERM, passages, claims, organization, registry, StubModel().generate,
        _prompt_render, art,
    )
    assert not art.polished.exists()
    # …but not destroyed: the invalidated polish is preserved in history/, like
    # every artifact a re-run overwrites.
    hist = art.root / "history"
    assert list(hist.glob("draft_polished.*.json")), sorted(p.name for p in hist.iterdir())


def test_reruns_preserve_prior_artifacts_in_history(corpus, registry, alignment):
    """A re-run may never silently discard evidence (audit rounds, old reports).

    The tara21 review lost its intermediate audit rounds to in-place overwrites —
    the exact record the step-13 feedback loop and the paper's pass-rate metric
    need. Every overwriting stage now snapshots the outgoing file first.
    """
    model = StubModel()
    art, passages, claims, wikitext, citations, audit, result = _run_chain(
        corpus, registry, alignment, model
    )
    first_audit = art.audit_report.read_text("utf-8")
    first_report = art.report.read_text("utf-8")

    draft_data = json.loads(art.draft.read_text("utf-8"))
    run_audit(TERM, draft_data, claims, StubModel(audit_blocking=True).generate,
              _prompt_render, art)
    run_verify(TERM, wikitext, citations, ["ནང་བསྟན།"], _loader(corpus), art)

    hist = art.root / "history"
    audits = sorted(hist.glob("audit.*.md"))
    reports = sorted(hist.glob("report.*.md"))
    assert audits and reports, sorted(p.name for p in hist.iterdir()) if hist.exists() else "no history/"
    # The preserved bytes are the first round's, not the second's.
    assert audits[0].read_text("utf-8") == first_audit
    assert reports[0].read_text("utf-8") == first_report
    # And the live artifacts are the new round's.
    assert art.audit_report.read_text("utf-8") != first_audit
    assert "audit.json" in {p.name for p in art.root.iterdir()} and list(hist.glob("audit.*.json"))


def test_extract_with_no_matching_spans_writes_an_empty_artifact(corpus, registry):
    empty = AlignmentReport(corpus="test", total_verses=0)
    art = TermArtifacts(corpus / "articles" / "empty")
    model = StubModel()
    passages = run_extract(TERM, empty, model.generate, _prompt_render, art)
    assert passages == []
    assert model.calls == []  # no spans, so the model is never called — no wasted tokens
    assert json.loads(art.extract.read_text("utf-8"))["passages"] == []
