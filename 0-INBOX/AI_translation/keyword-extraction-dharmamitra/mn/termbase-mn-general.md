---
title: Mongolian word list — Praise to the Twenty-One Tārās (general grade)
language: Mongolian (Cyrillic)
lang_tag: mn
file_type: termbase-review
grade: general
termbase: en-bo-mn-termbase-general.json
grade_file: bo_mn_keyword_general.json
decisions: mn-decisions-general.json
built_by: keyword-standardize/scripts/build_termbase.py
entries: 52
decided_flagged: 11
status: awaiting native-speaker review
---

# Mongolian word list — Praise to the Twenty-One Tārās (general grade)

The locked Mongolian words for this text. Every Mongolian translation step must use these words for these
Tibetan words. **Edit `mn-decisions-general.json`, not this file** — this file is rebuilt from it.

**Choices:** Cyrillic (Khalkha) · clear modern Mongolian that keeps the liturgical Buddhist words practitioners know (Дарь эх, мөргөмүй, бурхан), with old grammar forms (лугаа) modernised · mantra syllables as chanted in Mongolia, in Cyrillic (Ум дарэ дүдарэ дүрэ суха) · flagged picks decided by Claude, with the reason written down (Tenkal, 2026-09-25).

**Sources:** (1) the established Mongolian Buddhist vocabulary, translated from Tibetan since the 17th-century Kanjur (source code `standard`); (2) the recited Mongolian forms of the mantra syllables, as pinned in the track glossary Gemini/mn/glossary.tsv (`recitation`); (3) the Gemini zero-shot mn draft (Gemini/mn/, 2026-09-17), which already writes in this liturgical style (`mt`). No reference text: the Mongolian Kanjur version could not be fetched here. Several spirit-class words are uncertain and flagged for a native reviewer.

**Mongolian-only entries:** om, svaha, hara, tara_syllable, tara_sanskrit.

**Baseline:** the Gemini zero-shot draft (Gemini/mn/, 2026-09-17) already uses 117 of 136 locked words (86%). Misses: нүүр for ཞལ (the draft wrote тэргүүн 'head'), лянхуа (усан төрмөл), дүддара for дүдарэ, the Sanskrit title, 1-18 moon named only by its kenning, the new words for spirits and yakṣas.

## Flagged picks — please look at these first (11)

Sources disagreed or had nothing. Decided by: Claude pick — user delegated flagged picks ("same as Nepali"), 2026-09-25.

| Tibetan | English | Mongolian | Source | Verses | Why |
|---|---|---|---|---|---|
| ཕྱག / ཕྱག་འཚལ / ཕྱག་འཚལ་བ | Homage | **мөргө** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | I-0, I-2, I-3, 1-2, 1-10, 1-14, 1-21, 1-1, 1-12, 1-15, 1-18, 1-17, 1-20, 1-22, 1-11, 1-8, 1-16, 1-3, 1-6, 1-9, 1-19, 1-5, 1-4, 1-7, 1-13 | Flagged. The stem, so the refrain мөргөмүй and the noun мөргөл (I-0, 1-22) both match; hint мөргөмүй. The refrain is the liturgical form every Mongolian reciter knows, kept on purpose in the modern register. |
| གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ན་མཿཏཱ་རཱ / ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ | Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka | **Намо Тара Экавимшати Стотра Гунахита Сака** | the established Mongolian Buddhist term | I-1 | Flagged. The Sanskrit title in Cyrillic, as Mongolian texts write Sanskrit titles; the draft broke it into lower-case pieces (нама тара … гуна хита сака). |
| བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ | the Blessed Tārā | **Төгс нөгчсөн Дарь эх** | the established Mongolian Buddhist term | a-1 | Flagged. བཅོམ་ལྡན་འདས་མ is Mongolian Ялгуусан төгс нөгчсөн; the core Төгс нөгчсөн is common to every form. The draft's Итгэлт ('protector', མགོན་པོ) is a different word. |
| བཅོམ་ལྡན་འདས་མ | the Blessed One | **Төгс нөгчсөн** | the established Mongolian Buddhist term | a-1 | Flagged, with blessed_tara (the draft had Итгэлт). |
| ཞལ | face | **нүүр** | the established Mongolian Buddhist term | 1-2, 1-1, 1-8 | Flagged. The draft wrote тэргүүн ('head') at 1-2 and 1-8, which is wrong for ཞལ. |
| ཆུ་སྐྱེས / པདྨ | lotus | **лянхуа** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-3, 1-1, 1-8 | Flagged. The ordinary Mongolian word; the draft's усан төрмөл ('water-born') is a calque of ཆུ་སྐྱེས a general reader may not recognise. 1-3 keeps both ideas (усанд төрсөн лянхуа). |
| འབྱུང་པོ | spirits | **чөтгөр** | the established Mongolian Buddhist term | 1-6 | Flagged, uncertain. The draft's Гарва at 1-6 is not a Mongolian word for འབྱུང་པོ. чөтгөр ('spirit, ghost') is the widely known word, kept apart from ад (གདོན). A native reviewer should confirm. |
| རབ | supreme | **дээд** | the established Mongolian Buddhist term | 1-10 | Flagged. 'highest', kept apart from их; the draft had маш ('very') at 1-10. |
| ལྷ་མོ | goddess | **охин тэнгэр** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 2-1 | Flagged. The standard word for ལྷ་མོ and the draft's; but Охин тэнгэр is also the name of Palden Lhamo in Mongolia. The commentaries say the goddess is Tārā herself — a native reviewer should decide whether to write Дарь эх here. |
| རོ་ལངས | vetāla | **босоо** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-21, 1-6 | Flagged. རོ་ལངས 'risen corpse'; the draft had босоолон / босоарь. Locked as the stem; hint босоо үхдэл. |
| གནོད་སྦྱིན | yaksas | **хорлогч** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-6, 1-21 | Flagged. The Mongolian calque of གནོད་སྦྱིན ('harm-doer'), the draft's word at 1-21 (1-6 had хорлолт бирд). |

