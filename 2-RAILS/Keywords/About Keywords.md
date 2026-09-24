---
title: About Keywords
folder: 2-RAILS/Keywords
schema_owner: 4-SYSTEM/Skills/keyword-extract/SKILL.md
run: tara21-2026-08
run_date: 2026-08-19
promoted: 2026-09-22
terms_total: 367
queue_length: 114
gate_failures: 253
commentaries_measured: 16
status: descriptive-inventory
---

# 2-RAILS/Keywords — the source-term registry

This folder is the vault's **durable keyword layer**: which Tibetan terms this corpus is
about, what each one is called in English, how often each occurs where, and which ones carry
enough commentarial attention to support an article. It exists so that the keyword pipeline
is **run once and read many times** — the same reason `Claims/` and `Sections/Raw/toc-tree/`
exist. Nothing downstream should re-derive keywords; it should read these files.

Written and overwritten by [`keyword-extract`](../../4-SYSTEM/Skills/keyword-extract/SKILL.md)
(`$KEYWORDS` in `4-SYSTEM/Skills/_shared/PROFILES.md`). Read by
[`graded-translate`](../../4-SYSTEM/Skills/graded-translate/SKILL.md),
[`term-definition`](../../4-SYSTEM/Skills/term-definition/SKILL.md),
[`term-localization`](../../4-SYSTEM/Skills/term-localization/SKILL.md),
[`dharmamitra-termlocked`](../../4-SYSTEM/Skills/dharmamitra-termlocked/SKILL.md) and
[`article-subject-filter`](../../4-SYSTEM/Skills/article-subject-filter/SKILL.md).

## What this layer is *not*

**These files are not citation-chain rails.** They are descriptive inventories over the
corpus — counts, ranks and gate verdicts — and they carry no per-item `1-SOURCES/` citation.
A `3-TRANSFORMATIONS/` output may not cite a keyword file as its ground for a claim; it cites
`Claims/`, `Verses/` or `Local-Wiki/`. What this layer legitimately governs is **vocabulary**:
which term is which, and which rendering is locked for it.

The boundary rule from
[`keyword-extraction-methodology.md`](../../4-SYSTEM/Guidelines/keyword-extraction-methodology.md)
§1 still holds: *keywords select and order publication; they never define the consolidation
topic space.*

## Files

| File | Schema | Holds |
|---|---|---|
| `source-term-registry.json` | `source-term-registry/1` | 367 terms — canonical lemma per concept, variants, English renderings, root-text blocks |
| `frequency-matrix.json` | `frequency-matrix/1` | quote-excluded counts across the root text and 16 commentaries, plus spread |
| `article-queue.json` | `article-queue/1` | 114 terms passing the viability gate, ordered by composite score, plus 253 recorded gate failures |
| `article-subjects.json` | `article-subjects/1` | 101 subjects after the standalone / section-material / glossary verdict and the merge pass |

### `id`, `lemma`, `match_form` — read this before matching anything

- **`lemma`** is the canonical form and the real key: `སྒྲོལ་མ།`, with a trailing shad.
- **`match_form`** is the same term with the shad converted to a tsheg: `སྒྲོལ་མ་`. **This is
  the form to string-match against running Tibetan.** Matching the bare lemma against the root
  text hits 74 of 370 terms; `match_form` hits 348. Any tool that feeds this registry into a
  glossary, a counter or a translation prompt must use `match_form`, or it will silently drop
  four fifths of the vocabulary and look like it worked.
- **`id`** is `t-<sha1(lemma)[:8]>` — a pure function of the lemma, so it is stable across
  re-runs forever, as `keyword-extract` Phase 3 Rule 4 requires. `slug` is a readable,
  gloss-derived label and is advisory: it may change, `id` may not.

## Known gaps in the tara21-2026-08 run

Carried forward honestly rather than backfilled by guesswork:

1. **No `synonyms` or `epithets`** — `keyword-extract` Phase 3c was not part of the 2026-08
   run. Both fields are present and empty.
2. **No `dropped: true` rows** — the particle filter ran before ranking and its audit trail
   was not preserved, so the registry cannot show which candidates were filtered and why.
   Phase 3 Rule 3 requires that trail from the next run on.
