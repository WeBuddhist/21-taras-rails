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

### `raw-to-sources` **[exists]**
**Purpose:** Bring one raw OCR/segmentation text file into `1-SOURCES/` as a cleaned, frontmattered root-text or commentary file — the first step of the ingest chain, before any segmentation, TOC, or block IDs.
**Inputs:** One raw `.txt`/`.docx.txt` file, `--type root|commentary`, and optionally known metadata (title/author/tradition) from a curated catalog.
**Outputs:** `1-SOURCES/Text/<title>.md` or `1-SOURCES/Commentaries/<title>.md` — cleaned body, complete easy-field frontmatter, still unsegmented and un-block-ID'd.
→ [`raw-to-sources/SKILL.md`](raw-to-sources/SKILL.md)

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

### `clean-commentary-text` **[exists]**
**Purpose:** The commentary counterpart of `clean-raw-text` — inspects a raw Tibetan commentary for page markers, running headers/footers, extra spaces and encoding artifacts, generates a targeted cleaning script, runs it, and saves the cleaned draft.
**Inputs:** One raw or OCR-derived commentary.
**Outputs:** A cleaned draft in `0-INBOX/`, plus the per-text script it generated.
→ [`clean-commentary-text/SKILL.md`](clean-commentary-text/SKILL.md)

### `commentary-verse-id` **[exists]**
**Purpose:** Stamp `^chapter-n` block IDs onto a segmented Tibetan commentary, deriving the chapter from the nearest preceding root-text transclusion. Blocks before the first transclusion are tagged chapter 0 rather than left untagged — so every block is citable, including the front matter.
**Inputs:** A segmented commentary that already transcludes its root text.
**Outputs:** The same file with a block ID on every segment.
→ [`commentary-verse-id/SKILL.md`](commentary-verse-id/SKILL.md)

### `commentary-resegment` **[exists]**
**Purpose:** Re-paragraph a commentary that has one clause per line into readable sense-unit paragraphs. The model decides boundaries **by meaning** — content and context — not by grammar rules or particles.
**Inputs:** A one-clause-per-line commentary.
**Outputs:** The same text re-paragraphed, with a QC check.
→ [`commentary-resegment/SKILL.md`](commentary-resegment/SKILL.md)

### `block-resegmentation` **[exists]**
**Purpose:** Re-draw block boundaries in a Stage-1 segmented commentary into semantically coherent, citation-sized units. The model flags merge/split operations rather than rewriting. Runs after `commentary-segmentation` and after the TOC step.
**Inputs:** A Stage-1 segmented commentary with its TOC inserted.
**Outputs:** The same file with revised block boundaries, plus a QC report.
→ [`block-resegmentation/SKILL.md`](block-resegmentation/SKILL.md)

### `transclusion` **[exists]**
**Purpose:** Insert Obsidian block-transclusion links for root-text verses into another root-text version or into commentary files, at the correct structural position. The general-purpose sibling of `Transclusion-rootext-into-commentaries`, which additionally fixes sa-bcad spacing and bundles the three-stage script pipeline.
**Inputs:** A root text and the file to transclude into, both block-ID'd.
**Outputs:** The target file with `![[root#^N-V]]` links in place.
→ [`transclusion/SKILL.md`](transclusion/SKILL.md)

### `toc-tree-ingest` **[exists]**
**Purpose:** Ingest a TOC tree produced by `toc-tree-extraction` into a commentary by inserting markdown headings with block IDs, in a single document-order pass, in place in the canonical `1-SOURCES/` file. The write half of the TOC chain — `toc-tree-extraction` builds the tree, this one places it.
**Inputs:** A finished tree (`2-RAILS/Sections/Raw/toc-tree/<id>.md`, preferred) and the commentary it belongs to.
**Outputs:** The same `1-SOURCES/Commentaries/<id>.md` file, updated in place with heading lines and `^N-…-0` heading IDs — no side-copy.
→ [`toc-tree-ingest/SKILL.md`](toc-tree-ingest/SKILL.md)

