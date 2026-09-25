---
title: Vietnamese word list — Praise to the Twenty-One Tārās (general grade)
language: Vietnamese (full diacritics)
lang_tag: vi
file_type: termbase-review
grade: general
termbase: en-bo-vi-termbase-general.json
grade_file: bo_vi_keyword_general.json
decisions: vi-decisions-general.json
built_by: keyword-standardize/scripts/build_termbase.py
entries: 52
decided_flagged: 14
status: awaiting native-speaker review
---

# Vietnamese word list — Praise to the Twenty-One Tārās (general grade)

The locked Vietnamese words for this text. Every Vietnamese translation step must use these words for these
Tibetan words. **Edit `vi-decisions-general.json`, not this file** — this file is rebuilt from it.

**Choices:** Clear modern Vietnamese (general grade) with Sino-Vietnamese Buddhist vocabulary · mantra syllables in Latin letters without diacritics · flagged picks decided by Claude, with the reason written down (Tenkal, 2026-09-24).

**Sources:** No human Vietnamese translation. (1) The finished Chinese word list and translation (zh-general draft 3), read as Sino-Vietnamese (Hán-Việt) — code "related"; (2) the standard Vietnamese Buddhist term; (3) the Gemini zero-shot Vietnamese draft (3-TRANSFORMATIONS/Translations/machine-drafts/zero-shot/gemini-vi/), which suggests but never confirms. No published Vietnamese version was available to check against.

**Vietnamese-only entries:** greater, om, svaha, hara, tara_syllable.

**Baseline:** the Gemini zero-shot Vietnamese draft already uses 100 of 137 locked words (73%, check_termbase_consistency.py --lang vi --strict-diacritics). Most misses are Hán-Việt choices it paraphrased (chúng, quang, đầy đủ, tịch tĩnh), chữ Hum (it wrote âm Hum), and Tuttara for Tuttare.

## Flagged picks — please look at these first (14)

Sources disagreed or had nothing. Decided by: Claude pick — user delegated flagged picks ("go with your picks"), 2026-09-24.

