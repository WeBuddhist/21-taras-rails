# Vault Annex — Twenty-One Homages to Tārā conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions that are specific to *this* vault: the **Praise to the Twenty-One Tārās** (སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ, *Ekaviṃśati-stotra*).

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins.

---

## 1. The text

This vault serves the **Praise to the Twenty-One Tārās** (སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ, "Homage in Twenty-One Verses to Ārya Tārā") — a short liturgical praise attributed by tradition to the Buddha Vairocana (author field: རྣམ་པར་སྣང་མཛད), transmitted in the Kangyur (Tohoku catalogue no. 438; BDRC `WA0RK0438`), and among the most widely recited Tārā liturgies across all Tibetan traditions.

The text is a single short work, not a multi-volume collection, so there is one row rather than a books/volumes table:

| Source-text file | Content |
| --- | --- |
| `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` | The root praise: one invocation block (`^I-1`) + 21 homage stanzas + 1 closing stanza (`^1-1`–`^1-22`) |

Sixteen of the seventeen registered commentaries on this praise are ingested (§3). No other root text is served by this vault.

---

## 2. Addressing scheme

**`verse_id_format`:** `chapter-verse`

**Format example:** `^1-1` (chapter 1, verse 1) … `^1-21` (chapter 1, verse 21); `^I-1` for the pre-stanza title/invocation block; `^1-22`, `^2-1`–`^2-6` and `^a-1` for the closing benefits section.

### ⚑⚑ Correction 2026-09-22 — the benefits section is NOT `^a-1`–`^a-7`

The two paragraphs below describe a re-addressing of the benefits section to `^a-0`–`^a-7` that **the root text does not actually carry**. Read off the file itself, every block ID in `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` is:

```
^0 ^I-0 ^I-1 ^I-2 ^I-3
^1-0 ^1-1 … ^1-21 ^1-22
^2-0 ^2-1 … ^2-6
^a-0 ^a-1
```

