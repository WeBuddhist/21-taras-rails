# Facts, chart data, assets, and the pre-talk checklist

**§1** numbers I re-counted on disk · **§2** numbers from the paper · **§3** ready-to-plot chart
data · **§4** files to screenshot · **§5** ⚠ three discrepancies found · **§6** verify live ·
**§7** delivery notes.

---

## 1. Verified on disk today — safe to say on stage

I recounted these against the vault rather than copying them from the paper.

| Number | Claim | How verified |
|---|---|---|
| **16** | commentaries ingested | 16 files in `2-RAILS/Claims/raw/tree-guided/` |
| **582,332** | Tibetan characters of commentary | Python `len()` over all 16 source files, frontmatter stripped |
| **3,268** | citable blocks in the commentaries | block-ID regex over the same 16 files |
| **32** | blocks in the root text | same, on `1-SOURCES/Text/` |
| **580** | outline (sa-bcad) nodes across 16 trees | counted in `2-RAILS/Sections/Raw/toc-tree/` |
| **2,975** | claims, corpus-wide | summed `claim_count:` across all 16 — comes out exact |
| **16** | QC-clean TOC trees | `ls 2-RAILS/Sections/Raw/toc-tree/*.md` |
| **16** | spine maps | `ls 2-RAILS/Claims/raw/spine-map/` |
| **67** | consolidated topic pages | `ls 2-RAILS/Claims/*.md` (24 slot + 43 term) |
| **43 / 23** | term / slot articles drafted | `term-articles/` and `slot-articles/` |
| **42** | articles imported + batch-verified | `articles/` |
| **24** | canonical spine slots | annex §2a: `tara-01`–`tara-21` + `benefits` + `structure` + `origin` |
| **62** | skills with a `SKILL.md` | counted in `4-SYSTEM/Skills/` |
| **21** | skills carrying Python scripts | 44 scripts total |
| **11,251** | lines of `SKILL.md` prose | `cat */SKILL.md \| wc -l` |
| **37 nodes, 7 levels** | Gendün Drub's tree | `toc-tree/gendun-drub.md` |
| **5** | claims under node 2.2.2.2.1.1.2 | `c-…-2-1` … `-2-5`, blocks `^0-23`–`^0-27` |
| **120 / 10** | claims / questions on the lotus page | `2-RAILS/Claims/lotus.md` |

**Note:** I previously wrote **63 skills** — the correct count is **62**; the 63rd entry in that
folder is `SKILLS-CATALOG.md`, not a skill. Fixed throughout.

---

## 2. From the paper (sourced, not independently re-derived)

From `4-SYSTEM/Pipelines/wikipedia/paper/draft/paper-src.md`, which cites its own evidence.

**The gap** — 8,073 bo.wikipedia content articles (live API, 19 Aug 2026; **re-check, §6**) ·
~36 active users/month · 2 admins · ~350 new articles/year · ~7M speakers.

**Model performance** — TLUE: GPT-4 **17.5%** vs a **25%** random baseline · Qwen-2.5-72B
**84.7%** Chinese → **16.5%** Tibetan · Tibetan ≈ **4×** the token cost of Chinese
(Petrov et al. 2023).

**Comparators** — Welsh **91,000 → 280,000+** after 2017 government policy, became the
most-viewed Welsh-language website, credited with improving Welsh MT · Dzongkha program (Bhutan,
Aug–Dec 2025): dozens of participants, 5 months → **80 articles** · Scots ~23,000 articles by one
non-speaker · Cebuano ~6M bot stubs · **Greenlandic closed by LangCom, 2025** · Inuktitut ~⅔
MT-contaminated · several African-language wikis 40–60% uncorrected MT · Content Translation
(machine draft + mandatory human edit) shows **lower** deletion rates than from-scratch articles
across 2.4M+ creations.

**Keyword funnel** — 193 + 313 English candidates → **367** Tibetan terms → **114** past the
viability gate → **44** standalone (+47 section-material +10 glossary +13 merged = 114/114) →
**25 update / 19 create / 0 unresolved**. Gate: spread ≥ half the commentaries **and** ≥ 20
claims. Sensitivity: M=15→139, M=20→114, M=30→63.

