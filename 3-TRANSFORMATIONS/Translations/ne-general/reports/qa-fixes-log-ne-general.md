---
title: translation-qa fixes log — Nepali (general)
file_type: report
translation: 3-TRANSFORMATIONS/Translations/ne-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general.md
qa_report: 3-TRANSFORMATIONS/Translations/ne-general/reports/qa-report.md
from_draft: 5
to_draft: 6
date: 2026-09-25
fixes_applied: 15
approved_by: Tenkal (applying the QA fixes, as for English, Chinese, Vietnamese and Hindi)
---

# QA fixes — Nepali, general grade (draft 5 → draft 6)

All 15 findings of the 2026-09-25 QA run were Minor (0 Critical, 0 Major). All 15 were applied. None
contradicts a settled decision (the English decisions; Tenkal's 1-11 दरिद्रता, 1-7 "amid fire",
बोधिसत्त्व/बुद्ध, ग्रह) or the Nepali/English commentary consensus, and none removes a locked word. Every block
keeps its line count and block ID. Nothing was added that is not in the Tibetan. The ZWNJ in फट्‌द्वारा follows
the file's own form in बुद्धिमान्‌ले (2-1).

| # | Verse | Before | After (English gloss) | QA row / basis |
|---|---|---|---|---|
| 1 | 1-7 | वन्दना त्रट् र फट् द्वारा, | वन्दना त्रट् र फट्‌द्वारा, ("Homage — by traṭ and phaṭ,") — postposition attached, as हूँबाट, तुत्तारेद्वारा | 1-7 LocaleConvention |
| 2 | 1-8 | जसको कमल-मुखमा क्रोधित भृकुटी छ, | जसको कमल मुखमा क्रोधित भृकुटी छ, ("on whose lotus face is a wrathful frown") — exact lock कमल मुख (checker: 0 loose) | 1-8 Terminology; termbase `lotus_face` |
| 3 | 1-9 | जसको हत्केला सम्पूर्ण दिशाहरूको चक्रले सजिएको, | जसको हत्केला अशेष दिशाहरूको चक्रले सजिएको छ, ("whose palm is adorned with the wheel of the directions without exception,") — line 4 फैलाउने now returns to her; consensus palm wording kept | 1-9 Fluency + 1-9 Terminology; bo 1-9 l.3–4 |
| 4 | 1-13 | दाहिने तन्काएको र देब्रे खुम्च्याई चारैतिरबाट आनन्दले घेरिएकी, | दाहिने तन्काई र देब्रे खुम्च्याई, चारैतिरबाट आनन्दले घेरिएकी, ("with right extended and left drawn in, surrounded by joy on all sides,") — the posture goes with line 4 नष्ट गर्ने | 1-13 Fluency; bo 1-13 l.3–4; en 1-13 |
| 5 | 1-14 | क्रोधित भृकुटी सहितको हूँ अक्षरद्वारा, | क्रोधित भृकुटी र हूँ अक्षरद्वारा, ("with a wrathful frown and the syllable hūṃ,") — as 1-11; locked हूँ अक्षर kept | 1-14 Accuracy/Mistranslation; bo 1-14 l.3 ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཱུྃ་གིས |
| 6 | 1-15 | स्वाहा र ॐ सँग पूर्ण रूपले युक्त भई, | स्वाहा र ॐसँग पूर्ण रूपले युक्त भई, ("perfectly endowed with svāhā and oṃ,") — locked ॐ, पूर्ण रूपले युक्त kept | 1-15 LocaleConvention |
| 7 | 1-15 | महान् पाप नष्ट गर्ने। | महापाप नष्ट गर्ने। ("who destroys grave sin") — lock महा kept; compounded like महाविष, महामारी | 1-15 Fluency; bo 1-15 l.4 སྡིག་པ་ཆེན་པོ |
| 8 | 1-17 | हूँ को स्वरूपको बीज भएकी, | हूँको स्वरूपको बीज भएकी, ("who is the seed in the form of hūṃ,") | 1-17 LocaleConvention |
| 9 | 1-17 | मेरु, मन्दर र विन्ध्य पर्वत, / तीनै लोकहरूलाई हल्लाउने। | मेरु, मन्दर, विन्ध्य पर्वत र / तीनै लोकहरूलाई हल्लाउने। ("who shakes Meru, Mandara, the Vindhya mountains and the three worlds") — Vindhya kept (decision) | 1-17 Fluency; bo 1-17 l.3–4; en 1-17 |
| 10 | 1-18 | सम्पूर्ण विषहरूलाई अशेष रूपले हटाउने। | विषहरूलाई अशेष रूपले हटाउने। ("who removes the poisons without exception") — locked अशेष kept | 1-18 Fluency; bo 1-18 l.4 དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མ |
| 11 | 1-20 | अत्यन्त भयंकर महामारी हटाउने। | अत्यन्त भयङ्कर महामारी हटाउने। ("who dispels the most terrible epidemics") — Sanskrit nasal, as महाभयङ्करी | 1-20 LocaleConvention (spelling) |
| 12 | 1-21 | ग्रह, वेताल र यक्ष समूहहरूलाई, / नष्ट गर्ने … | ग्रह, वेताल र यक्ष समूहहरूलाई / नष्ट गर्ने … ("who destroys the hosts of grahas, vetālas and yakṣas") — comma dropped; ग्रह kept (decision) | 1-21 Fluency (punctuation) |
| 13 | 2-4 | अत्यन्त भयंकर महाविष, | अत्यन्त भयङ्कर महाविष, ("the most terrible great poison,") — consensus महाविष kept | 2-4 LocaleConvention (spelling) |
| 14 | 2-6 | धन चाहनेले धनहरू नै प्राप्त गर्नेछ, | धन चाहनेले धन नै प्राप्त गर्नेछ, ("one who wants wealth will obtain wealth itself,") | 2-6 Fluency; bo 2-6 l.3 ནོར་རྣམས་ཉིད་ཐོབ |

