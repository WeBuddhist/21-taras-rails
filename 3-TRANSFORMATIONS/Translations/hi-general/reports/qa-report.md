---
title: MQM quality check — Hindi (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-hi-general.md
skill: Webuddhist-Skills/rails/translation-qa
note: "Runs are appended, dated. Never overwrite an earlier run."
---

# QA report — Hindi, general grade

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-hi-general.md (draft 4) — 2026-09-24

**Score:** 96.6 / 100   **Gate:** PASS (0 critical, 0 major) — the file may go to native review; it stays `draft`
**Profile:** Fluency 19 · Accuracy 6 (Mistranslation 3, Omission 2, Addition 1) · Terminology 3 · Style/Register 2 · Audience 0 · LocaleConvention 0 · Markup/BlockID 0 — all 30 Minor
**Word count:** 880 Hindi words (space-separated Devanagari tokens in the 32 blocks and 5 headings; frontmatter, transclusion lines and `^` IDs excluded)
**Formula:** 100 − (30 × 1 / 880) × 100 = 96.59

**This is an LLM self-check.** It is not a sign-off. A native Hindi reader and a domain specialist decide.

**Rails basis:** `2-RAILS/Verses/` is empty for this text. Accuracy was scored against the Tibetan critical edition
(`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), the Hindi consensus
(`hi-general/reports/commentary-fact-check-consensus-hi-general.md`) and the English consensus
(`en-general/reports/commentary-fact-check-consensus-en-general.md`). The fact-checked English
(`en-general/bo-…-en-general.md`, draft 3) is the meaning reference. Translator decisions and translator notes in the
frontmatter are not counted as errors.

**Requirements basis:** there is no `requirements.md`. The contract is the Hindi **general** row of
`graded-translate/SKILL.md` § Registers ("Modern standard Hindi. Sanskrit Buddhist terms used freely. Flowing prose."),
its Liturgy note (mantras and Sanskrit title in Devanagari; no जिन / जिनपुत्र), and the Hindi section of
`keyword-standardize/SKILL.md` (Sanskrit spelling, mantra forms, no Hindu-devotional idiom).

**Stage 0 (mechanical):** `$HOME/qa/stage0-hi.json` — 32/32 blocks, 32 transclusions, 0 findings.
**Terminology (mechanical):** `check_termbase_consistency.py --lang hi` — 136/136 locked words found, 0 loose,
0 misses (same with `--strict-diacritics`). The 3 Terminology findings below are words the grade file does not lock
in that verse, but that break the file's own consistency.

**Coverage:** 32 blocks and 5 headings read. Line counts match the Tibetan in every block. Mantras are in Devanagari
(ॐ, तुत्तारे, तुरे, हूँ, त्रट्, फट्, तारे, हर, स्वाहा). Block IDs and transclusions are correct. No Urdu drift found.

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| 1-1 | Fluency (punctuation) | Minor | Line-end comma cuts a genitive from its noun: कमल के, / प्रस्फुटित केसर ("of the lotus, / the opening stamens"). | Drop the comma: कमल के / प्रस्फुटित केसर | — |
| 1-2 | Fluency (agreement) | Minor | समूहों के … आभा से ("of the hosts … by the radiance"). आभा ("radiance") is feminine, so the genitive must be की. | तारों के समूहों की / अत्यधिक प्रकाशमान आभा से | — |
| 1-2 | Fluency (punctuation) | Minor | Same comma problem: समूहों के, / … आभा ("of the hosts, / … radiance"). | Drop the comma (with the fix above). | — |
| 1-3 | Fluency (punctuation) | Minor | Comma splits adjective from noun: जल से उत्पन्न, / स्वर्णिम-नीले कमल ("water-born, / gold-blue lotus"). | जल से उत्पन्न / स्वर्णिम-नीले कमल | — |
| 1-4 | Fluency | Minor | अशेष सभी पारमिताओं ("all the perfections, without remainder, all") says "all" twice. The locked अशेष was added beside the draft's सभी. The Tibetan has one word: མ་ལུས་ཕ་རོལ་ཕྱིན་པ. | अशेष पारमिताओं को प्राप्त कर चुके | bo 1-4 l.3 |
| 1-4 | Fluency | Minor | जिनका अत्यंत आश्रय लेते हैं ("whose extreme refuge they take"). An intensifier before a noun reads oddly. Tibetan ཤིན་ཏུ་བསྟེན "rely on deeply". | जिनका गहरा आश्रय लेते हैं, or जिनकी भली-भाँति सेवा करते हैं | bo 1-4 l.4 |
| 1-7 | Terminology | Minor | The Tibetan line has ཞབས ("feet"), locked to चरण ("feet") in 1-5, 1-14 and 1-17. Here it is पैर ("leg"). Also आक्रांत करती हैं ("trample") has no object or instrument. | दायाँ चरण सिकोड़कर और बायाँ फैलाकर, चरणों से आक्रांत करती हैं — or keep पैर and add चरणों से | bo 1-7 l.3 གཡས་བསྐུམ་གཡོན་བརྐྱང་ཞབས་ཀྱིས་མནན་ཏེ |
| 1-7 | Fluency (spelling) | Minor | बायां ("left") — the standard spelling has chandrabindu. | बायाँ | — |
| 1-8 | Fluency | Minor | भृकुटी धारण करती हैं ("hold an eyebrow"). भृकुटी alone is "eyebrow"; धारण ("hold, wear") does not make a frown. Tibetan ཁྲོ་གཉེར "wrathful frown". Translator flagged it. Sanskrit spelling is भृकुटि. | अपने कमल मुख पर भृकुटि चढ़ाती हैं ("knit the brow on her lotus face") | bo 1-8 l.3 ཁྲོ་གཉེར་ལྡན་མཛད; en 1-8 "forms a frowning expression" |
| 1-9 | Fluency | Minor | Line 3 starts a new relative (जिनकी हथेली "whose palm"). Line 4 then has no subject, so the palm could be read as the one that radiates. | और जो अपने प्रकाश के समूहों को क्षुब्ध कर विकीर्ण करती हैं | bo 1-9 l.4 རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ |
| 1-10 | Fluency | Minor | Line 1 carries two clauses and splits adjective from noun across the line break: जिनका तेजोमय / मुकुट ("whose radiant / crown"). Reads stiffly after the locked-word change. | उनको नमस्कार, जो तेजस्वी, परम आनंद देने वाली हैं, / जिनका मुकुट प्रकाश की मालाएँ फैलाता है, | bo 1-10 l.1–2; en 1-10 |
| 1-11 | Accuracy/Mistranslation | Minor | सम्पूर्ण रूप से आकर्षित ("summon completely"). Tibetan ཐམས་ཅད་འགུགས is "summon all" (all the hosts). | पृथ्वी के रक्षकों के सभी समूहों को / आकर्षित करने में समर्थ हैं | bo 1-11 l.2; en 1-11 "All the hosts of guardians" |
| 1-11 | Fluency (spelling) | Minor | कंपित ("trembling") here, कम्पित in 1-17. Same word, two spellings. | कम्पित in both (the Sanskrit spelling the Hindi contract asks for) | keyword-standardize § Hindi "Script" |
| 1-12 | Accuracy/Addition | Minor | अर्धचन्द्र का मुकुट ("a crown of the half-moon") adds a crown. Tibetan ཟླ་བའི་རྩེ་མོས་དབུ་བརྒྱན "head adorned with the crescent". मुकुट is already the word for 1-10's head ornament. | जिनका शीश अर्धचन्द्र से अलंकृत है | bo 1-12 l.1; en 1-12 |
| 1-12 | Style/Register | Minor | उत्सर्जित होता है ("is emitted") is technical, science-report Hindi. | निरंतर अत्यधिक प्रकाश फैलता है | — |
| 1-13 | Fluency | Minor | The posture (दाहिना पैर फैलाकर … सिकोड़कर "right leg extended … bent") is tied to घिरी हैं ("are surrounded"). You do not stretch a leg in order to be surrounded. In the Tibetan and English the posture goes with destroying the armies. | जो दायाँ पैर फैलाए, बायाँ सिकोड़े, चारों ओर आनंद से घिरी, / शत्रुओं की सेनाओं का पूर्णतः विनाश करती हैं। (fold line 4's और जो) | bo 1-13 l.3–4; en 1-13 |
| 1-13 | Fluency (spelling) | Minor | बायां ("left") → chandrabindu. | बायाँ | — |
| 1-14 | Accuracy/Omission | Minor | अपनी भृकुटी ("with her eyebrow") drops the wrath. Tibetan ཁྲོ་གཉེར་ཅན "with a wrathful frown". | क्रुद्ध भृकुटि और हूँ बीजाक्षर से ("with a wrathful frown and the syllable hūṃ") | bo 1-14 l.3; en 1-14 "With a wrathful frown" |
| 1-16 | Fluency | Minor | Line 3 is a new relative (जिनमें "in whom"). Line 4 has no subject, so it can read as the mantra being the lamp. | और जो हूँ विद्याक्षर से उत्पन्न दीपक स्वरूप हैं | bo 1-16 l.4 རིག་པ་ཧཱུྃ་ལས་སྒྲོན་མ་ཉིད་མ |
| 1-18 | Terminology | Minor | सम्पूर्ण विषों को पूर्णतः नष्ट ("all poisons completely destroy"). The word for "without exception" is མ་ལུས, which the file renders अशेष (1-4, 1-8, 1-9). पूर्णतः is locked for ཡང་དག ("perfectly"). | विषों का अशेष निवारण करती हैं ("remove the poisons without exception") | bo 1-18 l.4 དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མ |
| 1-19 | Accuracy/Omission | Minor | ཀུན་ནས ("all-round, universal") is dropped from the armour. आनंदमय और तेजोमय कवच = "joyful and radiant armour". | अपने सर्वव्यापी आनंद के तेजोमय कवच से ("with the radiant armour of all-round joy") | bo 1-19 l.3; en 1-19 "armor of universal joy" |
| 1-20 | Fluency | Minor | Line 1 is very long and line 2 is three words. अत्यंत ("extremely") in lines 2 and 4. | उनको नमस्कार, पूर्ण सूर्य और चन्द्रमा के समान / जिनके दोनों नेत्र प्रखर प्रकाश से उज्ज्वल हैं, | bo 1-20 l.1–2 |
| 1-21 | Accuracy/Mistranslation | Minor | जिन पर तीन तत्त्व विन्यस्त हैं, / और शांति की शक्ति से पूर्णतः युक्त हैं ("on whom the three suchnesses are set, / and [they] are endowed with the might of peace"). युक्त हैं has no gender, so line 2 can read as the three suchnesses having the might. Tibetan ལྡན་མ: she has it. | और जो शांति की शक्ति से पूर्णतः युक्त हैं | bo 1-21 l.2 ཞི་བའི་མཐུ་དང་ཡང་དག་ལྡན་མ; en 1-21 |
| 1-21 | Terminology | Minor | अत्यंत श्रेष्ठ ("extremely excellent") for རབ་མཆོག "supreme". རབ is locked to परम ("supreme") in 1-10. Flagged as a style note in the consensus. | वे परम श्रेष्ठ तुरे हैं | bo 1-21 l.4; hi consensus "Style notes" |
| 1-21 | Fluency (punctuation) | Minor | Comma between object and verb: समूहों का, / विनाश करती हैं ("of the hosts, / destroy"). | Drop the comma. | — |
| 2-1 | Style/Register | Minor | सच्ची भक्ति ("true bhakti") — भक्ति carries Hindu devotional colour. The Hindi contract asks for Buddhist, not Hindu-devotional, idiom. Tibetan གུས "respect, devotion". | देवी के प्रति सच्ची श्रद्धा से युक्त | keyword-standardize § Hindi style.md; bo 2-1 l.1 |
| 2-3 | Fluency | Minor | सात कोटि बुद्धों द्वारा … अभिषेक प्राप्त होगा ("by seventy million Buddhas … empowerment will be obtained") mixes an agent with "receive". | सात कोटि बुद्धों से / शीघ्र ही अभिषेक प्राप्त होगा, | bo 2-3 l.1–2 |
| 2-3 | Accuracy/Mistranslation | Minor | इससे भी महानता प्राप्त करके ("obtaining greatness even from this"). Tibetan འདི་ལས་ཆེ་བ "greater than this". The comparison is lost. | और इससे भी बढ़कर महानता पाकर | bo 2-3 l.3; en 2-3 "even greater excellence than this" |
| 2-4 | Fluency | Minor | निराकरण ("refutation, settling of a complaint") is the wrong word for removing poison. | तो उनके स्मरण से पूर्णतः निवारण हो जाता है | bo 2-4 l.4 སེལ |
| 2-6 | Fluency | Minor | सभी कामनाएँ प्राप्त होंगी ("all wishes will be obtained"). Wishes are fulfilled, not obtained. | सभी कामनाएँ पूर्ण होंगी | bo 2-6 l.4 |

### Neutral (logged, not penalised)

- **Spelling mix.** The contract asks for Sanskrit spelling (चन्द्रमा, not चंद्रमा). The file mixes the two:
  अनन्त, सम्पूर्ण, मन्दर, क्षान्ति beside अत्यंत, प्रचंड, संध्याकाल, अंततः. Two locked words use the anusvara
  (शांति "peace", आनंद "joy"), so full consistency needs a word-list decision first. For the termbase reviewer.
- **I-3** ॐ! — the exclamation mark follows the English "Oṃ!". A danda or no mark is more usual in Hindi liturgy.
- **1-1** केसर means "stamen" here but most Hindi readers know it as "saffron". कमल-केसर is an accepted poetic phrase.
- **1-14** अपने हाथों की हथेलियों ("the palms of her hands") could simply be अपनी हथेलियों ("her palms").
- **1-18** बीजाक्षर ("seed-syllable") for फट् — only हूँ is locked to it. Consistent with the rule that the named
  syllable is बीजाक्षर.
- **1-21, 2-5** ग्रह for གདོན — a translator decision, flagged for the native reviewer (might read as "planets").
- **2-4** དེ་ཡི ("its / their") is not rendered. The meaning is unchanged.
- **2-6** पुत्र ("son") for བུ; the English has "child". Literal to the Tibetan. संतान ("offspring") is the neutral option.

### Top fixes

1. **1-21** add जो to line 2, so the might of peace is clearly hers, not the three suchnesses'.
2. **1-13** attach the posture to the destroying, not to "surrounded by joy".
3. **1-8 / 1-14** give the frown its wrath: भृकुटि चढ़ाती हैं (1-8), क्रुद्ध भृकुटि (1-14).
4. **1-2** fix the agreement: समूहों की … आभा.
5. **1-4, 1-10** undo the stiff locked-word joins: अशेष पारमिताओं; split 1-10 line 1 into "radiant, bringing supreme joy" and "whose crown spreads garlands of light".

Also quick: बायाँ (1-7, 1-13), कम्पित (1-11), श्रद्धा for भक्ति (2-1), इससे भी बढ़कर (2-3), निवारण (2-4).

## Re-check after fixes (draft 5) — 2026-09-24

**Fixes:** 30 of 30 Minor findings applied (see `hi-general/reports/qa-fixes-log-hi-general.md`). Neutral rows
not applied. No Tenkal decision, consensus fix or locked word changed.

**Stage 0 (mechanical):** `mqm_mechanical_checks.py <file> --source <root>` — 32 distinct verse IDs,
32 transclusions, 0 critical / 0 major / 0 minor. Stage-0 gate PASS-so-far.
**Alignment:** `check_translation_alignment.py` — OK (32 segments, 5 headings; every block keeps its line count).
**Terminology (mechanical):** `check_termbase_consistency.py --lang hi` — 136/136 locked words found, 0 loose,
1 covered by a longer locked phrase (a-1, unchanged), 0 misses; same with `--strict-diacritics`.
2-3 महा is still met (in महानता).
**Lint:** `lint_text_input.py` — OK (WARNs only: alt_titles, translator ids — unchanged from draft 4).

**Re-read:** the 30 draft-4 rows and every changed line. All 30 resolved; no new error found in the
changed lines. This re-check covers the listed findings and the edits. It is not a fresh full Stage 1 run.

**Word count:** 874 (same method as the draft-4 run, which counted 880).
**Counts:** 0 critical · 0 major · 0 minor.
**Score:** 100 − (0 / 874) × 100 = **100.0 / 100**   **Gate:** PASS — may go to native review; stays `draft`.

Still open for the reviewer (neutral, unchanged): spelling mix (needs a word-list decision), ग्रह in 1-21/2-5,
1-8 भृकुटि चढ़ाती हैं (new wording, translator note updated), 1-7 चरण beside 1-13 पैर (Tibetan differs).

**This is an LLM self-check.** It is not a sign-off.
