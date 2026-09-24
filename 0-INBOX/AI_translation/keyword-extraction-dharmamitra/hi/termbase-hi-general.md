---
title: Hindi word list — Praise to the Twenty-One Tārās (general grade)
language: Hindi (Devanagari)
lang_tag: hi
file_type: termbase-review
grade: general
termbase: en-bo-hi-termbase-general.json
grade_file: bo_hi_keyword_general.json
decisions: hi-decisions-general.json
built_by: keyword-standardize/scripts/build_termbase.py
entries: 51
decided_flagged: 7
status: awaiting native-speaker review
---

# Hindi word list — Praise to the Twenty-One Tārās (general grade)

The locked Hindi words for this text. Every Hindi translation step must use these words for these
Tibetan words. **Edit `hi-decisions-general.json`, not this file** — this file is rebuilt from it.

**Choices:** Devanagari script · Sanskritized Buddhist Hindi register (clear modern prose, general grade) · mantra syllables in Devanagari, transliterating the Sanskrit as chanted · flagged picks decided by Claude, with the reason written down (Tenkal, 2026-09-24).

**Sources:** (1) the standard Hindi/Sanskrit Buddhist term — Hindi borrows Buddhist vocabulary directly from Sanskrit (much more directly than Chinese or Vietnamese do), so most terms need no third-language reference: the 'standard' term IS the Sanskrit word, in Devanagari, as Hindi Buddhist writing already uses it; (2) the existing Gemini zero-shot hi draft (Gemini/hi/, 2026-09-17), which already writes in this same Sanskritized register and gets most terms right; (3) the mantra recitation form, for the seed syllables and mantra names. No classical canon version or related-language word list was used — unlike Chinese (CBETA) or Vietnamese (the Chinese list, read Hán-Việt), Hindi does not need a second language as a stepping stone to Sanskrit.

**Hindi-only entries:** om, svaha, hara, tara_syllable.

**Baseline:** the existing Gemini zero-shot draft (Gemini/hi/, 2026-09-17) already uses 121 of 136 locked words (89%, check_termbase_consistency.py --lang hi) before enforcement — far higher than Chinese (46%) or Vietnamese (73%), because Hindi Buddhist vocabulary is the Sanskrit vocabulary this list locks. Misses: joy written as the adjective मुदित, अत्यंत for परम, बीजाक्षर for the generic syllable, भगवती for रྗེ་བཙུན་མ་འཕགས་མ, the moon spelled चंद्रमा, तारा for the mantra syllable तारे.

## Flagged picks — please look at these first (7)

Sources disagreed or had nothing. Decided by: Claude pick — user delegated flagged picks ("go with your picks"), 2026-09-24.

| Tibetan | English | Hindi | Source | Verses | Why |
|---|---|---|---|---|---|
| རྗེ་བཙུན་མ་འཕགས་མ | Noble and Venerable | **पूज्य आर्या** | the standard Sanskrit-Hindi Buddhist term | I-3 | Sanskrit ārya (noble) + pūjya (venerable/worthy of reverence). Flagged: the Gemini draft renders this भगवती (I-3), the same word it uses for 'the Blessed One' at a-1 for a different Tibetan phrase (བཅོམ་ལྡན་འདས་མ). Kept the two English locks distinct in Hindi too, since བཅོམ་ལྡན་འདས་མ literally is the Tibetan calque of Bhagavatī and རྗེ་བཙུན་མ་འཕགས་མ is a separate epithet pair — reviewer should confirm. |
| ཟླ་བ / རི་དགས་རྟགས་ཅན | moon | **चन्द्र** | the standard Sanskrit-Hindi Buddhist term | 1-2, 1-12, 1-20, 1-18 | the Sanskrit-correct spelling (not चंद्रमा) for the Sanskritized register; consistent meaning throughout (1-2, 1-12, 1-20, 1-18). Locked as the stem चन्द्र (rule 6) so it also covers 1-12's अर्धचन्द्र ('crescent moon'); the draft's चंद्रमाओं (1-2) was respelled चन्द्रमाओं. |
| ཡི་གེ | syllable | **अक्षर** | the standard Sanskrit-Hindi Buddhist term | 1-5 | the generic word (1-5 only). Flagged: split from syllable_hum's बीजाक्षर (seed-syllable) — the draft uses बीजाक्षर for both, but 'syllable' alone (bare ཡི་གེ) and 'the syllable hum' (a named seed-syllable) are different English locks and should render differently in Hindi too. |
| རབ | supreme | **परम** | the standard Sanskrit-Hindi Buddhist term | 1-10 | Flagged: kept distinct from 'great' (महान्), matching the English's own disambiguation (रब vs ཆེན). The draft used अत्यंत ('extremely') at 1-10, which is an intensifier, not 'supreme' — परम is the standard word for 'supreme/highest', better preserving the distinction. |
| དགའ / དགའ་བ / བསྐོར་དགས | joy | **आनंद** | the standard Sanskrit-Hindi Buddhist term | 1-10, 1-16, 1-13, 1-19 | Flagged: the noun form. The draft mostly uses the adjective मुदित ('joyful', 1-10, 1-16, 1-13) or आनंदमय (1-19); Phase 2 will need to adapt the part of speech to the sentence, but the underlying lock is आनंद (the standard noun). |
| གདོན | demons | **ग्रह** | Gemini hi draft (2026-09-17) | 1-21, 2-5 | Flagged: the draft independently chose ग्रह (graha) at both 1-21 and 2-5. Unlike English (which kept the plain 'demons' for the general grade because 'graha' is obscure to an English reader), ग्रह is a term ordinary Hindi speakers already know in this exact sense (an afflicting planetary/spirit force — राहु-केतु ग्रह, ग्रह-दोष), so it fits the general grade in Hindi even though the parallel English term does not use its Sanskrit cognate. |
| ཏཱ་ར | TĀRA | **तारे** | the mantra syllable as chanted (Devanagari) | 1-18 | Hindi-only entry. 1-18 'reciting TĀRA twice': the recitation form तारे (ॐ तारे तुत्तारे …), the same normalisation as तुत्तारे and as Chinese 達咧 / Vietnamese Tare. Gemini wrote तारा, which reads as her name. |

