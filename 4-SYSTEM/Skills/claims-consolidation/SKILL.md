---
name: claims-consolidation
description: Consolidate one topic's claims across every commentary into a single question-driven topic page — per-commentary mapping in isolation, then question generation and per-facet synthesis, closed by a mandatory coverage check.
---

# claims-consolidation

This is step 5 of the corpus-wide claims pipeline documented in full at
`4-SYSTEM/Guidelines/claims-methodology.md` §2/§4. It takes every commentary's finished
raw claims file and produces one consolidated topic page — the first point in the
pipeline where claims from different commentaries are actually compared against each
other. It exists to prevent two failure modes: **silent claim loss** (a claim that
exists in the corpus never reaching any topic page, with no record that it was even
considered) and **false consensus** (commentaries that genuinely disagree being
merged into one flattened statement). Correct output is a page where every fact in the
corpus relevant to the topic is either synthesised into Consensus/⚑ Divergence/Unique,
or explicitly logged as reviewed-and-excluded — nothing simply absent without a trace.

---

## Inputs

- **A topic definition**: a spine slot (a specific node of the text's canonical
  structure — e.g. one homage/verse-group of a praise, one chapter-section of a
  treatise — or `global` for a cross-cutting topic like recitation benefits) plus a
  starting list of likely facets. Facets are *observed, not fixed* — derive them from
  what the corpus actually discusses, adjust per topic; do not force a fixed facet list
  onto every topic.
- **Every commentary's raw claims file** at `2-RAILS/Claims/raw/tree-guided/<registered_id>.md`
  (all commentaries that have one at run time — do not wait for 100% corpus coverage,
  but do consult everything that exists, including silence as a finding).
- **Every commentary's own TOC tree** at `2-RAILS/Sections/Raw/toc-tree/<registered_id>.md`
  — required because node numbering for "which spine slot is this" is **never uniform
  across commentaries** (see Rule 1).
- **The root text**, if the vault addresses one — `1-SOURCES/Text/` — as ground truth
  for verse/spine-slot boundaries and any epithet or heading text used to verify a
  commentary's own structure against the canonical spine.
- If missing any of the above for a commentary that should plausibly be consulted,
  stop and ask the human contributor rather than silently excluding it.

## Output

One file at `2-RAILS/Claims/<topic-slug>.md`, where `<topic-slug>` follows the
methodology's naming rule (spine + topic, never claim content — e.g. `tara-01`,
`benefits`, never renamed on a re-run).

---

## Output file format

Follow `4-SYSTEM/Templates/consolidated-claims-topic.md` exactly:

```markdown
---
topic: <spine-derived slug>
spine: <which spine node(s) this covers, or "global">
method: question-driven-consolidation
sources:
  - 2-RAILS/Claims/raw/tree-guided/<registered-id-1>.md
  - 2-RAILS/Claims/raw/tree-guided/<registered-id-2>.md
  ...
consolidation_questions:
  - "<question 1>"
  - "<question 2>"
date: <YYYY-MM-DD>
status: draft
---

# <Topic title>

> Consolidated from the raw claims files listed in `sources:`. Every attestation
> cites a raw claim ID; raw claims cite `1-SOURCES/` segments. This page never
> cites a commentary file directly, and regenerating it never touches `raw/`.

## Questions asked

1. <question 1>
2. <question 2>

---

## <Facet heading>

### Consensus
<shared assertion, original language + English gloss>
— attested: `<registered_id>:<claim_id>`, ... (<n> commentaries)

### ⚑ Divergences
<every genuinely conflicting position, each attributed, or "None observed.">

### Unique
<single-commentary claims, each cited, or "None.">

---
## Claims reviewed, not separately cited

<Every claim ID the mapping pass placed in this topic's bucket that did not become an
attestation above, each with a one-line reason (structural-only, duplicate of an
existing attestation, etc.). This section is what makes the coverage check pass —
never leave a gap here silently unexplained.>

---

## Coverage

| Commentary (`registered_id`) | Claims consulted | Contributed to |
|---|---|---|
| <id-1> | ... | ... |

**Commentaries silent on this topic:** <list with reasoning where derivable, or "none">
```

---

## Rules

1. **Node numbering is never assumed uniform.** One commentary may nest a spine
   slot's content at TOC node `1.1.N`, another at top-level node `N`, another may
   group several sub-facets per slot, another may title nodes by epithet/name instead
   of ordinal, another may merge or split slots differently than the canonical spine.
   Every mapping pass must verify against that commentary's *own* TOC tree and the
   root text — never assume a node number that worked for one commentary means the
   same thing in another.
2. **Extraction and consolidation stay separate.** Never edit, reinterpret, or
   "correct" anything under `2-RAILS/Claims/raw/` or `1-SOURCES/` while consolidating.
   Read-only on both. This skill writes only to `2-RAILS/Claims/<topic-slug>.md`.
3. **Citations are always `registered_id:claim_id`.** A bare claim ID (e.g. `c-1-1-3`)
   collides across commentaries — every citation on the page must carry both parts,
   copied verbatim from the source raw claims file.
4. **No consensus flattening.** A genuine disagreement between commentaries is a ⚑
   Divergence, always attributed to each holder, never merged into one Consensus
   statement that erases the disagreement.
