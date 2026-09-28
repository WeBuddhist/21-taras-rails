---
name: dharmamitra-translate
description: Produce a zero-shot machine-baseline translation of a block-ID'd source text by calling DharmaMitra's public cat-translate API on small batches of adjacent block IDs, threading the document's own preceding translations back in as context, and writing the result to a machine-baseline track under 3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/ — block-ID aligned to the Tibetan by transclusion, section headings translated separately, never replacing a human or rails-governed translation.
---

# dharmamitra-translate

Translates a source file from `1-SOURCES/` into any target language by calling DharmaMitra's public `cat-translate` endpoint on **a small batch of adjacent block IDs** — three stanzas, say — and threading the preceding blocks of the same document back into each call as context, so terminology and register stay coherent across the text. Batched blocks are separated by `[[n]]` marker lines that the model echoes back, and the response is split apart on those markers; each block still gets its own ledger record and its own block ID. The output is a **machine baseline**: raw API output, block-ID aligned, no `2-RAILS/` involvement and no termbase, written to its own track folder and marked `status: draft`. It never touches `1-SOURCES/` and never overwrites a rails-governed or human translation.

Correct output is a track folder whose translation file carries one target-language block per source block ID, in source order, with every block ID preserved exactly and an Obsidian transclusion of the Tibetan block above each one; plus an append-only JSONL ledger recording the exact request behind every line, so any rendering can be traced to the call that produced it.

The failure mode it prevents: silently mixing machine output into the vault's cited translation chain. Everything this skill writes is labelled `track_type: machine-baseline`, `rails_used: none`, and is explicitly ineligible to be cited by any `3-TRANSFORMATIONS/` output or marked `complete`.

This is the 21-taras-rails fork of the Liturgy-rails skill (imported 2026-09-17). What differs from the Liturgy version is marked `FORK(21-taras-rails)` in `scripts/dm_translate.py` and summarised in **This vault's conventions** below.

---

## This vault's conventions (read first)

| Topic | Rule here |
|---|---|
| Track folder | `3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/` (the Liturgy layout; the old `<tag>-dharmamitra-zeroshot` folders were retired on 2026-09-17). |
| Rendered file | `<source stem>-<tag>.md`, e.g. `bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en.md`. Never an English slug: the vault linter, parser and uploader derive the source from this filename. |
| Ledger | `work/<source stem>-<tag>.jsonl`, one record per block (and one per translated heading, `kind: heading`). |
| Layout | `--layout transclusion` (default): `![[<source stem>#^<id>]]` above each translated block — the form the vault parser reads the alignment from. `parallel` (blockquote copy) and `translation-only` still exist. |
| Headings | `##` section headings are translated **separately** with `--headings` (one call each, under `HEADING_STYLE`, never batched with verse). Until then the Tibetan heading is reproduced verbatim. The H1 is never machine-translated: it is the work's title from the frontmatter. |
| Frontmatter | What the vault linter expects of `file_type: translation` (`title` in the target language, `root_text`, `language`, `lang_tag`, `category_id`, `license`, `source`, `edition_type`) plus the provenance keys. Keys the renderer cannot know — researched title, backend ids, import provenance (`PRESERVE_FM_KEYS`) — are carried over from the file being overwritten and can be seeded with `--extra-fm <json>`. There is **no separate stamping pass** in this vault. |
| Warning callout | Lives in the frontmatter `note:` key, not in the body — the linter requires every non-transclusion body block to end in a block id. |
| Upload | Never from this skill. See `translation-upload` (`4-SYSTEM/scripts/upload_translation.py`). |

---

## Inputs

| Input | Description | Required |
|---|---|---|
| **Source file** | A block-ID'd file under `1-SOURCES/` — root text or commentary. Every translatable block must end in ` ^<id>`. Blocks without an ID are skipped. | yes |
| **Target language** | A free-form language **label**, not an ISO code: `english`, `german`, `modern chinese`, `hindi`. Passed verbatim to the API as `target_language`. | yes |
| **Source language** | Which `input_*` field the blocks fill: `tibetan` (default), `sanskrit`, `chinese`, `pali`. | no |
| **Style instruction** | Free-form prose read **verbatim** by the API model. Lives at `<track>/style.md`; seeded on first run and human-editable thereafter. | no |
| **Context header** | A work-neutral preamble prepended to every call's `context`; the per-text `Work: <title> (author: …)` line is derived from the source's frontmatter and appended at call time. Lives at `<track>/context-header.md`. | no |
| **Glossary** *(optional)* | A file of `source term<TAB>target rendering` lines. Entries whose source term appears in the current block are added to that call's context. | no |
| **Extra frontmatter** *(optional)* | `--extra-fm <file.json>`: keys to seed or override on render (researched `title`, `text_id`, `imported_from`, …). | no |