So the closing material sits at **`^1-22` (the mantra-praise line) + `^2-1`–`^2-6` (the seven ཕན་ཡོན stanzas' run) + `^a-1` (the colophon)** — 32 content blocks in total, which is also what the WeBuddhist library edition carries and what the ten verse-aligned commentaries in `1-SOURCES/Commentaries/New raw data/` anchor to. Those commentaries' frontmatter carries a note warning that their anchors "predate the resegmentation"; **that note is mistaken and should be removed** — their anchors match the root exactly.

Consequences, so nobody re-derives this:

- The `benefits` spine slot (§2a) is unchanged as a **slot ID**; only its root-anchor column was wrong. It covers `^1-22`, `^2-1`–`^2-6` and `^a-1`.
- `claims-fact-check` maps `^1-22`, `^2-*` and `^a-*` to `benefits` (`assemble_block_packet.py`), verified against `^2-3`: seven commentaries with prose, claims page attached.
- A human contributor should decide whether to *perform* the `^a-*` re-addressing these paragraphs describe, or to retire the plan. Until then the file wins over the annex.

There is functionally one "chapter" (the praise has no internal chapter divisions), so every verse ID's leading segment is `1`, and the addressing scheme's real content is the verse number: **`^1-1` through `^1-21`, one block per four-line homage stanza** — never a homage split across two or three blocks.

### ⚑ Benefits-section prefix: `a`, not a continuation of `^1-*` (revised 2026-08-07)

The praise's closing ཕན་ཡོན (benefits) section is addressed with its own `a` prefix — `^a-0` for its heading, `^a-1` … `^a-7` for its seven stanzas (the last being the colophon) — not as a continuation of the homage run. This mirrors the sibling `Liturgy-rails` vault, whose critical edition of this praise is the witness this vault now uses (see below), and keeps the homage numbers `^1-1`–`^1-21` in exact correspondence with the homage ordinals every commentary uses.

**This supersedes the earlier `^1-1` through `^1-22` scheme** ("21 homage stanzas plus one closing stanza"), which described neither the text as it now stands nor the file as it then stood. Until 2026-08-07 the root text was a raw OCR transcription (OpenPecha `MDAFBF633`) carrying 47 content blocks — each homage split across two or three of them, with inconsistent boundaries — and ending mid-clause after the twenty-first homage, omitting the benefits section entirely. It was replaced with the critical edition from `Liturgy-rails/1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ.md` (BDRC `WA0XLF0FAD365454A`); the superseded transcription is retained at `0-INBOX/root-text-backup-pre-resegmentation-2026-08-07.md`, and the two witnesses' variant readings are summarised in the root text's own `source_description`. Any rail written before that date that cites a root-text block ID is citing the old scheme and must be re-checked.

### ⚑ Intro-material prefix: `I`, not `0` — overrides `4-SYSTEM/CLAUDE.md` §5a's example

`4-SYSTEM/CLAUDE.md` §5a documents `## 0. Introduction ^0-0` as the generic pre-chapter slot. **This vault uses the Roman letter `I` instead of the digit `0`** for every block of introductory material — `^I-0` for the intro heading, `^I-1`, `^I-2`, … for its content blocks — in both the root text and all sixteen ingested commentaries. This is not a deviation to fix; it is this vault's actual convention, inherited from the `kwiki` Wikipedia pipeline's own `INTRO_PREFIX = "I"` (`4-SYSTEM/Pipelines/wikipedia/src/kangyur_wiki/stages/commentary.py`) and documented in that pipeline's `docs/reference/conventions.md` §1a. Per this annex's own governance line, `^I-*` is the rule for this vault; `^0-*` is not used anywhere in it.

A commentary's own `^I-*` run can be long — some commentaries carry 100+ intro blocks (front matter, homage to the author's teacher, the commentator's own preamble) before the first sa-bcad division, if any, begins.

### Heading hierarchy

| Markdown | Role | Anchor |
| -------- | ---- | ------ |
| `#` | Title of the work (root) / commentary title (commentaries) | none |
| `##` | The root text's three top-level sections: the title/invocation block (`## མཚན་བྱང་།`), the homages themselves (`## ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག`), and the closing benefits (`## བསྟོད་པའི་ཕན་ཡོན།`) | `^I-0` / `^1-0` / `^a-0` |
| `###`–`######` | A commentary's own ས་བཅད (sa bcad) structural divisions, when ingested via `toc-tree-extraction` + `toc-tree-ingest` | full decimal path, no segment cap — see below |

### ⚑ Sa-bcad heading depth: full decimal path, no four-segment cap — overrides `4-SYSTEM/CLAUDE.md` §5a

`4-SYSTEM/CLAUDE.md` §5a caps heading IDs at four segments ("IDs must not exceed four segments … flatten deeper structures"). **This vault does not cap sa-bcad heading depth.** A commentary's sa-bcad tree can and does nest past four levels (`toc-tree-extraction` has produced five-level trees on this vault's own commentaries — see `0-INBOX/toc-tree-lobsang-dawa.md`), and flattening a real fifth-level division into a fourth-level heading destroys the very structure the tree records. Heading block IDs therefore use the **full decimal path** the tree assigns, joined by `-`, with the trailing `-0` slot appended exactly as `4-SYSTEM/CLAUDE.md` §5a otherwise describes: `1.2.2.1.1.4` → `^1-2-2-1-1-4-0` (six segments plus the `-0` slot). Heading level scales the same way `toc-tree-ingest`'s proven convention (ported from the sibling `bodhisattvacharyavatara-rails` vault) already documents: depth 1→`##`, 2→`###`, 3→`####`, **4+→`#####`/`######` as needed**, never flattened. No sa-bcad headings have been ingested into `1-SOURCES/` yet in this vault (the TOC trees exist in `0-INBOX/`, unapplied) — this rule takes effect the first time `toc-tree-ingest` runs here.

### Verse numbering rule

Verse numbers run continuously through the single chapter, 1–21, with no restart (there is only one chapter), one block per four-line homage. The `^I-*` prefix is reserved for material before verse 1 and is never reused inside the chapter; the `^a-*` prefix is reserved for the closing benefits section after verse 21 and is likewise never reused inside the chapter.

---

## 2a. Canonical spine slots (`spine_scheme: tara21`)

The **spine** is the root text's own structure, expressed as a list of stable slot IDs. It is
the shared coordinate system every commentary is mapped onto by the `spine-map` skill, and the
unit `claims-consolidation` consolidates: one topic page per slot. Slot IDs are stable
forever — a topic page's filename comes from its slot, so renaming one orphans its page.

