## Praise to the Twenty-One Taras — Commentary Fact-Check (Chinese)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md`, Jetsün Drakpa Gyaltsen (1147–1216), *sgrol ma phyag 'tshal nyi shu rtsa gcig gi bstod pa'i rnam bshad gsal ba'i 'od zer*. Commentary id `drakpa-gyaltsen`.
- **Translation audited:** `3-TRANSFORMATIONS/Translations/zh-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general.md` (Chinese, Traditional characters, general grade, draft 4)
- **Root text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` (critical edition)
- **Date:** 2026-09-24

Method: a strict term-by-term alignment against this commentary's own glosses. It checks body (kāya), named entities, numbers, similes, agents, the order of lists and what modifies what. It is not a gist check. For each verse, every word Drakpa Gyaltsen glosses was aligned as Tibetan | gloss | Chinese | MATCH/MISMATCH before a verdict was given. Only the ⚠ ERROR and MISMATCH rows are shown below. Ground truth is the commentary's literal reading. Elaboration the verse need not carry was not flagged. The fact-checked English, the English consensus table, the Chinese word list and the Chinese reports (back-translation, light check, QA) were used as context only. Where the Chinese follows one of the seven settled English translator decisions, the row says so. Every Chinese phrase cited carries a one-line English gloss. Suggested fixes are in Traditional characters and keep the locked words. This is a preliminary self-check, not a scholarly sign-off. A domain specialist and a native Chinese reader must review it before it is treated as final (an LLM never marks its own output complete).

Extraction notes: there are 30 transclusion markers (I-3, 1-1 to 1-22, 2-1 to 2-6, a-1), with no empty buckets and no shift (`extract_commentary.py --strict`: 30 passages, 0 empty). Each bucket quotes its root line(s) and then glosses them. Every bucket ends with an ID such as `^1-2`. These are the commentary file's own paragraph IDs, which run one ahead of the root IDs; they are not transclusion markers, and the attribution is correct. I-1 and I-2 are not covered. Some buckets quote without glossing:
- I-3 is quoted with no gloss.
- 1-16 only identifies the two mantras.
- 2-1 has a fragmentary gloss ("[with] body, speech and mind, to the goddess").
- a-1 quotes the root colophon (in a variant reading) and then adds the translator's colophon (Nyen Lotsāwa, in the lineage from Nāgārjuna) and the author's colophon.

Scope is therefore 30 verses. I-1, I-2 and the headings were not checked.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6, a-1 (Chinese general, draft 4) |

#### Chapter I — I-3

Drakpa Gyaltsen quotes the homage (*oṃ rje btsun ma 'phags ma sgrol ma la phyag 'tshal lo*) with no gloss. The Chinese "嗡，敬禮至尊聖度母。" ("Om, homage to the venerable, noble Tārā.") matches word for word. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Chinese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | "*gser sngo*: a colour bright like the lustre of refined gold". Glossed on its own, before and apart from *chu nas skyes* ("the hand-emblem, the lotus", held in the left hand). One gold hue, not gold + blue, and not attached to the lotus | "手中以金藍色／水生蓮花為莊嚴者" ("whose hand is adorned with a **golden-blue** water-born lotus") | **Translator decision** (colours to the lotus, as in the English). Drakpa Gyaltsen gives a single gold colour that is probably hers. Leave, or note it |
| 1-6 | MISMATCH | སྣ་ཚོགས་དབང་ཕྱུག (sna tshogs dbang phyug) | "the great Maheśvara (*dbang phyug chen po*), who became the lord of them [Indra, Agni, Brahmā, Vāyu], offers worship at her feet". One being | "諸自在天" ("the various Īśvara gods", plural) | Single-commentary reading. The English consensus left the plural, because three other commentaries read it as plural. Leave |
| 1-8 | MISMATCH | ཏུ་རེ་འཇིགས་པ་ཆེན་མོ (tu re 'jigs pa chen mo) | His text reads *chen mos* (instrumental): "by the terror of TURE she dispels all māras; because she terrifies the māras she is the Great Terrifying One". Ture is the mantra | "敬禮都咧，令人大怖畏者" ("homage to Ture, the one who causes great terror", with Ture as her name) | **Translator decision** (Ture as her name). Leave |
| 1-8 | MISMATCH | བདུད་ཀྱི་དཔའ་བོ (bdud kyi dpa' bo) | "the *dpa' bo* is the māra of the afflictions (*nyon mongs pa'i bdud*); by conquering it, the other three [māras] are destroyed in passing" | "魔的勇士" ("Māra's warriors / heroes") | **Translator decision** ("champions of Mara"). Leave |
| 1-11 | MISMATCH | ས་གཞི་སྐྱོང་བའི་ཚོགས (sa gzhi skyong ba'i tshogs) | "the ten direction-protectors (*phyogs skyong bcu*)", who obey her and act as her messengers | "守護大地的神眾" ("the hosts of gods who guard the earth"). Literal, and it follows the English, but it does not name the class. Chinese has a plain word for it, 護方神 | Optional: "敬禮能將守護大地的護方神眾／全都召集而來者" ("homage to you who can summon all the hosts of direction-guardian gods who protect the earth"). Keeps locked 眾 and 能. Judgment; can leave |
| 1-11 | MISMATCH | ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ (phongs pa thams cad rnam par sgrol) | "**all beings** tormented by adverse conditions and destitute of favourable ones: she frees them from suffering and sets them in happiness". "All" goes with the *beings* she frees | "使人從一切貧困中解脫" ("frees people from **all poverty**"). "All" now goes with the condition, and 貧困 is mainly material poverty | e.g. "使一切困乏的眾生都得解脫" ("frees all destitute beings"). Judgment: the Chinese follows the English "liberate from all destitution" |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | First reading: rays from the vajra and HŪṂ "fill the abodes of the seven classes of beings (*'gro ba rigs bdun*) and clear all their obstacles". Alternative: "she scatters into pieces the nāgas, asuras and others dwelling in the seven underground levels" | "以吽字／摧毀七層者" ("who with the syllable hūṃ **destroys the seven levels**"). The levels themselves are destroyed | **Translator decision** ("seven levels", left open; translator note in the file). The verb 摧毀 fits only the alternative, and there the beings in the levels are scattered, not the levels. Leave, or soften the verb |
| 1-17 | MISMATCH | འབིགས་བྱེད ('bigs byed) | A verb: "Meru and Mandara (*ri rab man dā ra ba*, outside the trichiliocosm) are **pierced** by the light rays of the syllable HŪṂ" | "令須彌山、曼陀羅山、頻闍山／與三世界皆震動" ("makes Mount Meru, Mount Mandara, Mount Vindhya and the three worlds all tremble") | **Translator decision** (Vindhya; translator note in the file). Leave |
| 1-20 | MISMATCH | ཧ་ར་གཉིས་བརྗོད (ha ra gnyis brjod) | "*ha ra gnyis brjod*: by the mantra-speech of **the two, peaceful and wrathful** (*zhi khro gnyis*), she dispels extremely fierce epidemics". *Gnyis* is read as the two mantras, not as "twice" | "念誦兩遍喝囉，並以都達咧" ("reciting hara **twice**, and with tuttāre") | "Twice" is the plain grammar and the English reading. Drakpa Gyaltsen alone reads "the two". Leave |
| 1-21 | MISMATCH | དེ་ཉིད་གསུམ་རྣམས་བཀོད་པ (de nyid gsum rnams bkod pa) | "OṂ ĀḤ HŪṂ, the three, are set at her **body, speech and mind** (*sku gsung thugs*)". Three places | "敬禮身上安立三真如" ("homage to you, on whose **body** the three suchnesses are set"). 身上 ("on the body") is not in the root. A reader will put all three on the body, which leaves out speech and mind | Recommended: drop 身上: "敬禮安立三真如，" ("homage to you, on whom the three suchnesses are set"), as the English "set upon you". If the reviewer wants his reading spelled out: "敬禮身語意安立三真如，" ("… set at body, speech and mind") |
| 1-22 | MISMATCH | རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག (rtsa ba'i sngags kyi bstod pa 'di dang / phyag 'tshal ba ni nyi shu rtsa gcig) | "this praise of the peaceful and wrathful ones is **this very praise** by the twenty-one homages". One praise, described two ways | "這篇以根本咒所作的讚頌，／以及二十一偈敬禮。" ("this praise made with the root mantra, / **and** the twenty-one verses of homage"). Two items | **Translator decision** ("and"). Leave |

Readings that **support** the current Chinese:
- 1-1 *chu skyes zhal gyi*: "from his [Avalokiteśvara's] tears arose a lotus or utpala; she was born from the opening lotus". "三世界怙主面容所生蓮花，／從其花蕊綻放之中化現者" ("who appeared from the opening stamens of the lotus born from the face of the Protector of the Three Worlds") has a lotus arising from him, not a face that is a lotus. That fits (English consensus Fix #1). *Sgrol ma* = liberates from saṃsāra, *myur ma* = swift for beings' sake, *dpa' mo* = heroic in conquering the afflictions: "度母，迅捷勇猛者" ("Tārā, the swift and valiant one") fits. *Spyan … glog* → "雙目猶如剎那閃電光" ("eyes like a momentary flash of lightning") fits.
- 1-2: "a full moon heaped up many hundreds of times" fits "猶如一百輪／秋季滿月層層相疊" ("like a hundred autumn full moons heaped layer on layer"). He says the moons and the stars "are examples of countless radiating rays". "她以千顆星辰匯聚／所放射的光芒，極其熾燃" ("she blazes intensely with the light radiated by a thousand gathered stars") follows the root's instrumental and keeps the stars as light, with no added simile.
- 1-3 *dka' thub* = *tshul khrims* (ethical discipline): "持戒" ("keeping the precepts, ethical discipline") is exact. *spyod yul nyid ma* = wisdom, and "智慧" ("wisdom") is named. *zhi ba* = [pacifying] the afflictions → "寂靜" ("peace"). The list keeps the root order: 布施、精進、持戒、寂靜、忍辱、禪定、智慧.
- 1-4 *de bzhin gshegs pa'i gtsug tor* = like the uṣṇīṣa of all tathāgatas → "如來頂髻" ("the tathāgata's uṣṇīṣa"). *mtha' yas rnam par rgyal bar spyod* = she acts victorious over all opponents, māras and enemies → "以無邊的全然勝利而行持" ("who acts with boundless, complete victory"). *ma lus pha rol phyin pa thob pa'i* = the ten perfections, attained; the Chinese gives them to the bodhisattvas ("已證一切無餘波羅蜜的／諸菩薩", "the bodhisattvas who have realised all the perfections without exception"), which fits the genitive. *rgyal ba'i sras* = all the bodhisattvas → "諸菩薩" ("the bodhisattvas") is exact. *shin tu bsten* = they carry her as their crown → "所極力依止" ("deeply relied on") fits.
- 1-5 *'dod / phyogs / nam mkha'* = the desire, form and formless realms, and *gang* = fills → "充滿欲界、色界與無色界" ("fills the desire, form and formless realms") is exact (English consensus Fix #11). *'jig rten bdun* = five desire-realm destinies + form realm + formless realm → "七個世界" ("seven worlds") fits. *Tuttāre hūṃ* is "the mantra" → "以都達咧與吽字" ("with tuttāre and the syllable hūṃ") fits.
- 1-6: Indra ("帝釋"), Agni ("火神"), Brahmā ("梵天") and Vāyu ("風神") match, in the root order. *'byung po* = Gaṇapati and the like → "鬼神" ("spirits"). *ro langs* = "Maheśvara and the like", a class → "起屍" ("risen corpses", vetāla). *dri za* = Pañcaśikha etc. → "乾闥婆" (gandharva). *gnod sbyin* = Vaiśravaṇa etc. → "夜叉" (yakṣa). *tshogs* = the eight classes → "眾" ("hosts"). *mchod* → "所供養" ("worshipped by"). *mdun nas bstod* → "在她面前讚頌" ("praise her in her presence").
- 1-7 *pha rol 'khrul 'khor*: "with her wrathful speech she destroys and turns back the evil applications that others have performed". "徹底摧毀敵方咒術幻輪" ("utterly destroys the enemy's sorcery devices") fits; 咒術 ("sorcery") makes the evil rite explicit. The posture "right drawn in, left extended" matches ("右屈左伸"). He says she sits amid blazing fire; "於翻騰的火焰中極其熾燃" ("blazes intensely amid the swirling flames") fits.
- 1-8 *'jigs pa chen mo*: she terrifies the māras. "令人大怖畏" ("who causes great terror") is active; it does not have the "afraid" problem of the old English "Fearful" (English consensus Fix #4). *chu skyes zhal* = her own face, like an opened lotus → "蓮花面容" ("lotus face"). *khro gnyer ldan mdzad* = she abides as the wrathful one → "現忿怒顰眉" ("shows a wrathful frown"). *dgra bo thams cad* = "all the adverse side, the afflictions and so on" → "無餘誅殺一切怨敵" ("slays all enemies without exception").
- 1-9: one wheel on the palm of the right hand (supreme-giving gesture). "手掌以無餘十方之輪為飾" ("her palm is adorned with the wheel of all the ten directions") is singular and fits (English consensus Fix #5). 十方 ("the ten directions") is the ordinary Chinese for "all directions". The three extended fingers at the heart symbolise the Three Jewels: "以三寶手印之指，／莊嚴於心間" ("adorns her heart with fingers in the gesture of the Three Jewels") fits.
- 1-10 *rab tu dga' ba*: "fulfils the wishes of all beings, [who are] supremely joyful". The joy is what she brings, so "賜予極喜者" ("the one who grants supreme joy") fits (English consensus Fix #6). *brjid pa* = outshining others, kept on the crown ("其威嚴頭冠", "her majestic crown") as in the root. The laughter is the mantra's → "以都達咧的大笑聲" ("with the great laughter of tuttāre"). *bdud dang 'jig rten dbang du mdzad* → "令魔與世間皆受攝伏" ("brings Māra and the world under her control").
- 1-12: a first-day moon adorns her head → "以月牙莊嚴頭頂" ("adorns her head with a crescent moon"). *snang ba mtha' yas* (Amitābha) adorns her head amid her locks and "radiates immeasurable rays for beings" → "從她髮髻中的阿彌陀佛／恆常放出極其燦爛的光芒" ("from Amitābha in her locks, intensely brilliant light shines constantly"). Amitābha is the source of the light, as he says.
- 1-13: the fire at the end of the eon, when seven suns rise → "如劫末之火般熾燃的火鬘" ("a garland of fire blazing like the fire of the eon's end"). The posture is the reverse of 1-7: "右伸左屈" ("right extended, left bent") fits. *dgra yi dpung* = all adverse things → "敵人的軍隊" ("the enemy's armies").
- 1-14 *phyag gi mthil gyis bsnun*: "she strikes the ground with her left hand and makes the threatening gesture". "以手掌拍擊大地" ("strikes the earth with the palm") leaves the number of hands open, as the root does, and 拍擊 means "strike", so the Hindi row (plural hands, "injure") does not recur. "並以雙足踐踏" ("and tramples with both feet") follows *zhabs kyis brdung*.
- 1-15: *bde ma* = endowed with uncontaminated bliss, *dge ma* = free of the afflictions, *zhi ma* = suffering pacified, *mya ngan 'das* = conceptions exhausted. "安樂、善妙、寂靜者，／以涅槃寂靜為行境" ("blissful, virtuous, peaceful, whose sphere is the peace of nirvāṇa") fits. "摧毀大罪障" ("destroys great negativity") follows the root word.
- 1-16 *yi ge bcu pa'i ngag* = the peaceful mantra *oṃ tāre tuttāre ture svāhā* → "十字咒語" ("the ten-syllable mantra"). *rig pa hūṃ* = the wrathful (vidyā) mantra *oṃ namaḥ tāre namo hari hūṃ hara svāhā* → "明咒吽字" ("the vidyā-mantra syllable hūṃ") fits (English consensus Fix #7).
- 1-17: from the HŪṂ seed she is generated as the wrathful form → "她即是吽字形相的種子字" ("she is the seed syllable in the form of hūṃ") fits. "敬禮都咧頓足者" ("homage to Ture, who stamps her feet") makes Ture Tārā herself (English consensus Fix #8); Drakpa Gyaltsen does not gloss *tu re'i zhabs*. *'jig rten gsum* = the desire, form and formless realms → "三世界" ("the three worlds").
- 1-18: "she holds in her hand the moon disc, which is **like a celestial lake**; *ri dwags rtags can* is the moon". "手持形如天湖、／帶有鹿紋的月亮" ("holds the moon shaped like a celestial lake, bearing the deer-mark") puts both descriptions on the moon, so the simile tenor is right. The TĀRA mantra dispels stationary and moving poisons; "消除所有毒物，無一遺漏" ("removes every poison, none left") covers both, and "並以呸字" ("and with phaṭ") keeps "twice" on tāra only.
- 1-19 *lha yi tshogs rnams rgyal po*: "the lords of those hosts of gods, and Druma king of the kinnaras, worship at her feet". "敬禮天眾之王所侍奉" ("homage to you, served by the king(s) of the hosts of gods") puts the kings in the agent position; she is not their sovereign (English consensus Fix #9). The Hindi row on this verse does not recur. *mi'am ci* = kinnara → "緊那羅". *go cha* = the armour of deity-body and mantra → "周遍喜樂鎧甲" ("all-round armour of joy").
- 1-20 *rims nad* = epidemics → "極其猛烈的傳染病" ("extremely fierce infectious diseases"). The eyes "like the full sun and moon", and the light comes from them → "雙目如圓滿日月，／放射極其明亮之光" ("eyes like the full sun and moon, radiating very bright light").
- 1-21 *zhi ba'i mthu* = the might of pacifying the afflictions → "寂靜威力" ("the might of peace"). *gdon, ro langs, gnod sbyin* → "邪魅、起屍、夜叉眾" in the root order. *rab mchog* → "最勝" ("most supreme").

Style notes (not errors):
- 1-1: Drakpa Gyaltsen says the lotus grew from Avalokiteśvara's **tears** (*spyan chab*). "面容所生" ("born from the face") follows the root's *zhal*, which is fine.
- 1-2: the root has *brgya* ("a hundred") and *stong phrag* ("thousands"); he says "many hundreds". "一百輪" ("a hundred") and "千顆" ("a thousand") are fine.
- 1-3: "……為其行境者" ("… are her sphere") frames the whole list as her sphere, and names wisdom inside it. Acceptable, as in the English.
- 1-5 and 1-11 *'gugs*: he reads it as bringing under her power ("able to bring kings and others under control"; the protectors "act as her messengers"). "召集" ("summon, convene") is weaker than the classical 鉤召 ("hook and summon"). A reviewer may prefer 鉤召 or "召請攝伏".
- 1-8 "令人大怖畏" ("causes people great terror"): in his gloss those terrified are the māras. 令人 is an ordinary idiom and is fine; the reviewer may check it does not suggest she frightens her devotees.
- 1-9 *rang gi 'od kyi tshogs rnams 'khrug*: he says the wheel's rays outshine other lights. "自身的光聚翻騰湧動" ("her own mass of light swirls and surges") keeps the light but not the outshining. Fine.
- 1-10: he explains *'od kyi phreng ba* as "garlands of many jewels"; the Chinese keeps the root's "光鬘" ("garlands of light"). Fine.
- 1-11 and 1-14: "以顫動的忿怒顰眉和吽字" / "現忿怒顰眉，以吽字" ("with the quivering frown and the syllable hūṃ") makes the frown and HŪṂ two instruments. The root has "the HŪṂ of the frowning one", and he places the HŪṂ at the heart of her wrathful form. Minor.
- 1-12: he reads *brgyan pa thams cad shin tu 'bar* as the moon's light blazing; the Chinese keeps the root's "所有飾物" ("all the ornaments"). Fine.
- 1-15: the root and Drakpa Gyaltsen both read *swāhā oṃ*; the Chinese "嗡梭哈" ("oṃ svāhā") reverses the order, as the English does ("om and svaha"). He does not comment on it. The English consensus left this (only one commentary raised it; two say oṃ opens and svāhā closes the mantra). If the reviewer wants the root order: "圓滿具足梭哈與嗡". Optional.
- 1-15: he says she destroys others' afflictions "by her nature as dharmakāya". This is elaboration; no *sku* is in the root line and none is needed.
- 1-16 "十字咒語": in everyday modern Chinese 十字 first reads as "cross" (十字架, 十字路口), so a general reader may see "the cross mantra". The number is right. For the native reader: "十個字的咒語" or "十字（十音節）咒語" ("the ten-syllable mantra") keeps locked 咒.
- 1-16 "敵人之身" ("the enemy's body") follows the root's singular *dgra yi lus*. Fine.
- 1-19 *rtsod*: he says "the disputes of the tīrthikas". "爭鬥" ("fighting, strife") leans to physical conflict. "爭執" or "爭論" ("disputes") is closer. Optional.
- 1-20: he pairs the right eye with the moon and the left with the sun. The Chinese does not assign eyes, which is fine.
- 1-21 *'joms pa tu re rab mchog*: he attributes the destroying to "the power of the ten-syllable mantra". "摧毀它們的最勝都咧" ("the supreme Ture who destroys them") fits if Ture is her name (see 1-8). "它們" ("them", used for things or animals) is a little cold for classes of beings; the native reader may prefer "此等" or "諸眾".
- 1-22: the line ends with a full stop. In the root, 1-22 is a noun phrase that runs on into 2-1. The Chinese "此讚" ("this praise") in 2-1 still links back.

**Result: 13/22 clean, 0 verse(s) with errors, 9 with mismatches only (1-3, 1-6, 1-8, 1-11, 1-14, 1-17, 1-20, 1-21, 1-22); 11 mismatch row(s).**

#### Chapter 2 — 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Chinese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-6 | MISMATCH | བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག (bgegs rnams med cing so sor 'joms 'gyur cig) | His text reads *'joms 'gyur* (no *cig*). "Because the recitation has no hindrance, obstacles are absent; the things to be abandoned are each overcome by **their own antidote**". A statement of result | "願諸障礙皆無，並一一被摧毀。" ("**may** all obstacles be absent, and each one be destroyed"). Optative | **Translator decision** (optative, following our root's *cig*; translator note in the file). Leave. "一一" ("each one") keeps *so sor* |

Readings that **support** the current Chinese:
- 2-1: devotion to *lha mo* with body, speech and mind. "若有智者對此天女具足虔敬" ("if a wise person has devotion to this goddess") fits. He does not identify *lha mo*, so "天女" ("goddess") is not contradicted here; the reviewer question on 天女 in the file stands. *blo ldan* → "智者" ("a wise person").
- 2-2 *srod dang tho rangs*: dusk and dawn, each with its own practice (the wrathful form at dusk, the peaceful form at dawn) → "於黃昏與黎明" ("at dusk and at dawn") fits. *dran pas mi 'jigs*: "by merely recollecting **the deity's body** fearlessness is given". "憶念她，即得賜予一切無畏" ("by recollecting **her**, one is at once granted every fearlessness") names the deity as the object, so the Hindi row does not recur; 即 ("at once") carries some of his "merely". *sdig pa thams cad* pacified by mere recollection → "一切罪障都將徹底平息" ("all misdeeds will be thoroughly pacified"). *ngan 'gro* = "the result of the lower realms is pacified" → "一切惡趣都將被摧毀" ("all lower realms will be destroyed").
- 2-3: *bye ba phrag bdun* = seventy million, and "七千萬尊佛" ("seventy million buddhas") is exact. The empowerment is conferred on the reciter → "將迅速為此人授予灌頂" ("will swiftly confer empowerment on this person"). *sangs rgyas go 'phang mthar thug* → "那究竟的佛果" ("that ultimate buddhahood").
- 2-4: stationary and moving poisons (aconite-type plant poisons; snakes and scorpions), eaten or drunk → "無論是靜止的毒還是移動的毒，／即使是已經吃下或喝下的" ("whether stationary poison or moving poison, even what has been eaten or drunk") fits, with no "accidentally". He says the poisons are dispelled by recollecting "the praise, the deity and the mantra"; "憶念她" ("recollecting her") names one of the three, which is fine.
- 2-5: *gdon, rims, dug* "comprising cause and effect", removed by the power of Tārā's vidyā-mantra → "受邪魅、傳染病、毒物所苦" ("tormented by malevolent spirits, infectious diseases, poisons") in the root order. *sdug bsngal tshogs* → "一切苦難" ("all hardships"). *sems can gzhan pa rnams la yang ngo* = "just as for myself, one can benefit other beings too" → "其他眾生也同樣如此" ("it is the same for other beings too").
- 2-6: *gnyis gsum bdun* → "二、三、七遍" ("two, three or seven times"). Sons and wealth match. *'dod pa thams cad* = "all supreme and common siddhis are accomplished" → "一切所願皆能圓滿" ("all wishes can be fulfilled").

Style notes (not errors):
- 2-3 "比這更殊勝的成就" ("attainments greater than this"): he glosses *'di las che ba* as "not only this life, but more". 成就 ("attainment, siddhi") is supplied by the Chinese (the QA log flagged it for this check). It narrows "greatness" a little but is not contradicted, and it matches Gendun Drub's "the common great siddhis" in the word list. Leave.
- 2-4 "靜止的毒…移動的毒" ("stationary poison … moving poison") is literal. He means plant poisons and the venom of snakes and scorpions. A general reader may not see this. If the reviewer wants it plain: "無論是植物之毒還是蛇蠍之毒" ("whether plant poisons or the venom of snakes and scorpions"); that is interpretation, so optional.
- 2-6 "一一" ("one by one, each") is close to his "each by its own antidote". Fine.

**Result: 5/6 clean, 0 verse(s) with errors, 1 with mismatches only (2-6); 1 mismatch row(s).**

#### Colophon — a-1

Drakpa Gyaltsen quotes the colophon in a variant (see Textual notes) and gives no gloss. The Chinese "正等覺佛所宣說之世尊度母讚頌，至此圓滿。" ("The praise of the Blessed Tārā spoken by the Perfectly Complete Buddha is here complete.") follows our root. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

### Textual notes (variants between Drakpa Gyaltsen's quotation and our root; not errors — the Chinese follows our root)

Word-level differences (`find_textual_variants.py`):
- **1-8** *'jigs pa chen **mos*** (instrumental, "by the great terror") for our *chen mo*. This supports his reading of Ture as the mantra.
- **1-12** *zla ba'i **dum bus*** ("with a moon-piece") for our *zla ba'i **rtse mos*** ("with the moon's tip"). The referent is the same; "月牙" ("crescent moon") fits both.
- **1-16** *rig pa hūṃ las **sgrol ma*** ("liberator") for our ***sgron ma*** ("lamp"). The Chinese "明燈" ("lamp") follows our root.
- **1-20** *rims **nad*** ("epidemic disease") for our *rims **ni***. The meaning is unchanged.
- **2-1** *rab **dang** brjod* for our *rab **tu** brjod*. Possibly "with clear faith"; "以至誠之心" ("with utmost sincerity") fits either.
- **2-6** *'joms 'gyur* without *cig*: he reads the line as a statement of result, where our root is optative. See the 2-6 row.
- **a-1**: his colophon names the speaker as *yang dag par rdzogs pa'i sangs rgyas **rnam par snang mdzad chen pos*** ("the perfectly complete Buddha, the great Vairocana"). Our root has only *yang dag par rdzogs pa'i sangs rgyas kyis*. He then adds a translator's colophon: "transmitted from ācārya Nāgārjuna, translated by Nyen Lotsāwa".

Spelling and particles only:
- 1-1 *bye ba* / *phye ba*
- 1-4 *rgyal ba* / *rgyal bar*, *brten* / *bsten*
- 1-10 *dga' bar*, *phreng bas*
- 1-11 *nus pa* / *nus ma*
- 1-13 *mtha' ma* / *tha ma*
- 1-17 *man dhā ra*, *gsum po* / *gsum rnams*
- 1-18 *ri dwags* / *ri dgas*
- 1-19 *lta dang* (a scribal slip for *lha dang*)
- 1-22 *kyi* / *kyis*
- 2-2 *byas te* / *byas nas*
- 2-4 *gtan gnas* / *brtan gnas*, *'thungs ba*
- 2-5 *spangs te* / *spong ste*
- 2-6 *'dod pa ni* / *'dod pas ni*

### Second pass — kāya / named entity / number sweep

Nothing added beyond the rows above.
- **Named entities.** Avalokiteśvara (1-1, "三世界怙主", "Protector of the Three Worlds", unnamed as in the root), Indra ("帝釋"), Agni ("火神"), Brahmā ("梵天"), Vāyu ("風神"), gandharva ("乾闥婆"), yakṣa ("夜叉") (1-6), Amitābha ("阿彌陀佛", 1-12), Meru and Mandara ("須彌山、曼陀羅山", 1-17) and kinnara ("緊那羅", 1-19) all match. The bodhisattvas at 1-4 are named ("諸菩薩"). Maheśvara (1-6) and Vindhya (1-17) are already rows.
- **Numbers.** A hundred moons (1-2), seven worlds (1-5), one wheel (1-9), ten syllables (1-16), seventy million (2-3, "七千萬") and 2/3/7 recitations (2-6) all match. "Twice" (1-20) is already a row. At 1-14 the number of hands is left open, as in the root. At 1-19 "天眾之王" ("the king(s) of the god-hosts") is unmarked for number and sits in the agent position, so it does not make Tārā the king.
- **Kāya.** At 1-15 he says she destroys the afflictions "by her nature as dharmakāya", and at 1-17 she is generated as the wrathful body. Neither is rendered or required, and no *sku* is collapsed into "dharma" or "mind". At 1-21 the Chinese adds 身上 ("on the body") where he names body, speech and mind; that is the 1-21 row.
- **Agent / scope.** 1-19 (who serves whom), 1-10 (the joy she gives), 2-2 (the object of recollection is the deity) were confirmed on this pass. 1-11 ("all" moved from the beings to the poverty) is a row.

**Overall: 30 verses checked — 20 clean, 0 with errors, 10 with mismatches only.**
