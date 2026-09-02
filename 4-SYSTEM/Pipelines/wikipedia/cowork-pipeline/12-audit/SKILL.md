---
name: 12-audit
description: "Pipeline step 12 — Claude audit. Checks draft-gemini.md sentence by sentence against claims.md for added facts, dropped qualifiers, terminology drift, and softened attributions, ending with a publish/fix/return verdict. Use whenever the user says 'audit the draft', 'verify the rewrite', or when draft-gemini.md exists and audit.md does not. Nothing is published without surviving this audit."
---

# Step 12 — Claude audit

Sentence-by-sentence check of the Gemini text against the claims table. This is load-bearing invariant 2: **nothing is published that hasn't survived the audit.**

## Inputs
- `concepts/{{CONCEPT}}/draft-gemini.md`
- `concepts/{{CONCEPT}}/claims.md`

## Outputs
- `concepts/{{CONCEPT}}/audit.md` — one row per finding, ending with a verdict: publish / fix listed items / return to drafting

## Script
None.

## Invariants
- A school-position silently promoted to Wikipedia's voice is an **audit failure**.
- **Added facts and attribution loss are blocking**: the article cannot publish until fixed.
- The audit compares against `claims.md`, never against `passages.md` — the claims table is the standard of truth downstream.

## Canonical prompt

```
Compare draft-gemini.md sentence by sentence against claims.md. Output
audit.md, one row per finding:
sentence (quoted) | claim ID(s) | finding | severity.
Findings to detect: added fact (no claim ID covers it) · dropped or weakened
qualifier · terminology drift (glossary term paraphrased) · attribution
softened or dropped · claim ID attached to the wrong statement · meaning shift
in the rewrite.
Added facts and attribution loss are blocking: the article cannot publish
until fixed. End with a verdict: publish / fix listed items / return to
drafting.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
