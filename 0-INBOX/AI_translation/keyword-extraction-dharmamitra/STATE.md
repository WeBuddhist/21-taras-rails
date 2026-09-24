---
title: "Keyword extraction — Dharmamitra track (translation pipeline, not article ranking)"
generated: 2026-09-24
source: 3-TRANSFORMATIONS/Translations/Dharmamitra/en/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en.md
status: draft — awaiting human review before feeding graded-translate Phase 1
---

# Keyword extraction — Dharmamitra track

## Why this run exists, and how it differs from the earlier one

`0-INBOX/AI_translation/keyword-extraction/` (the earlier run) used the **Gemini
zero-shot literal draft** as its Step 0 input, and ran the full 6-step pipeline
to rank ~367 terms for **Wikipedia article ordering** (structural signal,
per-commentary claim-density, composite score).

This run is narrower and serves a **different goal**: building the termbase for
Tenkal's English translation pipeline (Dharmamitra draft -> keyword extraction ->
Tibetan pairing -> standardize -> term-locked second draft -> commentary
fact-check -> publish). It uses the **Dharmamitra machine-baseline draft** as
the real first draft, and stops after keyword-extract's Mode 1 (Steps 1-3) —
it does not re-run the structural/claim-density ranking, which isn't needed for
a termbase.

## What was run

1. `keyword-extract/scripts/keywords.py` (YAKE + spaCy) against the Dharmamitra
   draft. Output landed in `Webuddhist-Skills/rails/keyword-extract/scripts/output/`
   (that repo's own scratch dir) — only the verse-keyed file
   (`*-keyword_verses_yake.json`) was used; the corpus-level `*-keywords.md` /
   `*-raw.json` / `*-normalized.json` files are **not usable as-is**: the
   script's `__main__` block doesn't strip YAML frontmatter before running
   corpus-level YAKE, so they're contaminated with frontmatter noise
   ("payload chars style", "dharmamitra cat translate", etc.). Worth a fix
   upstream in Webuddhist-Skills if the corpus-level report is ever needed.
2. Step 3 (Tibetan enrichment), done directly (no API) against the aligned
   root text (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), verse by verse,
   all 34 blocks.

## Output

- `bo-tara21-dharmamitra-en_bo_keyword_meaning_enriched.json` — the
  `keyword-extract` Mode 1 output contract: `{verse_id: {text, keywords:
  [{key, rank, score, count, bo?, note?}]}}`. A `note` field flags anything
  uncertain instead of a silent guess, per the skill's own instruction.
- `termbase-candidate.md` — the same data regrouped by **Tibetan term**
  (84 unique terms), each with every English rendering seen and which verses
  it occurs in. This is the natural input to Step 4 (standardize) — one row
  per term is one decision to make.

## Known quality issues in the raw YAKE output

This is a 21-verse formulaic praise (every homage stanza opens with the same
word), which is a poor match for a statistical keyword ranker built for
longer, more varied prose. Flagged rather than silently smoothed over:

- **"homage"** (ཕྱག་འཚལ) was flagged as a keyword in nearly every verse — it's
  a real, correctly-consistent term, just not a *distinguishing* one. Belongs
  in the termbase once, not verse-by-verse.
- **`1-14`'s "face"** has no counterpart in that verse's English or Tibetan —
  most likely a keyword-boundary artifact from adjacent-verse bleed in the
  parser. Recommend dropping it rather than forcing a mapping.
- **Termbase drift already visible**, worth resolving at Step 4:
  - "spirit" renders **two different Tibetan words**: འབྱུང་པོ (1-6, elemental
    spirit/bhūta) vs. གདོན (1-21, 2-5, a possessing/malevolent spirit).
  - "goddess" renders **two different Tibetan words**: ལྷ་མོ (2-1, generic
    "goddess") vs. བཅོམ་ལྡན་འདས་མ (a-1, the title "Blessed One" — this is
    arguably mistranslated as "goddess" rather than a title).
  - "power" renders **three different Tibetan words**: དབང (1-10, 2-3),
    ནུས (1-11), མཐུ (1-21) — genuinely different senses (authority/ability/
    strength), so this may not need forcing to one English word.
  - "mantra" appears as a paraphrase of ངག ("speech", 1-16) in one verse and
    as the literal སྔགས in another (1-22).
  - "exception" renders two near-synonymous but different phrases: མ་ལུས
    (1-4, 1-8) vs. ལུས་པ་མེད་པར (1-5).

## Next step

Human review of `termbase-candidate.md` (this is the Step 6-equivalent gate —
nothing downstream should consume it unreviewed), then feed the approved
renderings into `graded-translate` Phase 1 to build
`en-bo-en-termbase-general.json` for the second, term-locked translation draft.

---

## Phase 1 complete — `graded-translate`, target `en`, grade `general`

Run 2026-09-24, no attested translation (built purely from the Dharmamitra
draft + this run's own enriched keywords, per instruction).

**Files:**
- `en-bo-en-termbase-general.json` — 46 locked terms, each with its Tibetan
  form(s), the standardized English rendering, best rank, and every verse it
  occurs in.
- `bo_en_keyword_general.json` — the grade file: all 34 verses, each with
  `text` (Dharmamitra English, unchanged), `bo_text` (aligned Tibetan lines),
  `en_text` (empty — Phase 2 fills this with the term-locked retranslation),
  and its surviving locked keywords.
- `dropped-keywords.md` — 27 keyword occurrences deliberately excluded, with
  reasons (grammatical intensifiers left free rather than force-locked;
  heading/meta paraphrase; one likely parser artifact at 1-14 "face").

**Standardization decisions made in place of an attested translation** (these
are real judgment calls — flag for human sign-off before Phase 2 runs):

- **"spirit" split in two**: འབྱུང་པོ (1-6) -> "spirits", གདོན (1-21, 2-5) ->
  "demons". The Dharmamitra draft used "spirit" for both.
- **"goddess" corrected for the colophon**: བཅོམ་ལྡན་འདས་མ (a-1) -> "the
  Blessed One" (a title), not "goddess" — ལྷ་མོ (2-1) keeps "goddess".
- **"power" split in three**: དབང (1-10/2-3) -> "power", ནུས (1-11) ->
  "ability", མཐུ (1-21) -> "might".
- **TUTTĀRA/TUTTĀRE spelling fixed**: same Tibetan word throughout; locked to
  TUTTĀRE (matches the standard mantra oṃ tāre tuttāre ture svāhā). 1-5 is
  the verse that needs correcting.
- **"mantra" standardized**: the literal སྔགས (1-22) and the 1-16 paraphrase
  "ten-syllable speech" both lock to "mantra".
- **"light" vs "lightning"**: འོད -> "light" throughout except 1-1's གློག
  ("flash of lightning") -> "lightning", previously conflated.
- Grammatical intensifiers (རྣམ་པར / རབ་ཏུ / ཀུན་ནས / ཐམས་ཅད, all loosely
  "complete/completely/utterly") were deliberately left **unlocked** —
  forcing one English word onto four different Tibetan intensifiers would
  hurt the prose more than it would help consistency.

**Completion check:** every verse has `bo_text`; every termbase entry has a
non-empty `en`; files reloaded and parse cleanly.

**Not yet done:** Phase 2 (translate `bo_text` into `en_text` at general
register, terms locked) and Phase 3 (drift check). Both need a go-ahead —
Phase 2 in particular means producing a fresh translation from the Tibetan
rather than regrading the Dharmamitra English, per the user's own pipeline
plan (step 5).
