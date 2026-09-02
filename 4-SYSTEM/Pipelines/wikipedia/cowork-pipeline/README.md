# Pipeline skills — Tibetan Buddhist texts → Wikipedia

One Cowork skill per pipeline step. Drop this folder into the vault as `/vault/skills/`; each step can then be invoked by name, re-run in isolation, and patched independently via the step 13 feedback loop (patches land in the pipeline document's canonical prompts first, then sync to the skill).

| Skill | Step | Output | Script |
|---|---|---|---|
| 01-ingest | Ingest & provenance | `texts/<id>.md` | `bdrc_fetch.py` |
| 02-alignment | Verse alignment & stable IDs | `alignment/<id>.md` | — |
| 03-keywords | TF-IDF variant clustering | cluster table | — |
| 04-concept-selection | Rank by distinctiveness × breadth | shortlist | — |
| 05-wikidata-concepts | Concept QID lookup | QID in concept note | — |
| 06-passages | Passage gathering | `passages.md` (immutable) | — |
| 07-outliers | Divergence classification | `outliers.md` | — |
| 08-claims | Atomic claims table | `claims.md` (immutable) | — |
| 09-outline | Claims-only outline | `outline.md` | — |
| 10-draft | Claude draft, claims-only | `draft-claude.md` | — |
| 11-polish | Gemini literary rewrite | `draft-gemini.md` | `gemini_polish.py` |
| 12-audit | Sentence-level audit | `audit.md` + verdict | — |
| 13-feedback | Causal-stage patching | `pipeline/feedback.md` | — |
| 14-source-publication | Wikisource / BDRC-link routing | `source_url` backfilled | `publish.py` |
| 15-wikidata-sync | Work & author items | `wikidata_*` backfilled | `publish.py` |
| 16-wikipedia | Pre-pub review gate + publish | live article + concept QID | `publish.py` |
| 17-rollout | Paced batches, community loop | batch plan, project page | — |

Load-bearing invariants (enforced across skills):
1. Nothing downstream touches source wording after the claims stage — `claims.md` is the only drafting input; `passages.md` stays closed from step 9 on.
2. Nothing publishes without surviving the step 12 audit and the pre-publication review (canonical copy in `16-wikipedia`, gating 14–16).
