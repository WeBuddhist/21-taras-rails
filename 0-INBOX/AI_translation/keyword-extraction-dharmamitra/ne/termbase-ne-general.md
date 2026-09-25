---
title: Nepali word list — Praise to the Twenty-One Tārās (general grade)
language: Nepali (Devanagari)
lang_tag: ne
file_type: termbase-review
grade: general
termbase: en-bo-ne-termbase-general.json
grade_file: bo_ne_keyword_general.json
decisions: ne-decisions-general.json
built_by: keyword-standardize/scripts/build_termbase.py
entries: 51
decided_flagged: 7
status: awaiting native-speaker review
---

# Nepali word list — Praise to the Twenty-One Tārās (general grade)

The locked Nepali words for this text. Every Nepali translation step must use these words for these
Tibetan words. **Edit `ne-decisions-general.json`, not this file** — this file is rebuilt from it.

**Choices:** Devanagari · standard Nepali with the Sanskrit Buddhist vocabulary and the forms familiar in Nepal's Tibetan Buddhist communities (general grade) · mantra syllables in Devanagari · flagged picks decided by Claude, with the reason written down (Tenkal, 2026-09-25).

**Sources:** (1) the standard Sanskrit Buddhist term in Nepali spelling (शान्ति, मन्त्र, आनन्द — Nepali keeps the Sanskrit nasal consonants); (2) the checked Hindi word list and Hindi draft 5 (source code `related`: same script, same Sanskrit vocabulary — a guide, not a copy, since Nepali grammar and several everyday words differ); (3) the Gemini zero-shot ne draft (Gemini/ne/, 2026-09-17), a suggestion only; (4) the mantra recitation form.

**Nepali-only entries:** om, svaha, hara, tara_syllable.

## Flagged picks — please look at these first (7)

Sources disagreed or had nothing. Decided by: Claude pick — user delegated flagged picks ("you do it"), 2026-09-25.

