---
title: Chinese word list — Praise to the Twenty-One Tārās (general grade)
language: Chinese (Traditional)
lang_tag: zh-Hant
file_type: termbase-review
grade: general
termbase: en-bo-zh-termbase-general.json
grade_file: bo_zh_keyword_general.json
decisions: zh-decisions-general.json
built_by: keyword-standardize/scripts/build_termbase.py
entries: 52
decided_flagged: 14
status: awaiting native-speaker review
---

# Chinese word list — Praise to the Twenty-One Tārās (general grade)

The locked Chinese words for this text. Every Chinese translation step must use these words for these
Tibetan words. **Edit `zh-decisions-general.json`, not this file** — this file is rebuilt from it.

**Choices:** Traditional characters · clear modern Chinese (general grade, not the chanting style) · mantra syllables in Chinese characters · flagged picks decided by Claude, with the reason written down (Tenkal, 2026-09-24).

**Sources:** (1) the classical canon version CBETA T1108B — the same text the 17th Karmapa office publishes — aligned in 0-INBOX/AI_translation/keyword-extraction-dharmamitra/zh/references/zh-classical-T1108B.md, used for its words only; (2) the standard Buddhist term; (3) the DharmaMitra zero-shot zh draft, which suggests but never confirms. The online Mahāvyutpatti (Oslo) could not be read in this session, so "standard Buddhist term" means the well-known pair — the reviewer should check those.

**Chinese-only entries:** greater, om, svaha, hara, tara_syllable.

**Baseline:** the DharmaMitra zero-shot draft already uses 63 of 137 locked words (46%, check_termbase_consistency.py --lang zh). Most misses are 頂禮 for 敬禮 and mantra syllables left in Latin letters.

## Flagged picks — please look at these first (14)

Sources disagreed or had nothing. Decided by: Claude pick — user delegated flagged picks ("go with your picks"), 2026-09-24.

