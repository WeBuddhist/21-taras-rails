---
name: glossary-select
description: >
  Choose the one target-language rendering each source lemma will receive in one
  translation track, and write it to that track's `termbase.md`. Step 0 builds the
  descriptive variant menu — every rendering the pivot (zero-shot) translation
  actually used for each lemma, with counts and block IDs — from the `keyword-extract`
  run's per-block en↔bo mappings. Step 1 decides each contested lemma from the track's
  purpose, audience, register and the text's TOC, never from frequency alone.

  Trigger on "standardise the vocabulary", "pick the English word for each term",
  "build the termbase for <track>", "which rendering should we use for <term>",
  "gather the translation variants", "vocab standardisation".
profile: rails-vault
---

> **Locations.** Paths below are this vault's. Cross-vault equivalents are in
> [`../_shared/PROFILES.md`](../_shared/PROFILES.md); block ID and heading rules
> are in [`../_shared/CONVENTIONS.md`](../_shared/CONVENTIONS.md).

# glossary-select

This is **the only skill in the rails workflow that introduces target-language
vocabulary into the project.** Every other skill catalogues what already exists;
this one chooses. That is why its output lives in `3-TRANSFORMATIONS/` (prescriptive)
and never in `2-RAILS/` (descriptive) — except for the Step 0 menu, which is a
pure count of what a translation already did.

The skill runs in two steps, and they are different in kind:

| Step | Kind | Does | Writes |
| --- | --- | --- | --- |
| 0 — Build the menu | Descriptive, mechanical | For each source lemma, gather every rendering the pivot translation used, with occurrence count and block IDs | `2-RAILS/Bilingual-Glossaries/<pair>.md` |
| 1 — Select | Prescriptive, judged | Choose one rendering per lemma for this track, and record what decided it | `3-TRANSFORMATIONS/Translations/<track>/termbase.md` |

Step 0 is a script and takes seconds. Step 1 is the actual work, and it is
**much smaller than the term count suggests** — see §The decision surface.

---

## Inputs

| Input | Step | Required | Notes |
| --- | --- | --- | --- |
| **Keyword mappings** | 0 | ✓ | `0-INBOX/AI_translation/keyword-extraction/output/mappings/batch*.json` — the `keyword-extract` run's per-block `{en, bo, drop, note}` records. This is the alignment data; it already exists for a promoted run. |
| **Keyword verses** | 0 | ✓ | `…/output/<run>_keyword_verses.json` — supplies the pivot English text per block, for counting. |
| **Source-term registry** | 0 | ✓ | `2-RAILS/Keywords/source-term-registry.json` — supplies each lemma's rank and `match_form`. |
| **Variant menu** | 1 | ✓ | `2-RAILS/Bilingual-Glossaries/<src>-<tgt>.md`, Step 0's output. |
| **Track contract** | 1 | ✓ | `3-TRANSFORMATIONS/Translations/<track>/` carrying `requirements.md`, `audience.md`. A track without its contract is not a track — create both before selecting. Older tracks may carry `about.md` + `style.md` instead; read those, but write the contract files before proceeding. |
| **TOC** | 1 | recommended | `2-RAILS/Sections/Raw/toc-tree/<commentary>.md` and the root text's own `##`/`###` headings. Used to tell which structural context a lemma occurs in. |
| **Meaning column** | 1 | fallback | `2-RAILS/termbases/term-localization.md` — the only legitimate source for a rendering when no attested one fits. |

---

## Output

```
3-TRANSFORMATIONS/Translations/<track>/termbase.md
```

**The first two columns are load-bearing.** `dharmamitra-termlocked`'s
`build_lock_glossary.py` parses this file positionally: column 1 must be the
source lemma (Tibetan), column 2 must be the locked rendering. It skips any row
whose first cell contains no Tibetan, and it splits several source variants in
one cell on ` / `. Add columns after those two freely; never reorder them.

```markdown
---
track: <track-name>
language_pair: <bo-en | …>
source_language: <bo>
target_language: <en>
requirements: 3-TRANSFORMATIONS/Translations/<track>/requirements.md
audience: 3-TRANSFORMATIONS/Translations/<track>/audience.md
variant_menu: 2-RAILS/Bilingual-Glossaries/<src>-<tgt>.md
total_terms: <count>
decided: <count>
undecided: <count>
last_updated: <ISO date>
status: draft
---

# Termbase — <track-name>

| Source lemma | Locked rendering | Origin | Decided by | Blocks |
| --- | --- | --- | --- | --- |
| སྒྲོལ་མ། | Tārā | attested | audience.md §who — a devotional reader knows the name; "liberates" reads as a verb and loses the vocative | 1-1, I-1, a-7 |
| གཙུག་ཏོར། | uṣṇīṣa | derived | no attested option fit; Meaning cell (dharmabhadra ^3-12) defines it as the cranial protuberance, not a crown | 1-4 |
| རིམས། |  | ⚑ undecided | "infectious disease" is accurate but breaks the line length requirement; needs a human call | 1-20, a-5 |

**An undecided row leaves column 2 empty** and carries the `⚑ undecided` marker in
`Origin`. This is not cosmetic: `build_lock_glossary.py` skips a row with an empty
rendering, but a row whose column 2 reads `⚑ undecided` is parsed as a lock and
the literal string `⚑ undecided` is sent to the translation engine. Verified
against `parse_termbase` — an empty cell is dropped, any non-empty cell is not.

## Notes on derivations

### གཙུག་ཏོར།

<Why no attested rendering satisfied the contract, and which Meaning-column
quotation the new rendering was derived from. Cite the block ID.>

## Sense notes

### ཚོགས། — locked as "assembly"

<The minority sense, its rendering, and the blocks that take it. Not lockable;
`commentary-fact-check` checks these by hand.>
```

