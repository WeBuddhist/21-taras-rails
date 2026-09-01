---
name: 13-feedback
description: "Pipeline step 13 — Feedback loop. Classifies each audit finding (and on-wiki feedback from step 17) by the stage that caused it and proposes a one-line patch to that stage's prompt, appended to pipeline/feedback.md. Use whenever the user says 'run feedback', 'patch the prompts', 'why did this drift', or after any audit.md is finalized and before the next article starts."
---

# Step 13 — Feedback step

Classify each audit finding by causal stage and patch that stage's prompt before the next article. The immutable per-stage outputs (`passages.md`, `claims.md`, drafts) make the drift diffable to its origin.

## Inputs
- `concepts/{{CONCEPT}}/audit.md`
- On-wiki community feedback routed in from step 17

## Outputs
- Appended rows in `pipeline/feedback.md`: finding | causal stage | proposed one-line patch to that stage's prompt
- Applied patches: **patch the pipeline document's canonical prompt first, then sync to the corresponding skill's SKILL.md** — this per-step packaging is why fixes land exactly where the drift originated and nowhere else

## Script
None.

## Invariants
- Four causal stages only: extraction (passage missed or mistagged) · claims (claim wrong, mistyped, or badly worded) · draft (Claude introduced it) · rewrite (Gemini introduced it).
- Findings recurring across articles get priority patches.
- When the causal stage is the rewrite, check the logged Gemini model version before blaming the prompt — the pin/log from step 11 exists to distinguish prompt problems from model-version drift.

## Canonical prompt

```
For each finding in audit.md, name the stage that caused it: extraction
(passage missed or mistagged) · claims (claim wrong, mistyped, or badly
worded) · draft (Claude introduced it) · rewrite (Gemini introduced it).
Append to pipeline/feedback.md:
finding | causal stage | proposed one-line patch to that stage's prompt.
Findings recurring across articles get priority patches.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Patches proposed here land in the document first, then sync to the target skill.