**Verification** — pilot **81/81** exact, **81/81** locators resolve · batch **861/882 (97.6%)** ·
of 293 validator findings, **269** are one reference-format mismatch between drafting routes ·
consolidation audit **418** citations → **0** fabricated IDs, 1 critical, 1 moderate, ~16 minor ·
same-model audit "publish, no findings" ×3 · cross-model **5 blocking**, 4 genuine · auditor
re-run pass rates **0.67 / 0.67 / 1.0** · the tsheg→shad catch at similarity **0.974**.

**Economics** — **$0.33–1.42**/article (central ≈ **$0.71**) · 100k articles ≈ **$35k–140k**
(central ≈ $70k) · 30–60 reviewer-min/article → **24–48 person-years** for 100k · vs ~**285
years** of writing at the observed rate · Wikimedia Rapid Fund grants run $500–5k.

**Context-size finding** — same model, same prompt: **93,000** chars in → 10 passages /
**873** chars out; **12,000** chars in → 20 passages / **5,224** chars out. Pilot capture rates
against what was offered: 45%, 19%, **1.1%**.

**Target-wiki quality baseline** — of 677 sampled bo.wikipedia articles, **15%** are raw model
dumps with no markup, **75%** have no citations.

---

## 3. Chart data — ready to plot

### 3a. Claim density per commentary (slide 17)

Real, recomputed. Sorted by density. The story: **8× spread**, and it tracks genre.

| Commentary | Author | chars | claims | **claims / 10k chars** | nodes |
|---|---|---|---|---|---|
| karma-maitri | Karma Maitri | 8,986 | 163 | **181** | 24 |
| taranatha | Tāranātha | 31,741 | 368 | **116** | 27 |
| drakpa-gyaltsen | Jetsün Drakpa Gyaltsen | 12,805 | 142 | **111** | **2** |
| lobsang-dawa | Geshe Lobsang Dawa | 9,967 | 87 | 87 | 30 |
| dharmabhadra | Ngulchu Dharmabhadra | 18,293 | 148 | 81 | 30 |
| gendun-drub | Gendun Drub (1st DL) | 20,060 | 131 | 65 | 37 |
| sungrab-tulku | Drepa Ratreng Sungrab Tulku | 27,112 | 160 | 59 | 26 |
| gendun-gyatso | Gendun Gyatso (2nd DL) | 11,004 | 62 | 56 | 22 |
| konchok-thabkhe | Konchok Thabkhe | 24,535 | 132 | 54 | 28 |
| yama-sonam | Jetsün Yama Sonam | 48,070 | 258 | 54 | 24 |
| sangye-nyentrul | Sangye Nyenpa Rinpoche | 24,562 | 125 | 51 | 44 |
| tenzin-dhonzang | Sermé Tsang Geshe Tenzin Dönzang | 71,628 | 327 | 46 | 27 |
| palden-sherab | Khenchen Palden Sherab | 82,236 | 282 | 34 | **120** |
| tsultrim-namdak | Khenpo Tsultrim Namdak | 143,634 | 329 | **23** | 89 |
| pema-namgyal | Ldombuwa Pema Namgyal | 18,620 | 104 | 56 | 14 |
| tenga-tulku | Dorlob Tenga Tulku | 29,079 | 157 | 54 | 36 |

**Chart form:** horizontal bars, sorted descending by density, with the commentary's genre as a
colour coding if you want a second dimension (word-commentary vs full exegesis). Or a scatter of
chars (x) against claims (y) with a diagonal — the outliers pop immediately.

**Structural spread, same data:** outline nodes run **2 → 120**. That's the number that motivates
the spine map on the next slide, so put it on this slide as a callout.

### 3b. The keyword funnel (slide plan, cut-slide 17 in the earlier draft; now spoken)

```
193 + 313  English candidates
      367  unique Tibetan terms
      114  pass the viability gate
       44  standalone subjects
  25 / 19  update / create
```

### 3c. The two audits (slide 23)