5. **Silence is a finding, not a gap.** Every commentary consulted must appear in the
   Coverage table or the "Commentaries silent on this topic" line — never simply
   absent with no record it was checked. State the reason for silence when one is
   derivable from the source (e.g. "this transmission's colophon is missing").
6. **Ambiguous claims are carried through transparently, never silently resolved.**
   A claim the mapping pass could not confidently place must be flagged as ambiguous,
   and the consolidation pass must either use it with a visible flag explaining the
   uncertainty, or explicitly log it as excluded with a reason — never silently
   absorbed as if certain, never silently dropped.
7. **The coverage check is mandatory, not optional.** After the page is written,
   every claim ID the mapping pass placed in the topic's main bucket must be
   mechanically accounted for — cited in a facet section, or logged in "Claims
   reviewed, not separately cited." A page that has not passed this check is not
   finished, regardless of how complete it looks.
8. **`status: draft`, always.** An LLM never marks its own consolidation `complete` —
   that is a domain specialist's judgment call, per `2-RAILS/About Rails.md`.

---

## Procedure

1. **Define the topic.** Fix the spine slot and a starting facet list. If this is
   part of a larger run covering many topics, this list comes from the corpus-wide
   spine grid (methodology §4 — e.g. 21 homages × observed facets for a 21-verse
   praise); if a one-off topic, derive facets from a quick read of 2–3 raw claims
   files' content on that spine slot.

2. **Stage 1 — per-commentary mapping, one isolated agent per commentary.** For each
   commentary with a raw claims file: read that file, its own TOC tree, and (if
   relevant) the root text passage the topic covers. Sort every claim into:
   - the topic's main bucket (claims clearly about this topic),
   - an `ambiguous` list (plausible but uncertain fit, with a reason),
   - or leave it out (genuinely irrelevant).
   Explicitly record which buckets this commentary is silent on. Output the **full
   claim content** (original-language text, English gloss, type, referent, citation)
   for every bucketed claim — not just IDs — so Stage 2 never needs to re-open the raw
   files. This stage is naturally parallel across commentaries (isolated context per
   commentary prevents cross-commentary contamination, the same guard
   `tree-guided-claims` uses per-node).

3. **Assemble the packet.** Concatenate every commentary's Stage 1 output for this
   topic into one document: per commentary, its structural notes, its main-bucket
   claims (verbatim), its ambiguous claims (verbatim, flagged), and an explicit
   silence marker if applicable.

4. **Stage 2 — consolidation, one agent per topic, downstream of the full packet.**
   Working only from the packet (never re-opening raw files):
   a. Generate consolidation questions: a facet grid (mechanical, from the topic's
      facets) plus claim-inversion (every distinctive claim in the packet becomes a
      question asked of the others). Record in `consolidation_questions:` frontmatter
      and echo in `## Questions asked`. A question nobody answers is kept, marked "no
      commentary addresses this," never deleted.
   b. Per facet, write Consensus / ⚑ Divergences / Unique, citing
      `registered_id:claim_id` throughout.
   c. Build the Coverage table covering every commentary in the packet, silent or not.
   d. Write the file at `2-RAILS/Claims/<topic-slug>.md` per the template. Report back
      the exact list of every claim ID cited (`registered_id:claim_id` form).

5. **Coverage check (deterministic, no model judgment).** Diff the claim IDs Stage 1
   placed in the topic's main bucket against the claim IDs Stage 2 reported as cited.
   For every ID in the gap: read where it would fit, and either (a) fold it into the
   appropriate facet section, or (b) add it with a one-line reason to a new "Claims
   reviewed, not separately cited" section (create this section, positioned just
   before "## Coverage", if it doesn't exist). Use `Edit`, not `Write`, for this pass
   — the file already exists and should be modified incrementally. This may be a
   separate small agent per topic, given only the gap list, so it does not need to
   re-read the whole corpus.

6. **Verify.** Confirm the file matches the template's section structure, every
   citation is `registered_id:claim_id`, `status: draft`, and the coverage check
   (step 5) has been run and its result is reflected in the file.

**Implementation note — orchestration.** This pipeline fits a two-phase multi-agent
workflow: Stage 2 needs *every* commentary's Stage 1 output before it can run, so
Stage 1 is a parallel fan-out with a barrier; Stage 2 (and the coverage-check
follow-up) can then run per topic, pipelined if consolidating several topics at once.
The coverage diff itself is plain deterministic comparison, not a model call. Do not
attempt this as a single monolithic prompt — Stage 1 alone needs one isolated context
window per commentary, exactly like `tree-guided-claims`'s per-node isolation; feeding
one agent all commentaries at once for both mapping and consolidation risks exactly
the cross-commentary contamination the isolation guard exists to prevent.

---

## Completion check

- [ ] Every commentary with a raw claims file was consulted in Stage 1 (mapped or
      explicitly marked silent) — none silently skipped
- [ ] Every Stage-1 main-bucket claim ID is accounted for on the finished page —
      either cited or logged in "Claims reviewed, not separately cited" (coverage
      check run and gap closed)
- [ ] Every citation on the page is in `registered_id:claim_id` form
- [ ] No ⚑ divergence was flattened into a false consensus
- [ ] Coverage table lists every commentary consulted, with silence stated and
      reasoned where derivable
- [ ] `status: draft` in frontmatter; `consolidation_questions:` populated and
      echoed in `## Questions asked`
- [ ] No file under `2-RAILS/Claims/raw/` or `1-SOURCES/` was modified
