---
topic: tara-06
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-06/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-06

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | This deity is the 6th verse of the Twenty-One Praises to Tara | same | YES | reworded only |
| 2 | Worshipped by Indra, fire god, Brahma, wind god, Vishvakarma; praised by bhutas, zombies, gandharvas, yakshas | same 5 deities + 4 groups | YES | list punctuation regrouped, no item added/dropped |
| 3 | Verbatim root-verse quote ("ཕྱག་འཚལ་བརྒྱ་བྱིན...བསྟོད་མ།") | character-for-character identical | YES | verbatim confirmed |
| 4 | Some commentaries don't count this among the 21 prostrations, instead as 5th sub-type of praise-manner | same | YES | ཁ་ཤས་→འགའ་ཞིག་ (flagged, see below) |
| 5 | Name not fixed; 3 different traditions | same | YES | གཞུང་ལུགས→བཞེད་སྲོལ (flagged) |
| 6 | Yama Sönam & Tenzin Dhonzang: "Victorious over the three worlds" | same | YES | verbs swapped (synonyms) |
| 7 | Gendun Drub: similar name, fewer words | same | YES | ཐ་སྙད→ཚིག་འབྲུ (flagged) |
| 8 | Palden Sherab, Tsultrim Namdak, Sungrab Tulku (called "the four") each name it by the "great terror who destroys spirit-classes" type | same 3 names, same count label ("four") | YES (after reversion) | a connecting དང་ between Tsultrim Namdak and Sungrab Tulku was dropped by Gemini, merging two list items without a conjunction — **reverted**, see below |
| 9 | Palden Sherab: "Great Terror Who Destroys Spirit-Classes"; Sangye Nyentrul: homophone-different-meaning term for gathered spirits | same | YES | minor particle/verb swaps |
| 10 | Remaining 12 commentaries: no special name, just "Tara" | same (12) | YES | |
| 11 | Two traditions on body form; ~4 of 16 commentaries detail it | same (2 traditions, 4/16) | YES | |
| 12 | Yama Sönam: red body, 1 face 4 arms, peaceful, lotus+moon seat, bodhisattva posture, vajra+sword (right), threat-mudra+lasso (left) | same attributes | YES | |
| 13 | Sangye Nyentrul & Palden Sherab: alternate wrathful form, red-black, half-vajra posture, 1 face 2 arms | same | YES | |
| 14 | Sangye Nyentrul detail: boon-granting mudra (R), vajra-kila in utpala (L), fire-lasso marked with hum, sparks | same | YES | |
| 15 | Palden Sherab elaborates same form generically for generation stage | same | YES | |
| 16 | Tsultrim Namdak: red-black, holds kila, hum-sparks; counted in this tradition despite unclear mudra/seat | same | YES | |
| 17 | No commentary reconciles the two body-form traditions or ranks one over the other | same | YES | |
| 18 | Main activity: pacifying harm from spirit-possession (Sangye Nyentrul & Palden Sherab, parallel practice instructions) | same | YES | |
| 19 | Sangye Nyentrul: subdues madness, amnesia, paralysis-causing obstructors, prevents recurrence | same 3 afflictions | YES | |
| 20 | Tsultrim Namdak: subdues obstructors, misleaders, rakshasa retinue, zombies, flesh-eaters, yakshas, mad demon-kings | same list (regrouped punctuation, no item dropped — verified by token diff) | YES | |
| 21 | Pema Namgyal: prostrating frees from fear of possession in this and all future lives | same | YES | |
| 22 | Tenzin Dhonzang: even great worldly gods prostrate, let alone humans; main activity = pacifying bhuta-possession | same | YES | |
| 23 | 8 commentaries place this verse directly as the 6th of the 21 prostrations | same (8) | YES | |
| 24 | Dharmabhadra, Gendun Drub, Lobsang Dawa (the four): count it instead as 5th sub-type of praise-manner; Dharmabhadra explains it as praise via honor from great worldly gods | same 3 names, "four" label, same content | YES | bold names byte-identical |
| 25 | Tenga Tulku likewise counts it as the 5th | same | YES | |
| 26 | This is not a dispute over the count of prostrations, just a difference in how the praise-manner subsections are counted | same | YES | |
| 27 | Who is Vishvakarma? 4 differing commentarial accounts | same (4 accounts) | YES | "ལྔ་པ"→"ལྷ་ལྔ་པ" adds "deity" — flagged, see below |
| 28 | Drakpa Gyaltsen: Great Lord, master of the four gods | same | YES | |
| 29 | Sangye Nyentrul: guardian of the south, Yama | same | YES | |
| 30 | Konchok Thabkhe: two deities — west water-god and earth-goddess Brtan-ma — combined, grounded in a sadhana manual + tantra citation | same 2 deities | YES | |
| 31 | Taranatha: not any single deity, but a group incl. wrathful and desire deities, sun-colored sages, phywa etc. | same | YES | |
| 32 | Tsultrim Namdak & Karma Maitri: unspecified, "many great lords" — close to Taranatha's reading | same | YES | |
| 33 | Chief of zombies: Drakpa Gyaltsen, Gendun Drub, Tsultrim Namdak (3) — all say "Great Lord" | same 3 names | YES | |
| 34 | Karma Maitri & Gendun Gyatso: a graveyard-dwelling zombie, unspecified name | same | YES | |
| 35 | Palden Sherab & Sangye Nyentrul: identify SW guardian as rakshasa Legden | same | YES | |
| 36 | Chief yaksha: many commentaries say Vaishravana himself | same | YES | |
| 37 | Gendun Drub distinguishes: "son of Vaishravana's son" | same | YES | |
| 38 | Karma Maitri & Gendun Gyatso: different name, "Mukdzin" | same | YES | |
| 39 | Konchok Thabkhe: claims his pairing of this verse with directional guardians is his own innovation, grounded in 3 reasons (tantra wording, Jowo's activity-cycle mantra-garland taming 10 guardians, own sadhanas surrounding Tara with guardians) | same 3 grounds | YES | |
| 40 | Palden Sherab, Sangye Nyentrul, Tenzin Dhonzang give detailed accounts of 10+ guardians but numbers/names don't directly match | same 3 names | YES | |
| 41 | Tenzin Dhonzang also cites an 8-guardian source from a Chakrasamvara mandala text, extended thence to 10–15 guardians | same numbers (8; 10–15) | YES | |
| 42 | Taranatha & Palden Sherab: hidden-meaning reading via completion-stage subtle body — Indra=earth, fire god=fire, Brahma=water, wind god=wind, Vishvakarma=space; 5 deities = 5 elements | same 5 correspondences, verified pairwise | YES | |
| 43 | Both: bhuta=channel, zombie=drop, gandharva=wind(-energy), yaksha=thought; dissolution of wind into drop = the meaning of the praise | same 4 correspondences, verified pairwise | YES | |
| 44 | Palden Sherab repeats the signless completion-stage explanation above | same | YES | |
| 45 | Taranatha's commentary lacks this second-stage reading | same | YES | |
| 46 | Summary: all commentaries agree the deity is worshipped/praised by 5 gods and 4 spirit-classes; but differ on name, body form, identity of Vishvakarma, and guardian details | same | YES | |

## Ref attachment walk

All 74 `<ref>` tokens verified in exact original sequence (script-checked positions match 1:1, before vs after — confirmed independently by extracting the ordered ref-name sequence from both `body-before.txt` and `body-after.txt`: identical, 74/74). Spot-walked every ref against its governing clause per the sentence table above:

- `taranatha`, `sungrab-tulku`, `tenzin-dhonzang` (opening def.) → still support "this is verse 6 of the 21 praises" — YES
- `palden-sherab` (×multiple) → each still attached to the same clause it supported before (worship description, root-verse quote, naming, body-form, activity, section-count, guardian detail, hidden-meaning) — YES
- `yama-sonam` → still supports naming + body-form description — YES
- `gendun-drub` → still supports the alternate-name claim — YES
- `tsultrim-namdak` → still supports body-form-2 + activity list + guardian-count — YES
- `sangye-nyentrul` → still supports naming, body-form-2, activity, SW guardian, Vishvakarma-account — YES
- `pema-namgyal`, `dharmabhadra`, `gendun-gyatso`, `karma-maitri`, `konchok-thabkhe`, `drakpa-gyaltsen`, `lobsang-dawa`, `tenga-tulku` → each still attached to the same claim as before — YES

No ref migrated to a different statement.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — does not block PASS:

| Before | After | Comment |
|---|---|---|
| གཞུང་ལུགས་ | བཞེད་སྲོལ་ / བཞེད་ཚུལ་ | "tradition/system" ↔ "assertion-tradition" — used consistently as a synonym pair throughout |
| ཁ་ཤས་ | འགའ་ཞིག་ | "some/several" — synonym |
| ཐ་སྙད་ | ཚིག་འབྲུ་ | "term/word" ↔ "syllable" — synonym in this context |
| བཀོད་ / གདགས་ | བཞེད་ / བཏགས་ | "posited/named" verb-pair alternation, same meaning |
| འཛིན་ | བསྣམས་ | "holds" — synonym |
| གསལ་བཤད་མཛད་ | བཀྲལ་ | "elucidated" — synonym |
| མ་བྱས་ | མ་མཛད་ | plain→honorific verb register for the same commentator's action (consistent with honorific register already used elsewhere in this article for commentators) |
| སྔགས་འཕྲེང་ | སྔགས་ཕྲེང་ | orthographic variant of the same word ("mantra garland") |
| གོང་དུ་སོར་ | གོང་དུ་སོ་སོར་ | appears to correct an abbreviated/typo'd form in the source (སོར→སོ་སོར, "individually") to the standard word — not a meaning change |
| རྩ་ཚིག་གི་ལྔ་པ་ | རྩ་ཚིག་གི་ལྷ་ལྔ་པ་ | added ལྷ ("deity") — makes explicit that Vishvakarma is "the fifth deity" of the root verse, which is already established as fact by paragraph 1's list of the five deities; does not introduce new content |

## Reverted drift (if any)

One instance of factual/structural drift found and corrected:

- **Location:** "མཚན་གྱི་ངེས་ཚིག" section, the sentence listing the four commentators who classify this deity under the "Great Terror Who Destroys Spirit-Classes" type.
- **Before (source):** `...མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་དང་མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་དང་འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ་བཞིས་ནི...`
- **Gemini's output (drift):** `...མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་དང་མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ་བཞིས་ནི...` — the connecting `དང་` between "Khenpo Tsultrim Namdak" and "Drepa-Dramé Sungrab Tulku" was silently dropped, leaving the two names juxtaposed without a conjunction. This is a mechanical/grammatical drift in how the list of named commentators is structured (not a name added or removed, and the "four" label and identity of each named commentator are unchanged), but it degrades the list's parseability and was not attested in the source, so it was reverted rather than accepted as a stylistic variant.
- **Remedy applied (Rule 8a, surgical reversion):** restored the exact source span `མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་དང་འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ་བཞིས་ནི` in `article.md`. `body-after.txt` was left untouched as the raw model record per Rule 8.

No other factual drift was found. In particular, every occurrence of a personal name (bolded and unbolded) was walked individually for the known honorific-insertion drift pattern (see script output above) — no honorific title (སློབ་དཔོན་, མཁན་ཆེན་, རྗེ་བཙུན་, etc.) was inserted before any name that did not already carry it in the source; all 24 bold spans are byte-identical in order and content between before and after.

## Verdict

**PASS-after-reversion.** No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator; every verbatim quotation is character-for-character identical; all 74 refs remain attached to the same statements they supported before; all numerals, doctrinal correspondences, and named commentator lists are unchanged. One mechanical drift (a dropped conjunction particle in a list of named commentators) was found and surgically reverted in `article.md`, restoring the source's exact wording. The remaining differences are prose-level lexical substitutions (word choice, verb-register, orthography, punctuation regrouping) that leave every fact and doctrinal position intact.
