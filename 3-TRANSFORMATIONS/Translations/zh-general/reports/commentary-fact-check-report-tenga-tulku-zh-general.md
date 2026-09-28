## Praise to the Twenty-One Taras — Commentary Fact-Check (Chinese)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-བསྟན་དགའ་སྤྲུལ་སྐུ།.md` — Dorlob Tenga Tulku (commentary id `tenga-tulku`; date and lineage not given in the file)
- **Translation audited:** `3-TRANSFORMATIONS/Translations/zh-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general.md` (Chinese, Traditional characters, general grade, draft 4)
- **Root text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`
- **Checked:** 2026-09-24

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Every content
word Tenga Tulku glosses was aligned against the Chinese before a verdict was
given; only ERROR and MISMATCH rows are printed. The Chinese was checked
directly against the Tibetan commentary. The fact-checked English, the English
consensus table, the Chinese word list, the Chinese back-translation, light-check
and QA reports, and the Hindi report on this same commentary were used for context
only. Their verdicts were not copied. Where the Chinese follows one of the seven
settled English translator decisions, the row says so. Every Chinese phrase quoted
carries an English gloss. Suggested fixes are in Traditional characters and keep
the locked Chinese words from the word list. No lock was found to be wrong; one
flagged lock (天女 at 2-1) is raised for the reviewer. Preliminary self-check, not a
scholarly sign-off — a domain specialist and a native Chinese reader must review it
before this is treated as final (an LLM never marks its own output complete).

Extraction notes: 29 transclusion buckets (I-3, 1-1 to 1-22, 2-1 to 2-6), none
empty, no cascading shift — each bucket quotes its own root verse and then
explains it. The `^1-1`, `^2-5` … `^3-19` markers inside the buckets are the
commentary file's own paragraph IDs, not root IDs. Not covered: I-1, I-2 and the
root colophon a-1. The commentator's own colophon ("ཞེས་རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ་མིང་པས་སོ")
sits at the end of the 2-6 bucket. The commentary was extracted into a private
scratch folder used by no other run, and every bucket was read in full from that
copy. The Chinese per-verse text (`extract_translation.py`, whole blocks; 23 blocks
in chapter 1 including the heading, 7 in chapter 2) matches the translation file.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6 (29 verses) |

#### Chapter I — I-3

He glosses *oṃ* (the nature of the five kāyas and five wisdoms), *rje btsun ma*
(protector and refuge of the three worlds, holding the three vows), *'phags ma*
(raised far above the level of ordinary beings) and *sgrol ma* (she who frees all
beings to the level of buddhahood). "嗡，敬禮至尊聖度母。" ("Oṃ, homage to the
venerable, noble Tārā.") *至尊* (most venerable) fits *rje btsun ma*. *聖* (noble,
ārya) fits *'phags ma*. *度母* ("the mother who carries across") fits *sgrol ma*.
The locked 至尊聖 is supported. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Chinese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-2 | MISMATCH | སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས (skar ma stong phrag tshogs pa rnams kyis) | A simile: "when about a thousand stars gather in one place, their light is unbearable to the eye; **likewise** light pours from her face" | "她以千顆星辰匯聚／所放射的光芒，極其熾燃" ("she blazes intensely with the light radiated by a thousand gathered stars") — no "like", so the stars' own light is what she blazes with. The number (千, a thousand) is right | Translator's call. Draft 4 dropped 如 ("like") on purpose (QA fixes log: the Tibetan *kyis* is instrumental, not a simile word), and the English reads the same way. To follow this commentary: "如千顆星辰匯聚，／放射極其熾燃的光芒" ("like a thousand gathered stars, she radiates intensely blazing light"). Keeps the locked 熾燃 |
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | Her body colour: "bright like the lustre of gold, with the aspect of blue". The lotus is a blue utpala held at her heart in the left hand | "手中以金藍色／水生蓮花為莊嚴者" ("whose hand is adorned with a golden-blue water-born lotus") — the colours go to the lotus | Translator decision (1-3 colours to the lotus), kept from the English. Tenga Tulku gives the colours to her body. Leave |
| 1-3 | MISMATCH | ཞི་བ (zhi ba) | Not a seventh item. *zhi ba* means the six perfections are "unstained by faults": giving by stinginess, discipline by broken vows, patience by anger, diligence by laziness, concentration by distraction, wisdom by faulty understanding | "布施、精進、持戒、寂靜、／忍辱、禪定與智慧為其行境者" ("generosity, diligence, discipline, peace, patience, concentration and wisdom are her domain") — seven items | Translator's call. The root lists *zhi ba* in the line, so the literal list is defensible, and the English has the same seven. To follow this commentary, make 寂靜 describe the six: "以寂靜的布施、精進、持戒、／忍辱、禪定與智慧為其行境者" ("whose domain is generosity, diligence, discipline, patience, concentration and wisdom, all peaceful"). Keeps the locked 寂靜 |
| 1-4 | MISMATCH | མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད (mtha' yas rnam par rgyal bar spyod) | *mtha' yas* = "infinite beings". She purifies the two obscurations that keep infinite beings from realising the perfection of wisdom, and so "acts in complete victory" | "以無邊的全然勝利而行持" ("who acts with boundless, complete victory") — "boundless" goes to her victory | Translator's call. The root's wording allows the Chinese, and the English has the same reading. To follow this commentary: "為無邊眾生以全然勝利而行持" ("who acts in complete victory for boundless beings") |
| 1-7 | MISMATCH | མེ་འབར་འཁྲུགས་པ་ཤིན་ཏུ་འབར་མ (me 'bar 'khrugs pa shin tu 'bar ma) | "Wisdom fire blazes from her body, burning and destroying all māras and obstacles". She herself blazes | "於翻騰的火焰中極其熾燃" ("blazes intensely **within** swirling flames") — the fire is around her, not hers | Translator's call. Draft 4 already makes her the one who blazes (QA fix), but 於…中 ("within") still puts the fire outside her. "自身烈焰翻騰，極其熾燃" ("flames swirl from her own body; she blazes intensely") follows this commentary. Keeps the locked 熾燃 |
| 1-10 | MISMATCH | རབ་ཏུ་དགའ་བ་བརྗིད་པ (rab tu dga' ba brjid pa) | The joy is hers: "she has supreme joy in giving all benefit and happiness to beings", with "great courage in that work" | "敬禮賜予極喜者，其威嚴／頭冠散發光鬘" ("homage to her who grants supreme joy; her majestic crown sends out garlands of light") | Follows the English consensus fix (3 of 4 commentaries read the joy as what she brings). Tenga Tulku is the one that disagrees. Leave, unless the translator reopens it ("敬禮具足極喜者", "homage to her who is endowed with supreme joy"; keeps the locked 極, 喜, 具足) |
| 1-11 | MISMATCH | ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ (phongs pa thams cad rnam par sgrol) | *phongs pa* are beings: "disciples with bad karma, destitute of emptiness and compassion, suffering and engaged in misdeeds". She places all of them in omniscient buddhahood | "使人從一切貧困中解脫" ("frees people from all poverty") — 貧困 is the condition, and in modern Chinese it means material poverty | Translator's call. The object is the destitute beings, and their lack is spiritual. "使一切匱乏的眾生都得解脫" ("frees all beings who are in want") keeps the literal sense and fits this commentary. 貧困 follows the English "destitution"; *phongs pa* is not a locked word |
| 1-12 | MISMATCH | བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར (brgyan pa thams cad shin tu 'bar) | "From **that** ornament" (the moon-crystal on her uṣṇīṣa) light blazes on "**all** beings tormented by the heat of the afflictions", cooling them. *thams cad* goes to the beings | "所有飾物都極其熾燃" ("all her ornaments blaze intensely") | Translator's call. The root's surface wording supports "all ornaments", and the English has the same. This commentary moves "all" to the beings and has the one moon ornament blaze. Leave |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | Rays from the dark-blue HŪṂ at her heart **protect** the beings in the seven levels (three lower realms, three higher, and desire and form taken together) from all suffering, or make them virtuous | "以吽字／摧毀七層者" ("who, with HŪṂ, destroys the seven levels") | "七層" (seven levels) is the translator decision and fits the number here (translator note: left open on purpose). The verb 摧毀 is literal for *'gems*, but this commentary reads it as protecting the beings there. Translator's call. The English ("shatter") has the same. Leave |
| 1-17 | MISMATCH | འབིགས་བྱེད ('bigs byed) | A verb: rays and mantras like vajra arrows from the HŪṂ at her heart shake and **pierce** Meru and Mandara | "令須彌山、曼陀羅山、頻闍山／與三世界皆震動" ("makes Mounts Meru, Mandara and Vindhya and the three worlds all shake") | Translator decision (1-17 Vindhya), recorded in the English and Chinese front matter. Tenga Tulku reads the verb. Leave |
| 1-21 | MISMATCH | ཞི་བའི་མཐུ (zhi ba'i mthu) | "The power by which all temporary and ultimate suffering is **pacified**" — an active, pacifying power | "圓滿具足寂靜威力者" ("perfectly endowed with tranquil power") — as a modifier, 寂靜 reads as "quiet, still", a quality of the power, not what it does | Translator's call. 寂靜 is locked for ཞི་བ and is right at 1-3 and 1-15; the lock is not wrong. Here the phrasing can carry the active sense and keep it: "圓滿具足能令寂靜的威力者" ("perfectly endowed with the power that brings peace"). Keeps the locked 圓滿具足, 寂靜, 威力 |

Readings that **support** the current Chinese (including places where earlier drafts had problems):
- 1-1: Avalokiteśvara, "the protector of the three worlds", shed many tears. They became a stream, an utpala grew from it, and she was born from its filaments. "三世界怙主面容所生蓮花，／從其花蕊綻放之中化現者" ("she who appeared from the opening stamens of the lotus born from the face of the Protector of the Three Worlds") has the lotus coming from him, not his face as a lotus. *myur ma* and *dpa' mo* are "acts quickly for beings" and "courage undaunted": "迅捷勇猛者" ("the swift and heroic one") fits. "剎那閃電光" ("a flash of lightning") fits her unobstructed wisdom-eye.
- 1-2: The autumn moon is clearest (no cloud, no dust), and the fifteenth-day moon is full. "一百輪／秋季滿月層層相疊" ("a hundred full autumn moons stacked together") fits, and her **face** is what is like them.
- 1-3: *dka' thub* = "the perfection of ethical discipline". "持戒" (keeping discipline) is right; *苦行* ("austerity") would have been the earlier English error. *spyod yul* = the perfection of wisdom, and the Chinese names "智慧" (wisdom). The Chinese keeps the root's order of the list.
- 1-4: *rgyal ba'i sras* are ārya-ground bodhisattvas who have the perfections of the ten grounds. "已證一切無餘波羅蜜的／諸菩薩所極力依止者" ("relied on deeply by the bodhisattvas who have attained all perfections without exception") names them plainly and has them relying on her. Draft 4 replaced 佛子 ("children of the Buddha"), which in modern Chinese can mean any Buddhist.
- 1-5: *'dod* = desire realm, *phyogs* = the seventeen abodes of the form realm, *nam mkha'* = the formless realm. "欲界、色界與無色界" ("the desire, form and formless realms") fits exactly. The seven worlds are the five abodes of the desire realm plus form and formless, and "七個世界" (seven worlds) has the number right. "能將一切無餘召集而來" ("able to summon all, leaving none") fits drawing every being to the higher realms and liberation, none left in the lower realms.
- 1-6: *sna tshogs dbang phyug* is read with the others as "the great direction-protectors" (plural), so "諸自在天" ("the various Īśvara gods") fits. The god order (Śakra 帝釋, Agni 火神, Brahmā 梵天, Vāyu 風神) follows the root. *'byung po* = "a class of pretas that roam the sky, always tormented by fear and suffering": "鬼神" (ghosts and spirits) fits. *ro langs* = "corpses made to act alive by the Māra of the dark side": "起屍" ("risen corpses") fits. *dri za* = bardo wanderers, and "乾闥婆" (gandharva) is the standard term. *gnod sbyin* = yakṣas with miraculous power: "夜叉" fits. They stand before her: "在她面前讚頌" ("praise her in her presence") fits.
- 1-7: *pha rol 'khrul 'khor* = the "machinations of the dark-side māras" behind adversaries' diseases and harm. "敵方咒術幻輪" ("the adversaries' sorcery and magic wheels") fits. Right leg drawn in, left extended ("右屈左伸"): the order is right.
- 1-8: "*phyag 'tshal tu re* gives the Venerable One's name", so "都咧" as her name fits (translator decision). The Māra line is glossed as the army of the four māras, and "魔的勇士" ("Māra's champions") fits the translator decision. "令人大怖畏者" ("the one who causes great terror") fits her wrathful form. "蓮花面容現忿怒顰眉" ("her lotus face shows a wrathful frown") fits.
- 1-9: The left hand at her heart makes the Three-Jewels mudrā, holding the utpala stem. The right hand is in the supreme-giving gesture, **its palm** adorned with a thousand-spoked wheel. "手掌以無餘十方之輪為飾" ("her palm is adorned with the wheel of all ten directions") has one wheel, on the palm. "自身的光聚翻騰湧動者" ("whose own masses of light swirl and surge") fits the wheel's rays "swirling without measure".
- 1-10: The five-family crown ornament fits "頭冠" (crown). "都達咧的大笑聲" ("the great laughter of tuttāre") fits. "令魔與世間皆受攝伏" ("brings Māra and the world under her control") fits "overwhelms or brings under control all three worlds".
- 1-11: *sa gzhi skyong ba* = the ten direction-guardians and their retinues, all summoned. "能將守護大地的神眾／全都召集而來者" ("who can summon all the hosts of gods who guard the earth") has "all" on the hosts, as he does. "顫動的忿怒顰眉" ("a trembling wrathful frown") fits "the frown moving like clouds".
- 1-12: Amitābha adorns her in the midst of her hair and light shines from him constantly. "從她髮髻中的阿彌陀佛／恆常放出極其燦爛的光芒" ("from Amitābha in her hair-knot, an intensely brilliant light shines constantly") fits. The moon ornament is on her head, as he says ("以月牙莊嚴頭頂", "adorned on the crown of the head with a crescent moon").
- 1-13: She sits amid a garland of flames like the fire at the end of the aeon, right leg extended and left bent. "如劫末之火般／熾燃的火鬘中央", "右伸左屈" fit. "摧毀敵人的軍隊" ("destroys the enemies' armies") fits the armies of the affliction-enemies.
- 1-14: She presses the earth with both palms and strikes it with both soles. "以手掌拍擊大地，／並以雙足踐踏" ("strikes the earth with her palms and tramples it with both feet") fits; draft 4 restored the palms.
- 1-15: *bde ma* / *dge ma* / *zhi ma* are glossed as bliss, virtue (the fruit of the path of virtue) and the pacification of habitual stains, and "安樂、善妙、寂靜者" ("the blissful, virtuous, peaceful one") fits. The mantra is "adorned with oṃ at the beginning and svāhā at the end"; "圓滿具足嗡梭哈" ("perfectly endowed with oṃ svāhā") puts them in his recitation order. "大罪障" ("great sins and obscurations") fits the ten non-virtues and five heinous acts, and "sins and obscurations destroyed at the root".
- 1-16: "The peaceful mantra is the ten syllables; the mantra practised in the fierce way is *oṃ tāre hūṃ hara hara hūṃ*." "布列十字咒語" ("sets out the ten-syllable mantra") fits the first. *rig pa hūṃ* is a mantra, and "明咒吽字" ("the knowledge-mantra HŪṂ") fits. "徹底粉碎敵人之身" ("utterly crushes the enemies' bodies") fits.
- 1-17: "The Venerable One herself, in fierce wrath, stamps her feet." "敬禮都咧頓足者" ("homage to Ture, who stamps her feet") has Ture as her, not a syllable she uses (draft 4 QA fix). The rays come from the HŪṂ seed at her heart, and "她即是吽字形相的種子字" ("she is the seed-syllable in the form of HŪṂ") fits. The three worlds are gods above the earth, humans on it and nāgas below, and "三世界" fits.
- 1-18: The full moon is "shaped like a lake of nectar pleasing to the gods", held in her left hand on the open utpala. "手持形如天湖、／帶有鹿紋的月亮者" ("who holds the deer-marked moon shaped like a celestial lake") fits. "念誦兩遍達咧，並以呸字" ("reciting tāra twice, and with the syllable phaṭ") has only tāra twice, as he does. The locked 達咧 (mantra syllable) avoids reading her name.
- 1-19: "The great world-protectors — the kings of the hosts of gods — and gods and kinnaras rely on her." "天眾之王所侍奉，／諸天與緊那羅所依止者" ("served by the kings of the god-hosts, relied on by gods and kinnaras") is the right way round. "周遍喜樂鎧甲" ("all-round armour of joy") keeps *kun nas*; he reads the armour as protecting those who rely on her from all ill omens at all times. *rtsod pa* = quarrels from unhappy minds: "爭鬥" ("strife") fits; "惡夢" ("bad dreams") fits.
- 1-20: "Her **two eyes**, like the sun and moon", blaze with light. "雙目如圓滿日月，／放射極其明亮之光者" ("whose two eyes, like the full sun and moon, radiate extremely bright light") has the eyes as the subject. *rims nad* are contagious diseases causing unbearable suffering, and "極其猛烈的傳染病" ("extremely fierce contagious diseases") fits. "兩遍喝囉" and "都達咧" fit the two *hara* and *tuttāre*.
- 1-21: "the suchness of body, white OṂ; of speech, red ĀḤ; of mind, blue HŪṂ, set at the three places of the body". "身上安立三真如" ("the three suchnesses set upon her body") has them on her, not establishing her. "邪魅、起屍、夜叉眾" fits "the harms of *gdon*, *ro langs* and *gnod sbyin*".
- 1-22: "the praise by the root mantra … **and** the twenty-one homages", counted 1 + 6 + 7 + 1 + 6. That is two items, which fits "這篇以根本咒所作的讚頌，／以及二十一偈敬禮" ("this praise made with the root mantra, and the twenty-one verses of homage"; the translator decision keeps "and").

Style notes (not errors):
- 1-4 "敬禮如來頂髻者" ("homage to the uṣṇīṣa of the tathāgatas") is literal. Tenga Tulku reads the line as the tathāgatas revering her, because she is the Mother, Prajñāpāramitā. He does not gloss *gtsug tor* itself.
- 1-9 "十方" ("the ten directions") for *ma lus phyogs* ("all directions") is the ordinary Chinese way to say "every direction". It adds no real number. Fine for a Chinese reader; noted for the second pass.
- 1-11 "守護大地的神眾" ("the hosts of gods who guard the earth") is literal. Tenga Tulku identifies them as the ten direction-guardians (Brahmā above, Indra in the east … the earth-lord below). "十方護法神眾" would name them exactly, but the literal line is fine.
- 1-13 "為喜悅所環繞" ("surrounded by joy") and 1-16 "周遭環繞極喜者" ("the one surrounded all around, supremely joyful"): Tenga Tulku reads *kun nas bskor* as joyful, faithful disciples who circle her. The Chinese allows that. "為歡喜的信眾所環繞" ("surrounded by joyful devotees") would make it explicit and keeps the locked 喜.
- 1-18 "毒物" ("poisonous substances") leans to physical toxins. Tenga Tulku's moving poisons are also the ignorance and afflictions in beings' minds. "諸毒" ("all poisons") is wider. Minor.
- 1-22 The two lines are a noun phrase with no verb. The Tibetan is the same, but a Chinese reader may feel the sentence is unfinished. A native reader should judge.

Second pass (kāya / named entity / number): no kāya terms at issue in the Chinese. Named entities are right: Avalokiteśvara (三世界怙主), Śakra (帝釋), Agni (火神), Brahmā (梵天), Vāyu (風神), Amitābha (阿彌陀佛), Meru (須彌山), Mandara (曼陀羅山), the kinnaras (緊那羅), the bodhisattvas (菩薩). Vindhya (頻闍山) is the translator decision. Numbers are right: 一百 (100) moons, 千 (1,000) stars, 七 (7) worlds, 十字 (10 syllables), 七層 (7 levels), 三世界 (3 worlds), 二十一 (21) homages, 兩遍 (twice). The only surprise is 十方 at 1-9 (style note). The seven-item perfection list at 1-3 is a row.

Textual notes (Tenga Tulku's quotation vs our root, not errors; the Chinese follows our root):
- 1-1 *ge sar phye ba* → *bye ba*. He glosses it as "born from its filaments".
- 1-12 *zla ba'i rtse mos* → *zla ba'i dum bus* ("a piece of moon-crystal"). "月牙" (crescent moon) follows our root. Also *'od ni mdzad* → *'od rab mdzad*.
- 1-13 *bskal pa tha ma'i* → *mtha' ma'i* (same meaning); *bskor dgas* → *bskor* (the quote drops *dgas*; the gloss has *rab tu dga' ba*).
- 1-14 *khro gnyer can mdzad* → *khro gnyer spyan mdzad* ("frowning eyes"). He glosses the two turbulent eyes. "現忿怒顰眉" ("shows a wrathful frown") follows our root.
- 1-16 *sgron ma* (lamp) → *sgrol ma* (liberator). "明燈" (lamp) follows our root.
- 1-20 *rims ni* → *rims nad* (same meaning).
- 1-21 *tu re rab mchog* → *tu re'i rab mchog*. He reads it as her granting "Ture's excellent and supreme wishes". "最勝都咧" ("the supreme Ture") follows our root.
- 1-8 The quote reads *'jigs pa chen* (the gloss has *chen mos*) and *bdud kyi dpa' bo*, but the gloss explains *bdud kyi dpung* (Māra's army).
- Spelling only: 1-7 *trad/traṭ*, 1-9 *'khrug/'khrugs*, 1-11 *nus ma/nus pa*, 1-10 and 1-20 *tuttāra*, 1-18 *ri dags/ri dwags*, 1-17 *man dā ra/mandara*.

**Result: 12/22 clean, 0 verse(s) with errors, 10 with mismatches only (1-2, 1-3, 1-4, 1-7, 1-10, 1-11, 1-12, 1-14, 1-17, 1-21); 11 mismatch row(s).**

#### Chapter 2 — 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Chinese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-1 | MISMATCH | ལྷ་མོ (lha mo) | "*lha mo de la*" ("to **that** goddess") points back to the Venerable One, Tārā herself, of the 21 homages | "對此天女具足虔敬" ("has full devotion to this 天女") — 天女 is the locked word, but in Chinese it often means a celestial maiden (devakanyā, apsaras), a lesser being in a god's heaven | Translator's call, already flagged in the word list and translator notes. 此 ("this") keeps the referent on Tārā, so it is not a wrong referent. If a native reader hears 天女 as a lesser being, change the lock in `zh-decisions-general.json` and use "對此聖尊具足虔敬" ("has full devotion to this noble goddess") |
| 2-3 | MISMATCH | མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར (myur du dbang ni bskur bar 'gyur) | The seventy million Victors of the ten directions **empowered the Venerable One** as the Mother, the Perfection of Wisdom. Relying on one-pointed prayer to her, the reciter gains higher-realm qualities, greatness (like a universal monarch, or Indra and Brahmā) and finally buddhahood | "七千萬尊佛／將迅速為此人授予灌頂" ("seventy million buddhas will swiftly confer empowerment on this person") — 為此人 ("on this person") makes the reciter the recipient | Translator's call. The root's future *'gyur* in a benefits passage more naturally has the reciter as recipient, and Tenga Tulku's reading is his own. "七千萬尊佛／將迅速授予灌頂" ("seventy million buddhas will swiftly confer empowerment") leaves the recipient open, as the English does. Keeps the locked 灌頂 |

Readings that **support** the current Chinese:
- 2-1: *blo ldan* = "a person with intelligence", and "若有智者" ("if there is a wise person") fits. "以至誠之心念誦此讚" ("recites this praise with a sincere heart") fits *rab tu brjod*, the reciting of the praise of the 21 homages.
- 2-2: "於黃昏與黎明起身後" ("after rising at dusk **and** at dawn") keeps both times, which he calls "the two main ones" (her wrathful form at dusk, her peaceful form at dawn). "憶念她" ("recollecting **her**") has her as the object, as he does ("recalling her qualities at all times", "by merely recalling [her] she grants all fearlessness"). The Hindi needed a fix here; the Chinese does not. "一切無畏" fits fearlessness from the eight and sixteen fears. "一切罪障都將徹底平息" ("all sins will be fully pacified") fits all non-virtue pacified. "一切惡趣都將被摧毀" ("all lower realms will be destroyed") fits freedom from the lower-realm abodes.
- 2-3: "七千萬" = 70 million, so the number is right. "佛" fits *rgyal ba* (Victors, the buddhas). "此人還會獲得比這更殊勝的成就，／並抵達那究竟的佛果" ("this person will also gain attainment greater than this, and reach that ultimate buddhahood") fits his greatness and ultimate buddhahood. The locked 更殊勝 fits the comparative.
- 2-4: The moving poisons are snakes, fang poisons, meat and hair poisons; the stationary are the obscurations that stay in beings' minds. "無論是靜止的毒還是移動的毒" ("whether stationary poison or moving poison") fits. "其毒極其猛烈" ("its poison is extremely fierce") carries *de yi* ("of that one"), as he reads it ("the poison of that person"). "即使是已經吃下或喝下的" ("even if already eaten or drunk") fits. "憶念她，也能將其徹底消除" ("by recollecting **her**, it can be fully removed") fits "by merely recollecting the Venerable One's blessing".
- 2-5: *gdon* = "the hosts of harm", *rims nad* = epidemic from disturbed elements, and "邪魅、傳染病、毒物" ("harmful spirits, contagious diseases, poisons") fits. "其他眾生也同樣如此" ("and so it is for other beings too") fits "not only for oneself — she protects other beings from all suffering too". The block ends with a full stop, so there is no run-on into 2-6.
- 2-6: "願諸障礙皆無，並一一被摧毀" ("may all obstacles be gone, and be destroyed one by one") is optative and agrees with his "*'joms par gyur cig*" (translator decision). The temporary wishes are children and wealth; the ultimate wish is buddhahood. "一切所願皆能圓滿" ("all wishes can be fulfilled") fits.

Style notes (not errors):
- 2-6 "誦持" ("recite and hold") for *mngon par brjod*: Tenga Tulku reads it as "recite with manifest faith". "以虔信誦持" ("recite with devoted faith") is closer. Minor.

**Result: 4/6 clean, 0 verse(s) with errors, 2 with mismatches only (2-1, 2-3); 2 mismatch row(s).**

**Overall: 29 verses checked — 17 clean, 0 with errors, 12 with mismatches only.**

For the reviewer: this is a preliminary machine self-check. A specialist in the Tibetan commentarial tradition and a native Chinese reader must both review it before any fix is treated as settled. No row is mechanical. The closest to it are 1-7 (於…中 still puts the fire outside her) and 1-21 (寂靜 as a quiet quality rather than a pacifying power); both fixes keep the locked words. Every other row is a translator's call or a settled translator decision. Compared with the Hindi check on this commentary, the Chinese already has the fixes the Hindi needed at 1-20 (the eyes as subject), 2-2 and 2-4 ("her", not "this"); it adds 1-21 and 2-1.
