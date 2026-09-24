# Keyword route comparison — A (English-mediated) vs B (Gemini on Tibetan)

- **A** `/Users/tashitsering/Desktop/work/Obsidian/21-taras-rails/2-RAILS/Keywords/source-term-registry.json` — `keyword-extract`, restricted to the 345 terms that occur in this root text (the only population both routes could see).
- **B** `0-INBOX/temp/keyword-extraction/gemini-direct-2026-09-22/gemini-terms.json` — `gemini-keyword-extract`, model `gemini-3.1-pro-preview`, 32 blocks in batches of 5.

Neither route is ground truth. This report says where they agree and what each sees alone; it does not score one against the other.

## Totals

| | count |
|---|---|
| A terms (in this text) | 345 |
| B terms | 208 |
| found by both | 154 |
| only A | 191 |
| only B | 54 |
| A's top 50 by rank, also found by B | 46/50 |

Matching is on the tsheg/shad/anusvara-normalised Tibetan string: the two routes hold terms in different citation conventions (A's lemmas end in a shad, B copies the running form), so raw-string comparison would report near-total disagreement and mean nothing.

## B's self-verification

Every term B returned was checked against the block it was attributed to:

| grade | count | meaning |
|---|---|---|
| VERBATIM | 282 | the exact string is in that block |
| NORMALIZED | 5 | present after normalisation — a citation form |
| ABSENT | 0 | not in the block — paraphrase, conflation or invention |

## Provenance agreement (terms both routes found)

| | count |
|---|---|
| identical block set | 99 |
| different block set | 55 |
| A recorded no blocks | 0 |

## Highest-ranked A terms that B did not find

A's rank is the composite score (claim density / structure / presence). A miss high in this list matters more than a long tail of misses.

| A rank | lemma | glosses |
|---|---|---|
| 29 | འཇིགས་པ། | terrifier |
| 31 | སྔོ། | blue |
| 39 | གསེར། | golden |
| 49 | གཡོན། | leave, left |
| 51 | གཡས། | right |
| 63 | ཡི་གེ་བཅུ་པའི། | syllables |
| 86 | རལ་པའི། | hair, matted |
| 89 | ཞི་བའི། | peace |
| 91 | གཡོ་བ། | tremble |
| 96 | སྤྱན་གཉིས་པོ། | eyes |
| 97 | རྒྱལ་བའི། | victorious |
| 98 | ངན་པ། | bad |
| 106 | བརྒྱ། | hundred |
| 107 | དབང་ཕྱུག། | ishvaras |
| 109 | ཏཱ་ར་གཉིས་བརྗོད། | pronounce tara |
| 110 | བདུན། | seventy |
| 111 | འགུགས་པ། | summon |
| 112 | ཕ་རོལ། | adversaries |
| 113 | རབ་ཏུ་དགའ་བ། | exceedingly joyful |
| 115 | དུག་རྣམས། | poisons |
| 121 | ཞི། | peace |
| 127 | ཏུ་རེ་རབ་མཆོག། | supreme ture |
| 129 | འབར་བའི་ཕྲེང་བ། | blaze garland |
| 138 | དགྲ་ཡི། | enemies |
| 139 | ཟླ་བའི་རྩེ་མོ། | crescent |

## Terms B found that A does not have

| term | gloss | kind | blocks | verification |
|---|---|---|---|---|
| གནོད་སྦྱིན་ཚོགས་ | host of yakshas | being-class | 1-21 | VERBATIM |
| གཡས་བརྐྱང་ | right leg extended | action | 1-13 | VERBATIM |
| གཡས་བསྐུམ་ | right leg drawn | action | 1-7 | VERBATIM |
| གཡོན་བརྐྱང་ | left leg extended | action | 1-7 | VERBATIM |
| གཡོན་བསྐུམ་ | left leg bent | action | 1-13 | VERBATIM |
| གསེར་སྔོ་ | golden blue | quality | 1-3 | VERBATIM |
| གུས་ | devotion | quality | 2-1 | VERBATIM |
| དགའ་བའི་བརྗིད་ | joyful splendor | quality | 1-19 | VERBATIM |
| དགྲ་ཡི་དཔུང་ | enemy forces | being-class | 1-13 | VERBATIM |
| དགྲ་ཡི་ལུས་ | enemy's body | object | 1-16 | VERBATIM |
| དབུ་བརྒྱན | crown ornament | object | 1-12 | VERBATIM |
| དབུས་ | center | place | 1-13 | VERBATIM |
| དེ་ཉིད་ | reality / suchness | doctrinal | 1-21 | VERBATIM |
| དྲག་པོ་ཆེན་པོ | great fierce | quality | 2-4 | VERBATIM |
| དྲག་པོའི་རིམས་ | fierce plague | doctrinal | 1-20 | VERBATIM |
| དྲན་ | mindfulness, remembering | action | 2-2, 2-4 | VERBATIM |
| ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ | Praise to 21 Taras | object | I-1 | VERBATIM |
| བགེགས་རྣམས་ | hindrances | being-class | 2-6 | VERBATIM |
| བདུད་ཀྱི་དཔའ་བོ་ | Mara's warriors | being-class | 1-8 | VERBATIM |
| བརྟན་གནས་ | stationary | quality | 2-4 | VERBATIM |
| བསྐལ་པ་ཐ་མའི་མེ་ | apocalyptic fire | doctrinal | 1-13 | VERBATIM |
| བསྐུར་ | bestow | action | 2-3 | VERBATIM |
| མཆོག་ | supreme | quality | 1-21 | VERBATIM |
| ཞལ་མ | She with a face | epithet | 1-2 | VERBATIM |
| ཞི་བའི་མཐུ་ | power of peace | quality | 1-21 | VERBATIM |
| འཇིག་རྟེན་གསུམ་མགོན་ | Protector of Three Worlds | epithet | 1-1 | VERBATIM |
| འཇིགས་པ་ཆེན་མོ | great terrifying one | epithet | 1-8 | VERBATIM |
| འདོད་པ་ཐམས་ཅད་ | all desires | doctrinal | 2-6 | VERBATIM |
| འོད་ཀྱི་ཕྲེང་བ་ | garland of light | object | 1-10 | VERBATIM |
| འོད་ཀྱི་ཚོགས་ | mass of light | object | 1-9 | VERBATIM |
| ཡི་གེ་བཅུ་ | ten syllables | doctrinal | 1-16 | VERBATIM |
| ཡི་གེ་བཅུ་པའི་ངག་ | ten-syllable mantra | doctrinal | 1-16 | VERBATIM |
| རལ་པ | matted hair | object | 1-12 | VERBATIM |
| རིག་པ་ | awareness | doctrinal | 1-16 | VERBATIM |
| རི་དགས་ | deer | being-class | 1-18 | VERBATIM |
| རིམ་པ་བདུན་ | seven levels | doctrinal | 1-14 | VERBATIM |
| རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་ | seven ten-millions of Victors | deity | 2-3 | VERBATIM |
| རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ | Noble Reverend Tara | deity | I-3 | VERBATIM |
| རྣམ་པར་རྒྱལ་བ | complete victory | doctrinal | 1-4 | VERBATIM |
| རྨི་ལམ་ངན་པ་ | bad dream | object | 1-19 | VERBATIM |
| རྩ་བའི་སྔགས་ | root mantra | doctrinal | 1-22 | VERBATIM |
| རྩེ་མོ | tip / point | object | 1-12 | VERBATIM |
| ལྷ་ཡི་མཚོ་ | divine lake | object | 1-18 | VERBATIM |
| ལྷ་ཡི་ཚོགས་ | assembly of gods | being-class | 1-19 | VERBATIM |
| ས་གཞིའི་ངོས་ | surface of the earth | place | 1-14 | VERBATIM |
| ས་གཞི་སྐྱོང་བ | earth protectors | being-class | 1-11 | VERBATIM |
| སངས་རྒྱས་གོ་འཕང་ | state of Buddhahood | doctrinal | 2-3 | VERBATIM |
| སྐར་མ་སྟོང་ཕྲག་ | Thousands of stars | object | 1-2 | VERBATIM |
| སྡིག་པ་ཆེན་པོ་ | great sin | doctrinal | 1-15 | VERBATIM |
| སྡུག་བསྔལ་ཚོགས་ | mass of suffering | doctrinal | 2-5 | VERBATIM |
| སྣ་ཚོགས་དབང་ཕྱུག་ | Vishveshvara | deity | 1-6 | VERBATIM |
| སྤོང་ | abandon | action | 2-5 | VERBATIM |
| སྤྱན་གཉིས་ | two eyes | object | 1-20 | VERBATIM |
| ཨོཾ | Om | mantra | 1-15, I-3 | VERBATIM |
