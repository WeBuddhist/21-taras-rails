---
name: 05-wikidata-concepts
description: "Pipeline step 5 — Wikidata match for concepts. Searches Wikidata for an existing item for a selected concept (Tibetan, Wylie, Sanskrit, English renderings) and records the QID in the concept note. Requires web access. Use whenever the user says 'check Wikidata for this concept', 'find the QID', or after a concept is shortlisted in step 4 and its concept note has no QID yet."
---

# Step 5 — Wikidata match (concepts)

For each selected concept, find (or note the absence of) a Wikidata item. Existing items show how en/zh/de articles structured the topic and confirm the concept isn't already covered under a variant name.

## Inputs
- Concept + all variant forms (from the step 3/4 tables)
- Web access

## Outputs
- QID written into the concept note's frontmatter (empty `wikidata: ""` if none exists — the item is created at step 16)
- Sitelink list and a 5-line structure summary of the largest existing article, when found

## Script
None (interactive web search; item *creation* happens later via `publish.py` at step 16).

## Invariants
- **Multiple candidates: never pick silently** — list them with distinguishing statements.
- None found: record `wikidata: ""` and note the closest related items (broader concept, school, root text).

## Canonical prompt

```
For concept {{CONCEPT}} (variants: {{VARIANTS}}), search Wikidata for an
existing item — try Tibetan, Wylie, Sanskrit, and English renderings.
- Found: write the QID into the concept note's frontmatter, list its sitelinks
  (en/zh/de/… articles), and summarize in 5 lines how the largest existing
  article structures the topic.
- Multiple candidates: list them with distinguishing statements; never pick
  silently.
- None: record wikidata: "" and note the closest related items (broader
  concept, school, root text).
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
