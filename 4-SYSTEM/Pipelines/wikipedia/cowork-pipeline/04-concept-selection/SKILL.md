---
name: 04-concept-selection
description: "Pipeline step 4 — Concept selection. Ranks candidate concepts by TF-IDF distinctiveness × breadth (independent commentators/schools), with an exception lane for famous single-commentator controversies. Use whenever the user says 'rank the concepts', 'which concepts get articles', 'shortlist', or hands over the cluster table from step 3."
---

# Step 4 — Concept selection

Rank candidates by **TF-IDF distinctiveness × breadth** (number of independent commentators/schools treating the concept). Breadth doubles as the due-weight and notability signal.

## Inputs
- `{{CLUSTER_TABLE}}` from step 3, with TF-IDF scores

## Outputs
- Ranked shortlist with one-line justifications
- Deferred list with reasons
- Flags on concepts whose coverage comes overwhelmingly from one school (their articles need extra attribution care)

## Script
None.

## Invariants
- **Exception lane:** a concept treated by only one commentator still qualifies if it (a) drew significant response/refutation literature, or (b) defines a school's position. This catches the famous controversies — often the most encyclopedically valuable articles.
- Breadth measures the existence of a topic (concept level); reception measures the weight of a position (claim level, step 8).

## Canonical prompt

```
For each candidate concept in {{CLUSTER_TABLE}}, score:
1. Distinctiveness (TF-IDF, given).
2. Breadth: how many independent commentators treat it, from how many schools —
   list them by name.
3. Exception lane: if breadth is low, check whether the concept (a) drew
   response/refutation literature or (b) defines a school's position. Either
   qualifies it despite low breadth.
Output a ranked shortlist with one-line justifications, and a deferred list
with reasons. Flag any concept whose coverage comes overwhelmingly from one
school — its article will need extra attribution care.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
