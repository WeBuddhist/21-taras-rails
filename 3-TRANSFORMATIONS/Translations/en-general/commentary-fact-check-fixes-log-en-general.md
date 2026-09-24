## Praise to the Twenty-One Taras — Fact-Check Fix Log — general grade

Method: fixes applied from `commentary-fact-check-consensus-en-general.md`, where at
least 3 of 4 commentaries (Drakpa Gyaltsen, Gendun Drub, Tāranātha, Tenga Tulku)
agree the English is wrong. Two termbase-consistency fixes found during the audit are
included and marked. Minimal edits only — the flagged span, nothing else; every
verse keeps its line count. Splits and single-commentary flags are listed below and
were not applied. This is a draft editing pass, not a scholarly sign-off — a domain
specialist should review before the translation is treated as final.

### Run — 2026-09-24 — all flagged verses

Pre-edit version: vault git backup `250b054` (2026-09-24 11:57); the same text is in
the grade file's `en_text`.

#### Applied

| Verse | Before | After | Grounds |
|---|---|---|---|
| 1-1 | Born from the opening stamens of the lotus face / Of the Lord of the Three Worlds. | Born from the opening stamens of the lotus / That arose from the face of the Lord of the Three Worlds. | 4/4 — lotus arose from Avalokiteśvara's tears/face (DG, GD, TN, TT) |
| 1-3 | She whose sphere of activity is generosity, diligence, austerity, peace, / Patience, and meditative concentration. | She whose sphere of activity is generosity, diligence, discipline, peace, / Patience, meditative concentration, and wisdom. | *dka' thub* = discipline 4/4; wisdom named (DG, GD, TT read *spyod yul* as wisdom; TN's framing 'the perfections are your domain' kept) |
| 1-5 | Fills the realms of desire, the directions, and space, | Fills the desire, form, and formless realms, | *phyogs*/*nam mkha'* = form and formless realms (DG, GD, TT; TN: 'space' = both) |
| 1-8 | Homage to ture, the Great Fearful One, | Homage to ture, the Great Terrifying One, | she terrifies the māras — DG, GD, TN (TT silent) |
| 1-9 | Adorned with wheels in every direction without exception, | Her palm adorned with the wheel of all directions without exception, | one wheel on her palm — DG, GD, TT (TN reads the directions' realms) |
| 1-10 | Homage to you, whose majestic and supreme joy / Spreads garlands of light from your crown, | Homage to you, who bring supreme joy, whose majestic / Crown ornament spreads garlands of light, | the joy is what she brings to beings — DG, GD, TN (TT: hers) |
| 1-12 | Constantly radiates a supreme light. | Constantly radiates an intense light. | termbase: `supreme` is locked to རབ; this line renders ཤིན་ཏུ ('intensely') |
| 1-16 | You are the lamp arising from the hum of awareness. | You are the lamp arising from the knowledge-mantra hum. | *rig pa* = knowledge-mantra 4/4; 'lamp' kept (our root and TN read *sgron ma*) |
| 1-17 | Homage to you, who stamp your feet with the syllable ture, | Homage to you, Ture, who stamp your feet, | Ture is Tārā herself — GD, TN, TT (DG silent) |
| 1-19 | Homage to the sovereign of the hosts of gods, / Whom gods and kinnaras rely upon; | Homage to you, served by the kings of the hosts of gods, / Relied upon by gods and kinnaras; | the kings of the gods serve her 4/4 |
| 1-21 | Homage to you, perfectly endowed with the power of peace, / Established by the three suchnesses; | Homage to you, perfectly endowed with the might of peace, / With the three suchnesses set upon you; | the three suchnesses are set upon her 4/4; termbase: མཐུ = `might`, kept distinct from དབང `power` |

Termbase changes made alongside (`en-bo-en-termbase-general.json`, `bo_en_keyword_general.json`):
- `lotus_face` narrowed to 1-8 (removed from 1-1).
- New entry `might` (མཐུ) at 1-21; the 1-21 keyword is retagged from `power` to `might`. The termbase now has 48 entries.
- `glossary-en-general.tsv`: added མཐུ → might.
- The grade file's `en_text` was left unchanged as the draft-2 snapshot.

#### Skipped — translator's choice (commentaries split)

| Verse | Discrepancy | Why not applied |
|---|---|---|
| 1-3 | *gser sngo*: the colours are hers, or the lotus's? | GD, TT: her body; TN: the lotus (golden stalk, blue flower); DG unclear |
| 1-8 | *tu re*: the one addressed, or the mantra she uses? | DG, TN: mantra; GD, TT: her name — 2–2 |
| 1-8 | "champions of Mara" | DG, GD: the kleśa-māra; TN: Māra's commanders; TT: the army of the four māras |
| 1-14 | "seven underworld levels" | GD, TT: seven levels of worlds/beings; TN: underground; DG gives both |
| 1-17 | *'bigs byed*: Vindhya, or the verb "pierces"? | DG, TT: verb; GD, TN: mountain (TN: "either is acceptable") — 2–2. A footnote is worth considering |
| 1-22 | One praise, or two items? | DG, TN: one; GD, TT: two — 2–2 |

#### Not applied — one commentary only

| Verse | Flag | Outcome |
|---|---|---|
| 1-6 | a single Maheśvara, not "the various Īśvaras" | DG only; GD, TN, TT read it as plural |
| 1-15 | "OṂ and SVĀHĀ" order | DG only; GD, TT: oṃ opens and svāhā closes the mantra |
| 1-3 | *zhi ba* = wisdom | TN only |
| 2-6 | optative last line ("may … be destroyed") | Not a commentary dispute — the root's *'gyur cig* is optative. Needs your call |

**Result: 11 edits — all 11 consensus fixes (1-3's two share one edit) and 2 termbase fixes (1-12 on its own; 1-21's "might" within the 1-21 edit). 6 left as translator's choice; 4 not applied.**

#### Re-verification

Mechanical:
- `check_translation_alignment.py` passes: 32 segments and 5 headings mirror the root, with the same line count in every verse.
- All 11 new lines are present, and none of the old lines remains. Compared with the pre-edit version (`250b054`), exactly these blocks changed: 1-1, 1-3, 1-5, 1-8, 1-9, 1-10, 1-12, 1-16, 1-17, 1-19, 1-21.
- Locked-term check against the grade file: no term newly missing; `might` newly present at 1-21. The 9 misses reported are unchanged from before the edits and expected — the loose matcher doesn't handle "world(s)" (1-1, 1-5, 1-17) or "blaze" for "blazing" (1-13); the I-1, I-3 and a-1 title and colophon lines keep "Tārā" by design.

Against the commentaries (each changed verse re-read against the consensus glosses):

| Verse | New reading matches | Result |
|---|---|---|
| 1-1 | the lotus arose from his face/tears (DG, GD, TN, TT) | OK |
| 1-3 | discipline (all 4); wisdom named (DG, GD, TT); TN's "domain" framing kept | OK |
| 1-5 | desire, form and formless realms (DG, GD, TT; TN on "space") | OK — TN's "ten directions" reading of *phyogs* is no longer reflected |
| 1-8 | she terrifies (DG, GD, TN) | OK |
| 1-9 | one wheel on her palm (DG, GD, TT) | OK |
| 1-10 | the joy is what she brings (DG, GD, TN); "majestic" crown ornament (*brjid*) | OK — TT's reading (her own joy) no longer reflected |
| 1-16 | knowledge-mantra; "lamp" (root, TN) | OK |
| 1-17 | Ture is her (GD, TN, TT) | OK |
| 1-19 | the kings of the gods serve her (all 4) | OK |
| 1-21 | the three suchnesses set upon her (all 4); `might` for མཐུ | OK |

**Re-verification: 10/10 fixed verses consistent with the commentary consensus; 0 flags remaining in the fix group.** Open items: the 6 translator's-choice rows and the 2-6 optative above.
