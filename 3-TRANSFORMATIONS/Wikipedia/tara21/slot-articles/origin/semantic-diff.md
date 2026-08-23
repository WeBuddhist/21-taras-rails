---
topic: origin
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/origin/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — origin

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Origin story of Tara, some 21-praise commentaries give it a special outline | same | YES | connective སྟེ→དེ།, sentence split only |
| 2 | Long ago under Buddha Dundubhisvara, princess Yeshe Dawa vowed bodhicitta in a woman's body, was renamed Tara, prophesied to keep that name until Dundubhisvara's own enlightenment | same | YES | connective/particle changes only (ནས→དེ།, ཏེ→ཤིང་།) |
| 3 | Geshe Lobzang Dawa gives two etymologies of the name (swift-acting heroine; all-seeing) from the origin-story section; other three commentaries omit this | same | YES | སྐད་ཅིག་གི→སྐད་ཅིག་ལ, མི་→མ་ (negation variant), added clarifying འདི་ནི — no fact change |
| 4 | Sungrab Tulku appends benefit teachings after the summary: reciting morning/evening grants fearlessness, pacifies misdeeds, destroys bad rebirth; prayer at any time protects from 8/16 fears and grants worldly/ultimate aims via 2/3/7 recitations; other commentaries omit this | same | YES | verb-form variants (སྣོན→བསྣན), sentence splits, added བཞུགས (honorific copula) — same claim, no new fact |
| 5 | 3 of 4 commentaries give the origin story a distinct outline heading; Sungrab Tulku names it directly, Khenpo Tsultrim Namdak makes it its own section, Geshe Tenzin Dhonzang folds it into his own opening | same | YES | ལ→ removed, minor case particle change, no fact change |
| 6 | Yeshe Dawa/Dundubhisvara story: worshipped Buddha's retinue for years, first generated bodhicitta, vowed to work for beings in a woman's body, attained acceptance of non-arising, was renamed Tara, prophesied to keep the name Tara until Dundubhisvara's own buddhahood | same | YES | word-order variants (སེམས་དང་པོར་བསྐྱེད→ཐོག་མར་སེམས་བསྐྱེད), sentence splits, no fact change |
| 7 | Geshe Lobzang Dawa: born from a lotus in Avalokiteshvara's eye; Khenpo Tsultrim Namdak (differing): born from Avalokiteshvara's tears; Buddha told Manjushri Tara is mother of all buddhas and taught this praise; Khenpo adds a third origin story (vow before Buddha Amoghasiddhi to protect beings); the three accounts don't preclude/contradict each other and none links itself to the other two — each is a distinct commentarial feature | same | YES (see flagged substitution) | see below — མི་ཁེགས→མི་འགལ flagged as lexical substitution |
| 8 | Geshe Tenzin Dhonzang alone gives the spread-in-Jambudvipa account per Taranatha: Avalokiteshvara taught countless Tara mantra-tantras in this aeon, re-taught by the Teacher himself and also in the Dakini Guhyatilaka Tantra; transmitted like the three sutra councils; upheld at Nalanda and Tibet's four great traditions via explanation and practice, all took Tara as yidam; resolves the Vajradhara/Vajrapani-as-compiler identity question by identifying Vajrapani as Samantabhadra, so teacher and compiler are not different tantras; supported also by the reasoning that Ananda alone could not have held the 84,000 dharma-heaps in one hearing (so the true compiler is Vajrapani/Samantabhadra, not Ananda) | same | YES (see flagged substitutions) | ཡིད་དམ→ཡི་དམ spelling normalization; རྒྱུད་གཞན་དུ་མེད→རྒྱུད་ཐ་དད་དུ་མེད flagged; ངོས་འཛིན→ངོས་བཟུང verb-form variant, no fact change |
| 9 | On who urged Yeshe Dawa to be reborn male: Sungrab Tulku says bodhisattvas and shravakas; Khenpo Tsultrim Namdak differs, says monks; Geshe Tenzin Dhonzang doesn't say who, just notes the vow briefly | same | YES | punctuation only |
| 10 | On the name of the samadhi: Sungrab Tulku names it "liberating beings from samsara"; Tenzin Dhonzang and Tsultrim Namdak both name it "liberating all beings" — different wording | same | YES | identical wording, punctuation only |
| 11 | On enjoying desire objects while meditating: Sungrab Tulku has her skillfully enjoy all five distinct sense qualities; Tsultrim Namdak has skillful enjoyment of desire qualities but doesn't itemize the five; Tenzin Dhonzang states only that she attained acceptance, no meditation detail | same | YES | punctuation only |
| 12 | On the scope of the prophecy: Sungrab Tulku and Tenzin Dhonzang say it concerns the name alone; Tsultrim Namdak adds that it also concerns taking a female body as support throughout the path and even after buddhahood | same | YES | concessive shifted from ཀྱང→ འོན་ཀྱང་ at clause boundary; ཙམ་མིན་པར→ཙམ་དུ་མ་ཟད rephrase, same meaning |
| 13 | On whether the 21 Taras are one or separate: Tenzin Dhonzang's own text gives two views without naming holders — (a) all 21 are emanations of Khadiravani Tara, (b) all 21 are 21 different types; he himself doesn't settle either view, considers either compatible (surrounded by 21 emanations, or all others gathered into Khadiravani) — either way, similar dependent-origination of being upheld by all 21 together | same after reversion | YES (after reversion) | see Reverted drift below |
| 14 | Summary: some 21-praise commentaries give the origin story its own outline — princess Yeshe Dawa vowed before Dundubhisvara to act for beings in a woman's body, attained samadhi, was named Tara; other origin accounts (from Avalokiteshvara) and the tantra-lineage account are appended by some commentaries | same | YES | verb variant སྣོན→བསྣན, punctuation only |

