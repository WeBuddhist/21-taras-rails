---
title: "vi — Gemini zero-shot (vietnamese)"
track_type: machine-baseline
target_language: vietnamese
lang_tag: vi
source_language: tibetan
generator: gemini-3.1-pro-preview
endpoint: https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent
rails_used: none
termbase: none
status: draft
seeded: 2026-09-17
---

# Gemini/vi — about this track

A **machine baseline**, not a rails-governed translation track.

Every file here is raw output of Google Gemini (model `gemini-3.1-pro-preview`, recorded per
block in the ledger as `model_version`), produced by
`4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py`, which sends a small
batch of adjacent block IDs per call and asks for a JSON object holding one
array of lines per block. Nothing in it passed through `2-RAILS/`: no
verse-context package, no consolidated bilingual glossary, no per-track
`termbase.md`, no human review. It therefore does **not** satisfy the
Translation-track contract in
[`../../About Transformations.md`](../../About%20Transformations.md) §3, and it is
not eligible to be marked `status: complete` or to be cited by any other
transformation.

**Source.** Every block is translated from the Tibetan in `1-SOURCES/Text/`,
which is the closest thing to the original that exists. `translation_of` and the
segment alignment therefore point at the Tibetan text. If a run was given an
existing machine translation as *reference* (`--reference-track`), that fact is
recorded in the frontmatter (`reference_translation`) and on every ledger
record (`reference_used`); the reference was context, not source.

## What it is for

- A first display translation for the app in a language no track covers yet.
- A comparison baseline against which a rails-governed translation can be judged.
- A drafting aid and a source of candidate renderings for
  `2-RAILS/Bilingual-Glossaries/` (via `glossary-extract-raw`).

## What governs it

| File | Role |
| --- | --- |
| `style.md` | The style instruction, sent **verbatim** as the system prompt on every call (followed by the fixed output contract). Edit it, then re-run with `--force` to regenerate. |
| `context-header.md` | A work-NEUTRAL, track-wide preamble prepended to every call. The per-text `Work: …` line is derived from each source's own metadata and appended after it. |
| `work/<text>-vi.jsonl` | Append-only ledger, one per source text: one record per block, holding source, translation, the exact context sent, model version, token usage, line-parity result and timings. The audit trail and the resume point. |
| `<text>-vi.md` | The rendered translation, block-ID aligned to the source. |

## Line parity

The whole point of a block-ID-aligned track is that block `^N` here renders
block `^N` of the Tibetan, line for line. The script checks every block's line
count against its source before recording it; a block that comes back wrong is
re-run alone with the required count stated, and only an exact match is
accepted silently. Anything still divergent is recorded with
`line_parity: false` and listed in the run report for human attention.

Regenerate or extend with:

```bash
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py \
  --source "1-SOURCES/Text/<text>.md" --lang vietnamese
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py \
  --source "1-SOURCES/Text/<text>.md" --lang vietnamese --headings     # section headings
```

The renderer carries the researched title, backend ids and import provenance
over from the file it overwrites (see `PRESERVE_FM_KEYS` in `dm_translate.py`),
so no separate stamping pass is needed in this vault.

## Import and run history (this vault)

| Date | Step | Result |
| --- | --- | --- |
| 2026-09-06 | Produced in `Liturgy-rails` by Gemini `gemini-3.1-pro-preview` against the flat block ids `^1`–`^29` of the earlier cut of the same critical edition; uploaded to the library and aligned 1:1 | 29/29 blocks, line-parallel to the source |
| 2026-09-16 | Library edition and alignment deleted when the root text was rebuilt with the rails ids and a table of contents (the translation TEXT and its `text_id` survive) | — |
| 2026-09-17 | Imported into this vault and **re-cut line by line** onto the rails ids (`4-SYSTEM/scripts/recut_liturgy_import.py`): `^1`→`^I-1`+`^I-2`, `^2`→`^I-3`, `^3`–`^22`→`^1-1`–`^1-20`, `^23`→`^1-21`+`^1-22`, `^24`–`^28` (4/4/4/4/6 lines)→`^2-1`–`^2-6` (2/4/4/4/3/5), `^29`→`^a-1`. No word was re-translated by the re-cut; the original ledger and render are under `work/imported-from-liturgy-rails/` | 32/32 blocks, every block line-parallel to the new source |
| 2026-09-17 | Tibetan readings that differ between the two cuts are recorded per block in the ledger (`recut.changed_lines`, 13 blocks; mostly orthographic — ཧཱུཾ/ཧཱུྃ, ཏུཏྟཱ་ར/ཏུ་ཏྟྭ་ར — plus one stray-character repair in `^1-19`). Word-level: `^1-1` བྱེ་བ→ཕྱེ་བ, `^1-11` ནུས་པ→ནུས་མ, `^2-1` རབ་དང→རབ་ཏུ, `^2-6` +ཅིག | — |
| 2026-09-17 | Re-translated with the same generator under the track's `style.md`: `^2-6` (the added optative ཅིག). The older record stays in the ledger; the newer one renders | see `work/*.jsonl` |
| 2026-09-17 | Section headings translated (`--headings`): `^I-0`, `^1-0`, `^2-0`, `^a-0`; the H1 is the researched title | 4/4 |
| 2026-09-17 | Rendered in the transclusion layout and checked (`gm_verify.py`, line parity, ids vs the Tibetan); lint + parse + live-root check pass; **not yet uploaded** — see `4-SYSTEM/Skills/translation-upload/SKILL.md` | pending human confirmation |
| 2026-09-17 | `^2-6` re-run once more with the track `style.md` plus a block note naming the optative ཅིག (recorded in that record's `style_instruction`), after the spot-read found the aspiration rendered as a plain future in en, zh, hi, ne, vi (mn already had болтугай); the Chinese `^I-1` re-run to drop the copied ༄༅༅ ornament; Chinese headings re-run in Traditional characters | newest record renders |
| 2026-09-17 | `^1-0` heading: the leading `1.` (an editorial numeral in the root's `## 1. བསྟོད་པ་དངོས།`) dropped on human instruction — a corrected heading record appended to the ledger (`edit_note`), re-rendered; payloads regenerated into `work/payloads/` and checked with `check_translation_alignment.py --payloads --live` (OK) | ready for upload, pending confirmation |
| 2026-09-17 | **Uploaded** to library.webuddhist.com under the existing text `vROdFp8qvU9rNYMEwhdjl`: edition `pQKlQBCpVAxL0ZLxDgWLy` (32 segments), alignment root→translation (32 identity pairs), TOC `zMB7oTfLcbXMpGAwDHWAI` (1 root section + 4 subsections); read back and diffed against the payloads | live |
