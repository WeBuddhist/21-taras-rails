# Skills Catalog

This file catalogues every skill available in a Railroads vault, grouped by workflow phase. Each entry names the skill, states its purpose, describes its inputs and outputs, and points to the SKILL.md that operationalises it.

Skills that already exist are marked **[exists]**. Skills that are planned but not yet written are marked **[planned]**.

The pipeline reads top-to-bottom: source ingestion populates `1-SOURCES/`, the rails-building skills turn those sources into `2-RAILS/` context (Sections / Verses / Local-Wiki / Bilingual Glossaries), the translation skills consume those rails to produce `3-TRANSFORMATIONS/Translations/<track-name>/`, and the QA skill checks the output back against the rails.

---

## Source ingestion skills

These skills bring raw material into `1-SOURCES/` in a consistent, citation-ready format.

### `epub-to-markdown` **[exists]**
Converts EPUB files (commentaries, reference texts) into formatted Obsidian markdown with block IDs, headings, and frontmatter.
→ [`epub-to-markdown/SKILL.md`](epub-to-markdown/SKILL.md)

### `json-to-source-text` **[exists]**
Converts JSON exports of root texts (e.g. from tipitaka.org or SuttaCentral) into formatted source-text markdown files. Includes example converters for tipitaka.org and English paired translations; new source schemas get their own converter in `json-to-source-text/converters/`.
→ [`json-to-source-text/SKILL.md`](json-to-source-text/SKILL.md)

### `json-to-commentary` **[exists]**
Converts JSON exports of classical commentaries into formatted commentary markdown files.
→ [`json-to-commentary/SKILL.md`](json-to-commentary/SKILL.md)

### `format-root-text` **[exists]**
Normalises an existing root-text file: heading structure, block IDs, verse formatting.
→ [`format-root-text/SKILL.md`](format-root-text/SKILL.md)

### `format-commentary` **[exists]**
Normalises an existing commentary file: OCR cleanup, heading structure, paragraph granularity, block IDs.
→ [`format-commentary/SKILL.md`](format-commentary/SKILL.md)

### `add-toc` **[exists]**
Inserts or regenerates a table of contents in a source or rails file.
→ [`add-toc/SKILL.md`](add-toc/SKILL.md)

---

The six skills below form the **deterministic ingest chain** for Tibetan material — clean → format/segment → tag → lint → transclude. They were ported from `webuddhist-library-data-pipeline` and `bodhisattvacharyavatara-rails` via the IATS-2026 repo, where they have been run in production over sixteen commentaries. Each bundles tested Python scripts under its own `scripts/`, dry-run by default, and each script asserts no-loss (output minus whitespace must equal input minus whitespace) before it writes. They are also the ingest stages the Wikipedia pipeline drives — see [`../Pipelines/wikipedia/README.md`](../Pipelines/wikipedia/README.md).

### `clean-raw-text` **[exists]**
**Purpose:** Strip the mechanical debris OCR and PDF-to-text conversion leave behind — repeated page headers and footers, page-number markers, mid-word spaces from justification engines, non-breaking tsheg characters. Does not restructure headings or add block IDs; that is the format skills' job.
**Inputs:** One raw or OCR-derived text file.
**Outputs:** A cleaned draft, plus the targeted per-text cleaning script it generated. Worked examples in `clean-raw-text/examples/`.
→ [`clean-raw-text/SKILL.md`](clean-raw-text/SKILL.md)

### `format-tibetan-root-text` **[exists]**
**Purpose:** Format a Tibetan root text into clean navigable verse — one stanza per paragraph, each verse-line on its own line, `^chapter-verse` block IDs, `^N-0` chapter anchors. The Tibetan-specific counterpart to the generic `format-root-text`; use this one for `bo` material.
**Inputs:** A cleaned Tibetan root-text file.
**Outputs:** A segmented root-text file. Two bundled formatters: `scripts/format_bca.py` (colophon-driven) and `scripts/format_bo_root.py` (table-driven).
→ [`format-tibetan-root-text/SKILL.md`](format-tibetan-root-text/SKILL.md)

