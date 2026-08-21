---
type: review-view
canonical_sources:
  - published.yaml
checked: 2026-08-21
---

# Published articles — tara21

> [!warning] Check this before publishing anything.
> A slot listed under **Live on bo.wikipedia** already exists on the wiki. Republishing it
> creates a duplicate article. Update it at its existing title instead — the page ID is the
> stable handle. Titles under **Not yet published** are reserved for their slot.

> [!note] Obsidian-readable view of [published.yaml](published.yaml). That file is canonical;
> regenerate this view after any change rather than editing it here.

**5 live · 18 not yet published · 10 awaiting a title decision** (as of 2026-08-21)

## Live on bo.wikipedia

| Slot | Title | Page ID | Repo file | Published |
|---|---|---|---|---|
| `origin` | [སྒྲོལ་མའི་ལོ་རྒྱུས།](https://bo.wikipedia.org/w/index.php?curid=28182) | 28182 | [article.md](slot-articles/origin/article.md) | 2026-08-21 |
| `structure-benefits` | [ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པ།](https://bo.wikipedia.org/w/index.php?curid=28183) | 28183 | [article.md](slot-articles/structure-benefits/article.md) | 2026-08-21 |
| `tara-01` | [སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ།](https://bo.wikipedia.org/w/index.php?curid=28184) | 28184 | [article.md](slot-articles/tara-01/article.md) | 2026-08-21 |
| `tara-02` | [སྒྲོལ་མ་བློ་གཏེར་དབྱངས་ཅན་མ།](https://bo.wikipedia.org/w/index.php?curid=28185) ⚑ | 28185 | [article.md](slot-articles/tara-02/article.md) | 2026-08-21 |
| `tara-03` | [སྒྲོལ་མ་གསེར་མདོག་ཅན།](https://bo.wikipedia.org/w/index.php?curid=28186) | 28186 | [article.md](slot-articles/tara-03/article.md) | 2026-08-21 |

⚑ **tara-02** — Source lead term is བློ་གཏེར་དབྱངས་ཅན་མ; the published title prefixes སྒྲོལ་མ་ for series consistency with tara-01/03. Either special-case this slot in any title-deriving tooling or amend the lead term in the source file.

## Title convention

- **Slot articles.** A Tārā slot article is titled with the deity's epithet prefixed by སྒྲོལ་མ་ — སྒྲོལ་མ་<epithet>། — so that the 21 titles form one visibly consistent series and each reads as the name of a deity rather than as a line of the praise. Established by the first three published (tara-01/02/03).
- **Subject articles.** Subject articles (origin, structure-benefits) take a plain descriptive Tibetan title; the སྒྲོལ་མ་ prefix rule does not apply to them.
- **Where the epithet comes from.** The epithet must be one attested in the commentaries and named in the article's own མཚན་གྱི་ངེས་ཚིག section — never invented, never taken from parametric knowledge. Where the commentaries disagree on the name (they do for most slots), the choice among attested candidates is a human editorial decision, recorded per slot below.
- **Do not derive the title from the lead bold term.** The title is NOT auto-derivable from the article's first bolded term. In most slot articles that term is the opening line of the root verse (ཕྱག་འཚལ་…), not a name; in tara-02 the published title adds the སྒྲོལ་མ་ prefix the source file lacks. Any tooling that derives a title from the lead bold term must read this file instead.

## Not yet published

`settled` = the attested names converge, the proposed title can be used as-is.
`contested` = the commentaries name this deity differently; a human picks among the candidates first.

| Slot | Proposed title | Status | Attested candidates (commentators) |
|---|---|---|---|
| `tara-04` | སྒྲོལ་མ་གཙུག་ཏོར་རྣམ་པར་རྒྱལ་མ། | ✅ settled | གཙུག་ཏོར་རྣམ་པར་རྒྱལ་མ — article lead term, bstan-'dzin-don-bzang (གཙུག་ཏོར་རྣམ་རྒྱལ་མ)<br>གཙུག་ཏོར་རྒྱན་པའི་སྒྲོལ་མ — gendun-drub<br>འཆི་མེད་ཚེ་སྒྲུབ — palden-sherab, sangye-nyentrul, tsultrim-namdak |
| `tara-05` | — *needs a decision* | ⚑ contested | *none attested in the article* |
| `tara-06` | — *needs a decision* | ⚑ contested | འཇིག་རྟེན་གསུམ་ལས་རྣམ་པར་རྒྱལ་བ — yama-sonam, tenzin-dhonzang<br>གདོན་རིགས་རྣམ་པར་འཇོམས་པ་འཇིགས་བྱེད་ཆེན་མོ — palden-sherab, tsultrim-namdak, sungrab-tulku |
| `tara-07` | — *needs a decision* | ⚑ contested | གཞན་མཐུ་འཇོམས་མ — yama-sonam, tenzin-dhonzang<br>དམག་དང་ཐོག་སེར་འཇོམས་མ་གཏུམ་མོ་གཞན་གྱིས་མི་ཐུབ་མ — palden-sherab, article lead term<br>གཞན་འཇོམས་མ — sungrab-tulku<br>རྒོལ་བ་འཇོམས་པའི་སྒྲོལ་མ — gendun-drub |
| `tara-08` | སྒྲོལ་མ་འཇིགས་པ་ཆེན་མོ། | ✅ settled | འཇིགས་པ་ཆེན་མོ — article lead term, sungrab-tulku, drakpa-gyaltsen |
| `tara-09` | སེང་ལྡེང་ནགས་ཀྱི་སྒྲོལ་མ། | ✅ settled | སེང་ལྡེང་ནགས་ཀྱི་སྒྲོལ་མ — gendun-drub, palden-sherab, tsultrim-namdak<br>མཆོག་སྩོལ་མ — yama-sonam |
| `tara-10` | སྒྲོལ་མ་བདུད་དང་འཇིག་རྟེན་དབང་སྡུད་མ། | ✅ settled | བདུད་དང་འཇིག་རྟེན་དབང་སྡུད་མ — article lead term, cone-pa<br>འཇིག་རྟེན་དབང་སྡུད་མ — tenzin-dhonzang<br>མྱ་ངན་སེལ་བའི་སྒྲོལ་མ — nyima-bepa sādhana |
| `tara-11` | — *needs a decision* | ⚑ contested | ཕོངས་པ་ཀུན་སེལ — tenzin-dhonzang, article lead term<br>ས་གཞི — taranatha<br>དགུག་པའི་སྒྲོལ་མ — gendun-drub |
| `tara-12` | སྒྲོལ་མ་བཀྲ་ཤིས་དོན་གྲུབ་མ། | ✅ settled | བཀྲ་ཤིས་དོན་གྲུབ་མ — sangye-nyentrul, tsultrim-namdak, article lead term<br>བཀྲིས་ཐམས་ཅད་སྦྱིན་མ — yama-sonam<br>བཀྲ་ཤིས་དོན་བྱེད་སྒྲོལ་མ — palden-sherab |
| `tara-13` | — *needs a decision* | ⚑ contested | སྨིན་པར་བྱེད་པའི་སྒྲོལ་མ — gendun-drub, nyima-bepa via yama-sonam<br>མེ་ལྟར་འབར་བའི་སྒྲོལ་མ — cone-pa, tenzin-dhonzang<br>དགྲ་དཔུང་འཇོམས་མ — tsultrim-namdak |
| `tara-14` | སྒྲོལ་མ་ཁྲོ་གཉེར་གཡོ་བ། | ✅ settled | ཁྲོ་གཉེར་གཡོ་བའི་སྒྲོལ་མ — gendun-drub<br>ཁྲོ་གཉེར་ཅན་གྱི་སྒྲོལ་མ — cone-pa<br>འགུགས་བྱེད་སྒྲོལ་མ — nyima-bepa via yama-sonam |
| `tara-15` | སྒྲོལ་མ་ཞི་བ་ཆེན་མོ། | ✅ settled | ཞི་བ་ཆེན་མོ — article first-named, sungrab-tulku (རྗེ་བཙུན་སྒྲོལ་མ་ཞི་བ་ཆེན་མོ) |
| `tara-16` | ཆགས་པ་འཇོམས་པའི་སྒྲོལ་མ། | ✅ settled | ཆགས་པ་འཇོམས་པའི་སྒྲོལ་མ — gendun-drub, yama-sonam citing nyima-bepa, article lead term<br>དགྲ་འཇོམས་མའི་སྒྲོལ་མ — yama-sonam citing nyima-bepa |
| `tara-17` | སྒྲོལ་མ་དཔག་མེད་གནོན་མ། | ⚑ contested | དཔག་མེད་གནོན་མ — palden-sherab, sangye-nyentrul, tsultrim-namdak<br>བདེ་བ་སྒྲུབ་པའི་སྒྲོལ་མ — yama-sonam, gendun-drub<br>འཇིག་རྟེན་གསུམ་གཡོ་མ — tenzin-dhonzang, sungrab-tulku |
| `tara-18` | — *needs a decision* | ⚑ contested | *none attested in the article* |
| `tara-19` | — *needs a decision* | ⚑ contested | མི་ཕམ་གཟི་བརྗིད་ཅན་གྱི་རྒྱལ་མོ — palden-sherab, sangye-nyentrul, tsultrim-namdak<br>སྡུག་བསྔལ་སྲེག་ཅིང་སེལ་བ — yama-sonam, gendun-drub<br>སྡུག་བསྔལ་སེལ་མ — tenzin-dhonzang |
| `tara-20` | — *needs a decision* | ⚑ contested | རི་ཁྲོད་ལོ་མ་གྱོན་མ — palden-sherab, sangye-nyentrul, tsultrim-namdak<br>དངོས་གྲུབ་འབྱུང་གནས — yama-sonam, gendun-drub |
| `tara-21` | — *needs a decision* | ⚑ contested | འོད་ཟེར་ཅན་མ — palden-sherab, tsultrim-namdak<br>ཡོངས་སུ་རྫོགས་བྱེད་སྒྲོལ་མ — yama-sonam, gendun-drub<br>འཕྲིན་ལས་སྒྲུབ་མཛད་མ — tenzin-dhonzang<br>བླུ་བྱེད — sangye-nyentrul |

### Notes

- **tara-04** — Candidates share the གཙུག་ཏོར་ + རྣམ་རྒྱལ་ core; the ཚེ་སྒྲུབ readings describe function, not name.
- **tara-05** — The article's མཚན་གྱི་ངེས་ཚིག section explains the mantra syllables, not a deity epithet — no epithet is attested for this slot at all. Needs either a fresh pass over the commentaries for a name or a descriptive title outside the series.
- **tara-06** — Article states outright མཚན་གཅིག་ཏུ་མ་ངེས; twelve further commentaries give no epithet.
- **tara-08** — ཏུ་རེ་ is the mantra syllable, not part of the name; drop it from the title.
- **tara-09** — Already carries སྒྲོལ་མ་ inside the attested epithet, so it takes no prefix — the series rule is satisfied without doubling the word.
- **tara-11** — Article states six commentaries give six different names; no convergence.
- **tara-14** — Article notes gendun-drub's name recurs in his own commentary — མཚན་འདི་ངེས་པར་མཐུན.
- **tara-16** — Epithet already contains སྒྲོལ་མ་; no prefix.
- **tara-17** — Proposal follows the three-commentary plurality, but two rival names have two each — confirm before publishing.
- **tara-18** — This is the only slot article with no མཚན་གྱི་ངེས་ཚིག section — no epithet is extracted anywhere in the file. Needs a name pass over the commentaries before it can take a series title.

## Recording a new publication

1. Add the slot to `published:` in [published.yaml](published.yaml) with its title, page ID and URL, and remove it from `planned:`.
2. Set the same `wiki_title` / `wiki_pageid` / `wiki_url` and `status: published` in that slot's `article.md` frontmatter.
3. Regenerate this view.
