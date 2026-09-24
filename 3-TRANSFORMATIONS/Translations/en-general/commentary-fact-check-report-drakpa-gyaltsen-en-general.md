## Praise to the Twenty-One Taras — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/New raw data/bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md` — Jetsün Drakpa Gyaltsen (1147–1216), *gsal ba'i 'od zer*
- **Translation audited:** `3-TRANSFORMATIONS/Translations/en-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general.md` (general grade, second draft)

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

Extraction notes: 30 transclusions, no empty buckets, no cascading shift (each
bucket's prose discusses the verse it is labelled with; the trailing `^N-M` ids
inside the passages are the commentary's own paragraph numbering). Not covered by
this commentary: I-1, I-2 (the Sanskrit and Tibetan title lines).
`extract_translation.py` could not be used as-is: in this vault's transclusion
layout it captures only the last line of each multi-line verse, so full verse text
was read from the grade file's `en_text` instead.

### Progress

| Scope checked |
|---|
| 2026-09-24 — I-3, 1-1 to 1-22, 2-1 to 2-6, a-1 (all 30 verses this commentary covers) |

#### Chapter I — verse I-3

No anchored terms beyond the root line itself (the commentary repeats it). Clean.

**Result: 1/1 clean, 0 errors, 0 notes.**

#### Chapter 1 — verses 1-1 to 1-22

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-1 | ⚠ ERROR | ཆུ་སྐྱེས་ཞལ་གྱི (chu skyes zhal gyi) | "the lotus or utpala that arose from his tears" (*de'i spyan chab las byung ba'i pad ma'am utpala*) — "his" = Avalokiteśvara, the Lord of the Three Worlds | "the opening stamens of the lotus face / Of the Lord of the Three Worlds" | English makes his face the lotus; commentary: an actual lotus born from his tears. e.g. "Born from the opening stamens of the lotus / That arose from the face of the Lord of the Three Worlds". Touches locked term `lotus_face` (right at 1-8, not here) — judgment call |
| 1-3 | ⚠ ERROR | དཀའ་ཐུབ (dka' thub) | "*dka' thub* is ethical discipline" (*tshul khrims*) — one of the six perfections | "austerity" | "discipline" |
| 1-3 | MISMATCH | སྤྱོད་ཡུལ་ཉིད་མ (spyod yul nyid ma) | "is wisdom (*shes rab*)" — the sixth perfection; by practising the six, Tārā's body is attained | "She whose sphere of activity is …" (a frame for the list; wisdom never named) | Judgment: literal line vs the commentary's six-perfection count |
| 1-3 | MISMATCH | གསེར་སྔོ (gser sngo) | "a colour bright like the light of refined gold" | "gold and blue" | "blue" not supported by this commentary — judgment |
| 1-5 | MISMATCH | ཕྱོགས / ནམ་མཁའ (phyogs / nam mkha') | with *'dod* (desire realm): "the form realm" and "the formless realm" | "the directions, and space" | Literal rendering kept; commentary reads them as the three realms — judgment |
| 1-6 | ⚠ ERROR | དབང་ཕྱུག (dbang phyug) | "Maheśvara (*dbang phyug chen po*), who is the lord over them" — one figure | "the various Īśvaras" (plural) | Singular: e.g. "and Īśvara, lord of them all" |
| 1-8 | ⚠ ERROR | འཇིགས་པ་ཆེན་མོ ('jigs pa chen mo) | "because she terrifies the māras (*bdud skrag par byed pas*) she is the Great Terrifying One" | "the Great Fearful One" | "Fearful" reads as "afraid" — she causes fear. → "the Great Terrifying One" |
| 1-8 | MISMATCH | ཏུ་རེ (tu re) | instrument: "by the terror of TURE she dispels all māras" (*tu re'i 'jigs pas*) | "Homage to ture," (ture as the one addressed) | Judgment — restructuring the line |
| 1-8 | MISMATCH | བདུད་ཀྱི་དཔའ་བོ (bdud kyi dpa' bo) | "the hero is the māra of the afflictions; defeating it, the other three are defeated along the way" | "the champions of Mara" (plural warriors) | Judgment |
| 1-9 | MISMATCH | མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས་བརྒྱན (ma lus phyogs kyi 'khor los brgyan) | "the palm of the right hand, in the supreme-giving gesture, is adorned with a wheel" | "Adorned with wheels in every direction" | Number, and what is adorned (her palm) — judgment |
| 1-10 | MISMATCH | རབ་ཏུ་དགའ་བ (rab tu dga' ba) | "fulfilling the wishes of all [supremely] joyful beings" | "whose majestic and supreme joy" (joy is hers) | Whose joy — judgment |
| 1-15 | MISMATCH | སྭཱ་ཧཱ་ཨོཾ (svāhā oṃ) | order: svāhā, then oṃ (commentary quotes the same) | "OṂ and SVĀHĀ" | Order reversed. Easy to fix if wanted |
| 1-16 | ⚠ ERROR | རིག་པ་ཧཱུཾ (rig pa hūṃ) | the knowledge-mantra (vidyā) with HŪṂ — commentary gives it: *oṃ namaḥ tāre namo hari hūṃ hara svāhā*, "the wrathful mantra" | "the hum of awareness" | "awareness" names a different thing → e.g. "the knowledge-mantra hum". (Commentary's copy reads *sgrol ma* "liberator" where our root has *sgron ma* "lamp" — a textual variant, not flagged) |
| 1-17 | ⚠ ERROR | འབིགས་བྱེད ('bigs byed) | a verb: "Meru and the one called Mandāra are pierced by the rays of the syllable HŪṂ" | "Mount Meru, Mandara, and Vindhya" (a third mountain) | Per this commentary there is no Vindhya. *'bigs byed* is also Vindhya's Tibetan name, and other commentaries may read it that way — compare before fixing (judgment) |
| 1-19 | ⚠ ERROR | ལྷ་ཡི་ཚོགས་རྣམས་རྒྱལ་པོ (lha yi tshogs rnams rgyal po) | "[these two lines:] the lords of those hosts of gods, and the kinnara king Druma etc., make offerings at her feet" | "Homage to the sovereign of the hosts of gods, / Whom gods and kinnaras rely upon" | Who does what is reversed — she is served by the kings; she is not the sovereign. e.g. "Homage to you, served by the kings of the hosts of gods, / By gods and kinnaras" |
| 1-21 | MISMATCH | དེ་ཉིད་གསུམ་རྣམས་བཀོད་པ (de nyid gsum rnams bkod pa) | "oṃ āḥ hūṃ set at body, speech and mind" | "Established by the three suchnesses" | The three are set on her (she is not "established by" them), and the phrase is opaque at general grade — judgment |
| 1-22 | MISMATCH | བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ཉི་ཤུ་རྩ་གཅིག (bstod pa 'di dang / phyag 'tshal ba nyi shu rtsa gcig) | "this praise of the peaceful and wrathful [mantras] is itself the praise by twenty-one homages" | "this praise of the root mantra, / And these twenty-one homages" (two items) | The commentary treats them as one praise; the root has *dang* — judgment |

Style / softening notes on otherwise-clean verses (not errors):
- 1-2 སྟོང་ཕྲག (stong phrag) = "thousands"; English "a thousand".
- 1-6 མདུན་ནས (mdun nas) "from before" reads as time; "before her / in her presence".
- 1-8, 1-19 switch between "her / who" and "your" mid-verse.
- 1-9 "turbulent" — commentary: her light outshines other lights (*zil gyis gnon*).
- 1-14 commentary: her left hand strikes the ground (singular); English "the palms of your hands".
- 1-19 རྩོད (rtsod) = disputes raised by non-Buddhist opponents (*mu stegs*); English "conflicts".

**Result: 9/22 clean, 7 verses with errors (1-1, 1-3, 1-6, 1-8, 1-16, 1-17, 1-19), 6 with mismatches only (1-5, 1-9, 1-10, 1-15, 1-21, 1-22); 10 mismatch rows in all, 6 style notes.**

#### Chapter 2 — verses 2-1 to 2-6

All anchored terms match (devotion of body, speech and mind; wrathful form recalled
at dusk and peaceful at dawn; seventy million Victors; stationary and moving poisons;
suffering of cause and result; the supreme and common siddhis; obstacles each
overcome by its antidote).

**Result: 6/6 clean, 0 errors.**

#### Colophon — a-1

Clean. The commentary names the Buddha who spoke the praise as Mahāvairocana
(*rnam par snang mdzad chen po*); the root doesn't, so that detail isn't flagged.

**Result: 1/1 clean, 0 errors.**

#### Termbase notes (found during the audit, outside the commentary's scope)

- 1-12 "supreme light" renders ཤིན་ཏུ (shin tu, "intensely"), but `supreme` is locked to རབ (rab).
- 1-21 "power of peace" renders མཐུ (mthu). The termbase's own note says མཐུ ("might") is kept distinct from དབང ("power"), but the grade file lists `power` at 1-21.

**Overall: 30 verses checked — 17 clean, 7 with errors, 6 with mismatches only.**
