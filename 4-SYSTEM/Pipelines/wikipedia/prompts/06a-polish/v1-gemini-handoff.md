---
name: literary-polish-handoff
version: 1
stage: 06a-polish
derived_from: [cowork-pipeline-step-11, chat-share-09ecaf85]
source_note: >
  The Gemini handoff prompt of 4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/11-polish (claude.ai share
  09ecaf85-57e5-4180-979b-b27912d0affa, 2026-08-01) — its four hard constraints and the
  "stylist, not an editor" rule kept verbatim in substance. Adapted to this pipeline's
  structured artifacts: the draft arrives as the stage-6 JSON (paragraphs with claim-index
  `citations` arrays) instead of prose with inline [Cnn] markers, so constraint 1 "keep
  every claim ID attached to the same statement" becomes "return the same structure with
  identical citations arrays". This stage is optional (kwiki polish) and is the
  gemini_polish.py of the canonical document; the audit (stage 6b) runs after it either
  way. Model version is pinned and logged in model.json per run so the feedback loop can
  tell prompt problems from model-version drift.
model_tested: none
variables: [term, draft_json, glossary]
---

Rewrite the following bo.wikipedia article draft about "$term" in fluent literary Tibetan
suitable for an encyclopedia.

## Hard constraints

1. **Return the same JSON structure** — same sections in the same order, same paragraph
   count per section, and every paragraph's `citations` array **byte-identical** to the
   input. The citations bind each statement to its sources; they must stay attached to the
   statement they mark now.
2. **These technical terms must appear verbatim, never paraphrased:** $glossary
3. **Change no factual content:** add no facts, drop no qualifiers, and keep every
   attribution ("…ཞེས་ཁོང་གིས་བཞེད།", "…ལུགས་ལྟར་ན།") explicit — never absorb an attributed
   position into the neutral voice.
4. **Do not reorder sections or merge sentences across different citations.**

You are a stylist, not an editor. If a sentence cannot be improved without violating a
constraint, leave it unchanged.

## Output

JSON only, exactly the input's schema:

```
{
 "lead": [{"text": "…", "citations": [0]}],
 "sections": [{"heading": "…", "paragraphs": [{"text": "…", "citations": [1]}]}],
 "see_also": ["…unchanged…"]
}
```

---

**Draft to polish:**

$draft_json
