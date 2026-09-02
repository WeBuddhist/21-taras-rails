#!/usr/bin/env python3
"""Run stages 4-7 with Claude standing in for Gemini, on the unchanged code path.

Why this exists: `generativelanguage.googleapis.com` is 403'd at the egress proxy
in both the cloud sandbox and the desktop bridge, so `GeminiClient` cannot make a
call however valid the key is. Rather than fake a run (pipeline.md forbids that),
this splits each model stage into two halves:

    prompt <term> <stage>   render the real prompt from prompts/ to a file
    apply  <term> <stage>   read the model's JSON reply and run the real stage

Everything between the two halves — the prompt text, the JSON schema, the
artifact writing, and above all stage 7's deterministic quote gate — is the
repo's own code, untouched. Only the identity of the model changes, and that is
recorded in `model.json` next to the artifacts so no number from this run can be
mistaken for a Gemini number.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from kangyur_wiki import registry as registry_mod
from kangyur_wiki.config import load_settings
from kangyur_wiki.ledger import Ledger, TermStatus, ledger_path
from kangyur_wiki.llm.gemini import PromptLibrary
from kangyur_wiki.stages import align as align_mod
from kangyur_wiki.stages.pipeline import (
    AUDIT_SCHEMA,
    CLAIMS_SCHEMA,
    DRAFT_SCHEMA,
    EXTRACT_SCHEMA,
    ORGANIZE_SCHEMA,
    Passage,
    TermArtifacts,
    load_claims,
    run_audit,
    run_claims,
    run_draft,
    run_extract,
    run_organize,
    run_verify,
)

MODEL_ID = "claude-opus-5"
CORPUS = "tara21"

STAGES = {
    "extract": ("04-extract", EXTRACT_SCHEMA),
    "claims": ("04b-claims", CLAIMS_SCHEMA),
    "organize": ("05-organize", ORGANIZE_SCHEMA),
    "draft": ("06-draft", DRAFT_SCHEMA),
    "audit": ("06b-audit", AUDIT_SCHEMA),
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _slug(term: str) -> str:
    return term.strip("།་")


def _setup(term: str):
    settings = load_settings()
    cdir = settings.corpus_dir(CORPUS)
    reg = registry_mod.load(cdir)
    alignment = align_mod.load_alignment(cdir / "work" / "aligned.json")
    library = PromptLibrary(settings.prompts_dir)
    artifacts = TermArtifacts(cdir / "articles" / _slug(term))
    return settings, cdir, reg, alignment, library, artifacts


class _Recorder:
    """A `generate` callable that writes the prompt out and reads the reply back."""

    def __init__(self, io_dir: Path, stage: str, mode: str):
        self.io = io_dir
        self.stage = stage
        self.mode = mode          # 'prompt' | 'apply'
        self.io.mkdir(parents=True, exist_ok=True)

    def __call__(self, prompt: str, schema=None):
        p = self.io / f"{self.stage}.prompt.txt"
        r = self.io / f"{self.stage}.response.json"
        if self.mode == "prompt":
            p.write_text(prompt, encoding="utf-8")
            (self.io / f"{self.stage}.schema.json").write_text(
                json.dumps(schema, ensure_ascii=False, indent=1), encoding="utf-8")
            raise SystemExit(f"PROMPT_WRITTEN {p} ({len(prompt)} chars)")
        if not r.exists():
            raise SystemExit(f"missing reply: {r}")
        return json.loads(r.read_text(encoding="utf-8"))


def cmd_prompt(term: str, stage: str) -> None:
    settings, cdir, reg, alignment, library, artifacts = _setup(term)
    io = cdir / "work" / "claude_io" / _slug(term)
    gen = _Recorder(io, stage, "prompt")
    render = lambda stage, **kw: library.render(stage, **kw)  # noqa: E731

    if stage == "extract":
        run_extract(term, alignment, gen, render, artifacts)
    elif stage == "claims":
        run_claims(term, _passages(artifacts), reg, gen, render, artifacts)
    elif stage == "organize":
        run_organize(term, load_claims(artifacts), gen, render, artifacts)
    elif stage == "draft":
        org = json.loads(artifacts.sections.read_text(encoding="utf-8"))
        run_draft(term, _passages(artifacts), load_claims(artifacts), org, reg,
                  gen, render, artifacts)
    elif stage == "audit":
        source = artifacts.polished if artifacts.polished.exists() else artifacts.draft
        draft_data = json.loads(source.read_text(encoding="utf-8"))
        run_audit(term, draft_data, load_claims(artifacts), gen, render, artifacts)
    else:
        raise SystemExit(f"unknown stage {stage}")


def _passages(artifacts: TermArtifacts) -> list[Passage]:
    data = json.loads(artifacts.extract.read_text(encoding="utf-8"))
    return [Passage(**{k: p.get(k, "") for k in
                       ("source_id", "quote", "kind", "segment_id", "note")})
            for p in data.get("passages", [])]


def cmd_apply(term: str, stage: str) -> None:
    settings, cdir, reg, alignment, library, artifacts = _setup(term)
    io = cdir / "work" / "claude_io" / _slug(term)
    gen = _Recorder(io, stage, "apply")
    render = lambda stage, **kw: library.render(stage, **kw)  # noqa: E731
    led = Ledger.load(ledger_path(settings.corpora_dir, CORPUS), corpus_id=CORPUS)

    if stage == "extract":
        passages = run_extract(term, alignment, gen, render, artifacts)
        print(f"extract:  {len(passages)} passages from "
              f"{len({p.source_id for p in passages})} distinct commentaries")
        led.set_status(term, TermStatus.EXTRACTED, _now())
    elif stage == "claims":
        claims = run_claims(term, _passages(artifacts), reg, gen, render, artifacts)
        print(f"claims:   {len(claims)} claims, "
              f"{sum(1 for c in claims if c.claim_type != 'consensus')} below consensus")
        led.set_status(term, TermStatus.CLAIMED if claims else TermStatus.FAILED, _now())
    elif stage == "organize":
        org = run_organize(term, load_claims(artifacts), gen, render, artifacts)
        print(f"organize: {len(org.get('sections', []))} sections, "
              f"{len(org.get('unused', []))} claims unused")
        led.set_status(term, TermStatus.ORGANIZED, _now())
    elif stage == "draft":
        org = json.loads(artifacts.sections.read_text(encoding="utf-8"))
        wikitext, citations = run_draft(term, _passages(artifacts), load_claims(artifacts),
                                        org, reg, gen, render, artifacts)
        print(f"draft:    {len(wikitext)} chars, {len(citations)} citations")
        led.set_status(term, TermStatus.DRAFTED, _now())
    elif stage == "audit":
        source = artifacts.polished if artifacts.polished.exists() else artifacts.draft
        draft_data = json.loads(source.read_text(encoding="utf-8"))
        audit = run_audit(term, draft_data, load_claims(artifacts), gen, render, artifacts)
        print(f"audit:    {audit.verdict or 'no verdict'} — "
              f"{len(audit.blocking)} blocking of {len(audit.findings)} findings")
        led.set_status(term, TermStatus.AUDITED if audit.passed else TermStatus.FAILED,
                       _now(), error=None if audit.passed else "audit found blocking issues")
    elif stage == "verify":
        wikitext = artifacts.wikitext.read_text(encoding="utf-8")
        citations = [
            __import__("kangyur_wiki.wiki.wikitext", fromlist=["Citation"]).Citation(**c)
            for c in json.loads(artifacts.citations.read_text(encoding="utf-8"))
        ]
        comm_dir = cdir / "source" / "commentaries"

        def source_loader(source_id: str) -> str:
            src = reg.source(source_id)
            if src is not None and src.local_path:
                p = cdir / src.local_path
                if p.exists():
                    return p.read_text(encoding="utf-8")
            for p in comm_dir.glob("*.md"):
                if source_id in p.stem:
                    return p.read_text(encoding="utf-8")
            raise FileNotFoundError(f"no commentary file matching source_id {source_id!r}")

        result = run_verify(term, wikitext, citations, ["ནང་བསྟན།"], source_loader, artifacts)
        n_err = sum(1 for f in result.findings if f.severity == "error")
        print("verify:   " + ("PASS" if result.passed else
                              f"FAIL — {n_err} errors, "
                              f"{len(result.quote_failures)} unverifiable quotations"))
        led.set_status(term, TermStatus.VERIFIED if result.passed else TermStatus.FAILED,
                       _now(), error=None if result.passed else "verification failed")
        artifacts.root.joinpath("model.json").write_text(json.dumps({
            "model": MODEL_ID,
            "note": ("Stages 4-6 were run with Claude standing in for Gemini: "
                     "generativelanguage.googleapis.com is 403'd at the egress proxy in "
                     "this environment. Prompts, schemas, artifact writing and the stage-7 "
                     "verification gate are the repo's own code, unmodified. Do not report "
                     "these as Gemini numbers."),
            "run_at": _now(),
            "prompts": {s: library.get(s).path.name
                        for s in ("04-extract", "04b-claims", "05-organize",
                                  "06-draft", "06b-audit")},
        }, ensure_ascii=False, indent=1), encoding="utf-8")
    else:
        raise SystemExit(f"unknown stage {stage}")
    led.save()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["prompt", "apply"])
    ap.add_argument("term")
    ap.add_argument("stage", choices=["extract", "claims", "organize", "draft", "audit", "verify"])
    a = ap.parse_args()
    (cmd_prompt if a.command == "prompt" else cmd_apply)(a.term, a.stage)