### `commentary-segmentation` **[exists]**
**Purpose:** Break an OCR-clean but under-segmented Tibetan commentary into short, individually-citable blocks, using the text's own functional signals — quotation frames, objection/answer markers, sa-bcad enumerations, sentence-final particles, verse meter. Runs after `format-commentary`'s OCR cleanup and before block-ID stamping.
**Inputs:** One commentary file from `1-SOURCES/Commentaries/`.
**Outputs:** The same file segmented into citation-sized blocks (1–2 sentences of prose, one stanza, or one quotation each). Four scripts, no-loss gated.
→ [`commentary-segmentation/SKILL.md`](commentary-segmentation/SKILL.md)

### `tag-inline-toc` **[exists]**
**Purpose:** Identify inline structural announcement phrases (*sa bcad*), wrap the announced terms in wikilinks, and insert standalone heading lines with block IDs — the convention in `4-SYSTEM/CLAUDE.md` §5b. Optional: skip it for texts with no inline announcements.
**Inputs:** A formatted root-text or commentary file.
**Outputs:** The same file with tagged announcements and heading lines.
→ [`tag-inline-toc/SKILL.md`](tag-inline-toc/SKILL.md)

### `lint-annotations` **[exists]**
**Purpose:** Annotation-convention linter — verse structure, lines per verse, block IDs, verse IDs, heading anchors, stray footnote digits. Sequences existing tested checkers and reads the result back in plain language; contains no detection logic of its own. **Report-only:** never fixes anything without explicit human confirmation.
**Inputs:** One formatted text file.
**Outputs:** A lint report.
→ [`lint-annotations/SKILL.md`](lint-annotations/SKILL.md)

### `Transclusion-rootext-into-commentaries` **[exists]**
**Purpose:** Place root-text verse transclusions inside a commentary and format the blank-line spacing around each one so the sa-bcad outline reads correctly in Obsidian. Three deterministic stages: insert `![[root#^N-V]]` before each verse's first full inline quotation, remove the blank line above it, add a blank line before the introducing sa-bcad block.
**Inputs:** One commentary file and its root text, both block-ID'd.
**Outputs:** The commentary with transclusion anchors and corrected spacing. Dry-run by default; `--apply` to write.
→ [`Transclusion-rootext-into-commentaries/SKILL.md`](Transclusion-rootext-into-commentaries/SKILL.md)

---

### `root-text-frontmatter` **[exists]**
Generates complete YAML frontmatter for a root-text file in `1-SOURCES/Text/` by extracting metadata from its title, colophon, and opening content.
→ [`root-text-frontmatter/SKILL.md`](root-text-frontmatter/SKILL.md)

### `commentary-frontmatter` **[exists]**
Generates complete YAML frontmatter for a commentary file in `1-SOURCES/Commentaries/`, including the `registered_id`, `root_text`, and `covers_verses` fields.
→ [`commentary-frontmatter/SKILL.md`](commentary-frontmatter/SKILL.md)

### `translation-frontmatter` **[exists]**
Generates complete YAML frontmatter for a translation file in `1-SOURCES/Translations/`, including translator, target language, and `translation_basis`.
→ [`translation-frontmatter/SKILL.md`](translation-frontmatter/SKILL.md)

### `reference-frontmatter` **[exists]**
Generates complete YAML frontmatter for a secondary-literature or reference file in `1-SOURCES/References/`.
→ [`reference-frontmatter/SKILL.md`](reference-frontmatter/SKILL.md)

---

## Rails-building skills (context preparation for translation)

These skills populate `2-RAILS/` with the structured context that translation and QA skills consume.

### `section-summary-raw` **[exists]**
**Purpose:** Generate a summary of one table-of-contents node in the original language, drawn from a single commentary.
**Inputs:** Commentary file(s) in `1-SOURCES/`, the TOC node to summarise.
**Outputs:** One summary file per commentary under `2-RAILS/Sections/Raw/<commentary-id>/<node-id>.md`.
**Rules:** Use only the terminology the commentary itself uses. No translation. No paraphrase beyond compression. Every claim cites a block ID from the source file.
→ [`section-summary-raw/SKILL.md`](section-summary-raw/SKILL.md)

