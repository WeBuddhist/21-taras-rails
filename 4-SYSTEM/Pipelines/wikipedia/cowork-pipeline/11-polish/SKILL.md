---
name: 11-polish
description: "Pipeline step 11 — Gemini rewrite. Sends draft-claude.md through scripts/gemini_polish.py for a literary Tibetan rewrite that preserves claim IDs and locked glossary terms, writing draft-gemini.md. Use whenever the user says 'polish the draft', 'Gemini rewrite', 'literary pass', or when draft-claude.md exists and draft-gemini.md does not."
---

# Step 11 — Gemini rewrite

Literary Tibetan rewrite of the Claude draft, preserving claim IDs and locked glossary terms. Gemini is a stylist, not an editor.

## Inputs
- `concepts/{{CONCEPT}}/draft-claude.md`
- The handoff prompt below + locked glossary `{{GLOSSARY}}`

## Outputs
- `concepts/{{CONCEPT}}/draft-gemini.md`

## Script
**`scripts/gemini_polish.py`** — sends the draft + handoff prompt + glossary to the Gemini API and writes the result back. **Pin and log the model version with each run** so the step 13 feedback loop can distinguish prompt problems from model-version drift.

## Invariants
- Every `[Cnn]` marker stays attached to the same statement.
- Glossary terms verbatim, never paraphrased.
- No factual change: no added facts, no dropped qualifiers, attributions stay explicit — an attributed position must never be absorbed into the neutral voice.
- No reordering of sections; no merging sentences across different claim IDs.
- If a sentence can't be improved without violating a constraint, it stays unchanged.

## Canonical prompt (sent to Gemini)

```
Rewrite the following draft in fluent literary Tibetan suitable for an
encyclopedia. Hard constraints:
1. Keep every claim ID marker [Cnn] attached to the same statement it marks
   now.
2. These technical terms must appear verbatim, never paraphrased: {{GLOSSARY}}.
3. Change no factual content: add no facts, drop no qualifiers, and keep every
   attribution ("X holds that…") explicit — never absorb an attributed
   position into the neutral voice.
4. Do not reorder sections or merge sentences across different claim IDs.
You are a stylist, not an editor. If a sentence cannot be improved without
violating a constraint, leave it unchanged.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here (and into the copy `gemini_polish.py` sends).
