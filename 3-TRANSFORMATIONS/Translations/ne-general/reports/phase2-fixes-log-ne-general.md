---
title: Phase 2 fixes log — Nepali (general), draft 3
translation: 3-TRANSFORMATIONS/Translations/ne-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general.md
base: 3-TRANSFORMATIONS/Translations/Gemini/ne-general/ (Gemini gemini-3.1-pro-preview, primed with the word list, 2026-09-25)
termbase: 0-INBOX/AI_translation/keyword-extraction-dharmamitra/ne/en-bo-ne-termbase-general.json (51 entries)
date: 2026-09-25
result: "locked words: zero-shot 126/136, primed run 128/136 → 136/136"
---

# Phase 2 fixes — Nepali, draft 2 → 3

The primed Gemini draft was kept word for word except for the locked words and five clear errors.

| Verse | Kind | Draft 2 (primed run) | Draft 3 |
|---|---|---|---|
| I-2 | grammar | तिब्बत भाषामा | तिब्बती भाषामा |
| 1-3 | lock: lotus | जलज पद्मद्वारा | जलज कमलद्वारा |
| 1-4 | lock: without exception | सम्पूर्ण पारमिताहरू | अशेष पारमिताहरू |
| 1-5, 1-7, 1-14, 1-17 | lock: feet | पाउ (everyday "foot") | चरण (the respectful word) |
| 1-8 | lock + spelling | निःशेष बध | अशेष वध |
| 1-11 | lock: ability | तान्न सक्ने क्षमता भएकी | तान्न समर्थ भएकी |
| 1-15 | error (stem hint) | महा पाप | महान् पाप |
| 1-16 | error + lock: mantra | परम रूपले तहसनहस … दश अक्षरको वाणी | पूर्ण रूपले तहसनहस … दश अक्षरको मन्त्र |
| 1-18 | lock + spelling | तारा दुई पटक … निशेष रूपले | तारे दुई पटक … अशेष रूपले |
| 2-3 | error (stem hint) | यसबाट महा नै प्राप्त गरी ("gains *mahā* from this") | यसभन्दा पनि महानता प्राप्त गरी ("gains greatness even beyond this") |
| 2-6 | error (optative lost) | विघ्नहरू रहने छैनन् … नष्ट हुनेछन् ("will not remain … will be destroyed") | विघ्नहरू नरहून् … नष्ट होऊन् ("may obstacles not remain … may each be destroyed"), as the root's ཅིག and the settled English decision |

**Lesson for the skill:** the run was given the lock *stems* महा and परम as hints, and wrote them as bare words
(2-3 महा नै, 1-15 महा पाप, 1-16 परम रूपले). A stem is right for checking, wrong as a hint — the glossary sent to
the model should carry a whole word (महान्).

Left for the meaning check: everything outside the locked words — e.g. 1-1 still has the "lotus face" reading,
1-5 "desire, directions and space", 1-19 "king" singular.
