---
title: Praise to the Twenty-One Taras — translation-qa fixes log (general grade)
file_type: report
translation: 3-TRANSFORMATIONS/Translations/en-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general.md
qa_report: 3-TRANSFORMATIONS/Translations/en-general/reports/qa-report.md
from_draft: 3
to_draft: 4
date: 2026-09-24
fixes_applied: 30
---

## translation-qa fixes — draft 3 → draft 4 — 2026-09-24

Approved by the project owner (Tenkal). Source of the fixes: the Errors table and Top fixes in `qa-report.md` (QA run on draft 3). Each change was checked against the Tibetan root (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), the commentary consensus and fixes log (settled translator decisions), and the locked word list (`en-bo-en-termbase-general.json`). Every block keeps its line count and block ID; nothing was added that is not in the Tibetan. Pre-edit copy: draft 3 is the version described in `commentary-fact-check-fixes-log-en-general.md`.

**Result: 30 of 31 QA rows applied (the 1 Major, 29 of 30 Minors; the 1-6 transliteration row only partly, see below). 1 not applied (a-1, locked). Neutral rows not applied.**

### Decisions taken

- **One voice.** All 21 homages now address her in the second person, "Homage to you, …", with the verbs agreeing ("you who … fill", "who … destroy", "bring", "shatter"). Where the Tibetan names her in line 1 (1-1 སྒྲོལ་མ; 1-8 and 1-17 ཏུ་རེ) the name follows "you" as a vocative: "Homage to you, Tara, …", "Homage to you, Ture, …" — the pattern 1-17 already had. I-3 (the translator's homage, not one of the 21) stays "Homage to the Noble and Venerable Tara".
- **Spelling.** The word list locks plain spellings for hum, phat, trat, tuttare, ture, yaksas and Tara ("general register, not a scholarly transliteration register" — `yaksha` note). The other items were brought into line with those locks: mantra syllables plain lower case (om, svaha, tara, hara; "Om!" at I-3), and unlocked Sanskrit names with the diacritics dropped the way the `yaksha` lock drops them (Usnisa, Tathagatas, Brahma, Vayu, Isvaras, nirvana, Amitabha). Three locked forms keep diacritics and are listed for the word list: `vetala` (vetāla), `blessed_tara` (the Blessed Tārā), `sanskrit_title` (I-1).
- **1-3, six perfections vs seven items.** Consensus row 3: DG, GD and TT read སྤྱོད་ཡུལ as wisdom (TN reads ཞི་བ as wisdom); direction "Name wisdom (the wording is a translator call)". Draft 3 rendered སྤྱོད་ཡུལ twice ("sphere of activity" + "wisdom"). Draft 4 renders it once, on the majority reading: "the very domain of wisdom" (སྤྱོད་ཡུལ་ཉིད་མ). ཞི་བ "peace" stays: it is in the Tibetan, and only TN counts it as wisdom (consensus "Leave" table: "Others read *zhi ba* as the pacifying of faults"). So the line keeps the Tibetan's seven words; no note needed.
- **1-22, "by the root mantra".** The consensus split at 1-22 concerns only whether the praise and the homages are one thing or two; the decision was to keep "and" (fixes log, decisions row 1-22), and it is kept. "of" → "by" is a separate point of grammar: རྩ་བའི་སྔགས་ཀྱིས is instrumental, and TN ("the praise by the ten-syllable root mantra") and TT ("the praise by the root mantra") read it so. The full stop became a comma, because the Tibetan sentence runs on into 2-1/2-2.
- **Ture capitalised at 1-8.** Settled decision (fixes log, decisions row 1-8): ture here is her name, "consistent with 1-17 and 1-21". The lock `ture` is case-insensitive in the checker, and its attested note already prescribes capitalising the name use.

### Applied

| Verse | Before | After | QA row / basis |
|---|---|---|---|
| 1-8 | Homage to ture, the Great Terrifying One, / Who completely destroys the champions of Mara, / Who forms a frowning expression upon your lotus face, / And slays all enemies without exception. | Homage to you, Ture, the Great Terrifying One, / Who completely destroy the champions of Mara, / Whose lotus face is set in a wrathful frown, / And who slay all enemies without exception. | **Major** 1-8 wrong referent (root ཆུ་སྐྱེས་ཞལ་ནི་ཁྲོ་གཉེར་ལྡན་མཛད; `lotus_face` note "Her own face"); Minor 1-8 "Ture" (decision row 1-8); Minor 1-11 ཁྲོ་གཉེར = "wrathful frown"; voice |
| I-2 | The Homage to Tara with Twenty-One Verses and its Benefits. | The Praise to Tara in Twenty-One Homages, with Its Benefits. | Minor I-2; root སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ཕན་ཡོན་དང་བཅས་པ |
| I-3 | Oṃ! | Om! | Minor 1-15 (one form for every mantra syllable); root ཨོཾ |
| 1-1 | Homage to Tara, the swift and heroic, | Homage to you, Tara, swift one and heroine, | Minor 1-1 (root མྱུར་མ་དཔའ་མོ); voice |
| 1-2 | Homage to her whose face … / … moons gathered together, / … / Of a thousand gathered stars. | Homage to you, whose face … / … moons heaped together, / … / Of thousands of gathered stars. | Minor 1-2 ×2 (root བརྩེགས "stacked"; སྟོང་ཕྲག "thousands"); voice |
| 1-3 | Homage to her whose hand … / … / She whose sphere of activity is generosity, diligence, discipline, peace, / Patience, meditative concentration, and wisdom. | Homage to you, whose hand … / … / Who are generosity, diligence, discipline, peace, / Patience, concentration, and the very domain of wisdom. | Minor 1-3 Addition; consensus row 3 (see Decisions); Minor 1-15 སྤྱོད་ཡུལ = "domain"; voice |
| 1-4 | Homage to the Uṣṇīṣa of the Tathāgatas, / She who acts … / … / Who have attained every single perfection without exception. | Homage to you, Usnisa of the Tathagatas, / Who act … / … / Who have attained all the perfections without exception. | Minor 1-4 (root མ་ལུས་ཕ་རོལ་ཕྱིན་པ); Minor 1-6 spelling; voice |
| 1-5 | Homage to her who … / Fills … / Trampling the seven worlds under her feet, | Homage to you who … / Fill … / Trampling the seven worlds under your feet, | voice (1-1 – 1-9 row) |
| 1-6 | Homage to her whom Indra, Agni, Brahmā, / Vāyu, and the various Īśvaras worship, / Praised from before by hosts of spirits, / Vetālas, gandharvas, and the hosts of yaksas. | Homage to you whom Indra, Agni, Brahma, / Vayu, and the various Isvaras worship, / Praised before you by spirits, / Vetālas, gandharvas, and hosts of yaksas. | Minor 1-6 Fluency (root མདུན་ནས; only གནོད་སྦྱིན་ཚོགས has ཚོགས); Minor 1-6 spelling (partial: `vetala` locked); voice. "the various Īśvaras" wording kept (consensus Leave) |
| 1-9 | Homage to her whose fingers … / Beautifully adorn her heart, / Her palm adorned with the wheel …, / Radiating a turbulent mass of her own light. | Homage to you, whose fingers … / Beautifully adorn your heart, / Whose palm is adorned with the wheel …, / Who radiate a turbulent mass of your own light. | Minor 1-9 dangling participle (root བརྒྱན་པའི … འཁྲུག་མ); voice |
| 1-10 | Brings maras and the world under your power. | Bring maras and the world under your power. | Minor 1-10 agreement |
| 1-11 | Who, with a vibrating frown and the syllable hum, | Who, with a quivering, wrathful frown and the syllable hum, | Minor 1-11 (root ཁྲོ་གཉེར་གཡོ་བའི) |
| 1-12 | Amitābha | Amitabha | Minor 1-6 spelling |
| 1-13 | With right leg extended and left bent, surrounded by joy, | With right leg extended and left drawn in, joyfully encircled, | Minor 1-13 Terminology (བསྐུམ = "drawn in" as at 1-7); Minor 1-13 Audience (root ཀུན་ནས་བསྐོར་དགས; consensus "Other findings": GD, TN, TT read an encircling retinue/dance) |
| 1-14 | … and trample it with your feet; | … and pound it with your feet; | Minor 1-14 (root བརྡུང; `trampling` = མནན) |
| 1-15 | Whose very sphere of experience is the peace of nirvāṇa; / … the syllables OṂ and SVĀHĀ, / You completely destroy great negativity. | Whose very domain is the peace of nirvana; / … the syllables om and svaha, / You completely destroy great misdeeds. | Minor 1-15 ×3 (སྤྱོད་ཡུལ as 1-3; སྡིག་པ as 2-2 "misdeeds"; syllable style per `hum`/`phat` locks); 1-6 spelling. Order om/svaha kept (consensus Leave) |
| 1-16 | Homage to you, surrounded by joy, / Who utterly shatters the bodies of enemies; / With the ten-syllable mantra arranged, / You are the lamp arising from the knowledge-mantra hum. | Homage to you, joyfully encircled, / Who utterly shatter the bodies of enemies, / In whom the ten-syllable mantra is set, / The lamp arising from the knowledge-mantra hum. | Minor 1-16 ×2 (agreement; root ཡི་གེ་བཅུ་པའི་ངག་ནི་བཀོད་པའི); 1-13 Audience ("Recurs at 1-16"; root ཀུན་ནས་བསྐོར་རབ་དགའ་བའི). "lamp" and "knowledge-mantra" kept (consensus row 7) |
| 1-18 | By reciting TĀRA twice … | By reciting tara twice … | Minor 1-18 (root ཏཱ་ར་གཉིས་བརྗོད) |
| 1-20 | By reciting HARA twice … | By reciting hara twice … | Minor 1-20 (root ཧ་ར་གཉིས་བརྗོད) |
| 1-22 | With this praise of the root mantra, / And these twenty-one homages. | With this praise by the root mantra / And these twenty-one homages, | Minor 1-22 (root རྩ་བའི་སྔགས་ཀྱིས; TN, TT); "and" kept (decision row 1-22) |
| 2-1 | Who recites this with supreme intent, | Who recites this earnestly, | Minor 2-1 (root རབ་ཏུ་བརྗོད; consensus "Other findings": GD "with great faith", TN "with diligence") |
| 2-2 | Having arisen at dusk and at dawn, | Rising at dusk and at dawn, | Minor 2-2 (root ལངས་པར་བྱས་ནས) |
| 2-3 | Seventy million Victorious Ones | Seventy million Victors | Minor 2-3 (རྒྱལ་བ as 1-4) |
| 2-4 | Their poisons, which are extremely fierce, | For such a person, poisons that are extremely fierce, | Minor 2-4 (root དེ་ཡི་དུག) |
| 2-5 | This applies to other sentient beings as well. | And so too for other sentient beings. | Minor 2-5 (root སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ; "sentient" kept for སེམས་ཅན) |

Voice row (1-1 – 1-9 Style/Register) is applied through 1-1, 1-2, 1-3, 1-4, 1-5, 1-6, 1-8, 1-9 above; 1-7 and 1-10 – 1-21 were already second person.

Count by QA row: Major 1-8 (1); Minors I-2, 1-1, 1-2 ×2, 1-3, 1-4, 1-6 ×2, 1-8, 1-1–1-9 voice, 1-9, 1-10, 1-11, 1-13 ×2, 1-14, 1-15 ×3, 1-16 ×2, 1-18, 1-20, 1-22, 2-1, 2-2, 2-3, 2-4, 2-5 (29). **Total 30.**

### Not applied

| Verse | QA row | Reason |
|---|---|---|
| a-1 | Terminology: "Tārā" vs "Tara" | Would change a locked rendering (`blessed_tara` = "the Blessed Tārā"). For the word list. |
| 1-6, 1-21 | LocaleConvention (residue): "vetālas" keeps its macron | Locked (`vetala` = "vetāla"). The rest of that row was applied. For the word list. |
| — | Neutral rows (1-3 "gold and blue", 1-8 "champions of Mara", 1-14 "the seven levels", 1-17 "Vindhya", 1-22 "and", 2-6 optative; 1-15 order, 1-6 "various Īśvaras"; 1-21 "three suchnesses"; 1-4 Usnisa as a loanword; 1-18 "moon"; `headings_translated`) | Neutral: settled decisions, single-commentary flags or preferences. Only the spelling of Usnisa/Isvaras changed, under the spelling rule. |

### For the word list

These need a change in `en-bo-en-termbase-general.json` (and the matching keywords in `bo_en_keyword_general.json`) before the file can follow them. Not changed here.

1. `blessed_tara`: "the Blessed Tārā" → "the Blessed Tara", to match `tara` (then a-1 can drop the macron).
2. `vetala`: "vetāla" → "vetala", to match the plain pattern of `yaksha` (1-6, 1-21).
3. `sanskrit_title` (I-1): "Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka" is the only other IAST left. A transliterated title may reasonably stay scholarly; decide and note it.
4. `ture`: update the note to say ture is capitalised as her name at 1-8, 1-17 and 1-21 (translator decision row 1-8), lower case only when it is the mantra syllable.
5. Optional: lock the forms now used consistently — ཁྲོ་གཉེར "wrathful frown" (1-8, 1-11, 1-14), སྤྱོད་ཡུལ "domain" (1-3, 1-15), སྡིག་པ "misdeeds" (1-15, 2-2), རྒྱལ་བ "Victors" (1-4, 2-3), བསྐུམ "drawn in" (1-7, 1-13), བརྡུང "pound" (1-14), and the plain mantra syllables om, svaha, tara (1-18), hara (1-20).

### Verification

- `check_translation_alignment.py`: OK — 32 segments, 5 headings mirror the root; every block keeps its line count and ID.
- `check_termbase_consistency.py --strict-diacritics`: 131/131 locked renderings found, 0 misses (4 loose, 3 covered) — same as draft 3.
- `lint_text_input.py`: OK.
- Frontmatter parses as YAML.