## Sources agree (41)

| Tibetan | English | Mongolian | Source | Verses | Why |
|---|---|---|---|---|---|
| སྒྲོལ་མ | Tara | **Дарь эх** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | I-2, I-3, 1-1, a-1 | the established Mongolian name (also the track glossary). |
| ཕན་ཡོན | benefits | **ач тус** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | I-2, 2-0 | the standard phrase; the draft has it at I-2 and 2-0. |
| རྗེ་བཙུན་མ་འཕགས་མ | Noble and Venerable | **богд хутагт** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | I-3 | རྗེ་བཙུན = богд, འཕགས་མ = хутагт, as the draft has it at I-3. |
| བསྟོད / བསྟོད་པ | praise | **магт** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-0, 1-22, 1-6, 2-0, a-1 | the stem (магтаал, магтсан, магтагдсан — the vowel drops); hint магтаал. |
| ཡང་དག / ཡང་དག་པར | perfectly | **сайтар** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-21, 1-15, a-1 | the draft's word (сайтар төгссөн 1-15, 1-21). |
| ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས | the Perfectly Complete Buddha | **төгс туулсан** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | a-1 | Samyaksambuddha = Үнэн төгс туулсан бурхан; the core is locked so inflected forms match. |
| བསྟོད་པ་དངོས | the actual praise | **Үндсэн магтаал** | Gemini mn zero-shot (2026-09-17) | 1-0 | the draft's 1-0 heading. |
| གློག | lightning | **цахилгаан** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-1 | the draft's word. |
| འཇིག་རྟེན | world(s) | **ертөнц** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-5, 1-1, 1-17 | consistent in the draft (гурван ертөнц). |
| ཆུ་སྐྱེས་ཞལ | lotus face | **лянхуан нүүр** | the established Mongolian Buddhist term | 1-8 | 1-8 only, her own lotus face (1-1 is the lotus from the Lord's face). |
| འོད | light | **гэр** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-2, 1-12, 1-10, 1-20, 1-9 | гэрэл; locked as the stem гэр because the vowel drops when it inflects (гэрлийн, гэрлийг). Hint гэрэл. |
| འབར | blazing | **бад** | Gemini mn zero-shot (2026-09-17) | 1-7, 1-2, 1-13 | a short stem, because the verb changes its vowel (бадрах, бадарсан, бадрангуй); hint бадрах. |
| ཟླ་བ / རི་དགས་རྟགས་ཅན | moon | **сар** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-2, 1-12, 1-20, 1-18 | the ordinary word. At 1-18 the draft wrote only the kenning гөрөөсний тэмдэгт ('deer-marked one'); the moon must be named. |
| ཞི / ཞི་བ | peace | **амар** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-3, 1-15, 1-21 | the stem (амарлингуй, амар амгалан); hint амар амгалан. |
| མ་ལུས | without exception | **үлдэлгүй** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-8, 1-4 | the track glossary's word (үлдэлгүйгээр). |
| ཧཱུཾ / ཧཱུྃ | hum | **хум** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | 1-5, 1-17, 1-14, 1-16, 1-11 | as chanted. |
| ཡི་གེ | syllable | **үс** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-5 | үсэг; locked as the stem үс because the vowel drops when it inflects (үсгээр). Hint үсэг. |
| མནན | trampling | **гишгэ** | Gemini mn zero-shot (2026-09-17) | 1-7, 1-5 | the stem (гишгэж, гишгэн). |
| ཞབས | feet | **өлмий** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-5, 1-17, 1-14 | the honorific word for a deity's feet; consistent in the draft. |
| ཏུ་ཏྟྭ་ར / ཏུཏྟྭ་ར | tuttare | **дүдарэ** | the syllable as chanted in Mongolia | 1-5, 1-10, 1-20 | as chanted (Ум дарэ дүдарэ дүрэ суха); the track glossary pins it; the draft wavered (дүддара). |
| ཚོགས | hosts | **чуулга** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-21, 1-6, 1-19, 1-11 | the stem (чуулган, чуулганаар). |
| འཇོམས | destroys | **дара** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-7, 1-15, 1-21, 1-13 | the stem (дарагч, даран); consistent in the draft. |
| ཕཊ / ཕཊ་ཀྱི་ཡི་གེ | phat | **пад** | the syllable as chanted in Mongolia | 1-7, 1-18 | as chanted (track glossary). |
| ཏྲད | trat | **трэд** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | 1-7 | as chanted. |
| ཏུ་རེ | ture | **дүрэ** | the syllable as chanted in Mongolia | 1-21, 1-17, 1-8 | as chanted (track glossary). |
| ཆེ་བ / ཆེན་པོ / ཆེན་མོ | great | **их** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-15, 1-8, 2-3 | the ordinary word, verse-scoped (1-15, 1-8, 2-3). |
| དབང | power | **эрх** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-10 | 1-10 эрхэндээ оруулах, 'bring under one's power'. |
| དགའ / དགའ་བ / བསྐོར་དགས | joy | **баяс** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-10, 1-16, 1-13, 1-19 | the stem (баясгалан, баясах); consistent in the draft. |
| ཡི་གེ་ཧཱུཾ / ཡི་གེ་ཧཱུྃ | the syllable hum | **хум үс** | Gemini mn zero-shot (2026-09-17) | 1-14, 1-11 | hum + syllable (хум үсгээр); stem for the same reason. |
| ནུས | ability | **чада** | Gemini mn zero-shot (2026-09-17) | 1-11 | the stem (чадагч, чадах). |
| ཡང་དག་ལྡན | perfectly endowed | **сайтар төгс** | Gemini mn zero-shot (2026-09-17) | 1-21, 1-15 | perfectly + endowed; the draft's сайтар төгссөн. |
| ལྡན | endowed | **төгс** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-21, 1-15, 2-1 | the stem of төгссөн / төгөлдөр. |
| ཡི་གེ་བཅུ་པའི་ངག / སྔགས | mantra | **тарни** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-22, 1-16 | the standard word. |
| དབང | empowerment | **авшиг** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 2-3 | the standard word. |
| གདོན | demons | **ад** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-21, 2-5 | the standard word for གདོན; the draft has it. |
| མཐུ | might | **хүч** | the established Mongolian Buddhist term + Gemini mn zero-shot (2026-09-17) | 1-21 | the draft's word (амарлингуйн хүч); kept apart from эрх. |
| ཨོཾ | Oṃ | **Ум** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | I-3, 1-15 | Mongolian-only entry: the syllable as chanted (track glossary). |
| སྭཱ་ཧཱ | svāhā | **суха** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | 1-15 | Mongolian-only entry: the syllable as chanted (track glossary). |
| ཧ་ར | HARA | **хара** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | 1-20 | Mongolian-only entry: the syllable as chanted (track glossary). |
| ཏཱ་ར | TĀRA | **дарэ** | the syllable as chanted in Mongolia + Gemini mn zero-shot (2026-09-17) | 1-18 | Mongolian-only entry: the syllable as chanted (track glossary). |
| ཏཱ་རཱ | Tārā (in the Sanskrit title) | **Тара** | the established Mongolian Buddhist term | I-1 | Mongolian-only split: in the Sanskrit title line (I-1) ཏཱ་རཱ stays the Sanskrit Тара; everywhere else she is Дарь эх. |