| Tibetan | English | Vietnamese | Source | Verses | Why |
|---|---|---|---|---|---|
| ཕན་ཡོན | benefits | **lợi ích** | standard Buddhist term + Gemini vi draft | I-2, 2-0 | ཕན་ཡོན = benefits. The Chinese chose 功德 (công đức), but in Vietnamese công đức means merit; lợi ích (利益) is the exact word and is what the Gemini draft has. |
| རྗེ་བཙུན་མ་འཕགས་མ | Noble and Venerable | **Chí Tôn Thánh** | Sino-Vietnamese reading of the zh word list | I-3 | Hán-Việt of 至尊聖 (རྗེ་བཙུན་ = 至尊 chí tôn, འཕགས་མ = 聖 thánh), used before Độ Mẫu: Chí Tôn Thánh Độ Mẫu. Gemini paraphrased it ("Thánh nữ … tôn quý"). |
| ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས | the Perfectly Complete Buddha | **Chánh Đẳng Chánh Giác** | Sino-Vietnamese reading of the zh word list + standard Buddhist term | a-1 | 正等正覺 (samyaksaṃbuddha). Gemini writes Chính Đẳng Chính Giác; Vietnamese Buddhist usage and the graded-translate register table (chánh niệm) use Chánh. |
| བསྟོད་པ་དངོས | the actual praise | **chánh văn tán thán** | new (no source had it) | 1-0 | Heading བསྟོད་པ་དངོས ("the praise itself"). Gemini's "tán thán chính tông" borrows chính tông ("orthodox lineage"), which is wrong here; chánh văn (正文) = the main text, as in the Chinese 讚頌正文. |
| མ་ལུས | without exception | **không sót** | Gemini vi draft | 1-8, 1-4 | མ་ལུས. The Hán-Việt of the Chinese 無餘 (vô dư) is not understood by general readers; không sót is the plain word Gemini uses (1-5, 1-8). |
| ཡི་གེ | syllable | **chữ** | standard Buddhist term | 1-5 | ཡི་གེ. Gemini says âm ("sound"); ཡི་གེ is the written syllable — chữ Hum, chủng tự — as Vietnamese Vajrayana texts write it, like the Chinese 字. |
| འབྱུང་པོ | spirits | **quỷ thần** | Sino-Vietnamese reading of the zh word list + standard Buddhist term | 1-6 | འབྱུང་པོ (bhūta). Hán-Việt of the Chinese 鬼神, the ordinary Vietnamese word for spirits. Gemini tinh linh reads as "sprites". Kept distinct from ác quỷ (གདོན). Commentary check: DG, GD, TN name Gaṇapati (ཚོགས་བདག) as their chief; TN: obstructers and misleaders. Quỷ thần fits. |
| ཆེན་པོ / ཆེན་མོ | great | **đại** | Sino-Vietnamese reading of the zh word list | 1-15, 1-8 | ཆེན་མོ / ཆེན་པོ (1-8 the Great Terrifying One, 1-15 great negativity): Hán-Việt 大 đại — đại bố úy, đại tội. 2-3 ཆེ་བ is split out as "greater". |
| ལྷ་མོ | goddess | **Nữ Thần** | standard Buddhist term | 2-1 | ལྷ་མོ (2-1); Gemini left it out. Gendun Drub and Taranatha identify it with Tārā herself (see the Chinese note). Nữ Thần is the plain word for a goddess. Reviewer: if it reads as a folk goddess, Thánh Mẫu or Tôn nữ are options. |
| རོ་ལངས | vetāla | **khởi thi** | Sino-Vietnamese reading of the zh word list | 1-21, 1-6 | རོ་ལངས ("risen corpse"): Hán-Việt of 起屍, the term in Vietnamese Mật tông texts. Gemini thây ma means "corpse / zombie" — the reading the English fact-check rejected. Reviewer: if khởi thi is too obscure, "thây ma sống dậy". Commentary check: TN glosses རོ་ལངས as a class of beings named after the rite; the word is "risen corpse", so khởi thi stays and thây ma ("zombie") does not. |
| གདོན | demons | **ác quỷ** | standard Buddhist term + Gemini vi draft | 1-21, 2-5 | གདོན (afflicting spirits): Gemini ác quỷ (1-21, 2-5). Ma is kept for བདུད (Māra, 1-8, 1-10), so the Chinese 邪魅 (tà mị) is not needed. Commentary check: TN — the eighteen གདོན; DG — all that obstructs. Ác quỷ fits. |
| ཆེ་བ | greater | **thù thắng hơn** | Sino-Vietnamese reading of the zh word list + standard Buddhist term | 2-3 | Vietnamese-only split from "great", as in Chinese: ཆེ་བ in 2-3 is comparative ("greater than this") → thù thắng hơn (更殊勝). Commentary check: GD — the common great siddhis; TN — many greater qualities. Thù thắng hơn fits. |
| སྭཱ་ཧཱ | svāhā | **Soha** | Vietnamese Vajrayana recitation | 1-15 | Vietnamese-only entry. Soha is how Vietnamese Vajrayana practitioners write svāhā in this mantra (Om Tare Tuttare Ture Soha); Gemini wrote Svaha. |
| ཏཱ་ར | TĀRA | **Tare** | Vietnamese Vajrayana recitation | 1-18 | Vietnamese-only entry. 1-18 "reciting TĀRA twice": the recitation form Tare (Om Tare Tuttare …), the same normalisation as tuttare and the Chinese 達咧. Gemini wrote Tara, which also reads as her name. |

## Sources agree (38)

