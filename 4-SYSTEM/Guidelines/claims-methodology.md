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
  4. spine map, per commentary                  (spine-map, one isolated subagent each)
     → 2-RAILS/Claims/raw/spine-map/<id>.md     — built ONCE, reused by every topic
  4b. packet assembly, per topic                 (assemble_packet.py — deterministic)
     → 0-INBOX/temp/packet-<slot>.md            + manifest for the coverage check
  5. question-driven consolidation per bucket   (one subagent per topic)
     → 2-RAILS/Claims/<topic>.md
  5b. coverage check + gap closure               (deterministic diff + small repair pass)
  5c. verification gates                         (gate 1: verify_consolidation.py script;
                                                  gate 2: claims-consolidation-audit,
                                                  fresh adversarial agent per page)
  6. generated indexes                           (matrix, tags, graph — from topic pages)
```

Only step 6 is a fully deterministic script with no model judgment. Step 4 was originally
designed as one too ("bucket claims by spine + facet — mechanical script, no judgment") but a
pilot run (2026-08-07, `claims-consolidation` skill, 16 commentaries × 3 topics) found this
assumption wrong — see "Bucketing is not mechanical" below. Steps 3, 4, and 5 all use model
judgment, always on a small, local input (one commentary, or one topic's assembled packet).
5b's diff itself is deterministic; only the gap-closing repair pass (when a gap is found) uses
judgment, and only on the specific claims the diff flagged.

### Why the spine matters

All commentaries on one root text share its canonical structure (for Tārā-21: 21 homages +
benefits). So topic alignment is two stages — slot each claim to its verse/Tārā (via the
per-commentary mapping pass, step 4 — see below for why this needs a real read, not a lookup),
then compare a handful of claims semantically *within* a bucket — never one expensive global
matching over thousands of claims.

### The mapping is per-commentary, not per-topic (revision of 2026-08-08)

The pilot's step 4 ran its mapping pass **inside every topic run**: for each topic, one
isolated subagent per commentary re-read that commentary's whole raw claims file to find the
topic's claims. That is correct but quadratic in the wrong variable. The corpus is 16
commentaries / 2,975 claims / ~3.8 MB of raw claims files (80 KB–604 KB each), and a full run
is ~22 spine slots plus global topics — so the pilot design implied **roughly 400 full-file
reads, ~25× re-reading of the same unchanged corpus**, at full price each time because the
isolation guard means fresh contexts with no cache reuse.

The observation that fixes it: **resolving one commentary's numbering against the spine
answers it for every slot at once.** "Which node of `karma-maitri` is Tārā 5" and "…is Tārā 12"
are the same act of reading its TOC tree. Split out, that judgment is made 16 times total
instead of ~400.

So the mapping moved upstream into its own artifact — `2-RAILS/Claims/raw/spine-map/<id>.md`,
written by the `spine-map` skill — and packet assembly became a deterministic script,
`4-SYSTEM/Skills/claims-consolidation/assemble_packet.py`. Consolidation itself is unchanged:
it still works from a packet, still generates questions from it, still never re-opens a raw
file.

What this buys beyond tokens:

- **Verbatim quoting by construction.** The assembler *copies* claim blocks out of the raw
  files. Several minor findings of the 2026-08-07 audit (silently elided syllables,
  normalized orthography) were a model retyping Tibetan; a script cannot.
- **A deterministic coverage input.** The packet's `## Manifest` is exactly the "claim IDs
  the mapping pass placed in this topic's bucket" that step 5b diffs against — now computed,
  not model-reported.
- **Loud failure instead of silent omission.** A commentary with claims but no spine map, or
  with no disposition for a slot, exits the assembler non-zero. Under the pilot design a
  commentary quietly missing from one topic's fan-out left no trace.
- **Reusability downstream.** `2-RAILS/Verses/` needs the same root-verse → commentary-passage
  routing; it can read the spine maps instead of re-deriving them.

The judgment that was in step 4 did not become cheaper or more mechanical — it moved. Rule 2
of `spine-map` is the old Rule 1, and the isolation requirement (one agent per commentary,
never several at once) moved with it, for the same anti-contamination reason. What follows
immediately below — why that judgment cannot be a script — is still the governing finding.

### Bucketing is not mechanical — it needs a per-commentary mapping pass

This corrects the pipeline diagram's original step 4 ("mechanical script — no judgment") and
the claim above that slotting is "nearly free" from the TOC node alone. The pilot run found
that **TOC node numbering for "which spine slot is this" is not uniform across commentaries**:
one commentary nests a Tārā's content at node `1.1.N`, another at top-level node `N`, another
groups several sub-facets per Tārā under one node, another titles nodes by the Tārā's epithet
name instead of an ordinal, and structures otherwise merge or split relative to the canonical
spine. A fixed formula (e.g. "node `1.1.N` is always Tārā N") silently mis-buckets claims the
moment it hits a commentary organized differently — and several of this vault's sixteen do.

