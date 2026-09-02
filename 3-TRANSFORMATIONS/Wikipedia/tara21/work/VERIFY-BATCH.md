# Verification batch — deterministic gate only (v2 adapter)

corpus `tara21` term-articles/ + slot-articles/ · 65 drafted articles (42 term, 23 slot) · no LLM, no network.

This report is produced by a scratch adapter script, not by the pipeline's own `scripts/verify_batch.py` (which still reads the stale, disconnected `3-TRANSFORMATIONS/Wikipedia/tara21/articles/` corpus format). It reuses the pipeline's own `kangyur_wiki.wiki.validator.validate()` and `kangyur_wiki.tibetan.verify.check_quote()` but reads directly from each topic's `article.md` (the ```wikitext fence) and `citations.md` (the ## Verification-ish section's audit table). See the script's own docstring for exactly how quotation/source pairs are recovered from citations.md's ~60 differently-worded table formats.

- **216 of 216 quotations (100.0%) appear character-for-character in the commentary they cite.**
- 54 of 65 articles carry no validator error and no hard error.
- validator errors by rule (total findings, not article count): V10×7, V2×14, V7×2, V8×5
- topics skipped outright: hara (stub, no wikitext fence)

## Term articles (42)

- **128 of 128 quotations (100.0%) verified character-for-character** against the commentary source they cite.
- 37 of 42 articles carry no validator error and no hard error.
- validator errors by rule (total findings, not article count): V2×1, V7×1, V8×4
- 5 article(s) flagged for manual review: the wikitext contains quotation marks but no (quotation, source) pair could be parsed out of citations.md — see below.

| article | quotes verified | validator errors | rules | notes |
|---|---|---|---|---|
| agni | 2/2 | 0 | — |  |
| amitabha | 2/2 | 0 | — |  |
| asceticism | 2/2 | 0 | — |  |
| bhuta | 3/3 | 0 | — |  |
| brahma | 2/2 | 0 | — |  |
| buddha | 2/2 | 0 | — |  |
| conqueror | 2/2 | 0 | — |  |
| dana | 2/2 | 0 | — |  |
| deva | 2/2 | 0 | — |  |
| dhyana | 2/2 | 0 | — |  |
| eon | 2/2 | 0 | — |  |
| gandharva | 1/1 | 0 | — |  |
| gdon | 20/20 | 0 | — |  |
| goddess | 0/0 | 0 | — | needs manual check |
| hum-syllable | 0/0 | 0 | — | needs manual check |
| indra | 2/2 | 0 | — |  |
| ishvara | 2/2 | 0 | — |  |
| kinnara | 2/2 | 0 | — |  |
| kshanti | 3/3 | 0 | — |  |
| lotus | 4/4 | 0 | — |  |
| mantra | 11/11 | 0 | — |  |
| mara | 3/3 | 2 | V2, V8 |  |
| meru | 2/2 | 0 | — |  |
| mudra | 2/2 | 0 | — |  |
| nirvana | 2/2 | 0 | — |  |
| obstacle | 4/4 | 0 | — |  |
| pacification | 1/1 | 1 | V7 |  |
| paramita | 3/3 | 0 | — |  |
| phat | 2/2 | 0 | — |  |
| suffering | 7/7 | 0 | — |  |
| svaha | 2/2 | 0 | — |  |
| tara-mantra | 3/3 | 1 | V8 |  |
| tathagata | 8/8 | 0 | — |  |
| three-jewels | 0/0 | 0 | — | needs manual check |
| three-worlds | 3/3 | 0 | — |  |
| ushnisha | 10/10 | 0 | — |  |
| vayu | 3/3 | 0 | — |  |
| vetala | 1/1 | 0 | — |  |
| vindhya | 2/2 | 0 | — |  |
| virya | 2/2 | 0 | — |  |
| wheel | 0/0 | 1 | V8 | needs manual check |
| yaksha | 0/0 | 1 | V8 | needs manual check |

## Slot articles (23)

- **88 of 88 quotations (100.0%) verified character-for-character** against the commentary source they cite.
- 17 of 23 articles carry no validator error and no hard error.
- validator errors by rule (total findings, not article count): V10×7, V2×13, V7×1, V8×1
- 1 article(s) flagged for manual review: the wikitext contains quotation marks but no (quotation, source) pair could be parsed out of citations.md — see below.

