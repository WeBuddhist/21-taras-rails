## Praise to the Twenty-One Taras — Commentary Fact-Check (Chinese)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-རྒྱལ་བ་དགེ་འདུན་གྲུབ།.md` — Gyalwa Gendun Drub (1st Dalai Lama, 1391–1474), commentary id `gendun-drub`
- **Translation audited:** `3-TRANSFORMATIONS/Translations/zh-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general.md` (Chinese, Traditional characters, general grade, draft 4)
- **Date:** 2026-09-24

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. For every verse
each word or phrase Gendun Drub glosses was aligned with the Chinese
(Tibetan | gloss | Chinese | MATCH/MISMATCH) before a verdict was given; only the
ERROR and MISMATCH rows are printed below. ⚠ ERROR = the Chinese names the wrong
thing (wrong referent, agent or grammatical role reversed, wrong number or scope, or
an added word that changes the meaning). MISMATCH = differs from Gendun Drub's reading,
but the right rendering is a translator's call. Where the Chinese follows a translator
decision already settled for the English (1-3 colours to the lotus; 1-8 Ture as her
name and "champions of Mara"; 1-14 "seven levels"; 1-17 Vindhya; 1-22 "and"; 2-6
optative), or a fix from the English consensus (1-1 lotus from the Lord's face; 1-9
"wheel of all directions"), the row says so. Locked words from the Chinese word list
(`0-INBOX/AI_translation/keyword-extraction-dharmamitra/zh/termbase-zh-general.md`) are
kept in every suggested fix. A second pass looked only for doctrinal-category swaps,
named entities and numbers. Chinese is glossed in English in parentheses.
Preliminary self-check, not a scholarly sign-off — a domain specialist and a native
Chinese reader must review it before it is treated as final (an LLM never marks its own
output complete).

Extraction notes: 29 buckets (I-3, 1-1 to 1-22, 2-1 to 2-6), none empty, no cascading
shift (`extract_commentary.py --strict`). Each bucket opens with Gendun Drub's outline
heading, quotes the root line or lines, then glosses them; he also gives each homage its
Tārā name (e.g. 1-1 "Tārā the greatly heroic", citing Paṇchen Nyima Bepa). Two boundary
effects, neither a shift: (1) the 2-3 bucket runs on into the first two lines of 2-4
(*de yi dug ni drag po chen po* = the wrong view that obstructs buddhahood; *brtan gnas*
= the "stationary poisons" of ignorance and hatred towards the Dharma), so 2-4 was
audited from both buckets; (2) the 2-6 bucket holds three readings of "two, three,
seven" (certain poets; Pang Lotsawa; Butön). The literal first reading was used as
ground truth. Not covered: I-1, I-2, a-1 and the section headings (e.g. 1-0 *讚頌正文*,
"the praise itself"), which Gendun Drub does not gloss; his own colophon sits under his
own heading, not under a root marker. Scope: 29 verses. The Chinese file was read as
whole blocks (transclusion layout, full four-line verses). Where it helps, the classical
Chinese canon version (CBETA T1108B, in
`0-INBOX/AI_translation/keyword-extraction-dharmamitra/zh/references/zh-classical-T1108B.md`)
is cited as context only, never as ground truth.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6 (29 verses) |

#### Chapter I — I-3