| Tibetan | English | Chinese | Source | Verses | Why |
|---|---|---|---|---|---|
| ཕྱག / ཕྱག་འཚལ / ཕྱག་འཚལ་བ | Homage | **敬禮** | classical canon (CBETA T1108) | I-0, I-2, I-3, 1-2, 1-10, 1-14, 1-21, 1-1, 1-12, 1-15, 1-18, 1-17, 1-20, 1-22, 1-11, 1-8, 1-16, 1-3, 1-6, 1-9, 1-19, 1-5, 1-4, 1-7, 1-13 | Classical has 敬禮 in all 21 stanzas; DharmaMitra has 頂禮. Both are standard. 敬禮 is what Chinese practitioners already chant, and a modern reader understands it. |
| བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ | the Blessed Tārā | **世尊度母** | DharmaMitra zh draft | a-1 | བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ; 世尊度母 is used in modern Tibetan-Buddhist Chinese. 薄伽梵母 would be the technical alternative (advanced grade). |
| བསྟོད་པ་དངོས | the actual praise | **讚頌正文** | new (no source had it) | 1-0 | Section heading བསྟོད་པ་དངོས. DharmaMitra 正行讚頌 borrows 正行 ("main practice"), which fits a sādhana, not a section of a text. 讚頌正文 = "the praise itself". |
| འཇིག་རྟེན | world(s) | **世界** | classical canon (CBETA T1108) | 1-5, 1-1, 1-17 | Classical 三世界 (1-1), 七世界 (1-5). DharmaMitra mixes 三界 / 七世間界. 三界 is avoided because in Chinese it names the desire/form/formless realms (ཁམས་གསུམ), a different Tibetan word. |
| ཏུ་ཏྟྭ་ར / ཏུཏྟྭ་ར | tuttare | **都達咧** | modern Tārā-mantra recitation | 1-5, 1-10, 1-20 | ཏུཏྟྭ་ར. The Tārā mantra is commonly recited 嗡 達咧 都達咧 都咧 梭哈. Classical writes it three ways (怛囉 1-5, 覩怛哩 1-10, 咄怛哩 1-20); DharmaMitra left Latin. Same normalisation as the English "tuttare". |
| འབྱུང་པོ | spirits | **鬼神** | new (no source had it) | 1-6 | འབྱུང་པོ (bhūta). Classical and DharmaMitra both write the transliteration 部多, which a general reader cannot parse. 鬼神 is the ordinary Chinese word for spirits and keeps it distinct from 邪魅 (གདོན). Commentary check: Drakpa Gyaltsen, Gendun Drub and Taranatha name Gaṇapati (ཚོགས་བདག) as their chief; Taranatha: obstructers and misleaders. 鬼神 fits. |
| ཕཊ / ཕཊ་ཀྱི་ཡི་གེ | phat | **呸** | modern Tārā-mantra recitation | 1-7, 1-18 | ཕཊ. 呸 is the common modern Chinese form in Tibetan-Buddhist mantras; classical writes 發. Chinese characters per the user's choice. |
| ཏྲད | trat | **特囉** | classical canon (CBETA T1108) | 1-7 | ཏྲད. Not part of the common mantra, so the classical form 特囉 (1-7 特囉胝發) is used. |
| དབང | power | **攝伏** | classical canon (CBETA T1108) | 1-10 | དབང in 1-10 (brings māras and the world under her power). Classical 作攝伏; DharmaMitra 降伏 ("subdue by force"), which is stronger than the Tibetan. 攝伏 = bring under one's control. Commentary check: all four read དབང་དུ་མཛད as bringing under her control (Gendun Drub: the māras and the eight great worldly gods). 攝伏 fits. |
| ལྷ་མོ | goddess | **天女** | DharmaMitra zh draft | 2-1 | ལྷ་མོ (2-1). 天女 is the usual Chinese for lha mo / devī (cf. 吉祥天女). Kept distinct from 世尊 (བཅོམ་ལྡན་འདས་མ), as in English. Commentary check 2026-09-24: Gendun Drub (ལྷ་མོ་སྒྲོལ་མ) and Taranatha (= བཅོམ་ལྡན་འདས་མ) identify ལྷ་མོ with Tārā herself. Reviewer: if 天女 reads as a lesser celestial being, use 聖尊 or 女尊. |
| གདོན | demons | **邪魅** | new (no source had it) | 1-21, 2-5 | གདོན (afflicting spirits). DharmaMitra 魔 / 鬼 — but 魔 is needed for བདུད (Māra) in 1-8 and 1-10. Classical 執魅 (1-21) points to 魅. 邪魅 = harmful spirits. Commentary check: Taranatha — the eighteen གདོན (e.g. ནམ་གུའི་གདོན); Drakpa Gyaltsen — all that obstructs. 邪魅 (harmful spirits) fits. |
| ཆེ་བ | greater | **更殊勝** | standard Buddhist term + DharmaMitra zh draft | 2-3 | Chinese-only split from "great": ཆེ་བ in 2-3 is comparative ("greater than this"), so 大 does not fit. DharmaMitra 更勝者. Commentary check: Gendun Drub — the common great siddhis; Taranatha — many greater qualities. 更殊勝 fits. |
| ཧ་ར | HARA | **喝囉** | classical canon (CBETA T1108) | 1-20 | Chinese-only entry. Not part of the common mantra; classical 1-20 誦二喝囉. |
| ཏཱ་ར | TĀRA | **達咧** | modern Tārā-mantra recitation | 1-18 | Chinese-only entry. 1-18 "reciting TĀRA twice": the recitation form 達咧 (as in 嗡 達咧 都達咧), same normalisation as tuttare. Classical 誦二怛囉. |

## Sources agree (38)

