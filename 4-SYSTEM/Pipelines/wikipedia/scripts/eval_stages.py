#!/usr/bin/env python3
"""Per-stage evaluation over a corpus's article artifacts.

Answers "how well is each important step performing" with metrics computed
deterministically from the artifacts on disk — no model calls unless
--audit-stability is given. Writes work/eval/EVAL_REPORT.md (English, for the
team and the IATS paper) and work/eval/eval.json (machine-readable).

Stages measured, per term:

  offer      what alignment put on the table for this term (segments, chars,
             commentaries with material)
  extract    what stage 4 captured: passages, capture ratio vs the offer,
             block-locator coverage, and extraction fidelity — every passage
             quote re-checked character-for-character against the reading view
  claims     stage 4b compression: claims per passage, passage utilization
             (extracted passages actually cited by ≥1 claim), type mix, drops
  outline    stage 5 placement: claims placed vs unused, gap report size
  draft      stage 6 coverage: % of claims cited in the article, paragraph
             citation discipline, article length vs the 1,500-syllable bar
  audit      stage 6b verdict on disk; with --audit-stability N, N repeated
             independent audits in an isolated temp workspace (real Gemini
             calls; ledger and artifacts untouched) → pass rate + finding
             categories, the number STATE.md says the paper must report
  verify     stage 7 re-run live (temp workspace): quote pass rate, locator
             resolution, warning histogram

Usage:
  ./.venv/bin/python scripts/eval_stages.py tara21
  ./.venv/bin/python scripts/eval_stages.py tara21 --audit-stability 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from kangyur_wiki import registry as registry_mod  # noqa: E402
from kangyur_wiki.stages import align as align_mod  # noqa: E402
from kangyur_wiki.stages.align import segments_for_term  # noqa: E402
from kangyur_wiki.stages.commentary import reading_view  # noqa: E402
from kangyur_wiki.stages.pipeline import (  # noqa: E402
    TermArtifacts,
    load_claims,
    run_audit,
    run_verify,
)
from kangyur_wiki.tibetan.verify import check_quote  # noqa: E402
from kangyur_wiki.wiki.wikitext import Citation  # noqa: E402

TSHEG = "་"
SHAD = "།"


def syllables(text: str) -> int:
    """ཚེག་བར count proxy: tsheg + shad boundaries, as the validator counts."""
    return text.count(TSHEG) + text.count(SHAD)


def source_loaders(comm_dir: Path):
    def raw(source_id: str) -> str:
        for p in sorted(comm_dir.glob("*.md")):
            if source_id in p.stem:
                return p.read_text(encoding="utf-8")
        raise FileNotFoundError(source_id)

    def reading(source_id: str) -> str:
        return reading_view(raw(source_id))

    return raw, reading


def eval_term(term: str, cdir: Path, alignment, raw, reading) -> dict:
    art = TermArtifacts(cdir / "articles" / term)
    out: dict = {"term": term}

    # ---- offer -----------------------------------------------------------
    segments = segments_for_term(alignment, term, raw)
    offer_chars = sum(len(s.text) for s in segments)
    offer_sources = {s.source_id for s in segments}
    out["offer"] = {
        "segments": len(segments),
        "chars": offer_chars,
        "commentaries_with_material": len(offer_sources),
    }

    # ---- extract ---------------------------------------------------------
    ex = json.loads(art.extract.read_text(encoding="utf-8"))
    passages = [p for p in ex.get("passages", []) if p.get("quote")]
    p_chars = sum(len(p["quote"]) for p in passages)
    fidelity = Counter()
    for p in passages:
        try:
            res = check_quote(p["quote"], reading(p["source_id"]), p["source_id"])
            fidelity[res.method if res.passed else "FAIL"] += 1
        except FileNotFoundError:
            fidelity["source-missing"] += 1
    silent = set(ex.get("no_explanation_in", []))
    out["extract"] = {
        "passages": len(passages),
        "chars": p_chars,
        "capture_ratio": round(p_chars / offer_chars, 3) if offer_chars else None,
        "distinct_sources": len({p["source_id"] for p in passages}),
        "block_located": sum(1 for p in passages if p.get("segment_id")),
        "fidelity": dict(fidelity),
        "fidelity_pass_rate": round(
            sum(v for k, v in fidelity.items() if k != "FAIL") / len(passages), 3
        ) if passages else None,
        "silent_claims_contradicted": sorted(
            s for s in silent if any(s in src for src in offer_sources)
            and any(s in p["source_id"] for p in passages)
        ),
    }

    # ---- claims ----------------------------------------------------------
    cl_data = json.loads(art.claims.read_text(encoding="utf-8"))
    claims = load_claims(art)
    used_passages = {i for c in claims for i in c.passage_indices}
    out["claims"] = {
        "claims": len(claims),
        "dropped_at_parse": len(cl_data.get("dropped", [])),
        "chars": sum(len(c.claim_bo) for c in claims),
        "compression_vs_extract": round(
            sum(len(c.claim_bo) for c in claims) / p_chars, 3
        ) if p_chars else None,
        "passage_utilization": round(len(used_passages) / len(passages), 3)
        if passages else None,
        "types": dict(Counter(c.claim_type for c in claims)),
        "contested": sum(1 for c in claims if getattr(c, "contested", False)),
        "school_tagged": sum(1 for c in claims if getattr(c, "school", "")),
    }

    # ---- outline ---------------------------------------------------------
    sec = json.loads(art.sections.read_text(encoding="utf-8"))
    placed = {i for s in sec.get("sections", []) for i in s.get("claim_indices", [])}
    placed |= set(sec.get("lead", []))
    out["outline"] = {
        "sections": len(sec.get("sections", [])),
        "claims_placed": len(placed & set(range(len(claims)))),
        "unused_declared": len(sec.get("unused", [])),
        "gap_report_lines": len(sec.get("gap_report", [])),
    }

    # ---- draft -----------------------------------------------------------
    draft = json.loads(art.draft.read_text(encoding="utf-8"))
    paras = list(draft.get("lead", []))
    for s in draft.get("sections", []):
        paras.extend(s.get("paragraphs", []))
    cited = {i for p in paras for i in p.get("citations", []) if isinstance(i, int)}
    wikitext = art.wikitext.read_text(encoding="utf-8")
    out["draft"] = {
        "paragraphs": len(paras),
        "paragraphs_cited": sum(1 for p in paras if p.get("citations")),
        "claim_coverage": round(len(cited & set(range(len(claims)))) / len(claims), 3)
        if claims else None,
        "article_chars": len(wikitext),
        "article_syllables_proxy": syllables(wikitext),
    }

    # ---- audit (on disk) -------------------------------------------------
    audit = json.loads(art.audit.read_text(encoding="utf-8"))
    out["audit_on_disk"] = {
        "verdict": audit.get("verdict"),
        "findings": len(audit.get("findings", [])),
    }

    # ---- verify (live, isolated) ----------------------------------------
    citations = [Citation(**c) for c in json.loads(art.citations.read_text("utf-8"))]
    with tempfile.TemporaryDirectory() as td:
        tmp_art = TermArtifacts(Path(td))
        result = run_verify(
            term, wikitext, citations, ["ནང་བསྟན།"], reading, tmp_art, raw_loader=raw
        )
    warn_hist = Counter(
        m.group(1)
        for f in result.findings
        if f.severity == "warning"
        for m in [re.match(r"^(W\d+)", f.rule or "")]
        if m
    )
    out["verify"] = {
        "passed": result.passed,
        "quote_failures": len(result.quote_failures),
        "citations": result.total_citations,
        "block_located": result.located,
        "locator_failures": len(result.locator_failures),
        "warnings": dict(warn_hist),
    }
    return out


def audit_stability(term: str, cdir: Path, n: int) -> dict:
    """N independent audits of the on-disk draft, in a temp workspace.

    Uses the same Gemini client + prompt library as `kwiki audit`, but never
    touches the article directory or the ledger — this is measurement, not a
    pipeline run.
    """
    from kangyur_wiki.config import load_settings
    from kangyur_wiki.llm.gemini import GeminiClient, PromptLibrary

    settings = load_settings()
    client = GeminiClient(
        api_key=settings.require_gemini_api_key(), model=settings.gemini_model
    )
    library = PromptLibrary(settings.prompts_dir)

    art = TermArtifacts(cdir / "articles" / term)
    draft_data = json.loads(art.draft.read_text(encoding="utf-8"))
    claims = load_claims(art)

    runs = []
    for _ in range(n):
        with tempfile.TemporaryDirectory() as td:
            res = run_audit(
                term, draft_data, claims, client.generate,
                lambda stage, **kw: library.render(stage, **kw), TermArtifacts(Path(td)),
            )
        runs.append(
            {
                "verdict": res.verdict,
                "passed": res.passed,
                "findings": len(res.findings),
                "blocking": len(res.blocking),
                "categories": sorted(
                    f.get("finding", "?") for f in res.findings if isinstance(f, dict)
                ),
            }
        )
    return {
        "model": client.model,
        "runs": runs,
        "pass_rate": round(sum(1 for r in runs if r["passed"]) / n, 3),
    }


def fmt_report(corpus: str, results: list[dict], stability: dict | None) -> str:
    lines = [f"# Stage evaluation — {corpus}", ""]
    lines.append(
        "Deterministic metrics computed from the on-disk artifacts (English labels "
        "throughout — this report is written for readers who do not read Tibetan). "
        "Generated by `scripts/eval_stages.py`; machine-readable copy in `eval.json`."
    )
    lines.append("")
    header = (
        "| stage / metric | " + " | ".join(r["term"] for r in results) + " |"
    )
    lines.append(header)
    lines.append("|---|" + "---|" * len(results))

    def row(label, fn):
        lines.append(f"| {label} | " + " | ".join(str(fn(r)) for r in results) + " |")

    row("**offer** — aligned segments", lambda r: r["offer"]["segments"])
    row("offer — characters", lambda r: f"{r['offer']['chars']:,}")
    row("offer — commentaries with material", lambda r: r["offer"]["commentaries_with_material"])
    row("**extract** — passages", lambda r: r["extract"]["passages"])
    row("extract — capture ratio (of offer)", lambda r: r["extract"]["capture_ratio"])
    row("extract — distinct sources", lambda r: r["extract"]["distinct_sources"])
    row("extract — block-located", lambda r: f"{r['extract']['block_located']}/{r['extract']['passages']}")
    row("extract — quote fidelity (char-exact)", lambda r: r["extract"]["fidelity_pass_rate"])
    row("**claims** — rows", lambda r: r["claims"]["claims"])
    row("claims — dropped at parse", lambda r: r["claims"]["dropped_at_parse"])
    row("claims — passage utilization", lambda r: r["claims"]["passage_utilization"])
    row("claims — compression (chars vs extract)", lambda r: r["claims"]["compression_vs_extract"])
    row("**outline** — sections", lambda r: r["outline"]["sections"])
    row("outline — claims placed", lambda r: f"{r['outline']['claims_placed']}/{r['claims']['claims']}")
    row("outline — gap-report lines", lambda r: r["outline"]["gap_report_lines"])
    row("**draft** — claim coverage", lambda r: r["draft"]["claim_coverage"])
    row("draft — paragraphs cited", lambda r: f"{r['draft']['paragraphs_cited']}/{r['draft']['paragraphs']}")
    row("draft — length (boundary-mark proxy)", lambda r: f"{r['draft']['article_syllables_proxy']:,}")
    row("draft — under validator's 1,500-syllable bar (W4)", lambda r: "yes" if r["verify"]["warnings"].get("W4") else "no")
    row("**audit** (on disk) — verdict", lambda r: r["audit_on_disk"]["verdict"])
    row("**verify** — passed", lambda r: "PASS" if r["verify"]["passed"] else "FAIL")
    row("verify — quotes exact", lambda r: f"{r['verify']['citations'] - r['verify']['quote_failures']}/{r['verify']['citations']}")
    row("verify — locators resolve", lambda r: f"{r['verify']['block_located']}/{r['verify']['citations']}")
    lines.append("")

    if stability:
        lines.append("## Audit stability (repeated independent runs)")
        lines.append("")
        for term, s in stability.items():
            cats = Counter(c for r in s["runs"] for c in r["categories"])
            lines.append(
                f"- **{term}** — {len(s['runs'])} runs on {s['model']}: "
                f"pass rate {s['pass_rate']}, verdicts "
                f"{[r['verdict'] for r in s['runs']]}, finding categories {dict(cats) or 'none'}"
            )
        lines.append("")
        lines.append(
            "Report audit outcomes as pass rates over repeated runs, never a single "
            "verdict (STATE.md rule; the auditor is nondeterministic)."
        )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("corpus")
    ap.add_argument("--audit-stability", type=int, default=0, metavar="N",
                    help="run N independent Gemini audits per term (live API calls)")
    args = ap.parse_args()

    cdir = REPO / "corpora" / args.corpus
    alignment = align_mod.load_alignment(cdir / "work" / "aligned.json")
    raw, reading = source_loaders(cdir / "source" / "commentaries")
    registry_mod.load(cdir)  # fail fast if the registry is broken

    terms = sorted(p.name for p in (cdir / "articles").iterdir()
                   if p.is_dir() and (p / "extract.json").exists())
    results = [eval_term(t, cdir, alignment, raw, reading) for t in terms]

    stability = None
    if args.audit_stability:
        stability = {t: audit_stability(t, cdir, args.audit_stability) for t in terms}

    out_dir = cdir / "work" / "eval"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "eval.json").write_text(
        json.dumps({"corpus": args.corpus, "terms": results, "audit_stability": stability},
                   ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    (out_dir / "EVAL_REPORT.md").write_text(
        fmt_report(args.corpus, results, stability), encoding="utf-8"
    )
    print(f"evaluated {len(results)} terms")
    print(f"  report: {out_dir / 'EVAL_REPORT.md'}")
    print(f"  data:   {out_dir / 'eval.json'}")


if __name__ == "__main__":
    main()
