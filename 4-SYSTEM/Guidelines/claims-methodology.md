# Claims methodology — extraction and consolidation

**Purpose of this document:** the full record of the claims-gathering methodology decided for
this vault, written so that any future session — including one on a different account with no
conversation history — can pick up the work without re-deriving the reasoning. Decisions here
were made 2026-08-02 through 2026-08-05 by the human contributor in discussion with the agent.

The goal: gather **every fact/claim** the Tārā-21 commentaries make, per commentary and then
consolidated, with the citation chain intact at every step — and do it in a way that scales to
other Tibetan Buddhist corpora (e.g. Bodhicaryāvatāra and its much larger commentaries).

---

## 1. The core principle: extract first, merge later

Extraction and consolidation are **separate phases**, never interleaved:

- **Extraction** reads one commentary in isolation and records what *it* says — expensive,
  careful, done once per commentary, redoable per commentary.
- **Consolidation** compares finished claims files — cheap, disposable, redoable at any time
  without re-reading a single commentary.

Merge decisions made *during* reading are made with incomplete information: the first
commentary read silently defines the topic space, and later commentaries with different
granularity (a 24 KB བསྡུས་འགྲེལ vs a 400 KB treatise) map onto it badly. Extraction errors and
merge errors contaminate each other and neither can be redone alone. This is why two
considered-and-rejected alternatives (see §5) were rejected.

Meaning-based segmentation of the source (`commentary-resegment`) improves citation quality
and within-commentary consistency, and is part of the pipeline — but it does **not** fix the
cross-commentary granularity problem, which is about the topic space, not the text units.

---

## 2. The pipeline

```
per commentary (isolation):
  1. clean + frontmatter + resegment          (raw-to-sources, commentary-resegment)
  2. TOC tree                                 (toc-tree-extraction, 4-pass, QC-gated)
     → 2-RAILS/Sections/Raw/toc-tree/<id>.md
  3. tree-guided claims extraction            (tree-guided-claims, per-node subagents)
     → 2-RAILS/Claims/raw/tree-guided/<id>.md

corpus-wide (after all extractions):
  4. bucket claims by spine + facet           (mechanical script — no judgment)
  5. question-driven consolidation per bucket (one subagent per topic)
     → 2-RAILS/Claims/<topic>.md
  6. generated indexes                        (matrix, tags, graph — from topic pages)
```

Steps 4 and 6 are deterministic scripts; only steps 3 and 5 use model judgment, always on a
small, local input.

### Why the spine matters

All commentaries on one root text share its canonical structure (for Tārā-21: 21 homages +
benefits). So topic alignment is two cheap stages — slot each claim to its verse/Tārā (nearly
free: the tree-guided extraction already records the TOC node), then compare a handful of
claims semantically *within* a bucket — never one expensive global matching over thousands of
claims.

---

## 3. Extraction — three methods, kept separate

All three write under `2-RAILS/Claims/raw/`, one file per commentary, and are **genuinely
different techniques being compared**, not revisions of one another:

| Method | Skill | Output | Character |
|---|---|---|---|
| Direct, fixed categories | `commentary-claims` | `raw/<id>.md` | One pass, nine fixed categories (A–I) |
| TOC-scaffolded | `toc-scaffolded-claims` | `raw/toc-scaffolded/<id>.md` | Existing extraction re-bucketed under the tree |
| Tree-guided | `tree-guided-claims` | `raw/tree-guided/<id>.md` | Fresh extraction, one isolated subagent per TOC node |

**Tree-guided is the preferred method going forward** — claims inherit their spine location
for free, which makes consolidation bucketing nearly automatic. Requires a QC-clean TOC tree
first.

Historical note: a model-comparison experiment (same skill, two models — "opus" and "sonnet"
runs over karma-maitri, lobsang-dawa, gendun-gyatso) found claim counts differing 5–12 per
commentary purely from granularity choices, while ⚑ internal-tension findings matched exactly.
Lesson baked into §4: consolidation must match claims by *content*, never expect one-to-one
claim alignment between extraction runs. Those runs are archived under the Wikipedia pipeline
folder (see `vault-annex.md`); the finding is what matters.

---

## 4. Consolidation — question-driven, per topic

### Where files go

- **`2-RAILS/Claims/raw/…`** — all per-commentary extractions (input layer, never modified by
  consolidation).
- **`2-RAILS/Claims/<topic>.md`** — one consolidated page per topic (output layer).

This mirrors the `Sections/` pattern (`Raw/` = per-commentary, top level = combined) — one
rule for the whole vault.

### How the questions are produced — generated, not authored

No human writes the question list. Two free sources:

1. **From the spine, mechanically:** 21 Tārās × observed facets (name/etymology, colour,
   implements, stance, activity, mantra, benefit) plus global topics ≈ a scripted question
   grid.
2. **From the extractions themselves:** every raw claim implies a question — one commentary's
   "the left hand's three fingers symbolise the Three Jewels" becomes "what does each
   commentary say the left hand symbolises?", asked of all the others.

The union of both is the question set. This makes question-driven consolidation a **derived
completeness check**: free extraction first, then generated questions catch what free reading
missed.

### What each topic page contains

