## Praise to the Twenty-One Taras — Commentary Fact-Check (Vietnamese)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md`, Jetsün Drakpa Gyaltsen (1147–1216), *sgrol ma phyag 'tshal nyi shu rtsa gcig gi bstod pa'i rnam bshad gsal ba'i 'od zer*. Commentary id `drakpa-gyaltsen`.
- **Translation audited:** `3-TRANSFORMATIONS/Translations/vi-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-vi-general.md` (Vietnamese, general grade, draft 3)
- **Root text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` (critical edition)

Method: a strict term-by-term alignment against this commentary's own glosses. It checks body (kāya), named entities, numbers, similes, agents and order. It is not a gist check. For each verse, every word Drakpa Gyaltsen glosses was aligned as Tibetan | gloss | Vietnamese | MATCH/MISMATCH before a verdict was given. Only the ⚠ ERROR and MISMATCH rows are shown below. Ground truth is the commentary's literal reading. Elaboration the verse need not carry was not flagged. The fact-checked English, the English consensus table and the Vietnamese word list were used as context only. Where the Vietnamese follows one of the seven settled English translator decisions, the row says so. Every Vietnamese phrase cited carries a one-line English gloss. This is a preliminary self-check, not a scholarly sign-off. A domain specialist and a native Vietnamese reader must review it before it is treated as final (an LLM never marks its own output complete).

Extraction notes: there are 30 transclusion markers (I-3, 1-1 to 1-22, 2-1 to 2-6, a-1), with no empty buckets and no shift. Each bucket quotes its root line(s) and then glosses them. Every bucket ends with an ID such as `^1-2`. These are the commentary file's own paragraph IDs, which run one ahead of the root IDs; they are not transclusion markers, and the attribution is correct. I-1 and I-2 are not covered. Before the verses, Drakpa Gyaltsen gives an outline (II-1 to II-3): the praise via the peaceful form, via the wrathful form and via activity, then the benefits in four parts. It is structural only. Some buckets quote without glossing:
- I-3 is quoted with no gloss.
- 1-16 only identifies the two mantras.
- 2-1 has a fragmentary gloss ("[with] body, speech and mind, to the goddess").
- a-1 quotes the root colophon (in a variant reading) and then adds the translator's colophon (Nyen Lotsāwa, in the lineage from Nāgārjuna) and the author's colophon.

The frontmatter says `covers_verses: 1-1–1-21`, but the file also quotes and glosses 1-22 and 2-1 to 2-6. Scope is therefore 30 verses.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6, a-1 (Vietnamese general, draft 3) |

#### Chapter I — I-3

Drakpa Gyaltsen quotes the homage (*oṃ rje btsun ma 'phags ma sgrol ma la phyag 'tshal lo*) with no gloss. The Vietnamese "Om! Kính lễ Chí Tôn Thánh Độ Mẫu!" ("Om! Homage to the Supremely Venerable Noble Tārā!") matches word for word. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Vietnamese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | "*gser sngo*: a colour bright like the lustre of refined gold". Glossed on its own, before and apart from *chu nas skyes* ("the hand-emblem, the lotus"). It is read as one gold hue, not gold + blue, and is not attached to the lotus | "đóa sen thủy sinh sắc vàng pha xanh" ("a water-born lotus coloured gold mixed with blue") | **Translator decision** (colours to the lotus, as in the English). Drakpa Gyaltsen gives a single gold colour that is probably hers. Leave, or note it |
| 1-4 | MISMATCH | རྒྱལ་བའི་སྲས (rgyal ba'i sras) | "the children of the Victors are all the bodhisattvas" | "Các Phật tử" ("the Buddha's children"). In everyday Vietnamese *Phật tử* means "Buddhist lay followers" | Name them unmistakably, e.g. "chư Bồ-tát" ("the bodhisattvas") or "các Phật tử Bồ-tát". Judgment |
| 1-6 | MISMATCH | སྣ་ཚོགས་དབང་ཕྱུག (sna tshogs dbang phyug) | "the great Maheśvara (*dbang phyug chen po*), who became the lord of them [Indra, Agni, Brahmā, Vāyu], offers worship at her feet". One being | "chư Tự Tại" ("the various Īśvaras", plural) | Single-commentary reading. The English consensus left the plural, because three other commentaries read it as plural. Leave; optional note |
| 1-8 | MISMATCH | ཏུ་རེ་འཇིགས་པ་ཆེན་མོ (tu re 'jigs pa chen mo) | His text reads *chen mos* (instrumental): "by the terror of TURE she dispels all māras; because she terrifies the māras she is the Great Terrifying One". Ture is the mantra | "Kính lễ Độ Mẫu Ture" ("Homage to Tārā Ture", with Ture as her name) | **Translator decision** (Ture as her name). Leave |
| 1-8 | MISMATCH | བདུད་ཀྱི་དཔའ་བོ (bdud kyi dpa' bo) | "the *dpa' bo* is the māra of the afflictions (*nyon mongs pa'i bdud*); by conquering it, the other three [māras] are destroyed in passing" | "các dũng tướng ma" ("Māra's champion generals") | **Translator decision** ("champions of Mara"). Leave |
| 1-11 | MISMATCH | ས་གཞི་སྐྱོང་བའི་ཚོགས (sa gzhi skyong ba'i tshogs) | "the ten direction-protectors (*phyogs skyong bcu*)", who obey her and act as her messengers | "chúng thần hộ địa" ("hosts of earth-guarding gods"). This can suggest the village earth-god (*Thổ Địa*) | e.g. "chúng thần hộ thế" ("the world-protector gods", lokapālas) or "chư thần hộ phương" ("the direction-protector gods"). Judgment |
| 1-11 | MISMATCH | ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ (phongs pa thams cad rnam par sgrol) | "all beings tormented by adverse conditions and destitute of favourable ones: she frees them from suffering and sets them in happiness". "All" goes with the *beings* she frees | "Giải thoát hoàn toàn khỏi mọi nghèo khó" ("completely liberates from all poverty"). The object is now a condition, narrowed to material poverty | e.g. "Cứu độ hết thảy chúng sinh khốn khó" ("rescues all beings in distress"). Judgment |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | First reading: rays from the vajra and HŪṂ "fill the abodes of the seven classes of beings (*'gro ba rigs bdun*) and clear all their obstacles". Alternative: "she scatters into pieces the nāgas, asuras and others dwelling in the seven underground levels" | "Phá vỡ tan tành cả bảy tầng" ("shatters to pieces all seven levels"). The levels themselves are shattered | **Translator decision** ("seven levels", left open). The verb "phá vỡ tan tành" fits only the alternative, and there the beings in the levels are scattered, not the levels. Leave, or soften the verb |
| 1-17 | MISMATCH | འབིགས་བྱེད ('bigs byed) | A verb: "Meru and Mandara (*ri rab man dā ra ba*, outside the trichiliocosm) are pierced by the light rays of the syllable HŪṂ". Possibly read as one mountain, "the Meru called Mandara" | "Núi Tu-di, Mạn-đà cùng núi Vindhya" ("Mount Meru, Mandara and Mount Vindhya") | **Translator decision** (Vindhya; already footnoted in the translation's notes). Leave |
| 1-18 | ⚠ ERROR | དུག་རྣམས་མ་ལུས་པར་ནི་སེལ (dug rnams ma lus par ni sel) | "with the mantra TĀRA she dispels the poisons both **stationary and moving** (*brtan pa dang g.yo ba'i dug*)", i.e. plant/mineral and animal | "Tiêu trừ toàn bộ không sót mọi nọc độc" ("eliminates every **venom** without exception"). *Nọc độc* is poison secreted by animals, so the stationary poisons are excluded and "without exception" is contradicted | "mọi chất độc" or "mọi độc tố" ("all poisons/toxins"; *độc tố* is already used at 2-4) |
| 1-18 | MISMATCH | ལྷ་ཡི་མཚོ་ཡི་རྣམ་པའི། རི་དྭགས་རྟགས་ཅན (lha yi mtsho yi rnam pa'i ri dwags rtags can) | "she holds in her hand the moon disc, **which is like a celestial lake**; *ri dwags rtags can* is the moon". The moon is the tenor | "tay cầm vầng trăng sáng, / Mang dấu ấn hươu như hồ nước chư thiên" ("holds the bright moon, / bearing a deer-mark like a lake of the gods"). The simile sits next to the deer-mark and can attach to it | Put the simile beside the moon, e.g. "Tay cầm vầng trăng như hồ nước chư thiên, / Mang dấu ấn hươu". Judgment |
| 1-20 | MISMATCH | ཧ་ར་གཉིས་བརྗོད (ha ra gnyis brjod) | "*ha ra gnyis brjod*: by the mantra-speech of **the two, peaceful and wrathful** (*zhi khro gnyis*), she dispels extremely fierce epidemics". *Gnyis* is read as the two mantras (*hara* from the wrathful, *tuttāre* from the peaceful), not as "twice" | "Tụng hai lần Hara cùng chữ Tuttare" ("reciting Hara twice with the syllable Tuttare") | "Twice" is the plain grammar and the English reading. Drakpa Gyaltsen alone reads "the two". Judgment; leave |
| 1-21 | MISMATCH | དེ་ཉིད་གསུམ་རྣམས་བཀོད་པ (de nyid gsum rnams bkod pa) | "OṂ ĀḤ HŪṂ, the three, set at her **body, speech and mind** (*sku gsung thugs*)" | "có ba chân như an lập nơi thân" ("the three suchnesses set upon the **body**"). In the triad *thân–khẩu–ý* (body–speech–mind), *thân* is only the first of the three places | e.g. "ba chân như an lập nơi thân, khẩu, ý" ("…at body, speech and mind"), or drop "nơi thân". Judgment |
| 1-22 | MISMATCH | རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག (rtsa ba'i sngags kyi bstod pa 'di dang / phyag 'tshal ba ni nyi shu rtsa gcig) | "this praise of the peaceful and wrathful ones is **this very praise** by the twenty-one homages". One praise, described two ways | "Đây là lời tán thán bằng căn bản chú, / Cùng với hai mươi mốt đoạn kệ kính lễ" ("This is the praise by the root mantra, / together with the twenty-one homage stanzas"). Two items | **Translator decision** ("and"). Leave |

Readings that **support** the current Vietnamese (several were problems in earlier drafts or in the English):
- 1-1 *chu skyes zhal gyi*: "from his [Avalokiteśvara's] tears arose a lotus or utpala; she was born from the opening lotus". The Vietnamese "Sen mọc từ gương mặt Hộ Chủ ba thế giới" ("a lotus grown from the face of the Lord of the Three Worlds") has a lotus arising from his face, not a face that is a lotus. That fits. *Sgrol ma* = liberates from saṃsāra's suffering, *myur ma* = swift for beings, *dpa' mo* = heroic in conquering the afflictions. "Độ Mẫu nhanh chóng, dũng mãnh" ("Tārā, swift and valiant") fits.
- 1-2: "a full moon heaped up many hundreds of times" fits "Trăm vầng trăng thu tròn đầy chồng lên nhau" ("a hundred full autumn moons stacked together"). "The two [moons and stars] are examples of countless radiating rays" supports treating the stars as a second simile ("Như ngàn vì tinh tú", "like a thousand stars").
- 1-3 *dka' thub* = *tshul khrims* (ethical discipline). "trì giới" ("upholding discipline") fits. *spyod yul nyid ma* = wisdom, and "trí tuệ" ("wisdom") is now named. Both were errors in the earlier English.
- 1-4 *de bzhin gshegs pa'i gtsug tor* = like the uṣṇīṣa of all tathāgatas. "đảnh kế Như Lai" ("uṣṇīṣa of the Tathāgata(s)") fits. *shin tu bsten* = "they carry her as their crown", and "hết lòng nương tựa" ("rely on her wholeheartedly") fits.
- 1-5 *'dod / phyogs / nam mkha'* = the desire, form and formless realms. "dục giới, sắc giới, vô sắc giới" is exact. *'jig rten bdun* = the five desire-realm destinies + the form realm + the formless realm, and "bảy thế giới" ("seven worlds") fits.
- 1-6: Indra ("Đế Thích"), Agni ("Hỏa thần"), Brahmā ("Phạm Thiên") and Vāyu ("Phong thần") all match. *'byung po* = Gaṇapati (*tshogs bdag*) and the like, so the generic "quỷ thần" ("spirits") fits. *ro langs* = "Maheśvara and the like", a class of beings, which fits "khởi thi" ("risen corpses", 起屍) as a class name. *dri za* = Pañcaśikha etc. → "càn-thát-bà" (gandharva). *gnod sbyin* = Vaiśravaṇa etc. → "dạ-xoa" (yakṣa). *mdun nas bstod* → "hiện tiền tán thán" ("praise in her presence").
- 1-7 *pha rol 'khrul 'khor*: "with her wrathful speech she destroys and turns back the evil applications (*sbyor ba ngan pa*) that others have performed". "tà thuật của kẻ thù" ("the evil sorcery of adversaries") fits closely. The posture "right drawn in, left extended" matches.
- 1-8 *chu skyes zhal*: "the lovely face of the glorious lady, like an opened lotus". This is her own face, and "Gương mặt hoa sen" ("lotus face") fits. *dgra bo thams cad*: "all the adverse side, the afflictions and so on". "tất thảy kẻ thù" ("all enemies") fits.
- 1-9: one wheel on the palm of the right hand, in the supreme-giving gesture. "Lòng bàn tay trang nghiêm bánh xe" ("the palm adorned with the wheel") fits. The three extended fingers of the left hand at the heart symbolise the Three Jewels, and "ngón tay kết ấn Tam Bảo … nơi trái tim" fits.
- 1-10 *rab tu dga' ba*: "fulfils the wishes of all beings, [who are] supremely joyful". The joy is what she brings to beings, so "ban niềm cực hỷ" ("who bestows supreme joy") fits. *bdud dang 'jig rten dbang du mdzad* = with that mantra-laughter she brings māras and the world under her control, so "Nhiếp phục" ("subjugates", 攝伏) fits.
- 1-12: *snang ba mtha' yas* (Amitābha) adorns her head amid her locks and "radiates immeasurable rays for beings". "Đức A Di Đà ngự trên búi tóc, / Thường hằng phóng chiếu vô lượng quang minh" fits. Amitābha is the one radiating, as in the Vietnamese.
- 1-13: the fire at the end of the eon, when seven suns rise, with the posture the reverse of 1-7. "Chân phải duỗi, chân trái co" ("right leg extended, left bent") fits.
- 1-15: *bde ma* = endowed with uncontaminated bliss, *dge ma* = free of the afflictions to be abandoned, *zhi ma* = suffering pacified, *mya ngan 'das* = conceptions exhausted. "an lạc, thiện lành, tịch tĩnh … Niết-bàn tịch diệt" fits.
- 1-16 *yi ge bcu pa'i ngag* = the peaceful mantra *oṃ tāre tuttāre ture svāhā*, and "câu chú mười chữ" ("the ten-syllable mantra") fits. *rig pa hūṃ* = the wrathful mantra *oṃ namaḥ tāre namo hari hūṃ hara svāhā*. "minh chú chữ Hum" ("the knowledge-mantra (vidyā) Hum") fits. The earlier draft's "awareness" was wrong.
- 1-17: from the HŪṂ seed she is generated as the wrathful form. "Chủng tử của ngài mang hình tướng chữ Hum" ("her seed-syllable has the form of Hum") fits. Drakpa Gyaltsen does not gloss *tu re'i zhabs*, so "Ture dậm bàn chân" ("Ture, stamping her feet") stands.
- 1-19 *lha yi tshogs rnams rgyal po*: "the lords of the hosts of gods, and Druma king of the kinnaras, worship at her feet". They serve her, and "được các vua của chúng trời phụng sự" ("served by the kings of the hosts of heaven") fits.
- 1-21 *gdon dang ro langs gnod sbyin*: "all that obstructs is pacified". The generic "ác quỷ" ("evil spirits") for *gdon* fits. *zhi ba'i mthu* = the might of pacifying the afflictions, and "uy lực tịch tĩnh" ("the might of peace") fits.

Style notes (not errors):
- 1-5 and 1-11 *'gugs*: Drakpa Gyaltsen reads it as bringing under her power ("able to bring kings and others under control"; the lokapālas "act as her messengers"). "triệu thỉnh" is the respectful verb for inviting deities. For *'gugs* (ākarṣaṇa), "câu triệu" (鉤召, "hook and summon") is the Vietnamese Vajrayana word, if a reviewer wants it.
- 1-8 *'jigs pa chen mo*: he says she terrifies the māras. "đại uy mãnh" ("great formidable might") keeps the awe but not the terror. "đại bố úy" (the termbase note's own example) would be closer. It does not have the "afraid" problem of the English "Fearful".
- 1-3: "và trí tuệ là hành xứ của ngài" ("and wisdom are her sphere") renders *spyod yul* twice, as "wisdom" and as the framing "sphere". That is acceptable, since wisdom is now named.
- 1-9 "mười phương" ("the ten directions") for *phyogs* is the idiomatic Vietnamese for "all directions". No number is at stake.
- 1-10 *'od kyi phreng ba*: Drakpa Gyaltsen explains it as "garlands of many jewels". The Vietnamese keeps the root's "chuỗi hào quang" ("garland of light"), which is fine.
- 1-12 *brgyan pa thams cad shin tu 'bar*: he reads this as the moon's light blazing. The Vietnamese keeps the root's "mọi món trang sức" ("all the ornaments"), which is fine.
- 1-15: the root and Drakpa Gyaltsen both read *swāhā oṃ*, and the Vietnamese has "Om và Soha". He does not comment on the order; the other commentaries say oṃ opens and svāhā closes. He glosses *sdig pa chen po* as "others' afflictions to be abandoned". "đại tội chướng" ("great sin-obscurations") follows the root word, which is fine.
- 1-16: "Phá vỡ tan tành thân thể **mọi** kẻ thù" adds "every". The root has only *dgra yi lus* ("the enemy's body"). This is harmless.
- 1-17 *'jig rten gsum*: he glosses it as the three realms (desire, form, formless). "ba thế giới" ("three worlds") follows the locked word *thế giới*; "ba cõi" would match his gloss exactly.
- 1-19: the Vietnamese reverses the pair to "ác mộng cùng mọi sự tranh chấp" ("bad dreams and all disputes"). The root order is disputes, then bad dreams. He specifies *rtsod pa* as the disputes of the tīrthikas. "rạng ngời hào quang" ("radiant with light") is an embellishment of *brjid* ("majesty"). He reads *go cha* as the armour of deity-body and mantra.
- 1-20: he pairs the right eye with the moon and the left with the sun. The Vietnamese does not assign eyes, which is fine.
- 1-21 *'joms pa tu re rab mchog*: he attributes the destroying to "the power of the ten-syllable mantra". "Ture tối thắng tiêu diệt tất cả" ("Ture the supreme destroys them all") fits if Ture is her name (see 1-8).
- 1-22: "Đây là…" ("This is…") closes the line as a full sentence. In the root, 1-22 is a noun phrase that runs on into 2-1 ("whoever recites this…"). The Vietnamese "những lời tán thán này" ("these praises") in 2-1 still links back.
- 1-0 heading "Chánh văn tán thán" ("the main text of the praise"): Drakpa Gyaltsen's own heading for this section is *bstod pa dngos* ("the praise proper"), so "chánh văn" fits.

**Result: 11/22 clean, 1 verse(s) with errors (1-18), 10 with mismatches only (1-3, 1-4, 1-6, 1-8, 1-11, 1-14, 1-17, 1-20, 1-21, 1-22); 13 mismatch row(s).**

#### Chapter 2 — 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Vietnamese (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-2 | ⚠ ERROR | དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར (dran pas mi 'jigs thams cad rab ster) | "by **merely** recollecting the deity's body (*lha'i sku dran pa tsam gyis*) fearlessness is given". The same *dran pa tsam gyis* ("by mere recollection") governs the next line on misdeeds | "Nhờ **luôn** ghi nhớ được ban mọi vô úy" ("through **always** remembering, one is granted all fearlessness"). *Luôn* ("always") is not in the Tibetan and makes constant recollection the condition, where the commentary stresses that mere recollection suffices | Drop "luôn", e.g. "Chỉ cần ghi nhớ, được ban mọi vô úy" ("by merely recalling [her], one is granted all fearlessness") or "Nhờ ghi nhớ…" |
| 2-2 | MISMATCH | སྲོད་དང་ཐོ་རངས (srod dang tho rangs) | "at dusk, recollect the wrathful form; at dawn, the peaceful form". Both sessions, each with its own practice | "lúc chạng vạng **hay** rạng đông" ("at dusk **or** dawn") | "lúc chạng vạng và rạng đông" ("at dusk and at dawn"). Judgment |
| 2-4 | MISMATCH | དྲན་པས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ (dran pas rab tu sel ba nyid thob) | "by recollecting the praise, the deity and the mantra, the poisons are dispelled" | "Nhờ **luôn** ghi nhớ **liền** tiêu trừ hoàn toàn" ("through **always** remembering, [they are] **at once** completely eliminated"). Neither "always" nor "at once" is in the Tibetan | Same fix as 2-2: "Nhờ ghi nhớ mà tiêu trừ hoàn toàn". Judgment |
| 2-5 | MISMATCH | སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ་ (sems can gzhan pa rnams la yang ngo) | "just as for myself, one is able to benefit other beings too". The removal of suffering applies to others as well; the sentence closes here (*ngo*) | "Cả đối với tất thảy những chúng sinh khác," ("Also toward all other sentient beings,"). An unfinished clause ending in a comma, so the benefit to others is never stated, and the line can run on into 2-6 | Close the clause, e.g. "Cho đến các chúng sinh khác cũng được như vậy." ("And likewise for other sentient beings.") |
| 2-6 | MISMATCH | བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག (bgegs rnams med cing so sor 'joms 'gyur cig) | His text reads *'joms 'gyur* (no *cig*). "Because the recitation has no hindrance, obstacles are absent; the things to be abandoned are each overcome by **their own antidote**". A statement of result, with *so sor* = "each individually" | "Nguyện mọi ma chướng tiêu tan, thảy đều tận diệt" ("**May** all obstacles vanish, all utterly destroyed"). Optative, and "each" becomes "all" | **Translator decision** (optative, following our root's *cig*). Leave. Optionally keep "each": "…từng thứ đều bị diệt trừ" |

Readings that **support** the current Vietnamese:
- 2-1: devotion to *lha mo* with body, speech and mind. "đầy đủ lòng kính tin nơi Nữ Thần" ("fully endowed with reverent faith toward the Goddess") fits. Drakpa Gyaltsen does not identify *lha mo*, so "Nữ Thần" is not contradicted.
- 2-2: *sdig pa thams cad* is pacified by mere recollection, and "Tiêu trừ … mọi ác nghiệp" ("eliminates … all evil karma") fits. *ngan 'gro* = "the result of the lower realms is pacified", and "Hủy diệt … mọi ác đạo" ("destroys … all lower destinies") fits.
- 2-3: *bye ba phrag bdun* = seventy million, and "bảy mươi triệu" is exact. The empowerment is conferred "uninterruptedly **on me**", on the reciter, so "ban truyền quán đảnh cho người" ("confer empowerment on the person") fits. *'di las che ba* = "not only this life, but more", and "điều thù thắng hơn thế" ("something more excellent than that") fits.
- 2-4: stationary and moving poisons (aconite-type plant poisons, snakes and scorpions), eaten or drunk. "độc tố … vật bất động hay loài di động" ("toxins … from immobile things or mobile creatures") fits. Drakpa Gyaltsen introduces the verse as "the common results".
- 2-5: *gdon, rims, dug* "comprising cause and effect", removed by the power of Tārā's vidyā-mantra. "ác quỷ, dịch bệnh và độc … tận diệt" ("evil spirits, epidemics and poison … eradicated") fits.
- 2-6: "those who want children obtain children…", with *'dod pa thams cad* = "all supreme and common siddhis are accomplished". "Mọi điều mong cầu thảy đều đạt được" ("all wishes are attained") fits.

Style notes (not errors):
- 2-3 "Đấng Như Lai Tôn Thắng" ("the Victorious Tathāgatas") adds *Như Lai* to *rgyal ba* (Victor). The referent is still the buddhas, so it is harmless.
- 2-4 "lỡ ăn vào hay lỡ uống vào" ("**accidentally** eaten or drunk"): *lỡ* ("by mistake") is not in the Tibetan or the gloss ("poison eaten and drunk"). It is harmless but narrows the scope; "dù đã ăn vào hay uống vào" would be neutral.
- 2-6 "ma chướng" ("demonic obstacles") for *bgegs*: he reads them as obstacles to the recitation, which fits.

**Result: 2/6 clean, 1 verse(s) with errors (2-2), 3 with mismatches only (2-4, 2-5, 2-6); 4 mismatch row(s).**

#### Colophon — a-1

Drakpa Gyaltsen quotes the colophon in a variant (see Textual notes) and gives no gloss. The Vietnamese "Bài tán thán Thế Tôn Độ Mẫu do đức Chánh Đẳng Chánh Giác thuyết giảng đến đây là viên mãn" ("The praise to the Blessed Tārā spoken by the Perfectly Complete Buddha is here complete") follows our root. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

### Textual notes (variants between Drakpa Gyaltsen's quotation and our root; not errors — the Vietnamese follows our root)

Word-level differences:
- **1-8** *'jigs pa chen **mos*** (instrumental, "by the great terror") for our *chen mo*. This supports his reading of Ture as the mantra.
- **1-12** *zla ba'i **dum bus*** ("with a moon-piece") for our *zla ba'i **rtse mos*** ("with the moon's tip"). The referent (a crescent moon; he says "a first-day moon") is the same.
- **1-16** *rig pa hūṃ las **sgrol ma*** ("liberator") for our ***sgron ma*** ("lamp"). The Vietnamese "ngọn đèn" ("lamp") follows our root.
- **1-20** *rims **nad*** ("epidemic disease") for our *rims **ni***. The meaning is unchanged.
- **2-1** *rab **dang** brjod* for our *rab **tu** brjod*. Possibly "with clear faith"; "chí thành" ("sincerely") fits either.
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
- **Named entities.** Avalokiteśvara (1-1, unnamed in the Vietnamese, as in the root), Indra, Agni, Brahmā, Vāyu, gandharva, yakṣa (1-6), Amitābha (1-12), Meru and Mandara (1-17) and kinnara (1-19) all match. Maheśvara (1-6) and Vindhya (1-17) are already rows.
- **Numbers.** Seven worlds (1-5), ten syllables (1-16), 2/3/7 recitations (2-6) and seventy million (2-3) all match. "Twice" (1-20) is already a row.
- **Kāya.** At 1-15 he says she destroys the afflictions "by her nature as dharmakāya", and at 1-17 she is generated as the wrathful body. Neither is rendered or required, and no *sku* is collapsed into "dharma" or "mind".
- **Scope.** The 1-18 venom narrowing and the 2-2 "always" were confirmed on this pass. The 1-21 "nơi thân" (one place for three) is already a row.

**Overall: 30 verses checked — 15 clean, 2 with errors, 13 with mismatches only.**
