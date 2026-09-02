---
name: commentary-claims
description: Extract every distinct claim a single commentary makes into one claims file per commentary at 2-RAILS/Claims/raw/<registered-id>.md, stated in the commentary's own Tibetan with a short English gloss and a citation to the segment it came from.
---

# commentary-claims

This skill produces the **per-commentary claims inventory**: an exhaustive, numbered list of every distinct assertion one commentary makes, in that commentary's own words, with a one-line English gloss under each.

It exists because the commentaries in this vault are long, unstructured, and mutually divergent, and because reading them comparatively — verse against verse, commentator against commentator — silently flattens what each one actually says. A claims file is built by reading **one commentary in isolation**, start to finish, with the root text closed. The result is a record of that commentator's position as *he* states it, before any synthesis, comparison, or alignment happens.

Correct output looks like this: a reader who has never opened the commentary can scan the claims file and know every interpretive move the commentator makes, in his own vocabulary, and can jump to the exact segment that supports each one. Nothing in the file comes from the root text, from another commentary, or from the model's own knowledge of Tārā literature.

---

## Inputs

| Input | Description | Path / format |
|---|---|---|
| **Commentary file** | Exactly one file from `1-SOURCES/Commentaries/`. Must carry frontmatter with `registered_id`, `title`, `author`, `lang_tag`. | `1-SOURCES/Commentaries/<filename>.md` |
| **`registered_id`** | The short ID from that file's frontmatter. Names the output file and prefixes every claim ID. | e.g. `karma-maitri` |
| **Segment addressing** | How the commentary's blocks are addressed. Determined by inspection — see Procedure Step 2. | numbered segments, or line numbers |

If the commentary file has no `registered_id` in its frontmatter, **stop** and run `commentary-frontmatter` first. Do not invent an ID.

If the human contributor supplies more than one commentary, run this skill once per commentary. Never merge two commentaries into one claims file.

## Output

One file per commentary at:

```
2-RAILS/Claims/raw/<registered-id>.md
```

`<registered-id>` is taken verbatim from the commentary's frontmatter (`karma-maitri` → `2-RAILS/Claims/raw/karma-maitri.md`). Create `2-RAILS/Claims/` if it does not exist.

---

## Output file format

```markdown
---
registered_id: <registered-id>
title: "<Tibetan title verbatim from the commentary frontmatter>"
title_in_english: "<English title verbatim from the commentary frontmatter>"
author: "<Tibetan author verbatim>"
author_in_english: "<English author verbatim>"
source_file: 1-SOURCES/Commentaries/<filename>.md
language: bo
citation_form: segment | line
claim_count: <integer — total claims in this file>
status: draft
---

# Claims — <title_in_english>

**Commentary:** `<registered-id>` · <author_in_english>
**Source:** [`<filename>.md`](../../1-SOURCES/Commentaries/<filename>.md)
**Citation form:** <one sentence stating how the `§` numbers in this file resolve
to the source — segment numbers carried in the source text, or line numbers.>

> Every claim below is drawn from this commentary alone. No claim originates in
> the root text, in another commentary, or outside `1-SOURCES/`.

---

## A. Framing claims

<Claims the commentator makes about the text as a whole before glossing it:
what the praise is, who spoke it, how it is divided, what the commentary
intends to do, lineage and transmission statements.>

### A1. <short label>
**བོད་ཡིག:** <the claim in the commentator's own Tibetan wording — quoted or
minimally compressed, never rephrased into other vocabulary>
**English:** <one-line gloss>
**Type:** structural
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

### A2. <short label>
...

---

## B. Word and phrase glosses

<Claims that explain what a word or phrase means: etymologies, ཚིག་འགྲེལ,
synonym substitutions, grammatical readings.>

### B1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** etymology | word-gloss | grammar
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## C. Identification and iconography claims

<Claims identifying a figure, colour, implement, posture, retinue, seat, or
ornament, and claims about what each stands for.>

### C1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** iconography | identification
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## D. Doctrinal claims

<Claims about doctrine: the pāramitās, the kāyas, emptiness, the grounds and
paths, the two accumulations, karma, the nature of mind.>

### D1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** doctrinal
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## E. Activity and function claims (ཕྲིན་ལས)

<Claims about what the deity does: what is pacified, subdued, increased,
magnetised; which obstacles are removed; which beings are protected.>

### E1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** activity
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## F. Practice and ritual claims

<Claims instructing practice: visualisation sequence (དམིགས་རིམ), mantra
recitation, offerings, timing, posture, number of repetitions.>

### F1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** practice | ritual | mantra
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## G. Benefit claims (ཕན་ཡོན)

<Claims about results of recitation or practice: what is averted, obtained,
purified, accomplished, and under what conditions.>

### G1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** benefit
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## H. External attributions

<Claims the commentator attributes to a named source outside this commentary:
a tantra, a sūtra, a named master, an oral instruction. Record the attribution
as the commentator states it. Do not verify, correct, or expand the reference.>

### H1. <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Attributed to:** <the source exactly as the commentator names it>
**Type:** attribution
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## I. Internal tensions

<Only if the commentary states two positions that do not sit together, or
offers an alternative reading with འམ། / གཞན་དག་ན་རེ། / ཁ་ཅིག་ན་རེ།. Mark each
with ⚑ and record both positions with their own citations. If the commentary
is internally consistent throughout, write "None observed." and keep the
heading.>

⚑ **I1. <short label>**
- **Position 1:** <Tibetan> — (…md §<n>)
- **Position 2:** <Tibetan> — (…md §<n>)
**English:** <one line stating what the tension is>

---

## Coverage log

| Source range | Claims extracted | Notes |
|---|---|---|
| §1–§<n> | A1–…, B1–… | |
| §<n>–§<n> | … | |

**Segments yielding no claim:** <list ranges that are pure root-text quotation,
colophon, or scribal matter, so a reviewer can see nothing was skipped silently.>
```