## Sources agree (44)

| Tibetan | English | Hindi | Source | Verses | Why |
|---|---|---|---|---|---|
| ཕྱག / ཕྱག་འཚལ / ཕྱག་འཚལ་བ | Homage | **नमस्कार** | Gemini hi draft (2026-09-17) | I-0, I-2, I-3, 1-2, 1-10, 1-14, 1-21, 1-1, 1-12, 1-15, 1-18, 1-17, 1-20, 1-22, 1-11, 1-8, 1-16, 1-3, 1-6, 1-9, 1-19, 1-5, 1-4, 1-7, 1-13 | consistent throughout the Gemini draft; the standard word for reverential salutation, matching the refrain use. |
| ཏཱ་རཱ / སྒྲོལ་མ | Tara | **तारा** | the standard Sanskrit-Hindi Buddhist term | I-1, I-2, I-3, 1-1, a-1 | the Sanskrit name, kept as in Hindi Buddhist usage (also style.md); covers both སྒྲོལ་མ and ཏཱ་རཱ. |
| ཕན་ཡོན | benefits | **लाभ** | Gemini hi draft (2026-09-17) | I-2, 2-0 | plain, clear modern word; matches the draft at I-2 and 2-0. |
| གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ན་མཿཏཱ་རཱ / ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ | Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka | **नमः तारा एकविंशति स्तोत्र गुणहित साक** | the standard Sanskrit-Hindi Buddhist term | I-1 | the Sanskrit title transliterated into Devanagari (Hindi's own script) rather than kept in Latin/IAST, since Hindi readers read Devanagari natively; compound गुणहित written as one word per Sanskrit sandhi (draft split it 'गुण हित'). |
| བསྟོད / བསྟོད་པ | praise | **स्तुति** | Gemini hi draft (2026-09-17) | 1-0, 1-22, 1-6, 2-0, a-1 | consistent throughout (1-0, 1-22, 1-6, 2-0, a-1); the standard word for a hymn of praise. |
| བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ | the Blessed Tārā | **भगवती तारा** | the standard Sanskrit-Hindi Buddhist term | a-1 | a-1; Bhagavatī is the standard Sanskrit-Hindi equivalent of བཅོམ་ལྡན་འདས་མ. |
| ཡང་དག / ཡང་དག་པར | perfectly | **पूर्णतः** | Gemini hi draft (2026-09-17) | 1-21, 1-15, a-1 | matches 1-15, 1-21 (a-1's यang dag par is inside the separate perfect_buddha epithet, not this generic adverb). |
| ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས | the Perfectly Complete Buddha | **सम्यक् सम्बुद्ध** | the standard Sanskrit-Hindi Buddhist term | a-1 | the standard Sanskrit-Hindi term (Samyaksambuddha); matches the draft at a-1 exactly. |
| བཅོམ་ལྡན་འདས་མ | the Blessed One | **भगवती** | the standard Sanskrit-Hindi Buddhist term | a-1 | the standard Sanskrit-Hindi equivalent of བཅོམ་ལྡན་འདས་མ, matching the draft at a-1. |
| བསྟོད་པ་དངོས | the actual praise | **मूल स्तुति** | Gemini hi draft (2026-09-17) | 1-0 | 1-0 heading; 'the root/actual praise', built on the 'praise' lock (मूल = root/actual). |
| གློག | lightning | **विद्युत** | Gemini hi draft (2026-09-17) | 1-1 | 1-1: क्षणिक विद्युत, 'a flash of lightning'. |
| འཇིག་རྟེན | world(s) | **लोक** | Gemini hi draft (2026-09-17) | 1-5, 1-1, 1-17 | consistent (1-5 सप्त लोकों, 1-1 त्रिलोकनाथ, 1-17 तीनों लोकों). |
| ཞལ | face | **मुख** | Gemini hi draft (2026-09-17) | 1-2, 1-1, 1-8 | consistent (1-2, 1-1, 1-8). |
| ཆུ་སྐྱེས / པདྨ | lotus | **कमल** | Gemini hi draft (2026-09-17) | 1-3, 1-1, 1-8 | consistent (1-3, 1-1, 1-8); the standard word, covers both ཆུ་སྐྱེས and པདྨ. |
| ཆུ་སྐྱེས་ཞལ | lotus face | **कमल मुख** | Gemini hi draft (2026-09-17) | 1-8 | 1-8; built on the lotus + face locks, matching the draft's कमल मुख। |
| འོད | light | **प्रकाश** | Gemini hi draft (2026-09-17) | 1-2, 1-12, 1-10, 1-20, 1-9 | most common rendering (1-12, 1-10); 1-2 and 1-9 use the near-synonym आभा/रश्मि in context, Phase 2 may need to vary the exact word grammatically but the lock is प्रकाश. |
| འབར | blazing | **प्रज्वलित** | Gemini hi draft (2026-09-17) | 1-7, 1-2, 1-13 | consistent (1-7, 1-2, 1-13 प्रज्वलित ज्वालाओं). |
| ཞི / ཞི་བ | peace | **शांति** | Gemini hi draft (2026-09-17) | 1-3, 1-15, 1-21 | consistent, standard term (1-3, 1-15, 1-21). |
| མ་ལུས | without exception | **अशेष** | Gemini hi draft (2026-09-17) | 1-8, 1-4 | 1-8 अशेष...अशेष वध; 1-4's मा लुस् is folded into सम्पूर्ण there in the draft — Phase 2 should render it explicitly as अशेष to keep the lock visible. |
| ཧཱུཾ / ཧཱུྃ | hum | **हूँ** | the mantra syllable as chanted (Devanagari) | 1-5, 1-17, 1-14, 1-16, 1-11 | the seed syllable as chanted; matches the draft everywhere. |
| མནན | trampling | **आक्रांत** | Gemini hi draft (2026-09-17) | 1-7, 1-5 | consistent (1-7, 1-5 आक्रांत करती हैं / आक्रांत कर). |
| ཞབས | feet | **चरण** | Gemini hi draft (2026-09-17) | 1-5, 1-17, 1-14 | consistent (1-5, 1-17, 1-14); the respectful register word, fitting a devotional praise. |
| ཏུ་ཏྟྭ་ར / ཏུཏྟྭ་ར | tuttare | **तुत्तारे** | the mantra syllable as chanted (Devanagari) | 1-5, 1-10, 1-20 | the mantra syllable as chanted (oṃ tāre tuttāre ture svāhā); matches the draft (1-5, 1-10, 1-20). |
| ཚོགས | hosts | **समूह** | Gemini hi draft (2026-09-17) | 1-21, 1-6, 1-19, 1-11 | consistent (1-21, 1-6, 1-19, 1-11 समूहों). |
| འབྱུང་པོ | spirits | **भूत** | Gemini hi draft (2026-09-17) | 1-6 | 1-6; the standard word, distinct from yaksha/vetala/demon below. |
| འཇོམས | destroys | **विनाश** | Gemini hi draft (2026-09-17) | 1-7, 1-15, 1-21, 1-13 | consistent (1-7, 1-15, 1-21, 1-13 विनाश करती हैं). |
| ཕཊ / ཕཊ་ཀྱི་ཡི་གེ | phat | **फट्** | the mantra syllable as chanted (Devanagari) | 1-7, 1-18 | the mantra syllable as chanted; matches the draft (1-7, 1-18). |
| ཏྲད | trat | **त्रट्** | the mantra syllable as chanted (Devanagari) | 1-7 | the mantra syllable as chanted; matches the draft (1-7). |
| ཏུ་རེ | ture | **तुरे** | the mantra syllable as chanted (Devanagari) | 1-21, 1-17, 1-8 | Tārā's mantra name/syllable, as chanted; matches the draft (1-21, 1-17, 1-8). |
| ཆེ་བ / ཆེན་པོ / ཆེན་མོ | great | **महा** | Gemini hi draft (2026-09-17) | 1-15, 1-8, 2-3 | shortest form (rule 6), so the lock covers महान् (1-15 महान पापों), the compound prefix (1-8 महाभयंकर) and 2-3's abstract महानता — all the same Sanskrit root mahā. |
| དབང | power | **वश** | Gemini hi draft (2026-09-17) | 1-10 | 1-10: मार और सम्पूर्ण लोकों को वश में करती हैं, 'brings under (her) power/control'; kept distinct from might/ability. |
| ཡི་གེ་ཧཱུཾ / ཡི་གེ་ཧཱུྃ | the syllable hum | **हूँ बीजाक्षर** | Gemini hi draft (2026-09-17) | 1-14, 1-11 | consistent (1-14, 1-11); बीजाक्षर ('seed-syllable') reserved for this named mantra syllable, distinct from the generic अक्षर ('syllable') above. |
| ནུས | ability | **समर्थ** | Gemini hi draft (2026-09-17) | 1-11 | 1-11 समर्थ हैं; kept distinct from power/might. |
| ཡང་དག་ལྡན | perfectly endowed | **पूर्णतः युक्त** | Gemini hi draft (2026-09-17) | 1-21, 1-15 | built from the perfectly + endowed locks; 1-15 and 1-21 both read पूर्णतः युक्त (1-21 reordered in draft 2 from पूर्ण शांति … युक्त). |
| ལྡན | endowed | **युक्त** | Gemini hi draft (2026-09-17) | 1-21, 1-15, 2-1 | consistent standalone (2-1 से युक्त, 1-21, 1-15). |
| ཡི་གེ་བཅུ་པའི་ངག / སྔགས | mantra | **मंत्र** | the standard Sanskrit-Hindi Buddhist term | 1-22, 1-16 | the standard word; matches the draft (1-22, 1-16). |
| ལྷ་མོ | goddess | **देवी** | Gemini hi draft (2026-09-17) | 2-1 | 2-1; the standard word, kept distinct from भगवती (blessed_one/blessed_tara) as English also keeps 'goddess' distinct from 'the Blessed One'. |
| རོ་ལངས | vetāla | **वेताल** | the standard Sanskrit-Hindi Buddhist term | 1-21, 1-6 | the Sanskrit word (vetāla, 'risen corpse'), same as Dharmamitra's Chinese/English choice; matches the draft (1-21, 1-6). |
| དབང | empowerment | **अभिषेक** | the standard Sanskrit-Hindi Buddhist term | 2-3 | the standard Sanskrit-Hindi term for tantric empowerment/abhisheka; matches the draft at 2-3 exactly, and is the technical term the English note itself names. |
| གནོད་སྦྱིན | yaksas | **यक्ष** | the standard Sanskrit-Hindi Buddhist term | 1-6, 1-21 | the Sanskrit word; matches the draft (1-6, 1-21 यक्षों). |
| མཐུ | might | **शक्ति** | Gemini hi draft (2026-09-17) | 1-21 | 1-21; kept distinct from power (वश) and ability (समर्थ), matching the English's three-way disambiguation. |
| ཨོཾ | Oṃ | **ॐ** | the mantra syllable as chanted (Devanagari) + Gemini hi draft (2026-09-17) | I-3, 1-15 | Hindi-only entry (English left mantra syllables unlocked; rule 5). The Devanagari sign ॐ, as the draft already wrote it. |
| སྭཱ་ཧཱ | svāhā | **स्वाहा** | the mantra syllable as chanted (Devanagari) + Gemini hi draft (2026-09-17) | 1-15 | Hindi-only entry. The Sanskrit svāhā in Devanagari, as chanted (ॐ तारे तुत्तारे तुरे स्वाहा). |
| ཧ་ར | HARA | **हर** | the mantra syllable as chanted (Devanagari) + Gemini hi draft (2026-09-17) | 1-20 | Hindi-only entry. |