3. **Quote exclusion was similarity-based, not tag-based** — the commentaries carried no
   transclusion anchors in August. The ten files in `1-SOURCES/Commentaries/New raw data/`
   now do. Re-running Phase 4 against those will give tag-exact counts.

## Top 60 of the article queue

Full list in `article-queue.json`; `freq` is root + commentary occurrences, quote-excluded.

| # | Lemma | Match form | English renderings | Claims | Spread | Freq | Composite |
|---|---|---|---|---|---|---|---|
| 1 | སྒྲོལ་མ། | `སྒྲོལ་མ་` | liberates, tara | 453 | 16 | 808 | 0.772 |
| 2 | རིམས། | `རིམས་` | disease, diseases, infectious | 57 | 16 | 67 | 0.545 |
| 3 | རྨི་ལམ། | `རྨི་ལམ་` | dreams | 38 | 16 | 42 | 0.532 |
| 4 | ཞི་བ། | `ཞི་བ་` | pacification, pacifying | 47 | 15 | 249 | 0.529 |
| 5 | བདུད། | `བདུད་` | maras | 56 | 16 | 185 | 0.525 |
| 6 | གདོན། | `གདོན་` | demon, demons | 58 | 16 | 97 | 0.522 |
| 7 | མྱུར་མ། | `མྱུར་མ་` | swift | 48 | 16 | 55 | 0.507 |
| 8 | རྩོད། | `རྩོད་` | conflicts | 32 | 15 | 40 | 0.504 |
| 9 | ཉི་ཤུ་རྩ་གཅིག། | `ཉི་ཤུ་རྩ་གཅིག་` | twenty-one | 77 | 16 | 54 | 0.500 |
| 10 | ཞལ། | `ཞལ་` | face | 35 | 14 | 248 | 0.500 |
| 11 | ཟླ་བ། | `ཟླ་བ་` | moon, moons | 117 | 15 | 221 | 0.494 |
| 12 | བསྟོད་པ། | `བསྟོད་པ་` | praise | 47 | 12 | 406 | 0.493 |
| 13 | དབུ་རྒྱན། | `དབུ་རྒྱན་` | crown ornament, crown-ornament | 50 | 16 | 56 | 0.492 |
| 14 | གཙུག་ཏོར། | `གཙུག་ཏོར་` | crown, protrusion | 39 | 16 | 41 | 0.491 |
| 15 | དུག། | `དུག་` | poison, poisons, son | 56 | 14 | 215 | 0.490 |
| 16 | ཏུ་རེ། | `ཏུ་རེ་` | king, ture | 83 | 16 | 96 | 0.486 |
| 17 | ཕྱག་འཚལ། | `ཕྱག་འཚལ་` | homage | 86 | 12 | 613 | 0.484 |
| 18 | འོད། | `འོད་` | light | 66 | 14 | 457 | 0.480 |
| 19 | དཔའ་མོ། | `དཔའ་མོ་` | heroine, heroine eye | 35 | 15 | 42 | 0.480 |
| 20 | ཞབས། | `ཞབས་` | feet, foot | 101 | 16 | 221 | 0.475 |
| 21 | སྡིག་པ། | `སྡིག་པ་` | actions, negative, negativity | 42 | 16 | 76 | 0.473 |
| 22 | དཀོན་མཆོག་གསུམ། | `དཀོན་མཆོག་གསུམ་` | jewels | 62 | 16 | 49 | 0.469 |
| 23 | ཧཱུྃ། | `ཧཱུྃ་` | hum | 47 | 12 | 87 | 0.469 |
| 24 | འཕགས་མ། | `འཕགས་མ་` | lady, noble, noble lady | 132 | 13 | 252 | 0.467 |
| 25 | ཁྲོ་གཉེར། | `ཁྲོ་གཉེར་` | frown, frowning, wrathful | 57 | 16 | 74 | 0.467 |
| 26 | རོ་ལངས། | `རོ་ལངས་` | vetalas, zombies | 44 | 14 | 48 | 0.467 |
| 27 | སྔགས། | `སྔགས་` | mantra | 63 | 12 | 450 | 0.463 |
| 28 | ཉི་མ། | `ཉི་མ་` | sun | 48 | 16 | 114 | 0.462 |
| 29 | འཇིགས་པ། | `འཇིགས་པ་` | terrifier | 31 | 13 | 176 | 0.461 |
| 30 | འཁོར་ལོ། | `འཁོར་ལོ་` | wheel | 44 | 16 | 96 | 0.460 |
| 31 | སྔོ། | `སྔོ་` | blue | 24 | 14 | 108 | 0.457 |
| 32 | ཞི་མ། | `ཞི་མ་` | peaceful | 41 | 16 | 71 | 0.456 |
| 33 | བརྒྱ་བྱིན། | `བརྒྱ་བྱིན་` | indra | 45 | 16 | 48 | 0.453 |
| 34 | བདེ་མ། | `བདེ་མ་` | blissful | 32 | 16 | 38 | 0.449 |
| 35 | རྒྱལ་བ། | `རྒྱལ་བ་` | conqueror, conquerors | 23 | 13 | 205 | 0.448 |
| 36 | ཕྱག་འཚལ་བ། | `ཕྱག་འཚལ་བ་` | homage, homages | 91 | 14 | 174 | 0.444 |
| 37 | གསེར། | `གསེར་` | golden | 35 | 14 | 61 | 0.440 |
| 38 | ཐུགས་ཀ། | `ཐུགས་ཀ་` | heart | 50 | 16 | 129 | 0.438 |
| 39 | ཕྱག་རྒྱ། | `ཕྱག་རྒྱ་` | mudra | 58 | 16 | 101 | 0.438 |
| 40 | སྤྱན། | `སྤྱན་` | eye, eyes, heroine eye | 42 | 16 | 156 | 0.435 |
| 41 | པདྨ། | `པདྨ་` | lotus | 113 | 15 | 148 | 0.431 |
| 42 | འཇིག་རྟེན་གསུམ། | `འཇིག་རྟེན་གསུམ་` | world arise | 37 | 12 | 78 | 0.431 |
| 43 | ས་གཞི། | `ས་གཞི་` | earth | 35 | 15 | 55 | 0.430 |
| 44 | ཕྱོགས། | `ཕྱོགས་` | direction, directions | 30 | 13 | 254 | 0.429 |
| 45 | ཚངས་པ། | `ཚངས་པ་` | brahma | 43 | 16 | 47 | 0.426 |
| 46 | དགེ་མ། | `དགེ་མ་` | virtuous | 34 | 16 | 37 | 0.424 |
| 47 | གཡོན། | `གཡོན་` | leave, left | 50 | 11 | 193 | 0.424 |
| 48 | སྡུག་བསྔལ། | `སྡུག་བསྔལ་` | sufferings | 32 | 13 | 167 | 0.424 |
| 49 | གཡས། | `གཡས་` | right | 46 | 11 | 189 | 0.421 |
| 50 | བསྐལ་པ། | `བསྐལ་པ་` | eon | 24 | 15 | 26 | 0.420 |
| 51 | མེ་ལྷ། | `མེ་ལྷ་` | agni | 26 | 16 | 23 | 0.419 |
| 52 | དྲི་ཟ། | `དྲི་ཟ་` | gandharvas | 25 | 16 | 26 | 0.418 |
| 53 | རྗེ་བཙུན་མ། | `རྗེ་བཙུན་མ་` | venerable | 49 | 14 | 170 | 0.417 |
| 54 | དེ་བཞིན་གཤེགས་པ། | `དེ་བཞིན་གཤེགས་པ་` | tathagata | 29 | 16 | 36 | 0.416 |
| 55 | གནོད་སྦྱིན། | `གནོད་སྦྱིན་` | yaksha, yakshas | 56 | 16 | 57 | 0.414 |
| 56 | ཕྱག། | `ཕྱག་` | hand | 25 | 9 | 1091 | 0.412 |
| 57 | ལྷ། | `ལྷ་` | celestial, god, gods | 26 | 10 | 685 | 0.412 |
| 58 | རི་རབ། | `རི་རབ་` | meru | 43 | 16 | 46 | 0.405 |
| 59 | ཡི་གེ་བཅུ་པའི། | `ཡི་གེ་བཅུ་པའི་` | syllables | 50 | 16 | 30 | 0.404 |
| 60 | ཕོངས་པ། | `ཕོངས་པ་` | poverty | 30 | 14 | 30 | 0.396 |
