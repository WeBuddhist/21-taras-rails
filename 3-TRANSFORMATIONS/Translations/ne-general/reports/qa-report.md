---
title: MQM quality check — Nepali (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general.md
skill: Webuddhist-Skills/rails/translation-qa
note: "Runs are appended, dated. Never overwrite an earlier run."
---

# QA report — Nepali, general grade

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general.md (draft 5) — 2026-09-25

**Score:** 97.4 / 100   **Gate:** PASS (0 critical, 0 major) — the file may go to native review; it stays `draft`
**Profile:** Fluency 7 · LocaleConvention 5 · Terminology 2 · Accuracy/Mistranslation 1 · Style/Register 0 · Audience 0 · Markup/BlockID 0 — all 15 Minor
**Word count:** 583 Nepali words (space-separated Devanagari tokens in the 32 blocks and 5 headings; frontmatter, transclusion lines and `^` IDs excluded)
**Formula:** 100 − (15 × 1 / 583) × 100 = 97.43

**This is an LLM self-check.** It is not a sign-off. A native Nepali reader and a domain specialist decide.

**Rails basis:** `2-RAILS/Verses/` is empty for this text. Accuracy was scored against the Tibetan critical edition
(`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), the Nepali consensus
(`ne-general/reports/commentary-fact-check-consensus-ne-general.md`) and the English consensus
(`en-general/reports/commentary-fact-check-consensus-en-general.md`). The fact-checked English
(`en-general/bo-…-en-general.md`) is the meaning reference. Translator decisions in the frontmatter (the 7 English
decisions; Tenkal's 1-11 दरिद्रता, 1-7 "amid fire", बोधिसत्त्व/बुद्ध, ग्रह kept and flagged) and the consensus
"Left" list are settled and are not counted as errors.

**Requirements basis:** there is no `requirements.md`. The contract is
`3-TRANSFORMATIONS/Translations/Gemini/ne-general/style.md` (line for line; standard Nepali, not Hindi, in
Devanagari; Nepali spelling of Sanskrit words such as शान्ति, मन्त्र, आनन्द; clear modern devotional Nepali;
mantras in Devanagari, no quotation marks; बुद्ध / बोधिसत्त्व; nothing added), read with the Hindi **general** row
and Liturgy note of `graded-translate/SKILL.md` § Registers. Nepali has no row of its own in § Registers.
The word list's `_meta` adds: "Nepali keeps the Sanskrit nasal consonants" (`ne-decisions-general.json`).

**Stage 0 (mechanical):** `$HOME/qa/stage0-ne.json` — 32/32 blocks, 32 transclusions, 0 findings.
**Terminology (mechanical):** `check_termbase_consistency.py --lang ne` — 136/136 locked words found, 1 loose
(1-8 कमल मुख, written कमल-मुखमा), 1 covered by a longer locked phrase (a-1), 0 misses.
**Alignment:** `check_translation_alignment.py` — OK (32 segments, 5 headings).

**Coverage:** 32 blocks and 5 headings read against the Tibetan. Line counts match in every block. Mantras are in
Devanagari with no quotation marks (ॐ, तुत्तारे, तुरे, हूँ, त्रट्, फट्, तारे, हर, स्वाहा). Block IDs and
transclusions correct. Honorific use checked: Tārā is उहाँ (2-2, 2-4); her attributes are participles, with
feminine -की/-एकी forms (भएकी, सजिएकी, घेरिएकी, गरिएकी); no non-honorific finite verb is used of her. Plural
subjects take plural verbs (चम्किन्छन् 1-20, हुन्छन् 2-2, हटाइनेछन् 2-5, हुनेछन् 2-6). No Hindi drift found.

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| 1-7 | LocaleConvention | Minor | फट् द्वारा ("by phaṭ") writes the postposition apart. The file attaches postpositions to mantra syllables everywhere else: हूँबाट ("from hūṃ", 1-16), तुत्तारेको ("of tuttare", 1-10), तुत्तारेद्वारा ("by tuttare", 1-20). | फट्‌द्वारा (with ZWNJ after the halanta, as in बुद्धिमान्‌ले 2-1) | file 1-10, 1-16, 1-20 |
| 1-8 | Terminology | Minor | कमल-मुखमा ("on the lotus-face") — the lock is कमल मुख ("lotus face"); the checker only loose-matches the hyphenated form. | कमल मुखमा | termbase `lotus_face` (1-8); bo 1-8 l.3 ཆུ་སྐྱེས་ཞལ |
| 1-9 | Fluency | Minor | जसको हत्केला … चक्रले सजिएको, ("whose palm … adorned with the wheel,") has no verb, so line 4's फैलाउने ("who spreads") can read as the palm spreading the light. In the Tibetan the light is hers (འཁྲུག་མ). | जसको हत्केला … चक्रले सजिएको छ, ("whose palm is adorned …") — then line 4 returns to her, as in 1-8 (जसको कमल-मुखमा … छ, / … वध गर्ने) | bo 1-9 l.4 རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ |
| 1-9 | Terminology | Minor | सम्पूर्ण दिशाहरूको ("of all the directions") for མ་ལུས་ཕྱོགས. The file renders མ་ལུས as अशेष ("without exception") in 1-4, 1-8 and 1-18. | अशेष दिशाहरूको चक्रले ("with the wheel of the directions without exception") | bo 1-9 l.3 མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས; en 1-9 "wheel of all directions without exception" |
| 1-13 | Fluency | Minor | दाहिने तन्काएको र देब्रे खुम्च्याई चारैतिरबाट आनन्दले घेरिएकी ("right extended [participle] and left drawing in [conjunctive], surrounded by joy") mixes two verb forms and ties the posture to "surrounded". In the Tibetan and English the posture goes with destroying the army. | दाहिने तन्काई र देब्रे खुम्च्याई, चारैतिरबाट आनन्दले घेरिएकी, ("with right extended and left drawn in, surrounded by joy,") — the conjunctives then attach to line 4 नष्ट गर्ने | bo 1-13 l.3–4 གཡས་བརྐྱང་གཡོན་བསྐུམ་…། དགྲ་ཡི་དཔུང་ནི་རྣམ་པར་འཇོམས་མ; en 1-13 |
| 1-14 | Accuracy/Mistranslation | Minor | क्रोधित भृकुटी सहितको हूँ अक्षरद्वारा ("by the hūṃ syllable that has a wrathful frown") gives the frown to the syllable. Tibetan: she makes a wrathful frown, and with the syllable hūṃ … | क्रोधित भृकुटी र हूँ अक्षरद्वारा ("with a wrathful frown and the syllable hūṃ"), as 1-11; locked हूँ अक्षर kept | bo 1-14 l.3 ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཱུྃ་གིས; en 1-14 "With a wrathful frown and the syllable hum"; ne consensus (1-11 frown and HŪṂ) |
| 1-15 | Fluency | Minor | महान् पाप ("great sin"): महान् is a praising word ("great, noble") and reads oddly with पाप. The file compounds महा- elsewhere: महाविष (2-4), महामारी (1-20, 2-5), महाभयङ्करी (1-8). | महापाप ("grave sin"); lock महा kept | bo 1-15 l.4 སྡིག་པ་ཆེན་པོ; ne consensus 2-4 ("महाविष is one word") |
| 1-15 | LocaleConvention | Minor | ॐ सँग ("with oṃ") — postposition written apart (see 1-7). | ॐसँग | file 1-16 हूँबाट |
| 1-17 | LocaleConvention | Minor | हूँ को स्वरूपको ("of the form of hūṃ") — postposition written apart, one verse after हूँबाट (1-16). | हूँको स्वरूपको | file 1-16 |
| 1-17 | Fluency | Minor | मेरु, मन्दर र विन्ध्य पर्वत, / तीनै लोकहरूलाई ("Meru, Mandara and Vindhya mountains, / the three worlds") — with no "and", line 4 reads as an apposition (the mountains *are* the three worlds), and only the second item takes लाई. | मेरु, मन्दर, विन्ध्य पर्वत र / तीनै लोकहरूलाई हल्लाउने ("Meru, Mandara, the Vindhya mountains and the three worlds she shakes"); Vindhya kept (decision) | bo 1-17 l.3–4 རི་རབ་མན་དཱ་ར་དང་འབིགས་བྱེད། འཇིག་རྟེན་གསུམ་རྣམས་གཡོ་བ; en 1-17 "And all the three worlds" |
| 1-18 | Fluency | Minor | सम्पूर्ण विषहरूलाई अशेष रूपले ("all poisons entirely") says "all" twice. The Tibetan has one word, མ་ལུས (रྣམས is the plural). Same kind of doubling the Hindi QA fixed at 1-4. | विषहरूलाई अशेष रूपले हटाउने ("removes the poisons without exception") | bo 1-18 l.4 དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མ |
| 1-20 | LocaleConvention (spelling) | Minor | भयंकर ("terrible") with anusvara. The file keeps Sanskrit nasal consonants (महाभयङ्करी 1-8, जङ्गम 2-4, शान्ति, मन्त्र, आनन्द, अनन्त), as the word list's `_meta` states. | भयङ्कर | `ne-decisions-general.json` _meta ("Nepali keeps the Sanskrit nasal consonants"); ne consensus reviewer note "भयङ्करी / भयंकर spelling" |
| 1-21 | Fluency (punctuation) | Minor | Comma between object and verb: समूहहरूलाई, / नष्ट गर्ने ("the hosts, / destroying"). | Drop the comma: समूहहरूलाई / नष्ट गर्ने | — |
| 2-4 | LocaleConvention (spelling) | Minor | भयंकर — as 1-20. | भयङ्कर | as 1-20 |
| 2-6 | Fluency | Minor | धनहरू नै ("wealths themselves") — धन ("wealth") is a mass noun; the plural reads oddly. The Tibetan རྣམས is only the plural marker. | धन नै प्राप्त गर्नेछ ("will obtain wealth itself") | bo 2-6 l.3 ནོར་རྣམས་ཉིད་ཐོབ; en 2-6 "will obtain wealth" |

**Counts:** 0 critical · 0 major · 15 minor. Profile: Fluency 7 (1-9, 1-13, 1-15, 1-17, 1-18, 1-21, 2-6) ·
LocaleConvention 5 (1-7, 1-15, 1-17, 1-20, 2-4) · Terminology 2 (1-8, 1-9) · Accuracy/Mistranslation 1 (1-14) ·
Style/Register 0 · Audience 0 · Markup/BlockID 0.

### Neutral (logged, not penalised)

- **1-1** शूरवीर ("hero, warrior") for དཔའ་མོ ("heroine") has no feminine ending; the same word serves Māra's
  champions in 1-8 (དཔའ་བོ). वीरा is the feminine option. For the reviewer.
- **1-1, 1-2, 1-13, 1-20; I-2, 1-14** जस्तो / जस्तै ("like") and सहित ("with") are written apart. Nepali
  orthography joins नामयोगी (बिजुलीजस्ता, लाभसहित), but the separate form is widespread; consistent within the file.
- **1-4, 1-6** सेवितलाई, पूजितलाई ("to the one served / worshipped") — the only refrain lines with -लाई; the rest end
  in a participle (…गर्ने, …भएकी). The short refrain वन्दना … is already a reviewer item (consensus).
- **1-10** दिने, तेजोमय / मुकुटबाट ("who brings, majestic / crown") splits adjective and noun across the line; this is
  the consensus wording and mirrors the Tibetan and English line break (བརྗིད་པའི / དབུ་རྒྱན; "majestic / Crown").
- **1-15** सुखी ("happy") beside feminine कल्याणी, शान्ता — reviewer item in the consensus.
- **1-18** देवतालको ("of the divine lake") may be misread as देवता + ल; दिव्य तालको is the plain alternative.
- **1-20** अत्यन्त ("very") in lines 2 and 4 (Tibetan རབ, ཤིན་ཏུ).
- **2-1** भक्ति ("devotion"): the Hindi QA moved to श्रद्धा because of the Hindi contract's no-Hindu-idiom rule; the
  Nepali contract has no such rule and भक्ति is current among Nepali Buddhists. जो बुद्धिमान्‌ले ("whichever wise one")
  is the consensus wording; जुन बुद्धिमान्‌ले is the more standard relative adjective — for the reviewer.
- **2-5** सम्पूर्ण ("all") before दुःखका समूहहरू has no word in the Tibetan (སྡུག་བསྔལ་ཚོགས); meaning unchanged.
- **2-6** पुत्र ("son") for བུ; the English has "child". Literal; सन्तान is the neutral option.
- **Throughout** पूर्ण रूपले, locked for ཡང་དག ("perfectly"), is also used for རྣམ་པར / རབ་ཏུ (1-3, 1-7, 1-8, 1-9, 1-11,
  1-13, 1-16, 2-2, 2-4, 2-5). Not a lock conflict; a reviewer may want variety.
- **Spelling** भृकुटी (1-8, 1-11, 1-14) vs Sanskrit भृकुटि; हजारौं vs हजारौँ (1-2). Both forms are current.
- **1-21, 2-5** ग्रह for གདོན — Tenkal decision, flagged (might read as "planet").

### Top fixes

1. **1-14** give the frown to her, not to the syllable: क्रोधित भृकुटी र हूँ अक्षरद्वारा.
2. **1-9** add छ so the surging light is hers, not the palm's; and अशेष for མ་ལུས.
3. **1-13** consistent posture verbs, tied to the destroying: दाहिने तन्काई र देब्रे खुम्च्याई, ….
4. **1-17** "and the three worlds": मेरु, मन्दर, विन्ध्य पर्वत र / तीनै लोकहरूलाई.
5. **1-15** महापाप for महान् पाप.

Also quick: भयङ्कर (1-20, 2-4); attached postpositions (1-7, 1-15, 1-17); कमल मुखमा (1-8); drop सम्पूर्ण (1-18);
drop comma (1-21); धन नै (2-6).

## Re-check after fixes (draft 6) — 2026-09-25

**Fixes:** 15 of 15 Minor findings applied (see `ne-general/reports/qa-fixes-log-ne-general.md`). Neutral rows not
applied. No settled/Tenkal decision, consensus fix or locked word changed.

**Stage 0 (mechanical):** `mqm_mechanical_checks.py <file> --source <root>` (re-run → `$HOME/qa-ne/stage0-ne-d6.json`)
— 32 distinct verse IDs, 32 transclusions, 0 critical / 0 major / 0 minor. Stage-0 gate PASS-so-far.
**Alignment:** `check_translation_alignment.py` — OK (32 segments, 5 headings; every block keeps its line count).
**Terminology (mechanical):** `check_termbase_consistency.py --lang ne` — 136/136 locked words found, 0 loose
(1-8 कमल मुख now exact), 1 covered by a longer locked phrase (a-1, unchanged), 0 misses.
1-15 महा is met in महापाप.
**Lint:** `lint_text_input.py` — OK (WARNs only: alt_titles, translator ids, languages API cache — unchanged from draft 5).

**Re-read:** the 15 draft-5 rows and every changed line. All 15 resolved; no new error found in the changed lines.
This re-check covers the listed findings and the edits. It is not a fresh full Stage 1 run.

**Word count:** 580 (same method as the draft-5 run, which counted 583).
**Counts:** 0 critical · 0 major · 0 minor.
**Score:** 100 − (0 / 580) × 100 = **100.0 / 100**   **Gate:** PASS — may go to native review; stays `draft`.

Still open for the reviewer (neutral, unchanged): the short refrain वन्दना …गर्ने; ग्रह in 1-21/2-5 (might read as
"planet"); 1-15 सुखी; 1-1 शूरवीर; 1-18 देवतालको; 2-1 भक्ति / जो बुद्धिमान्‌ले; भृकुटी vs भृकुटि.

**This is an LLM self-check.** It is not a sign-off.