---

## Rules

1. **One commentary per file, read in isolation.** Do not open a second commentary while extracting. Do not consult the root text to decide what a passage means. If the commentary quotes the root text, the quotation is context for the claim, not itself a claim.
2. **No root-text-derived organisation.** Claims are grouped by the categories A–I above, never by root verse number. A claims file must be readable without the root text open.
3. **The commentator's own vocabulary, verbatim.** Quote the Tibetan as written. Compression is allowed; substitution is not. If he writes བདུད་སྡེ་འཇོམས་པས་ན་དཔའ་མོ།, the claim reads བདུད་སྡེ་འཇོམས་པས་ན་དཔའ་མོ། — never "she is heroic because she conquers māras" in Tibetan paraphrase.
4. **Every claim carries a citation.** A claim with no `(1-SOURCES/Commentaries/<filename>.md §<n>)` reference is not a claim — delete it. This is the §8 hard rule of `2-RAILS/About Rails.md`.
5. **English is a gloss, not a translation.** One line, plain, for orientation only. It never adds information absent from the Tibetan and is never cited from.
6. **Exhaustive, not selective.** Every distinct assertion gets its own entry, including ones that merely restate a root phrase in other words — that restatement *is* the commentator's reading. Splitting is preferred to merging: two assertions in one sentence become two claims.
7. **No parametric knowledge.** Never add a fact about Tārā, a tantra, a lineage, or an iconographic convention that this commentary does not state. If the commentator's reference is obscure, record it as written and leave it obscure.
8. **Never mark `status: complete`.** This skill writes `status: draft`. Only a domain specialist promotes a claims file.
9. **Do not modify `1-SOURCES/`.** This skill reads the commentary and writes only to `2-RAILS/Claims/raw/`.
10. **Empty categories are kept, not deleted.** If a commentary makes no ritual claims, section F remains with the single line `None.` — the absence is itself a finding about that commentary.

---

## Procedure

### Step 1 — Load the commentary

a. Read the full frontmatter of the target file in `1-SOURCES/Commentaries/`.
b. Record `registered_id`, `title`, `title_in_english`, `author`, `author_in_english`.
c. If `registered_id` is absent, stop and report; run `commentary-frontmatter` first.

### Step 2 — Determine the citation form

a. Inspect the body of the commentary.
b. If blocks carry leading segment numbers (`2 དང་པོ་ནི། …`), set `citation_form: segment`; `§<n>` refers to that number.
c. If blocks carry no numbers, set `citation_form: line`; `§<n>` refers to the file's line number.
d. If blocks carry Obsidian block IDs (`^<n>`), set `citation_form: segment` and cite `#^<n>` in the standard `About Rails` §8 form instead of `§<n>`.
e. State the resolved form in the **Citation form** line of the output header.

### Step 3 — Read the commentary in full, in order

a. Read from the first block to the last. Do not sample, skim, or jump to the sections that look substantive.
b. Read in contiguous chunks sized so that no chunk is truncated mid-argument.
c. Keep a running note of the source range covered — this becomes the Coverage log.

### Step 4 — Extract claims chunk by chunk

For each chunk:

a. Identify every distinct assertion the commentator makes.
b. For each assertion, write the Tibetan in his own wording, then the one-line English gloss.
c. Assign it to exactly one category A–I. When an assertion could sit in two categories, place it in the more specific one (C over D, F over E).
d. Attach the segment or line citation.
e. Where the commentator marks an alternative view (འམ། / གཞན་དག་ན་རེ། / ཁ་ཅིག་ན་རེ།), record it in section I with ⚑ as well as in its own category.

### Step 5 — Number the claims

a. Number sequentially within each category: `A1, A2, …`, `B1, B2, …`.
b. Numbers are stable identifiers — never renumber an existing claims file when appending.

### Step 6 — Write the Coverage log

a. Record each source range against the claim IDs drawn from it.
b. List explicitly any ranges that yielded no claims, with the reason (root-text quotation, colophon, scribal matter).

### Step 7 — Write the file

a. Write to `2-RAILS/Claims/raw/<registered-id>.md`, creating the directory if needed.
b. Fill `claim_count` with the total across all categories.
c. Set `status: draft`.

### Step 8 — Self-verification

a. Confirm every `###` claim heading has a `**Cite:**` line.
b. Confirm no claim text mentions another commentary or the root text file.
c. Confirm every category heading A–I is present, including empty ones.
d. Confirm the Coverage log's ranges span the whole source file with no unexplained gap.

---

## Completion check

- [ ] Exactly one commentary was read, in isolation, from first block to last
- [ ] Output written to `2-RAILS/Claims/raw/<registered-id>.md` with `<registered-id>` matching the source frontmatter
- [ ] Frontmatter complete: `registered_id`, `title`, `author`, `source_file`, `citation_form`, `claim_count`, `status: draft`
- [ ] All nine category headings A–I present; empty ones carry `None.` rather than being deleted
- [ ] Every claim has a Tibetan statement, an English gloss, a `**Type:**`, and a `**Cite:**`
- [ ] Every citation resolves to a segment or line that actually exists in the source file
- [ ] No claim draws on the root text, another commentary, or parametric knowledge
- [ ] Alternative or conflicting positions recorded in section I with ⚑
- [ ] Coverage log accounts for the entire source file, including segments that yielded nothing
- [ ] `claim_count` equals the number of claim entries actually present
- [ ] `1-SOURCES/` unmodified
