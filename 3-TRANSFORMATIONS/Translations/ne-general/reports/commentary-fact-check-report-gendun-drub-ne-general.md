## Praise to the Twenty-One Taras — Commentary Fact-Check (Nepali)

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-རྒྱལ་བ་དགེ་འདུན་གྲུབ།.md` — Gyalwa Gendun Drub (1st Dalai Lama, 1391–1474), commentary id `gendun-drub`
- **Translation audited:** `3-TRANSFORMATIONS/Translations/ne-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne-general.md` (Nepali, general grade, draft 4)
- **Date:** 2026-09-25

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. For every verse
each word or phrase Gendun Drub glosses was aligned with the Nepali
(Tibetan | gloss | Nepali | MATCH/MISMATCH) before a verdict was given; only the
ERROR and MISMATCH rows are printed below. ⚠ ERROR = the Nepali names the wrong
thing (wrong referent, agent or grammatical role reversed, wrong number or scope, or
an added word that changes the meaning). MISMATCH = differs from Gendun Drub's reading,
but the right rendering is a translator's call. The Nepali was checked on its own
words; the Hindi report on the same commentary was used only as a model. Where the
Nepali follows a translator decision already settled for the English (1-3 colours to
the lotus; 1-8 Ture as her name and "champions of Mara"; 1-14 "seven levels"; 1-17
Vindhya; 1-22 "and"; 2-6 optative), a fix from the English consensus (1-1 lotus from
the Lord's face; 1-5 the three realms; 1-9 "wheel of all directions"), or a decision
Tenkal made in the Hindi consensus (1-4 बोधिसत्त्व and 2-3 बुद्ध; 1-7 "amid fire";
1-11 "destitution"; ग्रह kept and flagged), the row or note says so. Locked words from
the Nepali word list
(`0-INBOX/AI_translation/keyword-extraction-dharmamitra/ne/termbase-ne-general.md`) are
kept in every suggested fix. A second pass looked only for doctrinal-category swaps,
named entities and numbers. Nepali is glossed in English in parentheses. Nepali
grammar problems noticed along the way are listed as style notes.
Preliminary self-check, not a scholarly sign-off — a domain specialist and a native
Nepali reader must review it before it is treated as final (an LLM never marks its own
output complete).

Extraction notes: 29 buckets (I-3, 1-1 to 1-22, 2-1 to 2-6), none empty, no cascading
shift (`extract_commentary.py --strict`: 29 transclusions, 0 empty). Each bucket opens
with Gendun Drub's outline heading, quotes the root line or lines, then glosses them;
he also gives each homage its Tārā name. Two boundary effects, neither a shift:
(1) the 2-3 bucket runs on into the first two lines of 2-4 (*de yi dug ni drag po chen
po* = the wrong view that obstructs buddhahood; *brtan gnas* = the "stationary poisons"
of ignorance and hatred towards the Dharma), so 2-4 was audited from both buckets;
(2) the 2-6 bucket holds three readings of "two, three, seven" (certain poets; Pang
Lotsawa; Butön). The literal first reading was used as ground truth. Not covered: I-1,
I-2, a-1 and the section headings (e.g. 1-0 *मूल स्तुति*, "the root praise"), which
Gendun Drub does not gloss. Scope: 29 verses. The Nepali file parsed cleanly
(transclusion layout, whole four-line blocks).

### Progress

| Scope checked |
|---|
| 2026-09-25 — I-3, 1-1 to 1-22, 2-1 to 2-6 (29 verses) |

#### Chapter I — I-3

Glosses *oṃ* (going for refuge, offering, purifying), *rje* (supreme among the mothers
of all buddhas), *btsun* (holding the prātimokṣa, bodhisattva and mantra vows),
*'phags ma* (far from non-virtue, beyond saṃsāra and nirvāṇa), *sgrol ma* (she who
frees from the ocean of suffering), *phyag 'tshal* (sweeping away karma and
affliction; body, speech and mind in respect). "ॐ, भट्टारिका आर्या तारालाई वन्दना
गर्दछु।" (Om, I pay homage to the venerable noble Tārā) — every term matches.
*भट्टारिका* (the venerable lady) is the locked word for *rje btsun ma* and carries it
as one word, which is normal. Clean.

**Result: 1/1 clean, 0 verse(s) with errors, 0 with mismatches only; 0 mismatch row(s).**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Nepali (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 1-1 | MISMATCH | འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི (’jig rten gsum mgon chu skyes zhal gyi) | Avalokiteśvara, protector of the three realms, wept; "from the utpala born of the water of his tears, from the opening stamens of the utpala's face (*ut pa la'i zhal*), she was born". The face is the lotus's (its open blossom); the lotus grows from his tears | "तीन लोकका नाथको मुखबाट प्रकट कमलको / प्रस्फुटित केशरबाट उत्पन्न भएकी" (born from the opened stamens of the lotus that appeared from the face of the Lord of the three worlds) | Translator's call. The line follows the English consensus fix, which the root allows. If following Gendun Drub: "तीन लोकका नाथको आँसुबाट उत्पन्न कमलको" (of the lotus born from the tears of the Lord of the three worlds), though "tears" is not in the root. Leave |
| 1-2 | MISMATCH | སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། རབ་ཏུ་ཕྱེ་བའི་འོད (skar ma stong phrag tshogs pa rnams kyis rab tu phye ba'i 'od) | Comparative: from her face "light that spreads out even more than (*bas kyang*) a thousand gathered stars". He reads the hundred moons the same way (*brtsegs pa bas*: brighter even than a hundred heaped) | "हजारौं ताराहरूको समूहद्वारा / अत्यन्त प्रज्वलित प्रकाश छर्ने" (who spreads intensely blazing light **by means of** the hosts of thousands of stars) | Translator's call. *द्वारा* ("by") makes the stars the source or tool of her light; Gendun Drub makes her light outshine the stars. The root's *kyis* allows both, and the English has the same reading. E.g. "हजारौं ताराहरूको समूहभन्दा पनि / अत्यन्त प्रज्वलित प्रकाश छर्ने" (who spreads light blazing **even more than** the hosts of thousands of stars). The moon line "खप्टिए जस्तो" (like stacked) can stay |
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo; GD's text *ser sngo*) | "*sngo* is her body colour; *ser* shows the clarity of the colour — hence 'Tārā of golden colour'". The lotus is an utpala held at her heart by the left ring finger | "सुनौलो-नीलो जलज / कमलद्वारा" (with a golden-blue water-born lotus) | Translator decision (English settled: colours to the lotus). Gendun Drub gives the colours to her body, not the lotus. Leave |
| 1-4 | MISMATCH | མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད (mtha' yas rnam par rgyal bar spyod) | "She acts in complete victory over the limitless (*mtha' yas pa las*) misfortunes of this life, afflictive obscurations and cognitive obscurations" — *mtha' yas* is what she conquers | "अनन्त र पूर्ण विजयी आचरण गर्ने" (who acts with infinite and completely victorious conduct) | Translator's call. "Infinite" is attached to her victory; Gendun Drub attaches it to what she defeats. The English has the same wording. E.g. "अनन्त बाधाहरूमाथि पूर्ण विजयी आचरण गर्ने" (who acts in complete victory over limitless obstacles); "बाधा" (obstacle) is Gendun Drub's word, not the root's |
| 1-4 | MISMATCH | དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར (de bzhin gshegs pa'i gtsug tor) | "Because she is the mother of **all** the tathāgatas, they carry her like the uṣṇīṣa on their heads" — plural | "तथागतको उष्णीष स्वरूप" (who is the uṣṇīṣa of **the Tathāgata**) | Number. Nepali *-को* without *-हरू* reads as one Tathāgata; the Tibetan does not mark number, but Gendun Drub (and the English "of the Tathagatas", the Hindi "तथागतों") make it plural. Small edit: "तथागतहरूको उष्णीष स्वरूप" (the uṣṇīṣa of the Tathāgatas) |
| 1-9 | MISMATCH | རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག (rang gi 'od kyi tshogs rnams 'khrug) | "By the light of the wheel, her own emblem, other masses of light are stirred (*'khrug pa*), that is, outshone (*zil gyis gnon*)" | "आफ्नै प्रकाशका उर्लँदा समूह फैलाउने" (who spreads the surging masses of her own light) | Translator's call. The Nepali follows the English draft 4 ("radiate a turbulent mass of your own light"): her own light is the thing spread. In the commentary her light is the tool and **other** light is what is overwhelmed. E.g. "आफ्नै प्रकाश-समूहले अरू सबै प्रकाशलाई ओझेलमा पार्ने" (who with her own masses of light puts all other light in the shade). Keeps locked प्रकाश |
| 1-9 | MISMATCH | མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས་བརྒྱན་པའི (ma lus phyogs kyi 'khor los brgyan pa'i) | "the right hand, making the supreme giving **to all directions** without exception, its palm adorned with a wheel" — "all directions" goes with the giving gesture, not the wheel | "जसको हत्केला सम्पूर्ण दिशाहरूको चक्रले सजिएको" (whose palm is adorned with the wheel of all directions) | Leave. What-modifies-what differs, but the Nepali follows the root's word order and the English consensus fix (one wheel, on the palm, "of all directions"). The single wheel and the palm are right |
| 1-10 | MISMATCH | རབ་ཏུ་དགའ་བ་བརྗིད་པའི། དབུ་རྒྱན (rab tu dga' ba brjid pa'i dbu rgyan) | "Having fulfilled the wishes of the disciples who have faith and devotion, who are supremely joyful (*rab tu dga' ba*)" — the joy is the disciples', which she brings; the splendour belongs to her crown ornament | "परम आनन्दित तेजको / मुकुटबाट प्रकाशको माला फैलाउने" (who spreads garlands of light from the crown of **supremely joyful splendour**) | Translator's call, but worth taking. The joy is put on the splendour/crown, not on the beings she gladdens. The English consensus made this a fix (DG, GD, TN: "the joy is what she brings to beings"), and the English and Hindi now carry it ("who bring supreme joy"; "जो परम आनंद देती हैं"). The Nepali did not. E.g. "वन्दना परम आनन्द दिने, तेजोमय / मुकुटबाट प्रकाशको माला फैलाउने," (Homage, who gives supreme joy, who spreads garlands of light from her splendid crown). Keeps locked परम, आनन्द, प्रकाश |
| 1-14 | MISMATCH | རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས (rim pa bdun po rnams ni 'gems) | "With the HŪṂ at her heart she destroys (*'gems*), that is, dries up (*skems*), the ocean of existence of the seven levels of the world" — what is destroyed is their saṃsāric existence, not the levels | "सातै स्तरहरूलाई तहसनहस पार्ने" (who smashes all seven levels) | Translator decision ("seven levels" is settled and supported: seven world-levels). The object differs: Gendun Drub has her drying up the ocean of existence of the seven levels, not the levels themselves. The literal "smash" is defensible. Leave |
| 1-19 | MISMATCH | ལྷ་ཡི་ཚོགས་རྣམས་རྒྱལ་པོ། ལྷ་དང་མིའམ་ཅི་ཡིས་བསྟེན་མ (lha yi tshogs rnams rgyal po / lha dang mi'am ci yis bsten ma) | "The kings of the hosts of gods — Indra of the desire gods and Great Brahmā of the form realm — and the king of the kinnaras, Druma, serve her with bowed heads" — the kings serve her | "वन्दना देवसमूहका राजाहरू, / देवता र किन्नरहरूद्वारा सेवित," (Homage — [by] the kings of the god-hosts, gods and kinnaras, served) | Grammar risk on the agent. Read as one list sharing *द्वारा* ("by"), the line is right. But the comma and line break after "राजाहरू" let a reader take "वन्दना देवसमूहका राजाहरू" as "Homage to the kings of the god-hosts" — close to the error all four commentaries rejected in the English (English consensus fix #9). Mark the kings as agents too: "वन्दना देवसमूहका राजाहरूद्वारा, / देवता र किन्नरहरूद्वारा पनि सेवित," (Homage to her who is served by the kings of the god-hosts, and by gods and kinnaras too) |
| 1-21 | MISMATCH | དེ་ཉིད་གསུམ་རྣམས་བཀོད་པའི (de nyid gsum rnams bkod pa'i) | "The suchnesses of body, speech and mind: OṂ at the crown, ĀḤ at the throat, HŪṂ at the heart, set (*bkod pa*) on her" — the three are what is set; she is the one they are set on | "वन्दना तीन तत्त्वहरू स्थापित भएकी," (Homage, she who **has been established**, three tattvas) | The feminine participle *भएकी* makes Tārā the one established, with the three tattvas left unmarked. That leans towards the "established by the three suchnesses" reading which the English consensus fixed (#10, all four commentaries). E.g. "वन्दना जसमा तीन तत्त्व स्थापित छन्," (Homage to her, on whom the three tattvas are set). *तत्त्व* (tattva) itself is the right word for *de nyid* |

Readings that **support** the current Nepali:
- 1-1: *myur ma* = swift to benefit beings, *dpa' mo* = heroic in turning back the battle of saṃsāra → "द्रुत र शूरवीर" (swift and heroic). "जसका नयन क्षणभरको बिजुली जस्ता छन्" (whose eyes are like momentary lightning) matches "her two eyes, like lightning that flashes in an instant, look on the three worlds". "प्रस्फुटित केशरबाट" (from the opened stamens) matches.
- 1-2: *kun du gang ba* = the fully full autumn moon, not yet waning → "शरद् ऋतुका सय पूर्ण चन्द्रमाहरू" (a hundred full autumn moons). The draft 4 fix (सय "a hundred", not "hundreds") is right. *stong phrag* → "हजारौं" (thousands).
- 1-3: *dka' thub* = "that is, ethical discipline" → "शील" (discipline) is right. *spyod yul* = "the perfection of wisdom" → "प्रज्ञा" (wisdom) is named. The utpala adorning her hand → "जसको हात … कमलद्वारा पूर्ण रूपले सजिएको छ" (whose hand is fully adorned with a lotus).
- 1-4: she is carried like the crown uṣṇīṣa → "उष्णीष स्वरूप" (who is the uṣṇīṣa). *rgyal ba'i sras* = "the Victors' children, the bodhisattvas, who have attained the ten perfections" → "अशेष पारमिताहरू प्राप्त गरेका बोधिसत्त्वहरू" (the bodhisattvas who have attained all the perfections) — Tenkal's बोधिसत्त्व decision, and the bodhisattvas, not Tārā, are the ones who attained the perfections. "अत्यन्त सेवित" (deeply served) fits his reverent service "with the crown of the head".
- 1-5: *'dod / phyogs / nam mkha'* = desire, form, formless realms → "काम, रूप र अरूप लोकहरू भर्ने" (who fills the desire, form and formless realms) is exactly his reading (English consensus fix). "सातै लोक" (all seven worlds) matches his count: three lower realms, desire-realm gods and humans, form and formless. *'gugs* → "तान्न" (to draw in).
- 1-6: the order Indra, Agni, Brahmā, Vāyu is kept → "इन्द्र, अग्निदेव, ब्रह्मा, वायुदेव". *sna tshogs dbang phyug* is plural ("the chiefs") → "विभिन्न ईश्वरहरू" (the various Īśvaras). *'byung po* = "भूत", *ro langs* = "वेताल", *dri za* = "गन्धर्वहरू", *gnod sbyin* = "यक्ष समूह" (hosts of yakṣas). *mdun nas bstod* → "अगाडि स्तुति गरिएकी" (praised in front of her).
- 1-7: *pha rol 'khrul 'khor* = the sorcery (*mthu*) and effigy devices (*byad ma*) of others → "शत्रुको यन्त्रहरू" (the enemies' yantras) fits. Right leg drawn in (emptiness), left extended (compassion) → "दाहिने खुम्च्याएको र देब्रे तन्काएको चरणले कुल्चेर" (trampling with the right drawn in and the left extended). "प्रज्वलित अग्निमा" (amid blazing fire) follows the settled "amid fire" reading, which he supports ("haughty amid blazing fire").
- 1-8: *tu re* = "Tārā" → "वन्दना तुरे" (homage, Ture — her name). *'jigs pa chen mo* = "the wrathful one" → "महाभयङ्करी" (the greatly terrifying one), not "afraid". *bdud kyi dpa' bo* = the afflictions, and with them the four māras → the literal "मारका शूरवीरहरू" (Māra's champions) stands. *dgra bo* = the two obscurations → "सम्पूर्ण शत्रुहरूलाई अशेष" (all enemies without exception).
- 1-9: the left hand's three extended fingers at the heart form the Three Jewels mudrā → "त्रिरत्नको प्रतीक मुद्राको औंलाहरूद्वारा हृदयमा … सजिएकी" (adorned at the heart by the fingers of the mudrā symbolising the Three Jewels). **One** wheel on the right palm → "हत्केला … चक्रले" (the palm … with the wheel), singular.
- 1-10: *bzhad pa rab bzhad* = the mantra's laughter → "तुत्तारेको अट्टहास" (the loud laughter of tuttare). *bdud dang 'jig rten* = Māra and the eight great worldly gods → "मार र लोक" (Māra and the world), with no added "all". *dbang du mdzad* → "वशमा गर्ने" (who brings under her power).
- 1-11: *sa gzhi skyong ba* = the ten direction-guardians with their retinues → "पृथ्वीको रक्षा गर्ने समूहहरू सबैलाई" (all the hosts who protect the earth). *'phongs pa* = the destitute and those tormented by suffering → "सम्पूर्ण दरिद्रताबाट … तार्ने" (who frees from all destitution) — Tenkal's decision. *rnam par sgrol* → "तार्ने" (who ferries across, rescues) echoes her name well.
- 1-12: *zla ba'i rtse mo* = the first-day (crescent) moon → "अर्धचन्द्र" (crescent). **Agent:** "Amitābha dwells in the hair at her crown; for beings' sake, at all times, she (*mdzad ma*) spreads much light" → "जटाको बीचमा अमिताभबाट, / निरन्तर अत्यन्त प्रकाश प्रदान गर्ने" (she who, from Amitābha amid her locks, constantly gives intense light). The *-ने* participle makes Tārā the one who acts, as Gendun Drub does (the English makes Amitābha the agent; the Hindi had no agent). See the style note on "प्रदान".
- 1-13: right leg extended, left bent → "दाहिने तन्काएको र देब्रे खुम्च्याई". The fire at the end of the eon is the blaze of wisdom-fire → "कल्पको अन्त्यको अग्नि जस्तै / प्रज्वलित मालाको बीचमा रहने" (dwelling amid a blazing garland like the fire at the end of the eon); the draft 4 comma fix keeps the simile on the garland. *dgra yi dpung* = the afflictions of disciples → "शत्रुको सेना" (the enemy's army), literal and fine.
- 1-14: *rim pa bdun* = "the seven levels of the world" → "सातै स्तरहरू" (all seven levels), the translator decision, is supported. The palm of the hand striking the ground → "हातको हत्केलाले हिर्काउँदै" (striking with the palm of the hand) follows the root.
- 1-15: *bde ma* = undefiled bliss, *dge ma* = free of afflictions, *zhi ma* = suffering pacified, nirvāṇa as her sphere → "सुखी, कल्याणी, शान्ता, / निर्वाणको शान्ति जसको आचरणको क्षेत्र हो" (blissful, virtuous, peaceful, whose sphere is the peace of nirvāṇa). The ten-syllable mantra has OṂ first and SVĀHĀ last; "स्वाहा र ॐ सँग पूर्ण रूपले युक्त" (perfectly endowed with svāhā and oṃ) keeps the root's wording. *sdig pa chen po* → "महान् पाप" (great sin).
- 1-16: *yi ge bcu pa'i ngag* = oṃ tāre tuttāre ture svāhā → "दश अक्षरको मन्त्र" (the ten-syllable mantra). *rig pa hūṃ* = the wrathful knowledge-mantra → "विद्या हूँ" (vidyā HŪṂ), not "awareness". *dgra* = the enemies of liberation → "शत्रुको शरीर" (the enemy's body).
- 1-17: Ture is Tārā herself stamping ("the feet of Ture, arisen from the seed in the form of HŪṂ") → "वन्दना तुरे जसको चरणको प्रहारले" (homage, Ture, by the stamping of whose feet). *'bigs byed* is a mountain listed with Meru and Mandara → "विन्ध्य पर्वत" (the Vindhya mountains). She is the one who shakes them → "…हल्लाउने" (she who shakes). The mountains stand beside "तीनै लोक" (all three worlds), close to his "Meru, Mandara, Vindhya **and so on** — the three worlds". See the grammar note.
- 1-18: the moon is the thing that is lake-like → "देवतालको स्वरूपको / चन्द्रमा" (the moon in the form of the gods' lake) attaches the simile to the moon, as he does. TĀRA twice and PHAṬ remove the moving poisons → "सम्पूर्ण विषहरूलाई अशेष रूपले हटाउने" (who removes all poisons without exception).
- 1-19: the kings serve her (row above, on the wording only). Order "विवाद र नराम्रो सपना" (disputes and bad dreams) matches the root.
- 1-20: right eye sun-like (wrathful), left eye moon-like (peaceful) → "जसका दुई नेत्र पूर्ण सूर्य र चन्द्रमा जस्तै" (whose two eyes are like the full sun and moon) — the simile is on the eyes. HARA twice is the wrathful mantra and TUTTĀRA the peaceful one → "हर दुई पटक उच्चारण र तुत्तारे". *rims* = infectious disease → "महामारी" (epidemic).
- 1-21: *zhi ba'i mthu* → "शान्तिको शक्ति" (the might of peace). The supreme destroyer is Ture Tārā herself → "नष्ट गर्ने तुरे परम उत्तम भएकी" (Ture who destroys is supreme). "ग्रह" for *gdon* is kept (Tenkal's decision; see style note).
- 1-22: "these twenty-one praises with the root mantra of the peaceful and wrathful ones, **and** the homages with respectful three doors — twenty-one" → two items joined by "र" (and). The translator decision is supported.

Textual notes (commentary's text vs our root — not errors; the Nepali follows our root):
- 1-3 *ser sngo* for *gser sngo*. He still reads it as golden colour ("gser mdog can gyi sgrol ma"), so the sense is unchanged.
- 1-12 *ral pa'i khur na* for *ral pa'i khrod na* ("in the mass of her locks" / "amid her locks").
- 1-13 *mtha' ma'i* for *tha ma'i* (spelling).
- 1-16 *sgrol ma* ("liberator") for *sgron ma* ("lamp"). "दीप स्वरूप" (lamp-natured) follows our root.
- 1-10: the laughter line is not quoted, and the gloss reads *tA ra* (TĀRA) where the root has *tu ttwa ra*.
- 1-18 *ri dwags* for *ri dags* (spelling).
- 1-20 *rims nad* for *rims ni* (adds "disease").
- 1-21 *yang ldan* for *yang dag ldan* (drops *dag*; same sense).
- 2-2 adds *mal nas* ("from bed") to "rising".
- 2-3: his paraphrase has *dbang ni rim par bskul* ("empowerment urged in stages") for the root's *myur du dbang ni bskur* ("swiftly confer empowerment"); he still glosses *myur du* as "in this very life".
- 2-5 *spo* for *spong*.
- 2-6: Pang Lotsawa's paraphrase *'joms par 'gyur* ("will destroy") for our root's optative *'joms 'gyur cig*.

Style notes (not errors; the grammar points are for the native reader):
- 1-3 *zhi ba*: Gendun Drub reads it as the pacifying of the perfections' opposites (miserliness, laziness …), not as a seventh item. The Nepali keeps "शान्ति" (peace) inside the list, in the root's order. Harmless.
- 1-3 and elsewhere: "पूर्ण रूपले" (perfectly, fully) is the lock for *yang dag*, but the draft also uses it for *rnam par* (1-3, 1-7, 1-8, 1-11, 1-13) and *rab tu* (1-16, 2-2). Not wrong, but the locked phrase loses its link to one Tibetan word.
- 1-4 "सेवितलाई" and 1-6 "पूजितलाई" (to her who is served / worshipped) use *-लाई*; the other homages use the participle alone ("वन्दना … गर्ने", "Homage — she who …"). The native reader should pick one pattern.
- 1-5: "तान्न सक्ने क्षमता भएकी" (having the capacity to be able to draw in) says "able" twice. "तान्न समर्थ भएकी" (able to draw in) would match 1-11 and the lock *समर्थ* for *nus*.
- 1-7 grammar: "शत्रुको यन्त्रहरू" should be "शत्रुका यन्त्रहरू" (the enemy's yantras — *-का* before a plural noun). *'khrugs pa* (swirling, turbulent) is not rendered: "प्रज्वलित अग्निमा" (amid blazing fire). "उर्लँदो अग्निमा" (amid surging fire, the word used at 1-9) would restore it.
- 1-8 "महाभयङ्करी", but 1-20 and 2-4 "भयंकर": one spelling (ङ्क or ं) throughout.
- 1-11: the root has "the HŪṂ **of** the moving frown" (*khro gnyer g.yo ba'i yi ge hūṃ*), and Gendun Drub makes the HŪṂ the instrument, the frown her wrathful manner. "चलायमान क्रोधित भृकुटी र हूँ अक्षरद्वारा" (by the moving wrathful frown **and** the syllable HŪṂ) makes them two tools, as the English does. Harmless.
- 1-12: "प्रदान गर्ने" (who bestows) for *'od mdzad* / his *'gyed par mdzad* ("spreads"). "फैलाउने" (who spreads), the verb used at 1-10, is closer. Also "सम्पूर्ण आभूषणहरू अत्यन्त प्रज्वलित हुने" reads loosely; "जसका सम्पूर्ण आभूषणहरू अत्यन्त प्रज्वलित छन्" (all of whose ornaments blaze intensely) is clearer. "अर्धचन्द्रले मुकुट सजिएकी": *dbu* is the head, so "अर्धचन्द्रले शिर सजिएकी" (whose head is adorned with the crescent moon) is a shade closer.
- 1-13 grammar: "दाहिने तन्काएको र देब्रे खुम्च्याई" mixes two verb forms. Match 1-7: "दाहिने तन्काएको र देब्रे खुम्च्याएको चरणले" (with the right extended and the left drawn in). The line is also long.
- 1-13 and 1-16 *kun nas bskor (rab) dga'*: he reads "disciples with faith who delight in turning the Dharma wheel", and the enemies are theirs (afflictions; self-grasping). "चारैतिरबाट आनन्दले घेरिएकी" (surrounded on all sides by joy) is the settled literal reading.
- 1-15: "सुखी" (happy, well-off) is everyday Nepali; for *bde ma* (endowed with undefiled bliss) "सुखमयी" (blissful) is closer and matches कल्याणी, शान्ता.
- 1-16 grammar: "दश अक्षरको मन्त्र स्थापित भएको" (the ten-syllable mantra having been set) dangles — set where? "जसमा दश अक्षरको मन्त्र स्थापित छ" (in whom the ten-syllable mantra is set). "विद्या हूँ": to a lay reader *विद्या* means "learning"; "विद्यामन्त्र हूँ" (the knowledge-mantra HŪṂ) is clearer, as the English "knowledge-mantra hum".
- 1-17 grammar: "मेरु, मन्दर र विन्ध्य पर्वत, / तीनै लोकहरूलाई हल्लाउने" leaves the mountains without the object marker while the worlds have it, so a reader could take the mountains as a subject. E.g. "मेरु, मन्दर र विन्ध्य पर्वतलाई, / तीनै लोकलाई हल्लाउने" (who shakes Meru, Mandara and the Vindhya mountains, and all three worlds). Also "तीनै लोकहरू" doubles the plural (*तीनै* already means "all three").
- 1-18: "देवतालको" can be misread as "देवता-ल-को" (of the deity). Write "देव-तालको" or "दिव्य तालको" (of the divine lake). *ri dags rtags can* ("deer-marked", the moon) is rendered by the lock as plain "चन्द्रमा" (the moon). Nothing is wrong, and it avoids Gendun Drub's hare vs the root's deer; if the image is wanted, "शशाङ्क" (hare-marked, a standard Sanskrit moon name) fits him.
- 1-19: "नराम्रो सपना" (bad dream) is everyday; "दुःस्वप्न" is the liturgical word. The "armour of joy" he reads as the peaceful and wrathful mantras held with a joyful, one-pointed mind; "कवचको आनन्दमय तेज" (the joyful splendour of the armour) is the literal reading.
- 1-21 and 2-5: "ग्रह" for *gdon* (locked). It is the exact Sanskrit (*graha*, "seizer") and sits among spirits at 1-21 ("ग्रह, वेताल र यक्ष"). At 2-5, "ग्रह, महामारी र विष" could be read as "planets". Kept per Tenkal's decision; the native reader should confirm most readers take the spirit sense (the word list cites ग्रह लाग्नु, "to be seized by a graha").
- 1-21: "परम उत्तम" (supreme, best) doubles *rab mchog*; harmless.
- 1-22: "यो स्तुति र, / एक्काइस वन्दनाहरू।" (this praise and, / the twenty-one homages.) ends as a fragment with a full stop. 2-1 picks the text up again, so this is harmless.

**Result: 13/22 clean, 0 verse(s) with errors, 9 with mismatches only (1-1, 1-2, 1-3, 1-4, 1-9, 1-10, 1-14, 1-19, 1-21); 11 mismatch row(s).**

#### Chapter 2 — verses 2-1 to 2-6

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | Nepali (+ English gloss) | Fix |
|---|---|---|---|---|---|
| 2-4 | MISMATCH | དེ་ཡི་དུག་ནི་དྲག་པོ་ཆེན་པོ། བརྟན་གནས་པ (de yi dug ni drag po chen po / brtan gnas pa) | (in the 2-3 bucket) "the poison that obstructs **that** buddhahood — the great fierce one — is wrong view"; the "stationary" poisons are denigrating the Dharma through ignorance and hating the Dharma and its teachers. Only then come moving poisons (rabid dogs, snakes) and food-and-drink poisons | "त्यो भयंकर महा विष, / स्थावर होस् वा जङ्गम," (that terrible great poison, / whether stationary or moving) | Translator's call. Gendun Drub reads *de yi* as referring back to buddhahood, and the first two lines as spiritual poisons. The Nepali, like the English, reads them as physical poisons, and the root allows this. "त्यो" (that) renders *de yi* as a plain demonstrative ("that poison", not "the poison of that"). Leave |
| 2-6 | MISMATCH | བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག (bgegs rnams med cing so sor 'joms 'gyur cig) | Pang Lotsawa, cited: "obstacles cannot hinder it; there are no obstructors, and each antidote destroys (*'joms par 'gyur*) each thing to be abandoned" — indicative | "विघ्नहरू नरहून् र एक-एक गरी नष्ट होऊन्" (**may** obstacles not remain, and may they be destroyed one by one) | Translator decision (settled: optative, following our root's *'gyur cig*). Gendun Drub's source reads it as a statement. *so sor* ("each individually") is kept as "एक-एक गरी" (one by one). Leave |

Readings that **support** the current Nepali:
- 2-1: *lha mo* = "the goddess Tārā" → "देवीप्रति" (towards the goddess). *gus pa yang dag ldan* = endowed with genuine respect, not lip service → "पूर्ण रूपले भक्तिले युक्त" (fully endowed with devotion). *blo ldan* = one with a one-pointed, wise mind → "बुद्धिमान" (the wise one).
- 2-2: rising "from bed" at dusk **and** dawn → "साँझ र बिहान उठेर" (rising at evening and morning) — both sessions, joined by "र" (and). "by **merely** recollecting (*dran pa tsam gyis*)" her body, mantra and praise → "उहाँको स्मरण गर्नाले" (by recollecting her) — the draft 4 fix, with no added "always". *mi 'jigs thams cad* → "सम्पूर्ण अभय" (all fearlessness). *sdig pa* = the causes of lower rebirth → "सम्पूर्ण पापहरू" (all sins). *ngan 'gro* = the lower realms as result → "सम्पूर्ण दुर्गतिहरू" (all lower destinies).
- 2-3: *bye ba phrag bdun* → "सात करोड" (seven crore = seventy million) is the right number. *rgyal ba* → "बुद्धहरू" (buddhas), Tenkal's decision for the Hindi. The recipient is the practitioner, in this very life → "चाँडै अभिषेक दिइनेछ" (empowerment will swiftly be given). *'di las che ba* = the common great siddhis → "यसभन्दा पनि महानता" (greatness even beyond this). The supreme siddhi, final buddhahood → "अन्तिम बुद्ध पदमा पुग्नेछ" (will reach the final state of buddhahood), singular.
- 2-4: moving poisons = rabid dogs and snakes → "जङ्गम" (moving). Eaten and drunk = food and drink poisons → "खाएको र पिएको भए तापनि" (even if eaten and drunk). "by merely recollecting" her → "उहाँको स्मरण गर्नाले पूर्ण रूपले हट्नेछ" (will be completely removed by recollecting her).
- 2-5: *gdon* → "ग्रह" (graha), *rims* → "महामारी" (epidemic), *dug* → "विष" (poison). "अन्य प्राणीहरूका लागि पनि त्यस्तै हुनेछ।" (and so it will be for other beings too.) closes the sentence, matching his "other-benefit … one obtains the benefits as above". It does not run into 2-6.
- 2-6: the numbers "दुई, तीन, सात पटक" (two, three, seven times) are kept as numbers with no added "or", so all three of his readings fit. *mngon par brjod* → "स्पष्ट रूपले पाठ" (clear recitation). *bu* → "पुत्र" (son), as in his reading; wealth → "धनहरू नै" (wealth itself).

Style notes (not errors; the grammar points are for the native reader):
- 2-1 grammar: "जुन बुद्धिमानले राम्ररी पाठ गर्नाले," (by whichever wise one's reciting well) stacks two instrumentals and the *जुन* ("whoever") clause never gets its partner (*उसले* / *उसलाई*). E.g. "जुन बुद्धिमान्‌ले राम्ररी पाठ गर्छ," (whichever wise one recites well). "राम्ररी" (well) for *rab tu brjod*, which he glosses "recites with great faith" (*rab tu dad pas*); "श्रद्धापूर्वक" (with faith) is closer.
- 2-2 grammar: "सम्पूर्ण पापहरू पूर्ण रूपले शान्त हुन्छ" — plural subject, singular verb; "शान्त हुन्छन्". "सम्पूर्ण अभय राम्ररी प्रदान गर्छ" (grants all fearlessness) has no clear subject, and the plain *गर्छ* does not match the honorific *उहाँको* (her) if Tārā is the giver; "प्रदान गर्नुहुन्छ" (she grants) would keep the giver the Tibetan and the commentary have. "बिहान" (morning) for *tho rangs* (dawn); "बिहानै" / "प्रातःकाल" is a shade closer.
- 2-5 grammar: "ग्रह, महामारी र विषद्वारा पीडित भएको, / सम्पूर्ण दुःखका समूहहरू … हटाइनेछ" makes the sufferings "afflicted", not the people, and joins a plural subject to a singular verb. "सम्पूर्ण" (all) is also not in the root. E.g. "ग्रह, महामारी र विषले पीडित हुनेहरूका / दुःखका समूहहरू पूर्ण रूपले हट्नेछन्," (for those afflicted by grahas, epidemics and poisons, the masses of suffering will be completely removed). The Hindi needed the same fix.
- 2-6 grammar: "सम्पूर्ण इच्छाहरू प्राप्त हुनेछ" — plural subject, singular verb; "प्राप्त हुनेछन्".

**Result: 4/6 clean, 0 verse(s) with errors, 2 with mismatches only (2-4, 2-6); 2 mismatch row(s).**

#### Second pass — doctrinal-category swaps, named entities, numbers

- **Kāya / dharma / mind:** GD calls 1-15 the praise "by way of the dharmakāya" (the heading), but the verse's words (*bde ma … sdig pa chen po*) contain no *sku*. No kāya term appears in the Nepali, and none is collapsed. Nothing added.
- **Named entities:** Avalokiteśvara as "तीन लोकका नाथ" (Lord of the three worlds, 1-1) fits. Indra, Agni, Brahmā, Vāyu (1-6) are all present and in the root's order. The bodhisattvas as "बोधिसत्त्व" (1-4) fit. Amitābha (1-12) fits, with Tārā as the one who spreads the light, as he reads it. Meru, Mandara, Vindhya (1-17) are right, and she is the one who shakes them (grammar note above). The kinnaras (1-19) fit; the kings serve her, but the wording needs care (row above). The 1-18 moon carries no animal, so Gendun Drub's hare does not clash. "ग्रह" for *gdon* (1-21, 2-5) is a register point, not a wrong entity (style note).
- **Numbers:** a hundred moons, thousands of stars (1-2); seven worlds (1-5); seven levels (1-14); ten-syllable (1-16); three worlds (1-17); twenty-one (1-22); seven crore = seventy million (2-3); two, three, seven (2-6). All correct. One number point: "तथागतको" (of the Tathāgata, 1-4) reads as singular where he has "all the tathāgatas" (row above).
- **Scope words:** no added "all" at 1-10 (the Hindi had one). "सम्पूर्ण" (all) is added at 2-5 (style note). "सम्पूर्ण शत्रुहरूलाई अशेष" (1-8) mirrors the root's *thams cad ma lus*. No added "always" at 2-2 or 2-4. Nothing further added.

**Overall: 29 verses checked — 18 clean, 0 with errors, 11 with mismatches only.**
