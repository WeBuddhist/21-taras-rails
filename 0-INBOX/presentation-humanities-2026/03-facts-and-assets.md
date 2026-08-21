# Facts, assets, and the pre-talk checklist

Three things live here: **(1)** every number in the deck with where it came from and whether I
verified it on disk, **(2)** the exact files to screenshot, **(3)** what must be checked live
before you present.

---

## 1. Numbers — verified on disk today

I re-counted these against the vault rather than copying them from the paper. All of these are
safe to say on stage.

| Number | Claim | How verified |
|---|---|---|
| **16** | commentaries ingested | `ls 2-RAILS/Claims/raw/tree-guided/` = 16 files |
| **2,975** | total claims | summed `claim_count:` across all 16 tree-guided files — comes to exactly 2,975 |
| **16** | QC-clean TOC trees | `ls 2-RAILS/Sections/Raw/toc-tree/*.md` = 16 |
| **16** | spine maps | `ls 2-RAILS/Claims/raw/spine-map/` = 16 |
| **67** | consolidated topic pages | `ls 2-RAILS/Claims/*.md` = 67 (24 slot + 43 term) |
| **43** | term articles drafted | `ls .../term-articles/` = 43 |
| **23** | slot articles drafted | `ls .../slot-articles/` = 23 |
| **42** | articles imported + batch-verified | `ls .../articles/` = 42 |
| **24** | canonical spine slots | annex §2a: `tara-01`–`tara-21` + `benefits` + `structure` + `origin` |
| **63** | skills in the vault | `ls 4-SYSTEM/Skills/` = 63 entries |
| **37 nodes, 7 levels** | Gendün Drub's tree | counted in `2-RAILS/Sections/Raw/toc-tree/gendun-drub.md` |
| **131** | claims in Gendün Drub's file | frontmatter `claim_count:` — ⚠ see §4 |
| **5** | claims under node 2.2.2.2.1.1.2 | `c-2-2-2-2-1-1-2-1` … `-2-5`, blocks `^0-23`–`^0-27` |
| **120** | claims gathered for the lotus page | stated in `2-RAILS/Claims/lotus.md` header |
| **10** | questions on the lotus page | `consolidation_questions:` in its frontmatter |

## 2. Numbers from the paper (sourced, but not independently re-derived by me)

These come from `4-SYSTEM/Pipelines/wikipedia/paper/draft/paper-src.md`, which is the working
draft of the IATS paper and cites its own evidence. Solid to say — just know they trace to the
paper rather than to a count I ran.

**The gap**
- 8,073 content articles on bo.wikipedia (live API count, 19 Aug 2026) — **re-check, §5**
- ~36 active users in the trailing month · 2 administrators · ~350 new articles/year
- ~7 million Tibetan speakers

**Model performance**
- TLUE benchmark: GPT-4 at **17.5%** vs a **25%** random-guessing baseline
- Qwen-2.5-72B: **84.7%** in Chinese → **16.5%** in Tibetan
- Petrov et al. 2023: Tibetan ≈ **4×** the byte cost of Chinese to tokenize

**Comparators**
- Welsh: **91,000 → 280,000+** articles after 2017 government policy; became the most-viewed
  Welsh-language website; growth credited with improving Welsh MT
- Dzongkha Wikipedia Education Program (Bhutan, Aug–Dec 2025): dozens of participants, 5 months
  → **80 articles**
- Scots: ~23,000 articles by one non-speaker · Cebuano: ~6M bot stubs · **Greenlandic: closed by
  the Language Committee in 2025** over machine-generated content · Inuktitut ~⅔ MT-contaminated
  · several African-language wikis 40–60% uncorrected MT
- Content Translation (machine draft + mandatory human edit): **lower** deletion rates than
  from-scratch articles, across 2.4M+ creations

**The keyword funnel**
- 193 + 313 English candidates → **367** Tibetan terms → **114** pass the viability gate →
  **44** standalone (+ 47 section-material + 10 glossary + 13 merged = 114/114)
