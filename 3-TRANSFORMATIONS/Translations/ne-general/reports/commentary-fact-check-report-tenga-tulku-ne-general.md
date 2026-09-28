## Praise to the Twenty-One Taras — Commentary Fact-Check (Nepali)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-བསྟན་དགའ་སྤྲུལ་སྐུ།.md` — Dorlob Tenga Tulku (commentary id `tenga-tulku`; date and lineage not given in the file)
- **Translation audited:** `3-TRANSFORMATIONS/Translations/ne-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general.md` (Nepali, general grade, draft 4)
- **Root text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`
- **Checked:** 2026-09-25

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Every content
word Tenga Tulku glosses was aligned against the Nepali before a verdict was
given; only ERROR and MISMATCH rows are printed. The Nepali was checked
directly against the Tibetan commentary, on its own words. The fact-checked
English, the English consensus table, the Hindi consensus table, the Hindi Tenga
Tulku report, the Nepali word list and the Nepali back-translation report were
used for context only. Their verdicts were not copied. Where the Nepali follows a
settled translator decision (the English front matter and consensus, or Tenkal's
Hindi decisions: 1-11 "destitution", 1-7 "amid fire", ग्रह kept and flagged,
बोधिसत्त्व at 1-4 and बुद्ध at 2-3), the row says so. Every Nepali phrase quoted
carries an English gloss. Suggested fixes keep the locked Nepali words from the
word list; no lock was found to be wrong. Nepali grammar points are listed as
style notes. Preliminary self-check, not a scholarly sign-off — a domain
specialist and a native Nepali reader review before this is treated as final (an
LLM never marks its own output complete).

Extraction notes: 29 transclusion buckets (I-3, 1-1 to 1-22, 2-1 to 2-6), none
empty, no cascading shift — each bucket quotes its own root verse and then
explains it. The `^1-1`, `^2-5` … `^3-19` markers inside the buckets are the
commentary file's own paragraph IDs, not root IDs. Not covered: I-1, I-2 and the
root colophon a-1. The commentator's own colophon ("ཞེས་རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ་མིང་པས་སོ")
sits at the end of the 2-6 bucket. The commentary was extracted into a private
scratch folder (not shared with the parallel checkers) and read in full. The
Nepali per-verse text (`extract_translation.py`, whole blocks: 23 blocks in
chapter 1, 7 in chapter 2, headings included) matches the translation file.

### Progress

| Scope checked |
|---|
| 2026-09-25 — I-3, 1-1 to 1-22, 2-1 to 2-6 (29 verses) |

#### Chapter I — I-3

He glosses *oṃ* (the nature of the five kāyas and five wisdoms), *rje btsun ma*
(protector and refuge of the three worlds, holding the three vows), *'phags ma*
(raised far above the level of ordinary beings) and *sgrol ma* (she who frees all
beings to the level of buddhahood). "ॐ, भट्टारिका आर्या तारालाई वन्दना गर्दछु।"
("Om, I pay homage to the venerable noble Tārā.") *भट्टारिका* (bhaṭṭārikā, the
venerable lady) is the Sanskrit equivalent of *rje btsun ma*. *आर्या* (ārya, noble,
as opposed to ordinary beings) fits *'phags ma*. *तारा* (from Sanskrit *tṛ*, to
carry across) fits *sgrol ma*. The locked pair भट्टारिका आर्या is supported. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Nepali (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-2 | MISMATCH | སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས (skar ma stong phrag tshogs pa rnams kyis) | A simile: "when about a thousand stars gather in one place, their light is unbearable to the eye; **likewise** light pours from her face" | "हजारौं ताराहरूको समूहद्वारा / अत्यन्त प्रज्वलित प्रकाश छर्ने" ("who spreads exceedingly blazing light **by means of** the hosts of thousands of stars") — no "like"; the stars are the instrument. *हजारौं* is "thousands", not "a thousand" | Translator's call. The literal root allows the Nepali, and the English reads the same way. To follow this commentary: "हजार ताराहरू एकै ठाउँ जम्मा भए जस्तै / अत्यन्त प्रज्वलित प्रकाश छर्ने" ("who spreads exceedingly blazing light, like a thousand stars gathered in one place") |
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | Her body colour: "bright like the lustre of gold, with the aspect of blue". The lotus is a blue utpala held at her heart in the left hand | "जसको हात सुनौलो-नीलो जलज / कमलद्वारा पूर्ण रूपले सजिएको छ" ("whose hand is fully adorned with a golden-blue water-born lotus") — the colours go to the lotus | Translator decision (1-3 colours to the lotus), kept from the English. Tenga Tulku gives the colours to her body. Leave |
| 1-3 | MISMATCH | ཞི་བ (zhi ba) | Not a seventh item. *zhi ba* means the six perfections are "unstained by faults": giving by stinginess, discipline by broken vows, patience by anger, diligence by laziness, concentration by distraction, wisdom by faulty understanding | "दान, वीर्य, शील, शान्ति, / क्षान्ति, ध्यान र प्रज्ञा जसको आचरणको क्षेत्र हो" ("generosity, diligence, discipline, peace, patience, concentration and wisdom are the field of her conduct") — seven items | Translator's call. The root lists *zhi ba* in the line, so the literal list is defensible, and the English and Hindi have the same seven. To follow this commentary, make शान्ति describe the six: "शान्तियुक्त दान, वीर्य, शील, / क्षान्ति, ध्यान र प्रज्ञा जसको आचरणको क्षेत्र हो" ("whose field of conduct is generosity, diligence, discipline, patience, concentration and wisdom, all endowed with peace"). Keeps the locked शान्ति and युक्त |
| 1-4 | MISMATCH | མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད (mtha' yas rnam par rgyal bar spyod) | *mtha' yas* = "infinite beings". She purifies the two obscurations that keep infinite beings from realising the perfection of wisdom, and so "acts in complete victory" | "अनन्त र पूर्ण विजयी आचरण गर्ने" ("who acts with infinite and completely victorious conduct") — "infinite" goes to her victory | Translator's call. The root's wording allows the Nepali, and the English has the same reading. To follow this commentary: "अनन्त प्राणीहरूका लागि पूर्ण विजयी आचरण गर्ने" ("who acts in complete victory for infinite beings") |
| 1-7 | MISMATCH | མེ་འབར་འཁྲུགས་པ་ཤིན་ཏུ་འབར་མ (me 'bar 'khrugs pa shin tu 'bar ma) | "Wisdom fire blazes from her body, burning and destroying all māras and obstacles". She herself blazes. *'khrugs* = swirling | "प्रज्वलित अग्निमा अत्यन्त प्रज्वलित हुने" ("who blazes intensely **within** a blazing fire") — she blazes inside a fire; the fire is not hers, and "swirling" is dropped | Settled decision (1-7 "amid fire" kept, Tenkal, as in the English and Hindi). Leave. If reopened: "उर्लँदो अग्निको ज्वालाले स्वयं अत्यन्त प्रज्वलित हुने" ("who herself blazes intensely with swirling flames of fire"). Keeps the locked प्रज्वलित |
| 1-10 | MISMATCH | རབ་ཏུ་དགའ་བ་བརྗིད་པ (rab tu dga' ba brjid pa) | The joy is hers: "she has supreme joy in giving all benefit and happiness to beings", with "great courage in that work" | "परम आनन्दित तेजको / मुकुटबाट प्रकाशको माला फैलाउने" ("who spreads garlands of light from a crown of supremely joyful majesty") — the joy goes to the crown's majesty, not to her | Translator's call. The Nepali follows neither this commentary nor the English consensus fix (3 of 4 commentaries: the joy is what she brings; English "who bring supreme joy"). The back-translation check did not catch this. To follow the consensus: "वन्दना परम आनन्द दिने, तेजस्वी / मुकुटबाट प्रकाशको माला फैलाउने" ("Homage, you who give supreme joy, who spread garlands of light from your majestic crown"). To follow Tenga Tulku: "वन्दना परम आनन्दले युक्त, तेजस्वी / मुकुटबाट …" ("endowed with supreme joy"). Both keep the locked परम, आनन्द, प्रकाश |
| 1-11 | MISMATCH | ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ (phongs pa thams cad rnam par sgrol) | *phongs pa* are beings: "disciples with bad karma, destitute of emptiness and compassion, suffering and engaged in misdeeds". She places all of them in omniscient buddhahood | "सम्पूर्ण दरिद्रताबाट पूर्ण रूपले तार्ने" ("who fully frees from all poverty") — दरिद्रता is the condition, and in everyday Nepali it means material poverty | Settled decision (1-11 "destitution" kept, Tenkal). Leave. If reopened: "सम्पूर्ण दरिद्रहरूलाई पूर्ण रूपले तार्ने" ("who fully frees all the destitute") fits this commentary |
| 1-12 | MISMATCH | བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར (brgyan pa thams cad shin tu 'bar) | "From **that** ornament" (the moon-crystal on her uṣṇīṣa) light blazes on "**all** beings tormented by the heat of the afflictions", cooling them. *thams cad* goes to the beings | "सम्पूर्ण आभूषणहरू अत्यन्त प्रज्वलित हुने" ("all of whose ornaments blaze intensely") | Translator's call. The root's surface wording supports "all ornaments", and the English and Hindi have the same. This commentary moves "all" to the beings and has the one moon ornament blaze. Leave |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | Rays from the dark-blue HŪṂ at her heart **protect** the beings in the seven levels (three lower realms, three higher, and desire and form taken together) from all suffering, or make them virtuous | "सातै स्तरहरूलाई तहसनहस पार्ने" ("who devastates all seven levels") | "सात स्तर" (seven levels) is the translator decision and fits the number here. The verb तहसनहस is literal for *'gems*, but this commentary reads it as protecting the beings there. Translator's call; the English ("shatter") has the same. Leave |
| 1-17 | MISMATCH | འབིགས་བྱེད ('bigs byed) | A verb: rays and mantras like vajra arrows from the HŪṂ at her heart shake and **pierce** Meru and Mandara | "मेरु, मन्दर र विन्ध्य पर्वत" ("Mounts Meru, Mandara and Vindhya") | Translator decision (1-17 Vindhya), recorded in the English front matter. Tenga Tulku reads the verb. Leave |

Readings that **support** the current Nepali (including places where earlier drafts had problems):
- 1-1: Avalokiteśvara, "the protector of the three worlds", shed many tears. They became a stream, an utpala grew from it, and she was born from its filaments. "तीन लोकका नाथको मुखबाट प्रकट कमलको / प्रस्फुटित केशरबाट उत्पन्न भएकी" ("born from the opened stamens of the lotus that appeared from the face of the Lord of the Three Worlds") has the lotus coming from him, not his face as a lotus (the draft 3 error). *myur ma* and *dpa' mo* are "acts quickly for beings" and "courage undaunted": "द्रुत र शूरवीर" ("swift and heroic") fits. "क्षणभरको बिजुली" ("a moment's lightning") fits *skad cig glog*.
- 1-2: The autumn moon is clearest (no cloud, no dust), and the fifteenth-day moon is full. "शरद् ऋतुका / सय पूर्ण चन्द्रमाहरू खप्टिए जस्तो" ("like a hundred full autumn moons piled up") fits, with the number right (draft 3 had "hundreds").
- 1-3: *dka' thub* = "the perfection of ethical discipline". "शील" (ethical discipline) is right. *spyod yul* = the perfection of wisdom, and the Nepali names "प्रज्ञा" (wisdom). "जसको हात" ("whose hand", singular) fits one lotus in the left hand.
- 1-4: *rgyal ba'i sras* are ārya-ground bodhisattvas who have the perfections of the ten grounds. "अशेष पारमिताहरू प्राप्त गरेका / बोधिसत्त्वहरूद्वारा अत्यन्त सेवित" ("deeply served by the bodhisattvas who have attained all perfections without exception") is the right way round and follows Tenkal's Hindi decision (बोधिसत्त्व for जिनपुत्र).
- 1-5: *'dod* = desire realm, *phyogs* = the seventeen abodes of the form realm, *nam mkha'* = the formless realm. "काम, रूप र अरूप लोकहरू भर्ने" ("who fills the desire, form and formless realms") fits exactly. The seven worlds are the five abodes of the desire realm plus form and formless: "सातै लोक" ("all seven worlds") has the number right. "सबैलाई निःशेष तान्न" ("draw in all, leaving none") fits drawing every being to the higher realms and liberation, none left in the lower realms.
- 1-6: *sna tshogs dbang phyug* is read with the others as "the great direction-protectors" (plural), so "विभिन्न ईश्वरहरू" ("the various Īśvaras") fits. The god order (Śakra = इन्द्र, Agni, Brahmā, Vāyu) follows the root. *'byung po* = "pretas that roam the sky": "भूत" fits. *ro langs* = "corpses made to act alive by the Māra of the dark side": "वेताल" fits. *dri za* = bardo wanderers: "गन्धर्व". They serve her from in front: "अगाडि स्तुति गरिएकी" ("praised from in front") fits.
- 1-7: *pha rol 'khrul 'khor* = the "machinations of the dark-side māras" behind adversaries' diseases and harm. "शत्रुको यन्त्रहरू" ("the enemies' devices") fits. Right leg drawn in, left extended ("दाहिने खुम्च्याएको र देब्रे तन्काएको"): the order is right.
- 1-8: "*phyag 'tshal tu re* gives the Venerable One's name", so "तुरे" as her name fits. The Māra line is glossed as the army of the four māras, and "मारका शूरवीरहरू" ("Māra's champions") fits the translator decision. "महाभयङ्करी" ("the greatly terrifying one") fits her wrathful form. "कमल-मुख" (locked for 1-8) is her own lotus face, as he says.
- 1-9: The left hand at her heart makes the Three-Jewels mudrā, holding the utpala stem. The right hand is in the supreme-giving gesture, **its palm** adorned with a thousand-spoked wheel, whose own rays swirl without measure. "जसको हत्केला सम्पूर्ण दिशाहरूको चक्रले सजिएको, / आफ्नै प्रकाशका उर्लँदा समूह फैलाउने" ("whose palm is adorned with the wheel of all directions, who spreads the surging masses of her own light") has one wheel, on the palm, and उर्लँदा ("surging") carries *'khrugs*.
- 1-10: "overwhelms or brings under control all three worlds": "मार र लोकलाई वशमा गर्ने" ("who brings Māra and the world under control") fits. The five-family crown ornament fits "मुकुट". The laughter is *tuttāre*'s: "तुत्तारेको अट्टहास" fits.
- 1-11: "पृथ्वीको रक्षा गर्ने समूहहरू / सबैलाई तान्न समर्थ भएकी" ("able to draw in **all** the hosts who protect the earth") keeps *thams cad* on the hosts, as he does (the Hindi moved it). The frown and HŪṂ are two things, as in his gloss.
- 1-12: Amitābha is "in the midst of her matted locks": "जटाको बीचमा अमिताभबाट, / निरन्तर अत्यन्त प्रकाश" fits.
- 1-13: She sits amid a garland of flames like the fire at the end of the aeon, right leg extended and left bent: "कल्पको अन्त्यको अग्नि जस्तै / प्रज्वलित मालाको बीचमा रहने", "दाहिने तन्काएको र देब्रे खुम्च्याई" fit. "शत्रुको सेना" fits the army of afflictions (enemies).
- 1-14: Both palms press the earth, both feet stamp; the HŪṂ comes with a wrathful frown: "क्रोधित भृकुटी सहितको हूँ अक्षर" fits.
- 1-15: *bde ma* / *dge ma* / *zhi ma* are glossed as bliss, virtue (the fruit of the path of virtue) and the pacification of habitual stains: "सुखी, कल्याणी, शान्ता" fits. The mantra is "adorned with oṃ at the beginning and svāhā at the end"; "स्वाहा र ॐ सँग पूर्ण रूपले युक्त" follows the root's word order and does not claim a recitation order, so it is not flagged. "महान् पाप" ("great sins") fits the ten non-virtues and five heinous acts.
- 1-16: "The peaceful mantra is the ten syllables; the mantra practised in the fierce way is *oṃ tāre hūṃ hara hara hūṃ*." "दश अक्षरको मन्त्र" fits the first. *rig pa hūṃ* is a mantra, and "विद्या हूँ" ("the vidyā HŪṂ"; *vidyā* = knowledge-mantra) fits.
- 1-17: "The Venerable One herself, in fierce wrath, stamps her feet." "तुरे जसको चरणको प्रहारले" ("Ture, by whose stamping feet") has Ture as her. The rays come from the HŪṂ seed at her heart: "हूँ को स्वरूपको बीज भएकी" fits. The three worlds are gods above, humans on and nāgas below the earth: "तीनै लोकहरूलाई हल्लाउने" ("who shakes all three worlds") has her as the one who shakes.
- 1-18: The full moon is "shaped like a lake of nectar pleasing to the gods", held in her left hand on the open utpala. "देवतालको स्वरूपको / चन्द्रमा हातमा धारण गर्ने" ("who holds in her hand the moon in the form of a gods' lake") has the lake's form on the moon (the draft 3 comma problem is gone). The poisons are moving (ignorance and afflictions) and stationary (compounded poisons); "सम्पूर्ण विषहरू" ("all poisons") — विष is the general word and covers both. The locked "तारे" (mantra syllable) avoids reading her name.
- 1-19: "The great world-protectors — the kings of the hosts of gods — and gods and kinnaras rely on her." "देवसमूहका राजाहरू, / देवता र किन्नरहरूद्वारा सेवित" ("served by the kings of the god-hosts, by gods and kinnaras") is the right way round, with राजाहरू plural. *rtsod pa* = quarrels from unhappy minds: "विवाद" fits; "नराम्रो सपना" ("bad dreams") fits.
- 1-20: "Her **two eyes**, like the sun and moon", blaze with light. "जसका दुई नेत्र पूर्ण सूर्य र चन्द्रमा जस्तै / अत्यन्त उज्यालो प्रकाशले चम्किन्छन्" ("whose two eyes, like the full sun and moon, shine with exceedingly bright light") has the eyes as the subject (the Hindi needed this fix). *rims nad* are contagious diseases causing unbearable suffering: "अत्यन्त भयंकर महामारी" fits. "हर दुई पटक उच्चारण र तुत्तारे" fits the two *hara* and *tuttāre*.
- 1-21: "the suchness of body, white OṂ; of speech, red ĀḤ; of mind, blue HŪṂ, set at the three places of the body". "तीन तत्त्वहरू स्थापित भएकी" ("on whom the three tattvas are set") fits *bkod pa*; she is not "established by" them. "शान्तिको शक्ति" ("the power of peace/pacifying") carries his "power by which all temporary and ultimate suffering is pacified". "ग्रह" (locked for *gdon*) reads as afflicting spirits beside वेताल and यक्ष, which fits "the harms of *gdon*"; kept and flagged for the native reader, per Tenkal.
- 1-22: "the praise by the root mantra … **and** the twenty-one homages", counted 1 + 6 + 7 + 1 + 6. "मूल मन्त्रद्वारा गरिएको यो स्तुति र, / एक्काइस वन्दनाहरू।" ("this praise made by the root mantra, and the twenty-one homages") lists two items and closes the praise as a summary, as he reads it.

Style notes (not errors):
- 1-1 / 1-20: *spyan* is "नयन" at 1-1 and "नेत्र" at 1-20. Neither is locked. One word throughout (नेत्र, as in Hindi) would be more consistent.
- 1-4 "तथागतको उष्णीष" ("the uṣṇīṣa of the Tathāgata"): Nepali -को does not show the plural. Tenga Tulku has the tathāgatas (plural) revering her. "तथागतहरूको" makes that explicit.
- 1-5 "तान्न सक्ने क्षमता भएकी" ("who has the ability to be able to draw") says "able" twice. The locked word for ནུས is समर्थ (used at 1-11): "तान्न समर्थ भएकी" is shorter and consistent.
- 1-7 grammar: "शत्रुको यन्त्रहरू" should be "शत्रुका यन्त्रहरू" (the genitive agrees with a plural noun).
- Word list: "पूर्ण रूपले" is locked for ཡང་དག (perfectly), but it is also used for རྣམ་པར and རབ་ཏུ at 1-3, 1-7, 1-8, 1-9, 1-11, 1-13, 1-16. Not a commentary issue; a native reader may want a different adverb for those.
- 1-11 "पृथ्वीको रक्षा गर्ने समूहहरू" ("the hosts who protect the earth") is literal. Tenga Tulku names them as the ten direction-guardians (Brahmā above, Indra east … the earth-lord below); "दिक्पालहरू" would name them.
- 1-12 "अर्धचन्द्रले मुकुट सजिएकी" ("whose crown is adorned with a crescent moon"): the Tibetan says her **head** (*dbu*) is adorned, and Tenga Tulku puts the moon on top of her uṣṇīṣa. मुकुट is also the word used at 1-10 for *dbu rgyan*. "जसको शिर अर्धचन्द्रले सजिएको छ" ("whose head is adorned with the crescent moon") is closer.
- 1-13 grammar and length: "दाहिने तन्काएको र देब्रे खुम्च्याई" mixes a participle and a conjunctive form, and the line is much longer than the others. "दाहिने तन्काएर देब्रे खुम्च्याई" or splitting the line reads better. Also "चारैतिरबाट आनन्दले घेरिएकी" ("surrounded all around by joy"): Tenga Tulku reads *kun nas bskor* as joyful, faithful disciples who circle her. "आनन्दित भक्तहरूले घेरिएकी" ("surrounded by joyful devotees") keeps the locked आनन्द. Same at 1-16 ("चारैतिर परम आनन्दले घेरिएकी").
- 1-14 "हातको हत्केलाले" ("with the palm of the hand", singular): Tenga Tulku has both palms. "दुवै हातका हत्केलाले" is closer.
- 1-15 "सुखी" in everyday Nepali is "happy, well-off". Tenga Tulku glosses *bde ma* as "endowed with perfect bliss"; "सुखमयी" is closer.
- 1-16 "दश अक्षरको मन्त्र स्थापित भएको" is ambiguous about what is set where. "जसमा दश अक्षरको मन्त्र स्थापित छ" ("in whom the ten-syllable mantra is set") is clearer.
- 1-18 "देवतालको" (gods'-lake) as one compound may read as a place name. "देवताहरूको तालको स्वरूपको" is plainer.
- 1-22 / 2-1: 1-22 ends with a full stop, and 2-1 then has no object for "पाठ गर्नाले" ("by reciting"). Tenga Tulku: the wise one recites "the praise of the twenty-one homages". Adding "यसको" at 2-1 restores the link (see chapter 2 notes).

Second pass (kāya / named entity / number): no kāya terms at issue in the Nepali. Named entities are right: Avalokiteśvara (तीन लोकका नाथ), Śakra (इन्द्र), Agni, Brahmā, Vāyu, Amitābha, Meru, Mandara, the kinnaras, the bodhisattvas. Vindhya is the translator decision. Numbers are right: सय (100) moons, सातै (7) worlds, दश (10) syllables, सातै (7) levels, तीनै (3) worlds, एक्काइस (21) homages, सात करोड (70 million), दुई / तीन / सात (2 / 3 / 7) times. The exceptions are "हजारौं" ("thousands") for the thousand stars at 1-2 and the seven-item list at 1-3; both are rows.

Textual notes (Tenga Tulku's quotation vs our root, not errors; the Nepali follows our root):
- 1-1 *ge sar phye ba* → *bye ba*. He glosses it as "born from its filaments".
- 1-12 *zla ba'i rtse mos* → *zla ba'i dum bus* ("a piece of moon-crystal"). "अर्धचन्द्र" (crescent) follows our root. Also *'od ni mdzad* → *'od rab mdzad*.
- 1-13 *bskal pa tha ma'i* → *mtha' ma'i* (same meaning); *bskor dgas* → *bskor dga'*.
- 1-14 *khro gnyer can mdzad* → *khro gnyer spyan mdzad* ("frowning eyes"). He glosses the two turbulent eyes.
- 1-16 *sgron ma* (lamp) → *sgrol ma* (liberator). "दीप" (lamp) follows our root.
- 1-20 *rims ni* → *rims nad* (same meaning).
- 1-21 *tu re rab mchog* → *tu re'i rab mchog*. He reads it as her granting "Ture's excellent and supreme wishes". "तुरे परम उत्तम भएकी" ("Ture, who is supremely excellent") follows our root.
- 1-8 The quote reads *'jigs pa chen mos* (instrumental) and *bdud kyi dpa' bo*, but the gloss explains *bdud kyi dpung* (Māra's army).
- 2-6 The quoted root line drops *'gyur cig*, but the gloss has the optative *'joms par gyur cig*.
- Spelling only: 1-7 *trad/traṭ*, 1-9 *'khrug/'khrugs*, 1-11 *nus ma/nus pa*, 1-5 and 1-10 *tuttāra*, 1-18 *ri dags/ri dwags*, 1-17 *man dā ra/mandara*.

**Result: 13/22 clean, 0 verse(s) with errors, 9 with mismatches only (1-2, 1-3, 1-4, 1-7, 1-10, 1-11, 1-12, 1-14, 1-17); 10 mismatch row(s).**

#### Chapter 2 — 2-1 to 2-6

No ERROR or MISMATCH rows. The two recollection lines the Hindi had to fix (2-2, 2-4) already say "उहाँको स्मरण" ("recollecting her") in the Nepali.

Readings that **support** the current Nepali:
- 2-1: "*lha mo de la*" ("to **that** goddess") points back to Tārā, and "देवीप्रति पूर्ण रूपले भक्तिले युक्त" ("fully endowed with devotion to the goddess") fits. *blo ldan* = "a person with intelligence": "बुद्धिमान" fits. "राम्ररी पाठ गर्नाले" ("by reciting well") fits *rab tu brjod*.
- 2-2: "साँझ र बिहान उठेर" ("rising at dusk and at dawn") keeps both times, which he calls "the two main ones" (her wrathful form at dusk, her peaceful form at dawn). "उहाँको स्मरण गर्नाले सम्पूर्ण अभय राम्ररी प्रदान गर्छ" ("by recollecting her, [she] grants complete fearlessness") fits "by merely recalling [her] she grants all fearlessness" — recollecting her, not the text, and she is the one who grants. "सम्पूर्ण पापहरू पूर्ण रूपले शान्त" fits all non-virtue pacified. "सम्पूर्ण दुर्गतिहरूलाई नष्ट" fits freedom from the lower-realm abodes.
- 2-3: "सात करोड" = 70 million (one करोड is ten million), so the number is right. "बुद्धहरू" for *rgyal ba* follows Tenkal's Hindi decision (बुद्ध at 2-3), and he glosses *rgyal ba* as buddhas. "चाँडै अभिषेक दिइनेछ" ("empowerment will swiftly be given") leaves the recipient open, as the English does. Tenga Tulku's own reading (the Victors empowered Tārā as the Mother) is not contradicted, so it is not flagged; this is the open form the Hindi report suggested. "यसभन्दा पनि महानता प्राप्त गरी, / अन्तिम बुद्ध पदमा पुग्नेछ" ("attaining greatness beyond this, will reach the final state of buddhahood") fits his greatness and ultimate buddhahood, with a singular verb for the one reciter.
- 2-4: "उहाँको स्मरण गर्नाले पूर्ण रूपले हट्नेछ" ("by recollecting her, it will be fully removed") fits "by merely recollecting the Venerable One's blessing". The moving poisons are snakes, fang, meat and hair poisons; the stationary ones stay: "स्थावर होस् वा जङ्गम" ("whether stationary or moving") fits. "खाएको र पिएको भए तापनि" ("even if eaten and drunk") fits.
- 2-5: *gdon* = "the hosts of harm", *rims nad* = epidemic from disturbed elements: "ग्रह, महामारी र विष" fits (ग्रह kept and flagged, per Tenkal). "अन्य प्राणीहरूका लागि पनि त्यस्तै हुनेछ" ("and so it will be for other beings too") fits "not only for oneself — she protects other beings from all suffering too". The block ends with a full stop.
- 2-6: "विघ्नहरू नरहून् र एक-एक गरी नष्ट होऊन्" ("may obstacles not remain, and may they be destroyed one by one") is optative and agrees with his "*'joms par gyur cig*" (translator decision). The temporary wishes are children and wealth; the ultimate wish is buddhahood. "सम्पूर्ण इच्छाहरू प्राप्त हुनेछ" ("all wishes will be fulfilled") fits.

Style notes (not errors):
- 2-1 grammar: "जुन बुद्धिमानले राम्ररी पाठ गर्नाले" mixes a relative (जुन, "which") with a conditional (गर्नाले, "by doing"), and there is no object (see 1-22). "जो बुद्धिमान्‌ले यसको राम्ररी पाठ गर्छ," ("the wise one who recites this well") or "कुनै बुद्धिमान्‌ले यसको राम्ररी पाठ गरेमा," ("if any wise one recites this well") is smoother. "भक्तिले युक्त" (instrumental ले with युक्त) reads better as "भक्तियुक्त" or "भक्तिसँग युक्त"; both keep the locked युक्त.
- 2-2 grammar: "सम्पूर्ण पापहरू पूर्ण रूपले शान्त हुन्छ" — plural subject, so "हुन्छन्".
- 2-4 "त्यो भयंकर महा विष" ("that terrible great poison") does not carry *de yi* ("its", "that one's"). He reads it as "the poison of that person". Minor.
- 2-5 grammar: "पीडित भएको, / सम्पूर्ण दुःखका समूहहरू … हटाइनेछ" leaves "afflicted" dangling and the verb singular. "ग्रह, महामारी र विषद्वारा पीडित हुनेहरूका / सम्पूर्ण दुःखका समूहहरू पूर्ण रूपले हटाइनेछन्" ("the masses of suffering of those afflicted … will be fully removed").
- 2-6 grammar: "सम्पूर्ण इच्छाहरू प्राप्त हुनेछ" — plural subject, so "हुनेछन्". Also "स्पष्ट रूपले पाठ" ("recite clearly") for *mngon par brjod*: Tenga Tulku reads it as "recite with manifest faith". "श्रद्धापूर्वक पाठ" ("recite with faith") is closer.

**Result: 6/6 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

**Overall: 29 verses checked — 20 clean, 0 with errors, 9 with mismatches only.**

For the reviewer: this is a preliminary machine self-check. A specialist in the Tibetan commentarial tradition and a native Nepali reader must both review it before any fix is treated as settled. No row is an ERROR. The one row worth acting on is 1-10: the Nepali gives the joy to the crown, which neither this commentary nor the English consensus supports. Every other row is a translator's call or a settled translator decision. The grammar notes (1-7, 2-1, 2-2, 2-5, 2-6) are for the native reader.
