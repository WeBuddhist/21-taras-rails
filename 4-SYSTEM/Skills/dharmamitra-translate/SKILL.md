---
name: dharmamitra-translate
description: Produce a zero-shot machine-baseline translation of a block-ID'd source text by calling DharmaMitra's public cat-translate API once per block ID, threading the document's own preceding translations back in as context, and writing the result to a new machine-baseline track under 3-TRANSFORMATIONS/Translations/ — never replacing an existing translation.
---

# dharmamitra-translate

Translates a source file from `1-SOURCES/` into any target language by calling DharmaMitra's public `cat-translate` endpoint **once per block ID** — one homage stanza, one prose block — and threading the preceding blocks of the same document back into each call as context, so terminology and register stay coherent across the text. The output is a **machine baseline**: raw API output, block-ID aligned, no `2-RAILS/` involvement and no termbase, written to its own track folder and marked `status: draft`. It never touches `1-SOURCES/` and never overwrites a rails-governed or human translation.

Correct output is a track folder whose translation file carries one target-language block per source block ID, in source order, with every block ID preserved exactly; plus an append-only JSONL ledger recording the exact request behind every line, so any rendering can be traced to the call that produced it.

The failure mode it prevents: silently mixing machine output into the vault's cited translation chain. Everything this skill writes is labelled `track_type: machine-baseline`, `rails_used: none`, and is explicitly ineligible to be cited by any `3-TRANSFORMATIONS/` output or marked `complete`.

---

## Inputs

| Input | Description | Required |
|---|---|---|
| **Source file** | A block-ID'd file under `1-SOURCES/` — root text or commentary. Every translatable block must end in ` ^<id>`. Blocks without an ID are skipped. | yes |
| **Target language** | A free-form language **label**, not an ISO code: `english`, `german`, `modern chinese`, `hindi`. Passed verbatim to the API as `target_language`. | yes |
| **Source language** | Which `input_*` field the blocks fill: `tibetan` (default), `sanskrit`, `chinese`, `pali`. | no |
| **Style instruction** | Free-form prose read **verbatim** by the API model. Lives at `<track>/style.md`; seeded on first run and human-editable thereafter. | no |
| **Context header** | Fixed work-level orientation prepended to every call's `context`. Lives at `<track>/context-header.md`; seeded from the source's frontmatter. | no |
| **Glossary** *(optional)* | A file of `source term<TAB>target rendering` lines. Entries whose source term appears in the current block are added to that call's context. A consolidated `2-RAILS/Bilingual-Glossaries/<src>-<tgt>.md` can be reduced to this shape by hand. | no |

If the target language is not stated in the user's request, ask before running. Do not default to English silently.

## Output

One track folder per target language:

```
3-TRANSFORMATIONS/Translations/<lang-tag>-dharmamitra-zeroshot/
├── about.md                    # what this track is, and what it is not (seeded)
├── style.md                    # the style_instruction sent verbatim (seeded, editable)
├── context-header.md           # fixed work-level context (seeded, editable)
├── <text-slug>-<lang-tag>.md   # the rendered block-ID-aligned translation
└── work/
    └── <lang-tag>.jsonl        # append-only ledger: one record per API call
```

Example: `3-TRANSFORMATIONS/Translations/en-dharmamitra-zeroshot/praise-of-the-twenty-one-taras-en.md`.

---

## Output file format

The rendered translation file:

````markdown
---
title: "<English title of work> — DharmaMitra zero-shot (<language>)"
file_type: translation
track_type: machine-baseline
translation_of: 1-SOURCES/Text/<source file>.md
source_language: tibetan
target_language: english
lang_tag: en
generator: dharmamitra cat-translate v1
endpoint: "https://dharmamitra.org/api-search/cat-translate/v1/translate"
focus: tibetan
context_blocks: 3
style_instruction: "<verbatim string sent to the API>"
rails_used: none
generated: YYYY-MM-DD
blocks_translated: 29
blocks_total: 29
status: draft
---

> [!warning] Machine baseline — not a rails-governed translation.
> Every line below is raw DharmaMitra `cat-translate` output, produced one block at a
> time with no termbase, no verse-context rails, and no human review. …

# <source title line, reproduced>

## <source heading> ^I-0

> <source line 1>
> <source line 2>

<translation line 1>
<translation line 2> ^I-1
````

Rules the render obeys:

- Source headings are reproduced verbatim with their `^N-0` anchors; headings are **not** sent to the API.
- Each source block appears as a blockquote (`--layout parallel`, the default) immediately above its translation; `--layout translation-only` drops the blockquotes.
- The block ID sits at the end of the **last line** of its translation — the same position the source uses.
- A block present in the source but absent from the ledger renders as `*[not yet translated]* ^<id>`, never as a silent gap.

One ledger record per call (`work/<lang-tag>.jsonl`), holding `block_id`, `heading`, `source`, `translation`, `target_language`, `focus`, `style_instruction`, the exact `context` string sent, `endpoint`, `elapsed_s`, `ts`.

