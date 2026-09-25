---
title: QA fixes log — Mongolian (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-mn-general.md
qa_report: 3-TRANSFORMATIONS/Translations/mn-general/reports/qa-report.md
from_draft: 5
to_draft: 6
date: 2026-09-25
fixes_applied: 17
---

# QA fixes log — Mongolian, general grade (draft 5 → 6)

Applied with the project owner's approval (Tenkal). The QA run of 2026-09-25 had 0 critical, 0 major and 17 minor rows. All 17 are applied (16 line edits in 14 blocks; the 1-17 edit covers two rows). The Neutral rows are not applied. Every block keeps its ID and line count; nothing is added that the Tibetan lacks; the 136 locked words are all still present.

| Verse | Before | After (English gloss) | QA row |
|---|---|---|---|
| I-2 | Төвөд хэлээр: Дарь эхэд мөргөх хорин нэгэн магтаал, ач тусын хамт. | Төвөд хэлээр: Дарь эхэд хорин нэгэн мөргөлөөр магтсан магтаал, ач тусын хамт. ("In Tibetan: the praise to Tārā in twenty-one homages, with its benefits") | Accuracy/Mistranslation. Tibetan ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ; English "The Praise to Tara in Twenty-One Homages" |
| 1-2 | Үнэнхүү дэлгэрсэн гэрэл бадрагч танаа. | Машид дэлгэрсэн гэрэл бадрагч танаа. ("you who blaze with fully opened light") | Accuracy/Mistranslation. Tibetan རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ; locked гэр, бад kept |
| 1-6 | Чөтгөр, босоолой, үнэр идэгчид болон, | Чөтгөр, босоо үхдэл, үнэр идэгчид болон, ("spirits, vetālas, gandharvas and") | Terminology. word list `vetala` hint *босоо үхдэл*; lock *босоо* kept |
| 1-6 | Хорлогч чуулганаар өмнөөс магтаал өргөгдсөн танаа. | Хорлогч чуулганаар өмнө тань магтаал өргөгдсөн танаа. ("you, praised before you by the hosts of yakṣas") | Fluency (*өмнөөс* reads "on behalf of"). Tibetan མདུན་ནས་བསྟོད་མ; English "Praised before you" |
| 1-12 | Үргэлжид машид гэрэл цацруулагч танаа. | Үргэлж машид гэрэл цацруулагч танаа. ("constantly radiates intense light") | Style/Register (classical *-ид*). Tibetan རྟག་པར |
| 1-15 | Суха болон ум-тай сайтар төгссөнөөр, | Суха болон умтай сайтар төгссөнөөр, ("perfectly endowed with svāhā and oṃ") | LocaleConvention (hyphen before suffix) |
| 1-16 | Увидас тарнийн хум-ээс зул болсон танаа. | Увидас тарнийн хумаас зул болсон танаа. ("the lamp from the HŪṂ of the knowledge-mantra") | Fluency (vowel harmony *-аас*) + hyphen. mn consensus 1-16 wording kept |
| 1-17 | Хум-ын дүрт үр бүхий, | Хумын дүрт үр болсон, ("who are the seed in the form of HŪṂ") | Accuracy/Mistranslation (ཉིད་མ "who is") + LocaleConvention. English "Whose essence is the seed-syllable in the form of hum" |
| 1-18 | Хоёр дарэ-г өгүүлээд пад үсгээр, | Хоёр дарэг өгүүлээд пад үсгээр, ("saying tāra twice, with the syllable phaṭ") | LocaleConvention |
| 1-20 | Хоёр хара-г өгүүлээд дүдарэ-гээр, | Хоёр хараг өгүүлээд дүдарэгээр, ("saying hara twice, with tuttāre") | LocaleConvention |
| 1-21 | Ад, босоолой болон хорлогчдын чуулганыг | Ад, босоо үхдэл болон хорлогчдын чуулганыг ("the hosts of demons, vetālas and yakṣas") | Terminology. word list `vetala` |
| 1-21 | Дарагч, дүрэ дээд хутагт танаа. | Дарагч, дүрэ, дээдийн дээд танаа. ("you who destroy them, Ture, highest of the high") | Accuracy/Addition (*хутагт* not in the Tibetan). Tibetan འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ; English "the supreme Ture who destroys"; locked дүрэ, дара kept |
| 2-1 | Ухаан төгс хэн бөгөөс сайтар өгүүлснээр, | Ухаан төгс хэн боловч сайтар өгүүлснээр, ("any wise one who recites it well") | Style/Register (classical *бөгөөс*). Tibetan བློ་ལྡན་གང་གིས; locked төгс kept |
| 2-3 | Түргэнээ авшиг хүртэх болно, | Түргэн авшиг хүртэх болно, ("will quickly receive empowerment") | Fluency. Tibetan མྱུར་དུ; locked авшиг kept |
| 2-4 | Бат орших ба эсвэл хөдлөх, | Бат орших эсвэл хөдлөх, ("stationary or moving") | Fluency (*ба* + *эсвэл*). Tibetan བརྟན་གནས་པའམ |
| 2-6 | Хоёр, гурав, долоон удаа илт өгүүлвээс, | Хоёр, гурав, долоон удаа илт өгүүлбэл, ("if one recites it clearly two, three or seven times") | Style/Register (classical *-вээс*). Tibetan མངོན་པར་བརྗོད་ན |

Rows counted: I-2, 1-2, 1-6 (Terminology), 1-6 (Fluency), 1-12, 1-15, 1-16, 1-17 (Accuracy), 1-17 (LocaleConvention), 1-18, 1-20, 1-21 (Terminology), 1-21 (Addition), 2-1, 2-3, 2-4, 2-6 = **17**.

## Not applied

| Verse | QA row | Reason |
|---|---|---|
| — | (no scored row) | All 17 scored rows were applied; none contradicted a settled or Tenkal decision, the consensus, or a locked rendering. |
| Neutral rows | *танаа*, *дияан*, *уснаа ургасан*, *Түүнчлэн ирсэн*, *чухаг дээд гурав* / *мутарлага*, *хэлхээ* / *хүрээ*, *бутниргэгч*, *билээ*, *айдасгүйг*, *ч бас*, a-0 heading, tooling | Neutral: preferences or native-reviewer questions, not errors. *уснаа ургасан* is the Phase 2 wording; *танаа* goes with the settled refrain. |

## For the word list

1. **vetala (རོ་ལངས).** The lock is the stem *босоо*; the file now uses the hint *босоо үхдэл* in 1-6 and 1-21 (it had *босоолой*). If the list wants the full form enforced, lock *босоо үхдэл*.
2. **Suffixes on mantra syllables.** The file now attaches case suffixes directly, with Khalkha harmony (*умтай, хумаас, хумын, дарэг, хараг, дүдарэгээр, падаар, Дүдарэгийн*). Worth recording as a rule for all Mongolian grades.
3. **No locks for 2-2, 2-4, 2-6** in `bo_mn_keyword_general.json`; the script cannot check them. The grade file was not edited.
4. **Locked renderings.** None was changed; the termbase check still finds 136/136.
5. For the native reviewer (unchanged): 2-1 *охин тэнгэр* (also Palden Lhamo), 1-16 *увидас*, 1-19 *киннара*, 1-17 *Бигжид*, 1-3 *дияан*, 1-9 *чухаг дээд гурав*.