- Against the live wiki: **25 update / 19 create / 0 unresolved**
- Viability gate: spread ≥ half the commentaries **and** ≥ 20 claims
- Sensitivity: M=15 → 139 terms · M=20 → 114 · M=30 → 63

**Verification**
- Pilot: **81/81** quotations character-exact; **81/81** block locators resolve
- Batch: **861/882 (97.6%)** character-exact across 42 articles
- Of 293 validator findings, **269** are one reference-format mismatch between the two drafting
  routes — a mechanical reconciliation, not fabricated citations. *Say this if you show the
  number; it's the honest reading.*
- Consolidation audit: **418** citations re-checked → **0** fabricated IDs, 1 critical,
  1 moderate, ~16 minor
- Same-model audit: "publish, no findings" ×3. Cross-model: **5 blocking findings** on 2 of 3;
  4 genuine on adjudication
- Auditor variance across re-runs: **0.67, 0.67, 1.0**
- The tsheg→shad catch: string similarity **0.974**, FAIL

**Economics**
- ~**$0.33–1.42** per article (central ≈ **$0.71**) at flash-tier prices
- 100,000 articles ≈ **$35k–140k** (central ≈ $70k), one-time, parallelizable
- 30–60 reviewer-minutes/article → 100k articles = **24–48 person-years** of review
- vs ~**285 years** of writing at bo.wikipedia's observed rate
- Wikimedia Rapid Fund grants run $500–5k — *this needs a bigger grant, not a miracle*

**The extraction-capture finding (backup slide B2)**
- Same model, same prompt: **10 passages / 873 chars** returned when given 93,000 chars of
  context; **20 passages / 5,224 chars** when given 12,000
- Pilot capture rates against what was offered: 45%, 19%, **1.1%**

**Wiki quality baseline (justifies the validator)**
- Of 677 sampled articles on bo.wikipedia: **15%** are raw model dumps with no markup at all,
  **75%** have no citations

---

## 3. Assets — exact files to screenshot

Open each in Obsidian, set a comfortable font size, and capture. **Increase the Tibetan font
size before capturing** — on a shared screen at conference resolution, default Uchen is
unreadable.

| Slide | File | What to frame |
|---|---|---|
| 11 | `1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md` | lines 43–46 — verse 3 with `^1-3` visible |
| 12 | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md` | lines 88–96 — blocks `^0-23`–`^0-27` |
| 12 | `0-INBOX/raw-data/` | a raw OCR file, for the "before" panel |
| 13 | `2-RAILS/Sections/Raw/toc-tree/gendun-drub.md` | the tree, from `1.` down to `2.2.2.2.1.1.2` |
| 14 | `2-RAILS/Claims/raw/tree-guided/gendun-drub.md` | lines 396–432 — the five claims |
| 17 | `2-RAILS/Claims/raw/spine-map/karma-maitri.md` | the slot table (clean 1:1 mapping, reads well) |
| 18 | `2-RAILS/Claims/lotus.md` | the `## Questions asked` list |
| 19 | `2-RAILS/Claims/lotus.md` | the origin-narrative `### ⚑ Divergences` section |
| 20 | `3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/lotus/article-preview.md` | the rendered article with footnotes |
| 20 | `3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/lotus/citations.md` | the citation trail table |
| 9 | `4-SYSTEM/Skills/` folder pane + `toc-tree-extraction/SKILL.md` open | side by side |

**A note on the flow of slides 11 → 20:** they are all the same verse and the same commentary.
Say so at each transition — "same verse," "same commentary," "still block `^0-26`." The repetition
is what makes the chain visible to someone who doesn't read code.

**Verbatim text you can paste into slides** (copied character-for-character from the vault — do
not retype Tibetan by hand):

Root verse 3 (`^1-3`):
```
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། ། ^1-3
```

