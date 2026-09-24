---
title: Current translations — start here
file_type: index
updated: 2026-09-24
---

# Current translations — start here

**Rule:** in each language folder, the file at the top (`bo-…-<lang>-general.md`) is the **current
translation**. Everything in its `reports/` subfolder is the evidence behind it. `Dharmamitra/` and `Gemini/`
hold raw machine output, which is never the translation to use.

"Current" is not yet "final": no translation here has had its native-speaker or specialist review.

## Current translations

| Language | Current file | Draft | Checks done | Still to do | On the platform |
|---|---|---|---|---|---|
| English (general) | [[en-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general]] | 3 | locked words 131/131 · full commentary fact-check (4 commentaries, consensus) · translator decisions | specialist review · `translation-qa` · upload | no |
| Chinese (general, Traditional) | [[zh-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general]] | 3 | locked words 137/137 · back-translation meaning check · commentary light check | native Chinese review (word list first) · `translation-qa` · upload | no |

## Reports behind each translation

**English** — `en-general/reports/`
- `commentary-fact-check-report-*-en-general.md`: one per commentary (Drakpa Gyaltsen, Gendun Drub, Taranatha,
  Tenga Tulku)
- `commentary-fact-check-consensus-en-general.md`: what the four agree on
- `commentary-fact-check-fixes-log-en-general.md`: every fix applied, plus the translator decisions
- `comparison-draft1-vs-draft3-en-general.md` and `consistency-report-en-general.md`: how much the drafts
  improved

**Chinese** — `zh-general/reports/`
- `phase2-fixes-log-zh-general.md`: draft 1 → 2 (approved words enforced, clear errors fixed)
- `back-translation-check-zh-general.md`: draft 2 → 3 (meaning check, verse by verse)
- `commentary-light-check-zh-general.md`: Chinese-only word choices checked against the commentaries

**Word lists** (in `0-INBOX/AI_translation/keyword-extraction-dharmamitra/`): `en-bo-en-termbase-general.json`
for English; for Chinese, `zh-decisions-general.json` (the file to edit) and `termbase-zh-general.md` (the file
to review).

## Machine drafts — raw, not for use

| Folder | Language | What it is | On the platform |
|---|---|---|---|
| `Dharmamitra/en/` | English | DharmaMitra zero-shot (draft 0) | yes (baseline) |
| `Dharmamitra/en-general/` | English | DharmaMitra primed with the English word list (draft 1 of en-general) | no |
| `Dharmamitra/zh/` | Chinese | DharmaMitra zero-shot (draft 0) | yes (baseline) |
| `Dharmamitra/zh-general/` | Chinese | DharmaMitra primed with the Chinese word list (draft 1 of zh-general) | no |
| `Gemini/hi/`, `Gemini/mn/`, `Gemini/ne/`, `Gemini/vi/` | Hindi, Mongolian, Nepali, Vietnamese | Gemini zero-shot — the starting point for those languages | yes (baselines) |

These folders stay where they are, because the translation scripts write to these paths. Don't edit the files
by hand; a new run replaces them.
