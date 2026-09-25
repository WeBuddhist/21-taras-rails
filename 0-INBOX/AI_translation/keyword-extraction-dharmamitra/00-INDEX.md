---
title: Keywords folder — what's here
file_type: index
updated: 2026-09-24
---

# Keywords folder — what's here

The word-list work behind the translations: which Tibetan words are locked, and the one approved rendering for
each in every language. The translations themselves are in
[[3-TRANSFORMATIONS/Translations/00-INDEX-current-translations|3-TRANSFORMATIONS/Translations]].

**Edit** = change a decision here. **Read** = the file for a person to review. **Built** = made by a script;
don't edit it by hand, rebuild it.

## Start here

**`standardised-keywords-general.md`** has all standardised keywords in one table: the Tibetan term and its
locked English, Chinese, Vietnamese, Hindi and Nepali renderings, with the verses (52 terms). It is built from the word lists
below; to rebuild it after a change:

```bash
K=0-INBOX/AI_translation/keyword-extraction-dharmamitra
python3 ../Webuddhist-Skills/rails/keyword-standardize/scripts/multilingual_table.py \
  --base $K/en/en-bo-en-termbase-general.json \
  --lang zh=$K/zh/en-bo-zh-termbase-general.json --lang vi=$K/vi/en-bo-vi-termbase-general.json \
  --lang hi=$K/hi/en-bo-hi-termbase-general.json --lang ne=$K/ne/en-bo-ne-termbase-general.json \
  --title "Praise to the Twenty-One Tārās" -o $K/standardised-keywords-general.md
```

## `en/` — English (general)

| File | What | |
|---|---|---|
| `en-bo-en-termbase-general.json` | English word list: 47 locked Tibetan terms with verse scopes and notes. It is also the Tibetan side every other language reuses | **Edit** |
| `bo_en_keyword_general.json` | Per-verse keywords and Tibetan text; `en_text` = English draft 2 | Edit with care |
| `en-bo-en-termbase-general.archived-entries.json` | Entries removed from the word list, kept rather than deleted | Archive |
| `glossary-en-general.tsv` | The word list in DharmaMitra's format, as used for English draft 1 | Historical |
| `notes/termbase-candidate.md`, `notes/dropped-keywords.md` | Working notes from building the first list | Notes |

## `zh/` — Chinese (general, Traditional)

| File | What | |
|---|---|---|
| `zh-decisions-general.json` | **The one file to edit**: each Chinese word with its source and reason | **Edit** |
| `termbase-zh-general.md` | Review table, with the 14 flagged picks first — start here | **Read** |
| `en-bo-zh-termbase-general.json` | Chinese word list | Built |
| `bo_zh_keyword_general.json` | Per-verse keywords; `zh_text` = Chinese draft 2 (kept on rebuild) | Built |
| `glossary-zh-general.tsv` | For DharmaMitra (verse-scoped), as used for Chinese draft 1 | Built |
| `zh-worksheet-general.md` | Evidence per term and verse | Built |
| `references/zh-classical-T1108B.md` | Classical Chinese version (CBETA T1108B), aligned to our verses — vocabulary evidence only | Reference |

After editing `zh-decisions-general.json`, rebuild from the vault root:

```bash
K=0-INBOX/AI_translation/keyword-extraction-dharmamitra
python3 ../Webuddhist-Skills/rails/keyword-standardize/scripts/build_termbase.py \
  --decisions $K/zh/zh-decisions-general.json \
  --base-termbase $K/en/en-bo-en-termbase-general.json --base-grade-file $K/en/bo_en_keyword_general.json \
  --meaning-text "3-TRANSFORMATIONS/Translations/en-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general.md" \
  --reference $K/zh/references/zh-classical-T1108B.md \
  --mt-draft "3-TRANSFORMATIONS/Translations/Dharmamitra/zh/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh.md" \
  --out-dir $K/zh --force
```

## `vi/` — Vietnamese (general)

| File | What | |
|---|---|---|
| `vi-decisions-general.json` | **The one file to edit**: each Vietnamese word with its source and reason | **Edit** |
| `termbase-vi-general.md` | Review table, with the 14 flagged picks first — start here | **Read** |
| `en-bo-vi-termbase-general.json`, `bo_vi_keyword_general.json`, `glossary-vi-general.tsv`, `vi-worksheet-general.md` | Built, the same as for Chinese | Built |

Rebuild: the same command as for Chinese, with `vi/vi-decisions-general.json`, `--out-dir $K/vi`, and the
Gemini draft (`3-TRANSFORMATIONS/Translations/Gemini/vi/…-vi.md`) as `--mt-draft`. Use no `--reference`: the
Chinese reference is shown in the worksheet only.

## `hi/` — Hindi (general)

| File | What | |
|---|---|---|
| `hi-decisions-general.json` | **The one file to edit**: each Hindi word with its source and reason | **Edit** |
| `termbase-hi-general.md` | Review table, with the 7 flagged picks first — start here | **Read** |
| `en-bo-hi-termbase-general.json`, `bo_hi_keyword_general.json` (`hi_text` = Hindi draft 2), `glossary-hi-general.tsv`, `hi-worksheet-general.md` | Built, the same as for Chinese | Built |

Rebuild: the same command as for Chinese, with `hi/hi-decisions-general.json`, `--out-dir $K/hi`, the Gemini
draft (`3-TRANSFORMATIONS/Translations/Gemini/hi/…-hi.md`) as `--mt-draft`, and no `--reference` (Hindi uses
the Sanskrit terms directly).

## `ne/` — Nepali (general)

| File | What | |
|---|---|---|
| `ne-decisions-general.json` | **The one file to edit**: each Nepali word with its source and reason (`hint` = the whole word sent to Gemini where the lock is a stem) | **Edit** |
| `termbase-ne-general.md` | Review table, with the 7 flagged picks first — start here | **Read** |
| `en-bo-ne-termbase-general.json`, `bo_ne_keyword_general.json` (`ne_text` = Nepali draft 3), `glossary-ne-general.tsv`, `ne-worksheet-general.md` | Built | Built |

Rebuild: as for Hindi, with `ne/…`, `--mt-draft 3-TRANSFORMATIONS/Translations/Gemini/ne/…-ne.md`. The Hindi translation
is the reference shown in the worksheet (`--reference … --reference-prefix ""`), not passed to the build.

## `shared/` — keyword extraction (used by every language)

| File | What |
|---|---|
| `bo-tara21-dharmamitra-en_bo_keyword_meaning_enriched.json` | `keyword-extract` output: ranked keywords, each matched to the Tibetan it renders |
| `tfidf/` | TF-IDF runs behind the ranking |

## Top level

- `STATE.md`: running log of every step, in order. The older entries use the file paths from before this reorganisation.
- A new language gets its own folder beside `en/`, `zh/`, `vi/`, `hi/` and `ne/` (e.g. `mn/`).