| Tibetan | English | Chinese | Source | Verses | Why |
|---|---|---|---|---|---|
| ཏཱ་རཱ / སྒྲོལ་མ | Tara | **度母** | classical canon (CBETA T1108) + DharmaMitra zh draft | I-1, I-2, I-3, 1-1, a-1 | Classical 救度母 / 尊聖救度母; DharmaMitra 度母 / 救度母; the Karmapa-office title uses 度母. The short name 度母 is the common modern one. |
| ཕན་ཡོན | benefits | **功德** | standard Buddhist term + DharmaMitra zh draft | I-2, 2-0 | Standard rendering of ཕན་ཡོན; classical has no heading for it. |
| རྗེ་བཙུན་མ་འཕགས་མ | Noble and Venerable | **至尊聖** | standard Buddhist term + DharmaMitra zh draft | I-3 | རྗེ་བཙུན་ = 至尊 (standard); འཕགས་མ = 聖. Classical opening has 尊聖救度母; DharmaMitra 至尊聖救度母. Used before 度母: 至尊聖度母. |
| གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ན་མཿཏཱ་རཱ / ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ | Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka | **Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka** | kept as in the English | I-1 | The Sanskrit title line stays in IAST, as in English (zh register rule). |
| བསྟོད / བསྟོད་པ | praise | **讚頌** | standard Buddhist term + DharmaMitra zh draft | 1-0, 1-22, 1-6, 2-0, a-1 | Classical uses 讚 / 讚嘆 / 稱歎; DharmaMitra 讚頌. 讚頌 is the clearest modern word for བསྟོད་པ. |
| ཡང་དག / ཡང་དག་པར | perfectly | **圓滿** | DharmaMitra zh draft | 1-21, 1-15, a-1 | ཡང་དག / ཡང་དག་པར as a modifier; appears inside 圓滿具足 (1-15, 1-21). In a-1 it is part of 正等覺佛. |
| ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས | the Perfectly Complete Buddha | **正等覺佛** | standard Buddhist term | a-1 | ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས = samyaksaṃbuddha = 正等覺 (standard pair). DharmaMitra wrote 正等覺如來, adding 如來 which is not in the Tibetan. |
| བཅོམ་ལྡན་འདས་མ | the Blessed One | **世尊** | standard Buddhist term + DharmaMitra zh draft | a-1 | བཅོམ་ལྡན་འདས(མ) = 世尊. Only occurs inside 世尊度母 (a-1). |
| གློག | lightning | **閃電** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-1 | Classical 電光; DharmaMitra 閃電光. 閃電 is the plain modern word. |
| ཞལ | face | **面容** | DharmaMitra zh draft | 1-2, 1-1, 1-8 | Classical 面 (single character, too short to lock in modern prose); DharmaMitra 面容 / 容顏. Also inside 蓮花面容 (1-8). |
| ཆུ་སྐྱེས / པདྨ | lotus | **蓮花** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-3, 1-1, 1-8 | Classical 蓮華 is the same word in older spelling; 蓮花 is the modern form. |
| ཆུ་སྐྱེས་ཞལ | lotus face | **蓮花面容** | DharmaMitra zh draft | 1-8 | 1-8 only (her own face, likened to a lotus), as settled in the English fact-check. |
| འོད | light | **光** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-2, 1-12, 1-10, 1-20, 1-9 | All sources use 光. |
| འབར | blazing | **熾燃** | DharmaMitra zh draft | 1-7, 1-2, 1-13 | DharmaMitra 熾燃 / 熾然 (inconsistent — locked to 熾燃); classical 熾盛. 熾燃 keeps the sense of flames. |
| ཟླ་བ / རི་དགས་རྟགས་ཅན | moon | **月** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-2, 1-12, 1-20, 1-18 | All sources use 月. Includes the kenning རི་དགས་རྟགས་ཅན ("deer-marked one") in 1-18, as in English. |
| ཞི / ཞི་བ | peace | **寂靜** | standard Buddhist term + DharmaMitra zh draft | 1-3, 1-15, 1-21 | ཞི / ཞི་བ = 寂靜 (standard). Classical 靜 / 善靜 / 寂滅. |
| མ་ལུས | without exception | **無餘** | classical canon (CBETA T1108) | 1-8, 1-4 | Classical 盡無餘 / 攝無餘; DharmaMitra 無餘. Readers know 一切無餘. |
| ཧཱུཾ / ཧཱུྃ | hum | **吽** | classical canon (CBETA T1108) + modern Tārā-mantra recitation | 1-5, 1-17, 1-14, 1-16, 1-11 | All Chinese sources write 吽. |
| ཡི་གེ | syllable | **字** | classical canon (CBETA T1108) | 1-5 | Classical 吽字; DharmaMitra 字. |
| མནན | trampling | **踏** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-7, 1-5 | Classical 足踏 / 踐蹋; DharmaMitra 足下踏. Single character so the verb can sit in natural phrases (踩踏, 踏於). |
| ཞབས | feet | **足** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-5, 1-17, 1-14 | Classical and DharmaMitra 足. |
| ཚོགས | hosts | **眾** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-21, 1-6, 1-19, 1-11 | Classical and DharmaMitra 眾. |
| འཇོམས | destroys | **摧毀** | DharmaMitra zh draft | 1-7, 1-15, 1-21, 1-13 | DharmaMitra 摧毀; classical 摧壞 / 摧滅 (same root 摧). |
| ཏུ་རེ | ture | **都咧** | modern Tārā-mantra recitation | 1-21, 1-17, 1-8 | ཏུ་རེ. Recitation form 都咧 (嗡 達咧 都達咧 都咧 梭哈); classical 都哩. |
| ཆེན་པོ / ཆེན་མོ | great | **大** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-15, 1-8 | ཆེན་མོ / ཆེན་པོ (1-8 大怖畏, 1-15 大罪). 2-3 ཆེ་བ is split out as "greater" for Chinese. |
| རབ | supreme | **極** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-10 | རབ in 1-10 (supreme joy): classical 最極喜, DharmaMitra 極喜. |
| དགའ / དགའ་བ / བསྐོར་དགས | joy | **喜** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-10, 1-16, 1-13, 1-19 | Classical 歡悅 / 喜悅 / 喜笑; DharmaMitra 喜 / 歡喜 / 極喜. The shared character 喜 is locked so compounds stay natural. |
| ཡི་གེ་ཧཱུཾ / ཡི་གེ་ཧཱུྃ | the syllable hum | **吽字** | classical canon (CBETA T1108) | 1-14, 1-11 | Classical 吽字 / 吽聲; Chinese puts the syllable before 字. |
| ནུས | ability | **能** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-11, 1-5 | ནུས ("able to"). Chinese says this with 能 (classical 亦能鉤召 1-11, 悉能鉤召 1-5). Added 1-5 for Chinese, where the same ནུས occurs; English did not lock it there. |
| ཡང་དག་ལྡན | perfectly endowed | **圓滿具足** | DharmaMitra zh draft | 1-21, 1-15 | ཡང་དག་ལྡན (1-15, 1-21). DharmaMitra 圓滿具足; classical 皆具足. |
| ལྡན | endowed | **具足** | classical canon (CBETA T1108) + DharmaMitra zh draft | 1-21, 1-15, 2-1 | ལྡན. Classical 具足 (1-21). |
| ཡི་གེ་བཅུ་པའི་ངག / སྔགས | mantra | **咒** | classical canon (CBETA T1108) + standard Buddhist term | 1-22, 1-16 | སྔགས. Classical 呪 is a variant of 咒; DharmaMitra alternates 咒 / 真言 — locked to 咒 (根本咒 1-22, 十字咒 / 明咒 1-16). |
| རོ་ལངས | vetāla | **起屍** | classical canon (CBETA T1108) | 1-21, 1-6 | རོ་ལངས ("risen corpse"): classical 起屍 (1-6). DharmaMitra has 起屍 in 1-21 but 羅剎 (rākṣasa, a different being) in 1-6 — Phase 2 must correct 1-6. Commentary check: Taranatha glosses རོ་ལངས as a class of beings (ལྷའི་སྲིན་པོའི་རིགས་དགུ), which may be why DharmaMitra wrote 羅剎; the word itself is "risen corpse", so 起屍 stays. |
| དབང | empowerment | **灌頂** | classical canon (CBETA T1108) + standard Buddhist term + DharmaMitra zh draft | 2-3 | དབང in 2-3 (the Victors confer empowerment). Classical benefits section 灌頂. |
| གནོད་སྦྱིན | yaksas | **夜叉** | standard Buddhist term + DharmaMitra zh draft | 1-6, 1-21 | གནོད་སྦྱིན. Classical 藥叉 is the older spelling of the same word. |
| མཐུ | might | **威力** | classical canon (CBETA T1108) | 1-21 | མཐུ (1-21): classical 善靜威力; DharmaMitra 威德力. |
| ཨོཾ | Oṃ | **嗡** | modern Tārā-mantra recitation | I-3, 1-15 | Chinese-only entry: English left mantra syllables unlocked. 嗡 is the common modern form; classical 唵. |
| སྭཱ་ཧཱ | svāhā | **梭哈** | modern Tārā-mantra recitation | 1-15 | Chinese-only entry. Recitation form 梭哈; classical 莎訶. |