### `section-summary-combined` **[exists]**
**Purpose:** Combine the per-commentary raw summaries for one TOC node and add an English translation of the combined summary.
**Inputs:** All raw summary files for the target node under `2-RAILS/Sections/Raw/`.
**Outputs:** One combined file at `2-RAILS/Sections/<node-id>.md` containing the original-language synthesis and an English translation.
→ [`section-summary-combined/SKILL.md`](section-summary-combined/SKILL.md)

### `verse-context` **[exists]**
**Purpose:** Build the verse-level context file for one verse.
**Inputs:** Root-text verse (from `1-SOURCES/`), all commentary passages that discuss it (via block transclusions from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Verses/<verse-id>.md` containing: (1) transclusions of commentary passages, (2) a synthesis of the commentators' interpretations in the original language, (3) a disambiguated restatement of the verse in the original language precise enough to exclude any mistranslation.
→ [`verse-context/SKILL.md`](verse-context/SKILL.md)

### `local-wiki-article` **[exists]**
**Purpose:** Create or update a Local-Wiki article for one key term.
**Inputs:** Commentary passages that explain or define the term (via block citations from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Local-Wiki/<term>_(<disambiguator>).md` containing: cited commentary explanations in the original language, and a short contextual definition drafted from those citations (also in the original language).
→ [`local-wiki-article/SKILL.md`](local-wiki-article/SKILL.md)

### `term-definition-from-commentaries` **[exists]**
**Purpose:** Fill the Meaning column of a term-localization table by locating definitional passages in the commentaries and extracting them **verbatim**, formatted in traditional Tibetan quotation style. A definitional passage is one using the formulaic markers `[term]ནི་`, `[term]ཞེས་པ་ནི་`, `[term]ཅེས་པ་ནི་`. The skill never paraphrases, summarises, or writes explanatory text of its own.
**Inputs:** One or more Tibetan terms, plus the commentary files in `1-SOURCES/Commentaries/`.
**Outputs:** The term-localization table under `2-RAILS/Local-Wiki/`, updated in place — one quotation entry per commentary passage found.
**Note:** written against the BCA vault's `BCA-Term-Localization.md`; repoint the table path for this vault before running.
→ [`term-definition-from-commentaries/SKILL.md`](term-definition-from-commentaries/SKILL.md)

### `english-keyword-extraction` **[exists]**
**Purpose:** Extract ranked keywords per verse from an **English translation** of a Tibetan root text (YAKE + spaCy, optional TF-IDF against a general-English IDF corpus), then enrich each English keyword with its contextually correct Tibetan equivalent — producing a bilingual en↔bo key-term list keyed by verse block ID. The translation-mediated route to key terms, for when Tibetan-only extraction over-returns or fragments (tokenization is contested and no standard reference corpus exists).
**Inputs:** A block-ID-preserving English translation of the root text (see `zeroshot-translator`), plus the Tibetan root text.
**Outputs:** A ranked bilingual en↔bo candidate term list for human review.
→ [`english-keyword-extraction/SKILL.md`](english-keyword-extraction/SKILL.md)

### `interlinear-gloss` **[exists]**
**Purpose:** For one root text + one translation, build an interlinear gloss file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md` pairing them verse by verse. Each verse becomes a `gloss` block in the Obsidian Interlinear Glossing plugin format (`\gla` source tokens, `\glb` morphology/lemma, `\glc` token-by-token target glosses, `\ex` free translation). Token-level alignment lives here so every downstream bilingual glossary step reads from one place.
**Inputs:** `1-SOURCES/Text/<root-text>.md`, one translation under `1-SOURCES/Translations/`.
**Outputs:** One gloss file per translation under `2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang>-gloss.md`.
→ [`interlinear-gloss/SKILL.md`](interlinear-gloss/SKILL.md)

### `glossary-extract-raw` **[exists]**
**Purpose:** Extract every source-language keyword and the rendering(s) it receives, from one interlinear gloss file, into a raw per-source bilingual glossary.
**Inputs:** One gloss file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md`.
**Outputs:** One bilingual glossary file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>.md` with a table mapping source lemma → rendering used in that translation.
→ [`glossary-extract-raw/SKILL.md`](glossary-extract-raw/SKILL.md)

### `glossary-combine` **[exists]**
**Purpose:** Merge all raw bilingual glossary files for one language pair into a single consolidated bilingual glossary.
**Inputs:** All relevant files under `2-RAILS/Bilingual-Glossaries/Raw/`.
**Outputs:** One consolidated bilingual glossary at `2-RAILS/Bilingual-Glossaries/<lang-pair>.md` showing every attested rendering side by side.
→ [`glossary-combine/SKILL.md`](glossary-combine/SKILL.md)

### `glossary-select` **[exists]**
**Purpose:** Build the prescriptive per-track termbase for one track by selecting the preferred rendering for each term from the consolidated bilingual glossary, guided by the track's `requirements.md`. If no existing rendering is satisfactory, derive one from the Local-Wiki article for that term and feed the new rendering back into the consolidated bilingual glossary.
**Inputs:** `2-RAILS/Bilingual-Glossaries/<lang-pair>.md`, `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, Local-Wiki articles as needed.
**Outputs:** `3-TRANSFORMATIONS/Translations/<track-name>/termbase.md` — the prescriptive termbase scoped to keywords that appear in the text being translated; plus updates to the consolidated bilingual glossary for any new derived renderings.
→ [`glossary-select/SKILL.md`](glossary-select/SKILL.md)

### `commentary-claims` **[exists]**
**Purpose:** Extract every distinct claim a single commentary makes into a per-commentary claims inventory, in the commentary's own language, read in isolation from the root text and from every other commentary.
**Inputs:** Exactly one commentary file from `1-SOURCES/Commentaries/` carrying a `registered_id` in its frontmatter.
**Outputs:** One file at `2-RAILS/Claims/<registered-id>.md` — claims grouped in nine fixed categories (framing, word-gloss, iconography, doctrinal, activity, practice, benefit, attribution, internal tensions), each with the original-language statement, a one-line English gloss, a type, and a segment citation, plus a coverage log.
→ [`commentary-claims/SKILL.md`](commentary-claims/SKILL.md)

### `toc-candidate-extraction` **[exists]**
**Purpose:** Extract every ས་བཅད (sa bcad) structural-outline candidate — announcements, node headers, closing counts — from a Tibetan commentary, prioritising recall. Imported from the `bodhisattvacharyavatara-rails` vault.
**Inputs:** One Tibetan commentary/root-text file, chunked by the bundled `scripts/chunk_file.py`.
**Outputs:** One merged file at `0-INBOX/toc-candidates-<commentary-id>.md`, plus resumable per-chunk staging under `0-INBOX/temp/<commentary-id>/`.
→ [`toc-candidate-extraction/SKILL.md`](toc-candidate-extraction/SKILL.md)

### `toc-tree-extraction` **[exists]**
**Purpose:** Build the full nested, decimal-numbered ས་བཅད TOC tree for a Tibetan commentary via a four-pass isolated-subagent pipeline (candidates → verbatim enumerations → nested tree → deterministic QC + repair). Claude-native port of the Gemini-based `extract_toc_tree.py`; imported from the `bodhisattvacharyavatara-rails` vault.
**Inputs:** One Tibetan commentary/root-text file, normally under `1-SOURCES/Commentaries/`.
**Outputs:** `0-INBOX/toc-candidates-<id>.md`, `0-INBOX/toc-enumerations-<id>.md`, `0-INBOX/toc-tree-<id>.md`, `0-INBOX/toc-tree-qc-<id>.md`, plus resumable per-chunk staging under `0-INBOX/temp/TOC-<id>/`.
→ [`toc-tree-extraction/SKILL.md`](toc-tree-extraction/SKILL.md)

### `toc-scaffolded-claims` **[exists]**
**Purpose:** Extract every distinct claim/fact a single commentary makes into one consolidated claims file, organised by that commentary's own decimal-numbered TOC tree instead of fixed A–I categories, with every claim anchored to the source-attested referent it concerns (figure/form, person, place, text, event, date) — so several commentaries on the same root text can be compared section by section and each claim is traceable to something concrete.
**Inputs:** One commentary file from `1-SOURCES/Commentaries/` with a `registered_id`, plus its TOC tree from `toc-tree-extraction` (or the Gemini script).
**Outputs:** One file at `2-RAILS/Claims/toc-scaffolded/<registered-id>.md` — a Grounding index of attested referents, then claims grouped under headings mirroring the TOC tree's own nodes, each with the original-language statement, a one-line English gloss, a type, a referent anchor (or explicit `[unanchored]`), and a citation, plus internal-tensions and unanchored-claims rollups and a coverage log.
→ [`toc-scaffolded-claims/SKILL.md`](toc-scaffolded-claims/SKILL.md)

---

## Translation requirements skills

### `requirements-author` **[planned]**
**Purpose:** Author or audit a track's `requirements.md` so it contains everything the `translate-section` skill needs to behave consistently across the whole text.
**Inputs:** The track folder `3-TRANSFORMATIONS/Translations/<track-name>/`; the per-track termbase (if it exists yet); samples of any prior translation in the same target language.
**Outputs:** A complete `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, written in the target language.
→ `requirements-author/SKILL.md` *(to be written)*

---

## Translation skills

### `zeroshot-translator` **[exists]**
**Purpose:** Produce a direct, zero-shot translation of a source text into a target language, guided by an audience profile — **no termbase at all**: no keyword extraction, no sense-tagging, no locked terminology. The fast path, for a first draft or a quick comparison, as an alternative to the full rails route (`glossary-*` → `translate-section`).
**Inputs:** Source text (or its split chapters); target language, named by the user; an existing audience profile.
**Outputs:** A translation, **pada-aligned to the source** — each segment's translation mirrors its source's exact line count, with every segment ID preserved in the same position. Structural fidelity applies even without a termbase.
**Note:** its block-ID-preserving output is what `english-keyword-extraction` consumes.
→ [`zeroshot-translator/SKILL.md`](zeroshot-translator/SKILL.md)

### `translate-section` **[planned]**
**Purpose:** Translate a small batch of TOC nodes into the target language.
**Inputs:** `requirements.md`, `termbase.md`, `audience.md` for the track; relevant section and verse packages from `2-RAILS/`; Local-Wiki articles as needed.
**Outputs:** Updated translation file(s) in `3-TRANSFORMATIONS/Translations/<track-name>/`. Each file's frontmatter lists the rail files it was generated from.
**Rules:** Translate small batches only — one or a few TOC nodes at a time. Every keyword rendering must match the per-track termbase. Introduce no new rendering without first adding it to the termbase and feeding it back into the consolidated bilingual glossary.
→ `translate-section/SKILL.md` *(to be written)*

---

## Translation QA skills

### `translation-qa` **[planned]**
**Purpose:** Review a translated section against the MQM translation error taxonomy, the track requirements, and the source rails.
**Inputs:** Translated section(s); `requirements.md`; `termbase.md`; relevant `2-RAILS/` files.
**Outputs:** Appended entries in `3-TRANSFORMATIONS/Translations/<track-name>/qa-report.md`. Each entry records: the segment, MQM error category, severity (critical / major / minor), and a suggested correction.
→ `translation-qa/SKILL.md` *(to be written)*

### `style-consistency-check` **[planned]**
**Purpose:** Catch style drift over long texts — creeping changes in register, sentence length, verse formatting, list handling, term gloss style.
**Inputs:** All translated files in `3-TRANSFORMATIONS/Translations/<track-name>/`; `requirements.md`; termbase.
**Outputs:** A style-drift section appended to `qa-report.md`, with span references back to the offending passages.
→ `style-consistency-check/SKILL.md` *(to be written)*

---

## Utility skills

### `source-property-extractor` **[exists]**
Extracts structured metadata (author, date, edition, language, publisher) from a source file and writes it to the frontmatter.
→ [`source-property-extractor/SKILL.md`](source-property-extractor/SKILL.md)

### `property-creator` **[exists]**
Creates or updates Obsidian frontmatter properties on a file.
→ [`property-creator/SKILL.md`](property-creator/SKILL.md)

### `structural-outline-ingest` **[exists]**
Ingests a structural outline (TOC) into a source or rails file.
→ [`structural-outline-ingest/SKILL.md`](structural-outline-ingest/SKILL.md)

---

## System skills

These skills operate on the vault's own structure — creating new skills, maintaining registrations, and auditing integrity. They are meta-level tools for contributors, not pipeline steps.

### `create-skill` **[exists]**
**Purpose:** Scaffold a new skill completely and correctly in a single pass — creates the SKILL.md, registers it in SKILLS-CATALOG.md, creates the slash command file, and optionally adds it to the CLAUDE.md quick-reference table.
**Inputs:** Skill name, purpose sentence, catalog section, inputs/outputs description, and whether it belongs in the CLAUDE.md §12 table.
**Outputs:** `4-SYSTEM/Skills/<skill-name>/SKILL.md`, a new catalog entry, `.claude/commands/<skill-name>.md`, and optionally a new §12 table row in `4-SYSTEM/CLAUDE.md`.
→ [`create-skill/SKILL.md`](create-skill/SKILL.md)

---

## Maintenance skills

These skills check and report on vault integrity. They are read-only and safe to run on a schedule. They never modify vault content — they produce reports for human action.

### `vault-audit` **[exists]**
**Purpose:** Read-only weekly audit of the vault. Checks that every skill folder is registered in the catalog and has a command file; that 2-RAILS and 3-TRANSFORMATIONS files have required frontmatter; that no 3-TRANSFORMATIONS file references 1-SOURCES directly; that no complete output depends on a draft rail; that 0-INBOX/temp/ has no stale files; and that no internal wiki links are dead.
**Inputs:** None — operates on the vault as a whole.
**Outputs:** One dated report at `0-INBOX/vault-audit-<YYYY-MM-DD>.md` with checkboxed issues per category.
→ [`vault-audit/SKILL.md`](vault-audit/SKILL.md)

---

## Pipelines — not skills

A **pipeline** is a multi-stage program with its own code, prompts, gates and CLI. It is not invoked as a skill; it is installed and run. Pipelines live under [`../Pipelines/`](../Pipelines/), one folder each, and are listed here so the skill-first rule in `4-SYSTEM/CLAUDE.md` does not send you looking for a skill that was never going to exist.

### `Pipelines/wikipedia` — Tibetan Wikipedia article generation (`kwiki`)
Takes a Tibetan root text plus its commentaries and produces cited Tibetan Wikipedia articles, creating or updating them on bo.wikipedia behind a human review gate. Ported from the IATS-2026 repo on 2026-08-03; 547 tests pass.

Its stages: align root↔commentaries → seed key terms → extract cited passages → build an atomic claims table → outline → draft (claims-only) → optional literary polish → LLM audit → **deterministic verification gate** → dry-run publish. The gate uses no LLM: a quotation that does not appear character-for-character in its cited source file fails the build.

It **drives the six ingest-chain skills above** — `kwiki commentaries` resolves their scripts directly out of `4-SYSTEM/Skills/`. It also carries the team's canonical 17-step pipeline as one skill per step under `Pipelines/wikipedia/cowork-pipeline/`, kept verbatim; those are reference documents, not vault skills.

Slash commands: `/ingest`, `/pipeline`, `/publish`.
→ [`../Pipelines/wikipedia/README.md`](../Pipelines/wikipedia/README.md)
