---
name: 15-wikidata-sync
description: "Pipeline step 15 — Wikidata sync for texts & authors. Matches or creates Wikidata items for every cited work and its author directly from vault frontmatter (PD and copyrighted alike), backfilling QIDs into wikidata_work / wikidata_author. Use whenever the user says 'sync Wikidata', 'create the work items', or when cited texts have empty wikidata_* fields after step 14."
---

# Step 15 — Wikidata sync (texts & authors)

For each cited source text — **PD and copyrighted alike** (metadata is facts; only republishing full text is restricted) — match or create Wikidata items for the **work** and its **author**, so every Wikipedia ref is backed by a structured, queryable record.

## Inputs
- Text note frontmatter (`texts/*.md`) — the sole source of statements
- `source_url` values written by step 14

## Outputs
- Wikidata items (work + author) with: instance of (literary work / religious text), title (Tibetan + Wylie as aliases), author, language of work, the BDRC resource ID property, and edition information
- PD works: their Wikisource page linked to the item; copyrighted works: anchored through the BDRC ID
- QIDs written back into `wikidata_work` / `wikidata_author` in the vault frontmatter

## Script
**`scripts/publish.py`** — Wikidata API for item creation/updates; QIDs written back into frontmatter automatically after each successful call.

## Gate
Part of the publication layer: the pre-publication review (canonical in `skills/16-wikipedia/SKILL.md`) gates steps 14–16 and must return **publish** before `publish.py` runs. (Its check 4 verifies this step is complete before the article publishes at step 16.)

## Invariants
- Statements come from frontmatter only — never from model memory (same rule as step 1).
- Sync copyrighted works too: metadata is facts.
- Frontmatter stays the single source of truth; QIDs are backfilled, never tracked elsewhere.

## Prompt maintenance
This step has no canonical drafting prompt. Behavior patches land in the pipeline document first, then sync here.