| Check | Scope | Result |
|---|---|---|
| Deterministic gate, pilot | 81 quotations | 81/81 exact · 81/81 locators resolve |
| Deterministic gate, batch | 882 quotations / 42 articles | 861/882 (97.6%) |
| Consolidation audit | 418 citations / 3 pages | 0 fabricated · 1 critical · 1 moderate · ~16 minor |
| Same-model audit | 3 articles | "publish, no findings" ×3 |
| Cross-model audit | same 3 | **5 blocking** · 4 genuine |
| Auditor variance | 3 re-runs | 0.67 / 0.67 / 1.0 |

### 3d. Time and money (slides 7 and 25)

| | Rate | 100,000 articles |
|---|---|---|
| bo.wikipedia, observed | ~350/yr | **~285 years** of writing |
| This pipeline, review-bound | 30–60 min/article | **24–48 person-years** of reviewing |
| Machine cost | ~$0.71/article | ~$70k (central) |

### 3e. TLUE (slide 4)

| Series | Score |
|---|---|
| Qwen-2.5-72B — Chinese | 84.7% |
| GPT-4 — Tibetan | 17.5% |
| Qwen-2.5-72B — Tibetan | 16.5% |
| *random-guessing baseline* | *25% (threshold line)* |

### 3f. Context size vs output (slide 12b)

| Context given | Passages | Characters returned |
|---|---|---|
| 93,000 | 10 | 873 |
| 12,000 | 20 | 5,224 |

---

## 4. Assets — files to screenshot

**Raise the Tibetan font size before capturing.** At conference screen-share resolution, default
Uchen is unreadable.

| Slide | File | Frame |
|---|---|---|
| 9 | `4-SYSTEM/Skills/` folder pane | the list of skill names |
| 10 | `4-SYSTEM/Skills/tree-guided-claims/SKILL.md` | collapsed to headings |
| 11 | same file, lines 14–56 | "Why this skill exists" + the five guards |
| 11 | `4-SYSTEM/Skills/claims-consolidation/SKILL.md`, lines 119–197 | rules 9–16, each with its cause |
| 13 | `1-SOURCES/Text/…བསྟོད་པ།.md` lines 43–46 | verse 3 with `^1-3` |
| 14 | `1-SOURCES/Commentaries/…ཕྲེང་བ།.md` lines 88–96 | blocks `^0-23`–`^0-27` |
| 14 | `0-INBOX/raw-data/` | a raw OCR file, for the "before" panel |
| 15 | `2-RAILS/Sections/Raw/toc-tree/gendun-drub.md` | `1.` down to `2.2.2.2.1.1.2` |
| 16 | `2-RAILS/Claims/raw/tree-guided/gendun-drub.md` lines 396–432 | the five claims |
| 18 | `2-RAILS/Claims/raw/spine-map/karma-maitri.md` | the slot table |
| 19 | `2-RAILS/Claims/lotus.md` | `## Questions asked` |
| 20 | `2-RAILS/Claims/lotus.md` | the origin-narrative `### ⚑ Divergences` |
| 21 | `…/term-articles/lotus/article-preview.md` | the rendered article + footnotes |
| 21 | `…/term-articles/lotus/citations.md` | the citation trail table |

**Verbatim text to paste** (copied from the vault — **do not retype Tibetan by hand**):

Root verse 3 (`^1-3`):
```
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། ། ^1-3
```

Claim `c-2-2-2-2-1-1-2-4` (*iconography*, cite `^0-26`):
```
དེའི་ཕྱག་གཡོན་གྱི་སྲིན་ལག་གིས་ཆུ་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨུཏྤ་ལས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པ་སྟེ།
བཟུངས་ནས་སྙན་གྱི་ཐད་ཀར་ཁ་བྱེ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དག་པའི་རྟགས་སོ། །
```

The variant for slide 20:
```
root text     ^1-3   →   ཕྱག་འཚལ་གསེར་སྔོ་...
Gendün Drub   ^0-24  →   ཕྱག་འཚལ་སེར་སྔོ་...
```

---

## 5. ⚠ Three discrepancies found in the vault

