---
title: "Praise of the Twenty-One Taras — DharmaMitra zero-shot (modern chinese)"
track_type: machine-baseline
target_language: modern chinese
lang_tag: zh
translation_of: 1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md
generator: dharmamitra cat-translate v1
endpoint: https://dharmamitra.org/api-search/cat-translate/v1/translate
rails_used: none
termbase: none
status: draft
seeded: 2026-09-17
---

# zh-dharmamitra-zeroshot — about this track

A **machine baseline**, not a rails-governed translation track.

Every file here is raw output of DharmaMitra's public `cat-translate` endpoint,
produced in small batches of adjacent block IDs by
`4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py`, then split back
apart on segment markers so each block keeps its own record. Nothing in it
passed through `2-RAILS/`: no verse-context package, no consolidated bilingual
glossary, no per-track `termbase.md`, no human review. It therefore does **not**
satisfy the Translation-track contract in
[`../About Transformations.md`](../About%20Transformations.md) §3, and it is not
eligible to be marked `status: complete` or to be cited by any other
transformation.

## What it is for

- A comparison baseline against which a rails-governed translation can be judged.
- A drafting aid and a source of candidate renderings for
  `2-RAILS/Bilingual-Glossaries/` (via `glossary-extract-raw`).
- A fast first look at a text in a language no track covers yet.

## What governs it

| File | Role |
| --- | --- |
| `style.md` | The `style_instruction` string, sent **verbatim** to the API on every call. Edit it, then re-run with `--force` to regenerate. |
| `context-header.md` | A work-NEUTRAL, track-wide preamble prepended to every call's `context`. The per-text `Work: …` line is derived from each source's own metadata and appended after it. |
| `work/zh.jsonl` | Append-only ledger: one record per API call — source, translation, the exact context sent, timings. The audit trail and the resume point. |
| `bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh.md` | The rendered translation, block-ID aligned to the source. |

## Provenance

- Endpoint: `https://dharmamitra.org/api-search/cat-translate/v1/translate` (public, unauthenticated)
- Source: [`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`](1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md)
- Granularity: up to 3 adjacent source block IDs per API call, never crossing a
  heading; each block still gets its own ledger record and its own block ID.
- Rolling context: the preceding translated blocks of this same document are
  threaded into each call so terminology and register stay coherent.

Regenerate or extend with:

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md" --lang modern chinese
```

## Import and run history (this vault)

| Date | Step | Result |
| --- | --- | --- |
| 2026-08-29 | Produced in `Liturgy-rails` by DharmaMitra `cat-translate` against the flat block ids `^1`–`^29` of the earlier cut of the same critical edition; uploaded to the library and aligned 1:1 | 29/29 blocks, line-parallel to the source |
| 2026-09-16 | Library edition and alignment deleted when the root text was rebuilt with the rails ids and a table of contents (the translation TEXT and its `text_id` survive) | — |
| 2026-09-17 | Imported into this vault and **re-cut line by line** onto the rails ids (`4-SYSTEM/scripts/recut_liturgy_import.py`): `^1`→`^I-1`+`^I-2`, `^2`→`^I-3`, `^3`–`^22`→`^1-1`–`^1-20`, `^23`→`^1-21`+`^1-22`, `^24`–`^28` (4/4/4/4/6 lines)→`^2-1`–`^2-6` (2/4/4/4/3/5), `^29`→`^a-1`. No word was re-translated by the re-cut; the original ledger and render are under `work/imported-from-liturgy-rails/` | 32/32 blocks, every block line-parallel to the new source |
| 2026-09-17 | Tibetan readings that differ between the two cuts are recorded per block in the ledger (`recut.changed_lines`, 13 blocks; mostly orthographic — ཧཱུཾ/ཧཱུྃ, ཏུཏྟཱ་ར/ཏུ་ཏྟྭ་ར — plus one stray-character repair in `^1-19`). Word-level: `^1-1` བྱེ་བ→ཕྱེ་བ, `^1-11` ནུས་པ→ནུས་མ, `^2-1` རབ་དང→རབ་ཏུ, `^2-6` +ཅིག | — |
| 2026-09-17 | Re-translated with the same generator under the track's `style.md`: `^2-6` (the added optative ཅིག). The older record stays in the ledger; the newer one renders | see `work/*.jsonl` |
| 2026-09-17 | Section headings translated (`--headings`): `^I-0`, `^1-0`, `^2-0`, `^a-0`; the H1 is the researched title | 4/4 |
| 2026-09-17 | Rendered in the transclusion layout and checked (`gm_verify.py`, line parity, ids vs the Tibetan); lint + parse + live-root check pass; **not yet uploaded** — see `4-SYSTEM/Skills/translation-upload/SKILL.md` | pending human confirmation |
| 2026-09-17 | `^2-6` re-run once more with the track `style.md` plus a block note naming the optative ཅིག (recorded in that record's `style_instruction`), after the spot-read found the aspiration rendered as a plain future in en, zh, hi, ne, vi (mn already had болтугай); the Chinese `^I-1` re-run to drop the copied ༄༅༅ ornament; Chinese headings re-run in Traditional characters | newest record renders |
| 2026-09-17 | `^1-0` heading: the leading `1.` (an editorial numeral in the root's `## 1. བསྟོད་པ་དངོས།`) dropped on human instruction — a corrected heading record appended to the ledger (`edit_note`), re-rendered; payloads regenerated into `work/payloads/` and checked with `check_translation_alignment.py --payloads --live` (OK) | ready for upload, pending confirmation |
| 2026-09-17 | **Uploaded** to library.webuddhist.com under the existing text `O9TxCvL6lhjufpaaOAxAj`: edition `PHYYTAPEDkEDb0cxNZf1u` (32 segments), alignment root→translation (32 identity pairs), TOC `OLPyu5ELI2kykrg21xYR9` (1 root section + 4 subsections); read back and diffed against the payloads | live |