| article | quotes verified | validator errors | rules | notes |
|---|---|---|---|---|
| origin | 2/2 | 0 | — |  |
| structure-benefits | 4/4 | 2 | V2, V7 |  |
| tara-01 | 5/5 | 1 | V8 |  |
| tara-02 | 5/5 | 0 | — |  |
| tara-03 | 6/6 | 0 | — |  |
| tara-04 | 8/8 | 0 | — |  |
| tara-05 | 2/2 | 0 | — |  |
| tara-06 | 3/3 | 0 | — |  |
| tara-07 | 2/2 | 2 | V10 |  |
| tara-08 | 2/2 | 4 | V10 |  |
| tara-09 | 0/0 | 0 | — | needs manual check |
| tara-10 | 3/3 | 0 | — |  |
| tara-11 | 3/3 | 0 | — |  |
| tara-12 | 3/3 | 0 | — |  |
| tara-13 | 3/3 | 0 | — |  |
| tara-14 | 3/3 | 0 | — |  |
| tara-15 | 3/3 | 12 | V2 |  |
| tara-16 | 2/2 | 0 | — |  |
| tara-17 | 17/17 | 1 | V10 |  |
| tara-18 | 3/3 | 0 | — |  |
| tara-19 | 3/3 | 0 | — |  |
| tara-20 | 3/3 | 0 | — |  |
| tara-21 | 3/3 | 0 | — |  |

## Needs a human's attention — quotation marks present, no citation pair parsed

For these articles the wikitext body contains `"..."`-style quotation marks, but no live `(quotation, registered_id)` pair could be recovered from `citations.md`'s verification-ish table(s) — either the table has no column carrying the actual Tibetan quotation text (e.g. it records only a claim-id reference, as in `three-jewels`'s second table), or the retained quotation is described only in prose with no table row at all (e.g. `wheel`, `agni`-style narrative-only sections). Their quotations exist and may well be genuine, but this script did not verify them — a human should spot-check `article.md` against `citations.md` directly for these.

| article | kind |
|---|---|
| goddess | term |
| hum-syllable | term |
| three-jewels | term |
| wheel | term |
| yaksha | term |
| tara-09 | slot |

## Validator error detail

| article | kind | rule | message |
|---|---|---|---|
| mara | term | V2 | source 'utpala' is not declared in sources.yaml |
| mara | term | V8 | section 'བསྡུས་དོན།' has no citation — a section the sources do not support must not be written at all |
| pacification | term | V7 | category 'ཤེར་ཕྱིན།' is not on the allowlist; the live namespace contains misspellings and shad typos, so categories are curated, never invented |
| tara-mantra | term | V8 | section 'བསྡུས་དོན།' has no citation — a section the sources do not support must not be written at all |
| wheel | term | V8 | section 'བསྡུས་དོན།' has no citation — a section the sources do not support must not be written at all |
| yaksha | term | V8 | section 'བསྡུས་དོན།' has no citation — a section the sources do not support must not be written at all |
| structure-benefits | slot | V2 | source 'utpala' is not declared in sources.yaml |
| structure-benefits | slot | V7 | category 'བསྟན་བཅོས།' is not on the allowlist; the live namespace contains misspellings and shad typos, so categories are curated, never invented |
| tara-01 | slot | V8 | section 'བསྡུས་དོན།' has no citation — a section the sources do not support must not be written at all |
| tara-07 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — ས་བཅད་འདིའི་གྲངས་འཇོག'''ནི་འགྲེལ |
| tara-07 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — '''སྦས་དོན་གྱི་བཤད་པ'''ནི་མཁན་ཆ |
| tara-08 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — ཀྱི་དཔའ་བོའི་ངོས་འཛིན'''ནི། གོང་ |
| tara-08 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — གཉེར་གྱིས་གསོད་པའི་ཚད'''ནི། དགེ་ |
| tara-08 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — '''མཚན་གཞན་བཏགས་ཚུལ'''ནི། ཚིགས |
| tara-08 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — 'སྦས་དོན་གྱི་བཤད་ལུགས'''ནི། ཇོ་ན |
| tara-15 | slot | V2 | source 'utpala' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'gendundrub' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'sungrabtulku' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'tenzindhonzang' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'paldensherab' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'sangyenyentrul' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'tsultrimnamdak' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'tengatulku' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'drakpa' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'gendungyatso' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'konchok' is not declared in sources.yaml |
| tara-15 | slot | V2 | source 'pemanamgyal' is not declared in sources.yaml |
| tara-17 | slot | V10 | no tsheg (U+0F0B) at the ''' boundary — ་རེའི་ཞབས་ནི་བརྡབས་པས'''ནི་ སྒྲོ |

