# Vault Annex — Twenty-One Homages to Tārā conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions that are specific to *this* vault: the **Praise to the Twenty-One Tārās** (སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ, *Ekaviṃśati-stotra*).

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins.

---

## 1. The text

This vault serves the **Praise to the Twenty-One Tārās** (སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ, "Homage in Twenty-One Verses to Ārya Tārā") — a short liturgical praise attributed by tradition to the Buddha Vairocana (author field: རྣམ་པར་སྣང་མཛད), transmitted in the Kangyur (Tohoku catalogue no. 438; BDRC `WA0RK0438`), and among the most widely recited Tārā liturgies across all Tibetan traditions.

The text is a single short work, not a multi-volume collection, so there is one row rather than a books/volumes table:

| Source-text file | Content |
| --- | --- |
| `1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md` | The root praise: one invocation block (`^I-1`) + 21 homage stanzas + 1 closing stanza (`^1-1`–`^1-22`) |

Sixteen of the seventeen registered commentaries on this praise are ingested (§3). No other root text is served by this vault.

---

## 2. Addressing scheme

**`verse_id_format`:** `chapter-verse`

**Format example:** `^1-1` (chapter 1, verse 1) … `^1-21` (chapter 1, verse 21); `^I-1` for the pre-stanza title/invocation block; `^a-1` … `^a-7` for the closing benefits section.

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

## 3. Registered commentary IDs

Every commentary file in `1-SOURCES/Commentaries/` declares a `registered_id` in its frontmatter. That short ID is the only string used to attribute claims to the commentary throughout `2-RAILS/` and throughout the `kwiki` pipeline's `3-TRANSFORMATIONS/Wikipedia/tara21/` output (its `sources.yaml` carries the same `registered_id` per entry, added 2026-08-04 — see §6).

Once assigned, a `registered_id` never changes. New commentaries must be added to the roster below before their `registered_id` is used in any rail.

| `registered_id` | Author (English) | School / tradition | Pipeline siglum | File |
| --- | --- | --- | --- | --- |
| `drakpa-gyaltsen` | Drakpa Gyaltsen ⚑ (see note) | Sakya | `TARAC02_DGT` | `སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md` |
| `gendun-drub` | Gendun Drub (1st Dalai Lama) | Gelug | `TARAC03_GDD` | `སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md` |
| `gendun-gyatso` | Gendun Gyatso Palzangpo (2nd Dalai Lama) | Gelug | `TARAC04_GDG` | `ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md` |
| `taranatha` | Tāranātha | Jonang | `TARAC05_TRN` | `ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md` |
| `anon-utpala` | Ngulchu Dharmabhadra | Gelug | `TARAC06_NDB` | `སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md` |
| `konchok-thabkhe` | Konchok Thabkhe (a.k.a. Tenpa Gyatso) | Gelug | `TARAC07_KTK` | `ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md` |
| `tenga-tulku` | Dorlob Tenga Tulku | (unaffiliated / Nyima Bepé tradition) | `TARAC08_DTG` | `ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས་སོ།། །.md` |
| `anon-trinle-char` | (colophon lost; anonymous) | (unaffiliated / Nyima Bepé tradition) | `TARAC09_ANON` | `སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md` |
| `pema-namgyal` | Domboba Pema Namgyal | (unaffiliated) | `TARAC10_DPN` | `ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།.md` |
| `karma-maitri` | Karma Maitri | (unaffiliated) | `TARAC11_KMT` | `ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md` |
| `palden-sherab` | Khenchen Palden Sherab | Nyingma | `TARAC12_PDS` | `རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ་དད་བརྩོན་བྱང་ཆུབ་སེམས་མཆོག་གི་པདྨའི་གཞོན་ནུ་ཁ་འབྱེད་པའི་ཐབས་ཤེས་ཉི་ཟླའི་འཛུམ་རླབས་ཞེས་བྱ་བཞུགས།.md` |
| `tenzin-dhonzang` | Sermé Tsang Geshe Tenzin Dhonzang | Gelug | `TARAC13_TDZ` | `སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ།.md` |
| `lobsang-dawa` | Geshe Lobsang Dawa (compiler) | Gelug | `TARAC14_LZD` | `སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md` |
| `sangye-nyentrul` | Sangye Nyentrul | (unaffiliated) | `TARAC15_SNT` | `རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་ཉུང་ངུར་བཀོད་པ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས།.md` |
| `sungrab-tulku` | Drepa Ratreng Sungrab Tulku | Gelug (contemporary) | `TARAC16_PSR` | `སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md` |
| `tsultrim-namdak` | Khenpo Tsultrim Namdak | Kagyu | `TARAC17_TSN` | `སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md` |
| `anon-rnam-snang` | Dharmabhadra ⚑ (see note) | — | **not in pipeline corpus** | `ཡང་དག་པ་རྫོགས་པའི་སངས་རྒྱས་རྣམ་པར་སྣང་མཛད་ཀྱིས་གསུངས་པ་འཕགས་མ་སྒྲོལ་མ་ལ་བསྟོད་པ་ཕྱག་འཚལ་བ་ཉི་ཤུ་རྩ་གཅིག.md` |

