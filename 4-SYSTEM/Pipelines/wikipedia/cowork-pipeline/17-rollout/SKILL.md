---
name: 17-rollout
description: "Pipeline step 17 — Paced rollout. Manages small-batch publication cadence, the on-wiki method-disclosure project page, and routing community reaction back into the step 13 feedback loop. Use whenever the user says 'rollout', 'how many articles this batch', 'community feedback', or after any article publishes via step 16."
---

# Step 17 — Paced rollout

First articles go out in small batches; the method is disclosed on a project page; community reaction is absorbed before scaling volume.

## Inputs
- Published articles (step 16)
- On-wiki reactions: talk pages, edits to published articles, project-page discussion

## Outputs
- Batch plan (what publishes next, and how many)
- Maintained project page disclosing the method
- Community feedback routed into `pipeline/feedback.md` **alongside audit findings, feeding step 13**

## Script
None.

## Procedure
1. Keep batch sizes small until community reaction to prior batches has been read and absorbed.
2. Maintain the on-wiki project page describing the method — disclosure precedes scale.
3. Collect on-wiki feedback (reverts, talk-page critique, editor corrections) and classify it through the step 13 loop like audit findings: name the causal stage, propose the prompt patch.
4. Only scale volume once feedback per batch stabilizes.

## Invariants
- No volume scaling before community reaction to prior batches is absorbed.
- On-wiki feedback is first-class feedback-loop input, not a side channel.

## Prompt maintenance
This step has no canonical prompt. Behavior patches land in the pipeline document first, then sync here.
