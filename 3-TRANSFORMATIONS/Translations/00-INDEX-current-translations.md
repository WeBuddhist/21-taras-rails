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
| English (general) | [[en-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general]] | 4 | locked words 131/131 · full commentary fact-check (4 commentaries, consensus) · translator decisions · **QA 99.8, PASS** (after fixes) | specialist review · upload | no |
| Chinese (general, Traditional) | [[zh-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general]] | 5 | locked words 137/137 · back-translation meaning check · **QA 99.9, PASS** (after fixes) · full commentary fact-check (4 commentaries, no errors, 5 fixes) | native Chinese review (word list first) · upload | no |
| Vietnamese (general) | [[vi-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-vi-general]] | 5 | locked words 137/137 · back-translation meaning check · full commentary fact-check (9 fixes, 4 translator decisions) · **QA 99.8, PASS** (after fixes) | native Vietnamese review (word list first) · upload | no |
| Hindi (general) | [[hi-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-hi-general]] | 5 | locked words 136/136 · back-translation meaning check · full commentary fact-check (no errors, 13 fixes, 2 translator decisions) · **QA 100.0, PASS** (after fixes) | native Hindi review (word list first) · upload | no (the old Gemini baseline is) |
| Nepali (general) | [[ne-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general]] | 6 | locked words 136/136 · back-translation meaning check · full commentary fact-check (1 error fixed, 15 fixes) · **QA 97.4 → 100.0, PASS** | native Nepali review (word list first) · upload | no (the old Gemini baseline is) |

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
- `commentary-light-check-zh-general.md`: the earlier light check (superseded)
- `qa-report.md`, `qa-fixes-log-zh-general.md`: draft 3 → 4 (translation-qa)
- `commentary-fact-check-report-*-zh-general.md`, `…-consensus-zh-general.md`, `…-fixes-log-zh-general.md`: draft 4 → 5

**Vietnamese** — `vi-general/reports/`
- `phase2-fixes-log-vi-general.md`: draft 1 (Gemini zero-shot) → 2 (approved words enforced, clear errors fixed)
- `back-translation-check-vi-general.md`: draft 2 → 3 (meaning check, verse by verse)
- `commentary-fact-check-report-*-vi-general.md`: one full report per commentary
- `commentary-fact-check-consensus-vi-general.md` and `commentary-fact-check-fixes-log-vi-general.md`: draft 3 → 4
- `commentary-light-check-vi-general.md`: the earlier light check (superseded)

**Hindi** — `hi-general/reports/`
- `phase2-fixes-log-hi-general.md`: draft 1 (Gemini zero-shot) → 2 (approved words enforced)
- `back-translation-check-hi-general.md`: draft 2 → 3 (meaning check, verse by verse)
- `commentary-fact-check-report-*-hi-general.md`: one full report per commentary
- `commentary-fact-check-consensus-hi-general.md` and `commentary-fact-check-fixes-log-hi-general.md`: draft 3 → 4

**Nepali** — `ne-general/reports/`
- `phase2-fixes-log-ne-general.md`: draft 2 (Gemini primed with the word list) → 3 (approved words enforced)
- `back-translation-check-ne-general.md`: draft 3 → 4
- `commentary-fact-check-report-*-ne-general.md`, `…-consensus-ne-general.md`, `…-fixes-log-ne-general.md`: draft 4 → 5
- `qa-report.md`, `qa-fixes-log-ne-general.md`: draft 5 → 6

**QA** — each language's `reports/qa-report.md` (translation-qa: MQM score, gate, and the re-check after fixes) and `reports/qa-fixes-log-<lang>-general.md` (the fixes applied: en D3→4, zh D3→4, vi D4→5, hi D4→5)

**Word lists** — `0-INBOX/AI_translation/keyword-extraction-dharmamitra/`; its `00-INDEX.md` says what each file
is. English: `en/en-bo-en-termbase-general.json`. Chinese, Vietnamese and Hindi: `zh/zh-decisions-general.json`,
`vi/vi-decisions-general.json`, `hi/hi-decisions-general.json`, `ne/ne-decisions-general.json` (the files to edit) and `zh/termbase-zh-general.md`,
`vi/termbase-vi-general.md`, `hi/termbase-hi-general.md` (to review). All languages in one table:
`standardised-keywords-general.md`.

## Machine drafts — raw, not for use

| Folder | Language | What it is | On the platform |
|---|---|---|---|
| `Dharmamitra/en/` | English | DharmaMitra zero-shot (draft 0) | yes (baseline) |
| `Dharmamitra/en-general/` | English | DharmaMitra primed with the English word list (draft 1 of en-general) | no |
| `Dharmamitra/zh/` | Chinese | DharmaMitra zero-shot (draft 0) | yes (baseline) |
| `Dharmamitra/zh-general/` | Chinese | DharmaMitra primed with the Chinese word list (draft 1 of zh-general) | no |
| `Gemini/vi/` | Vietnamese | Gemini zero-shot (draft 1 of vi-general) | yes (baseline) |
| `Gemini/hi/` | Hindi | Gemini zero-shot (draft 1 of hi-general) | yes (baseline) |
| `Gemini/ne/` | Nepali | Gemini zero-shot (draft 1 of ne-general) | yes (baseline) |
| `Gemini/ne-general/` | Nepali | Gemini primed with the Nepali word list (draft 2 of ne-general); `run-ne-general.sh` re-runs it | no |
| `Gemini/mn/` | Mongolian | Gemini zero-shot — the starting point for Mongolian | yes (baseline) |
| `Dharmamitra/en-commentaries/` | English | DharmaMitra zero-shot of the eight commentaries (not the root) | yes (2026-09-24) |
| `Dharmamitra/zh-commentaries/` | Chinese (Traditional) | DharmaMitra zero-shot of the eight commentaries (not the root) | yes (2026-09-24) |

These folders stay where they are, because the translation scripts write to these paths. Don't edit the files
by hand; a new run replaces them.