## Ref attachment walk

All 56 `<ref>` tokens were checked against the statement they sit on in both before/after texts.

- `sungrab-tulku` (first def. + repeats): every occurrence still closes the exact clause it closed before (origin-story frame, benefit teachings, both origin narratives, urging-to-rebirth, samadhi-name, five-qualities enjoyment, prophecy scope, summary) — YES, unchanged attachment throughout.
- `tenzin-dhonzang` (first def. + repeats): still attached to the same statements (origin-story frame, section-placement claim, both origin narratives, Jambudvipa spread account and all its sub-claims, samadhi-name, prophecy scope, the two-views passage, summary) — YES.
- `tsultrim-namdak` (first def. + repeats): still attached to the same statements (origin-story frame, section-placement claim, both origin narratives, Avalokiteshvara-tears narrative, Manjushri teaching, third origin story, urging-to-rebirth, five-qualities enjoyment, prophecy-scope addendum) — YES.
- `lobsang-dawa` (first def. + repeats): still attached to the two etymologies and the lotus-birth narrative — YES.

No ref migrated to a different clause; no ref dropped or duplicated onto a new claim.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — listed for domain-expert acceptance, do not block PASS:

| Before | After | Context |
|---|---|---|
| ཐུན་མོང་མིན་པའི་... སྒོས་སུ་ཕྱེ | ཐུན་མོང་མ་ཡིན་པའི་... ཟུར་དུ་ཕྱེ | negation/spelling + "separately" synonym |
| སྐད་ཅིག་གི་ནམ་མཁའི་གློག | སྐད་ཅིག་ལ་ནམ་མཁའི་གློག (+ སྤྱན་གྱིས) | grammar-particle rephrase of "wisdom eye sees in an instant" |
| མི་ཁེགས (three origin accounts do not "block/exclude" each other) | མི་འགལ (do not "contradict" each other) | verb substitution, same overall claim (accounts are mutually compatible) |
| ཡིད་དམ | ཡི་དམ | spelling normalization of "yidam" |
| རྒྱུད་གཞན་དུ་མེད་པར | རྒྱུད་ཐ་དད་དུ་མེད་པར | "not another tantra" → "not a different/separate tantra" — synonym |
| ངོས་འཛིན་ནས | ངོས་བཟུང་ནས | verb-form variant of "identified/recognized as" |
| སྣོན / སྤྱོད | བསྣན | verb-form variants of "to append/add" |
| གཏན་ལ་མ་ཕབ་པར (unsettled) vs མ་གཏན་ལ་འབེབས་པར | both idiom variants of "not settling on" | grammar-form variant of the same idiom |

## Reverted drift

**Line (paragraph on whether the 21 Taras are one or separate):**

- Before: `སྒྲོལ་མ་ཉེར་གཅིག་གཅིག་ཏུ་གྱུར་པའམ་སོ་སོར་ཡོད་པའི་དྲི་བར` — "regarding the question of whether the 21 Taras became one, or exist separately"
- Gemini's draft: `སྒྲོལ་མ་ཉེར་གཅིག་ངོ་བོ་གཅིག་ཏུ་གྱུར་པའམ་སོ་སོར་ཡོད་པའི་དོགས་གནས་ལ` — inserted **ངོ་བོ** ("in essence/nature"), narrowing the plain "became one" into the specific philosophical claim "became one *in essence*"

This is exactly the doctrinal ambiguity this paragraph goes on to discuss (the source's own two-views passage never resolves *what kind* of "one" is meant). Adding "ngo bo" prejudges that ambiguity with a technical term not present in the source article. Per Rule 8(a), this span was surgically reverted in `article.md` to the source's exact wording (`སྒྲོལ་མ་ཉེར་གཅིག་གཅིག་ཏུ་གྱུར་པའམ`), keeping Gemini's other, unrelated improvements to this sentence (the `དྲི་བ→དོགས་གནས` synonym swap and the added sentence-final punctuation) untouched. `body-after.txt` is left as the unedited raw model record per Rule 8(a).

## Verdict

**PASS-after-reversion.** Aside from the one reverted span (an inserted technical qualifier on a live doctrinal ambiguity), no fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator; every `<ref>` remains attached to the exact statement it supported before; all "..." verbatim quotations are character-for-character identical; no honorific was inserted before any personal name (Sungrab Tulku, Tenzin Dhonzang, Tsultrim Namdak, Lobsang Dawa all appear exactly as in the source, with no titles added or removed).