Glosses *oṃ* (going for refuge, offering, purifying), *rje* (supreme among the mothers
of all buddhas), *btsun* (holding the prātimokṣa, bodhisattva and mantra vows),
*'phags ma* (far from non-virtue, beyond saṃsāra and nirvāṇa), *sgrol ma* (she who
frees from the ocean of suffering), *phyag 'tshal* (sweeping away karma and
affliction; body, speech and mind in respect). "嗡，敬禮至尊聖度母。" (Om, homage to the
venerable noble Tārā) — every term matches. *至尊* (venerable, supreme) carries *rje btsun*
and *聖* (noble) carries *'phags ma*; both are locked. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Chinese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-1 | MISMATCH | འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི (’jig rten gsum mgon chu skyes zhal gyi) | Avalokiteśvara, protector of the three realms, wept; "from the utpala born of the water of his tears, from the opening stamens of the utpala's face (*ut pa la'i zhal*), she was born". The face is the lotus's (its open blossom); the lotus grows from his tears | "三世界怙主面容所生蓮花，／從其花蕊綻放之中化現者" (the lotus born from the face of the Protector of the three worlds, / she who appeared from its opening stamens) | Translator's call. The line follows the English consensus fix ("the lotus / That arose from the face of the Lord"), which the root allows. If following Gendun Drub: "三世界怙主淚水所生蓮花" (the lotus born from the tears of the Protector of the three worlds), though "tears" is not in the root. Leave |
| 1-2 | MISMATCH | སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། རབ་ཏུ་ཕྱེ་བའི་འོད (skar ma stong phrag tshogs pa rnams kyis rab tu phye ba'i 'od) | Comparative: from her face "light that spreads out even more than (*bas kyang*) **thousands** of gathered stars". He reads the hundred moons the same way (*brtsegs pa bas*: brighter even than a hundred heaped) | "她以千顆星辰匯聚／所放射的光芒，極其熾燃" (she blazes intensely with the light radiated by **a thousand** gathered stars) | Translator's call. The Chinese (like the English) gives her the stars' light; Gendun Drub makes her light outshine the stars. The root's *kyis* allows both. The classical Chinese canon reads it Gendun Drub's way too (如千星宿俱時聚，殊勝威光超於彼, "like a thousand stars gathered at once, her supreme light surpasses them"). Also *stong phrag* is "thousands", not exactly "a thousand" (千顆). E.g. "她的光芒勝過成千星辰的匯聚，／向四周放射，極其熾燃" (her light surpasses the gathering of thousands of stars, / spreading all around, blazing intensely). Keeps locked 光 and 熾燃. The moon line "猶如" (like) can stay |
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo; GD's text *ser sngo*) | "*sngo* is her body colour; *ser* shows the clarity of the colour — hence 'Tārā of golden colour'". The lotus is an utpala held at her heart by the left ring finger | "手中以金藍色／水生蓮花為莊嚴者" (whose hand is adorned with a golden-blue water-born lotus) | Translator decision (English settled: colours to the lotus). Gendun Drub gives the colours to her body, not the lotus. Leave |
| 1-4 | MISMATCH | མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད (mtha' yas rnam par rgyal bar spyod) | "She acts in complete victory over the limitless (*mtha' yas pa las*) misfortunes of this life, afflictive obscurations and cognitive obscurations" — *mtha' yas* is what she conquers | "以無邊的全然勝利而行持" (who acts with limitless, complete victory) | Translator's call. "Limitless" is attached to her victory; Gendun Drub attaches it to what she defeats. The English has the same wording as the Chinese. E.g. "全然戰勝無邊障礙而行持" (who acts in complete victory over limitless obstacles); "障礙" (obstacles) is Gendun Drub's, not the root's |
| 1-9 | MISMATCH | རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག (rang gi 'od kyi tshogs rnams 'khrug) | "By the light of the wheel, her own emblem, other masses of light are stirred (*'khrug pa*), that is, outshone (*zil gyis gnon*)" | "自身的光聚翻騰湧動者" (whose own mass of light churns and surges) | Translator's call. In the Chinese her own light is what churns (no object); in the commentary her light is the instrument and **other** light is what is overwhelmed. E.g. "以自身的光聚壓過其他一切光芒者" (who, with her own mass of light, overpowers all other light). Keeps locked 光 |
| 1-9 | MISMATCH | མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས་བརྒྱན་པའི (ma lus phyogs kyi 'khor los brgyan pa'i) | "the right hand, making the supreme giving **to all directions** without exception, its palm adorned with a wheel" — "all directions" goes with the giving gesture, not the wheel | "手掌以無餘十方之輪為飾" (whose palm is adorned with the wheel of the ten directions without exception) | Leave. What-modifies-what differs, but the Chinese follows the root's word order and the English consensus fix (one wheel, "of all directions"). The single wheel is right. *十方* ("ten directions") is the normal Chinese for "all directions" |
| 1-12 | MISMATCH | འོད་དཔག་མེད་ལས། རྟག་པར་ཤིན་ཏུ་འོད་ནི་མཛད་མ ('od dpag med las / rtag par shin tu 'od ni mdzad ma) | "Amitābha dwells amid the hair at her crown; for beings' sake, at all times, she (*mdzad ma*) makes much light spread" — Tārā is the one who emits the light | "從她髮髻中的阿彌陀佛／恆常放出極其燦爛的光芒" (from the Amitābha in her hair-knot, extremely brilliant light is constantly sent out) | Agent: the Chinese has no stated subject, and most readers will take Amitābha as the one sending out light. The commentary makes her (*mdzad ma*, "she who does") the one who spreads it. The settled English makes Amitābha the agent, so this is a translator's call. Smallest fix, moving one character: "她從髮髻中的阿彌陀佛／恆常放出極其燦爛的光芒" (she, from the Amitābha in her hair-knot, constantly sends out extremely brilliant light) |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | "With the HŪṂ at her heart she destroys (*'gems*), that is, dries up (*skems*), the ocean of existence of the seven levels of the world" — what is destroyed is their saṃsāric existence, not the levels | "以吽字／摧毀七層者" (who, with the syllable HŪṂ, destroys the seven levels) | Translator decision ("seven levels" is settled, with a translator note, and this commentary supports it: seven world-levels). The object differs: Gendun Drub has her drying up the ocean of existence of the seven levels, not the levels themselves. The literal "destroy" is defensible. Leave |
| 1-18 | MISMATCH | རི་དགས་རྟགས་ཅན (ri dags rtags can) | "the moon disc, like a celestial lake, marked with a **hare** (*ri bong gi rtags can*)"; holding it signals the removal of stationary poison, the torment of the afflictions | "帶有鹿紋的月亮" (the moon bearing **deer** markings) | Worth changing. *ri dags* is Skt. *mṛga* (deer, wild animal), so "deer" is literal, but Gendun Drub names the hare. Unlike Hindi (हरिणांक, "deer-marked moon"), Chinese has no deer-moon image: readers know the moon hare (玉兔). "鹿紋的月亮" reads oddly. E.g. "帶有兔紋的月亮" (the moon bearing hare markings). The lock is only 月 (moon), so this keeps it; the word-list note "deer-marked one" would need updating. The classical canon avoids the choice (神獸像, "the image of a divine animal") |

