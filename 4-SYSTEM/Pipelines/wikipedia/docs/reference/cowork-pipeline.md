# Tibetan Buddhist Texts → Wikipedia Pipeline (canonical, 17 steps)

> **Provenance.** Designed in a claude.ai session by the team lead on 2026-08-01
> (<https://claude.ai/share/dbdee4e9-5786-4672-9119-51ea1786cd05>) and delivered to this repo on
> 2026-08-02. The share snapshot preserves the document's *first* version verbatim plus the
> full text of every later change description; the final embedded prompts survive verbatim in
> the per-step skills (<https://claude.ai/share/09ecaf85-57e5-4180-979b-b27912d0affa>, ported to
> `4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/`). This file is the repo's reconstruction of the final
> document from those two sources. Where it disagrees with the skills, the skills win — they
> postdate the last edit.
>
> **This document is the canonical home of the step prompts** (maintenance rule stated in every
> skill): a step-13 patch lands here first, then syncs to the skill — and in this repo, also to
> a new version file under `prompts/` (never edit a shipped prompt version in place).

Corpus: public-domain root texts and commentaries (BDRC-sourced OCR), staged in a private
Obsidian vault with Claude Cowork; final articles published to bo.wikipedia with sources on
multilingual wikisource.org.

Two load-bearing invariants:

1. **Nothing downstream ever touches source wording after the claims stage** — the claims table
   is the only drafting input; passages remain in the vault as verification material.
2. **Nothing is published that hasn't survived the audit** (step 12) **and the pre-publication
   review** (step 16, gating steps 14–16).

Everything else is replaceable machinery around those two rules.

---

## Vault layout

```
/vault/
  texts/<text-id>.md            ← step 1: one note per source text; frontmatter = canonical metadata
  alignment/<text-id>.md        ← step 2: verse-alignment tables
  concepts/<concept>/
    passages.md                 ← step 6 (immutable)
    outliers.md                 ← step 7
    claims.md                   ← step 8 (immutable; the only drafting input)
    outline.md                  ← step 9
    draft-claude.md             ← step 10
    draft-gemini.md             ← step 11
    audit.md                    ← step 12
  pipeline/feedback.md          ← step 13 ledger; also receives step-17 community feedback
  skills/<nn>-<name>/SKILL.md   ← one skill per step
  scripts/                      ← bdrc_fetch.py · gemini_polish.py · publish.py
```

*(This repo's equivalent layout is `corpora/<id>/…` — the mapping table is in
`4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/PROVENANCE.md`.)*

## Execution environment

The whole pipeline runs in **Claude Cowork**, with each of the 17 steps packaged as its own
skill (`skills/<nn>-<name>/SKILL.md`) declaring its prompt, inputs/outputs, invariants, and any
script it invokes. The prompt blocks in this document are the canonical prompt text — patch
here, then sync to the skill. The step-13 feedback loop targets skills, which is the payoff of
per-step packaging: fixes land exactly where the drift originated.

Three scripts carry the deterministic work:

- **`bdrc_fetch.py`** — prefills step-1 frontmatter from the BDRC API. Claude verifies rather
  than recalling metadata from memory.
- **`gemini_polish.py`** — the step-11 rewrite, with the model version **pinned and logged per
  run**, so the feedback loop can tell prompt problems from model-version drift.
- **`publish.py`** — drives steps 14–16 through the MediaWiki and Wikidata APIs, writing URLs
  and QIDs back into frontmatter automatically. **Gate: it only runs after the pre-publication
  review prompt returns "publish"** — the second invariant is enforced by process, not habit.

---

## A. Corpus layer (Obsidian vault)

**1. Ingest & provenance.**
Ingest root texts + commentaries. Record edition provenance for every e-text (Derge, Pedurma,
etc.). Check death dates for any modern commentators — 20th-century masters are typically still
under copyright (life + 50–70 yrs); modern editorial apparatus can be too. OCR quality is
covered by the BDRC collaboration; no separate spot-check stage.
Run `scripts/bdrc_fetch.py` first; the note header below is the **canonical metadata record**
for the whole pipeline — every downstream stage reads from it, and step 15 pushes it to
Wikidata.

Frontmatter schema (canonical — copy exactly):

```yaml
---
id: derge-madhyamakavatara-comm-tsongkhapa   # stable ID prefix (edition–text)
title_bo: དབུ་མ་དགོངས་པ་རབ་གསལ།
title_wylie: dbu ma dgongs pa rab gsal
type: commentary            # root | commentary | subcommentary | refutation
comments_on: derge-madhyamakavatara   # stable ID of target text (commentaries/refutations)
author_bo: ཙོང་ཁ་པ་
author_wylie: tsong kha pa blo bzang grags pa
author_dates: 1357–1419
copyright: public-domain    # router: derived from author death date; decides step 14 target
school: gelug
edition: derge              # printing/edition of this e-text
bdrc_id: W00000             # BDRC work/scan ID (provenance + Wikidata property)
ocr_source: bdrc-ocr        # e-text provenance
language: bo
wikidata_work: ""           # QID — filled by step 15
wikidata_author: ""         # QID — filled by step 15
source_url: ""              # filled by step 14: Wikisource page (PD) or BDRC/WeBuddhist link
---
```

`copyright` is a **router, not a gate**: it decides *where* readers verify a source (step 14),
never whether the text may be cited. `wikidata_*` and `source_url` stay empty at ingest — the
publication layer fills them, so the vault and the wikis never diverge.

Canonical prompt:

```
For the source text {{FILE}}, create texts/{{TEXT_ID}}.md using the frontmatter
schema exactly, fully filled.
- Derive `copyright` from the author's death date: public-domain if the author
  died 70+ years ago; otherwise `copyrighted`. If dates are uncertain, write
  `copyrighted-assumed` and flag for my review.
- Identify the edition from colophon/catalog data; if ambiguous, list the
  candidates instead of guessing.
- For commentaries, resolve `comments_on` to the root text's stable ID; if the
  root text isn't in the vault yet, flag it.
- Leave wikidata_* and source_url empty.
- Below the frontmatter, add a 3–5 line prose note: what the text is, its place
  in its school's curriculum, and known reception (who cited or refuted it).
Never invent metadata. Every uncertain field gets a `# TODO:` comment, not a
plausible guess.
```

**2. Verse alignment & stable IDs.**
Align commentaries to the root text verse-by-verse. Mint **edition-aware stable IDs**
(`edition–text–chapter–verse`) used everywhere downstream, and later as Wikisource section
anchors — so refs generated during drafting survive publication unchanged.

```
Align {{COMMENTARY_ID}} to its root text {{ROOT_ID}} verse by verse. Output
alignment/{{COMMENTARY_ID}}.md as a table:
root verse stable ID | commentary locator (edition-aware) | confidence
(high/medium/low) | note.
- Use the commentary's own structural markers (sa bcad, root-verse citations)
  as anchors.
- A section covering multiple verses maps to all of them; skipped verses are
  recorded as explicit gaps.
- Mark low confidence rather than forcing an alignment; list all unaligned
  sections at the end.
```

**3. Keyword extraction.**
TF-IDF over the corpus → candidate terms (scripted; the prompt covers only the judgment half).
Cluster Wylie/Unicode/Sanskrit/orthographic variants and abbreviations per concept so counts
don't split.

```
Here are the top TF-IDF terms for the corpus: {{TERM_LIST}}. Cluster them into
concepts:
- Merge orthographic variants, abbreviations, Wylie/Unicode duplicates, and
  standard Sanskrit equivalents of the same concept.
- Do NOT merge distinct technical terms that are merely related — when unsure,
  keep separate and note the relation.
- Output one row per concept: canonical Tibetan form | all variants | Sanskrit
  equivalent if standard | one-line gloss.
```

**4. Concept selection.**
Rank candidates by **TF-IDF distinctiveness × breadth** (number of independent
commentators/schools treating the concept). Breadth doubles as the due-weight and notability
signal.
**Exception lane:** a concept treated by only one commentator still qualifies if it (a) drew
significant response/refutation literature, or (b) defines a school's position. This catches
the famous controversies — often the most encyclopedically valuable articles.

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

**5. Wikidata match (concepts).**
For each selected concept, find or note the absence of a Wikidata item. Existing items show how
en/zh/de articles structured the topic and confirm the concept isn't already covered under a
variant name.

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

---

## B. Extraction layer (Claude Cowork)

**6. Passage gathering.**
Per concept, pull relevant passages via the verse links. Tag each with edition-aware locator +
commentator + school → `passages.md` (**immutable once written**). Passages stay in the vault
as verification material — never published, never seen again by the drafting stages.

```
You are preparing the bo.wikipedia article "{{CONCEPT}}". Your reader is an
educated Tibetan speaker who is not a scholastic specialist.
Using the alignment tables, gather every passage relevant to {{CONCEPT}} (all
variant forms) into concepts/{{CONCEPT}}/passages.md, grouped by source text.
For each passage record:
- LOCATOR: edition-aware stable ID (+ section within it)
- AUTHOR/SCHOOL: from the text note's frontmatter
- ANSWERS: which reader question it serves — definition · etymology/Sanskrit
  background · doctrinal context · positions & interpretations · disputes &
  refutations · practice relevance · history of the term
- NOTE: one line on why it matters or how it differs from other sources on the
  same point
Copy passages verbatim — they stay private as verification material and are
never published. Extract disagreements aggressively: passages where a
commentator names and refutes another position are the most valuable. Skip
tangential mentions. This file is immutable once written.
```

**7. Outlier detection (mechanical).**
Using the verse alignment, diff commentaries on the same root verse. Where one diverges
lexically or doctrinally from the others, classify: **substantive divergence** vs.
**idiosyncratic phrasing** vs. **OCR artifact**. The alignment makes this nearly free — use it.
Only (a) items feed the claims table as positions; (c) items go back to the corpus team.

```
Using the alignment tables for the verses relevant to {{CONCEPT}}, compare all
commentaries verse by verse. Where one commentary diverges from the others on
the same root verse, classify the divergence:
(a) substantive doctrinal divergence — a different position, not different
    wording
(b) idiosyncratic phrasing of the same point
(c) probable OCR/e-text artifact
Output concepts/{{CONCEPT}}/outliers.md:
verse ID | diverging commentator | class | one-line description | for (a):
who, if anyone, responds to this position elsewhere in the corpus.
Only (a) items feed the claims table as positions; (c) items are reported back
to the corpus team.
```

**8. Atomic claims (in Tibetan).**
Convert passages → claims table, one verifiable fact per row → `claims.md` (immutable):

| Field | Content |
|---|---|
| ID | C-number |
| Claim | one fact, own words, Tibetan, locked glossary terms preserved |
| Locator | edition-aware verse/section ID |
| Commentator / School | author + Nyingma / Gelug / Sakya / Kagyu / Jonang / … |
| **Claim type** | consensus · majority-with-dissent · school-position · single-commentator |
| **Reception** | cited by whom · refuted by whom (dgag lan and response literature) · unengaged |

Claim-type and reception rules:

- **Weight by authority and response, not headcount.** A position held by one major figure
  outweighs one shared by several minor commentators. The corpus-internal proxy for authority
  is how often *other* commentators cite or refute the position — refutation literature is a
  reception record; a position that drew rebuttals has proven weight.
- **Normalize for corpus composition.** Tag each concept's coverage per school. If the corpus
  is skewed (e.g. Gelug-heavy), a sole representative of an entire school is a
  **school-position, never a fringe view** — Zhentong is a one-author outlier by headcount and
  a defining doctrine by reality.
- Nothing is dropped for being an outlier; claim type determines treatment downstream.

```
Read concepts/{{CONCEPT}}/passages.md and outliers.md. Produce claims.md: one
verifiable fact per row, written in Tibetan in your own words — never reuse a
source's sentence structure. These glossary terms must appear verbatim:
{{GLOSSARY}}.
Columns: ID | claim (bo) | locator | commentator/school | claim type |
reception.
- Claim type: consensus · majority-with-dissent · school-position ·
  single-commentator. Weight by authority and response, not headcount. A
  commentator who is the sole representative of his school in our corpus is a
  school-position, never single-commentator.
- Reception: cited by … / refuted by … (name the texts) / unengaged.
- One fact per row; split compound statements. Conflicting positions get one
  row each — never merge into a compromise no source states.
- Forbidden: any claim requiring two sources combined to reach a conclusion
  neither states alone. Record temptations in a "forbidden syntheses" list at
  the end instead.
- Flag rows resting only on a copyrighted source (verifiable only via the
  BDRC/WeBuddhist link).
This file is immutable once written.
```

---

## C. Drafting layer

**9. Outline.**
Built from claims only → `outline.md`. Sections weighted by breadth across independent
commentaries, **adjusted by reception**: an outlier position that others argued against gets a
section; an unengaged idiosyncrasy gets a sentence or footnote. Divergent school positions
marked for in-text attribution.

```
From claims.md ONLY (do not open passages.md), propose the article outline in
outline.md:
- Lead + body sections per bo.wikipedia conventions; under each section, the
  claim IDs it will use.
- Weight sections by breadth across independent commentaries, adjusted by
  reception: a refuted-and-defended position gets a section; an unengaged
  idiosyncrasy gets at most a sentence.
- Mark every section containing sub-consensus claims — these need in-text
  attribution when drafted.
- Gap report: sections resting on one source; reader questions (step 6
  taxonomy) with no claims; contested points needing "According to X…"
  treatment.
```

**10. Claude draft.**
From claims only — passages closed — claim IDs inline → `draft-claude.md`.
Voice rules by claim type: **consensus** claims may sit in Wikipedia's voice; **everything
below consensus gets mandatory in-text attribution** ("Mipham holds that…", "in the Gelug
presentation…"). An outlier must never appear unattributed.

```
Write the article draft in Tibetan in draft-claude.md, using ONLY outline.md
and claims.md. passages.md stays closed — you must never see source wording
while drafting.
- Every factual sentence ends with its claim ID(s): [C12][C31]. A sentence
  without IDs must contain no factual assertion.
- Voice by claim type: consensus → Wikipedia's voice; everything below
  consensus → in-text attribution naming the commentator or school.
- Glossary terms verbatim: {{GLOSSARY}}. Define technical terms on first use
  for a non-specialist reader.
- Lead: summarizes the body, defines the concept in the first sentence,
  contains nothing not in the body.
- Add no fact, date, or example from your own knowledge — if it has no claim
  ID, it does not exist.
Style is polished later; correctness and attribution are your only priorities.
```

**11. Gemini rewrite.**
Literary Tibetan rewrite, preserving claim IDs and locked glossary terms → `draft-gemini.md`.
Runs through `gemini_polish.py`; **pin and log the model version per run**. Gemini is a
stylist, not an editor.

```
Rewrite the following draft in fluent literary Tibetan suitable for an
encyclopedia. Hard constraints:
1. Keep every claim ID marker [Cnn] attached to the same statement it marks
   now.
2. These technical terms must appear verbatim, never paraphrased: {{GLOSSARY}}.
3. Change no factual content: add no facts, drop no qualifiers, and keep every
   attribution ("X holds that…") explicit — never absorb an attributed
   position into the neutral voice.
4. Do not reorder sections or merge sentences across different claim IDs.
You are a stylist, not an editor. If a sentence cannot be improved without
violating a constraint, leave it unchanged.
```

**12. Claude audit.**
Sentence-by-sentence check of the Gemini text against `claims.md` → `audit.md`: added facts,
dropped qualifiers, terminology drift, and **softened or dropped attributions** (a
school-position silently promoted to Wikipedia's voice is an audit failure). The audit compares
against `claims.md`, never against `passages.md`.

```
Compare draft-gemini.md sentence by sentence against claims.md. Output
audit.md, one row per finding:
sentence (quoted) | claim ID(s) | finding | severity.
Findings to detect: added fact (no claim ID covers it) · dropped or weakened
qualifier · terminology drift (glossary term paraphrased) · attribution
softened or dropped · claim ID attached to the wrong statement · meaning shift
in the rewrite.
Added facts and attribution loss are blocking: the article cannot publish
until fixed. End with a verdict: publish / fix listed items / return to
drafting.
```

**13. Feedback step.**
Classify each audit finding by the stage that caused it (extraction / claims / draft / rewrite)
and patch that stage's prompt before the next article. Immutable per-stage outputs make the
drift diffable to its origin. When the causal stage is the rewrite, check the logged Gemini
model version before blaming the prompt. Patches land in **this document** first, then sync to
the skill.

```
For each finding in audit.md, name the stage that caused it: extraction
(passage missed or mistagged) · claims (claim wrong, mistyped, or badly
worded) · draft (Claude introduced it) · rewrite (Gemini introduced it).
Append to pipeline/feedback.md:
finding | causal stage | proposed one-line patch to that stage's prompt.
Findings recurring across articles get priority patches.
```

---

## D. Publication layer

Gate for the whole layer: the **pre-publication review** (step 16 — its canonical prompt gates
steps 14–16 as a unit) must return **publish**, and `audit.md` must carry a publish verdict,
before `publish.py` runs anything.

**14. Source publication (routed by `copyright`).**
- **Public domain** → page on multilingual wikisource.org with section anchors matching the
  vault stable IDs; the edition stated on each text's page.
- **Copyrighted** → no republication; a stable link to the text on BDRC or WeBuddhist (prefer
  BDRC's persistent work/scan IDs where both exist). Refs to copyrighted texts lose verse-level
  deep-linking, so **the ref itself must carry the full locator** (folio/page) from the claims
  table; keep any verbatim quotation in such refs brief.
- Either way the resulting URL is written back into the text note's `source_url` — frontmatter
  stays the single source of truth.

This actually widens the usable corpus: modern commentaries can enter the pipeline as claim
sources (with attribution as usual), since nothing requires republishing them — the claims
table extracts facts, the passages stay private in the vault, and readers verify via the BDRC
link.

**15. Wikidata sync (texts & authors).**
For each cited source text — **PD and copyrighted alike** (metadata is facts; only republishing
full text is restricted) — match or create Wikidata items for the work and its author from the
frontmatter: instance of, title (Tibetan + Wylie aliases), author, language, the BDRC resource
ID property, edition information. PD works get their Wikisource page linked to the item;
copyrighted works anchor through the BDRC ID. QIDs are written back into `wikidata_work` /
`wikidata_author`. Check whether BDRC's catalog records already carry QIDs — matching via the
BDRC ID first avoids duplicate items. Statements come from frontmatter only, never from model
memory.

**16. Wikipedia.**
Publish the article to bo.wikipedia with refs deep-linking to the Wikisource anchors. Link the
article to its concept's Wikidata item (create one if needed; backfill the QID from step 5) —
interwiki links wire up automatically.

Pre-publication review (canonical copy in `skills/16-wikipedia/SKILL.md`; gates 14–16):

```
Act as a skeptical reviewer of the final wikitext before publication:
1. Refs: every ref resolves — PD sources to a Wikisource anchor matching the
   vault ID; copyrighted sources to a BDRC/WeBuddhist link carrying the full
   folio/page locator in the ref text. No more than a short phrase quoted
   verbatim in refs to copyrighted texts.
2. Attribution: scan for any sub-consensus claim sitting in neutral voice.
3. Synthesis: any sentence whose conclusion requires two sources combined.
4. Wikidata: concept QID present; cited works' and authors' QIDs exist
   (step 15 complete).
5. Restate the strongest independence case: which sources establish the
   concept's weight beyond a single school.
Verdict: publish / fix first.
```

**17. Paced rollout.**
First articles in small batches; method disclosed on a project page; community reaction
absorbed before scaling volume. On-wiki feedback (reverts, talk-page critique, editor
corrections) flows back into step 13 alongside audit findings — first-class feedback-loop
input, not a side channel. No volume scaling before community reaction to prior batches is
absorbed.

---

## Weighting principle (summary)

**Breadth measures the existence of a topic; reception measures the weight of a position.**

- Concept level: breadth (× the exception lane) decides what gets an article.
- Claim level: authority + citation/refutation record decides how much space and what voice a
  position gets.
- Buddhist polemical culture left a reception record — the pipeline is built to read it.