---

## Rules

1. **Never write to `1-SOURCES/`.** This skill reads it and nothing more.
2. **Never write into an existing translation track.** Output goes only to a `*-dharmamitra-zeroshot` track (or an explicit `--track` the user named for this purpose). If the target folder already holds a non-baseline translation, stop and report it.
3. **One block ID per API call.** Do not batch several stanzas into one call to save time, and do not split one block across calls. The block ID is the unit of alignment for the whole vault; the ledger and the render both key on it.
4. **Every block ID in the source appears exactly once in the output**, in source order, unaltered. Block IDs are never renumbered, merged, or invented.
5. **This output is never cited.** It is not a rail, it may not be cited by any other `3-TRANSFORMATIONS/` output, and it must not be promoted past `status: draft` by an LLM. Its renderings may feed `2-RAILS/Bilingual-Glossaries/` only through `glossary-extract-raw`, which re-checks them against the sources.
6. **`target_language` is a label, never an ISO code** (`"german"`, not `"de"`). The lang **tag** (`de`) is used only for folder and file naming.
7. **Do not lower the 90 s timeout.** The endpoint is synchronous, 1–8 s typical; a Cloudflare cap at 100 s surfaces as HTTP 524.
8. **Respect the rate limit.** The endpoint is public, unauthenticated and shared: it starts returning HTTP 429 above roughly 10 calls/minute. Keep `--sleep` at 4 s or higher; on 429 the script waits out `Retry-After` (or 20 s → 180 s) before retrying. Never work around a 429 by running several instances in parallel.
9. **The ledger is append-only.** Never hand-edit it. To change a rendering, edit `style.md` and re-run that block with `--force --only <id>`.
10. **Report a partial run as partial.** If the run stops early, say which block it stopped at and how many blocks are done — the frontmatter's `blocks_translated` / `blocks_total` must match reality.

---

## Procedure

### Step 1 — Confirm the inputs

1. Confirm the source file exists under `1-SOURCES/` and its blocks carry `^<id>` markers:
   ```bash
   python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
     --source "1-SOURCES/Text/<file>.md" --list
   ```
   This parses only — it makes no API calls. Check the block count against the vault annex's addressing scheme before going further.
2. Confirm the target language with the user if they did not state one.
3. Confirm the target track folder does not already hold a non-baseline translation.

### Step 2 — Smoke-test three blocks

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> --limit 3
```

This seeds `about.md`, `style.md` and `context-header.md` in the track folder on first run. Read the three translations back before continuing:

- Does the line count of each translation match its source block? (Verse should stay verse.)
- Are mantra syllables and proper names transliterated rather than translated?
- Is the register what the user asked for?

If any answer is wrong, edit `<track>/style.md` — its text goes verbatim to the API — and re-run the same three blocks with `--force`. Iterate here, not after 29 blocks.

### Step 3 — Run the remaining blocks

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language>
```

Blocks already in the ledger are skipped, so this command is also the resume command. If it stops on a rate limit, wait a minute and run it again, or raise `--sleep`.

### Step 4 — Verify the render

1. Confirm `blocks_translated == blocks_total` in the output frontmatter, or state the shortfall.
2. Confirm no `*[not yet translated]*` markers remain (or list the blocks that still carry them).
3. Spot-check that block IDs in the output match the source one-for-one:
   ```bash
   diff <(grep -o '\^[A-Za-z0-9-]*$' "1-SOURCES/Text/<file>.md") \
        <(grep -o '\^[A-Za-z0-9-]*$' "3-TRANSFORMATIONS/Translations/<track>/<file>.md")
   ```
4. Re-render at any time without re-calling the API: add `--render-only`.

### Step 5 — Report

Tell the user: blocks done / total, the track path, the style instruction in force, and any block where the API's line count diverged from the source's. Do not mark anything `complete`; a domain specialist owns that decision, and for a machine baseline the answer is normally that it stays `draft` permanently.

### Adding another language

Re-run Step 2–4 with a different `--lang`. Each language gets its own track folder, its own `style.md`, and its own ledger; no other track is touched.

---

## Completion check

- [ ] `--list` block count matches the source's addressing scheme in the vault annex
- [ ] Target language was stated by the user or explicitly confirmed
- [ ] Three-block smoke test was read back and the style instruction adjusted if needed
- [ ] Track folder contains `about.md`, `style.md`, `context-header.md`, the rendered translation, and `work/<lang-tag>.jsonl`
- [ ] Every source block ID appears exactly once in the rendered file, in source order
- [ ] `blocks_translated` / `blocks_total` in the frontmatter match the ledger and were reported honestly
- [ ] Output frontmatter carries `track_type: machine-baseline`, `rails_used: none`, `status: draft`
- [ ] Nothing under `1-SOURCES/`, `2-RAILS/`, or any other translation track was modified
