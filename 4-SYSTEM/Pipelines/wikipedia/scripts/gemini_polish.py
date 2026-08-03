#!/usr/bin/env python3
"""Step 11 of the canonical pipeline: the Gemini literary rewrite.

`docs/reference/cowork-pipeline.md` names three scripts; this is the Gemini one
(`4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/11-polish/SKILL.md` declares it). It sends the draft
plus the handoff prompt and the locked glossary to Gemini and writes the result back,
**with the model version pinned and logged per run** so the step-13 feedback loop can
tell a prompt problem from model-version drift.

Why a script and not only `kwiki polish`: the canonical pipeline runs in Cowork, where
steps are invoked by name and the Gemini leg is a script the skill shells out to. Both
doors call the same `stages.pipeline.run_polish`, so there is one implementation and no
way for the two to drift.

    python scripts/gemini_polish.py tara21 སྒྲོལ་མ།
    python scripts/gemini_polish.py tara21 སྒྲོལ་མ། --model gemini-3.5-flash
    python scripts/gemini_polish.py tara21 སྒྲོལ་མ། --dry-run   # render the prompt, call nothing

**Gemini is a stylist, not an editor.** The four hard constraints are enforced in code,
not merely asked for in the prompt: if the rewrite changes any citations array, paragraph
count, heading order, or see-also list, it is rejected whole, nothing on disk changes, and
this exits non-zero. After an accepted polish the prose has changed, so `kwiki audit` and
`kwiki verify` must both be re-run — the audit reads meaning, the gate reads characters,
and neither has seen this text yet.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from kangyur_wiki import registry as registry_mod
from kangyur_wiki.config import load_settings
from kangyur_wiki.stages.pipeline import (
    Passage,
    TermArtifacts,
    glossary_for,
    load_claims,
    record_stage_model,
    run_polish,
)

STAGE = "06a-polish"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _passages(artifacts: TermArtifacts) -> list[Passage]:
    data = json.loads(artifacts.extract.read_text(encoding="utf-8"))
    return [
        Passage(
            source_id=p.get("source_id", ""),
            quote=p.get("quote", ""),
            kind=p.get("kind", ""),
            segment_id=p.get("segment_id", ""),
            note=p.get("note", ""),
        )
        for p in data.get("passages", [])
        if p.get("quote")
    ]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", help="Corpus id, e.g. tara21")
    ap.add_argument("term", help="The key term whose draft should be polished")
    ap.add_argument("--model", default=None, help="Override the Gemini model id (default: settings)")
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Render the handoff prompt to stdout and exit. No API call, nothing written.",
    )
    args = ap.parse_args(argv)

    from kangyur_wiki.llm.gemini import GeminiClient, PromptLibrary  # late: needs an API key

    settings = load_settings()
    cdir = settings.corpus_dir(args.corpus)
    artifacts = TermArtifacts(cdir / "articles" / args.term.strip("།་"))

    for needed in (artifacts.draft, artifacts.claims, artifacts.extract):
        if not needed.exists():
            print(f"error: no {needed} — run the earlier stages first", file=sys.stderr)
            return 2

    library = PromptLibrary(settings.prompts_dir)
    prompt_file = library.get(STAGE).path.name

    if args.dry_run:
        print(
            library.render(
                STAGE,
                term=args.term,
                draft_json=artifacts.draft.read_text(encoding="utf-8"),
                glossary=glossary_for(args.term),
            )
        )
        return 0

    registry = registry_mod.load(cdir)
    client = GeminiClient(
        api_key=settings.require_gemini_api_key(), model=args.model or settings.gemini_model
    )

    def prompt_render(stage: str, **kwargs) -> str:
        return library.render(stage, **kwargs)

    result = run_polish(
        args.term,
        _passages(artifacts),
        load_claims(artifacts),
        registry,
        client.generate,
        prompt_render,
        artifacts,
    )
    # Logged whether or not the rewrite was accepted: a rejection is a fact about
    # this model version, and that is exactly what the feedback loop wants to see.
    record_stage_model(
        artifacts, STAGE, model=client.model, prompt=prompt_file, run_at=_now()
    )

    if not result.accepted:
        print(f"polish REJECTED ({client.model}, {prompt_file}) — nothing was changed:")
        for problem in result.structure_problems:
            print(f"  - {problem}")
        print("\nThe stylist broke a hard constraint. Fix the prompt or try another model;")
        print("do not relax the check — it is what keeps the rewrite from silently")
        print("re-sourcing a sentence.")
        return 1

    print(f"polish accepted ({client.model}, {prompt_file}) — {len(result.wikitext)} chars")
    print(f"  polished: {artifacts.polished}")
    print(f"  article:  {artifacts.wikitext}")
    print(f"  model log: {artifacts.model}")
    print(f"\nRe-run `kwiki audit {args.corpus} {args.term}` and "
          f"`kwiki verify {args.corpus} {args.term}` — the prose changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