**This registry is the only source of slot IDs.** The `spine-map` skill may not coin a slot
locally; if a commentary needs one that is not listed here, a human contributor registers it
here first.

### Spine-proper slots (mechanically derived from the root text's own blocks)

| Slot | Root anchor | Content |
| --- | --- | --- |
| `tara-01` … `tara-21` | `^1-1` … `^1-21` | One slot per four-line homage stanza, in exact ordinal correspondence: `tara-07` is the homage at `^1-7`. |
| `benefits` | `^a-1`–`^a-7` | The closing ཕན་ཡོན section (the seventh stanza is the colophon). |

Twenty-two slots. Every commentary's spine map must dispose of each of them — mapped, routed
by claim, or explicitly marked silent.

### Global slots (registered as observed across the corpus)

These are not root-text blocks; they are recurring bodies of commentarial material that sit
outside the homage sequence. They are added here as the corpus is mapped, never invented
per-commentary.

| Slot | Content | First observed |
| --- | --- | --- |
| `structure` | The commentary's own sa-bcad division of the praise as a whole — how many parts, where the praise proper ends and the benefits begin. | `karma-maitri` node `1.1` |
| `origin` | Tārā's origin narrative / ལོ་རྒྱུས — where a commentary gives it as its own section rather than inside homage 1. | `tsultrim-namdak` node `2.1.1` |

**Not every body of material belongs to a slot.** A commentary's own front matter, colophon,
ritual appendices (maṇḍala rites, sādhana sequences) and story collections are dispositioned
as *unmapped nodes* in its spine map. That is a legitimate outcome, not a coverage failure —
those claims are preserved in `Claims/raw/`, they simply feed no topic page.

### Scaling note