Per facet: **Consensus** (with per-commentary attestations), **⚑ Divergences** (never
flattened — vault hard rule), **Unique** (claims only one commentator makes). Plus a coverage
table including which commentaries are *silent* on the topic — absence is a finding.

### Questions are recorded in the page itself

Frontmatter `consolidation_questions:` (machine-queryable) **and** a visible
`## Questions asked` section. A question that found no answers is kept and marked "no
commentary addresses this" rather than deleted. Template:
`4-SYSTEM/Templates/consolidated-claims-topic.md`.

### Invariants

1. Topic pages cite **raw claim IDs**, never source files — the chain is
   topic page → raw claim → source segment.
2. Each consolidated answer lives in **exactly one** file; indexes point, never duplicate.
3. File names come from **spine + topic**, never claim content — stable across re-runs.
4. Consolidation is disposable: regenerating any topic page never touches `raw/`.

### Scaling rule (for BCA and other large corpora)

> Folders follow the text's spine; files sit at the level where a page stays readable;
> anything finer becomes headings inside the file.

Tārā-21: ~21 per-Tārā pages + a handful of global pages, facets as headings. BCA: one folder
per chapter, one file per topic/term or verse-group. The split trigger is mechanical: when a
topic page would exceed ~40–50 claims or a few hundred lines, split one spine level down.
Never decide file granularity per-text by taste.

---

## 5. Alternatives considered and rejected (and why)

Recorded so they are not re-proposed from scratch:

- **File-per-claim, merged during reading** ("see a claim → check if a file exists → append
  or create"): granularity decided blind, first-commentary bias, sequential (no parallelism),
  extraction and merge errors entangled, thousands of unstable stub files.
- **Tags-as-method** (tag claims inline while reading, index the tags, graph at the end):
  flat namespace with no citation payload; tag drift (`#tara-swift` vs `#myurma`) recreates
  the matching problem with less structure; requires annotating inside `1-SOURCES/`, which is
  frozen. Tags/wikilinks are valuable **as generated output** from finished topic pages — not
  as the method.
- **Pairwise/tournament merge** (merge 1+2, then +3 …): order-dependent, early merges shape
  everything, drifts by the tenth commentary.
- **Embedding clustering:** right tool when a corpus has *no* shared spine; unnecessary here,
  and clusters still need human cleanup.
- **Knowledge-graph triples:** machine-queryable but destroys verbatim-Tibetan fidelity — the
  thing the whole citation chain protects. Actively skipped.
- **Question-driven as the *only* extraction:** finds only what was asked; unique/unexpected
  claims get missed. Kept as the consolidation mechanism and second-pass completeness check,
  not the primary extraction.
- **No consolidation (RAG-style, query-time merge):** cheap and always current, but no
  browsable artifact and no persistent divergence record. Available "for free" over the claim
  files anyway; not a substitute for topic pages.

---

## 6. Related layout decisions

- **TOC trees** live at `2-RAILS/Sections/Raw/toc-tree/<registered-id>.md` (decision
  2026-08-05; previously a top-level `2-RAILS/TOC-Trees/`). Rationale: the tree is raw
  distilled structure — per-commentary, descriptive, every title attestation-checked — so it
  belongs with the other per-commentary distillations under `Sections/Raw/`. All skills,
  commands, and docs were repointed; the QC gate and promotion flow are unchanged.
- **Claims layout** (decision 2026-08-05): per-commentary extractions moved under
  `Claims/raw/`; `Claims/` top level reserved for consolidated topic pages. References in
  `commentary-claims`, `tree-guided-claims`, `toc-scaffolded-claims`, `SKILLS-CATALOG`,
  `/extract-claims`, `About Rails` §6b, and `CLAUDE.md` §2/§7 all updated.

---

## 7. Status snapshot (2026-08-05)

- Ingest chain + TOC tree + tree-guided claims complete for **karma-maitri** only
  (`Claims/raw/tree-guided/karma-maitri.md`, tree at `Sections/Raw/toc-tree/karma-maitri.md`,
  `status: complete`).
- Remaining 15 commentaries: raw texts in `0-INBOX/raw-data/སྒྲོལ་མ་ཉེར་གཅིག/`, awaiting
  `/ingest` + `/extract-claims`. Two raw texts there (Gendun Drub, Ngulchu Dharmabhadra) have
  never been registered as sources at all.
- Consolidation (steps 4–6 of §2): **not started** — deliberately blocked until extraction
  covers enough of the corpus. No bucketing script or consolidation skill exists yet; when
  built, the consolidation skill should follow this document and the template.

## 8. Where everything lives

| Thing | Path |
|---|---|
| This methodology | `4-SYSTEM/Guidelines/claims-methodology.md` |
| Topic-page template | `4-SYSTEM/Templates/consolidated-claims-topic.md` |
| Canonical Claims rules | `2-RAILS/About Rails.md` §6b (wins over CLAUDE.md on conflict) |
| Ingest chain | `.claude/commands/ingest.md` |
| Claims extraction command | `.claude/commands/extract-claims.md` |
| TOC trees | `2-RAILS/Sections/Raw/toc-tree/<registered-id>.md` |
| Raw claims | `2-RAILS/Claims/raw/{,toc-scaffolded/,tree-guided/}<registered-id>.md` |
| Consolidated topic pages | `2-RAILS/Claims/<topic>.md` |