If the target language is not stated in the user's request, ask before running. Do not default to English silently.

## Output

```
3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/
├── about.md                          # what this track is, and what it is not (seeded)
├── style.md                          # the style_instruction sent verbatim (seeded, editable)
├── context-header.md                 # work-neutral preamble (seeded, editable)
├── <source stem>-<tag>.md            # the rendered block-ID-aligned translation
└── work/
    ├── <source stem>-<tag>.jsonl     # append-only ledger: one record per block / heading
    └── extra-fm.json                 # (optional) seeded frontmatter keys
```

## Output file format

````markdown
---
title: Praises to the Twenty-One Tārās            # the work's title in the target language
track: DharmaMitra zero-shot (english)
title_original: སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།
language: English
lang_tag: en
file_type: translation
track_type: machine-baseline
root_text: 1-SOURCES/Text/<source stem>.md
translation_of_text_id: <root text_id>
translation_of_edition_id: <root edition_id>
text_id:                                          # this translation's own ids, filled by the uploader
edition_id:
toc_id:
category_id: <copied from the root>
license: public
translator: dharmamitra cat-translate v1
source: https://dharmamitra.org
edition_type: critical
source_language: tibetan
target_language: english
generator: dharmamitra cat-translate v1
endpoint: "https://dharmamitra.org/api-search/cat-translate/v1/translate"
focus: tibetan
context_blocks: 3
batching: "<=3 blocks/call, <=900 src chars, <=6000 payload chars"
style_instruction: "<verbatim string sent to the API>"
rails_used: none
generated: YYYY-MM-DD
blocks_translated: 32
blocks_total: 32
headings_translated: 4
note: Machine baseline — not a rails-governed translation. …
status: draft
---

# <title> ^0

## <translated heading, or the Tibetan heading until --headings has run> ^I-0

