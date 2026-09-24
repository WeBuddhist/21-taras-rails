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

---

## Attested-translation cross-check (Phase 1, Steps 3-4)

Checked all 46 termbase entries against `1-SOURCES/Translations/en-The Twenty-One
Praises to Tara.md` (colophon: adapted by Dzongsar Jamyang Khyentse Rinpoche from
a terma revealed by Chokgyur Dechen Lingpa, 2021) — a free, metrical translation,
not a literal one, so not every keyword has a clean 1:1 match. Per "attested beats
base beats invented," applied every clear, repeated match; logged the rest as
options rather than forcing them.

**Applied (strong, repeated evidence):**
- `Tārā` -> **`Tara`** — attested drops the macron consistently, 20+ occurrences.
- Mantra syllables switched from Dharmamitra's scholarly caps+diacritics to
  attested's plain lowercase, confirmed at every occurrence: `HŪṂ` -> **`hum`**,
  `TUTTĀRE` -> **`tuttare`** (this also resolves the earlier TUTTĀRA/TUTTĀRE
  spelling clash — attested is consistent where Dharmamitra wasn't), `PHAṬ` ->
  **`phat`**, `TRAṬ` -> **`trat`**, `TURE` -> **`ture`** (attested capitalizes
  "Ture" only when it's used as a direct epithet — "Supreme Ture," 1-21 — not
  as a mantra reference elsewhere; apply that contextually in Phase 2 rather
  than as a second locked term).
- `zombie` (རོ་ལངས) -> **`vetāla`** — attested explicitly uses "vetālas" (1-21).
- **`might`/`power`/`ability` collapsed from three words to two.** I'd
  originally locked three distinct English words for three distinct Tibetan
  words (དབང/ནུས/མཐུ), all glossed "power" in the Dharmamitra draft. Attested
  gave no clean support for a three-way split — it uses "power" for མཐུ too
  ("Commands all the power she needs," 1-21) — so `might` is now merged into
  `power`; `ability` (ནུས) stays separate, still unconfirmed either way.
- **`power` split by sense, confirmed.** 2-3's དབང ("Victors will confer
  ___") is the technical tantric-initiation sense — attested confirms with
  "receive abhishekas." Split into its own term, **`empowerment`**, separate
  from 1-10's general "power."

**Flagged, not applied — genuine open calls for you:**
- **`demon` (གདོན) -> `graha`?** Attested uses "grahas" (Sanskrit) at 1-21, but
  "evil" at 2-5 — not even self-consistent. "Graha" is a real but much less
  commonly known term than "demon" for a general-register audience; your call.
- **`goddess` (ལྷ་མོ, 2-1) -> `devi`?** Same trade-off — attested uses the
  Sanskrit "devi." Left as "goddess" for now.
- **1-16's "mantra"**: attested renders this literally as "your ten letters,"
  not "mantra." Dharmamitra already said "mantra" independently, so I kept the
  standardization, but attested doesn't support it — flagging rather than
  silently deciding.
- **`without_exception` (མ་ལུས / ལུས་པ་མེད་པར)**: attested renders this
  contextually — "without exception" at 1-5, but "completely" at 1-8 — rather
  than as one fixed phrase. Left it locked for consistency, but this is the
  kind of term where locking costs some of the naturalness a free translation
  has; worth knowing that trade-off is real here, not hypothetical.
- Several verbs vary in attested where I've locked one word — most visibly
  `destroy` (འཇོམས): attested uses "destroy," "destroys...completely,"
  "vanquish," "annihilates" across its four occurrences. That's the locking
  methodology's whole trade-off (consistency vs. natural variation), not a
  new finding, but worth restating now that there's a concrete comparison.

Files updated in place: `en-bo-en-termbase-general.json` (11 changes logged
per-entry under `attested_check`), `bo_en_keyword_general.json` (keyword
`term`/`en` fields re-synced to match).

---

## Flagged items resolved (my judgment, per user request)

Correction first: the previous section said "graha" and "devi" were flagged
but not applied. That was wrong — an earlier script actually did rename
`demon` -> `graha` in the termbase. Caught and reverted on review.

Decisions, applying one consistent rule: the **general** grade is an educated
general reader with common loanwords unglossed (karma, nirvana, bodhichitta —
the register table's own examples), not a Sanskrit-rich technical register
(that's what an **advanced** grade would be for).

- **`demon` (གདོན)** — kept, not `graha`. Attested's "graha" is a real Sanskrit
  astrological term but far less familiar than the register's own loanword
  examples, and attested isn't even consistent with it ("evil" at 2-5). Revisit
  for an advanced-grade termbase if one gets built.
- **`goddess` (ལྷ་མོ)** — kept, not `devi`, same reasoning.
- **`mantra` (1-16)** — kept, not attested's literal "ten letters." "Mantra"
  is immediately meaningful to a general reader; "ten letters" isn't
  self-explanatory out of context. Recommend Phase 2 write "the ten-syllable
  mantra" at 1-16 to preserve the numeral without losing clarity.
- **`vetāla`** (already applied last turn, not reopened) stays — that one was
  kept for accuracy (avoids "zombie"'s misleading horror-movie connotation),
  not familiarity, so the same general/advanced logic doesn't apply to it.

Both files updated; grade-file `graha` references retargeted to `demon`.

---

## TF-IDF pass (keyword-extract Mode 1, Step 2 — optional, run on request)

`generate_en_translation_idf.py` against the Dharmamitra draft, output in
`tfidf/`. Unlike `keywords.py`'s own `__main__` block, this script's
`tokenize()` does strip frontmatter correctly — output is clean, no
contamination this time.

Cross-checked its top 60 words against the 46-term locked termbase: strong
agreement (homage, Tara, hum, praise, hosts, destroy, syllable, blazing,
joy, ture, moon, endowed, lotus, world(s), light, peace, perfectly, spirits,
etc. all rank highly here too). Nothing in the gap list looks like a missed
content term — mostly plurals of terms already locked (syllables, zombies),
words already deliberately excluded (completely/utterly — the intensifiers),
or generic narrative nouns (eyes, fire, leg, wealth, child) not worth
locking. One candidate worth a look if the termbase gets extended: "yakṣa"
(gandharvas/yakṣas class of being) wasn't picked up by YAKE and isn't in
the current termbase at all.

---

## Added `yaksha` (manually, TF-IDF-sourced)

47th termbase entry. Missed by YAKE entirely; found via the TF-IDF pass
(rank 43). Occurs at 1-6 and 1-21. Locked to `yaksas` — the attested
translation's spelling, dropping the diacritic on the same reasoning already
applied to Tara/hum/tuttare/trat/phat/ture (general register, not scholarly
transliteration). Added to both files.

Small bug noted for the record: the TF-IDF script's tokenizer doesn't
recognize `ṣ` as a word character, so it split "yakṣas" into "yak" + "as"
instead of counting it as one word — that's why it took manual digging to
find rather than showing up cleanly in the report.

---

## Phase 2 — DharmaMitra draft + termbase enforcement (general grade) — DONE

**Network blocker along the way:** the sandboxed proxy this session runs
through (both the cloud workspace and the `device_bash` channel) rejects
`dharmamitra.org` with a 403 at the CONNECT level — an org/account network
policy, not a DharmaMitra problem. The user ran `dm_translate.py` directly
in their own Terminal (outside the sandboxed channel) instead, which reached
the API fine but then hit a local `SSL: CERTIFICATE_VERIFY_FAILED` (Python's
cert bundle wasn't wired up) — fixed with `pip3 install --upgrade certifi`
+ `export SSL_CERT_FILE=$(python3 -m certifi)`, then the real run succeeded:
32/32 blocks, 0 dropped, no `[[n]]` marker fallbacks, no `not yet translated`
gaps.

**What ran:**
1. Converted the 47-term termbase into `glossary-en-general.tsv` (70 lines —
   multi-form `bo` entries split into one line per surface form, since
   `dm_translate.py`'s glossary hit-check is a literal substring match).
2. `dm_translate.py --source ... --lang english --glossary glossary-en-general.tsv
   --out 3-TRANSFORMATIONS/Translations/Dharmamitra/en-general` — new track,
   kept separate from the original zero-shot `Dharmamitra/en/` baseline so
   neither gets overwritten. This raw output stays untouched (machine-baseline
   convention: never hand-edited) — headings weren't run (`--headings` needs
   the same blocked API access; left for the user if they want that specific
   baseline file's own heading fields filled).
3. Went block-by-block through all 32 translated verses against the 47-term
   termbase's `verse_ids`. 16 blocks needed a fix; 16 were already correct.
   Full before/after log kept in this session; the pattern was almost
   entirely DharmaMitra using the scholarly/diacritic spelling
   (TUTTĀRA/TUTTARE, HŪṂ, PHAṬ→PHAT, TRAṬ→TRAT, TURE, yakṣas, Tārā) where the
   general-grade termbase had already locked the plain attested-translation
   spelling (tuttare, hum, phat, trat, ture/Ture, yaksas, Tara) — exactly the
   drift the consistency pass exists to catch. Two substantive (non-spelling)
   fixes: 1-11 "power to summon" → "ability to summon" (ནུས, not དབང — the
   Dharmamitra draft flattened both to "power," the termbase's whole reason
   for splitting `ability` out); 1-6/1-21 "Zombies/zombies" → "Vetālas/vetālas"
   (རོ་ལངས is locked to `vetāla`, not the English gloss); 2-1 "Goddess" →
   "goddess" (lowercase, matching the plain-register choice over "Devi").
   Left two untouched on purpose as out-of-scope: `TĀRA` at 1-18 and `HARA`
   at 1-20 are real mantra-syllable words (ཏཱ་ར, ཧ་ར) but neither is one of
   the 47 locked terms, so no termbase basis to force a spelling on them —
   flagged here as an optional future addition, not applied unilaterally.
4. Filled `en_text` for all 34 tracked entries in
   `bo_en_keyword_general.json` (the grade file) with the corrected text.
   Section headings (I-0, 1-0, 2-0) used the grade file's own pre-existing
   `text` field verbatim rather than re-inventing a translation — it already
   read well ("Meaning of the Title and the Translator's Homage", "The
   Actual Praise", "The Benefits of the Praise"). The colophon heading
   (a-0) and verse 2-6 aren't tracked in the grade file at all (no keyword
   was ever extracted for either) — translated directly into the final
   markdown without a termbase basis, since neither needed one.
5. Wrote the actual Phase 2 deliverable — not a hand-edit of the raw
   baseline, a new file — to
   `3-TRANSFORMATIONS/Translations/en-general/bo-...-en-general.md`,
   transclusion layout, `track_type: graded`, `status: draft`,
   `rails_used: graded-translate (Phase 1, Phase 2)`. 32/32 blocks, 4/4
   headings, no leftover `[[n]]` markers or "not yet translated" gaps.

**Not done yet / explicitly out of scope for this pass:**
- `check_termbase_consistency.py` (graded-translate's own Phase 3 script)
  expects a `termbase.md` table and `2-RAILS/Verses/<id>.md` rail files with
  `concepts_in_verse` frontmatter — infrastructure this project never built
  (we used the lighter JSON termbase + grade file, appropriate for a single
  32-block text rather than a 900-verse corpus). Ran the equivalent check by
  hand instead (Step 3 above) rather than force-fitting that script's format.
- Commentary fact-check (pipeline Step 6 / the user's original step 6) —
  not started.
- `TĀRA` (1-18) and `HARA` (1-20) — real transliterated mantra syllables,
  currently left in DharmaMitra's own scholarly spelling; worth adding to
  the termbase if the user wants full consistency with tuttare/hum/phat/
  trat/ture's plain-spelling treatment.

---

## Commentary fact-check (Phase 1, report only) — Drakpa Gyaltsen — DONE

**Commentary inventory, corrected:** the earlier claim that none of the commentaries
were transcluded was wrong (only folder names had been checked). In
`1-SOURCES/Commentaries/New raw data/`, 8 of 10 files already carry
`![[root#^verse-id]]` markers that `extract_commentary.py` reads. All their verse IDs
exist in the root. The two Khenpo Tsultrim Namdak files have no markers or
frontmatter and still need transclusion. Sangye Nyenpa covers only 1-1 to 1-21.

**Source fix (user-approved):** Padma Namgyal line 264 was transcluded as `^2-2` but
its prose quotes verse 2-5 (between 2-4 and 2-6). Changed to `^2-5`. That is the only
edit made to `1-SOURCES/`.

**Run:** `commentary-fact-check` Phase 1 against Jetsün Drakpa Gyaltsen
(`bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md`), scope = all 30 verses it covers (I-3, 1-1 to 1-22,
2-1 to 2-6, a-1). The translation was not edited. Report:
`3-TRANSFORMATIONS/Translations/en-general/commentary-fact-check-report-drakpa-gyaltsen-en-general.md`.

**Result:** 17 clean, 7 with errors, 6 with mismatches only.
- Errors: 1-1 (lotus born from Avalokiteśvara's tears, not "lotus face"); 1-3
  ("austerity" = ethical discipline); 1-6 (one Maheśvara, not "various Īśvaras");
  1-8 ("Fearful" → she terrifies); 1-16 (*rig pa* = knowledge-mantra, not "awareness");
  1-17 (*'bigs byed* read as the verb "pierce", not the mountain Vindhya); 1-19 (the
  kings of the gods serve her; she isn't "the sovereign").
- The whole of chapter 2 and the colophon are clean.
- Two termbase issues surfaced: `supreme` used for ཤིན་ཏུ at 1-12, and `power` used
  for མཐུ at 1-21 (the termbase note itself says མཐུ = "might").
- The `lotus_face` lock is too broad: right at 1-8, wrong at 1-1 per this commentary.

**Tool limitation:** `extract_translation.py` captures only the last line of each
multi-line verse in the transclusion layout. The audit used the grade file's
`en_text` instead. Worth fixing upstream before this skill runs on other verse texts.

**Next:** Phase 2 (apply mechanical fixes only, log the judgment calls). Before
fixing 1-17 (Vindhya), cross-check a second commentary.

---

## Commentary fact-check across 4 commentaries (Phase 1, report only) — DONE

Added Gyalwa Gendun Drub, Tāranātha and Dorlob Tenga Tulku to the Drakpa Gyaltsen run.
One report each, plus `commentary-fact-check-consensus-en-general.md`, all in
`3-TRANSFORMATIONS/Translations/en-general/`. The translation has still not been edited.

Rule: fix when ≥3 of 4 say the English is wrong; translator's choice on a split; leave
single-commentary flags.

**Fix (11 items, 10 verses):** 1-1 lotus from tears/face (4/4); 1-3 austerity →
discipline (4/4); 1-3 wisdom missing from the six perfections (3/4); 1-5 realms, or keep
literal deliberately (3/4); 1-8 "Fearful" → Terrifying (3/3 that gloss it); 1-9 one wheel
on her palm (3/4); 1-10 the joy she brings (3/4); 1-16 knowledge-mantra, not "awareness"
(4/4); 1-17 Ture is her, not a syllable (3/3); 1-19 the kings serve her (4/4); 1-21 the
three suchnesses set on her, not "established by" (4/4).

**Split — translator's choice:** 1-3 whose colours; 1-8 ture as the one addressed;
1-8 "champions"; 1-14 "underworld"; 1-17 Vindhya vs "pierces" (2–2); 1-22 one praise
vs two.

**Dropped:** Drakpa Gyaltsen's 1-6 (singular Maheśvara) and 1-15 (order) flags —
the other three disagree.

**Worth a look apart from the commentaries:** 2-6's root line is optative
(*'joms 'gyur cig*), but the English is future tense.

**Correction for the record:** in chat I called Tenga Tulku "Kagyu". His file says only
"Dorlob Tenga Tulku", and his lineage isn't recorded here.

**Next:** Phase 2 — apply the 11 fixes (minimal edits, logged), handle the termbase
changes they imply (`lotus_face` narrowed to 1-8; `supreme` at 1-12 and `power` at 1-21),
then re-run the check.

---

## Commentary fact-check Phase 2 — fixes applied (draft 3) — DONE

Edited `3-TRANSFORMATIONS/Translations/en-general/bo-...-en-general.md` in place
(the user chose in-place editing over a separate file). Pre-edit version: git
`250b054` (11:57). Note that the vault's auto-backup then committed the edited file
at 12:23 (`07697ce`), so use `250b054` for the draft-2 text, not HEAD~ from a later
point.

- **11 edits:** all 11 consensus fixes, plus 2 termbase fixes (1-12 "supreme" →
  "intense", for ཤིན་ཏུ; 1-21 "power" → "might", for མཐུ). The log is
  `commentary-fact-check-fixes-log-en-general.md`.
- **Properties updated so the file shows what was done:** `draft: 3`, `draft_history`,
  `revised`, `fact_checked`, `fact_check_commentaries` (the 4 paths),
  `fact_check_consensus`, `fact_check_fixes_log`, `fact_check_fixes_applied: 11`,
  `fact_check_open_items: 6`; `rails_used`, `generator`, `translator` and `note`
  rewritten. `status: draft` is unchanged. YAML parses. The vault linter defines an
  allowed-key list but never enforces it, and the file already carried extra keys.
- **Termbase (now 48 entries):** `lotus_face` narrowed to 1-8; new `might` (མཐུ, 1-21);
  the 1-21 keyword in the grade file is retagged; glossary TSV updated. The grade file's
  `en_text` is intentionally left as the draft-2 snapshot, so it no longer matches the
  .md for the 11 edited verses.
- **Verified:** alignment checker OK; exactly the 11 intended blocks changed; no locked
  term newly missing; all 10 fixed verses re-read against the consensus glosses.

**Open for the translator:** the 6 split readings (1-3 colours, 1-8 ture and
"champions", 1-14 underworld, 1-17 Vindhya — footnote?, 1-22), and 2-6's optative.
**Next in the original pipeline:** human/specialist review, then publish (step 7).

---

## Open items decided (user) — DONE

The user decided the 7 open items. Changed: 1-14 "seven underworld levels" → "seven
levels"; 2-6 last line to the optative ("And may obstacles be absent, each one
destroyed."). Kept: 1-3 colours on the lotus; 1-8 "ture" as her name; 1-8 "champions of
Mara"; 1-17 Vindhya, with the "pierces" reading recorded in the `translator_notes`
property; 1-22 "and". Properties: `fact_check_open_items: 0`, `translator_decisions: 7`,
`translator_notes`. Alignment check OK.

**State of the translation:** draft 3, no open fact-check items, `status: draft`.
**Next:** specialist review, then publish (pipeline step 7). Upload goes through
`translation-upload` / `4-SYSTEM/scripts/upload_translation.py`, not this workflow.

---

## Draft 1 vs draft 3 comparison — DONE

`3-TRANSFORMATIONS/Translations/en-general/comparison-draft1-vs-draft3-en-general.md`:
a verse-by-verse word diff (Obsidian ~~strike~~ / ==highlight==), with each change
attributed to the termbase pass (T), the fact-check (F) or a user decision (D).
21 of 32 verses changed: 16 by T, 13 by F/D, 8 by both; 11 unchanged. The zero-shot
DharmaMitra draft (`Dharmamitra/en/`) is ~88% similar to the glossary-primed draft 1 —
the soft glossary hint barely steered the output.

---

## Consistency measurement — DONE

`3-TRANSFORMATIONS/Translations/en-general/consistency-report-en-general.md`, covering
D0 zero-shot, D1 glossary-primed, D2 termbase pass and D3 fact-checked.
- **Locked-term adherence** (122 verse–term pairs, 5 subsumed pairs excluded): 78.7% → 86.9% → 99.2% → 100%.
- **Repeated words with more than one spelling** (8 tracked): 1 → 2 → 0 → 0 (tuttare; D1 also hum).
- **Distinct Tibetan words merged** (3 groups): 2 → 1 → 1 → 0 (ནུས/དབང/མཐུ all "power"
  until D2/D3; D0 used "spirits" for both འབྱུང་པོ and གདོན).
- **Caveat:** the yardstick is our own termbase, so D2/D3 score high by design.
  The script is in the session scratch (`~/fc_tmp/consistency.py`), not the vault.

---

## Skill improvements from this run (2026-09-24)

Fixes committed to the shared Webuddhist-Skills repo (`main`):
- **keyword-extract:** clean corpus outputs; full IAST tokenizer; `--keep-transliterated`; `keyword_gap_report.py`.
- **graded-translate:** `validate_grade_file.py`; grade-file mode and `--strict-diacritics` in `check_termbase_consistency.py`; `termbase_to_glossary.py` and `termbase_to_md.py`.
- **commentary-fact-check:** whole-verse `extract_translation.py`; duplicate and unknown-ID checks in `extract_commentary.py`; `find_textual_variants.py`; `tally_report.py`; Phase 1b consensus; a generic Phase 2.
- **machine-translate:** fail-fast network errors; certifi; verse-scoped glossary lines.
- **CONVENTIONS §7:** translation history properties.

The vault's `4-SYSTEM/Skills/dharmamitra-translate/` is **archived** (moved, not deleted) to
`4-SYSTEM/Skills/_archive/`. `/dharmamitra-translate` and `recut_liturgy_import.py` now
point at `../Webuddhist-Skills/rails/machine-translate/`.

**The new validator found 3 errors in this project's termbase/grade file** (fixed 2026-09-24 — see next section):
- **I-3 `noble_venerable`:** the Tibetan is written འཕགས་མ་རྗེ་བཙུན་མ, but the verse reads རྗེ་བཙུན་མ་འཕགས་མ (reversed order).
- **1-5 `tuttare`:** ཏུཏྟྭ་ར་ཡི་གེ isn't contiguous in the verse, because hūṃ sits between the words.
- **1-13 `joy`:** the root spells the word དགས, but the entry has དགའ.

Also: `venerable_tara` uses a "..." form, which can never match text. Together with
`noble_venerable` it causes the 2 remaining drift-check misses at I-3.

Run: `python3 ../Webuddhist-Skills/rails/graded-translate/scripts/validate_grade_file.py
--termbase <this folder>/en-bo-en-termbase-general.json --grade-file <this folder>/bo_en_keyword_general.json`.

## Termbase fixes from the validator (2026-09-24)

- **`noble_venerable`:** Tibetan corrected to རྗེ་བཙུན་མ་འཕགས་མ (the text's word order). Rendering changed
  from "the Noble and Venerable One" to **"Noble and Venerable"**, which is what the fact-checked I-3 says
  before "Tara".
- **`venerable_tara`:** **archived, not deleted.** It moved to `en-bo-en-termbase-general.archived-entries.json`
  with its I-3 grade-file keyword, the date and the reason. `noble_venerable` + `tara` already cover I-3.
- **`tuttare`:** the form is now ཏུ་ཏྟྭ་ར / ཏུཏྟྭ་ར. The 1-5 keyword is ཏུཏྟྭ་ར.
- **`joy`:** added the form བསྐོར་དགས for 1-13, which is now the 1-13 keyword. Bare དགས is left out on purpose:
  it also occurs in 1-18 inside རི་དགས "deer".
- `en_text` in the grade file is unchanged (it is still the D2 snapshot). `glossary-en-general.tsv` is unchanged
  (it is the historical D1 input). For a new DharmaMitra run, regenerate it with `termbase_to_glossary.py`.

The termbase now has **47 entries**, plus 1 archived.
- `validate_grade_file.py`: **0 errors**, 22 warnings. The warnings are W2/W3/W5 and are all intended splits or
  nestings.
- `check_termbase_consistency.py --grade-file … --strict-diacritics` on the fact-checked translation:
  **131/131 locked renderings found, 0 misses** (before the fix: 130/132, with 2 misses at I-3).

## Chinese (zh), general grade — Phase 1 word list (2026-09-24)

**Tenkal's choices:** Traditional characters; clear modern Chinese (general grade, not the chanting style);
mantra syllables in Chinese characters; flagged picks "go with your picks" (decided by Claude, with the reason
recorded).

**Direction:** translate from the Tibetan, not from the English. The English (D3) and the commentary consensus
are the meaning check. Keyword extraction was not re-run: the 47 Tibetan terms and their verse scopes are reused.

**No attested Chinese translation**, so every value has a source (graded-translate Phase 1 Step 4b, new):
1. the classical canon version, CBETA T1108B (the same text the 17th Karmapa's office publishes), aligned to our
   block IDs in `../zh-references/zh-classical-T1108B.md` (vocabulary evidence only);
2. the standard Buddhist term;
3. the zero-shot DharmaMitra zh draft (`Dharmamitra/zh/`), as a suggestion only.
The online Mahāvyutpatti (Oslo TLB) could not be read with this session's tools; web search is off for the org.

**Files (this folder):**
- `en-bo-zh-termbase-general.json` — 52 entries: 47 carried over, plus 5 Chinese-only (`greater` split from
  `great` at 2-3; mantra syllables `om`, `svaha`, `hara`, `tara_syllable`). Each entry has `zh`, `zh_source`,
  `zh_note` and `zh_evidence`; the 14 decided by Claude also have `zh_decision`. `ability` also covers 1-5.
- `bo_zh_keyword_general.json` — 34 verses, 148 keywords. `text` is the fact-checked English D3, used as the
  meaning reference; `zh_text` is empty until Phase 2.
- `glossary-zh-general.tsv` — built with `termbase_to_glossary.py --lang zh --scope-all` (76 lines, all
  verse-scoped, so 1-8's 蓮花面容 is not hinted in 1-1).
- `termbase-zh-general.md` — readable review table, with Claude's 14 decisions first.

**Checks:**
- `validate_grade_file.py --lang zh`: **0 errors**, 22 warnings (intended splits and nestings).
- Baseline: the zero-shot zh draft already uses **63/137 locked words (46%)**
  (`check_termbase_consistency.py --lang zh --grade-file …`). Most misses are 頂禮 for 敬禮 and mantra syllables
  left in Latin letters. 1-6 has 羅剎 where the Tibetan is རོ་ལངས (起屍).

**Skill changes (Webuddhist-Skills):** a `zh` register section plus Step 4b in graded-translate; `--lang` on
`validate_grade_file.py`, `check_termbase_consistency.py` and `termbase_to_glossary.py`; `--scope-all` on
`termbase_to_glossary.py`.

**Next — Phase 2 (DharmaMitra, run by Tenkal in Terminal):** new track
`3-TRANSFORMATIONS/Translations/Dharmamitra/zh-general/`. `style.md` is written already (Traditional, clear
modern Chinese, Chinese-character mantras). Then enforce the word list verse by verse → zh-general D2 →
consistency check → meaning check against the English D3 and the consensus → back-translation → native
reviewer.

### Update — Chinese word list is now a skill (2026-09-24)

New shared skill **`zh-keyword-standardize`** (Webuddhist-Skills `rails/zh-keyword-standardize/`,
slash command `/zh-keyword-standardize`). It covers choices → classical reference → worksheet → decisions →
build → validate/baseline/glossary.
- **`zh-decisions-general.json` is now the file to edit.** `build_zh_termbase.py --force` rebuilds
  `en-bo-zh-termbase-general.json`, `bo_zh_keyword_general.json` and `termbase-zh-general.md` from it. The
  rebuild matched the hand-built files exactly; only the evidence field names and the order of source labels
  changed.
- `zh-worksheet-general.md`: the evidence per term and verse, from `zh_worksheet.py`. It shows 10 terms whose
  Tibetan also occurs where the term is not locked. Two examples: སྒྲོལ་མ in 1-11 is the verb "liberate", not
  Tārā's name; ཆུ་སྐྱེས་ཞལ in 1-1 is the Lord's face, not hers.
- Re-checked: validator (`--lang zh`) 0 errors; baseline 63/137; glossary 76 lines, all verse-scoped.