**(a) The corpus-size figure in the paper is understated.** The paper says the sixteen
commentaries total **~540,000 characters**. Counting Unicode codepoints across the current
`1-SOURCES/Commentaries/` files with frontmatter stripped gives **582,332**. The paper's own
corrected draft already flags this as unresolved — it notes that the counting script "must define
whether this value counts Unicode code points or grapheme clusters and whether whitespace and
markup are included." The likeliest explanation is annotation added since the figure was taken.
**Use 582,332, or say "roughly 580,000."** Don't say 540,000 — you'd be understating your own
corpus. *(Note: `wc -m` will mislead you here — in this shell's locale it returns bytes, giving
1,673,569.)*

**(b) Per-commentary claim counts disagree between two files.** Six spine maps report a
`claim_count:` that doesn't match the claims file they were built from:

| Commentary | spine-map | claims file |
|---|---|---|
| gendun-drub | 136 | 131 |
| gendun-gyatso | 64 | 62 |
| konchok-thabkhe | 135 | 132 |
| palden-sherab | 283 | 282 |
| tenzin-dhonzang | 328 | 327 |
| yama-sonam | 260 | 258 |

The **corpus total of 2,975 is safe** — it sums the claims files and comes out exact. But your
running example is one of the six, so if asked "how many claims in the First Dalai Lama's
commentary," say **"about 130."** Flagged as a separate task.

**(c) Two broken `source_file` references.** In `2-RAILS/Claims/raw/tree-guided/`, these two
frontmatter paths don't resolve — both are trailing-shad mismatches against the real filenames:

- `pema-namgyal` → `…བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md` (actual file ends `བཞུགས་སོ།.md`)
- `tenga-tulku` → `…གསལ་བའི་མེ་ལོང་…བཞུགས་སོ།། །།.md` (actual ends `བཞུགས་སོ།.md`)

Small, but it breaks automated traceability for those two commentaries — anything walking the
citation chain programmatically will silently skip them. Worth fixing before the paper's
reproducibility claims are tested. **Not a talk problem** — neither is your running example.

**(d) Not a discrepancy, but say it proactively:** every claims file, spine map and consolidated
page carries `status: draft`. That's by design — the model never marks its own output complete;
only a domain specialist does. If you show a frontmatter block on screen, someone *will* read
`status: draft` off the slide and ask. Get ahead of it: it's the review state, and it's a feature.

---

## 6. Verify live, the morning of the talk

- [ ] **bo.wikipedia article count** (currently 8,073, as of 19 Aug 2026):
      `https://bo.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=statistics&format=json`
- [ ] **Comparator article counts** for slide 3. Welsh is sourced in the project bibliography;
      **Basque, Icelandic and Estonian are not sourced in this vault** — pull them from
      `https://meta.wikimedia.org/wiki/List_of_Wikipedias`. Don't quote a remembered figure.
- [ ] **Speaker populations** for the same chart, if shown — one source for all four, not a mix.
- [ ] **Model pricing**, if you show the cost slide. The cost note is dated 2026-08-02 and says
      itself that prices are falling. Round generously, or say "on the order of."
- [ ] Anything **live from Wikipedia** — re-fetch, don't use a cached snapshot.

---

## 7. Delivery notes

- **Screenshot everything Tibetan as an image.** Never rely on a font being present on the
  conference platform.
- **Crop hard.** More than ~8 lines of visible content in a screenshot is unreadable on a shared
  screen.
- **Cut order: 17 → 7 → 3 → 12b.** But **protect slide 20** (what consolidation finds) and
  **slide 11** (why the rules exist) — those are the two slides each half of the room will
  remember. If you're long, cut slide 17 and cover it in one sentence: *"claim density across the
  sixteen varies eightfold, and it tracks genre — happy to go into it in questions."*
- **Practice the Act III transitions out loud.** The whole act is one continuous example and only
  works if each slide opens by naming where you are: *"same verse," "same commentary," "still
  block `^0-26`."*
- **Slide 12b is the one to restore if a technical audience shows up hotter than expected** — and
  the one to drop first if the room skews humanities on the day. Judge it from the chat.
- Have **B1–B5 loaded but hidden.** B4 (limitations) is what buys credibility with a skeptic;
  B3 (isolation architecture) is what the engineers will ask about.