For a vault on a different root text the spine is derived the same way: one slot per unit of
the root's own structure, at whatever granularity keeps a topic page under roughly 40–50
claims (`2-RAILS/About Rails.md` §6b's split rule). For Bodhicaryāvatāra that is a chapter or
verse-group rather than a homage, with the root anchor being the corresponding block-ID range.
Nothing in the `spine-map` skill or `assemble_packet.py` is specific to twenty-one homages —
only this table is.

---

## 3. Registered commentary IDs

Every commentary file in `1-SOURCES/Commentaries/` declares a `registered_id` in its frontmatter. That short ID is the only string used to attribute claims to the commentary throughout `2-RAILS/` and throughout the `kwiki` pipeline's `3-TRANSFORMATIONS/Wikipedia/tara21/` output (its `sources.yaml` carries the same `registered_id` per entry, added 2026-08-04 — see §6).

Once assigned, a `registered_id` never changes. New commentaries must be added to the roster below before their `registered_id` is used in any rail.

**2026-08-19 ID migration (human-contributor directive — the sanctioned exception to the line above):** the placeholder-derived IDs `anon-trinle-char`, `anon-utpala`, and `anon-rnam-snang` were retired vault-wide after the author review identified the authors — they are now **`yama-sonam`** (Jetsün Yama Sonam), **`dharmabhadra`** (Ngulchu Dharmabhadra), and **`rnam-snang`** (text-based; authorship still ⚑-flagged below). Every live file and filename was migrated in one pass, including the pipeline siglum `TARAC09_ANON` → `TARAC09_JYS`. The old IDs survive only in git history and in the team's dkar-chag spreadsheet (`སྒྲོལ་མ་ཉེར་གཅིག་དཀར་ཆག.xlsx`), which the team should update to match. The never-changes rule otherwise stands.

| `registered_id` | Author (English) | School / tradition | Pipeline siglum | File |
| --- | --- | --- | --- | --- |
| `drakpa-gyaltsen` | Jetsün Drakpa Gyaltsen | Sakya | `TARAC02_DGT` | `སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md` |
| `gendun-drub` | Gyalwa Gendun Drub (1st Dalai Lama) | Gelug | `TARAC03_GDD` | `སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md` |
| `gendun-gyatso` | Gendun Gyatso Palzangpo (2nd Dalai Lama) | Gelug | `TARAC04_GDG` | `ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md` |
| `taranatha` | Tāranātha | Jonang | `TARAC05_TRN` | `ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md` |
| `dharmabhadra` | Ngulchu Dharmabhadra | Gelug | `TARAC06_NDB` | `སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md` |
| `konchok-thabkhe` | Konchok Thabkhe (a.k.a. Tenpa Gyatso) | Gelug | `TARAC07_KTK` | `ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md` |
| `tenga-tulku` | Dorlob Tenga Tulku | (unaffiliated / Nyima Bepé tradition) | `TARAC08_DTG` | `ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས་སོ།། །.md` |
| `yama-sonam` | Jetsün Yama Sonam | (unaffiliated / Nyima Bepé tradition) | `TARAC09_JYS` | `སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md` |
| `pema-namgyal` | Ldombuwa Pema Namgyal | (unaffiliated) | `TARAC10_DPN` | `ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།.md` |
| `karma-maitri` | Karma Maitri | (unaffiliated) | `TARAC11_KMT` | `ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md` |
| `palden-sherab` | Khenchen Palden Sherab | Nyingma | `TARAC12_PDS` | `རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ་དད་བརྩོན་བྱང་ཆུབ་སེམས་མཆོག་གི་པདྨའི་གཞོན་ནུ་ཁ་འབྱེད་པའི་ཐབས་ཤེས་ཉི་ཟླའི་འཛུམ་རླབས་ཞེས་བྱ་བཞུགས།.md` |
| `tenzin-dhonzang` | Sermé Tsang Geshe Tenzin Dhonzang | Gelug | `TARAC13_TDZ` | `སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ།.md` |
| `lobsang-dawa` | Geshe Lobsang Dawa (compiler) | Gelug | `TARAC14_LZD` | `སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md` |
| `sangye-nyentrul` | Sangye Nyenpa Rinpoche | (unaffiliated) | `TARAC15_SNT` | `རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་ཉུང་ངུར་བཀོད་པ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས།.md` |
| `sungrab-tulku` | Drepa Ratreng Sungrab Tulku | Gelug (contemporary) | `TARAC16_PSR` | `སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md` |
| `tsultrim-namdak` | Khenpo Tsultrim Namdak | Kagyu | `TARAC17_TSN` | `སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md` |
| `rnam-snang` | Dharmabhadra? ⚑ (unverified — see note; distinct from `dharmabhadra` above) | — | **not in pipeline corpus** | `ཡང་དག་པ་རྫོགས་པའི་སངས་རྒྱས་རྣམ་པར་སྣང་མཛད་ཀྱིས་གསུངས་པ་འཕགས་མ་སྒྲོལ་མ་ལ་བསྟོད་པ་ཕྱག་འཚལ་བ་ཉི་ཤུ་རྩ་གཅིག.md` |

**⚑ One open flag on this roster, for a human to resolve, not silently fixed here:**

- ~~`drakpa-gyaltsen`'s author identity was inconsistent across this file's own metadata~~ — **resolved 2026-08-19** during the human author-name review: the commentary's frontmatter now reads རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་ (Jetsün Drakpa Gyaltsen), matching the commentary's own colophon (`…ལོཙྪ་བ་གཉན་གྱིས་བསྒྱུར་བ། རྗེ་བཙུན་ཆེན་པོ་གྲགས་པ་རྒྱལ་མཚན་གྱིས་གཏན་ལ་ཕབ་པའོ།།`) and `sources.yaml`. An interim value naming Situ ༠༩ Pema Nyinje Wangpo was reverted the same day.
- **`rnam-snang`'s title is textually identical to the root text's own title** (STATE.md flagged this; it has no counterpart in the pipeline corpus, per §6). Whether this file is a genuine commentary or a second copy of the root deserves a human read before it is cited as a commentary anywhere.

**Tier ordering.** This praise has no single root commentary with named sub-commentaries the way a scholastic treatise does — its seventeen commentaries are independent works from five schools plus several unaffiliated authors. There is therefore no default primary/secondary ranking. When a verse package or claims comparison presents multiple commentaries together, group by school in the order the roster lists them above (Sakya → Gelug → Jonang → Nyingma → Kagyu → unaffiliated), and within a school by the roster's own order; do not invent a "the real commentary is X" hierarchy this tradition does not have.

---

## 4. Language tracks

| Tag | Language | Translation track | Status |
| --- | -------- | ------------------ | ------ |
| `bo` | Tibetan | — (source; every `1-SOURCES/` file in this vault) | — |
| `en` | English | `3-TRANSFORMATIONS/Translations/Dharmamitra/en/` | `track_type: machine-baseline`, `rails_used: none`, permanently `status: draft` |
| `en` | English | `3-TRANSFORMATIONS/Translations/Dharmamitra-termlocked/en/` | planned — the vocabulary-standardised track (`dharmamitra-termlocked`); not yet generated as of 2026-09-22 |

**The zero-shot English baseline is not a governed translation track.** It carries no
`requirements.md` / `termbase.md` / `audience.md`, cites no rails, and may not be cited by any
other `3-TRANSFORMATIONS/` output. It exists as the **control**: the record of what the machine
says with nothing whispered to it, against which a term-locked run is measured. Nothing may be
written into it that was produced with a termbase.

**Five tracks were deleted on 2026-09-21** (DharmaMitra `zh`; Gemini `hi`, `mn`, `ne`, `vi`) on
the human contributor's instruction, from both the vault and the WeBuddhist library, because a
zero-shot track has neither vocabulary standardisation nor a per-segment fact check. They are to
be rebuilt through the chain in §4a. `4-SYSTEM/scripts/upload_ledger.json` keeps their entries
marked `deleted: 2026-09-21`; a re-upload creates a new library text id.

The `kwiki` pipeline's `article.en.md` files
(`3-TRANSFORMATIONS/Wikipedia/tara21/articles/<term>/article.en.md`) are **English
check-translations for human review**, not a registered `en` track — they let a reviewer who
reads English confirm a Tibetan draft's content, and are not governed by
`About Transformations.md`'s per-track contracts.

---

## 4a. The vocabulary-standardised translation chain

Decided with the human contributor 2026-09-22. This is the path a translation must travel
before it is uploaded anywhere; each step names the skill that performs it.

```
1  keyword-extract          → 2-RAILS/Keywords/source-term-registry.json
                               which terms the corpus is about (descriptive)
2  term-definition          → 2-RAILS/termbases/term-localization.md, Meaning column
                               verbatim commentary definitions, each cited to a block ID
3  term-localization        → same table, target-language columns
                               rendering derived from the definition, not a dictionary
4  graded-translate P1      → 3-TRANSFORMATIONS/Translations/<track>/termbase.md
                               THE CONTRACT: one locked rendering per term, per track
5  dharmamitra-termlocked   → the translation, with the lock glossary sent on every call
   (or graded-translate P2, which translates with the agent's own model)
6  check_locks / P3         → every lock that should have applied, verified EXACT/LOOSE/MISSING
7  commentary-fact-check    → meaning checked against one commentary at a time
   + claims-fact-check      → and against the whole corpus + consolidated claims
8  re-translate the failures → back to step 5 for those blocks, or fix the termbase (step 3/4)
                               when the fault is the rendering rather than the block
9  translation-upload       → dry-run first; never `--execute` without explicit confirmation
```

Steps 1–3 are **descriptive and live in `2-RAILS/`** — they record what the tradition says a
term means. Step 4 is the **first prescriptive step** and lives in `3-TRANSFORMATIONS/`: it is a
choice, and choices do not belong in the rails.

### Steps 2–4, the attested route (added 2026-09-23)

Steps 2–3 above are the **definition-driven** route: read what the commentaries say the term
means, then derive a rendering from that. It is the more authoritative route and the slower one —
step 2 must run before step 3 can produce anything, and a term whose Meaning cell is empty is
skipped rather than guessed.

`glossary-select` is the **attested route** to the same contract, and it can run today:

```
2b glossary-select Step 0  → 2-RAILS/Bilingual-Glossaries/bo-en.md
                              every rendering the zero-shot actually used per lemma,
                              with counts, block IDs, and a lexical/inflectional split
4b glossary-select Step 1  → 3-TRANSFORMATIONS/Translations/<track>/termbase.md
                              one rendering chosen per lemma, decided by the track's
                              purpose, audience, register and the text's TOC
```

The two routes are not rivals; they meet at step 4. The attested route starts from what a
translation already did and asks *which of these words is right for this audience*; the
definition route starts from the commentary and asks *what does this term mean*. When
`glossary-select` cannot decide a lemma from the attested options, its fallback **is** the
Meaning column — so an unfinished step 2 becomes a per-term backlog rather than a blocker, and
every run reports which terms it needed a definition for.

Use the attested route when a block-aligned pivot translation exists and the question is which
English word to standardise on. Use the definition route when the term is contested in the
commentaries, or when no pivot translation renders it at all.

Both routes are still descriptive up to the moment of choice. **Step 4 / 4b is where choice
enters**, and it lives in `3-TRANSFORMATIONS/` either way.

**Why step 6 exists:** the lock is a prompt-side instruction. Measured against the DharmaMitra
endpoint on 2026-09-22, a batched call honoured 3 of 11 locks unglossed and 10 of 11 glossed,
the residual being an inflection rather than a substitution. Strong, not total — so the
guarantee comes from the check, not the asking. Evidence:
`4-SYSTEM/Skills/dharmamitra-termlocked/references/glossary-probe-2026-09-22.md`.

**Why steps 7 both exist:** `commentary-fact-check` grades against one commentary per run, which
is right for asking *does this match this authority* and wrong for a corpus of seventeen
independent commentaries with no ranking among them — it flags a faithful rendering of one
school whenever the run is against another. `claims-fact-check` grades against the consolidated
claims page, which has already separated Consensus from ⚑ Divergences, so a rendering that
follows one attested side of a divergence is graded **⚑ tradition-specific** rather than wrong.

---

## 5. Keyword and termbase layers

**`2-RAILS/Keywords/`** holds the 2026-08 Tārā-21 keyword run, promoted out of
`0-INBOX/AI_translation/keyword-extraction/output/` on 2026-09-22: 367 terms in the registry,
370 rows of the frequency matrix across 16 commentaries, 114 terms passing the viability gate
with 253 recorded gate failures, and 101 article subjects. This **supersedes the open question
in `keyword-extraction-methodology.md` §5 about where the registry lives** — the answer is
`2-RAILS/Keywords/`, per `$KEYWORDS` in `4-SYSTEM/Skills/_shared/PROFILES.md`.

Three gaps are carried forward honestly rather than backfilled, and are listed in
`2-RAILS/Keywords/About Keywords.md`: no synonyms/epithets, no `dropped` audit trail, and
similarity-based rather than tag-based quote exclusion.

**`2-RAILS/termbases/term-localization.md`** was seeded 2026-09-22 with the 345 registry terms
that occur in the root text, ordered by composite rank, Meaning and `En` empty. Unfilled rows
are inert in every consumer, so its length is not a commitment to filling all of it.

---

## 5a. Bilingual glossary pairs

None yet. `2-RAILS/Bilingual-Glossaries/` and its `Raw/` subfolder are empty (`.gitkeep` only).
The first pair created here follows `interlinear-gloss` → `glossary-extract-raw` →
`glossary-combine`, per `4-SYSTEM/CLAUDE.md` §7.

---

## 6. Active transformation tracks

One `Translations/` track exists (the DharmaMitra English machine baseline, §4); no
`Adaptations/` track has been started, and `Plans/` holds `21-Day-Plans-bo/`.

**The `kwiki` Wikipedia pipeline is this vault's one active generative system**, and it sits outside the `Translations`/`Adaptations`/`Plans` taxonomy `4-SYSTEM/CLAUDE.md` §9 defines. Its output lives at `3-TRANSFORMATIONS/Wikipedia/tara21/`:

| Path | Contents |
| --- | --- |
| `sources.yaml`, `terms.yaml`, `ledger.json` | Registry and per-term progress state |
| `work/aligned.json` | Root↔commentary alignment as of the last `kwiki align` run (historical — see below) |
| `articles/<term>/` | Per-term pipeline artifacts (extract → claims → outline → draft → audit → verify) |
| `review/{pending,approved,published}/` | The human pre-publication gate |

**Claims extraction moved out of the pipeline folder on 2026-08-04.** All three methods —
`commentary-claims` (fixed categories), `toc-scaffolded-claims` (re-bucketed under the tree),
`tree-guided-claims` (fresh, tree-scaffolded extraction) — now write to `2-RAILS/Claims/raw/` (see
`2-RAILS/About Rails.md` §6b) as first-class rails, not pipeline-owned experimental data. The
`opus`/`sonnet` one-off model-comparison runs and the resulting `claims/_comparison-report.md`
predate this move and are historical only — read as evidence for why `tree-guided-claims`'s five
guards exist, not as a live path. If those two direct-extraction methods are ever re-run, they
also belong under `2-RAILS/Claims/raw/` going forward, not back under this pipeline folder. (The `2-RAILS/Claims/` top level is reserved for consolidated topic pages — see `2-RAILS/About Rails.md` §6b.)

Ingest (raw text → annotated `1-SOURCES/` file → TOC tree → claims) is likewise now driven
end-to-end by vault skills (`raw-to-sources`, `commentary-resegment`, `toc-tree-extraction`,
`toc-tree-ingest`, `Transclusion-rootext-into-commentaries`, `commentary-verse-id`), not by
`kwiki commentaries`/`kwiki align`. The `kwiki` pipeline's own role is now scoped to article
generation only (stages 4–7, `articles/<term>/` onward) — see `/ingest`'s rewritten procedure.

**Why this is a sanctioned exception to the citation chain**, not an unnoticed violation of it: `4-SYSTEM/CLAUDE.md`'s citation chain requires `3-TRANSFORMATIONS/` to cite `2-RAILS/` only, never reaching past the rails into `1-SOURCES/` directly. The `kwiki` pipeline reaches directly into `1-SOURCES/Text/` and `1-SOURCES/Commentaries/` by design — its own citation discipline is the deterministic `kwiki verify` gate (stage 7: every quotation is checked character-for-character against its cited source file before an article may verify), which is a different but equally rigorous guarantee than the rails chain provides, built for a different output (a cited Wikipedia article rather than a rails-fed transformation track). Treat `3-TRANSFORMATIONS/Wikipedia/` as governed by the pipeline's own rules (`4-SYSTEM/Pipelines/wikipedia/CLAUDE.md`), not by `About Transformations.md`'s per-track contract files.

Two output paths of the pipeline **do** feed back into the standard rails/vault structure, and are governed by their own skills as usual:

- **`2-RAILS/Local-Wiki/<term>.md`** — emitted automatically by `kwiki article` (or on demand by `kwiki local-wiki`) once a term's article passes both the audit and the deterministic verify gate. Follows `4-SYSTEM/Skills/local-wiki-article/SKILL.md`'s format; still `status: draft` until a domain specialist promotes it, same as any other Local-Wiki article.
- **`1-SOURCES/Commentaries/`** itself — `kwiki commentaries <corpus>` promotes its finished output (sa-bcad headings, transclusion anchors, block IDs) back over the vault's own commentary files by default (`--promote`, on by default; `--no-promote` to review first). This is the vault's sanctioned exception to "`1-SOURCES/` is read-only": the reading-view invariant (`commentary.reading_view()`) guarantees the underlying Tibetan text is provably unchanged before any promotion is allowed to land.

---

## 7. Source-language tags used in this vault

| Tag | Script / System | Use in this vault |
| --- | --------------- | ------------------ |
| `-bo` | Unicode Tibetan | Every file in `1-SOURCES/` — the root text and all seventeen commentaries |

The default (and, currently, only) source language in this vault is `-bo`.

---

## 8. Where to look next

- [`../CLAUDE.md`](../CLAUDE.md) — the vault's operational quick-reference (this annex overrides it on the points above).
- [`../../1-SOURCES/About Sources.md`](../../1-SOURCES/About%20Sources.md) — source-file rules.
- [`../../2-RAILS/About Rails.md`](../../2-RAILS/About%20Rails.md) — rails schema.
- [`../../3-TRANSFORMATIONS/About Transformations.md`](../../3-TRANSFORMATIONS/About%20Transformations.md) — track and output rules (does not govern `Wikipedia/` — see §6).
- [`../Pipelines/wikipedia/CLAUDE.md`](../Pipelines/wikipedia/CLAUDE.md) — the `kwiki` pipeline's own operating rules.
- [`../Pipelines/wikipedia/STATE.md`](../Pipelines/wikipedia/STATE.md) — the pipeline's handover note; read first when picking up pipeline work.