Claim `c-2-2-2-2-1-1-2-4` (type: *iconography*, cite: `^0-26`):
```
དེའི་ཕྱག་གཡོན་གྱི་སྲིན་ལག་གིས་ཆུ་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨུཏྤ་ལས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པ་སྟེ།
བཟུངས་ནས་སྙན་གྱི་ཐད་ཀར་ཁ་བྱེ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དག་པའི་རྟགས་སོ། །
```

The variant for slide 19 — root text vs Gendün Drub's quotation:
```
root text      ^1-3   →   ཕྱག་འཚལ་གསེར་སྔོ་...
Gendün Drub    ^0-24  →   ཕྱག་འཚལ་སེར་སྔོ་...
```

---

## 4. ⚠ Two data inconsistencies I found — don't get caught by these

**(a) Per-commentary claim counts disagree between two files.** Six spine maps report a
`claim_count:` that doesn't match the corresponding claims file's frontmatter:

| Commentary | spine-map | claims file |
|---|---|---|
| gendun-drub | 136 | 131 |
| gendun-gyatso | 64 | 62 |
| konchok-thabkhe | 135 | 132 |
| palden-sherab | 283 | 282 |
| tenzin-dhonzang | 328 | 327 |
| yama-sonam | 260 | 258 |

The **corpus total of 2,975 is safe** — it sums the tree-guided claims files, and it comes out
exact. But if someone asks "how many claims in the First Dalai Lama's commentary," the vault has
two answers. Either say "about 130," or resolve it before the talk. I've flagged this as a
separate task; it's a data-integrity question, not a presentation one.

**(b) Status fields.** Every claims file, spine map and consolidated page carries
`status: draft`. That's by design — the model never marks its own output complete; only a domain
specialist does. **Say this proactively if you show a frontmatter block on screen**, because a
sharp audience member will read `status: draft` off the slide and ask. It's a feature: it's the
review state, and nothing below `complete` is supposed to feed a transformation. The paper is
explicit that the batch was drafted from pages still marked draft, with the responsible human
accepting that risk knowingly and per-article warnings recording it.

---

## 5. Verify live, the morning of the talk

- [ ] **bo.wikipedia article count.** Currently quoted as 8,073 (19 Aug 2026). Get the fresh
      number: `https://bo.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=statistics&format=json`
- [ ] **Comparator article counts** for the slide-3 chart. Welsh is documented in the project
      bibliography; **Basque, Icelandic and Estonian counts are not sourced in this vault** —
      pull them from `https://meta.wikimedia.org/wiki/List_of_Wikipedias` and use that day's
      numbers. Do not quote a remembered figure.
- [ ] **Speaker-population figures** for the same chart, if you show them. Cite one source for
      all four rather than mixing.
- [ ] **Model pricing**, if you show the cost slide. The cost note is dated 2026-08-02 and says
      itself that prices are falling. Round generously or say "on the order of."
- [ ] **Anything about a live Wikipedia article** you plan to show — re-fetch it, don't use a
      cached snapshot.

---

## 6. Delivery reminders for an online talk

- **Tibetan renders badly on other people's machines.** Screenshot everything Tibetan as an
  image. Never rely on a font being present on the conference platform.
- **Screen-share resolution kills small text.** If a screenshot needs more than about eight lines
  of visible content, crop it or split it across two slides.
- The four cuttable slides, in order: **16 → 7 → 3 → 19**. But protect 19 — it's the slide that
  proves the method does philology, and it's the one this audience will remember. If you're
  running long, cut slide 16 (the keyword funnel) and cover it in one spoken sentence instead:
  *"we also have a statistical chain that picks which subjects are worth an article — happy to
  go into it in questions."*
- **Practice the transitions in Act III out loud.** The whole act is one continuous example, and
  it only works if each slide opens by naming where you are: "same verse," "same commentary,"
  "still block `^0-26`."
- **Have backup slides B1–B5 loaded but hidden.** B2 (the extraction-capture cliff) is the one
  a technical audience member will most want, and B4 (limitations) is the one that buys you
  credibility if someone comes in skeptical.
