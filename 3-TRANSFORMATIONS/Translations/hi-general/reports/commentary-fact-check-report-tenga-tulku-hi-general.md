## Praise to the Twenty-One Taras — Commentary Fact-Check (Hindi)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-བསྟན་དགའ་སྤྲུལ་སྐུ།.md` — Dorlob Tenga Tulku (commentary id `tenga-tulku`; date and lineage not given in the file)
- **Translation audited:** `3-TRANSFORMATIONS/Translations/hi-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-hi-general.md` (Hindi, general grade, draft 3)
- **Root text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`
- **Checked:** 2026-09-24

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Every content
word Tenga Tulku glosses was aligned against the Hindi before a verdict was
given; only ERROR and MISMATCH rows are printed. The Hindi was checked
directly against the Tibetan commentary. The fact-checked English, the English
consensus table, the Hindi word list and the Hindi back-translation report were
used for context only. Their verdicts were not copied. Where the Hindi follows one
of the seven settled English translator decisions, the row says so. Every Hindi
phrase quoted carries an English gloss. Suggested fixes keep the locked Hindi words
from the word list; no lock was found to be wrong. Preliminary self-check, not a
scholarly sign-off — a domain specialist and a native Hindi reader review before
this is treated as final (an LLM never marks its own output complete).

Extraction notes: 29 transclusion buckets (I-3, 1-1 to 1-22, 2-1 to 2-6), none
empty, no cascading shift — each bucket quotes its own root verse and then
explains it. The `^1-1`, `^2-5` … `^3-19` markers inside the buckets are the
commentary file's own paragraph IDs, not root IDs. Not covered: I-1, I-2 and the
root colophon a-1. The commentator's own colophon ("ཞེས་རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ་མིང་པས་སོ")
sits at the end of the 2-6 bucket. One extraction run wrote to a scratch folder that
another run overwrote while it was being read, so its 2-1 to 2-6 buckets briefly held
Tāranātha's prose. The commentary was re-extracted into a private folder and
checked against the raw file; everything below uses Tenga Tulku's own text. The
Hindi per-verse text (`extract_translation.py`, whole blocks) was spot-checked
against the translation file and matches it.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6 (29 verses) |

#### Chapter I — I-3

He glosses *oṃ* (the nature of the five kāyas and five wisdoms), *rje btsun ma*
(protector and refuge of the three worlds, holding the three vows), *'phags ma*
(raised far above the level of ordinary beings) and *sgrol ma* (she who frees all
beings to the level of buddhahood). "ॐ! पूज्य आर्या तारा को नमस्कार है।" ("Om!
Homage to the venerable, noble Tārā.") *आर्या* (ārya, noble, as opposed to
ordinary *पृथग्जन*) fits *'phags ma*. *पूज्य* (worthy of reverence) fits *rje btsun
ma*. *तारा* (from Sanskrit *tṛ*, to carry across) fits *sgrol ma*. The locked pair
पूज्य आर्या is supported. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Hindi (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-2 | MISMATCH | སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས (skar ma stong phrag tshogs pa rnams kyis) | A simile: "when about a thousand stars gather in one place, their light is unbearable to the eye; **likewise** light pours from her face" | "जो सहस्रों तारों के समूहों के, / अत्यधिक प्रकाशमान आभा से प्रज्वलित हैं" ("who blaze with the exceedingly bright radiance of the hosts of thousands of stars") — no "like", so the stars' own light is what she blazes with. *सहस्रों* is "thousands", not "a thousand" | Translator's call. The literal root allows the Hindi, and the English reads the same way. To follow this commentary: "जो सहस्र तारों के एकत्रित समूह के समान / अत्यधिक प्रकाशमान आभा से प्रज्वलित हैं" ("who blaze with exceedingly bright radiance, like a thousand gathered stars") |
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | Her body colour: "bright like the lustre of gold, with the aspect of blue". The lotus is a blue utpala held at her heart in the left hand | "स्वर्णिम-नीले कमल से" ("with a golden-blue lotus") — the colours go to the lotus | Translator decision (1-3 colours to the lotus), kept from the English. Tenga Tulku gives the colours to her body. Leave |
| 1-3 | MISMATCH | ཞི་བ (zhi ba) | Not a seventh item. *zhi ba* means the six perfections are "unstained by faults": giving by stinginess, discipline by broken vows, patience by anger, diligence by laziness, concentration by distraction, wisdom by faulty understanding | "दान, वीर्य, शील, शांति, / क्षान्ति, ध्यान और प्रज्ञा" ("generosity, diligence, discipline, peace, patience, concentration and wisdom") — seven items | Translator's call. The root lists *zhi ba* in the line, so the literal list is defensible, and the English has the same seven. To follow this commentary, make शांति describe the six: "जो शांति से युक्त दान, वीर्य, शील, / क्षान्ति, ध्यान और प्रज्ञा के गोचर में स्थित हैं" ("who abide in the domain of generosity, diligence, discipline, patience, concentration and wisdom, all imbued with peace") |
| 1-4 | MISMATCH | མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད (mtha' yas rnam par rgyal bar spyod) | *mtha' yas* = "infinite beings". She purifies the two obscurations that keep infinite beings from realising the perfection of wisdom, and so "acts in complete victory" | "जो अनन्त और पूर्ण विजय से कार्य करती हैं" ("who act with infinite and complete victory") — "infinite" goes to her victory | Translator's call. The root's wording allows the Hindi, and the English has the same reading. To follow this commentary: "जो अनन्त सत्त्वों के लिए पूर्ण विजय से कार्य करती हैं" ("who act in complete victory for infinite beings") |
| 1-7 | MISMATCH | མེ་འབར་འཁྲུགས་པ་ཤིན་ཏུ་འབར་མ (me 'bar 'khrugs pa shin tu 'bar ma) | "Wisdom fire blazes from her body, burning and destroying all māras and obstacles". She herself blazes | "और प्रज्वलित अग्नि की प्रचंड ज्वालाओं में अत्यंत देदीप्यमान हैं" ("and who shine brightly **within** the fierce flames of a blazing fire") — she shines inside a fire; the fire is not hers | Translator's call. Make her the one who blazes: "और उमड़ती अग्नि-ज्वालाओं से स्वयं अत्यंत प्रज्वलित हैं" ("and she herself blazes intensely with swirling flames of fire"). Keeps the locked प्रज्वलित |
| 1-10 | MISMATCH | རབ་ཏུ་དགའ་བ་བརྗིད་པ (rab tu dga' ba brjid pa) | The joy is hers: "she has supreme joy in giving all benefit and happiness to beings", with "great courage in that work" | "जो परम आनंद देती हैं" ("who gives supreme joy"). The majesty goes to the crown: "तेजोमय मुकुट" ("majestic crown") | Follows the English consensus fix (3 of 4 commentaries read the joy as what she brings). Tenga Tulku is the one that disagrees. Leave, unless the translator reopens it ("जो परम आनंद से युक्त हैं", "who are endowed with supreme joy") |
| 1-11 | MISMATCH | ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ (phongs pa thams cad rnam par sgrol) | *phongs pa* are beings: "disciples with bad karma, destitute of emptiness and compassion, suffering and engaged in misdeeds". She places all of them in omniscient buddhahood | "सभी प्रकार की दरिद्रता से पूर्णतः मुक्त करती हैं" ("completely frees from every kind of poverty") — दरिद्रता is the condition, and in ordinary Hindi it means material poverty | Translator's call. The object is the destitute beings, and their destitution is spiritual. "सभी दरिद्र जनों को पूर्णतः मुक्त करती हैं" ("completely frees all who are destitute") keeps the literal word and fits this commentary. Draft 3 chose दरिद्रता on purpose (back-translation check, following the English "destitution") |
| 1-12 | MISMATCH | བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར (brgyan pa thams cad shin tu 'bar) | "From **that** ornament" (the moon-crystal on her uṣṇīṣa) light blazes on "**all** beings tormented by the heat of the afflictions", cooling them. *thams cad* goes to the beings | "जिनके सभी आभूषण अत्यंत प्रकाशमान हैं" ("all of whose ornaments are extremely luminous") | Translator's call. The root's surface wording supports "all ornaments", and the English has the same. This commentary moves "all" to the beings and has the one moon ornament blaze. Leave |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | Rays from the dark-blue HŪṂ at her heart **protect** the beings in the seven levels (three lower realms, three higher, and desire and form taken together) from all suffering, or make them virtuous | "सात स्तरों को छिन्न-भिन्न करती हैं" ("shatters the seven levels") | "सात स्तर" (seven levels) is the translator decision and fits the number here; it avoids the "seven underworlds" (पाताल) of draft 2. The verb छिन्न-भिन्न is literal for *'gems*, but this commentary reads it as protecting the beings there. Translator's call. The English ("shatter") has the same |
| 1-17 | MISMATCH | འབིགས་བྱེད ('bigs byed) | A verb: rays and mantras like vajra arrows from the HŪṂ at her heart shake and **pierce** Meru and Mandara | "मेरु, मन्दर और विन्ध्य पर्वतों को" ("Mounts Meru, Mandara and Vindhya") | Translator decision (1-17 Vindhya), recorded in the English front matter. Tenga Tulku reads the verb. Leave |
| 1-20 | MISMATCH | ཉི་མ་ཟླ་བ་རྒྱས་པའི། སྤྱན་གཉིས་པོ (nyi ma zla ba rgyas pa'i spyan gnyis po) | "Her **two eyes**, like the sun and moon", blaze with light and rays | "जो पूर्ण सूर्य और चन्द्रमा के समान, / अपनी दोनों आँखों से अत्यंत प्रकाशमान हैं" ("who, like the full sun and moon, shine brilliantly with her two eyes") — the simile attaches to her, and the eyes become the means | Near-mechanical: "जिनके दोनों नेत्र पूर्ण सूर्य और चन्द्रमा के समान / अत्यंत प्रकाशमान हैं" ("whose two eyes shine brilliantly like the full sun and moon"). The English also has the eyes as the subject. नेत्र matches 1-1 |

Readings that **support** the current Hindi (including places where earlier drafts had problems):
- 1-1: Avalokiteśvara, "the protector of the three worlds", shed many tears. They became a stream, an utpala grew from it, and she was born from its filaments. "जो त्रिलोकनाथ के मुख से प्रकट कमल के, / प्रस्फुटित केसर से उत्पन्न हुई हैं" ("born from the opened stamens of the lotus that appeared from the face of the Lord of the Three Worlds") has the lotus coming from him, not his face as a lotus. That was the draft 2 error. *myur ma* and *dpa' mo* are "acts quickly for beings" and "courage undaunted": "त्वरित और शूरवीर" ("swift and heroic") fits. "क्षणिक विद्युत" ("a flash of lightning") fits.
- 1-2: The autumn moon is clearest (no cloud, no dust), and the fifteenth-day moon is full. "शरद ऋतु के सौ पूर्ण चन्द्रमाओं" ("a hundred full autumn moons") fits.
- 1-3: *dka' thub* = "the perfection of ethical discipline". "शील" (ethical discipline) is right; *तप* ("austerity") would have been the earlier English error. *spyod yul* = the perfection of wisdom, and the Hindi names "प्रज्ञा" (wisdom).
- 1-4: *rgyal ba'i sras* are ārya-ground bodhisattvas who have the perfections of the ten grounds. "जिनपुत्र" (Jina-sons) is the standard Sanskrit word for bodhisattvas and has no everyday "lay Buddhist" sense (the Vietnamese *Phật tử* problem does not arise). "अशेष सभी पारमिताओं को प्राप्त कर चुके जिनपुत्र जिनका अत्यंत आश्रय लेते हैं" ("the Jina-sons who have attained all perfections without exception rely deeply on her") is the right way round.
- 1-5: *'dod* = desire realm, *phyogs* = the seventeen abodes of the form realm, *nam mkha'* = the formless realm. "काम, रूप और अरूप लोकों" ("the desire, form and formless realms") fits exactly. The seven worlds are the five abodes of the desire realm plus form and formless, and "सप्त लोकों" has the number right. "बिना शेष छोड़े सबको आकर्षित करने में समर्थ" ("able to draw in all, leaving none") fits drawing every being to the higher realms and liberation, none left in the lower realms. आकर्षण is the Sanskrit term for this summoning.
- 1-6: *sna tshogs dbang phyug* is read with the others as "the great direction-protectors" (plural), so "विभिन्न ईश्वरों" ("the various Īśvaras") fits. The god order (Śakra, Agni, Brahmā, Vāyu) follows the root. *'byung po* = "a class of pretas that roam the sky, always tormented by fear and suffering": "भूत" (ghost, spirit) fits. *ro langs* = "corpses made to act alive by the Māra of the dark side": "वेताल" fits. *dri za* = bardo wanderers, and "गन्धर्व" is the standard term. They stand before her: "जिनके सम्मुख स्तुति" ("praised in her presence") fits.
- 1-7: *pha rol 'khrul 'khor* = the "machinations of the dark-side māras" behind adversaries' diseases and harm. "शत्रुओं के यन्त्रों" ("the enemies' magic devices") fits. Right leg drawn in, left extended ("दाहिना पैर सिकोड़कर और बायां फैलाकर"): the order is right.
- 1-8: "*phyag 'tshal tu re* gives the Venerable One's name", so "तुरे" as her name fits. The Māra line is glossed as the army of the four māras (divine-son, lord of death, aggregates, afflictions), and "मार के शूरवीरों" ("Māra's champions") fits the translator decision. "महाभयंकर" ("greatly terrifying") fits her wrathful form.
- 1-9: The left hand at her heart makes the Three-Jewels mudrā, holding the utpala stem. The right hand is in the supreme-giving gesture, **its palm** adorned with a thousand-spoked wheel. "जिनकी हथेली अशेष दिशाओं के चक्र से सुशोभित है" ("whose palm is adorned with the wheel of all directions") has one wheel, on the palm.
- 1-10: "overwhelms or brings under control all three worlds" — "वश में करती हैं" ("brings under control") fits. The five-family crown ornament fits "मुकुट". The laughter is *tuttāre*'s: "तुत्तारे के महान हास्य" fits.
- 1-13: She sits amid a garland of flames like the fire at the end of the aeon, right leg extended and left bent. "कल्पान्त की अग्नि के समान", "दाहिना पैर फैलाकर और बायां सिकोड़कर" fit.
- 1-15: *bde ma* / *dge ma* / *zhi ma* are glossed as bliss, virtue (the fruit of the path of virtue) and the pacification of habitual stains, and "सुखमयी, कल्याणमयी और शांतिमयी" ("blissful, virtuous, peaceful") fits. The mantra is "adorned with oṃ at the beginning and svāhā at the end"; "स्वाहा और ॐ से पूर्णतः युक्त" follows the root's word order and does not claim a recitation order, so it is not flagged. "महान पापों" ("great sins") fits the ten non-virtues and five heinous acts.
- 1-16: "The peaceful mantra is the ten syllables; the mantra practised in the fierce way is *oṃ tāre hūṃ hara hara hūṃ*." "दस अक्षरों के मंत्र" ("the ten-syllable mantra") fits the first. *rig pa hūṃ* is a mantra, and "हूँ विद्याक्षर" ("the vidyā-syllable HŪṂ"; *vidyā* = knowledge-mantra) fits. The English second draft had "awareness".
- 1-17: "The Venerable One herself, in fierce wrath, stamps her feet." "तुरे, जो अपने चरणों से प्रहार करती हैं" ("Ture, who strikes with her feet") has Ture as her, not a syllable she uses. The rays come from the HŪṂ seed at her heart, and "जिनका बीजाक्षर हूँ के रूप में है" ("whose seed-syllable is in the form of HŪṂ") fits. The three worlds are gods above the earth, humans on it and nāgas below, and "तीनों लोकों" fits.
- 1-18: The full moon is "shaped like a lake of nectar pleasing to the gods", held in her left hand on the open utpala. "देवों के सरोवर के रूप वाले, हरिण के चिह्न वाले चन्द्रमा को हाथ में धारण करती हैं" fits. The poisons are moving (ignorance and afflictions) and stationary (compounded poisons, *sbyar dug*). "सम्पूर्ण विषों" ("all poisons") — विष is the general word and covers both, so the Vietnamese narrowing (*nọc độc*, venom) does not arise. The locked "तारे" (mantra syllable) avoids reading her name.
- 1-19: "The great world-protectors — the kings of the hosts of gods — and gods and kinnaras rely on her." "जो देवसमूहों के राजा, / देवों और किन्नरों द्वारा सेवित हैं" ("who is served by the kings of the god-hosts, by gods and kinnaras") is the right way round. *rtsod pa* = quarrels from unhappy minds, and "विवादों" ("disputes") fits; "दुःस्वप्नों" ("bad dreams") fits.
- 1-20: *rims nad* are contagious diseases causing unbearable suffering, and "अत्यंत भयंकर महामारियों" ("the most terrible epidemics") fits. "दो बार हर और तुत्तारे" fits the two *hara* and *tuttāre*.
- 1-21: "the suchness of body, white OṂ; of speech, red ĀḤ; of mind, blue HŪṂ, set at the three places of the body". "तीन तत्त्वों से अलंकृत" ("adorned with the three tattvas") has them on her, not establishing her; the English second draft had "established by". "शांति की शक्ति" ("the power of peace/pacifying"): Hindi शांति also names the pacifying activity (*śāntika*, शान्तिक कर्म), so it carries his "power by which all temporary and ultimate suffering is pacified". The Vietnamese *tịch tĩnh* problem does not arise, and the locked शांति stands. "ग्रहों" (locked for *gdon*) reads as afflicting spirits beside वेताल and यक्ष, which fits "the harms of *gdon*".
- 1-22: "the praise by the root mantra … **and** the twenty-one homages", counted 1 + 6 + 7 + 1 + 6. That is two items, which fits "और ये इक्कीस नमस्कार हैं" ("and these are the twenty-one homages", the translator decision). He treats the line as a summary of the praise, which fits the Hindi closing statement.

Style notes (not errors):
- 1-3 "जिनके हाथ … अलंकृत हैं" ("whose hand(s) are adorned"): the honorific plural reads naturally but can suggest both hands. Tenga Tulku has the lotus in the left hand at her heart.
- 1-4 "जो तथागतों का उष्णीष हैं" ("who is the uṣṇīṣa of the tathāgatas") is literal. Tenga Tulku reads the line as the tathāgatas revering her, because she is the Mother, Prajñāpāramitā. He does not gloss *gtsug tor* itself.
- 1-9 "अपने प्रकाश के समूहों को प्रज्वलित करती हैं" ("sets ablaze the masses of her own light"): *'khrugs* is "swirling, turbulent", and प्रज्वलित is the locked word for འབར (blazing), a different verb. Tenga Tulku has the light as the wheel's own rays swirling without measure. "उमड़ाती हैं" ("sets surging") is closer.
- 1-11 "पृथ्वी के रक्षकों" ("the protectors of the earth") is literal. Tenga Tulku identifies them as the ten direction-guardians (Brahmā above, Indra in the east … the earth-lord below). "दिक्पालों" names them exactly. "सम्पूर्ण रूप से" ("completely") also moves *thams cad* from the hosts to the manner; he has all of them, with their retinues.
- 1-12 "जिनके शीश पर अर्धचन्द्र का मुकुट है" ("on whose head is a crescent-moon crown"): the Tibetan says her **head** is adorned with the moon, and Tenga Tulku puts it on top of her uṣṇīṣa. मुकुट is also the word used at 1-10 for *dbu rgyan*. "जिनका शीश अर्धचन्द्र से अलंकृत है" ("whose head is adorned with the crescent moon") is closer.
- 1-13, 1-16 "चारों ओर आनंद से घिरी" ("surrounded all around by joy"): Tenga Tulku reads *kun nas bskor* as joyful, faithful disciples who circle her. The Hindi allows that; "आनंदित भक्तों से घिरी" ("surrounded by joyful devotees") would make it explicit and keeps the locked आनंद.
- 1-14 "आहत करती हैं" ("wounds, injures") for *bsnun* (strike; Tenga Tulku: "press" with both palms) has a sense of injury. "आघात करती हैं" ("strikes") is plainer.
- 1-16 "हूँ विद्याक्षर" is supported (see above). "हूँ विद्यामंत्र" would name the wrathful mantra he quotes more exactly.
- 1-18 "फट् बीजाक्षर": ཡི་གེ here is the plain "letter". The word list gives अक्षर for bare ཡི་གེ and reserves बीजाक्षर for "the syllable HŪṂ". A word-list consistency point, not a commentary issue.
- 1-19 "आनंदमय और तेजोमय कवच" ("joyful and majestic armour") drops *kun nas* ("all-round"). Tenga Tulku reads the armour as protecting those who rely on her from all ill omens at all times.
- 1-21 "तीन तत्त्वों से अलंकृत": *bkod pa* is "set, arranged". "जिनके तीन स्थानों पर तीन तत्त्व स्थापित हैं" ("on whose three places the three tattvas are set") is closer to his gloss.

Second pass (kāya / named entity / number): no kāya terms at issue in the Hindi. Named entities are right: Avalokiteśvara (त्रिलोकनाथ), Śakra, Agni, Brahmā, Vāyu, Amitābha, Meru, Mandara, the kinnaras, the Jinas. Vindhya is the translator decision. Numbers are right: सौ (100) moons, सप्त (7) worlds, दस (10) syllables, सात (7) levels, तीनों (3) worlds, इक्कीस (21) homages, सात कोटि (70 million), दो / तीन / सात (2 / 3 / 7) times. The exceptions are "सहस्रों" ("thousands") for the thousand stars at 1-2 and the seven-item perfection list at 1-3; both are rows.

Textual notes (Tenga Tulku's quotation vs our root, not errors; the Hindi follows our root):
- 1-1 *ge sar phye ba* → *bye ba*. He glosses it as "born from its filaments".
- 1-12 *zla ba'i rtse mos* → *zla ba'i dum bus* ("a piece of moon-crystal"). "अर्धचन्द्र" (crescent) follows our root. Also *'od ni mdzad* → *'od rab mdzad*.
- 1-13 *bskal pa tha ma'i* → *mtha' ma'i* (same meaning); *bskor dgas* → *bskor dga'*.
- 1-14 *khro gnyer can mdzad* → *khro gnyer spyan mdzad* ("frowning eyes"). He glosses the two turbulent eyes.
- 1-16 *sgron ma* (lamp) → *sgrol ma* (liberator). "दीपक" (lamp) follows our root.
- 1-20 *rims ni* → *rims nad* (same meaning).
- 1-21 *tu re rab mchog* → *tu re'i rab mchog*. He reads it as her granting "Ture's excellent and supreme wishes". "वे तुरे अत्यंत श्रेष्ठ हैं" ("she, Ture, is most supreme") follows our root.
- 1-8 The quote reads *'jigs pa chen mos* (instrumental) and *bdud kyi dpa' bo*, but the gloss explains *bdud kyi dpung* (Māra's army).
- 2-6 The quoted root line drops *'gyur cig*, but the gloss has the optative *'joms par gyur cig*.
- Spelling only: 1-7 *trad/traṭ*, 1-9 *'khrug/'khrugs*, 1-11 *nus ma/nus pa*, 1-5 and 1-10 *tuttāra*, 1-18 *ri dags/ri dwags*, 1-17 *man dā ra/mandara*.

**Result: 12/22 clean, 0 verse(s) with errors, 10 with mismatches only (1-2, 1-3, 1-4, 1-7, 1-10, 1-11, 1-12, 1-14, 1-17, 1-20); 11 mismatch row(s).**

#### Chapter 2 — 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Hindi (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-2 | MISMATCH | དྲན་པས (dran pas) | Recollecting **her**: praying "while recalling her qualities at all times", "by merely recalling [her] she grants all fearlessness" | "इसके स्मरण से सम्पूर्ण अभय प्राप्त करता है" ("by recollecting **this**, obtains complete fearlessness") — इसके points back to the praise of 2-1 ("इसका सम्यक् पाठ", "recites this properly") | Near-mechanical: "उनके स्मरण से" ("by recollecting her"). The root gives no object; this commentary supplies her, not the text |
| 2-3 | MISMATCH | མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར (myur du dbang ni bskur bar 'gyur) | The seventy million Victors of the ten directions **empowered the Venerable One** as the Mother, the Perfection of Wisdom. Relying on one-pointed prayer to her, the reciter gains higher-realm qualities, greatness (like a universal monarch, or Indra and Brahmā) and finally buddhahood | "सात कोटि जिनों द्वारा, / शीघ्र ही अभिषेक प्राप्त होगा" ("from the seventy million Jinas, empowerment will swiftly be received") — *प्राप्त होगा* ("will be received") makes the reciter the recipient | Translator's call. The root's future *'gyur* in a benefits passage more naturally has the reciter as recipient, and Tenga Tulku's reading is his own. "सात कोटि जिन शीघ्र ही अभिषेक प्रदान करेंगे" ("the seventy million Jinas will swiftly confer empowerment") leaves the recipient open, as the English does |
| 2-4 | MISMATCH | དྲན་པས (dran pas) | "By merely recollecting the Venerable One's blessing", one gains special bliss and the suffering is removed | "तो इसके स्मरण से पूर्णतः निराकरण प्राप्त होता है" ("then by recollecting **this**, complete removal is obtained") | Near-mechanical, as at 2-2: "तो उनके स्मरण से …" ("by recollecting her"). His first reading of line 1, the three obscurations as poison ("*chos mtshungs pa*", "comparable to"), is figurative elaboration and is not flagged |

Readings that **support** the current Hindi:
- 2-1: "*lha mo de la*" ("to **that** goddess") points back to Tārā, and "देवी के प्रति सच्ची भक्ति से युक्त" ("endowed with true devotion to the goddess") fits. *blo ldan* = "a person with intelligence", and "जो भी बुद्धिमान" fits. "सम्यक् पाठ" ("recites properly") fits *rab tu brjod*.
- 2-2: "संध्याकाल **और** उषाकाल में उठकर" ("rising at dusk **and** at dawn") keeps both times, which he calls "the two main ones" (her wrathful form at dusk, her peaceful form at dawn). The Vietnamese needed a fix here; the Hindi does not. "सम्पूर्ण अभय" fits fearlessness from the eight and sixteen fears. "सम्पूर्ण पाप पूर्णतः शांत" fits all non-virtue pacified. "सभी दुर्गतियों का पूर्णतः विनाश" fits freedom from the lower-realm abodes.
- 2-3: "सात कोटि" = 70 million (one कोटि is ten million), so the number is right. "जिन" fits *rgyal ba* and matches जिनपुत्र at 1-4. "इससे भी महानता प्राप्त करके, / अंततः बुद्धत्व के पद तक पहुँचेंगे" ("attaining greatness beyond this, they will finally reach the state of buddhahood") fits his greatness and ultimate buddhahood.
- 2-4: The moving poisons are snakes, fang poisons, meat and hair poisons; the stationary are the obscurations that stay in beings' minds. "चाहे स्थावर हो या जंगम" ("whether stationary or moving") fits. "यदि खाया या पिया भी गया हो" ("even if eaten or drunk") fits.
- 2-5: *gdon* = "the hosts of harm", *rims nad* = epidemic from disturbed elements, and "ग्रहों, महामारियों और विषों" ("grahas, epidemics and poisons") fits. "और अन्य सत्त्वों के लिए भी ऐसा ही है" ("and so it is for other beings too") fits "not only for oneself — she protects other beings from all suffering too". The block ends with a full stop, so the Vietnamese run-on into 2-6 does not arise.
- 2-6: "विघ्न न रहें और वे एक-एक कर विनष्ट हो जाएँ" ("may obstacles not remain, and may they be destroyed one by one") is optative and agrees with his "*'joms par gyur cig*" (translator decision). The temporary wishes are children and wealth; the ultimate wish is buddhahood. "सभी कामनाएँ प्राप्त होंगी" ("all wishes will be fulfilled") fits.

Style notes (not errors):
- 2-4 "अत्यंत भयंकर महान विष" ("extremely fierce great poison") does not carry *de yi* ("its", "that one's"). He reads it as "the poison of that person". The English has "Their poisons". Minor.
- 2-6 "स्पष्ट पाठ" ("recite clearly") for *mngon par brjod*: Tenga Tulku reads it as "recite with manifest faith". "श्रद्धापूर्वक पाठ" ("recite with faith") is closer.

**Result: 3/6 clean, 0 verse(s) with errors, 3 with mismatches only (2-2, 2-3, 2-4); 3 mismatch row(s).**

**Overall: 29 verses checked — 16 clean, 0 with errors, 13 with mismatches only.**

For the reviewer: this is a preliminary machine self-check. A specialist in the Tibetan commentarial tradition and a native Hindi reader must both review it before any fix is treated as settled. The near-mechanical fixes are 1-20, 2-2 and 2-4. Every other row is a translator's call or a settled translator decision.