The table is the artefact. **Notes on derivations** carries a paragraph only for
rows whose `Origin` is `derived`; attested selections need no prose beyond their
`Decided by` cell.

---

## The decision surface

Do not treat the term count as the workload. On this vault's 2026-08 run the
menu holds **372 lemmas / 510 renderings**, but:

- **269 lemmas have exactly one attested rendering.** There is nothing to decide —
  copy it, unless the contract forbids it.
- **42 lemmas are contested by inflection only** (`disease`/`diseases`,
  `pacification`/`pacifying`). One lexical choice covers the family; the translator
  inflects to fit the line. Marked `~` in the menu. Do not burn a decision on these.
- **61 lemmas are lexically contested** — two or more genuinely distinct words
  (`crown` vs `protrusion`, `Tārā` vs `liberates`). Marked `⚑`. **These are the job.**

Work down by rank and stop where the returns stop. A lemma at rank 300 appearing
in one block rarely repays a considered decision.

The `~` / `⚑` split is a crude suffix heuristic for triage. Read the rows, not
the mark.

---

## What decides a rendering

In precedence order. A lower signal never overrides a higher one.

1. **Explicit directives in `requirements.md`.** A named term mapping is binding.
   If a directive conflicts with everything else, follow the directive and note
   the conflict in `Decided by`.
2. **Purpose and audience** (`audience.md`): who reads this, with what prior
   knowledge, for what use. A liturgy a practitioner recites and a study text a
   scholar annotates take different words for the same lemma. This is usually
   the signal that actually decides.