### `Outline-Extractor` **[exists]**
**Purpose:** Extract the structural outline (ས་བཅད) from a Tibetan commentary into a nested `.md` file — YAML frontmatter, heading-based hierarchy for levels 1–5, indented bold list items below that.
**Inputs:** One Tibetan commentary.
**Outputs:** One structured outline file.
→ [`Outline-Extractor/SKILL.md`](Outline-Extractor/SKILL.md)

### `tibetan-ocr-quality` **[exists]**
**Purpose:** Score a Tibetan OCR output by calculating perplexity with KenLM over Botok-normalised text — a number for "is this OCR good enough to ingest?" before any of the chain runs.
**Inputs:** One OCR output file.
**Outputs:** A perplexity score.
→ [`tibetan-ocr-quality/SKILL.md`](tibetan-ocr-quality/SKILL.md)

### `colophon-metadata-extractor` **[exists]**
**Purpose:** Extract author, title and language from a Tibetan text's colophon (last 200 syllables) and opening (first 200 syllables), and populate the file's YAML frontmatter in place. Does not rename or move the file.
**Inputs:** One Tibetan source file.
**Outputs:** The same file with frontmatter filled.
→ [`colophon-metadata-extractor/SKILL.md`](colophon-metadata-extractor/SKILL.md)

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
Generates complete YAML frontmatter for a commentary file in `1-SOURCES/Commentaries/`, including the `registered_id`, `root_text`, and `covers_verses` fields. Also documents the human-supplied `author_in_use` key (the in-article name form used by the wiki-article skills) — the LLM never writes its value.
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

### `commentary-fact-check` **[exists]**
**Purpose:** Audit an English translation verse by verse against a Tibetan commentary that transcludes the root text, using strict **term-by-term alignment** — for every content word the commentary glosses, check the translation renders it — rather than a gist/comprehension check.
**Inputs:** A graded English translation and the commentary that transcludes the root.
**Outputs:** A `commentary-fact-check-report-<grade>.md` with ⚠ discrepancies.
**Note:** imported from `bodhisattvacharyavatara-rails`; its paths and grade names are BCA-specific — repoint them before running here.
→ [`commentary-fact-check/SKILL.md`](commentary-fact-check/SKILL.md)

### `commentary-fact-check-apply-fixes` **[exists]**
**Purpose:** Apply the ⚠ discrepancies already logged in a `commentary-fact-check` report to the graded translation, one grade at a time.
**Inputs:** A fact-check report and the translation it grades.
**Outputs:** The translation, corrected.
**Note:** same BCA-path caveat as `commentary-fact-check`.
→ [`commentary-fact-check-apply-fixes/SKILL.md`](commentary-fact-check-apply-fixes/SKILL.md)

### `commentary-claims` **[exists]**
**Purpose:** Extract every distinct claim a single commentary makes into a per-commentary claims inventory, in the commentary's own language, read in isolation from the root text and from every other commentary.
**Inputs:** Exactly one commentary file from `1-SOURCES/Commentaries/` carrying a `registered_id` in its frontmatter.
**Outputs:** One file at `2-RAILS/Claims/raw/<registered-id>.md` — claims grouped in nine fixed categories (framing, word-gloss, iconography, doctrinal, activity, practice, benefit, attribution, internal tensions), each with the original-language statement, a one-line English gloss, a type, and a segment citation, plus a coverage log.
→ [`commentary-claims/SKILL.md`](commentary-claims/SKILL.md)

### `toc-candidate-extraction` **[exists]**
**Purpose:** Extract every ས་བཅད (sa bcad) structural-outline candidate — announcements, node headers, closing counts — from a Tibetan commentary, prioritising recall. Imported from the `bodhisattvacharyavatara-rails` vault.
**Inputs:** One Tibetan commentary/root-text file, chunked by the bundled `scripts/chunk_file.py`.
**Outputs:** One merged file at `0-INBOX/toc-candidates-<commentary-id>.md`, plus resumable per-chunk staging under `0-INBOX/temp/<commentary-id>/`.
→ [`toc-candidate-extraction/SKILL.md`](toc-candidate-extraction/SKILL.md)