(Row 3 covers two QA rows: 1-9 Fluency and 1-9 Terminology. 14 rows, 15 findings.)

Frontmatter: `draft: 6`; draft_history entry 6 added ("(this file)" moved from entry 5); `qa_report`,
`qa_fixes_log`, `qa_fixes_applied: 15`; `rails_used` adds translation-qa (MQM); `revised: 2026-09-25`; `note`
updated ("Sixth draft …"). The grade file (`bo_ne_keyword_general.json`) was not touched.

Checked after the fixes: alignment OK (32 segments, 5 headings), locked words 136/136 (0 loose), Stage 0
0 findings, linter OK.

## Not applied

- **Critical/Major:** none reported.
- **Minor:** none left out — no QA row contradicted a settled/Tenkal decision or the consensus, none changed a
  locked rendering, and none was only a preference.
- **Neutral rows (logged, not penalised) — not applied, by rule:** 1-1 शूरवीर (no feminine ending);
  जस्तो/सहित written apart; 1-4/1-6 -लाई refrain endings; 1-10 line break दिने, तेजोमय / मुकुटबाट (consensus wording,
  mirrors the Tibetan and English break); 1-15 सुखी (consensus reviewer item); 1-18 देवतालको; 1-20 अत्यन्त twice;
  2-1 भक्ति and जो बुद्धिमान्‌ले (consensus wording); 2-5 सम्पूर्ण; 2-6 पुत्र; spread of पूर्ण रूपले; भृकुटी/भृकुटि
  and हजारौं/हजारौँ spelling; ग्रह (Tenkal decision, kept).

## For the word list

- **1-9, 1-18 མ་ལུས → अशेष** — not locked in these verses (locked in 1-4, 1-8). Suggest locking it there.
- **1-14 ཁྲོ་གཉེར → क्रोधित भृकुटी** (1-8, 1-11, 1-14 now all have it) — candidate entry; spelling भृकुटी vs Sanskrit
  भृकुटि needs a decision.
- **1-15 ཆེན་པོ → महा** is now met by महापाप (a compound, as महाविष, महामारी). The lock hint महान् is right for
  2-3 (महानता) but not as a free adjective before a noun; note on the `great` entry.
- **Spelling policy:** भयङ्कर (Sanskrit nasal) is now used throughout (1-8, 1-20, 2-4). If the word list wants a
  rule for tatsam nasals, `_meta` already states one ("Nepali keeps the Sanskrit nasal consonants").
- **Postpositions after mantra syllables** are now attached throughout (फट्‌द्वारा, ॐसँग, हूँको, हूँबाट, तुत्तारेको,
  तुत्तारेद्वारा). For the style file, if wanted.