3. **Register and style** (`requirements.md`, or an older track's `style.md`):
   devotional vs analytical, line-length and syllable constraints, whether
   Sanskrit is transliterated or translated.
4. **The TOC and section titles.** The menu gives each rendering's block IDs.
   Map those blocks to their section — the root text's `##`/`###` headings, or a
   commentary's tree under `2-RAILS/Sections/Raw/toc-tree/`. The section's title
   states what that passage is doing, which often resolves a lemma that looks
   ambiguous in isolation. On a short root text this signal is weak; on a
   commentary, where one lemma spans a doctrinal section and a ritual one, it is
   frequently the deciding signal.
5. **Attested frequency.** A tie-breaker only. The pivot is a zero-shot machine
   translation — its counts record what a model happened to emit, not what the
   tradition attests. **Never let frequency decide a lemma on its own.**

---

## Rules

1. **Attested first, derived only when forced.** If any rendering in the menu
   satisfies the contract, take it. Derive only when none does.
2. **A derived rendering comes from the Meaning column, never from parametric
   knowledge.** Read `2-RAILS/termbases/term-localization.md` for that lemma. If
   its Meaning cell is empty, run `term-definition` for that one term first, or
   leave the row `⚑ undecided`. **Inventing a rendering from general Buddhist
   knowledge breaks the citation chain and is the one failure this skill exists
   to prevent.**
3. **Flag, don't guess.** A row you cannot decide gets an **empty** rendering
   cell and `⚑ undecided` in `Origin`, with the reason in `Decided by`, and is
   listed in the end report. Only an empty column 2 is inert; see §Output. A
   guessed row is a silent error that reaches the published translation.
4. **One rendering per lemma per track.** This is a contract, not a thesaurus.
   **The lock glossary cannot express a sense split** — it matches the source
   lemma by plain substring, so two rows for one lemma give two conflicting
   locks, and a disambiguator written into column 1 (`ཚོགས། (assembly)`) is
   carried through verbatim and matches no block. So: lock the dominant sense in
   column 2, and record the minority sense under **Sense notes** with its block
   IDs and its rendering, flagged for `commentary-fact-check` to check by hand.
   Say in `Decided by` which sense was locked and why.
5. **Choose the lexical family, not the inflection.** Record the citation form;
   the translator inflects. Do not create a row per inflection.
6. **`Decided by` is mandatory and names its signal.** Not "sounds better" —
   name the clause of `audience.md`, the requirements directive, or the section
   title that decided it. Downstream, `commentary-fact-check` reads these when a
   rendering is challenged, and a future run needs to know whether a choice was
   reasoned or default.
7. **Never write back into the variant menu.** Step 0's output is machine-generated
   and regenerated from the mappings; a hand-added row is destroyed on the next
   run. (This reverses the pre-2026-09 rule, which predates the menu being derived.)
   Derived renderings live in the track termbase only.
8. **Columns 1 and 2 are fixed.** See §Output. Reordering them silently empties
   the lock glossary.
9. **Script preserved.** Source lemmas keep the menu's form, including the
   trailing shad. Do not convert to `match_form` here — `build_lock_glossary.py`
   does that conversion, and doing it twice is how locks get dropped.

---

## Procedure

### Step 0 — Build the variant menu

```bash
python3 4-SYSTEM/Skills/glossary-select/scripts/build_variant_menu.py \
  --mappings-dir "0-INBOX/AI_translation/keyword-extraction/output/mappings" \
  --keyword-verses "0-INBOX/AI_translation/keyword-extraction/output/<run>_keyword_verses.json" \
  --registry "2-RAILS/Keywords/source-term-registry.json" \
  --pivot "<run-name>" \
  --out "2-RAILS/Bilingual-Glossaries/bo-en.md"
```

It prints the lemma count, the rendering count, and the contested split. Read
that line before going on — it is the size of the job.

Rows the keyword run adjudicated as extraction artefacts (`drop: true`) are
excluded from the menu and listed under **Dropped pairs**, so the decision stays
visible rather than disappearing.

> **The alternative producer.** `interlinear-gloss` → `glossary-extract-raw` →
> `glossary-combine` builds the same file token by token from an aligned
> translation. Use that route when there is no `keyword-extract` run, or when
> more than one translation exists and the menu should show them side by side.
> This script's advantage is that it reuses alignment work already done; its
> limit is that it sees only the blocks the keyword run covered (on this vault,
> the root text's 29 blocks — not the commentaries).

### Step 1 — Select

1. **Read the contract.** `requirements.md` and `audience.md` in full. Note the
   hard directives separately from the soft preferences — rule 1 depends on the
   distinction.
2. **Read the menu's header line.** It tells you how many lemmas are lexically
   contested. Those and the single-option rows are two different passes.
3. **Single-option rows:** copy the rendering. Check only that the contract does
   not forbid it (a transliteration in a track that translates Sanskrit, say).
   These can be done in bulk.
4. **For each ⚑ lemma, by rank:**
   - Read its rows: the renderings, their counts, their blocks.
   - Resolve the blocks to their sections (root headings; commentary toc-trees).
   - Apply the signals in §What decides a rendering, in order. Stop at the first
     one that settles it, and name it in `Decided by`.
   - If none settles it, open `2-RAILS/termbases/term-localization.md` for that
     lemma and derive from the Meaning cell — `Origin: derived`, plus a paragraph
     in **Notes on derivations**.
   - If the Meaning cell is empty, write `⚑ undecided`. Do not guess.
5. **Write `termbase.md`.** Set `total_terms`, `decided`, `undecided`,
   `last_updated`; `status: draft`.
6. **Verify it parses as a lock glossary** before declaring the step done:

   ```bash
   python3 4-SYSTEM/Skills/dharmamitra-termlocked/scripts/build_lock_glossary.py \
     --termbase "3-TRANSFORMATIONS/Translations/<track>/termbase.md" \
     --source "1-SOURCES/Text/<root-text>.md" \
     --out "3-TRANSFORMATIONS/Translations/<track>/lock-glossary.tsv"
   ```

   Read its coverage report. A lemma that matches no block of the source is
   either a bad lemma form or a term the root text does not use — both worth
   knowing before spending API calls.

---

## Re-running

Regenerate the **menu** whenever the keyword run is re-promoted or the mappings
are corrected. Regenerate the **termbase** whenever `requirements.md` or
`audience.md` changes, or the menu gains renderings.

On a re-run, read the existing `termbase.md` first and **preserve every
`Decided by` cell whose underlying selection still holds.** Those cells are
human reasoning; the menu is cheap and they are not.

A translation pass that introduces a new rendering on the fly records it in the
track termbase; it never edits the menu (rule 7).

---

## End report

State:

- Menu: lemmas, renderings, lexically contested, inflection-only, dropped pairs.
- Termbase: rows written, `attested` vs `derived`, `⚑ undecided` (list them).
- Every row where a hard directive overrode another signal.
- Every lemma whose Meaning cell was empty when a derivation was needed — these
  are the `term-definition` backlog this run generated.
- The `build_lock_glossary.py` coverage figure.

---

## Completion check

- [ ] Every menu lemma appears as a termbase row, or is excluded for a stated reason
- [ ] Column 1 is the Tibetan lemma, column 2 the rendering — unreordered
- [ ] Every decided row has an `Origin` and a `Decided by` that names a signal
- [ ] Every `derived` row has a paragraph citing the Meaning-column block ID
- [ ] No rendering was invented from parametric knowledge (rule 2)
- [ ] Undecided rows have an EMPTY column 2, with `⚑ undecided` in `Origin`
- [ ] Sense splits lock one sense and record the other under **Sense notes** — no disambiguator in column 1
- [ ] No row was written back into `2-RAILS/Bilingual-Glossaries/`
- [ ] `build_lock_glossary.py` parses the file and its coverage report was read
- [ ] Frontmatter `requirements`, `audience` and `variant_menu` paths resolve
