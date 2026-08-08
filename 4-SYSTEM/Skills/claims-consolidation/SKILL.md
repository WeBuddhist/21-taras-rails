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
- **Every commentary's spine map** at `2-RAILS/Claims/raw/spine-map/<registered_id>.md`,
  built once per commentary by the `spine-map` skill. This is what resolves "which node
  of *this* commentary is this spine slot" — never uniform across commentaries (Rule 1).
  A commentary with a raw claims file but no spine map is a hard stop, not a silent
  omission: `assemble_packet.py` exits non-zero on it.
- **Every commentary's raw claims file** at `2-RAILS/Claims/raw/tree-guided/<registered_id>.md`
  (all commentaries that have one at run time — do not wait for 100% corpus coverage,
  but do consult everything that exists, including silence as a finding). Read by the
  assembler, not by you: never re-open these while consolidating.
- **The registered slot list** at `4-SYSTEM/Guidelines/vault-annex.md` §2a — the topic's
  slot ID and root anchor come from there.
- **The root text**, if the vault addresses one — `1-SOURCES/Text/` — as ground truth
  for the slot's verse text when writing the topic page's heading and framing.
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
   of ordinal, another may run every slot inside a single undivided node. This is
   resolved once per commentary by the `spine-map` skill against that commentary's
   *own* TOC tree and the root text — never re-derived here, and never assumed from a
   node number that worked for another commentary. If a packet looks wrong for a
   commentary, fix its spine map and re-assemble; do not patch the topic page.
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

The following rules encode the error classes found by the 2026-08-07 adversarial
audit of the three pilot pages (one critical false-corroboration, one moderate
overstretch, ~16 minor findings across 418 citations). Each rule exists because the
audit caught a real instance of its violation:

9. **Full-statement support.** A claim may be listed in a Consensus attestation list
   only if it supports the *entire* consensus statement. If the statement bundles two
   propositions (the pilot case: "recite at dusk/dawn" + "wrathful at dusk, peaceful
   at dawn") and some claims attest only one, either split the facet into two
   statements, or split the attestation list ("attested (timing only): …"). Never pad
   a list with same-topic-but-partial claims — the count becomes a false measure of
   how widely the full statement is attested.
10. **Corroboration must be re-read, not remembered.** Before writing "X and Y
    independently attest…", re-open both claims in the packet and confirm each one
    actually contains the shared content. The audit's single critical finding was
    exactly this: a "three flaws" framing attributed to a second commentary whose
    cited claim contains no such framing (the consolidator had the right *idea* in
    the corpus but attached the wrong claim ID).
11. **One side per divergence.** A claim ID appears on at most one side of any single
    ⚑ divergence. If it seems to support two readings, that is a finding about the
    claim — say so explicitly rather than citing it both ways.
12. **Verbatim quotes or marked ellipsis.** Tibetan quoted *from a specific claim*
    is copied character-for-character from the packet's བོད་ཡིག — no silent elision
    (use … for omissions), no orthographic normalization, no dropped particles.
    Synthesised consensus Tibetan is permitted, but must not be attributed to a
    specific claim ID.
13. **Harmonization is the page's, not the claim's.** When the page derives something
    the claim does not itself state (the pilot case: reading 7×7=49 into a claim
    whose own gloss says only "cycles of seven"), attribute the derivation to the
    page ("read together, these imply…"), never to the claim.
14. **Epistemic strength is copied, not upgraded.** A tentative authorial aside
    (…སྙམ་མོ, "I think") is reported as tentative — never as "endorses" or "holds."
15. **Counts are computed, never hand-tallied.** Every "(N commentaries)" label and
    every "N of sixteen" arithmetic statement is recomputed from the final attestation
    list before the page is done (the deterministic checker does this — see Procedure
    step 6). Five of five hand-tallied count labels on the pilot's worst page were
    wrong.
16. **Every consulted claim gets a disposition.** Any claim ID the Coverage table
    lists as consulted must appear either as a citation in some facet or as an entry
    in "Claims reviewed, not separately cited" — no third state.

---

## Procedure

1. **Define the topic.** Fix the spine slot and a starting facet list. If this is
   part of a larger run covering many topics, this list comes from the corpus-wide
   spine grid (methodology §4 — e.g. 21 homages × observed facets for a 21-verse
   praise); if a one-off topic, derive facets from a quick read of 2–3 raw claims
   files' content on that spine slot.

2. **Confirm every commentary has a spine map.** The per-commentary routing lives at
   `2-RAILS/Claims/raw/spine-map/<registered-id>.md`, built once per commentary by the
   `spine-map` skill. If any commentary with a raw claims file lacks one, stop and run
   `spine-map` on it first — step 3 will fail loudly rather than silently omitting it.

3. **Assemble the packet — deterministic, no model call.**

   ```
   python3 4-SYSTEM/Skills/claims-consolidation/assemble_packet.py <slot> \
       --out 0-INBOX/temp/packet-<slot>.md \
       --manifest-out 0-INBOX/temp/manifest-<slot>.txt
   ```

   This replaces what used to be a per-commentary mapping pass run once per topic — a
   full re-read of all sixteen raw claims files for every topic, ~400 full-corpus reads
   across a complete run. The routing judgment now happens once per commentary, in the
   spine map; this script does only the mechanical part: collecting the slot's claims
   out of each raw file and concatenating them.

   The packet carries, per commentary: its node(s) and verbatim node titles, every claim
   block **copied character-for-character** from the raw file, claims routed by ID rather
   than node (flagged ⓘ), ambiguous claims (flagged ⚑, to be carried through per Rule 6),
   and an explicit silence marker where the spine map records silence. A non-zero exit
   means a real gap — a commentary with no disposition for this slot, or none at all —
   never proceed past it.

   Because the script copies rather than retypes, it also removes at the source the
   quote-fidelity error class the pilot audit found (silently elided syllables,
   normalized orthography). Quote Tibetan **from the packet**, never from memory.

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

5. **Coverage check (deterministic, no model judgment).** Diff the packet's
   `## Manifest` (equivalently, `--manifest-out`) against the claim IDs Stage 2
   reported as cited.
   For every ID in the gap: read where it would fit, and either (a) fold it into the
   appropriate facet section, or (b) add it with a one-line reason to a new "Claims
   reviewed, not separately cited" section (create this section, positioned just
   before "## Coverage", if it doesn't exist). Use `Edit`, not `Write`, for this pass
   — the file already exists and should be modified incrementally. This may be a
   separate small agent per topic, given only the gap list, so it does not need to
   re-read the whole corpus.

6. **Deterministic checks (gate 1).** Run the bundled checker on the finished page:

   ```
   python3 4-SYSTEM/Skills/claims-consolidation/verify_consolidation.py 2-RAILS/Claims/<topic-slug>.md
   ```

   It verifies citation existence (including ⚑ bold-block internal-tension claims),
   recomputes every "(N commentaries)" label, flags claims cited on both sides of a
   facet's Consensus/Divergences, finds undispositioned Coverage-table claims, and
   counts unprefixed citations. **Fix every ERROR and re-run until zero remain**;
   review each WARN and either fix it or note why it stands. Also confirm the file
   matches the template's section structure and `status: draft`.

7. **Adversarial attribution audit (gate 2 — model judgment).** Run the
   `claims-consolidation-audit` skill on the page (one fresh agent per page that did
   NOT write it, checking every attribution against the raw files). This is what the
   deterministic checker cannot do: confirm each claim actually *says* what the page
   attributes to it, quotes are faithful, divergences are real, epistemic strength is
   preserved. Fix every critical and moderate finding, apply or consciously decline
   each minor one, then re-run the audit on the changed sections. A page that has not
   passed both gates is not finished. (The pilot pages skipped this gate on first
   writing; the retrospective audit then found a false corroboration that reached the
   final file — the gate exists so that never happens again.)

**Implementation note — orchestration.** Packet assembly is now a script, so the only
model work per topic is Stage 2 (one agent, working from the packet) plus any gap-closing
repair. Topics are therefore independent and fan out cleanly — consolidating twenty-odd
slots is twenty-odd parallel Stage-2 agents, each reading one packet, not a corpus.

The isolation guard that used to live in Stage 1 has moved upstream to `spine-map`, which
is still one isolated agent per commentary and still for the original reason: an agent
primed on one commentary's numbering mis-reads the next one's. Do not hand a single agent
several commentaries' spine maps to build at once.

The coverage diff is a plain set comparison against the packet manifest, not a model call.

---

## Completion check

- [ ] Every commentary with a raw claims file has a spine map, and the packet was
      assembled with `assemble_packet.py` exiting zero — none silently skipped
- [ ] Every claim ID in the packet's `## Manifest` is accounted for on the finished
      page — either cited or logged in "Claims reviewed, not separately cited"
      (coverage check run and gap closed)
- [ ] Every citation on the page is in `registered_id:claim_id` form
- [ ] No ⚑ divergence was flattened into a false consensus
- [ ] Coverage table lists every commentary consulted, with silence stated and
      reasoned where derivable
- [ ] `status: draft` in frontmatter; `consolidation_questions:` populated and
      echoed in `## Questions asked`
- [ ] **Gate 1:** `verify_consolidation.py` run on the final page — zero ERRORs,
      every WARN either fixed or consciously accepted
- [ ] **Gate 2:** `claims-consolidation-audit` run by a fresh agent — zero
      critical/moderate findings outstanding
- [ ] No file under `2-RAILS/Claims/raw/` or `1-SOURCES/` was modified