### `toc-tree-extraction` **[exists]**
**Purpose:** Build the full nested, decimal-numbered ས་བཅད TOC tree for a Tibetan commentary via a four-pass isolated-subagent pipeline (candidates → verbatim enumerations → nested tree → deterministic QC + repair). Claude-native port of the Gemini-based `extract_toc_tree.py`; imported from the `bodhisattvacharyavatara-rails` vault. Pass 4's QC now runs **two** deterministic checkers: `qc_check_tree.py` (tree vs. the LLM's own candidates/enumerations corpus) and `qc_tree_vs_source.py` (tree vs. the commentary itself — pointer bounds, near-pointer title attestation, monotonicity, repeated-pointer collisions, sibling-count congruence). All three trees shipped in this vault passed the first checker cleanly while carrying real defects the second one catches; see that script's module docstring.
**Inputs:** One Tibetan commentary/root-text file, normally under `1-SOURCES/Commentaries/`.
**Outputs:** Working intermediates in `0-INBOX/` (`toc-candidates-<id>.md`, `toc-enumerations-<id>.md`, `toc-tree-<id>.md`, both QC reports, resumable per-chunk staging under `0-INBOX/temp/TOC-<id>/`); once QC-clean, promoted to the rail at `2-RAILS/Sections/Raw/toc-tree/<id>.md`.
→ [`toc-tree-extraction/SKILL.md`](toc-tree-extraction/SKILL.md)

### `toc-scaffolded-claims` **[exists]**
**Purpose:** Extract every distinct claim/fact a single commentary makes into one consolidated claims file, organised by that commentary's own decimal-numbered TOC tree instead of fixed A–I categories, with every claim anchored to the source-attested referent it concerns (figure/form, person, place, text, event, date) — so several commentaries on the same root text can be compared section by section and each claim is traceable to something concrete.
**Inputs:** One commentary file from `1-SOURCES/Commentaries/` with a `registered_id`, plus its TOC tree from `toc-tree-extraction` (or the Gemini script).
**Outputs:** One file at `2-RAILS/Claims/raw/toc-scaffolded/<registered-id>.md` — a Grounding index of attested referents, then claims grouped under headings mirroring the TOC tree's own nodes, each with the original-language statement, a one-line English gloss, a type, a referent anchor (or explicit `[unanchored]`), and a citation, plus internal-tensions and unanchored-claims rollups and a coverage log.
→ [`toc-scaffolded-claims/SKILL.md`](toc-scaffolded-claims/SKILL.md)

### `tree-guided-claims` **[exists]**
**Purpose:** The vault's method-3 claims extraction — a genuinely independent, fresh extraction done node by node against a commentary's own TOC tree, via one isolated subagent per node, never a re-bucketing of an existing claims file. Built after `_comparison-report.md` found that this vault's earlier `toc-scaffolded` run was Sonnet's category-scaffolded claims re-bucketed under the tree, not a real third extraction. Bakes in the report's five guards: claim IDs namespaced away from node decimals (`c-<decimal>-<n>`, never a bare number), a recomputed (never inherited) `claim_count`, per-node isolation as the structural guard against cross-node/cross-commentary contamination, a `stated` referent rule that resolves within the claim's own quotation, and a deterministic verifier run before the file is considered final.
**Inputs:** One commentary file from `1-SOURCES/Commentaries/` with a `registered_id`, plus its TOC tree — checked clean (or human-reviewed) by **both** `toc-tree-extraction` QC scripts.
**Outputs:** One file at `2-RAILS/Claims/raw/tree-guided/<registered-id>.md` — a Grounding index, claims under TOC-tree-mirrored headings with namespaced IDs, internal-tensions and unanchored-claims rollups, a coverage log, and a `verify_claims.py` pass (quote containment, count recomputation, ID collisions, `stated`-referent validity).
→ [`tree-guided-claims/SKILL.md`](tree-guided-claims/SKILL.md)

