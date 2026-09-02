"""Fix pass over the tara21 drafts, per the adjudicated cross-model audit findings.

Edits draft.json only (the drafter's own artifact), then re-renders article.wiki +
citations.json through the repo's render_draft_payload — the same deterministic
renderer run_draft uses, so quotations still enter only from extract.json. A
citations-array equality assertion guarantees the fix pass moved no references.

Findings fixed (audit 2026-08-02, gemini-3.5-flash auditing claude-sonnet-5 drafts):
  སྒྲོལ་མ    lead exaggerated three scholars to many (dropped-qualifier)
             ངེས་ཚིག added "none dispute it" beyond claim_bo (added-fact; claim
             metadata does say uncontested — tightened to claim_bo wording anyway)
             མཚན་ཉིད over-generalized 4 attested verse-names to "each verse" (added-fact)
  སྡུག་བསྔལ  lead said མཚན་ཉིད (defining characteristic) where claim 0 says the
             name's meaning (meaning-shift)
             claim-2 sentence attributed "one commentary" to Gendun Drub by name
             (added-fact; the ref carries the source identity, prose follows the claim)
  all three  lead body restated the term, which render_lead's bolded-term prepend
             duplicated (cosmetic; the draft-prompt tuning item)
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/tashitsering/Desktop/work/IATS-2026")
sys.path.insert(0, str(REPO / "src"))

from kangyur_wiki import registry as registry_mod
from kangyur_wiki.stages.pipeline import (
    Passage,
    TermArtifacts,
    load_claims,
    render_draft_payload,
)

CDIR = REPO / "corpora" / "tara21"

EDITS = {
    "སྒྲོལ་མ": [
        # finding 1: three scholars, not many — and drop the duplicated leading term
        ("སྒྲོལ་མ་ཞེས་པའི་མིང་གི་ངེས་ཚིག་ལ་མཁས་པ་མི་འདྲ་བ་མང་པོས་",
         "ཞེས་པའི་མིང་གི་ངེས་ཚིག་ལ་མཁས་པ་མི་འདྲ་བ་གསུམ་གྱིས་"),
        # finding 2: hew to claim_bo's ending
        ("མིང་གི་དོན་ལ་མཐུན་ཞིང་སུས་ཀྱང་མ་བསྙོན་པའོ།",
         "མིང་གི་དོན་ལ་མཐུན་པའོ།"),
        # finding 3: names for some verses, not every verse
        ("བསྟོད་པའི་ཚིག་རེ་རེའི་མཚན་ལ་མིང་གཞན་སོ་སོ་བཏགས་ཏེ།",
         "བསྟོད་པའི་ཚིག་འགའ་ཞིག་གི་མཚན་ལ་མིང་གཞན་སོ་སོར་བཏགས་ཏེ།"),
    ],
    "འཇིག་རྟེན་གསུམ": [
        # lead dedup only (audit passed this article)
        ("འཇིག་རྟེན་གསུམ་ཞེས་པ་ནི་ཐུན་མོང་",
         "ཞེས་པ་ནི་ཐུན་མོང་"),
    ],
    "སྡུག་བསྔལ": [
        # finding 1: the claim is about the name's meaning, not a མཚན་ཉིད — plus lead dedup
        ("སྡུག་བསྔལ་ཞེས་པའི་མིང་དོན་ལ་བརྟེན་ནས་སྒྲོལ་མའི་མཚན་ཉིད་ཉིད་ཀྱང་འགྲེལ་བར་བྱེད་དེ།",
         "ཞེས་པའི་མིང་དོན་ལ་བརྟེན་ནས་སྒྲོལ་མའི་མཚན་གྱི་དོན་ཡང་འགྲེལ་བར་བྱེད་དེ།"),
        # finding 2: the claim says one commentary, unnamed; the ref names the source
        ("རྒྱལ་བ་དགེ་འདུན་གྲུབ་ཀྱི་འགྲེལ་བཤད་ནང་། མཁས་པ་གཞན་ཁ་ཅིག་གི་",
         "འགྲེལ་པ་གཅིག་གིས་མཁས་པ་གཞན་ཁ་ཅིག་གི་"),
    ],
}


def walk_paras(draft: dict):
    for p in draft.get("lead", []):
        yield p
    for s in draft.get("sections", []):
        for p in s.get("paragraphs", []):
            yield p


def main() -> None:
    reg = registry_mod.load(CDIR)
    for term, edits in EDITS.items():
        artifacts = TermArtifacts(CDIR / "articles" / term)
        draft = json.loads(artifacts.draft.read_text(encoding="utf-8"))

        applied = 0
        for old, new in edits:
            hits = [p for p in walk_paras(draft) if old in (p.get("text") or "")]
            assert len(hits) == 1, f"{term}: edit target not unique ({len(hits)} hits): {old[:40]}…"
            hits[0]["text"] = hits[0]["text"].replace(old, new)
            applied += 1

        claims = load_claims(artifacts)
        extract = json.loads(artifacts.extract.read_text(encoding="utf-8"))
        passages = [
            Passage(
                source_id=p.get("source_id", ""),
                quote=p.get("quote", ""),
                kind=p.get("kind", ""),
                segment_id=p.get("segment_id", ""),
                note=p.get("note", ""),
            )
            for p in extract.get("passages", [])
            if p.get("quote")
        ]

        before = json.loads(artifacts.citations.read_text(encoding="utf-8"))
        wikitext, citations = render_draft_payload(
            term, draft, claims, passages, reg, ["ནང་བསྟན།"]
        )
        after = [json.loads(json.dumps(c.__dict__, ensure_ascii=False, default=str)) for c in citations]
        assert len(before) == len(after), f"{term}: citation count changed {len(before)}→{len(after)}"
        for b, a in zip(before, after):
            assert b.get("source_id") == a.get("source_id") and b.get("quote") == a.get("quote"), (
                f"{term}: a citation changed: {b.get('source_id')}"
            )

        artifacts.draft.write_text(
            json.dumps(draft, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        artifacts.wikitext.write_text(wikitext, encoding="utf-8")

        model = json.loads(artifacts.model.read_text(encoding="utf-8"))
        model.setdefault("fix_passes", []).append(
            {
                "applied_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "by": "claude-fable-5 (Claude Code, local session)",
                "reason": "cross-model audit findings, gemini-3.5-flash auditing the "
                          "claude-sonnet-5 draft; plus lead term-duplication cleanup",
                "edits": applied,
                "citations_unchanged": True,
            }
        )
        artifacts.model.write_text(
            json.dumps(model, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        print(f"{term}: {applied} edits applied, {len(after)} citations unchanged, re-rendered")


if __name__ == "__main__":
    main()