The fix, validated in the pilot: **one isolated subagent per commentary**, reading that
commentary's own TOC tree, its raw claims file, and (for texts with a verse-numbered spine)
the relevant root-text passage as ground truth — never a script applying one node-numbering
rule to every commentary. This subagent also resolves the corpus-wide **completeness
guarantee** the rest of §4 already promises: it must place every claim into the topic bucket,
an explicit `ambiguous` list (uncertain fit, with a reason — never silently dropped, never
silently force-fit), or leave it out as genuinely irrelevant; and it must explicitly mark a
commentary silent on a slot rather than leaving it merely empty.

Since 2026-08-08 this subagent is the `spine-map` skill and its output is the routing index
(node numbers, claim IDs, slot names — addresses, never claim content), written once per
commentary. The claim *content* the consolidation pass needs is copied out of the raw files
verbatim at packet time by `assemble_packet.py`, so step 5 still never re-opens a raw claims
file. The completeness guarantee is now mechanically enforced rather than merely required:
`verify_spine_map.py` fails any map in which a claim has zero dispositions (silent loss) or
two (silent duplication).

A finding from the first corpus-wide run, worth stating because it is the general case rather
than the exception: **the sa-bcad is sometimes coarser than the spine.** `tsultrim-namdak`
carries all twenty-one homages inside a single undivided node (`2.1.2.1`, 75 claims), so no
node-level rule can route it at all. Its spine map routes those slots by claim-ID range
instead, using the extraction's own root-verse quotation claims ("Verse N quoted: …") as the
boundary markers. Any spine-mapping method that assumes one node per slot will silently
mis-route commentaries of this shape.

### The coverage invariant (step 5b) — closing the loop the pipeline only aspired to before

§4's original design already treats question generation as a "derived completeness check" —
free extraction first, generated questions catch what free reading missed. The pilot added the
mechanism that actually *enforces* this instead of leaving it aspirational: after step 5
writes a topic page, **mechanically diff** every claim ID step 4 placed in that topic's main
bucket against every claim ID the topic page actually cites. Any claim in the gap must be
closed — folded into the page, or logged with a one-line reason in an explicit "Claims
reviewed, not separately cited" section — never left silently absent. In the pilot this caught
real, specific, fixable gaps (roughly 5–12% of a topic's mapped claims per page, mostly
non-substantive structural/duplicate claims once reviewed, but not always — e.g. one
commentary's parallel mantra-syllable benefit glosses were found missing and folded in on
review). The diff itself is a deterministic set comparison, not a model judgment call; only
the repair pass over the flagged gap uses judgment, and only on the specific claims flagged —
never a full re-read of the topic. See `4-SYSTEM/Skills/claims-consolidation/SKILL.md` for the
full procedure, including this check as a mandatory (not optional) step.

### The verification gates (step 5c) — what a retrospective audit of the pilot proved necessary

On 2026-08-07 the three pilot pages were adversarially audited — a fresh agent per page
re-checking every one of 418 unique citations against the raw claims files. Result: zero
fabricated claim IDs, but **one critical finding** (a "corroboration" cited to a claim that
contains nothing of the sort — the consolidator had a real corpus idea attached to the wrong
claim ID), one moderate overstretch, and ~16 minor findings falling into a stable taxonomy:
partial-support padding of consensus attestation lists, the same claim cited on both sides of
one divergence, page-level harmonizations presented as a claim's own reading, epistemic
upgrades ("endorses" for a tentative སྙམ་མོ aside), silently elided syllables in Tibetan
quotes, hand-tallied "(N commentaries)" labels (five of five wrong on the worst page), and
consulted claims left with no disposition anywhere.

Consolidation therefore now ends with two mandatory gates, encoded in the skill:

- **Gate 1 — deterministic** (`4-SYSTEM/Skills/claims-consolidation/verify_consolidation.py`):
  citation existence (both heading and ⚑ bold-block claim forms), recomputed count labels,
  both-sides-of-a-divergence flags, disposition completeness against the Coverage table,
  prefix discipline. Zero ERRORs required. Validated by reproducing every mechanical finding
  of the human audit, plus one it missed.
- **Gate 2 — adversarial attribution audit** (`claims-consolidation-audit` skill): a fresh
  agent that did not write the page checks every attribution against the raw claims —
  attribution fidelity, verbatim quote fidelity, divergence reality, epistemic strength.
  Report-only; the consolidator fixes, the auditor re-checks. No critical/moderate finding
  may remain.

The corresponding prevention rules (full-statement support, re-read-before-corroborating,
one side per divergence, verbatim-or-ellipsis quoting, harmonization attributed to the page,
computed counts, no undispositioned claims) are Rules 9–16 of the consolidation skill.

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