### `spine-map` **[exists]**
**Purpose:** Build one commentary's routing index from its own TOC nodes and claim IDs onto the canonical spine slots of the root text — the once-per-commentary judgment (node numbering is never uniform across commentaries, and some run many spine slots inside one undivided node) that `claims-consolidation` used to re-derive inside every topic run. Records addresses only, never claim content; every claim in the commentary's raw file gets exactly one disposition, so nothing can silently vanish from a later packet.
**Inputs:** One commentary's finished TOC tree (`2-RAILS/Sections/Raw/toc-tree/<id>.md`), its raw claims file (`2-RAILS/Claims/raw/tree-guided/<id>.md`, heading lines suffice), the root text, and the registered slot list in `Guidelines/vault-annex.md` §2a.
**Outputs:** One routing index at `2-RAILS/Claims/raw/spine-map/<registered-id>.md` — slot map, claim-level routing, ambiguous claims, silent slots, unmapped nodes — passing `verify_spine_map.py` with zero errors.
→ [`spine-map/SKILL.md`](spine-map/SKILL.md)

### `claims-consolidation` **[exists]**
**Purpose:** Consolidate one topic's claims across every commentary into a single question-driven topic page — per-commentary mapping in isolation (node numbering is never uniform across commentaries, so this needs a real read of each one's own TOC tree, not a fixed formula), then question generation and per-facet synthesis into Consensus/⚑ Divergences/Unique, closed by a mandatory coverage check and a two-gate verification: the bundled deterministic checker (`verify_consolidation.py` — citation existence, recomputed count labels, both-sides flags, disposition completeness) and an adversarial attribution audit (`claims-consolidation-audit`) by a fresh agent. Rules 9–16 encode the error classes the 2026-08-07 pilot audit proved real (false corroboration, partial-support padding, harmonization-as-attribution, epistemic upgrades, hand-tallied counts).
**Inputs:** A topic definition (spine slot + facets) and every commentary's raw claims file plus TOC tree under `2-RAILS/Claims/raw/tree-guided/` and `2-RAILS/Sections/Raw/toc-tree/`.
**Outputs:** One consolidated topic page at `2-RAILS/Claims/<topic-slug>.md`, following `Templates/consolidated-claims-topic.md`, passing both verification gates.
→ [`claims-consolidation/SKILL.md`](claims-consolidation/SKILL.md)

### `claims-consolidation-bo` **[exists]**
**Purpose:** Tibetan-language variant of `claims-consolidation` — a delta skill inheriting the full base pipeline (mapping, question-driven synthesis, coverage check, Rules 1–16, both verification gates) but writing the topic page's entire analytical content in Tibetan: synthesis, questions, divergence discussion, review reasons, coverage notes. Structural headings carry bilingual anchors (`### མཐུན་སྣང (Consensus)`) so the deterministic checker still parses; count labels use `(འགྲེལ་པ N)`; every attested claim quotes its བོད་ཡིག verbatim inline. The consolidator never reads the English counterpart, keeping `-en`/`-bo` pairs a clean comparison of consolidation-by-language.
**Inputs:** Same as `claims-consolidation` (topic definition + raw claims files + TOC trees); optionally the cached Stage-1 mapping when an English run already produced it.
**Outputs:** One Tibetan topic page at `2-RAILS/Claims/<topic-slug>-bo.md` with `lang_tag: bo` and a `counterpart:` link, passing both gates.
→ [`claims-consolidation-bo/SKILL.md`](claims-consolidation-bo/SKILL.md)

