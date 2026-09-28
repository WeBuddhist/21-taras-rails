---
title: Phase 2 fixes log — Hindi (general), draft 2
translation: 3-TRANSFORMATIONS/Translations/hi-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-hi-general.md
base: 3-TRANSFORMATIONS/Translations/Gemini/hi/ (Gemini zero-shot, 2026-09-17)
termbase: 0-INBOX/AI_translation/keyword-extraction-dharmamitra/hi/en-bo-hi-termbase-general.json (51 entries: 47 + 4 Hindi-only)
date: 2026-09-24
result: "locked words 123/136 (90%) → 136/136"
---

# Phase 2 fixes — Hindi, draft 2

The Gemini draft was kept word for word; only locked words were substituted, verse by verse
(graded-translate Phase 2, "enforce on a machine draft").

| Verse | Lock | Before | After |
|---|---|---|---|
| I-0 | homage | नामार्थ और अनुवादक की वंदना | नामार्थ और अनुवादक का नमस्कार |
| I-1 | sanskrit_title | … स्तोत्र गुण हित साक | … स्तोत्र गुणहित साक |
| I-3 | noble_venerable | ॐ आर्या भगवती तारा को नमस्कार है। | ॐ! पूज्य आर्या तारा को नमस्कार है। |
| 1-2 | moon | सौ पूर्ण चंद्रमाओं | सौ पूर्ण चन्द्रमाओं |
| 1-4 | without_exception | सम्पूर्ण पारमिताओं को प्राप्त कर लिया है | समस्त पारमिताओं को अशेष प्राप्त कर लिया है |
| 1-5 | syllable | तुत्तारे और हूँ बीजाक्षरों से | तुत्तारे और हूँ अक्षर से |
| 1-9 | light | अपनी रश्मियों के समूहों को | अपने प्रकाश के समूहों को |
| 1-10 | supreme, joy | जो अत्यंत मुदित और तेजोमय हैं | जो परम आनंद और तेजोमय हैं |
| 1-13 | joy | … मुदित चक्र में स्थित हैं | … आनंद-चक्र में स्थित हैं |
| 1-16 | joy | जो अत्यंत मुदित चक्र से घिरी हैं | जो आनंद-चक्र से घिरी हैं |
| 1-18 | tara_syllable | दो बार तारा और फट् | दो बार तारे और फट् |
| 1-21 | perfectly, perfectly_endowed | और पूर्ण शांति की शक्ति से युक्त हैं | और शांति की शक्ति से पूर्णतः युक्त हैं |

**Word-list changes made while enforcing** (in `hi-decisions-general.json`, termbase rebuilt, `hi_text` kept):
`great` locked as the stem महा (covers महान्, महाभयंकर, महानता); `moon` as the stem चन्द्र (covers
अर्धचन्द्र in 1-12); `perfectly_endowed` as the contiguous पूर्णतः युक्त; four Hindi-only mantra entries
added (ॐ, स्वाहा, हर, तारे).

**Not changed here** (left for the meaning check): wording outside the locked words.