**⚑ Two open flags on this roster, for a human to resolve, not silently fixed here:**

- **`drakpa-gyaltsen`'s author identity is inconsistent across this file's own metadata.** Its frontmatter names the author "Gendun Drakpa Gyaltsen" (a Gelug-style name), but the pipeline corpus's `sources.yaml` entry for the same text (`TARAC02_DGT`) and the commentary's own colophon (`…ལོཙྪ་བ་གཉན་གྱིས་བསྒྱུར་བ། རྗེ་བཙུན་ཆེན་པོ་གྲགས་པ་རྒྱལ་མཚན་གྱིས་གཏན་ལ་ཕབ་པའོ།།`) both point to "Jetsün Drakpa Gyaltsen," which reads as the Sakya patriarch (1147–1216), not a Gelug figure. Worth a philological check before either value is trusted in output.
- **`anon-rnam-snang`'s title is textually identical to the root text's own title** (STATE.md flagged this; it has no counterpart in the pipeline corpus, per §6). Whether this file is a genuine commentary or a second copy of the root deserves a human read before it is cited as a commentary anywhere.

**Tier ordering.** This praise has no single root commentary with named sub-commentaries the way a scholastic treatise does — its seventeen commentaries are independent works from five schools plus several unaffiliated authors. There is therefore no default primary/secondary ranking. When a verse package or claims comparison presents multiple commentaries together, group by school in the order the roster lists them above (Sakya → Gelug → Jonang → Nyingma → Kagyu → unaffiliated), and within a school by the roster's own order; do not invent a "the real commentary is X" hierarchy this tradition does not have.

---

## 4. Language tracks

| Tag | Language | Translation track | Plan stream |
| --- | -------- | ------------------ | ----------- |
| `bo` | Tibetan | — (source; every `1-SOURCES/` file in this vault) | — |

No target-language translation track exists yet under `3-TRANSFORMATIONS/Translations/` (the folder holds only its `About` file). The `kwiki` pipeline's `article.en.md` files (`3-TRANSFORMATIONS/Wikipedia/tara21/articles/<term>/article.en.md`) are **English check-translations for human review**, not a registered `en` track — they exist to let a reviewer who reads English confirm a Tibetan draft's content, and are not translation-track output governed by `3-TRANSFORMATIONS/About Transformations.md`'s per-track contracts (`requirements.md`/`termbase.md`/`audience.md`). A genuine `en` (or any other) translation track, if started, follows the standard process: create `3-TRANSFORMATIONS/Translations/en-<descriptor>/`, write its three contract files, and populate this table.

---

## 5. Bilingual glossary pairs

None yet. `2-RAILS/Bilingual-Glossaries/` and its `Raw/` subfolder are empty (`.gitkeep` only). The first pair created here follows `interlinear-gloss` → `glossary-extract-raw` → `glossary-combine`, per `4-SYSTEM/CLAUDE.md` §7.

---

## 6. Active transformation tracks

No `Translations/`, `Adaptations/`, or `Plans/` track has been started under `3-TRANSFORMATIONS/` (each holds only its `About` file).

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