### `claims-consolidation-audit` **[exists]**
**Purpose:** Adversarial attribution audit of a consolidated claims topic page — a fresh agent (never the page's author) re-checks every `registered_id:claim_id` citation against the raw claims files: does the claim actually say what the page attributes to it, are Tibetan quotes verbatim, are divergences real and two-sided, is epistemic strength preserved. Report-only — findings go in a severity-ranked report (critical/moderate/minor), never edits. Serves as gate 2 of `claims-consolidation` and runs standalone on any existing topic page.
**Inputs:** One topic page at `2-RAILS/Claims/<topic-slug>.md` plus the raw claims files it cites; the deterministic checker should run first so model judgment is spent only where a script cannot decide.
**Outputs:** A structured findings report (VERIFIED / ERRORS / QUOTE MISMATCHES / OTHER), delivered in-response or written to `0-INBOX/claims-audit-<topic-slug>-<date>.md` on request.
→ [`claims-consolidation-audit/SKILL.md`](claims-consolidation-audit/SKILL.md)

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

### `dharmamitra-translate` **[exists]**
**Purpose:** Produce a zero-shot **machine-baseline** translation of a block-ID'd source file by calling DharmaMitra's public `cat-translate` API once per block ID, threading the document's own preceding translations back in as context.
**Inputs:** A block-ID'd file under `1-SOURCES/`; a target-language label (`english`, `german`, `modern chinese`, …); optionally a style instruction, a context header, and a flat `source<TAB>target` glossary.
**Outputs:** `3-TRANSFORMATIONS/Translations/<lang-tag>-dharmamitra-zeroshot/` — the block-ID-aligned translation, its `about.md` / `style.md` / `context-header.md`, and an append-only per-call ledger under `work/`.
**Rules:** One block ID per API call; never writes to `1-SOURCES/`; never writes into an existing translation track; output is `track_type: machine-baseline`, `rails_used: none`, permanently `status: draft`, and may not be cited by any other transformation. The endpoint is public and shared — keep `--sleep` at 4 s or higher and never parallelise around a 429.
**Contrast with `zeroshot-translator`:** that skill translates with the agent's own model and enforces pada alignment; this one calls an external multi-witness API and records exactly what was sent for every line. Use it for a fast external baseline, for a language no track covers, or as raw material for `glossary-extract-raw`.
→ [`dharmamitra-translate/SKILL.md`](dharmamitra-translate/SKILL.md)

---

## Translation QA skills

### `translation-qa` **[exists]**
**Purpose:** MQM-based quality check of a translation file or track against the source text, the `2-RAILS/` verse packages, and the track's `requirements.md` + `termbase.md`. Use it to QA, grade or compare translations, and to decide whether one is ready to move from `status: draft` to `status: complete`. Especially suited to zero-shot output, which reads fluently while hiding omissions, mistranslations and broken verse IDs.
**Inputs:** Translated section(s); `requirements.md`; `termbase.md`; relevant `2-RAILS/` files.
**Outputs:** `3-TRANSFORMATIONS/Translations/<track-name>/qa-report.md` — per-verse MQM annotations (dimension + severity + suggested fix) plus an aggregate scorecard with a pass/fail gate.
**Note:** imported from `bodhisattvacharyavatara-rails`; its examples are Hindi but the skill is language-agnostic.
→ [`translation-qa/SKILL.md`](translation-qa/SKILL.md)

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

### `author-metadata-sync` **[exists]**
**Purpose:** Propagate human-curated author metadata (`author`, `author_in_use`, `author_in_english`) from the commentary frontmatters in `1-SOURCES/` into the raw tree-guided claims files, and report every registry surface (vault-annex table, `sources.yaml`, drafted articles) that still disagrees — run it after any human review of author names.
**Inputs:** The `1-SOURCES/Commentaries/*.md` frontmatters (point of truth) and the `2-RAILS/Claims/raw/tree-guided/` files; all writes go through the bundled `scripts/sync_author_metadata.py` (check mode first, then `--write`).
**Outputs:** Synced author fields + header line in each claims file; a console report of annex/sources.yaml mismatches and article placeholder strings for the manual passes the SKILL.md prescribes.
→ [`author-metadata-sync/SKILL.md`](author-metadata-sync/SKILL.md)

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

## Wikipedia article skills

These skills generate encyclopedic output for bo.wikipedia from the vault's rails, writing drafts into `3-TRANSFORMATIONS/Wikipedia/`. They never publish — publishing stays behind the pipeline's `/publish` gate.

### `wiki-article-from-claims` **[exists]**
**Purpose:** Draft a cited, readable Tibetan Wikipedia article from one consolidated claims topic page — claims-only drafting with the fixed claim-resolution chain and character-for-character quotation verification against `1-SOURCES/`, rendered as encyclopedic wikivoice (consensus stated plainly without inline commentator attribution, at most 3 refs per statement, at most 2 commentary quotations per article), under the Tibetan punctuation contract (sentence-final shad `།`, paragraph-final double shad `།།`, no commas anywhere) and in-prose author naming via the human-curated `author_in_use` frontmatter key — plus a generated read-only `article-preview.md` (Obsidian footnotes) so reviewers read the article without inline `<ref>` clutter. *(2026-08-21: the former `wiki-article-from-claims-v2` was promoted to be this skill; the original v1 is retired and lives in git history.)*
**Inputs:** A spine-slot or keyword topic whose consolidated page exists in `2-RAILS/Claims/`, that page's raw tree-guided claims files, and the pipeline's wikitext spec as the output contract (Mode A); or an existing verified `article.md` + `citations.md` for register-only revision (Mode B).
**Outputs:** `article.md` (fenced wikitext) + `citations.md` (audit trail, incl. full attestation beyond the in-article refs) + `article-preview.md` (script-generated footnote rendering with author-name footnote labels) written under `term-articles/<topic>/` or `slot-articles/<topic>/` (Mode B replaces the existing files in place — git preserves prior versions); bundled `scripts/make_preview.py` also runs standalone on existing articles.
→ [`wiki-article-from-claims/SKILL.md`](wiki-article-from-claims/SKILL.md)

### `article-subject-filter` **[exists]**
**Purpose:** Classify every article-queue term as a standalone encyclopedic subject, section material for a named target article, or a glossary-only term — merging near-duplicate subjects — with a recorded reason for every verdict (keyword pipeline Step 7).
**Inputs:** `article_queue.json` and the Tibetan term registry from the keyword-extraction run, the methodology doc's §Step 7 criteria, and the existing `2-RAILS/Claims/` pages as merge targets.
**Outputs:** `0-INBOX/AI_translation/keyword-extraction/output/article_subjects.{json,md}` — verdicts, merges, and a term-conservation check; all prior step outputs untouched.
→ [`article-subject-filter/SKILL.md`](article-subject-filter/SKILL.md)

### `wiki-article-inventory` **[exists]**
**Purpose:** Determine for every standalone article subject whether bo.wikipedia already has the article — title/variant lookup plus Wikidata sitelink check — and save a per-subject inventory with dated wikitext snapshots (keyword pipeline Step 8).
**Inputs:** `article_subjects.json` (Step 7 output) with variant sets, plus read-only API access to bo.wikipedia and Wikidata.
**Outputs:** `3-TRANSFORMATIONS/Wikipedia/tara21/wiki-inventory.yaml`, snapshots under `work/wiki-snapshots/`, and the kwiki-schema `terms.yaml` with `status: candidate` throughout.
→ [`wiki-article-inventory/SKILL.md`](wiki-article-inventory/SKILL.md)

---

## Pipelines — not skills

A **pipeline** is a multi-stage program with its own code, prompts, gates and CLI. It is not invoked as a skill; it is installed and run. Pipelines live under [`../Pipelines/`](../Pipelines/), one folder each, and are listed here so the skill-first rule in `4-SYSTEM/CLAUDE.md` does not send you looking for a skill that was never going to exist.

### `Pipelines/wikipedia` — Tibetan Wikipedia article generation (`kwiki`)
Takes a Tibetan root text plus its commentaries and produces cited Tibetan Wikipedia articles, creating or updating them on bo.wikipedia behind a human review gate. Ported from the IATS-2026 repo on 2026-08-03; 547 tests pass.

Its stages: align root↔commentaries → seed key terms → extract cited passages → build an atomic claims table → outline → draft (claims-only) → optional literary polish → LLM audit → **deterministic verification gate** → dry-run publish. The gate uses no LLM: a quotation that does not appear character-for-character in its cited source file fails the build.

It **drives the six ingest-chain skills above** — `kwiki commentaries` resolves their scripts directly out of `4-SYSTEM/Skills/`. It also carries the team's canonical 17-step pipeline as one skill per step under `Pipelines/wikipedia/cowork-pipeline/`, kept verbatim; those are reference documents, not vault skills.

Slash commands: `/ingest`, `/pipeline`, `/publish`.
→ [`../Pipelines/wikipedia/README.md`](../Pipelines/wikipedia/README.md)