Readings that **support** the current Chinese:
- 1-1: *myur ma* = swift to benefit beings, *dpa' mo* = heroic in turning back the battle of saṃsāra → "迅捷勇猛者" (the swift and heroic one). "雙目猶如剎那閃電光" (whose two eyes are like an instant's lightning flash) matches "her two eyes, like lightning that flashes in an instant, look on the three worlds". *'jig rten gsum mgon* = protector of the three realms, Avalokiteśvara → "三世界怙主" (Protector of the three worlds); *三世界* keeps it apart from *三界* (desire, form, formless realms) as the word list intends. Her birth from the opening stamens, "從其花蕊綻放之中化現" (appeared from its opening stamens), matches.
- 1-2: *kun du gang ba* = the fully full autumn moon, not yet waning → "一百輪秋季滿月" (a hundred full autumn moons). *brtsegs pa* → "層層相疊" (heaped layer on layer).
- 1-3: *dka' thub* = "that is, ethical discipline" → "持戒" (keeping discipline) is right. *spyod yul* = "the perfection of wisdom" → "智慧" (wisdom) is named, as the English consensus asked. The list keeps the root's order: 布施、精進、持戒、寂靜、忍辱、禪定與智慧 (generosity, diligence, discipline, peace, patience, concentration and wisdom). *chu nas skyes kyi padma* → "水生蓮花" (water-born lotus) adorning her hand.
- 1-4: she is carried like the crown uṣṇīṣa, as mother of all tathāgatas → "如來頂髻者" (she who is the uṣṇīṣa of the Tathāgatas). *rgyal ba'i sras* = "the Victors' children, the bodhisattvas, who have attained the ten perfections" → "已證一切無餘波羅蜜的諸菩薩" (the bodhisattvas who have attained all the perfections without exception) names them exactly as he does, and the bodhisattvas, not Tārā, are the ones who attained the perfections.
- 1-5: *'dod / phyogs / nam mkha'* = desire, form, formless realms → "欲界、色界與無色界" is exactly his reading. "七個世界" (seven worlds) matches his count: three lower realms, desire-realm gods and humans, form and formless. *'gugs par nus* → "能將一切無餘召集而來" (able to summon all without exception).
- 1-6: the order Indra, Agni, Brahmā, Vāyu is kept → "帝釋、火神、梵天、風神". *sna tshogs dbang phyug* is plural ("the chiefs") → "諸自在天" (the various Īśvara gods). *'byung po* (chief Gaṇapati) = "鬼神" (spirits). *ro langs* (chief Maheśvara) = "起屍" (risen corpses). *dri za* (chief Pañcaśikha) = "乾闥婆" (gandharvas). *gnod sbyin* (chief Vaiśravaṇa) = "夜叉眾" (hosts of yakṣas). *mdun nas bstod* = "都在她面前讚頌" (all praise her in her presence).
- 1-7: *pha rol 'khrul 'khor* = the sorcery (*mthu*) and effigy devices (*byad ma*) of others → "敵方咒術幻輪" (the adversaries' sorcery and magic wheels) fits closely. The legs, right drawn in (emptiness) and left extended (compassion), match "右屈左伸以足踏" (trampling with right drawn in and left extended).
- 1-8: *tu re* = "Tārā" → "敬禮都咧" (homage to Ture — her name). *'jigs pa chen mo* = "the wrathful one" → "令人大怖畏者" (she who causes great terror) makes her the one who terrifies, as the consensus fix asked. *bdud kyi dpa' bo* = the afflictions, and with them the four māras → the literal "魔的勇士" (Māra's champions) stands. *dgra bo* = the two obscurations, so "一切怨敵" (all enemies) stands. Her own face → "蓮花面容" (lotus face), the 1-8 lock.
- 1-9: left hand, with thumb and ring finger holding the utpala and three fingers extended at the heart, is the Three Jewels mudrā → "以三寶手印之指，莊嚴於心間" (with the fingers of the Three Jewels mudrā, adorning the heart). **One** wheel on the palm → "之輪" (the wheel), singular.
- 1-10: the joy is that of "disciples with faith, whose wishes she fulfils" → "賜予極喜者" (she who grants supreme joy). The splendour belongs to her head ornament, interwoven with garlands of light → "其威嚴頭冠散發光鬘" (her majestic crown sends out garlands of light). *bdud dang 'jig rten* → "魔與世間" (Māra and the world): no added "all" (the Hindi had to drop one); "皆" here means "both". *dbang du mdzad* → "攝伏" (bring under her control), locked.
- 1-11: *sa gzhi skyong ba* = the ten direction-guardians with their retinues → "守護大地的神眾" (the hosts of deities guarding the earth). *'phongs pa* = the destitute and those tormented by suffering → "使人從一切貧困中解脫" (frees people from all poverty).
- 1-12: *zla ba'i rtse mo* = the first-day (crescent) moon → "月牙" (crescent moon). All her ornaments blaze → "所有飾物都極其熾燃". Amitābha amid the hair at her crown → "她髮髻中的阿彌陀佛" (the Amitābha in her hair-knot) — his *ral pa'i khur* / our root *ral pa'i khrod*. *rtag par* → "恆常" (constantly).
- 1-13: right leg extended, left bent → "右伸左屈". The fire at the end of the eon is the blaze of wisdom-fire → "如劫末之火般熾燃的火鬘中央" (amid a garland of fire blazing like the fire at the eon's end). *dgra yi dpung* = the afflictions of disciples → "敵人的軍隊" (the armies of enemies), literal and fine.
- 1-14: *rim pa bdun* = "the seven levels of the world" → "七層" (seven levels), the translator decision, is supported by this commentary.
- 1-15: *bde ma* = undefiled bliss, *dge ma* = free of afflictions, *zhi ma* = suffering pacified, nirvāṇa as her sphere → "安樂、善妙、寂靜者，以涅槃寂靜為行境" (the blissful, virtuous, peaceful one, whose sphere is the peace of nirvāṇa). The ten-syllable mantra has OṂ first and SVĀHĀ last, so "嗡梭哈" (OṂ SVĀHĀ) gives his order, not the root's word order; this is fine. *sdig pa chen po* → "大罪障" (great sins and obscurations).
- 1-16: *yi ge bcu pa'i ngag* = oṃ tāre tuttāre ture svāhā → "十字咒語" (the ten-syllable mantra). *rig pa hūṃ* = the wrathful knowledge-mantra (oṃ nama tāre namo hare hūṃ hara svāhā) → "明咒" (knowledge-mantra, vidyā): not "awareness". *dgra* = the enemies of liberation → "敵人之身" (the enemies' bodies).
- 1-17: Ture is Tārā herself stamping ("the feet of Ture, arisen from the seed in the form of HŪṂ") → "敬禮都咧頓足者" (homage to Ture, who stamps her feet). *'bigs byed* is listed as a mountain with Meru and Mandara → "頻闍山" (Mount Vindhya). She is the one who shakes them → "令須彌山、曼陀羅山、頻闍山與三世界皆震動" (she makes Meru, Mandara, Vindhya and the three worlds all tremble). The agent is right.
- 1-18: the moon is the thing that is lake-like → "形如天湖、帶有…的月亮" (the moon shaped like a celestial lake) attaches the simile to the moon, as he does. TĀRA twice and PHAṬ remove the moving poisons → "念誦兩遍達咧，並以呸字消除所有毒物" (reciting TĀRA twice, and with PHAṬ, removes all poisons).
- 1-19: the kings of the hosts of gods are Indra (desire realm) and Mahābrahmā (form realm), and Druma is king of the kinnaras. They **serve** her → "天眾之王所侍奉，諸天與緊那羅所依止者" (served by the kings of the god-hosts, relied on by gods and kinnaras). Order "爭鬥與惡夢" (strife and bad dreams) matches the root.
- 1-20: right eye sun-like (wrathful), left eye moon-like (peaceful) → "雙目如圓滿日月" (two eyes like the full sun and moon). HARA twice is the wrathful mantra and TUTTĀRA the peaceful one → "念誦兩遍喝囉，並以都達咧" matches. *rims* = infectious disease → "傳染病" (infectious diseases).
- 1-21: *de nyid gsum* = the suchnesses of body, speech and mind: OṂ at the crown, ĀḤ at the throat, HŪṂ at the heart, set on her → "身上安立三真如" (the three suchnesses set on her body): the consensus fix. *zhi ba'i mthu* → "寂靜威力" (the might of peace), locked. The supreme destroyer is Ture Tārā herself → "摧毀它們的最勝都咧" (the supreme Ture who destroys them).
- 1-22: "these twenty-one praises with the root mantra of the peaceful and wrathful ones, **and** the homages with respectful three doors — twenty-one" → two items joined by "以及" (and). The translator decision is supported.

Textual notes (commentary's text vs our root — not errors; the Chinese follows our root):
- 1-3 *ser sngo* for *gser sngo*. He still reads it as golden colour ("gser mdog can gyi sgrol ma"), so the sense is unchanged.
- 1-12 *ral pa'i khur na* for *ral pa'i khrod na* ("in the mass of her locks" / "amid her locks").
- 1-13 *mtha' ma'i* for *tha ma'i* (spelling).
- 1-16 *sgrol ma* ("liberator") for *sgron ma* ("lamp"). "明燈" (bright lamp) follows our root.
- 1-10: the laughter line is not quoted, and the gloss reads *tA ra* (TĀRA) where the root has *tu ttwa ra*.
- 1-18 *ri dwags* for *ri dags* (spelling).
- 1-19 *tshogs rgyal po* for *tshogs rnams rgyal po* (drops the plural marker; same sense).
- 1-20 *rims nad* for *rims ni* (adds "disease").
- 1-21 *yang ldan* for *yang dag ldan* (drops *dag*; same sense).
- 2-2 adds *mal nas* ("from bed") to "rising".
- 2-5 *spo* for *spong*.
- 2-6: Pang Lotsawa's paraphrase *'joms par 'gyur* ("will destroy") for our root's optative *'joms 'gyur cig*.

Style notes (not errors):
- 1-3 "…為其行境者" (… which are her sphere of activity): the Chinese makes the whole list her field of practice. Gendun Drub reads the perfections as the cause she arose from (*de'i rgyu las byung*), and *zhi ba* as the pacifying of their opposites (miserliness, laziness …), not as a seventh item. Harmless.
- 1-4: "一切無餘波羅蜜" (all the perfections without exception) doubles *ma lus*; *無餘* alone carries the lock. "極力依止" (rely on with all their strength) for *shin tu bsten*, which he glosses as reverent service "with the crown of the head" (*shin tu gus pa'i gtsug gis*). "恭敬依止" (rely on with reverence) or "深深依止" (deeply rely on) would be closer.
- 1-6: "…風神與諸自在天所供養" makes the Īśvaras a fifth item. Gendun Drub uses *sna tshogs dbang phyug* to sum up Indra, Agni, Brahmā and Vāyu as "the chiefs". Harmless, and the English and Hindi read it the same way.
- 1-11: "以顫動的忿怒顰眉和吽字" (with the quivering wrathful frown **and** the syllable HŪṂ) makes two instruments. The root has one: "the HŪṂ of the moving frown", and he makes the light of the HŪṂ at her heart the thing that frees. "以忿怒顰眉顫動時的吽字" (with the HŪṂ of her quivering wrathful frown) would be closer. Minor.
- 1-13 and 1-16 *kun nas bskor (rab) dga'*: he reads "disciples with faith who delight in turning the Dharma wheel", and the enemies are theirs (afflictions; self-grasping). "為喜悅所環繞" / "周遭環繞極喜者" (surrounded by joy / surrounded all round by supreme joy) is the settled literal reading.
- 1-14: his paraphrase has "the sole of her right foot strikes the ground" and her hand in the threatening mudrā. The root says *phyag gi mthil* (palm of the hand). The Chinese follows the root ("以手掌拍擊大地", strikes the earth with the palms of her hands). No change.
- 1-16: "明咒吽字" (the knowledge-mantra, the syllable HŪṂ) — he treats *rig pa hūṃ* as a whole mantra, so "吽明咒" (the HŪṂ knowledge-mantra) would be a shade closer than naming a single 字 (syllable). Also, "十字咒語" is the locked form, but *十字* alone can also mean "cross"; a native reader should confirm "布列十字咒語" (arranges the ten-syllable mantra) cannot be misread.
- 1-17: "她即是吽字形相的種子字" (she is herself the seed-syllable in the form of HŪṂ) follows the root's *sa bon nyid ma* literally. He reads Ture's feet as "arisen from" that seed. Harmless.
- 1-17: "與三世界" (and the three worlds) makes the mountains and the three worlds two objects. He treats the mountains as examples within the three worlds (*la sogs pa*). Harmless.
- 1-18: "所有毒物，無一遺漏" (all poisons, none left out) says "all" twice for *dug rnams ma lus par*. Harmless.
- 1-19: "爭鬥" (strife, fighting) for *rtsod*; he glosses it as the disputes of opponents (*pha rol po'i rtsod pa*). "爭訟" or "爭論" (disputes) would be closer. He reads the "armour of joy" as the peaceful and wrathful mantras held with a joyful, one-pointed mind; "周遍喜樂鎧甲的威嚴" (the majesty of the all-covering armour of joy) is the literal reading.

**Result: 14/22 clean, 0 verse(s) with errors, 8 with mismatches only (1-1, 1-2, 1-3, 1-4, 1-9, 1-12, 1-14, 1-18); 9 mismatch row(s).**

#### Chapter 2 — verses 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Chinese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-1 | MISMATCH | ལྷ་མོ (lha mo) | "the goddess Tārā" (*lha mo sgrol ma*) — the goddess is Tārā herself | "對此天女具足虔敬" (endowed with devotion to this celestial maiden / goddess) | Locked word, already flagged for the reviewer. In Chinese *天女* often means a celestial maiden (apsaras) of lower rank, which the commentary rules out. Two options: keep the lock and add her name as he does, "對天女度母具足虔敬" (endowed with devotion to the goddess Tārā); or change the lock to "聖尊" (holy one) or "女尊" (female deity). The native reader decides |
| 2-4 | MISMATCH | དེ་ཡི་དུག་ནི་དྲག་པོ་ཆེན་པོ། བརྟན་གནས་པ (de yi dug ni drag po chen po / brtan gnas pa) | (in the 2-3 bucket) "the poison that obstructs **that** buddhahood — the great fierce one — is wrong view"; the "stationary" poisons are denigrating the Dharma through ignorance and hating the Dharma and its teachers. Only then come moving poisons (rabid dogs, snakes) and food-and-drink poisons | "其毒極其猛烈，／無論是靜止的毒還是移動的毒" (its poison is extremely fierce, / whether the poison is stationary or moving) | Translator's call. Gendun Drub reads *de yi* as referring back to buddhahood, and the first two lines as spiritual poisons. The Chinese, like the English, reads all of them as physical poisons, and the root allows this. *其* (its) does render *de yi*. Leave. (Style: "其毒極其猛烈" can read as a full sentence about someone's poison; "即使是極其猛烈的毒，" (even extremely fierce poison) would fold it into the list, if the reviewer wants) |
| 2-6 | MISMATCH | བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག (bgegs rnams med cing so sor 'joms 'gyur cig) | Pang Lotsawa, cited: "obstacles cannot hinder it; there are no obstructors, and each antidote destroys (*'joms par 'gyur*) each thing to be abandoned" — indicative | "願諸障礙皆無，並一一被摧毀" (**may** all obstacles be absent, and be destroyed one by one) | Translator decision (settled: optative, following our root's *'gyur cig*, with a translator note in the file). Gendun Drub's source reads it as a statement. *so sor* ("each individually") is kept as "一一" (one by one). Leave |

Readings that **support** the current Chinese:
- 2-1: *gus pa yang dag ldan* = endowed with genuine respect, not lip service → "具足虔敬" (endowed with devotion), with the sincerity carried by "至誠之心" (a most sincere heart). *blo ldan* = one with a one-pointed, wise mind → "智者" (the wise one). *rab tu brjod* = recites "with great faith" (*rab tu dad pas*) → "以至誠之心念誦" (recites with a most sincere heart) is close.
- 2-2: rising "from bed" at dusk **and** dawn → "於黃昏與黎明起身後" (after rising at dusk and dawn) — both sessions, joined by "與" (and). "by **merely** recollecting (*dran pa tsam gyis*)" her body, mantra and praise → "憶念她" (recollecting her), with no added "always". The giver is kept: "即得賜予一切無畏" (one is then granted all fearlessness), for *rab ster* ("grants"). *sdig pa* = the causes of lower rebirth → "一切罪障" (all sins and obscurations). *ngan 'gro* = the lower realms as result → "一切惡趣" (all lower realms).
- 2-3: *bye ba phrag bdun* → "七千萬" (seventy million = seven koṭis) is the right number. *rgyal ba* → "佛" (Buddhas). The recipient is the practitioner, in this very life → "將迅速為此人授予灌頂" (will swiftly confer empowerment on this person). *'di las che ba* = the common great siddhis → "比這更殊勝的成就" (attainments even more excellent than this): *成就* (siddhi) is his word. The supreme siddhi, final buddhahood → "並抵達那究竟的佛果" (and reach that ultimate fruit of buddhahood).
- 2-4: moving poisons = rabid dogs and snakes → "移動的毒" (moving poison). Eaten and drunk = food and drink poisons → "即使是已經吃下或喝下的" (even what has already been eaten or drunk). "by **merely** recollecting the goddess's body etc." → "憶念她，也能將其徹底消除" (by recollecting her, it can be completely removed); "她" (her) matches his *lha mo'i sku sogs dran pa*.
- 2-5: *gdon* → "邪魅" (harmful spirits), *rims* → "傳染病" (infectious diseases), *dug* → "毒物" (poisons), in the root's order. The line "其他眾生也同樣如此。" (and so it is for other beings too.) closes the sentence, matching his "the other-benefit … one obtains the benefits as above". It does not run into 2-6.
- 2-6: the numbers "二、三、七遍" (two, three, seven times) are kept as numbers, with no added "or", so all three of his readings fit. *mngon par brjod* → "誦持" (recite and uphold). The son → son and wealth → wealth lines match: "求子者即得子嗣，求財者即得財富" (who seeks a child gains a child, who seeks wealth gains wealth).

Style notes (not errors):
- 2-1: *yang dag* ("genuine") has no word of its own in "具足虔敬"; the next line's "至誠" (utmost sincerity) carries it. Fine.
- 2-5: "一切苦難皆得遠離" (all sufferings are left behind) renders *sdug bsngal tshogs* ("the mass of sufferings") as "all sufferings". Same scope. He reads the sufferings as those born from affliction by spirits, disease and poison; the Chinese keeps that link with "受…所苦" (suffering from …).

**Result: 3/6 clean, 0 verse(s) with errors, 3 with mismatches only (2-1, 2-4, 2-6); 3 mismatch row(s).**

#### Second pass — doctrinal-category swaps, named entities, numbers

- **Kāya / dharma / mind:** GD calls 1-15 the praise "by way of the dharmakāya" (the heading), but the verse's words (*bde ma … sdig pa chen po*) contain no *sku*. No kāya term appears in the Chinese, and none is collapsed. Nothing added.
- **Named entities:** Avalokiteśvara as "三世界怙主" (Protector of the three worlds, 1-1) fits. Indra, Agni, Brahmā, Vāyu (1-6) are all present and in the root's order. The bodhisattvas as "諸菩薩" (1-4) are named exactly as he names them. Amitābha (1-12) fits, but the agent differs (row above). Meru, Mandara, Vindhya (1-17) are right, and she is the one who shakes them. The kinnaras (1-19) fit. The deer for Gendun Drub's hare in 1-18 is the only animal divergence (row above). *天女* for *lha mo* (2-1) is a rank question for the locked word (row above).
- **Numbers:** hundred moons (1-2); a thousand stars for "thousands" (1-2, in the row above); seven worlds (1-5); ten directions for "all directions" (1-9, normal Chinese); ten-syllable (1-16); three worlds (1-17); twenty-one (1-22); seventy million (2-3); two, three, seven (2-6). No wrong number.
- **Scope words:** no added "all" at 1-10 (*皆* = "both"). *一切無餘* (1-4) and *所有…無一遺漏* (1-18) double "without exception" without changing scope. No added "always" at 2-2 or 2-4. Nothing further added.

**Overall: 29 verses checked — 18 clean, 0 with errors, 11 with mismatches only.**