| Tibetan | English | Vietnamese | Source | Verses | Why |
|---|---|---|---|---|---|
| ཕྱག / ཕྱག་འཚལ / ཕྱག་འཚལ་བ | Homage | **Kính lễ** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | I-0, I-2, I-3, 1-2, 1-10, 1-14, 1-21, 1-1, 1-12, 1-15, 1-18, 1-17, 1-20, 1-22, 1-11, 1-8, 1-16, 1-3, 1-6, 1-9, 1-19, 1-5, 1-4, 1-7, 1-13 | Hán-Việt of the Chinese 敬禮; the Gemini draft already opens every stanza with Kính lễ. (Đảnh lễ, used by Gemini in I-0/I-2, is the same act; one form is locked.) |
| ཏཱ་རཱ / སྒྲོལ་མ | Tara | **Độ Mẫu** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | I-1, I-2, I-3, 1-1, a-1 | Hán-Việt of 度母; used throughout the Gemini draft and pinned in its track glossary. |
| གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / ཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ན་མཿཏཱ་རཱ / ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ / སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ / ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ | Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka | **Namaḥ Tārā Ekaviṃśati Stotra Guṇahita Sāka** | kept as in the English | I-1 | The Sanskrit title line stays in IAST, as in English and Chinese (Gemini dropped the diacritics). |
| བསྟོད / བསྟོད་པ | praise | **tán thán** | standard Buddhist term + Gemini vi draft | 1-0, 1-22, 1-6, 2-0, a-1 | བསྟོད་པ. Tán thán (讚歎) is the usual Vietnamese Buddhist word and the Gemini draft's; the Chinese 讚頌 would be tán tụng, which is less common. |
| བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ | the Blessed Tārā | **Thế Tôn Độ Mẫu** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | a-1 | Hán-Việt of 世尊度母; Gemini has the same. |
| ཡང་དག / ཡང་དག་པར | perfectly | **viên mãn** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-21, 1-15, a-1 | 圓滿 viên mãn; Gemini uses it in 1-15, 1-21, a-1. |
| བཅོམ་ལྡན་འདས་མ | the Blessed One | **Thế Tôn** | Sino-Vietnamese reading of the zh word list + standard Buddhist term + Gemini vi draft | a-1 | 世尊; only inside Thế Tôn Độ Mẫu (a-1). |
| གློག | lightning | **tia chớp** | standard Buddhist term | 1-1 | གློག. Gemini paraphrased ("chớp sáng tựa luồng điện xẹt"); tia chớp is the plain word. Chinese 閃電. |
| འཇིག་རྟེན | world(s) | **thế giới** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-5, 1-1, 1-17 | 世界 thế giới; Gemini 1-5, 1-17. Not cõi, which Vietnamese uses for realm (ཁམས, as in ba cõi / dục giới) — the same distinction the Chinese keeps (世界 vs 三界). |
| ཞལ | face | **gương mặt** | standard Buddhist term + Gemini vi draft | 1-2, 1-1, 1-8 | ཞལ. Gemini gương mặt (1-1, 1-2, 1-8), the plain modern word; Hán-Việt dung nhan is literary. |
| ཆུ་སྐྱེས / པདྨ | lotus | **sen** | standard Buddhist term + Gemini vi draft | 1-3, 1-1, 1-8 | ཆུ་སྐྱེས / པདྨ. Locks the core word so hoa sen, đóa sen, sen thủy sinh all fit. |
| ཆུ་སྐྱེས་ཞལ | lotus face | **gương mặt hoa sen** | Gemini vi draft | 1-8 | 1-8 only (her own face, likened to a lotus), as settled in the English fact-check. Gemini has the same phrase there. |
| འོད | light | **quang** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-2, 1-12, 1-10, 1-20, 1-9 | འོད. Hán-Việt 光 quang, as in hào quang / quang minh, which Gemini uses (1-2, 1-9, 1-12). Locked short so the compound can vary. |
| འབར | blazing | **rực** | Gemini vi draft | 1-7, 1-2, 1-13 | འབར. Rực covers rực cháy (fire, 1-7, 1-13) and rực sáng (light, 1-2); Gemini has rực rỡ / rực cháy. The Hán-Việt xí nhiên (熾燃) is not used in prayers. |
| ཟླ་བ / རི་དགས་རྟགས་ཅན | moon | **trăng** | standard Buddhist term + Gemini vi draft | 1-2, 1-12, 1-20, 1-18 | ཟླ་བ and the kenning རི་དགས་རྟགས་ཅན (1-18): vầng trăng, trăng thu, trăng khuyết. Gemini throughout. |
| ཞི / ཞི་བ | peace | **tịch tĩnh** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-3, 1-15, 1-21 | ཞི / ཞི་བ = 寂靜 tịch tĩnh (Gemini 1-3). Gemini used an bình / bình an in 1-15 and 1-21; one form is locked. |
| ཧཱུཾ / ཧཱུྃ | hum | **Hum** | Vietnamese Vajrayana recitation + Gemini vi draft | 1-5, 1-17, 1-14, 1-16, 1-11 | Latin, without diacritics, as Vietnamese Vajrayana practitioners write it (Tenkal's choice). |
| མནན | trampling | **đạp** | Gemini vi draft | 1-7, 1-5 | མནན; Gemini 1-5, 1-7. |
| ཞབས | feet | **chân** | Gemini vi draft | 1-5, 1-17, 1-14 | ཞབས: bàn chân. Note for the drift check: chân is also in chân ngôn (mantra) and chân như (suchness); neither occurs in the verses where feet is locked (1-5, 1-14, 1-17). |
| ཏུ་ཏྟྭ་ར / ཏུཏྟྭ་ར | tuttare | **Tuttare** | Vietnamese Vajrayana recitation | 1-5, 1-10, 1-20 | ཏུཏྟྭ་ར. Latin, as in Om Tare Tuttare Ture Soha. Gemini wrote Tuttara in 1-5, 1-10, 1-20. |
| ཚོགས | hosts | **chúng** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-21, 1-6, 1-19, 1-11 | ཚོགས = 眾 chúng (chúng dạ-xoa, chúng thần). |
| འཇོམས | destroys | **tiêu diệt** | standard Buddhist term + Gemini vi draft | 1-7, 1-15, 1-21, 1-13 | འཇོམས; Gemini 1-8, 1-13, 1-15, 1-21. The Hán-Việt of 摧毀 (tồi hủy) is not used. |
| ཕཊ / ཕཊ་ཀྱི་ཡི་གེ | phat | **Phat** | Vietnamese Vajrayana recitation + Gemini vi draft | 1-7, 1-18 | Latin, without diacritics. |
| ཏྲད | trat | **Trat** | Vietnamese Vajrayana recitation + Gemini vi draft | 1-7 | Latin, without diacritics. |
| ཏུ་རེ | ture | **Ture** | Vietnamese Vajrayana recitation + Gemini vi draft | 1-21, 1-17, 1-8 | Latin, as in the mantra. |
| རབ | supreme | **cực** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-10 | རབ in 1-10 (supreme joy): 極 cực — cực hỷ. |
| དབང | power | **nhiếp phục** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-10 | དབང in 1-10: 攝伏 nhiếp phục; Gemini has exactly this ("Nhiếp phục ác ma"). The commentaries read it as bringing under her control. Commentary check: all four read དབང་དུ་མཛད as bringing under her control. Nhiếp phục fits. |
| དགའ / དགའ་བ / བསྐོར་དགས | joy | **hỷ** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-10, 1-16, 1-13, 1-19 | དགའ: 喜 hỷ, locked short so hoan hỷ / cực hỷ fit; Gemini hoan hỷ in 1-10, 1-13, 1-16, 1-19. |
| ཡི་གེ་ཧཱུཾ / ཡི་གེ་ཧཱུྃ | the syllable hum | **chữ Hum** | standard Buddhist term | 1-14, 1-11 | ཡི་གེ་ཧཱུཾ; Vietnamese puts chữ before the syllable. |
| ནུས | ability | **năng lực** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-11, 1-5 | ནུས: 能力 năng lực; Gemini 1-11 ("có năng lực triệu thỉnh"). Also 1-5 (same ནུས), as in Chinese. |
| ཡང་དག་ལྡན | perfectly endowed | **viên mãn đầy đủ** | standard Buddhist term | 1-21, 1-15 | ཡང་དག་ལྡན (1-15, 1-21). The Hán-Việt of 圓滿具足 (viên mãn cụ túc) is literary; viên mãn đầy đủ is clear and keeps both locked parts. |
| ལྡན | endowed | **đầy đủ** | standard Buddhist term | 1-21, 1-15, 2-1 | ལྡན. Plain word; the Hán-Việt cụ túc (具足) is literary. |
| ཡི་གེ་བཅུ་པའི་ངག / སྔགས | mantra | **chú** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-22, 1-16 | སྔགས = 咒 chú: căn bản chú (1-22), chú mười chữ and minh chú (1-16). Gemini also had chân ngôn once; one form is locked. |
| དབང | empowerment | **quán đảnh** | Sino-Vietnamese reading of the zh word list + standard Buddhist term + Gemini vi draft | 2-3 | དབང in 2-3: 灌頂 quán đảnh; Gemini the same. |
| གནོད་སྦྱིན | yaksas | **dạ-xoa** | Sino-Vietnamese reading of the zh word list + standard Buddhist term + Gemini vi draft | 1-6, 1-21 | གནོད་སྦྱིན: 夜叉 dạ-xoa; Gemini the same. |
| མཐུ | might | **uy lực** | Sino-Vietnamese reading of the zh word list + Gemini vi draft | 1-21 | མཐུ (1-21): 威力 uy lực; Gemini the same. |
| ཨོཾ | Oṃ | **Om** | Vietnamese Vajrayana recitation + Gemini vi draft | I-3, 1-15 | Vietnamese-only entry (English left mantra syllables unlocked). Latin, as in Om Tare Tuttare Ture Soha. |
| ཧ་ར | HARA | **Hara** | Vietnamese Vajrayana recitation + Gemini vi draft | 1-20 | Vietnamese-only entry. |
