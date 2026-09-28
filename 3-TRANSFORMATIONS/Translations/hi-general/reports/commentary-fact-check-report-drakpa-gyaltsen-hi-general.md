## Praise to the Twenty-One Taras — Commentary Fact-Check (Hindi)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md`, Jetsün Drakpa Gyaltsen (1147–1216), *sgrol ma phyag 'tshal nyi shu rtsa gcig gi bstod pa'i rnam bshad gsal ba'i 'od zer*. Commentary id `drakpa-gyaltsen`.
- **Translation audited:** `3-TRANSFORMATIONS/Translations/hi-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-hi-general.md` (Hindi, general grade, draft 3)
- **Root text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` (critical edition)
- **Date:** 2026-09-24

Method: a strict term-by-term alignment against this commentary's own glosses. It checks body (kāya), named entities, numbers, similes, agents, the order of lists and what modifies what. It is not a gist check. For each verse, every word Drakpa Gyaltsen glosses was aligned as Tibetan | gloss | Hindi | MATCH/MISMATCH before a verdict was given. Only the ⚠ ERROR and MISMATCH rows are shown below. Ground truth is the commentary's literal reading. Elaboration the verse need not carry was not flagged. The fact-checked English, the English consensus table, the Hindi word list and the Hindi back-translation report were used as context only. Where the Hindi follows one of the seven settled English translator decisions, the row says so. Every Hindi phrase cited carries a one-line English gloss. This is a preliminary self-check, not a scholarly sign-off. A domain specialist and a native Hindi reader must review it before it is treated as final (an LLM never marks its own output complete).

Extraction notes: there are 30 transclusion markers (I-3, 1-1 to 1-22, 2-1 to 2-6, a-1), with no empty buckets and no shift (`extract_commentary.py --strict`: 30 passages, 0 empty). Each bucket quotes its root line(s) and then glosses them. Every bucket ends with an ID such as `^1-2`. These are the commentary file's own paragraph IDs, which run one ahead of the root IDs; they are not transclusion markers, and the attribution is correct. I-1 and I-2 are not covered. Before the verses, Drakpa Gyaltsen gives an outline (II-1 to II-3): the praise via the peaceful form, via the wrathful form and via activity, then the benefits in four parts. It is structural only. Some buckets quote without glossing:
- I-3 is quoted with no gloss.
- 1-16 only identifies the two mantras.
- 2-1 has a fragmentary gloss ("[with] body, speech and mind, to the goddess").
- a-1 quotes the root colophon (in a variant reading) and then adds the translator's colophon (Nyen Lotsāwa, in the lineage from Nāgārjuna) and the author's colophon.

The frontmatter says `covers_verses: 1-1–1-21`, but the file also quotes and glosses 1-22 and 2-1 to 2-6. Scope is therefore 30 verses.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6, a-1 (Hindi general, draft 3) |

#### Chapter I — I-3

Drakpa Gyaltsen quotes the homage (*oṃ rje btsun ma 'phags ma sgrol ma la phyag 'tshal lo*) with no gloss. The Hindi "ॐ! पूज्य आर्या तारा को नमस्कार है।" ("Om! Homage to the venerable, noble Tārā.") matches word for word. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Hindi (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | "*gser sngo*: a colour bright like the lustre of refined gold". Glossed on its own, before and apart from *chu nas skyes* ("the hand-emblem, the lotus"). It is read as one gold hue, not gold + blue, and is not attached to the lotus | "स्वर्णिम-नीले कमल" ("a golden-blue lotus") | **Translator decision** (colours to the lotus, as in the English). Drakpa Gyaltsen gives a single gold colour that is probably hers. Leave, or note it |
| 1-4 | MISMATCH | རྒྱལ་བའི་སྲས (rgyal ba'i sras) | "the children of the Victors are **all the bodhisattvas**" | "जिनपुत्र" ("sons of the Jina"). Correct Buddhist Sanskrit (*jinaputra*), but to an ordinary Hindi reader *जिन* first means the Jain Tīrthaṅkaras | Optionally name them plainly: "जिनपुत्र बोधिसत्त्व" ("the bodhisattvas, sons of the Victors") or "बोधिसत्त्वगण" ("the bodhisattvas"). Judgment; can leave |
| 1-5 | MISMATCH | འདོད་དང་ཕྱོགས་དང་ནམ་མཁའ་གང་མ ('dod dang phyogs dang nam mkha' gang ma) | "*gang ba*: she **fills** the desire, form and formless realms" with the power and light rays of the mantra syllables | "काम, रूप और अरूप लोकों को पूर्ण करती हैं" ("**completes / fulfils** the desire, form and formless worlds"). The realms are right, but in Hindi *पूर्ण करना* usually means "complete, fulfil", not "fill" | e.g. "…लोकों को व्याप्त करती हैं" ("pervades the … worlds") or "…लोकों को (प्रकाश से) भर देती हैं" ("fills the … worlds [with light]"). Judgment |
| 1-6 | MISMATCH | སྣ་ཚོགས་དབང་ཕྱུག (sna tshogs dbang phyug) | "the great Maheśvara (*dbang phyug chen po*), who became the lord of them [Indra, Agni, Brahmā, Vāyu], offers worship at her feet". One being | "विभिन्न ईश्वरों" ("the various Īśvaras", plural) | Single-commentary reading. The English consensus left the plural, because three other commentaries read it as plural. Leave; optional note |
| 1-8 | MISMATCH | ཏུ་རེ་འཇིགས་པ་ཆེན་མོ (tu re 'jigs pa chen mo) | His text reads *chen mos* (instrumental): "by the terror of TURE she dispels all māras; because she terrifies the māras she is the Great Terrifying One". Ture is the mantra | "जो तुरे, महाभयंकर हैं" ("who is Ture, the greatly terrifying one", with Ture as her name) | **Translator decision** (Ture as her name). Leave |
| 1-8 | MISMATCH | བདུད་ཀྱི་དཔའ་བོ (bdud kyi dpa' bo) | "the *dpa' bo* is the māra of the afflictions (*nyon mongs pa'i bdud*); by conquering it, the other three [māras] are destroyed in passing" | "मार के शूरवीरों" ("Māra's warriors / heroes", plural) | **Translator decision** ("champions of Mara"). Leave |
| 1-11 | MISMATCH | ས་གཞི་སྐྱོང་བའི་ཚོགས (sa gzhi skyong ba'i tshogs) | "the ten direction-protectors (*phyogs skyong bcu*)", who obey her and act as her messengers | "पृथ्वी के रक्षकों के समूहों" ("hosts of protectors of the earth"). Literal, but it does not name the class; Hindi has the exact word *दिक्पाल* | e.g. "सभी दिक्पालों के समूहों को आकर्षित करने में समर्थ हैं" ("able to draw in all the hosts of direction-guardians"). This also moves "all" (*thams cad*) back onto the hosts, where the Hindi now has "सम्पूर्ण रूप से" ("completely"). Judgment |
| 1-11 | MISMATCH | ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ (phongs pa thams cad rnam par sgrol) | "**all beings** tormented by adverse conditions and destitute of favourable ones: she frees them from suffering and sets them in happiness". "All" goes with the *beings* she frees | "सभी प्रकार की दरिद्रता से पूर्णतः मुक्त करती हैं" ("fully frees from every kind of poverty"). The object is now a condition, and *दरिद्रता* is material poverty; "every kind of" widens it a little | e.g. "सभी दीन-दुःखी प्राणियों को पूर्णतः मुक्त करती हैं" ("fully frees all destitute and suffering beings"). Judgment (the back-translation pass chose *दरिद्रता* to follow the English "poverty") |
| 1-14 | MISMATCH | ཕྱག་གི་མཐིལ་གྱིས་བསྣུན (phyag gi mthil gyis bsnun) | "she strikes the ground with her **left hand** and makes the threatening gesture". One hand | "अपने हाथों की हथेलियों से, पृथ्वी के तल को आहत करती हैं" ("with the **palms of her hands** she wounds the surface of the earth"). Plural hands; and *आहत करना* means "injure", not "strike" | e.g. "जो अपने हाथ की हथेली से पृथ्वी-तल पर आघात करती हैं" ("who strikes the earth's surface with the palm of her hand"). The root does not mark number, so judgment |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | First reading: rays from the vajra and HŪṂ "fill the abodes of the seven classes of beings (*'gro ba rigs bdun*) and clear all their obstacles". Alternative: "she scatters into pieces the nāgas, asuras and others dwelling in the seven underground levels" | "सात स्तरों को छिन्न-भिन्न करती हैं" ("tears apart the seven levels"). The levels themselves are shattered | **Translator decision** ("seven levels", left open). The verb *छिन्न-भिन्न* fits only the alternative, and there the beings in the levels are scattered, not the levels. Leave, or soften the verb |
| 1-17 | MISMATCH | འབིགས་བྱེད ('bigs byed) | A verb: "Meru and Mandara (*ri rab man dā ra ba*, outside the trichiliocosm) are **pierced** by the light rays of the syllable HŪṂ". Possibly read as one mountain, "the Meru called Mandara" | "मेरु, मन्दर और विन्ध्य पर्वतों को, तथा तीनों लोकों को कम्पित करती हैं" ("shakes the mountains Meru, Mandara and Vindhya, and the three worlds") | **Translator decision** (Vindhya; footnoted in the English). Leave |
| 1-19 | MISMATCH | ལྷ་ཡི་ཚོགས་རྣམས་རྒྱལ་པོ (lha yi tshogs rnams rgyal po) | "the **lords** of those hosts of gods, and Druma **king** of the kinnaras, worship at her feet". They serve her; she is not their sovereign (the English fix, 4 of 4 commentaries) | "जो देवसमूहों के राजा, / देवों और किन्नरों द्वारा सेवित हैं" ("who [is] the king of the god-hosts, / served by gods and kinnaras" — or: "who is served by the king of the god-hosts, by gods and kinnaras"). Singular *राजा*, and with the line break a reader can take Tārā as the king — the error the English fixed | "जो देवसमूहों के राजाओं, / देवों और किन्नरों द्वारा सेवित हैं" ("who is served by the kings of the god-hosts, / by gods and kinnaras"). The oblique plural *राजाओं* puts the kings in the agent list. Recommended |
| 1-20 | MISMATCH | ཧ་ར་གཉིས་བརྗོད (ha ra gnyis brjod) | "*ha ra gnyis brjod*: by the mantra-speech of **the two, peaceful and wrathful** (*zhi khro gnyis*), she dispels extremely fierce epidemics". *Gnyis* is read as the two mantras, not as "twice" | "दो बार हर और तुत्तारे के उच्चारण से" ("by uttering HARA twice and TUTTĀRE") | "Twice" is the plain grammar and the English reading. Drakpa Gyaltsen alone reads "the two". Judgment; leave |
| 1-22 | MISMATCH | རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག (rtsa ba'i sngags kyi bstod pa 'di dang / phyag 'tshal ba ni nyi shu rtsa gcig) | "this praise of the peaceful and wrathful ones is **this very praise** by the twenty-one homages". One praise, described two ways | "मूल मंत्र द्वारा यह स्तुति, / और ये इक्कीस नमस्कार हैं।" ("This praise by the root mantra, / and these are the twenty-one homages.") Two items | **Translator decision** ("and"). Leave |

Readings that **support** the current Hindi (several were problems in earlier drafts, in the English or in the Vietnamese):
- 1-1 *chu skyes zhal gyi*: "from his [Avalokiteśvara's] tears arose a lotus or utpala; she was born from the opening lotus". "त्रिलोकनाथ के मुख से प्रकट कमल के, / प्रस्फुटित केसर से उत्पन्न" ("born from the blossoming stamens of the lotus that appeared from the face of the Lord of the Three Worlds") has a lotus arising from him, not a face that is a lotus. That fits. *Sgrol ma* = liberates from saṃsāra's suffering, *myur ma* = swift for beings, *dpa' mo* = heroic in conquering the afflictions. "त्वरित और शूरवीर" ("swift and valiant") fits. *Spyan … glog* → "नेत्र क्षणिक विद्युत के समान" ("eyes like a momentary flash of lightning") fits.
- 1-2: "a full moon heaped up many hundreds of times" fits "सौ पूर्ण चन्द्रमाओं के एकत्रित रूप" ("the gathered form of a hundred full moons"). He says the moons and the stars "are examples of countless radiating rays". "सहस्रों तारों के समूहों के … आभा से प्रज्वलित" ("blazing with the radiance of hosts of thousands of stars") follows the root's instrumental and keeps the stars as light.
- 1-3 *dka' thub* = *tshul khrims* (ethical discipline). "शील" ("ethical discipline") is exact. *spyod yul nyid ma* = wisdom, and "प्रज्ञा" ("wisdom") is named. The list keeps the root order: दान, वीर्य, शील, शांति, क्षान्ति, ध्यान, प्रज्ञा.
- 1-4 *de bzhin gshegs pa'i gtsug tor* = like the uṣṇīṣa of all tathāgatas. "तथागतों का उष्णीष" ("the uṣṇīṣa of the tathāgatas") fits. *ma lus pha rol phyin pa thob pa'i* = the ten perfections, attained; the Hindi gives them to the bodhisattvas ("सभी पारमिताओं को प्राप्त कर चुके जिनपुत्र", "the Jina-sons who have attained all the perfections"), which fits the genitive. *shin tu bsten* = "they carry her as their crown"; "अत्यंत आश्रय लेते हैं" ("deeply rely on her") fits.
- 1-5 *'dod / phyogs / nam mkha'* = the desire, form and formless realms. "काम, रूप और अरूप लोक" is exact. *'jig rten bdun* = the five desire-realm destinies + the form realm + the formless realm, and "सप्त लोक" ("seven worlds") fits. *Tuttāre hūṃ* is "the mantra", and "तुत्तारे और हूँ अक्षर से" ("with the syllables tuttāre and hūṃ") fits.
- 1-6: Indra ("शक्र"), Agni ("अग्नि"), Brahmā ("ब्रह्मा") and Vāyu ("वायु") match, in the root order. *'byung po* = Gaṇapati and the like → "भूत" (bhūta). *ro langs* = "Maheśvara and the like", a class → "वेताल" (vetāla). *dri za* = Pañcaśikha etc. → "गन्धर्व". *gnod sbyin* = Vaiśravaṇa etc. → "यक्ष". *tshogs* = the eight classes → "समूहों" ("hosts"). *mdun nas bstod* → "सम्मुख स्तुति" ("praise in her presence").
- 1-7 *pha rol 'khrul 'khor*: "with her wrathful speech she destroys and turns back the evil applications that others have performed". "शत्रुओं के यन्त्रों का पूर्णतः विनाश" ("utterly destroys the enemies' yantras") fits; *यन्त्र* here reads as a magical device. The posture "right drawn in, left extended" matches ("दाहिना पैर सिकोड़कर और बायां फैलाकर").
- 1-8 *'jigs pa chen mo*: she terrifies the māras. "महाभयंकर" ("greatly terrifying") is active; it does not have the "afraid" problem of the old English "Fearful". *chu skyes zhal* = her own face, like an opened lotus → "कमल मुख" ("lotus face") fits. *dgra bo thams cad* = "all the adverse side, the afflictions and so on" → "सभी शत्रुओं का अशेष वध" ("slays all enemies without exception") fits.
- 1-9: one wheel on the palm of the right hand. "जिनकी हथेली अशेष दिशाओं के चक्र से सुशोभित है" ("whose palm is adorned with the wheel of all directions") is singular and fits. The three extended fingers at the heart symbolise the Three Jewels, and "त्रिरत्न की मुद्रा से, / अपनी अंगुलियों द्वारा हृदय को … अलंकृत" fits.
- 1-10 *rab tu dga' ba*: "fulfils the wishes of all beings, [who are] supremely joyful". The joy is what she brings, so "परम आनंद देती हैं" ("who gives supreme joy") fits. *brjid pa* = outshining others, kept on the crown ("तेजोमय मुकुट", "radiant crown") as in the root. *bdud dang 'jig rten dbang du mdzad* → "मार और … लोकों को वश में करती हैं" ("brings Māra and the worlds under her control") fits.
- 1-12: *snang ba mtha' yas* (Amitābha) adorns her head amid her locks and "radiates immeasurable rays for beings". "जटाओं के मध्य में स्थित अमिताभ से, / निरंतर अत्यधिक प्रकाश …" ("from Amitābha amid her locks, great light constantly …") fits; Amitābha is the source of the light.
- 1-13: the fire at the end of the eon, when seven suns rise → "कल्पान्त की अग्नि" ("the fire of the eon's end"). The posture is the reverse of 1-7: "दाहिना पैर फैलाकर और बायां सिकोड़कर" ("right leg extended, left bent") fits. *dgra yi dpung* = all adverse things → "शत्रुओं की सेनाओं" ("enemy armies") fits.
- 1-15: *bde ma* = endowed with uncontaminated bliss, *dge ma* = free of the afflictions, *zhi ma* = suffering pacified, *mya ngan 'das* = conceptions exhausted. "सुखमयी, कल्याणमयी और शांतिमयी … निर्वाण की शांति" fits.
- 1-16 *yi ge bcu pa'i ngag* = the peaceful mantra *oṃ tāre tuttāre ture svāhā*, and "दस अक्षरों के मंत्र" ("the ten-syllable mantra") fits. *rig pa hūṃ* = the wrathful (vidyā) mantra *oṃ namaḥ tāre namo hari hūṃ hara svāhā*. "हूँ विद्याक्षर" ("the vidyā-syllable hūṃ") fits.
- 1-17: from the HŪṂ seed she is generated as the wrathful form. "जिनका बीजाक्षर हूँ के रूप में है" ("whose seed-syllable is in the form of hūṃ") fits. Drakpa Gyaltsen does not gloss *tu re'i zhabs*, so "तुरे, जो अपने चरणों से प्रहार करती हैं" ("Ture, who strikes with her feet") stands. *'jig rten gsum* = the three realms → "तीनों लोकों" fits.
- 1-18: "she holds in her hand the moon disc, which is **like a celestial lake**; *ri dwags rtags can* is the moon". "देवों के सरोवर के रूप वाले, / हरिण के चिह्न वाले चन्द्रमा" ("the moon shaped like the lake of the gods, bearing the deer-mark") puts both descriptions on the moon, so the simile tenor is right (the Vietnamese row does not recur). *dug rnams ma lus* = poisons both stationary and moving; "सम्पूर्ण विषों" ("all poisons") covers both, since *विष* is any poison (the Vietnamese "venom" error does not recur).
- 1-19 *mi'am ci* = kinnara → "किन्नर". *go cha* = the armour of deity-body and mantra → "आनंदमय और तेजोमय कवच" ("joyful and radiant armour"). *rtsod dang rmi lam ngan pa* = the tīrthikas' disputes and bad dreams → "विवादों और दुःस्वप्नों" ("disputes and bad dreams"), in the root order.
- 1-20 *rims nad* = epidemics → "अत्यंत भयंकर महामारियों" ("extremely fierce epidemics"). The eyes "like the full sun and moon" → "पूर्ण सूर्य और चन्द्रमा के समान, / अपनी दोनों आँखों से" fits.
- 1-21 *de nyid gsum*: OṂ ĀḤ HŪṂ set at her body, speech and mind. "तीन तत्त्वों से अलंकृत" ("adorned with the three tattvas") has the three set upon her, not "established by" them, and names no single place (the Vietnamese "at the body" row does not recur). *zhi ba'i mthu* = the might of pacifying the afflictions → "शांति की शक्ति" ("the might of peace") fits. *gdon, ro langs, gnod sbyin* → "ग्रहों, वेतालों और यक्षों" in the root order.

Style notes (not errors):
- 1-1: Drakpa Gyaltsen says the lotus grew from Avalokiteśvara's **tears** (*spyan chab*). "मुख से" ("from the face") follows the root's *zhal*, which is fine.
- 1-3: "प्रज्ञा के गोचर में स्थित" ("abides in the sphere of … wisdom") renders *spyod yul* twice, as wisdom and as the framing "sphere". Acceptable, since wisdom is named.
- 1-5 and 1-11 *'gugs*: he reads it as bringing under her power ("able to bring kings and others under control"; the protectors "act as her messengers"). "आकर्षित करना" is the tantric *ākarṣaṇa*, but in everyday Hindi it means "attract, charm". "आकृष्ट कर वश में करना" ("draw in and bring under control") is available if a reviewer wants it.
- 1-9 *rang gi 'od kyi tshogs rnams 'khrug*: he says the wheel's rays outshine other lights. "अपने प्रकाश के समूहों को प्रज्वलित करती हैं" ("sets ablaze the hosts of her own light") keeps the light but not the outshining. Fine.
- 1-10: he explains *'od kyi phreng ba* as "garlands of many jewels"; the Hindi keeps the root's "प्रकाश की मालाओं" ("garlands of light"). "सम्पूर्ण लोकों" ("all the worlds") adds "all". Both harmless.
- 1-11 and 1-14: "भृकुटी के विक्षेप और हूँ बीजाक्षर से" / "अपनी भृकुटी और हूँ बीजाक्षर से" ("with the frown and the seed-syllable hūṃ") makes the frown and HŪṂ two instruments. The root has "the HŪṂ of the frowning one" (*khro gnyer … yi ge hūṃ*), and he places the HŪṂ at the heart of her wrathful form. Minor.
- 1-12: he reads *brgyan pa thams cad shin tu 'bar* as the moon's light blazing; the Hindi keeps the root's "सभी आभूषण" ("all the ornaments"), which is fine. He calls the moon "a first-day moon"; "अर्धचन्द्र" (conventionally "the crescent") fits. "उत्सर्जित होता है" ("is emitted") is a technical word (also used for excretion and emissions). "विकीर्ण होता है" or "फैलता है" ("radiates, spreads") would read better.
- 1-15: the root and Drakpa Gyaltsen both read *swāhā oṃ*, and the Hindi has "स्वाहा और ॐ". He does not comment on the order. He glosses *sdig pa chen po* as "others' afflictions to be abandoned", destroyed "by her nature as dharmakāya"; "महान पापों" ("great sins") follows the root word, which is fine.
- 1-16 "शत्रुओं के शरीरों" ("the enemies' bodies") pluralises the root's *dgra yi lus*. Harmless.
- 1-18 "फट् बीजाक्षर" ("the seed-syllable phaṭ"): the word list reserves *बीजाक्षर* for HŪṂ and uses *अक्षर* for bare *yi ge*. A word-list point, not a commentary one. Also *ma lus* is "सम्पूर्ण" here where the lock for *ma lus* is *अशेष* (listed for 1-4 and 1-8 only).
- 1-20: he pairs the right eye with the moon and the left with the sun. The Hindi does not assign eyes, which is fine.
- 1-21 *'joms pa tu re rab mchog*: he attributes the destroying to "the power of the ten-syllable mantra". "वे तुरे अत्यंत श्रेष्ठ हैं" ("she, Ture, is most excellent") fits if Ture is her name (see 1-8). The word list locks *rab* to *परम*; "परम श्रेष्ठ" would follow it.
- 1-22: "…हैं।" closes the line as a full sentence. In the root, 1-22 is a noun phrase that runs on into 2-1. The Hindi "इसका" ("this") in 2-1 still links back.
- 1-0 heading "मूल स्तुति" ("the main praise"): his heading is *bstod pa dngos* ("the praise proper"), so it fits.

**Result: 11/22 clean, 0 verse(s) with errors, 11 with mismatches only (1-3, 1-4, 1-5, 1-6, 1-8, 1-11, 1-14, 1-17, 1-19, 1-20, 1-22); 14 mismatch row(s).**

#### Chapter 2 — 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Hindi (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-2 | MISMATCH | དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར (dran pas mi 'jigs thams cad rab ster) | "by **merely** recollecting **the deity's body** (*lha'i sku dran pa tsam gyis*) fearlessness is given": the wrathful form at dusk, the peaceful form at dawn | "इसके स्मरण से सम्पूर्ण अभय प्राप्त करता है" ("by remembering **this** [the praise, from 2-1 'इसका पाठ'] one gains complete fearlessness"). The Hindi supplies an object — the praise — where he names the deity herself | e.g. "उनके स्मरण मात्र से सम्पूर्ण अभय प्राप्त करता है" ("by merely remembering her, one gains complete fearlessness"). This also carries his "merely" (*tsam*). Judgment |
| 2-6 | MISMATCH | བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག (bgegs rnams med cing so sor 'joms 'gyur cig) | His text reads *'joms 'gyur* (no *cig*). "Because the recitation has no hindrance, obstacles are absent; the things to be abandoned are each overcome by **their own antidote**". A statement of result | "विघ्न न रहें और वे एक-एक कर विनष्ट हो जाएँ" ("**may** obstacles not remain, and may they be destroyed one by one"). Optative | **Translator decision** (optative, following our root's *cig*). Leave. "एक-एक कर" keeps *so sor* ("each") |

Readings that **support** the current Hindi:
- 2-1: devotion to *lha mo* with body, speech and mind. "देवी के प्रति सच्ची भक्ति से युक्त" ("endowed with true devotion toward the goddess") fits. He does not identify *lha mo*, so "देवी" is not contradicted.
- 2-2 *srod dang tho rangs*: dusk and dawn, each with its own practice. "संध्याकाल और उषाकाल में" ("at dusk **and** at dawn") fits (the Vietnamese "or" row does not recur). No "always" is added (the Vietnamese error does not recur). *sdig pa thams cad* pacified by mere recollection → "सम्पूर्ण पाप पूर्णतः शांत हो जाते हैं" ("all sins are fully pacified"). *ngan 'gro* = "the result of the lower realms is pacified" → "सभी दुर्गतियों का पूर्णतः विनाश" ("all lower destinies fully destroyed").
- 2-3: *bye ba phrag bdun* = seventy million, and "सात कोटि" (seven *koṭi* = seventy million) is exact. The empowerment is conferred on the reciter; "शीघ्र ही अभिषेक प्राप्त होगा" ("empowerment will soon be received") fits. *'di las che ba* = "not only this life, but more" → "इससे भी महानता प्राप्त करके" ("attaining greatness beyond this") fits. *sangs rgyas go 'phang mthar thug* → "अंततः बुद्धत्व के पद तक" ("finally to the state of buddhahood").
- 2-4: stationary and moving poisons (aconite-type plant poisons; snakes and scorpions), eaten or drunk. "स्थावर हो या जंगम" is the exact Sanskrit pair (*sthāvara / jaṅgama viṣa*). "खाया या पिया भी गया हो" ("even if eaten or drunk") fits, with no "accidentally". He says the poisons are dispelled by recollecting "the praise, the deity and the mantra", so "इसके स्मरण से" ("by remembering this") fits here.
- 2-5: *gdon, rims, dug* "comprising cause and effect", removed by the power of Tārā's vidyā-mantra → "ग्रहों, महामारियों और विषों" ("grahas, epidemics and poisons") in the root order. *sems can gzhan pa rnams la yang ngo* = "just as for myself, one can benefit other beings too" → "और अन्य सत्त्वों के लिए भी ऐसा ही है" ("and it is the same for other beings too"). The clause is closed (the Vietnamese row does not recur).
- 2-6: *gnyis gsum bdun* → "दो, तीन या सात बार". Sons and wealth match. *'dod pa thams cad* = "all supreme and common siddhis are accomplished" → "सभी कामनाएँ प्राप्त होंगी" ("all wishes will be attained").

Style notes (not errors):
- 2-3 "जिनों" ("the Jinas") for *rgyal ba*: correct, and consistent with "जिनपुत्र" at 1-4, but see the 1-4 row on the Jain association. "पहुँचेंगे" ("they will reach", plural) shifts from the singular reciter of 2-1/2-2 ("करता है", "प्राप्त करता है"). A native reader should smooth it.
- 2-5 "ग्रहों, महामारियों और विषों से पीड़ित होने वाले, / दुःखों का समूह" ("the mass of sufferings of those afflicted by …") is grammatically loose; "…से पीड़ित होने के दुःखों का समूह" would be cleaner.
- 2-6 "एक-एक कर" ("one by one") is sequential; he means "each by its own antidote". Close enough.

**Result: 4/6 clean, 0 verse(s) with errors, 2 with mismatches only (2-2, 2-6); 2 mismatch row(s).**

#### Colophon — a-1

Drakpa Gyaltsen quotes the colophon in a variant (see Textual notes) and gives no gloss. The Hindi "सम्यक् सम्बुद्ध द्वारा भाषित भगवती तारा की स्तुति सम्पूर्ण हुई।" ("The praise of the Blessed Tārā spoken by the Perfectly Complete Buddha is complete.") follows our root. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

### Textual notes (variants between Drakpa Gyaltsen's quotation and our root; not errors — the Hindi follows our root)

Word-level differences (`find_textual_variants.py`):
- **1-8** *'jigs pa chen **mos*** (instrumental, "by the great terror") for our *chen mo*. This supports his reading of Ture as the mantra.
- **1-12** *zla ba'i **dum bus*** ("with a moon-piece") for our *zla ba'i **rtse mos*** ("with the moon's tip"). The referent (a crescent moon; he says "a first-day moon") is the same.
- **1-16** *rig pa hūṃ las **sgrol ma*** ("liberator") for our ***sgron ma*** ("lamp"). The Hindi "दीपक" ("lamp") follows our root.
- **1-20** *rims **nad*** ("epidemic disease") for our *rims **ni***. The meaning is unchanged.
- **2-1** *rab **dang** brjod* for our *rab **tu** brjod*. Possibly "with clear faith"; "सम्यक् पाठ" ("proper recitation") fits either.
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
- **Named entities.** Avalokiteśvara (1-1, "त्रिलोकनाथ", unnamed as in the root), Indra ("शक्र"), Agni, Brahmā, Vāyu, gandharva, yakṣa (1-6), Amitābha (1-12), Meru and Mandara (1-17) and kinnara (1-19) all match. Maheśvara (1-6) and Vindhya (1-17) are already rows.
- **Numbers.** Seven worlds (1-5), one wheel (1-9), ten syllables (1-16), seven *koṭi* = seventy million (2-3) and 2/3/7 recitations (2-6) all match. "Twice" (1-20) is already a row. Two number points are rows: the plural hands at 1-14 (he says the left hand) and the singular "राजा" at 1-19 (he says the lords of the god-hosts and the kinnara king).
- **Kāya.** At 1-15 he says she destroys the afflictions "by her nature as dharmakāya", and at 1-17 she is generated as the wrathful body. Neither is rendered or required, and no *sku* is collapsed into "dharma" or "mind".
- **Agent / scope.** 1-19 (who serves whom) and 1-11 (freeing beings vs freeing from poverty) were confirmed on this pass. The two Vietnamese errors (1-18 "venom", 2-2 "always") do not recur in the Hindi.

**Overall: 30 verses checked — 17 clean, 0 with errors, 13 with mismatches only.**