| Tibetan | English | Nepali | Source | Verses | Why |
|---|---|---|---|---|---|
| ཕྱག / ཕྱག་འཚལ / ཕྱག་འཚལ་བ | Homage | **वन्दना** | the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | I-0, I-2, I-3, 1-2, 1-10, 1-14, 1-21, 1-1, 1-12, 1-15, 1-18, 1-17, 1-20, 1-22, 1-11, 1-8, 1-16, 1-3, 1-6, 1-9, 1-19, 1-5, 1-4, 1-7, 1-13 | Flagged. The Hindi lock is नमस्कार, but in Nepali नमस्कार is the everyday greeting; वन्दना is the devotional word and the zero-shot draft already uses it for every refrain (वन्दना उनलाई). I-2 had प्रणाम in the draft. |
| རྗེ་བཙུན་མ་འཕགས་མ | Noble and Venerable | **भट्टारिका आर्या** | the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | I-3 | Flagged. भट्टारिका is the Sanskrit equivalent of རྗེ་བཙུན་མ (the venerable lady), and Nepal's Buddhists know it from the Sanskrit liturgy (आर्यतारा भट्टारिका); the draft chose it on its own. Kept apart from भगवती (བཅོམ་ལྡན་འདས་མ), as in Hindi. The plainer alternative is पूज्य आर्या (the Hindi lock). |
| གློག | lightning | **बिजुली** | Gemini ne zero-shot (2026-09-17) | 1-1 | Flagged. Everyday Nepali for lightning (the draft's word); Hindi locked the Sanskrit विद्युत, which in Nepali reads as technical 'electricity'. |
| མནན | trampling | **कुल्च** | Gemini ne zero-shot (2026-09-17) | 1-7, 1-5 | Flagged. The stem of the native Nepali verb 'to trample' (कुल्चेर, कुल्चँदै in the draft); Hindi's आक्रांत is literary in Nepali. Locked as the stem so every verb form matches. |
| དགའ / དགའ་བ / བསྐོར་དགས | joy | **आनन्द** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term | 1-10, 1-16, 1-13, 1-19 | Flagged. The noun, in Nepali spelling (Hindi आनंद); आनन्दित/आनन्दमय also match. The draft uses प्रमुदित throughout, so the primed run and enforcement must change 1-10, 1-13, 1-16, 1-19. |
| གདོན | demons | **ग्रह** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-21, 2-5 | Flagged, as in Hindi: ग्रह in the sense of an afflicting spirit (ग्रहदशा, ग्रह लाग्नु are everyday Nepali). The draft chose it too. |
| ཏཱ་ར | TĀRA | **तारे** | the mantra syllable as chanted (Devanagari) | 1-18 | Nepali-only entry. The recitation form, as Hindi/Chinese/Vietnamese; the draft wrote 'तारा', which reads as her name. |

## Sources agree (44)

| Tibetan | English | Nepali | Source | Verses | Why |
|---|---|---|---|---|---|
| ཏཱ་རཱ / སྒྲོལ་མ | Tara | **तारा** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term | I-1, I-2, I-3, 1-1, a-1 | the Sanskrit name; also the Hindi lock. |
| ཕན་ཡོན | benefits | **लाभ** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | I-2, 2-0 | as Hindi; the draft has लाभसहित (I-2) and लाभ (2-0). |
| གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ན་མཿཏཱ་རཱ / ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ | Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka | **नमः तारा एकविंशति स्तोत्र गुणहित साक** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term | I-1 | the Sanskrit title in Devanagari, as in Hindi; the draft matches. |
| བསྟོད / བསྟོད་པ | praise | **स्तुति** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-0, 1-22, 1-6, 2-0, a-1 | as Hindi; consistent in the draft. |
| བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ | the Blessed Tārā | **भगवती तारा** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | a-1 | a-1; Bhagavatī is the Sanskrit of བཅོམ་ལྡན་འདས་མ. |
| ཡང་དག / ཡང་དག་པར | perfectly | **पूर्ण रूपले** | Gemini ne zero-shot (2026-09-17) | 1-21, 1-15, a-1 | the natural Nepali adverb (Hindi पूर्णतः); the draft uses it in 1-15 and 1-21. |
| ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས | the Perfectly Complete Buddha | **सम्यक्सम्बुद्ध** | the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | a-1 | Samyaksambuddha, written as one word as in the draft (Hindi सम्यक् सम्बुद्ध). |
| བཅོམ་ལྡན་འདས་མ | the Blessed One | **भगवती** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term | a-1 | as Hindi. |
| བསྟོད་པ་དངོས | the actual praise | **मूल स्तुति** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-0 | as Hindi; the draft matches. |
| འཇིག་རྟེན | world(s) | **लोक** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 1-5, 1-1, 1-17 | as Hindi; consistent in the draft (त्रिलोक, सप्तलोक). |
| ཞལ | face | **मुख** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-2, 1-1, 1-8 | as Hindi; also covers the draft's मुखमण्डल. |
| ཆུ་སྐྱེས / པདྨ | lotus | **कमल** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-3, 1-1, 1-8 | as Hindi. The draft's जलजात ('water-born') at 1-8 is to be replaced by the lock. |
| ཆུ་སྐྱེས་ཞལ | lotus face | **कमल मुख** | Hindi word list and Hindi draft 5 | 1-8 | 1-8 only, her own lotus face. In 1-1 the lotus grows from the Lord's face (consensus); the draft's कमल-मुखको there is the same error the other languages had. |
| འོད | light | **प्रकाश** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-2, 1-12, 1-10, 1-20, 1-9 | as Hindi; consistent in the draft. |
| འབར | blazing | **प्रज्वलित** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-7, 1-2, 1-13 | as Hindi; the draft uses it in 1-2, 1-12, 1-13. |
| ཟླ་བ / རི་དགས་རྟགས་ཅན | moon | **चन्द्र** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term | 1-2, 1-12, 1-20, 1-18 | the stem, as in Hindi (covers चन्द्रमा, अर्धचन्द्र). At 1-18 the draft wrote मृगाङ्क (चन्द्रमा) — the parenthesis is an addition. |
| ཞི / ཞི་བ | peace | **शान्ति** | the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 1-3, 1-15, 1-21 | Nepali spelling of the Sanskrit (Hindi writes शांति). |
| མ་ལུས | without exception | **अशेष** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-8, 1-4 | as Hindi; the draft uses it in 1-4 and 1-8. |
| ཧཱུཾ / ཧཱུྃ | hum | **हूँ** | the mantra syllable as chanted (Devanagari) | 1-5, 1-17, 1-14, 1-16, 1-11 | the seed syllable as chanted. The draft puts syllables in quotation marks ('हूँ'); the style asks for none. |
| ཡི་གེ | syllable | **अक्षर** | the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 1-5 | the generic word; the draft's word. |
| ཞབས | feet | **चरण** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-5, 1-17, 1-14 | the respectful word, as Hindi; consistent in the draft. |
| ཏུ་ཏྟྭ་ར / ཏུཏྟྭ་ར | tuttare | **तुत्तारे** | the mantra syllable as chanted (Devanagari) | 1-5, 1-10, 1-20 | as chanted (ॐ तारे तुत्तारे तुरे स्वाहा). The draft wrote 'तुत्तार' — wrong ending. |
| ཚོགས | hosts | **समूह** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-21, 1-6, 1-19, 1-11 | as Hindi; consistent in the draft. |
| འབྱུང་པོ | spirits | **भूत** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-6 | as Hindi. |
| འཇོམས | destroys | **नष्ट** | Gemini ne zero-shot (2026-09-17) | 1-7, 1-15, 1-21, 1-13 | the Nepali verb नष्ट गर्नु, consistent in the draft (Hindi विनाश). |
| ཕཊ / ཕཊ་ཀྱི་ཡི་གེ | phat | **फट्** | the mantra syllable as chanted (Devanagari) | 1-7, 1-18 | as chanted. |
| ཏྲད | trat | **त्रट्** | the mantra syllable as chanted (Devanagari) | 1-7 | as chanted (traṭ). The draft wrote 'त्रत्'. |
| ཏུ་རེ | ture | **तुरे** | the mantra syllable as chanted (Devanagari) | 1-21, 1-17, 1-8 | Tārā's mantra name, as chanted. |
| ཆེ་བ / ཆེན་པོ / ཆེན་མོ | great | **महा** | Hindi word list and Hindi draft 5 | 1-15, 1-8, 2-3 | the stem, as Hindi (महान्, महाभयङ्करी, महिमा…). |
| རབ | supreme | **परम** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term | 1-10 | as Hindi, kept apart from 'great'. The draft had अत्यन्त ('very') at 1-10. |
| དབང | power | **वश** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-10 | as Hindi; the draft's वशीभूत contains it. |
| ཡི་གེ་ཧཱུཾ / ཡི་གེ་ཧཱུྃ | the syllable hum | **हूँ अक्षर** | Gemini ne zero-shot (2026-09-17) | 1-14, 1-11 | built from the hum + syllable locks, as the English does ('the syllable hum'); the draft's form. (Hindi split अक्षर / हूँ बीजाक्षर; Nepali keeps one word for ཡི་གེ.) |
| ནུས | ability | **समर्थ** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-11 | as Hindi; the draft matches. |
| ཡང་དག་ལྡན | perfectly endowed | **पूर्ण रूपले युक्त** | Gemini ne zero-shot (2026-09-17) | 1-21, 1-15 | perfectly + endowed; the draft's form in 1-15 and 1-21. |
| ལྡན | endowed | **युक्त** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-21, 1-15, 2-1 | as Hindi. At 2-1 the draft paraphrased (भक्तिभाव राख्ने). |
| ཡི་གེ་བཅུ་པའི་ངག / སྔགས | mantra | **मन्त्र** | the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 1-22, 1-16 | Nepali spelling (Hindi मंत्र); the draft matches. |
| ལྷ་མོ | goddess | **देवी** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 2-1 | as Hindi. |
| རོ་ལངས | vetāla | **वेताल** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 1-21, 1-6 | the Sanskrit word. |
| དབང | empowerment | **अभिषेक** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 2-3 | the Sanskrit term. |
| གནོད་སྦྱིན | yaksas | **यक्ष** | Hindi word list and Hindi draft 5 + the standard Sanskrit-Nepali Buddhist term + Gemini ne zero-shot (2026-09-17) | 1-6, 1-21 | the Sanskrit word. |
| མཐུ | might | **शक्ति** | Hindi word list and Hindi draft 5 + Gemini ne zero-shot (2026-09-17) | 1-21 | as Hindi. |
| ཨོཾ | Oṃ | **ॐ** | the mantra syllable as chanted (Devanagari) + Gemini ne zero-shot (2026-09-17) | I-3, 1-15 | Nepali-only entry (as Hindi). |
| སྭཱ་ཧཱ | svāhā | **स्वाहा** | the mantra syllable as chanted (Devanagari) + Gemini ne zero-shot (2026-09-17) | 1-15 | Nepali-only entry. |
| ཧ་ར | HARA | **हर** | the mantra syllable as chanted (Devanagari) + Gemini ne zero-shot (2026-09-17) | 1-20 | Nepali-only entry. |
