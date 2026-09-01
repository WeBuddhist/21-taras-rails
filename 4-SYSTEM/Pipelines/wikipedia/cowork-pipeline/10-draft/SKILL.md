---
name: 10-draft
description: "Pipeline step 10 — Claude draft. Writes the Tibetan article draft from outline.md + claims.md only, with inline claim IDs on every factual sentence and voice rules by claim type. Use whenever the user says 'draft the article', 'write <concept>', or when outline.md exists and draft-claude.md does not. passages.md must stay closed throughout."
---

# Step 10 — Claude draft

Draft the article from claims only — passages closed — with claim IDs inline.

## Inputs
- `concepts/{{CONCEPT}}/outline.md` and `claims.md` — and nothing else
- Locked glossary `{{GLOSSARY}}`

## Outputs
- `concepts/{{CONCEPT}}/draft-claude.md`

## Script
None.

## Invariants
- **`passages.md` stays closed — the drafter must never see source wording** (load-bearing invariant 1).
- Every factual sentence ends with its claim ID(s); a sentence without IDs must contain no factual assertion. If it has no claim ID, it does not exist.
- **Voice by claim type: consensus claims may sit in Wikipedia's voice; everything below consensus gets mandatory in-text attribution** ("Mipham holds that…", "in the Gelug presentation…"). An outlier must never appear unattributed.
- Glossary terms verbatim; correctness and attribution over style (style is step 11's job).

## Canonical prompt

```
Write the article draft in Tibetan in draft-claude.md, using ONLY outline.md
and claims.md. passages.md stays closed — you must never see source wording
while drafting.
- Every factual sentence ends with its claim ID(s): [C12][C31]. A sentence
  without IDs must contain no factual assertion.
- Voice by claim type: consensus → Wikipedia's voice; everything below
  consensus → in-text attribution naming the commentator or school.
- Glossary terms verbatim: {{GLOSSARY}}. Define technical terms on first use
  for a non-specialist reader.
- Lead: summarizes the body, defines the concept in the first sentence,
  contains nothing not in the body.
- Add no fact, date, or example from your own knowledge — if it has no claim
  ID, it does not exist.
Style is polished later; correctness and attribution are your only priorities.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
