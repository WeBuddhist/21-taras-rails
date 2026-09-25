---
title: "Commentaries on the Praise to the Twenty-One Tārās — DharmaMitra zero-shot (modern chinese)"
track_type: machine-baseline
target_language: modern chinese
lang_tag: zh
translation_of: "1-SOURCES/Commentaries/New raw data/ (eight commentaries)"
generator: dharmamitra cat-translate v1
endpoint: https://dharmamitra.org/api-search/cat-translate/v1/translate
rails_used: none
termbase: none
status: draft
seeded: 2026-09-24
---

# zh-commentaries — about this track

A **machine baseline**, not a rails-governed translation track: raw DharmaMitra `cat-translate` output for eight
Tibetan commentaries on the Praise to the Twenty-One Tārās, one file per commentary, block-ID aligned to the
source, with a transclusion of each Tibetan commentary block above its translation. No termbase, no rails, no
human review; not eligible for `status: complete` or to be cited by any other transformation.

It is kept apart from `../zh/` because that track's `style.md` is written for the root verse (line-by-line
verse); commentary is prose and needs its own instruction.

## Files

| File | Role |
| --- | --- |
| `style.md` | `style_instruction` for body blocks, sent verbatim. |
| `heading-style.md` | `style_instruction` for the sa-bcad headings (`--headings --heading-batch 8`). |
| `context-header.md` | Work-neutral preamble; each call appends the text's own `Work:` line. |
| `work/<stem>-zh.jsonl` | Append-only ledger per commentary. |
| `work/extra-fm-<stem>.json` | Seeded frontmatter: target-language `title`, `title_original`, `title_source`. |
| `<stem>-zh.md` | Rendered translation. `translation_of_text_id` / `translation_of_edition_id` are the commentary's WeBuddhist ids, copied from its own frontmatter. |

## Sources

Tenga Tulku, Karma Maitri, Tāranātha, Ngulchu Dharmabhadra, Pema Namgyal, Gendun Drub, Drakpa Gyaltsen,
Sangye Nyenpa — `1-SOURCES/Commentaries/New raw data/bo-<author>.md`. (The two Khenpo Tsulnam files there
have no block IDs yet and are not translated.)

Regenerate or resume one text:

```bash
python3 ../Webuddhist-Skills/rails/machine-translate/scripts/dm_translate.py --source "<source>" --lang "modern chinese" --out 3-TRANSFORMATIONS/Translations/machine-drafts/commentaries/dharmamitra-zh --extra-fm 3-TRANSFORMATIONS/Translations/machine-drafts/commentaries/dharmamitra-zh/work/extra-fm-<stem>.json
python3 ../Webuddhist-Skills/rails/machine-translate/scripts/dm_translate.py --source "<source>" --lang "modern chinese" --out 3-TRANSFORMATIONS/Translations/machine-drafts/commentaries/dharmamitra-zh --extra-fm 3-TRANSFORMATIONS/Translations/machine-drafts/commentaries/dharmamitra-zh/work/extra-fm-<stem>.json --headings --heading-batch 8 --heading-style "$(cat 3-TRANSFORMATIONS/Translations/machine-drafts/commentaries/dharmamitra-zh/heading-style.md)"
```

## Run history

- **2026-09-24** — all 8 commentaries, 510/510 blocks and 271/271 headings (headings 8 per call). Block IDs match
  each source one-for-one; no marker fallbacks; no line-count divergences; no `[[n]]` or `*[not yet translated]*`
  left. `status: draft`, not uploaded.
- Review notes (zh): register leans literary (此句之義為……之故) rather than plain modern; a few Wylie/Sanskrit glosses
  kept in brackets. (The three Tibetan-script quotations and the Tāranātha ^3-10 三摩地 gloss were fixed in the review pass.)
- **2026-09-24 (titles)** — four zh titles re-run through DharmaMitra with a stricter title instruction: Karma Maitri
  (name now in Chinese, 噶瑪彌怛), Dharmabhadra (utpala 優缽羅, was 優曇華 = udumbara), Drakpa Gyaltsen (明亮光芒),
  Sangye Nyenpa (聖救度母加持驟雨…; the earlier 甘露 was not in the Tibetan). Payloads rebuilt.
- **2026-09-24 (review)** — `translation-alignment-check` fixes, all at the ledger (`--force --only`) and re-rendered:
  line-count re-runs for 8 quoted-verse blocks (en: Tenga Tulku ^2-9 ^3-2, Dharmabhadra ^3-2, Pema Namgyal ^II-15,
  Sangye Nyenpa ^1-44; zh: Dharmabhadra ^2-2 ^3-14, Sangye Nyenpa ^1-66), each sent with its line count stated;
  58 en headings re-run under a heading style that forbids leading digits; 3 zh blocks re-run without Tibetan script
  (Tāranātha ^3-10, Dharmabhadra ^2-42, Sangye Nyenpa ^1-9). Markdown emphasis (`*term*`) is stripped at render time.
  Lint + parse payloads built for all 16 (`4-SYSTEM/scripts/parser-root-text/output/<stem>/`); refs equal the live
  commentary editions, alignment identity, TOC = source headings. Remaining checker flag "TOC leaked into content" is a
  false positive for commentaries (heading words recur naturally in the text; the Tibetan sources carry the same flags).
  Not uploaded.