## 7a. Status snapshot (2026-08-08) — spine-map layer added

- **`spine-map` skill registered and validated.** `4-SYSTEM/Skills/spine-map/SKILL.md`,
  its deterministic gate `verify_spine_map.py`, the template
  `4-SYSTEM/Templates/spine-map.md`, and the `/spine-map` command all exist. The
  assembler `4-SYSTEM/Skills/claims-consolidation/assemble_packet.py` is written and
  tested end-to-end (packet claim blocks confirmed byte-identical to their raw source).
- ⚑ **Only 1 of 16 spine maps exists** — `karma-maitri`, written as the validation case.
  The other fifteen must be built before any topic can be consolidated; `assemble_packet.py`
  exits non-zero and names them until they are. Run `/spine-map <registered-id>` per
  commentary, one isolated agent each (never several at once — Rule 2).
- **Canonical slot registry created** at `Guidelines/vault-annex.md` §2a: `tara-01`…`tara-21`
  + `benefits` (spine-proper), plus global slots `structure` and `origin`. Slots are never
  coined locally; new ones are registered there by a human first.
- **Bug fixed in gate 1.** `verify_consolidation.py` matched claim IDs as `c-[0-9]…`, so
  letter-prefixed pseudo-node IDs (`c-z-1`, the back-matter/colophon claims present in
  `gendun-drub`, `lobsang-dawa`, `tenga-tulku`) were invisible to it: citing one was neither
  verified nor flagged. Now `c-[0-9a-z]…` throughout. Numeric range-expansion patterns were
  left numeric on purpose — a letter-prefixed range falls back to endpoint checking.
- ⚑ **The five pilot topic pages were deleted** in the 2026-08-08 10:10 backup commit
  (`tara-01`, `tara-02`, `benefits` and the two `-bo` pages). They are recoverable from
  commit `878862a` if that was not intended. The audit findings they carried are still
  preserved at `0-INBOX/claims-audit-findings-2026-08-07.md`.

## 7. Status snapshot (2026-08-07)

- Ingest chain + TOC tree (`status: complete`) + tree-guided claims extraction are done for
  **all 16 ingested commentaries** (`Claims/raw/tree-guided/<id>.md`, trees at
  `Sections/Raw/toc-tree/<id>.md`). All 16 raw claims files are `status: draft` — extraction
  drafts, not yet reviewed by a domain specialist (the LLM never marks its own extraction
  complete). Total corpus: 2,975 claims (62–368 per commentary).
- One commentary remains outside this count: `anon-rnam-snang`, excluded pending a human check
  on whether it is a genuine seventeenth commentary or a second copy of the root text (see
  `Guidelines/vault-annex.md` §3's open flags).
- Consolidation (steps 4–6 of §2): pipeline designed and **piloted** 2026-08-07 — 3 topic
  pages exist at `Claims/tara-01.md`, `Claims/tara-02.md`, `Claims/benefits.md`
  (`status: draft`), built via the now-registered `claims-consolidation` skill
  (`4-SYSTEM/Skills/claims-consolidation/SKILL.md`), including a coverage-check gap-fill pass
  on all three. The remaining ~18 per-Tārā pages (Tārā 3–21) and any further global topics
  have not been run yet.
- ⚑ **The three pilot pages carry known, deliberately-unfixed audit findings.** The
  2026-08-07 retrospective audit (see §4 "verification gates") found one critical
  misattribution on `tara-02.md` (`gendun-gyatso:c-1-2-1` cited for a "three flaws" framing
  it does not contain), one moderate overstretch (`tsultrim-namdak:c-3-5`), and ~16 minor
  findings across the three pages. Per the human contributor's decision, the pages were left
  as-is and the effort went into guardrails (skill Rules 9–16, the two verification gates)
  so later pages cannot ship these errors. The full findings are preserved at
  `0-INBOX/claims-audit-findings-2026-08-07.md`; fix the pilot pages against that list
  before any transformation consumes them.
- Verification tooling exists and is validated: `verify_consolidation.py` (gate 1,
  deterministic) and the `claims-consolidation-audit` skill (gate 2, adversarial). Both
  gates are mandatory for every new topic page.

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
| Spine maps (routing index) | `2-RAILS/Claims/raw/spine-map/<registered-id>.md` |
| Canonical spine slot registry | `4-SYSTEM/Guidelines/vault-annex.md` §2a |
| Spine-map skill + its verifier | `4-SYSTEM/Skills/spine-map/{SKILL.md,verify_spine_map.py}` |
| Packet assembler | `4-SYSTEM/Skills/claims-consolidation/assemble_packet.py` |
| Consolidated topic pages | `2-RAILS/Claims/<topic>.md` |