![[<source stem>#^I-1]]

<translation line> ^I-1

![[<source stem>#^1-1]]

<translation line 1>
<translation line 2>
<translation line 3>
<translation line 4> ^1-1
````

Rules the render obeys:

- Every source heading keeps its `^N-0` anchor; the H1 carries the frontmatter `title`.
- The block ID sits at the end of the **last line** of its translation — the same position the source uses.
- A block present in the source but absent from the ledger renders as `*[not yet translated]* ^<id>`, never as a silent gap.

One ledger record **per block** (`work/<source stem>-<tag>.jsonl`) — batching never collapses two blocks into one record — holding `block_id`, `heading`, `source`, `translation`, `target_language`, `focus`, `style_instruction`, the exact `context` string sent, `endpoint`, `elapsed_s`, `ts`, plus `batch_size`, `batch_block_ids` and `batch_fallback`. Heading records add `kind: heading`. Records imported from another vault add a `recut` object (see `4-SYSTEM/scripts/recut_liturgy_import.py`).

---

## Batching

DharmaMitra's own agent chunks source into **3–5 sentences (~80–150 source words)** per `cat-translate` call. This skill follows that guidance at block granularity. Latency is nearly all fixed overhead (one block ≈ 8 s, five blocks ≈ 8 s), so the batch size, not the text length, decides how long a run takes.

| Knob | Default | What it bounds |
|---|---|---|
| `--batch` | 3 | Blocks per call. `1` = one call per block. 5 is DharmaMitra's stated ceiling. |
| `--batch-max-chars` | 900 | Source characters in one batch. |
| `--batch-max-lines` | 32 | Source lines in one batch. |
| `--payload-cap` | 6000 | context + style_instruction + source for the whole call. |

A batch is also closed at a **heading boundary** — sections are never mixed — and any block that alone busts a cap is sent on its own. **Marker protocol:** for a batch of more than one block the source is sent as `[[1]]`, block, `[[2]]`, block, … and a clause is appended to the style instruction telling the model to reproduce every marker verbatim. If the markers do not come back as exactly `[[1]]`…`[[N]]`, in order, the response is discarded and the batch is re-run one block per call. Alignment is never inferred from line counts.

---

## Rules

1. **Never write to `1-SOURCES/`.** This skill reads it and nothing more.
2. **Never write into a non-baseline track.** If the target folder already holds a `file_type: translation` file without `track_type: machine-baseline`, stop and report it.
3. **Batch small, and never guess a split.** See Batching.
4. **Every block ID in the source appears exactly once in the output**, in source order, unaltered. Block IDs are never renumbered, merged, or invented.
5. **This output is never cited.** It may not be cited by any other `3-TRANSFORMATIONS/` output and must not be promoted past `status: draft` by an LLM. Its renderings may feed `2-RAILS/Bilingual-Glossaries/` only through `glossary-extract-raw`.
6. **`target_language` is a label, never an ISO code** (`"german"`, not `"de"`). The tag (`de`) is used only for folder and file naming.
7. **Do not lower the 90 s timeout.** A Cloudflare cap at 100 s surfaces as HTTP 524.
8. **Respect the rate limit — it is a DAILY quota** (400 requests per day, observed 2026-08-27). Count calls, not blocks; `--dry-run` prints the call count without spending any. A daily 429 aborts immediately; short-burst 429s back off 20 s → 180 s. Never run several instances in parallel.
9. **The ledger is append-only.** Never hand-edit it. To change a rendering, edit `style.md` and re-run that block with `--force --only <id>`; the newest record wins at render time.
10. **Report a partial run as partial.** `blocks_translated` / `blocks_total` must match reality.

---

## Procedure

All commands run from the vault root.

### Step 1 — Confirm the inputs (no calls)

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --list
```

Check the block count against the vault annex's addressing scheme. Confirm the target language. Confirm the target track folder holds no non-baseline translation.

### Step 2 — Smoke-test six blocks

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> --limit 6
```

Six rather than three, so the smoke test exercises two real batches. This seeds `about.md`, `style.md` and `context-header.md` on first run. Read the translations back: line count per block equal to the source's, mantras and names transliterated, register as asked, no marker fallback on most batches. If anything is wrong, edit `<track>/style.md` and re-run the same blocks with `--force`.

### Step 3 — Run the remaining blocks

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language>
```

Blocks already in the ledger are skipped, so this is also the resume command.

### Step 3b — Translate the section headings

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> --headings
```

One call per `##` heading (level ≥ 2) under `HEADING_STYLE`; the H1 is never sent. Read the four-or-so results back: a short label, numeral kept, nothing added. Re-run one with `--headings --force --only <id>` if needed. These become the section titles of the translation's table of contents on upload.

### Step 4 — Verify the render

1. `blocks_translated == blocks_total` and `headings_translated` equals the number of `##` headings, or state the shortfall.
2. No `*[not yet translated]*` markers, no stray `[[n]]` markers:
   ```bash
   grep -n '\[\[[0-9]\+\]\]\|not yet translated' "3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/<stem>-<tag>.md" || echo clean
   ```
3. Block IDs match the source one-for-one (headings included):
   ```bash
   diff <(grep -o '\^[A-Za-z0-9-]*$' "1-SOURCES/Text/<file>.md") \
        <(grep -o '\^[A-Za-z0-9-]*$' "3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/<stem>-<tag>.md") && echo IDS OK
   ```
4. Line parity per block and no Tibetan inside translation lines: `python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_verify.py --lang-tag <tag> --track 3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>` (the checker is generator-agnostic).
5. Re-render at any time without calling the API: `--render-only` (add `--extra-fm work/extra-fm.json` to seed frontmatter keys).

### Step 5 — Report

Blocks done / total, calls made, headings translated, the track path, the style instruction in force, any batch that fell back to one-block calls, and any block where the API's line count diverged from the source's. Do not mark anything `complete`.

### Step 6 — Upload (separate decision)

Uploading is outward-facing and is done by the `translation-upload` skill, never from here: it lints, parses, checks the live root and asks for confirmation before sending.

---

## Completion check

- [ ] `--list` block count matches the source's addressing scheme in the vault annex
- [ ] Target language was stated by the user or explicitly confirmed
- [ ] Six-block smoke test read back and `style.md` adjusted if needed
- [ ] Section headings translated with `--headings` and read back
- [ ] Track folder contains `about.md`, `style.md`, `context-header.md`, `<stem>-<tag>.md`, `work/<stem>-<tag>.jsonl`
- [ ] Every source block ID (headings included) appears exactly once in the rendered file, in source order
- [ ] `blocks_translated` / `blocks_total` / `headings_translated` reported honestly
- [ ] Frontmatter carries `track_type: machine-baseline`, `rails_used: none`, `status: draft`, `root_text`, `title` in the target language
- [ ] Nothing under `1-SOURCES/`, `2-RAILS/`, or any other translation track was modified
