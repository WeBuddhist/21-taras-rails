# 11 - Pipeline Steps in Detail

> **What this is.** The complete, step-by-step reference of the article-generation workflow, written 2026-08-18 as study material for the IATS paper and the conference presentation. Every step is documented in tree form: what goes in, what comes out, what happens inside, and *why it was designed that way*. Compiled from the skills (`4-SYSTEM/Skills/`), the guidelines (`keyword-extraction-methodology.md`, `claims-methodology.md`, `vault-annex.md`), the pipeline docs (`docs/reference/cowork-pipeline.md`, `wikitext-spec.md`, `STATE.md`), the methods draft (`paper/draft/paper-methods.md` §5 — a superseded intermediate, deleted 2026-08-23, in git history), and the actual on-disk artifacts of the tara21 run.
>
> **Scope note (2026-08-23).** Two retired steps were removed from this reference on the lead's
> instruction: the meaning-based commentary **resegmentation** variant (the rule-engine
> segmentation of A3 is the production path) and the root↔commentary **alignment /
> transclusion-anchor** step. Neither is in the production path — no transclusion anchor remains
> in `1-SOURCES/Commentaries/`, and nothing downstream consumes alignment data; the node-by-node
> claims layer (C1) supersedes it. Git history holds the earlier text.
>
> **How to read it.** Section 0 is the overview (matches the "overview" workflow diagram). Sections A–E are the five phases; inside each phase, every step follows the same skeleton: **Input → Output → What happens → Why → Gate**. The nested bullets under "What happens" are the sub-steps (matches the "detailed" workflow diagram).

---

## 0. The pipeline at a glance

### The five phases (overview diagram)

```
A. SOURCE PREPARATION      raw OCR text  →  clean, segmented, block-ID'd, structurally
   (ingest, per text)         annotated sources in 1-SOURCES/ — the frozen ground truth

B. SUBJECT SELECTION       corpus  →  ranked Tibetan keywords  →  encyclopedic article
   (keyword chain)            subjects  →  create-vs-update decision per subject

C. CLAIMS LAYER            each commentary in isolation  →  atomic cited claims  →
   (rails, per commentary     routing maps onto the root text's spine  →  one
    then per topic)           consolidated topic page per subject, double-gated

D. ARTICLE GENERATION      consolidated topic page  →  Tibetan wikitext article with
   (per subject)              verbatim-verified citations  →  deterministic batch gate

E. PUBLICATION             verified article  →  pre-publication review  →  human
   (human gate)               approval  →  dry run  →  --execute to bo.wikipedia
```

### The full step list (detailed diagram)

| # | Step | Skill / script | Deterministic gate |
|---|------|----------------|--------------------|
| A1 | Clean the raw OCR | `clean-raw-text` (inside `raw-to-sources`) | profile shown before any change; raw never overwritten |
| A2 | Place in 1-SOURCES + frontmatter | `raw-to-sources` | collision stop; `status: 0-raw` |
| A3 | Segment into citable blocks | `format-tibetan-root-text` (root), `commentary-segmentation` (commentaries) | `assert_no_loss` — abort if one non-whitespace char changed |
| A4 | Extract the sa-bcad TOC tree | `toc-tree-extraction` (4 isolated passes) | `qc_check_tree.py` + `qc_tree_vs_source.py`, both zero-issue |
| A5 | Ingest headings into the source | `toc-tree-ingest` (+ `tag-inline-toc`) | `verify_prose_unchanged` diff-back |
| A6 | Lint | `lint-annotations` | report-only pre-flight |
| B1 | Literal English translation | `zeroshot-translator` | block IDs preserved, pada-aligned |
| B2 | English candidate extraction | YAKE + spaCy, TF-IDF vs Reuters IDF | scripts, deterministic |
| B3 | en→bo mapping → Tibetan term registry | LLM per occurrence (5 parallel agents) | terms regrouped by Tibetan form |
| B4 | Tibetan-side counting | string-match scripts, quote-excluded | deterministic frequency matrix |
| B5 | Composite scoring | Signals A (attention) / B (structure) / C (presence), 0.6/0.25/0.15 | min-max normalised, weights recorded |
| B6 | Article-viability gate v1 | spread ≥ ⌈16/2⌉ AND claims ≥ 20 | mechanical cutoff — 114 of 367 pass |
| B7 | Subject filter + merge | `article-subject-filter` | conservation of terms (hard failure) |
| B8 | Existing-article inventory | `wiki-article-inventory` | live API, no guessing; read-only |
| C1 | Tree-guided claims extraction | `tree-guided-claims` (one subagent per TOC node) | `verify_claims.py` (4 hard checks) |
| C2 | Spine map per commentary | `spine-map` (one isolated agent each) | `verify_spine_map.py` (disposition completeness) |
| C3 | Packet assembly per topic | `assemble_packet.py` — script, no model | exits non-zero on any gap |
| C4 | Question generation + consolidation | `claims-consolidation` (one agent per topic) | manifest coverage diff |
| C5 | Consolidation gates | `verify_consolidation.py` (Gate 1); `claims-consolidation-audit` (Gate 2) | zero errors; no critical/moderate finding |
| D1 | Draft the article | `wiki-article-from-claims` (claims-only drafting) | per-quote PASS table in `citations.md` |
| D1b | Native-reviewer style revision (v2) | `wiki-article-from-claims-v2` (Mode A fresh / Mode B register-only) + `make_preview.py` — *promoted 2026-08-21 to be the sole `wiki-article-from-claims`; v1 retired* | style walk (ref cap 3, quote budget 2, punctuation contract, `author_in_use` naming); preview generated, never authored |
| D2 | Import into the pipeline layout | `import_term_article.py` + `build_vault_registry.py` | mechanical bridge; ledger `drafted` |
| D3 | Deterministic verification | `verify_batch.py` / `kwiki verify` | character-exact quotes; validator V1–V12 |
| E1 | Pre-publication review | `prompts/08-review/v1-prepublication.md` | must return "publish" |
| E2 | Publish | `kwiki publish` | dry-run default; ledger ≥ `verified`; explicit `--execute` per article |

### Three design principles (repeat at every stage)

1. **The model judges; the script verifies.** Linguistic judgment (what is a sa-bcad, what a passage claims) is model work. Everything checkable — byte identity, count arithmetic, ID resolution, structural invariants — is done or re-done by deterministic code that fails closed. Every stage ends in a gate a model cannot talk its way past.
2. **Isolation over context.** Wherever precision matters, work is split into single-purpose subagent calls that see only their own input — one chunk, one node, one commentary, one topic packet — so an error cannot propagate by contamination and a task cannot drift into its neighbour's instructions.
3. **Nothing interpretive touches the source layer.** `1-SOURCES/` receives only structure: block boundaries, IDs, headings, navigation links. Every script that writes near a source file carries a no-loss assertion that aborts if a single non-whitespace character changed.

### Two load-bearing invariants (the article chain)

1. **Nothing downstream ever touches source wording after the claims stage.** The claims table is the only drafting input; passages/quotations stay in the vault as verification material and re-enter the article only through code.
2. **Nothing is published that hasn't survived the audit and the pre-publication review.** Everything else is replaceable machinery around these two rules.

---

## Phase A — Source preparation (ingest)

*Run once per text: the root text first (commentaries anchor to its block IDs), then each of the 16 commentaries. Orchestrated by `/ingest`. Ingest is a pure `1-SOURCES/` + `2-RAILS/` operation — no Wikipedia-pipeline artifacts are written here.*

### A1. Cleaning — `clean-raw-text`

- **Input:** the raw OCR/segmentation export (`.txt`, `.docx.txt`) under `0-INBOX/raw-data/` — read-only, never edited.
- **Output:** a cleaned flat-markdown body (working file); the raw file untouched.
- **What happens:**
  1. **Profile first** — the skill reads the raw text and builds a profile JSON of mechanical issues: page markers (`^\s*-\d+-\s*$`), running headers (lines repeating verbatim >5 times), mid-word spaces, non-breaking tshegs (U+0F0C), orphaned fragments (≤15 chars mid-paragraph). The profile is shown to the human **before anything is changed**.
  2. **Generate a bespoke cleaner** — a small Python script handling exactly the profiled issues and nothing else: page markers out; headers out (only when the string is the *entire* line — never substring matching, because header text can legitimately appear mid-sentence); U+0F0C → U+0F0B (declared "never ambiguous"); mid-word spaces removed (`([ༀ-࿿]) +([ༀ-࿿])` → joined, repeated until stable); orphaned fragments joined; blank-line runs collapsed.
  3. **Run it, review the first 100 lines**, report residuals.
- **Why:** cleaning is strictly mechanical — no spelling fixes, no paraphrase, no restructuring. Verse lines (ending `།།` or `། །`) are never collapsed into prose. Anything interpretive (broken syllables, OCR repair) is deferred to later stages or to the human edition. Profile-before-change means the human sees exactly what will be deleted before a byte moves.
- **Gate:** raw file never overwritten; ambiguous repeated lines are flagged and asked about, never silently removed; the LLM never marks the result complete.

### A2. Into 1-SOURCES with frontmatter — `raw-to-sources`

- **Input:** the cleaned body; `--type root|commentary` (required, never inferred); optionally curated catalog metadata (the དཀར་ཆག xlsx) — authoritative over colophon guesses.
- **Output:** exactly one file — `1-SOURCES/Text/<title>.md` or `1-SOURCES/Commentaries/<title>.md` — with frontmatter (`title`, `author`, `file_type`, `lang_tag`, `source_description`, `book_id`, `status: 0-raw`; commentaries also get their `registered_id`). Body still unsegmented.
- **What happens:** resolve inputs → clean (A1) → derive the filename from the text's own Tibetan title (ID prefixes and process suffixes stripped into frontmatter) → collision check (hard stop) → write body → run the frontmatter skill (`root-text-frontmatter` / `commentary-frontmatter`, which owns `registered_id` assignment) → reconcile with catalog metadata → report.
- **Why:** a thin orchestrator by design, so failures are isolatable. Fields that need external lookup (`bdrc_work_id`, `school`, `copyright`) are left **blank rather than guessed** — blank is correct output. `registered_id` is the stable name every later citation uses (e.g. `taranatha`, `karma-maitri`); once assigned it never changes. The 16 pipeline commentaries carry IDs `drakpa-gyaltsen` … `tsultrim-namdak` (sigla `TARAC02_DGT` … `TARAC17_TSN`), registered in `vault-annex.md` §3.
- **Note on the root text:** the tara21 root is a **critical edition** — it replaced an OCR export on 2026-08-07 because the OCR's verse segmentation was wrong and omitted the entire benefits (ཕན་ཡོན) section; the two witnesses differ at 17 of the 21 homages. This matters downstream: the pipeline is *sic*-faithful to the ingested edition (D3), so textual correction happens **here, at the source layer, or not at all**.

### A3. Segmentation into citable blocks

- **Input:** the cleaned, placed source file.
- **Output:** the same text with block boundaries and stable block IDs — the vault's sole cross-file reference mechanism. Root: one stanza per paragraph, `^chapter-verse` IDs (`^1-1` … `^1-21`, invocation `^I-1`, benefits `^a-1`–`^a-7`). Commentaries: citation-sized blocks (1–2 prose sentences, one stanza, or one quotation each).
- **What happens:**
  - **Root — `format-tibetan-root-text`:** a small grammar of Tibetan punctuation drives a deterministic formatter: verse-line separator `། །`; mid-verse breaks at `[letter] །[letter]` (negative lookbehind prevents matching inside a `། །` pair); stanza = typically 4 verse-lines, one block ID per stanza on the last line; double-shad `།།` appears only in colophons, so it detects colophon lines reliably; chapter headings get `^N-0` anchors (the `-0` slot is reserved for headings so they can never collide with content IDs).
  - **Commentaries — rule-engine segmentation (`commentary-segmentation`):** a boundary-cue engine over seven lexical signals — terminal particles (`འོ`/`ནོ`/`དོ`… + `།`), quote closers (`ཞེས་སོ། །` …), quote openers (`…ལས།`), enumeration heads (`…ལ་གསུམ་སྟེ།`), ordinal openers (`དང་པོ་…`), objection close/open (`…ཞེ་ན།` / `འོ་ན་…`), and a protected verse-stanza detector (2–4 uniform clause units of 6–11 syllables, peeled out whole and never re-cut). Target granularity ~40 syllables; over-cap blocks split at shads; residue no rule can cut is flagged `STAGE2_MANUAL` for the human.
- **Why:** blocks are the unit of citation — small enough that a claim can cite exactly the span it needs. Weak signals report rather than cut ("when in doubt, under-cut; over-long is safer than wrong"). Verses are protected because meter is a stronger signal than any prose rule.
- **Gate:** `assert_no_loss` in every script — output minus whitespace must equal input minus whitespace, **or it aborts and writes nothing**. This is "the property that makes this safe to run at all."

### A4. TOC-tree extraction — `toc-tree-extraction`

Tibetan commentaries announce their own structure inline (the sa-bcad): the author enumerates coming sections before elaborating each. This step reconstructs the complete nested decimal tree of that structure — the scaffold everything in Phase C leans on.

- **Input:** one commentary file; chunk plan.
- **Output:** `2-RAILS/Sections/Raw/toc-tree/<registered-id>.md` — the QC-clean decimal tree, each node carrying a `[[N]]` line pointer into the source (e.g. `* 1.2.2 གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ [[45]]`), plus the promoted evidence trail (candidates, enumerations, both QC reports).
- **What happens — four isolated passes:**
  1. **Pass 0 (deterministic):** `chunk_file.py --chunk-size 150 --overlap 25 --index-only` — an index of line windows; the 25-line overlap guarantees every candidate appears whole in at least one window.
  2. **Pass 1 — section candidates:** one isolated subagent per chunk, in parallel, each seeing only its own line window. Recall/precision dial set explicitly: "when not confident, LEAVE IT OUT."
  3. **Pass 2 — verbatim enumerations:** one isolated subagent per chunk whose entire job is a START/STOP rule — start at the topic word being divided, stop the instant the division closes; never continue into the elaboration.
  4. **Pass 3 — tree building:** one isolated subagent joins the two views. The author's own enumerations are *more authoritative* than individual candidates — used both to kill false positives and to fill gaps. Counter-rule: doctrinal lists (items enumerated as subject matter, not divisions) enter the tree only when each part is subsequently *opened* as its own section. Titles match by meaning, not string equality; ordinals are kept but never fabricated.
  5. **Pass 4 — two deterministic checkers + repair loop:** `qc_check_tree.py` checks the tree against the model's own candidate corpus (indentation, ordinal↔decimal agreement, duplicate decimals, sibling gaps, three-tier title attestation). `qc_tree_vs_source.py` checks against **the commentary itself**: line-pointer validity (`[[?]]` is always an issue), title attestation within ±3 lines of the pointer, document-order monotonicity, repeated-pointer collisions (≥3 shared values = the "lost cursor" signature), sibling-count congruence against the announcing text's own cardinal. Repair by a fresh isolated subagent per round, looped to zero issues, then promotion.
- **Why the two checkers:** "consistent with the candidates" and "true of the source" are different claims. All three trees originally shipped in this vault reported zero issues from the self-consistency checker while carrying real defects between them — a top-level misattachment (twenty homage children filed under the wrong parent), an unresolved `[[?]]` node, and seven collided line pointers (the value `130` repeated four times — the extractor lost its cursor). The source-checker is the one that catches those, because it reads the one thing the other cannot.
- **Why isolation:** each pass is a separate call with only its own task's prompt and input. "The candidate-extraction call never sees the tree-building instructions, so it cannot drift into tree-building; the verbatim-copy call never sees the 'interpret and reconcile' instructions, so it stays literal. Merging the four jobs into one context collapses that isolation and precision drops."
- **Gate:** both checkers' exit codes = issue count; promotion requires both clean (or only human-accepted ambiguities). "Never declare the tree clean on a subagent's say-so, and never report zero issues when a checker was not actually run." **State: all 16 commentaries have promoted trees; 15 hold clean under the current source versions, and one (gendun-gyatso) needs its source-check rerun — its source file was re-stamped two minutes *after* the tree's QC ran, so the line pointers have drifted. The defect is recorded inside the affected claims file rather than hidden.**

### A5. Headings into the source — `toc-tree-ingest` (+ `tag-inline-toc`)

- **Input:** the promoted tree; the commentary file.
- **Output:** the same commentary with editorial headings inserted in place (`## … ^1-0`, `### … ^1-2-0`, down to `###### … ^1-2-2-1-1-3-1-0`) and, where applicable, inline wikilink tags wrapping each announced term (`[[#^1-2-0|བཤད་པ་]]`) so the enumeration sentence links forward to the section it announces.
- **What happens:** the model (Phase 1) *points* — it identifies candidates and their locations; the script (Phase 2) *copies bytes* — assigns block IDs from depth, inserts headings, wraps exact substrings, and diffs the result back against the source before writing.
- **Why:** sa-bcad detection has too many surface variants for regex ("every rule spawns three exceptions; tuning it is an endless loop") — so reading for meaning is model work. But because block IDs are assigned by code, "depth-skipping and numbering bugs are impossible by construction," and because wraps are exact-substring and diffed back, "silent transcription drift is caught and the run fails loudly. **The model never retypes prose — it only points at substrings that already exist.**" A corpus-driven lesson: tara21's sa-bcad openers are near-universally bare ordinals (`དང་པོ་ནི།`) recurring up to forty times per file with no unique substring — which forced **line-number anchors** into the annotation contract, because a context-string-only contract left those sections legally unannotatable.
- **Gate:** `verify_prose_unchanged` — the tagged file may differ from the source only by headings and link wrappers; any prose change is a PROSE INTEGRITY VIOLATION and the run fails. "Never work around it by editing the source."

### A6. Lint — `lint-annotations`

- **What happens:** a report-only pre-flight that sequences existing deterministic checkers — every content block ends with a block ID; every heading ID ends in `-0`; no deprecated anchor forms; verse IDs sequential per chapter; merged half-lines detected; stray flattened footnote digits flagged.
- **Why report-only:** every finding goes to the human before any fix — some pattern matches are legitimate (opening ornaments, colophon terminals), "which is exactly why findings go to the human before any fix." Fixes route back to the owning step rather than being patched ad hoc.

---

## Phase B — Subject selection (the keyword chain)

*Which subjects get articles, in what order, and create-vs-update per subject. Methodology: `4-SYSTEM/Guidelines/keyword-extraction-methodology.md`. Core design: **detect in English, measure in Tibetan** — and **attention beats presence**.*

**The boundary rule:** keywords select and *order publication*; they never define the consolidation topic space (that comes from the spine grid + claim-derived questions, Phase C). A high-keyness term with no claims is a finding, not an article.

### B1. The English measuring stick — `zeroshot-translator`

- **Input:** the Tibetan root text; a purpose-built audience profile (`literal-keyword`).
- **Output:** a deliberately *literal* English translation, verse-by-verse, pada-aligned, **every block ID preserved in position** (29 blocks). A working aid for B2–B3, not a vault translation track.
- **Why literal and why generated:** free published translations paraphrase — "keyword absent in English ≠ absent in Tibetan." A literal translation maximises the recall of the English detection pass.

### B2. English candidate extraction (recall, not ranking)

- **What happens:** YAKE + spaCy noun-phrase filtering per verse (`keywords.py`), **each verse treated as one document** so IDF punishes words recurring in every verse (similes' "like", the homage formula); plus a corpus-level TF-IDF pass against a general-English reference corpus (Reuters-21578, 10,788 documents). Keep a generous pool.
- **Why English at all:** Tibetan has no word boundaries — the tsheg separates syllables, not words — so statistical keyword tools can't run on it without a contested segmenter. Tokenisation is free in English, so English *discovers what the candidates are*. **Numbers:** 193 YAKE candidates; 313 TF-IDF terms.

### B3. en→bo mapping → the Tibetan term registry

- **What happens:** for each English candidate occurrence, open the same-numbered Tibetan block and identify the span it translates (LLM judgment, 5 parallel agents); **regroup by Tibetan term**; drop grammatical particles (ལྟ་བུ་, བཞིན་); add spelling variants and attested synonyms. An orthographic-equivalence pass (tsheg/whitespace-insensitive, anusvara ཾ↔ྃ) merged 3 doublet clusters.
- **Why:** statistics on a translation measure the *translator's* vocabulary. Two failure modes fixed by per-occurrence mapping: **split** (ཡེ་ཤེས་ → "wisdom"/"gnosis"/"pristine awareness" — count divided, rank sinks) and **merge** ("wisdom" ← ཤེས་རབ་ *and* ཡེ་ཤེས་ — distinct terms collapsed). Counting a known string needs no segmentation, so all measuring happens on the Tibetan side, "where the truth lives."
- **Numbers:** **370 → 367 unique Tibetan terms** after doublet merge.

### B4. Tibetan-side counting (presence)

- **What happens:** deterministic string-match per registry term across root + each of the 16 commentaries, **counting the commentary's own prose only — root-text quotations excluded** (via a difflib ≥0.8 similarity quote-detector, which finds the quoted stanza in the commentary's own text). Output: the frequency matrix with a spread column.
- **Why quote-excluded:** a commentary that quotes the verse inflates every word in it; what matters is what the commentator *says*, not what he copies.

### B5. Composite scoring — attention beats presence

- **What happens:** three signal classes, min-max normalised, weighted **A 0.6 / B 0.25 / C 0.15**:
  - **Signal A — Attention (dominant):** claim density — how many claims are *about* the term, across how many commentaries, read from the tree-guided claims files (16 parallel agents, one per commentary). Robust against paraphrase, synonyms, quotation inflation.
  - **Signal B — Structure:** the term appears in TOC-node titles; commentaries explicitly define it. Kills function words (present everywhere, defined nowhere).
  - **Signal C — Presence (tie-breaker only):** the quote-excluded frequency × spread from B4 — deliberately the weakest, because it is the signal the distortions attack.
- **Why:** raw frequency + spread cannot separate ལྟ་བུ་ ("like", in every commentary) from ཡེ་ཤེས་ ("wisdom") — both frequent, both widespread. Only attention separates them: no commentary defines ལྟ་བུ་, no TOC node is titled by it, no claim is about it. **Empirical validation:** pre-A/B, raw presence ranking put Tibetan intensifier particles (རབ་ཏུ་, ཤིན་ཏུ་, ཉིད) in the top 20; none survive into the final top 60. The homage formula ཕྱག་འཚལ་ lands at rank 17, not rank 1 — and then gets filtered as glossary at B7.

### B6. Article-viability gate v1 (mechanical cutoff)

- **The rule:** a term enters the article queue **iff** `commentary_spread ≥ ⌈N/2⌉ (= 8 of 16)` **AND** `claim_count ≥ 20`. Selection is by the gate; *ordering* within the queue is by composite score. Gate-failures stay in the registry as Local-Wiki/glossary candidates — nothing is deleted.
- **Why these constants:** articles are drafted from claims only, and consolidation collapses many raw claims into one cited statement — so the raw count must substantially exceed the final article's cited-statement count; 20 raw claims ≈ a lead plus two-to-three cited sections after shrinkage. Spread ≥ half the commentaries because an article needs due-weight structure across multiple independent sources; the ⌈n/2⌉ form scales to any corpus. The constants are **calibrated once and frozen** — the value of the rule is reproducibility (sensitivity: M=15→139 terms, M=20→114, M=30→63).
- **Why a mechanical gate at all:** it replaced per-run human N-picking after the human contributor asked for a reasoned, repeatable cutoff. **Numbers: 114 of 367 terms pass** (253 retained as glossary candidates); only 2 of the composite top-40 fail the gate, both at 18–19 claims — the gate and the ranking agree.

### B7. Subject filter + merge — `article-subject-filter`

- **Input:** the 114-term queue; the term registry (variant sets as merge evidence); the existing consolidated pages as merge targets.
- **Output:** `article_subjects.{json,md}` — every term classified with a recorded one-line reason.
- **What happens:**
  1. **Merge pass:** cluster queue rows that are the *same subject* (lemma variants དགྲ/དགྲ་བོ/དགྲ་ཡི; verbal/nominal forms; spelling variants of one mantra element). Head = citation form. **Never merge doctrinally distinct terms however close** — ཤེས་རབ vs ཡེ་ཤེས stay separate; when in doubt, don't merge, flag ⚑ borderline.
  2. **Verdict pass**, tests in order: **standalone** (a general encyclopedia would give it its own entry — deities, classes of beings, cosmological entities, named persons, doctrinal categories, mantra elements, epithets with their own commentary literature) → **section-material** (an attribute/body-part/implement whose claims describe *another* subject; must name its target) → **glossary** (generic vocabulary).
  3. **Hub-and-spoke check:** the 21 Tārās resolve to spoke articles; སྒྲོལ་མ remains the hub.
- **Why:** prevents two failure modes — non-subjects (body parts, directions) getting standalone articles, and one subject appearing as several queue rows getting parallel articles. **Judge subjecthood, not material volume** — "a 100-claim body part is still section material; a 20-claim deity is still standalone" (the gate already decided sufficiency). Editorial rules fixed with the human contributor 2026-08-12: **one subject = one article** (existing bo.wikipedia articles are updated with cited sections, **never forked**); hub-and-spoke for the 21 Tārās.
- **Gate:** **conservation of terms** — standalone + section-material + glossary + merged must equal the input count exactly; every term appears exactly once; a term absent or double-counted is a hard failure. **Numbers: 44 standalone + 47 section-material + 10 glossary + 13 merged = 114/114.** ✓
- **Governance note:** under the review-at-end model there is **no human gate mid-chain** — every judgment step instead leaves a full audit trail (per-term verdicts with reasons, merge mappings) so the single end review over finished articles can reject selectively instead of rerunning the pipeline.

### B8. Existing-article inventory — `wiki-article-inventory`

- **Input:** the 44 standalone subjects + variants; live API access to bo.wikipedia and Wikidata (if unavailable: stop — never emit an inventory of guesses).
- **Output:** `wiki-inventory.yaml` (authoritative, with per-subject `action: update|create`), dated wikitext snapshots, and `terms.yaml` in the exact minimal schema the kwiki loader reads (a null `wikipedia_url` *is* the create signal — kwiki's own red-link convention).
- **What happens:** per subject, **both** mechanisms always run — title lookup (with redirects, batched with variants) and Wikidata `wbsearchentities` (bo label, then per English gloss) checking for a `bowiki` sitelink, with entity verification against the glosses ("a gloss like 'king' must not resolve ཏུ་རེ to generic royalty"). Existing articles get a snapshot, section list, and an assessment (substantial/stub/disambiguation). Read-only: GET requests, ≤1 req/s, no edits.
- **Why existence decides the plan:** it is the fact that chooses between the pipeline's create path and its update path — one subject = one article, update never fork. Snapshots are planning context only; article generation must re-fetch live. A disambiguation page is not the article.
- **Numbers: 25 update · 19 create · 0 unresolved** (16 substantial, 9 stubs; 15 QIDs recorded). One notable record: **སྒྲོལ་མ (Tārā) is deferred as its own dedicated effort** — strict-match search found no exact title, but 741 full-text hits suggest an article exists under a longer title.

---

## Phase C — The claims layer (rails)

*The heart of the method. Core principle: **extract first, merge later.** Extraction reads one commentary in isolation (expensive, redoable per commentary); consolidation compares finished claims files (cheap, disposable, redoable any time without re-reading a commentary). Merge decisions made during reading are made with incomplete information — the first commentary read silently defines the topic space. Methodology: `Guidelines/claims-methodology.md`.*

### C1. Tree-guided claims extraction — `tree-guided-claims`

- **Input:** one commentary (with `registered_id`); its QC-clean TOC tree (checked against *this exact file version* — a stale tree's line pointers are worthless).
- **Output:** `2-RAILS/Claims/raw/tree-guided/<registered-id>.md` — every distinct claim the commentary makes, one heading per TOC node in tree order, plus a Grounding index (FIG/PER/PLC/TXT/EVT entities), ⚑ internal-tension rollup, unanchored rollup, and a per-node Coverage log. `status: draft` — always.
- **The claim format:** ID `c-<node-decimal>-<n>` (node 1.2.3's third claim = `c-1-2-3-3` — a string that cannot be mistaken for a heading number); fields **བོད་ཡིག** (verbatim Tibetan) / **English** / **Type** (word-gloss, etymology, iconography, doctrinal, ritual, benefit, …) / **Referent** (Grounding ID + basis) / **Cite** (`1-SOURCES/Commentaries/<file>.md#^<block-id>`).
- **What happens:**
  1. Orchestrator loads commentary + tree, computes each node's **reading window** (own pointer → line before the next node's pointer).
  2. **One isolated subagent per TOC node**, in parallel — each given *only* the extraction rules, its node's line window, and its node's decimal + title. Never another node's output, never another commentary, never any earlier extraction.
  3. Orchestrator assembles replies at tree position (a wrong-looking reply → fresh subagent for that node, never hand-editing), builds the Grounding index, numbers claims, **counts** `claim_count` at the end, writes the file.
  4. Runs `verify_claims.py`.
- **Why per-node isolation — it makes the guards structural, not disciplinary:** a subagent that only ever sees one node's window *cannot* extract a claim under the wrong node, *cannot* re-bucket an earlier extraction it was never given, *cannot* import content from another commentary (each of these is a documented failure from earlier method runs — including a claim whose Tibetan text and citation both belonged to a different commentary's file).
- **Why this method won (three methods compared):** fixed-category (`commentary-claims`), TOC-scaffolded re-bucketing, and tree-guided fresh extraction were run as genuinely different techniques. The comparison found the "toc-scaffolded" run was not an independent extraction at all — 114 of 118 Tibetan strings byte-identical to the earlier run, claim counts copied not recomputed, transcription errors inherited — and presenting a re-bucketing as a second extraction hid real defects (a cross-document contamination; a fabricated mantra promoted to canonical status). Five load-bearing guards came out of that audit: claim IDs are never node IDs; `claim_count` is computed by counting, never inherited; a node-boundary check backs every placement; `(stated)` means the referent's name occurs in *this claim's own* quoted Tibetan; every claim is independently re-derived.
- **Internal disagreement is preserved, never averaged:** when one commentary itself reports two positions, it becomes a ⚑ entry with both positions cited — the divergence machinery starts *inside* single commentaries.
- **Gate — `verify_claims.py`, four hard checks (exit code = issue count):**
  1. **Quote containment:** every བོད་ཡིག string, NFC-normalised and stripped of `།༎་༅༄༈` + whitespace, must be a literal substring of its cited block; ellipsis-joined fragments tested individually ("a claim quoting two real phrases is legitimate; one real phrase and one invented one is not — splitting is what catches the latter").
  2. **`claim_count` recomputed** from the file.
  3. **ID-collision scan** (format regex; duplicate IDs; node-decimal coincidences).
  4. **`(stated)`-referent validation** — the name must occur inside that claim's own quoted Tibetan.
  Repair is always by fresh per-node subagent — "never hand-edit a claim to make the checker pass; never suppress a finding to make the count read zero."
- **State: 16 files, 2,975 claims (62–368 per commentary), all `status: draft`** — the LLM never marks its own extraction complete.

### C2. Spine maps: routing without interpretation — `spine-map`

- **The problem it solves:** consolidation needs to know, for every commentary, which of its own TOC nodes hold which canonical spine slot's content. The pilot answered this inside every topic run — correct but quadratic in the wrong variable (~400 full-file reads over a 3.8 MB corpus, ~25× re-reading the same unchanged files). The fix: **one routing table per commentary, built once, reused by every topic** — 16 judgments instead of ~400, because "which node of karma-maitri is Tārā 5" and "…is Tārā 12" are the same act of reading its tree.
- **The spine (`vault-annex.md` §2a):** the root text's own structure as stable slot IDs — `tara-01` … `tara-21` (one per homage stanza, `^1-1` … `^1-21`), `benefits` (`^a-1`–`^a-7`), plus two observed global slots `structure` and `origin`. **24 registered slots.** Slot IDs are the only source of topic-page filenames and are never coined locally — a new slot is registered by a human first. Nothing in the machinery is specific to twenty-one homages — only the table is; for the Bodhicaryāvatāra the spine would be chapters or verse-groups.
- **Input:** the commentary's tree + its claims file (heading lines only) + the root text + the slot registry.
- **Output:** `2-RAILS/Claims/raw/spine-map/<registered-id>.md` — five tables whose heading names and columns are a parsing contract: Slot map (node-level routing), Claim-level routing, Ambiguous claims, Silent slots, Unmapped nodes.
- **What happens:** one isolated agent per commentary (never several at once — "an agent that has just mapped another commentary's tree is primed to see the same numbering here") establishes the correspondence *with evidence* (an ordinal in the title, an epithet, a root-verse quotation claim as boundary marker) and assigns **exactly one disposition to every claim**.
- **Why a model and not a formula:** node numbering is not uniform across commentaries — one nests a homage at `1.1.N`, another at top level `N`, another titles nodes by epithet, and one (`tsultrim-namdak`) carries **all twenty-one homages inside a single undivided node** (75 claims), so no node-level rule can route it at all; its map routes by claim-ID range using the extraction's own "Verse N quoted" claims as boundaries. "A numbering rule that worked for the last commentary is evidence of nothing about this one."
- **Why routing only, never interpretation:** the file records addresses, never what a claim says — so a spine map adds no link to the citation chain and can never become a rail.
- **Gate — `verify_spine_map.py`:** node existence, claim existence, **disposition completeness** (zero dispositions = silent loss; two = silent duplication — both errors), counts recomputed, slot hygiene. Silence is recorded, never inferred: a slot neither mapped nor marked silent is a gap the assembler will refuse. **State: all 16 maps exist.**

### C3. Packet assembly — `assemble_packet.py` (script, no model)

- **What happens:** for one spine slot, the script collects every commentary's routed claims out of the raw files, **copying each claim block character-for-character** ("a script cannot mis-transcribe བོད་ཡིག"), expands claim-ID ranges, deduplicates, marks ambiguous claims visibly (⚑ carry the uncertainty through — never silently absorb or drop), records explicit silences, and emits a `## Manifest` of every `registered_id:claim_id` included — the deterministic input to the coverage check.
- **Why loud failure:** a commentary with claims but no spine map, or no disposition for the slot, **exits non-zero** — "a real gap, not a formatting nit; never proceed past it." Under the pilot design a commentary quietly missing from one topic's fan-out left no trace; now the absence is structurally impossible to miss. Fix the map and re-assemble; never patch the topic page.

### C4. Question generation + consolidation — `claims-consolidation`

- **Input:** the packet only. The consolidating agent **never re-opens the raw files** — everything it may use is in front of it.
- **Output:** `2-RAILS/Claims/<topic>.md` — per facet: **Consensus** (with per-commentary attestation lists and computed counts), **⚑ Divergences** (never flattened — vault hard rule), **Unique** (single-commentator claims), plus "Claims reviewed, not separately cited" and a Coverage table where **silence is itself a finding**. Citations always `registered_id:claim_id`.
- **What happens:**
  1. **Questions are generated, not authored.** Two free sources: (a) *from the spine, mechanically* — 21 Tārās × observed facets (name/etymology, colour, implements, stance, activity, mantra, benefit) ≈ a scripted grid; (b) *from the extractions themselves* — every distinctive claim implies a question asked of all the others ("the left hand's three fingers symbolise the Three Jewels" → "what does each commentary say the left hand symbolises?"). The union makes consolidation a **derived completeness check**: free extraction first, generated questions catch what free reading missed. A question nobody answers is kept and marked, never deleted — including negative controls ("is X's silence on this slot a real gap, or routed elsewhere?").
  2. One agent per topic writes the page from the packet; topics fan out in parallel (the isolation guard moved upstream into the spine maps).
  3. **Coverage check (deterministic set diff):** the packet manifest is diffed against every claim ID the page cites; every claim in the gap is either folded in or logged with a reason — "no third state." In the pilot this caught real gaps in **5–12% of a topic's mapped claims per page**.
- **Why two-stage matching:** all commentaries share the root text's structure, so alignment is slot-first, then a handful of claims compared semantically *within* a bucket — "never one expensive global matching over thousands of claims."
- **What consolidation surfaces:** fifteen-commentary consensus statements with full attestation lists; divergences down to root-text-level variants (one commentary's own quotation reads དཔལ་མོ "Glorious One" where the corpus reads དཔའ་མོ "Heroine" — "the two readings license different etymologies for the same syllable-position"); and disagreements that exist only as a commentator's report of "earlier commentaries."
- **A Tibetan variant (`claims-consolidation-bo`)** produces `-bo` twin pages under the same rules and both gates, with bilingual structural headings (`### མཐུན་སྣང (Consensus)`) so the deterministic checker still parses them, and a strict independence rule — the `-bo` consolidator must not read the English counterpart, so the pairs double as a controlled comparison of consolidation quality by working language.
- **State: 24 registered-slot pages (tara-01…21, benefits, structure, origin) + 43 term-level topic pages** (the keyword subjects) = 67 consolidated pages, all `status: draft`.

### C5. The consolidation gates — and the error taxonomy that wrote them

On 2026-08-07 the pilot topic pages were adversarially audited: a fresh agent per page re-checked **all 418 unique citations** against the raw claims files. Headline: **zero fabricated claim IDs** — and one critical finding, one moderate, ~16 minor, in a stable taxonomy. The critical case justifies the whole audit design: a claim cited as independently corroborating a "three flaws" framing **contains no flaws framing at all** — the consolidator had a real corpus idea attached to the wrong claim ID. **A deterministic script can prove a cited claim exists; only a reader can prove it says what the page attributes to it.** The minor findings were equally instructive: partial-support padding of consensus lists, the same claim cited on both sides of one divergence, page-level harmonizations presented as a claim's own reading, epistemic upgrades ("endorses" for a tentative སྙམ་མོ aside), silently elided syllables in Tibetan quotes, and hand-tallied "(N commentaries)" labels — five of five wrong on the worst page.

Every error class became either a rule (`claims-consolidation` Rules 9–16: full-statement support; corroboration re-read, not remembered; one side per divergence; verbatim quotes or marked ellipsis; harmonization attributed to the page, not the claim; epistemic strength copied, never upgraded; counts computed, never hand-tallied; every consulted claim gets a disposition) or a check in one of two standing gates:

- **Gate 1 — deterministic, `verify_consolidation.py`:** citation existence against the raw files; count labels recomputed per paragraph; consensus/divergence overlap flags; disposition completeness against the Coverage table; prefix discipline. **Zero errors required.** Validated by reproducing every mechanical finding of the human audit — plus one it missed.
- **Gate 2 — adversarial attribution audit, `claims-consolidation-audit`:** a fresh agent that did **not** write the page ("an agent auditing its own consolidation re-reads its own intentions, not the text") checks every attribution against the raw claims only — never its own knowledge of the tradition, never `1-SOURCES/` directly. Severity critical/moderate/minor; report-only; the consolidator fixes, the auditor re-checks the changed sections; **no critical or moderate finding may remain.**

**Why Gate 2 is not optional (batch experience):** on the first two audited keyword pages (mudra, lotus), every quotation was character-perfect and yet Gate 2 found 4 critical defects — a divergence manufactured from English-gloss noise over identical Tibetan, an inverted corpus fact, a citation corroborating content it lacks, and a uniqueness claim pinned to the wrong claim ID. A clean quote check is never publication-ready by itself: the deterministic gate reads characters; the audit reads meaning; neither replaces the other.

---

## Phase D — Article generation and verification

*Two drafting routes share one doctrine — **claims-only drafting** — and one deterministic gate. Route (a), the `kwiki` per-term chain, produced the reviewed 3-article pilot. Route (b), the rails route, produced the corpus-wide batch and is described first because it is what actually ran at scale.*

### D1. Drafting from the consolidated page — `wiki-article-from-claims` (route b)

- **Input:** one consolidated topic page (facts, in English) + the raw tree-guided claims files it cites (the verbatim Tibetan, the `Cite:` block targets, author/title frontmatter) + the wikitext spec (V1–V12 as acceptance criteria) + `1-SOURCES/` read-only for quote verification.
- **Output:** two files per article — `article.md` and `citations.md` — under `3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/<slug>/` (keyword subjects) or `slot-articles/<slug>/` (per-homage/work articles).
- **What happens:**
  1. **Build the claim-resolution table before drafting a sentence:** every cited `registered_id:claim_id` → raw file → བོད་ཡིག + gloss + `Cite:` target + author/title. The resolution chain is fixed: consolidated attestation → raw claim → verbatim Tibetan + source block. **An attestation that does not resolve is dropped and logged under Unresolvable attestations — never guessed, never cited anyway.**
  2. **Plan:** map consolidated sections onto the article skeleton (section headings are "a menu, not a quota"); mark consensus backbone vs attributed-unique vs ⚑ divergences; choose at most 1–3 verbatim quotations per major section.
  3. **Draft in Tibetan only:** lead (`'''TERM'''ནི་…`, every assertion cited), body with a `<ref>` on every claim-bearing clause, then the fixed tail — `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` → `== ལུང་ཁུངས། ==` + `<references />` → `== དཔྱད་གཞིའི་ཡིག་ཆ། ==` → one allowlisted category.
  4. **Due weight follows attestation counts:** consensus forms the unattributed backbone cited to 2–4 representative commentaries; unique claims are attributed inline by commentator name; ⚑ divergences present *every* position, attributed, never adjudicated.
  5. **Write `citations.md`** — the full audit trail: a reference map (ref → commentary → claim IDs → verbatim quotation → source block), claims used but not quoted, unresolvable attestations, warnings, and a per-quotation verification table.
  6. **Verify:** every quotation located character-for-character (whitespace-collapsed) in the `1-SOURCES/` file its claim cites, PASS/FAIL logged per quote; every ref present in the reference map; V1–V12 walked as a checklist.
- **Why claims-only:** "No parametric knowledge — no dates, Sanskrit forms, iconographic details, or doctrinal framings that are not in a claim, however standard they seem. If it cannot be cited, it does not go in." The named failure modes are added facts, flattened divergences, and quotations that are not character-for-character real. A subject with no citable claims is **refused** rather than padded — one of the 44 subjects (`hara`) ends at `status: not-drafted` for exactly this reason.
- **Why `.md` with a wikitext fence (2026-08-12 decision):** raw `.wiki` files are invisible to Obsidian, and unfenced wikitext misrenders and pollutes the graph with fake links. So the article is YAML frontmatter + a reviewer callout + the complete wikitext in a single ```` ```wikitext ```` fence, byte-identical to what would be published. Reviewers edit inside the fence only; the publish step ships exactly the fence body.
- **Honest-warnings discipline:** every article's `citations.md` records `rails_status: draft` where true (the consolidated page not yet human-promoted), every ref with no public URL, anonymous authors marked openly (`མཚན་བྱང་མེད།`) rather than invented, and which commentaries were consulted but not drafted in.

### D1b. Native-reviewer style revision — `wiki-article-from-claims-v2` (2026-08-18/19)

> **Skill promotion, 2026-08-21.** After the corpus-wide Mode B rewrite completed, the human contributor retired v1 and promoted this skill to be the sole `wiki-article-from-claims` (version suffix dropped). The two-skill situation described below is history; the section is kept as the record of how the feedback rule produced it.

The first review of the 43-article batch by the project's Tibetan linguist produced the pipeline's clearest demonstration of its own feedback rule: reader feedback became executable drafting rules, in a **new versioned skill**, never an in-place edit of the shipped one.

- **The feedback (round 1, 2026-08-18):** (1) inline `<ref>` tags carrying full Tibetan author + title make raw wikitext unreadable in review; (2) statements carry more citations than they need; (3) the articles read as stitched-together claims ("X says… Y says…") — a literature review, not an encyclopedia article.
- **The feedback (round 2, same day, on the Mode B pilot):** (4) Tibetan punctuation was wrong at paragraph level — every sentence must end with a shad `།` and every paragraph's final sentence with a double shad `།།`, which the pilot articles almost entirely lacked; (5) commas do not exist in Tibetan — every `,` is either a genuine boundary (write a shad) or nothing; (6) commentators must be named in prose by a **human-curated respectful name form**, not the catalog name.
- **Input:** an existing verified `article.md` + `citations.md` (Mode B — register-only revision, the cheap path: claim resolution and quote verification are treated as settled and never redone) or a consolidated topic page (Mode A — full fresh draft under the new rules).
- **Output:** revised `article.md` + `citations.md` (with a new section, *Full attestation beyond in-article refs*, so capped citations lose nothing) + a **generated, read-only `article-preview.md`** — produced by `scripts/make_preview.py`, rendering citations as Obsidian footnote superscripts so the reviewer reads clean prose in reading view. The preview is derived, never authored, never published; edits go in `article.md` only. During piloting, Mode B writes to `work/pilot-v2/<topic>/`, never over the article under review.
- **What the new rules do (the style delta — all trust machinery unchanged):**
  1. **Wikivoice for consensus:** claims the consolidated page marks consensus are stated as plain fact, no commentator names, no quotes — the `<ref>`s carry the support. Inline attribution is *reserved* for unique claims and ⚑ divergences.
  2. **Citation cap 3:** at most 3 refs per statement — 2–3 *representative* commentaries for consensus; the complete attestation list moves to `citations.md`, so the audit trail keeps what the article no longer displays.
  3. **Quotation budget 2:** at most 2 verbatim commentary quotations per article, spent only where exact wording is itself the point.
  4. **Prose before fragments + readability as a completion criterion:** merge related claims into connected sentences; reread the whole article as a reader before verifying.
  5. **The punctuation contract:** sentence-final shad, paragraph-final double shad `།།`, zero comma characters anywhere in the fence body, punctuation always *before* the `<ref>` tags it closes over.
  6. **`author_in_use`:** a new human-curated frontmatter key on each source commentary — the respectful in-article name form (e.g. རྒྱལ་བ་དགེ་འདུན་གྲུབ་). Flow: commentary frontmatter → copied verbatim into the raw claims file's frontmatter → used for every in-prose mention. **The model never invents or upgrades an honorific — its only job is to copy.** Refs and bibliography keep the formal `author` + `title`.
- **Why a new skill and not an edit:** v1 remains the skill of record until the human retires it — the v2 pilot must prove itself first, and the two must stay diffable. The same discipline as the prompt tree: version forward, never rewrite shipped behaviour in place.
- **State (2026-08-19):** three Mode B pilot revisions written to `work/pilot-v2/` (`mudra`, `lotus`, `tara-21`), awaiting the linguist's approval; the corpus-wide redraft deliberately **waits** on that approval. The coworker's `author_in_use` pass landed on all 16 commentary frontmatters (including two genuine re-attributions found in the process: drakpa-gyaltsen → སི་ཏུ་པདྨ་ཉིན་བྱེད་དབང་པོ་, yama-sonam → རྗེ་བཙུན་ཡ་མ་བསོད་ནམས།) and was synced into all 16 raw claims files as a metadata-only pass — not a re-extraction. A survey found 68 of 69 drafted articles carry old-form author names (~1,779 prose mentions); the fix is folded into the pending v2 redraft, **not** hand-patched — blind string replacement breaks ergative particles.

### D1-alt. The `kwiki` per-term chain (route a — the pilot)

The code route (`kwiki article <corpus> <term>`): **extract → claims → outline → draft [→ polish] → audit → verify**, all artifacts under `articles/<term>/`, every stage's model + prompt version pinned in `model.json`, every re-run preserving the outgoing artifact to `history/`.

- **Extract (4):** Tibetan-language prompt; quote character-for-character ("ཡི་གེ་གཅིག་ཀྱང་བསྒྱུར་བ་…མི་ཆོག" — with the warning a machine will check every letter); only passages that *explain* the term; echo the block's own `segment_id`; write "འགྲེལ་བཤད་མེད།" rather than invent. Batched above 25,000 chars, never splitting a commentary across calls.
- **Claims (4b):** passages → atomic table — one verifiable fact per row, own words, **claim-typed** (consensus / majority-with-dissent / school-position / single-commentator) and **reception-tagged** (cited by / refuted by / unengaged). Weight by authority and response, not headcount: a sole corpus representative of a school is a *school-position, never single-commentator*. **Forbidden: synthesis** — no claim may require two sources combined to reach a conclusion neither states alone.
- **Outline (5):** from claims only; sections weighted by breadth × reception; attribution-required marks; gap report.
- **Draft (6):** the drafter sees **outline + claims only** — never source wording (verified in code: the prompt render passes term, outline, claims, glossary, and nothing else). It cites **claim indices**; code (`render_draft_payload`) expands each cited claim back to its passages and renders the refs — "quotations enter the article only from `extract.json`, never from the drafting model — which is what keeps the character-for-character gate meaningful under claims-only drafting." Voice follows claim type: consensus may sit in Wikipedia's neutral voice; everything below consensus gets mandatory in-text attribution.
- **Polish (6a, optional):** the Gemini literary rewrite, structurally fenced **in code** — a changed citations array, paragraph count, or heading order rejects the rewrite untouched. "The stylist is never trusted with structure."
- **Audit (6b):** sentence-by-sentence read-back against the claims table; six finding categories; **two block in code regardless of the model's own verdict** (`AUDIT_BLOCKING = {added-fact, attribution-loss}`) — "a model that lists an added fact and still says publish is overruled by its own finding." Cross-model auditing is the rule for any number the paper reports: the same-model audit said "publish, no findings" ×3 where the cross-model audit found 5 blocking findings, 4 confirmed genuine on hand-adjudication. *The auditor never writes; the writer never audits.*
- **Feedback (step 13):** every audit finding is classified by causal stage (extraction / claims / draft / rewrite) and patches that stage's prompt — canonical doc first, then the skill, then a **new version file** under `prompts/` (never edit a shipped prompt in place). Immutable per-stage outputs make drift diffable to its origin.

### D2. Import into the pipeline layout — `import_term_article.py`

- **The gap it closes:** everything in the corpus came from the skills route, whose layout (`term-articles/<slug>/article.md`) the kwiki gate and publisher cannot see. This script is the mechanical bridge — "it moves and reshapes, it never rewrites wikitext and never invents a citation."
- **What happens (fully deterministic):** extract the wikitext fence body verbatim → `articles/<term>/article.wiki`; parse the hand-written `citations.md` reference map by *keyword-located* columns (headers drift across sessions; semantics don't); resolve each row to a registry source four ways in order, reporting rather than mis-attributing on a miss; store block IDs caret-stripped (the form the block parser yields); recover elided quotations by unique-prefix match against the article's own quoted runs, else split on ellipsis and check each fragment separately; write `citations.json` + provenance `import.json`; set the ledger status.
- **The registry join (`build_vault_registry.py`):** rebuilds `sources.yaml` at the path the pipeline reads, joining the frozen human-curated metadata to the vault's `1-SOURCES/` files — `local_path` vault-relative, `registered_id` filled per entry. This is the join that lets skill-flow citations (which say `taranatha`) resolve to pipeline sources (which say `TARAC05_TRN_bo_segmented`), while `source_id` stays the stable siglum every existing artifact was written against.
- **Ledger discipline:** imported terms are set to **`drafted`, never `verified`** — "verified means the gate passed *and* the audit cleared, and neither is this script's to assert." A term already past a gate is never walked backwards. The ledger's status vocabulary *is* the pipeline order: `pending → extracted → claimed → organized → drafted → audited → verified → approved → published` (+ terminal `failed`).

### D3. The deterministic verification gate

- **What it is:** last in the chain, blocking, and LLM-free. Two halves:
  1. **Quotation check** — every cited quotation must appear in its cited source. Four tiers, deliberately unequal: `exact` (substring — pass), `collapsed` (substring after whitespace removal — pass; line wrapping is not part of the text), `fuzzy` (substring only after shads/tshegs/head marks are also dropped — **not a pass**: the letters agree but the punctuation does not, so the article is not quoting what the file says), `missing` (fail). "Reporting a fuzzy hit as success would quietly reintroduce exactly the class of error this gate exists to catch — `found` is not the gate; `passed` is."
  2. **Wikitext validator V1–V12** — the output contract: every quotation character-real (V1); every ref resolves to a declared source (V2); `<references />` present iff refs exist (V3); **never `{{Reflist}}`** (V4 — bo.wikipedia's template injects its own heading, producing two stacked headings; verified on a live render; "the single most likely failure mode, because the idiom is correct on English Wikipedia and every LLM reaches for it"); refs balanced (V5); ≥1 heading (V6); ≥1 allowlisted category (V7 — the model never invents a category name, because the live namespace contains misspellings); every section cited (V8); Tibetan script only outside ref URLs (V9); **a tsheg survives every `'''` and `[[` boundary** (V10 — a Tibetan spelling error MediaWiki itself will never surface; only the linter catches it); fixed tail order (V11); no placeholders or model chatter (V12). Non-blocking warnings: refs missing year/page (W1), unlinked refs (W2), short articles <1,500 syllables (W4).
- **The reading view:** quotations are compared against the commentary with every layer ingest added (block IDs, headings, wikilinks) stripped back off — "not one Tibetan character touched" — because a faithful quotation spanning a block boundary must never fail on a caret the pipeline itself wrote. Independently, every block locator is resolved: the quotation must also appear inside the specific block its citation names (a wrong locator is a warning, not a failure — the quote is real, but it sends a reviewer to the wrong paragraph).
- **Why it matters (the paper's best evidence):** in a live run the gate caught a model silently promoting a tsheg to a shad inside a quotation — similarity 0.974, invisible to a human skimming Tibetan prose at speed. That is the class of drift that makes a quotation not a quotation. Corollary: articles are ***sic*-faithful** to the ingested edition — textual correction is an editorial act for the source layer, never a liberty of the drafting model. **There is no bypass flag, and an audit "publish" verdict does not skip the gate.**
- **Batch form (`verify_batch.py`):** runs the same gate over every drafted article and writes one distribution report (`work/VERIFY-BATCH.md`) instead of exiting non-zero per term — "which is right for a gate and useless for a batch." Re-run after any fix pass; the numbers are the fix's evidence.
- **Batch results (2026-08-15, 42 imported articles):**
  - **861 of 882 quotations (97.6%) appear character-for-character in the commentary they cite.**
  - Validator: 1 of 42 articles fully clean; error mass **V2×269, V1×9, V8×3, V7×1, V9×1**. The V2 mass is a **format mismatch between the two factories** (the skill flow hand-writes `AUTHOR། TITLE།` ref bodies from raw-file frontmatter; the validator expects the registry-composed string) — a bridge-reconciliation problem, not fabricated citations. The genuine remaining work: 21 quotation misses (two of which are import artifacts — English note-text that leaked into a quote field), 3 unsourced sections, 1 category error, 1 script error.

---

## Phase E — Publication (the human gate)

*Nothing has been published yet — deliberately. The pilot's three articles sit at `verified`; the 42 batch articles at `drafted`. `kwiki publish` refuses anything below `verified`, so today zero articles are publishable — by design, not accident.*

### E1. Preconditions (all three, no skipping)

1. Ledger status `verified` or `approved` — an audit failure marks the term `failed`, and there is no path to `verified` around the audit.
2. `report.md` shows **PASS** and `audit.md` shows a **publish** verdict with no blocking findings — both files read directly, never inferred from the ledger.
3. Bot credentials of the `Account@botname` form — never a main-account password.

### E2. Pre-publication review

The canonical review prompt (`prompts/08-review/v1-prepublication.md`) gates the whole publication layer and must return **publish** before any `--execute` — including sandbox. A skeptical-reviewer checklist: every ref resolves (public-domain sources → Wikisource anchors matching the vault IDs; copyrighted sources → a BDRC/WeBuddhist link **carrying the full locator in the ref text**, so verifiability survives without republishing the text); no sub-consensus claim sitting in neutral voice; no sentence whose conclusion requires two sources combined; the topic's independence case restated. A ref with no URL is "the known gap to surface, never to hide."

**The copyright router:** `copyright` is a router, not a gate — it decides *where* readers verify a source, never whether the text may be cited. This widens the corpus: modern in-copyright commentaries can serve as claim sources, since facts are not copyrightable and the passages stay private in the vault.

### E3. Dry run → ask → execute

- **Dry-run always first** (`kwiki publish` without `--execute`): shows the title, create-vs-update, the wikitext, and for updates the diff against the live article. `dry_run=True` is the default on the MediaWiki client and every publish path.
- **Ask, per article:** "Approval for one article is not approval for the next. Do not batch-publish because the human approved one."
- **Execute:** sandbox first by default (it renders on the real wiki, with real templates and fonts, where rendering problems become visible), then `--mainspace --execute`. The edit summary is fixed and disclosing — `pipeline-assisted draft, human-reviewed` — and must never be removed or softened: transparency is what separates this project from the machine-translation flooding that damaged other small-language Wikipedias.
- **Update path:** insert-only merges; conflicts are flagged ⚑ and read to the human verbatim — "they are the cases the pipeline refused to decide, and deciding them is the human's job."

### E4. Paced rollout and the feedback loop

Small batches; method disclosed on a project page naming every pipeline-assisted article and its reviewer; community reaction absorbed before scaling. On-wiki feedback (reverts, talk-page critique, editor corrections) is first-class feedback-loop input, classified by causal stage exactly like an audit finding, feeding the step-13 prompt-patch discipline. "Never scale volume because the last batch went quietly." bo.wikipedia has no policy on machine-assisted content; the project reads that vacuum as *stop* — a public bilingual village-pump proposal precedes content.

---

## Appendix 1 — Numbers to quote

| Quantity | Value |
|---|---|
| Corpus | Praise to the Twenty-One Tārās (Tōh. 438) + 16 commentaries, ~540k chars, 5 schools |
| Root units | 22 stanzas + invocation (23 units); benefits section `^a-1`–`^a-7` |
| TOC trees | 16 promoted; 15 clean under both checkers, 1 (gendun-gyatso) pending a source-check rerun after a post-QC restamp |
| Claims | 2,975 across 16 files (62–368 per commentary), all cited to source blocks |
| Spine | 24 registered slots; 16 spine maps |
| Consolidated pages | 24 slot pages + 43 term pages = 67, all double-gated design |
| Pilot consolidation audit | 418 citations re-checked; 0 fabricated IDs; 1 critical + 1 moderate + ~16 minor → Rules 9–16 + two standing gates |
| Coverage check | catches 5–12% of mapped claims per page |
| Keyword funnel | 193 EN candidates → 370 → 367 Tibetan terms → 114 pass gate v1 → 44 standalone subjects (+47 section, +10 glossary, +13 merged) → 25 update / 19 create |
| Batch articles | 43 term-articles drafted (1 refused for no citable claims) + 23 slot-articles; 42 imported |
| Batch verification | 882 quotations, **861 (97.6%) character-for-character verbatim**; 1/42 validator-clean; error mass V2×269 = ref-format mismatch between the two factories |
| Pilot (kwiki chain) | 3 articles end-to-end, cross-model audited, ledger `verified`, 81/81 citations block-located; audit-stability pass rates 0.67/0.67/1.0 over 3 runs |
| Style revision (v2) | 2 linguist review rounds → `wiki-article-from-claims-v2` (wikivoice, ref cap 3, quote budget 2, punctuation contract, `author_in_use`); 3 Mode B pilots in `work/pilot-v2/` awaiting approval; `author_in_use` curated on all 16 commentaries + synced to all 16 claims files |
| Cost (pilot) | 22 model calls, ≈$0.33–1.42/article (central ≈$0.71) on Gemini 3.5 Flash; 100k articles ≈ $35–70k machine cost — the constraint is reviewer-minutes, by design |
| Published | **0** — deliberate; community consent precedes content |

## Appendix 2 — Honest open items (know these before Q&A)

1. **W2 everywhere:** no source has a public URL yet (`wikisource_text_url: None` ×17), so no citation is reader-verifiable online. The copyright router says how to fix it (BDRC fetch → PD texts to Wikisource, the rest BDRC/WeBuddhist links). An article whose quotations a reader cannot check is the failure mode the pipeline exists to prevent — this is the single biggest pre-publication debt.
2. **V2 reconciliation:** the 269 V2 findings are the skill-flow ref format vs the registry-composed format — a mechanical bridge fix, but until it lands, 41/42 batch articles show validator FAIL.
3. **21 quotation misses** (2 import artifacts, the rest real) + 3 unsourced sections + 1 category + 1 script error.
4. **Ledger:** batch articles are `drafted`; the audit stage (6b) and per-article verify have not run over them, so none can reach `verified` yet. Gate 2 (`claims-consolidation-audit`) has run on only a few of the 43 term pages — and where it ran it found real critical defects with quote checks clean, so it is not skippable.
5. **`rails_status: draft` corpus-wide:** no consolidated page has been promoted `complete` by a domain specialist; the vault rule that transformations generate from complete rails is being consciously waived and recorded per article.
6. **Registry drift:** the 43 term-level topic slugs are not in `vault-annex.md` §2a's slot registry (which defines 24); either the registry grows or those pages sit outside the "slots are never coined locally" rule. Similarly `claims-methodology.md` §7a still says only 1 spine map exists — stale; all 16 exist.
7. **Two annotated copies of the corpus** still exist (vault `1-SOURCES/` for the rails route; `corpora/tara21/source/` for the kwiki route) — the citation chain is intact in both, but the duplication is real and scheduled to collapse.
8. **No dgag-lan signal in this corpus** (0 reception-contested claims in 2,975): a praise-commentary genre explains and extols. The reception-weighting machinery is demonstrated adversarially on the Bodhicaryāvatāra corpus (7,279 spans, ten commentaries, the Ju Mipham exchanges).
9. **The v2 redraft is pending, deliberately:** 68 of 69 drafted articles still carry v1 register and old-form author names; the corpus-wide Mode B redraft waits on the linguist approving the three pilots — never batch-redraft ahead of the human gate. Three `author_in_use` values are flagged for human verification (sungrab-tulku looks institutional; taranatha's long vowels; drakpa-gyaltsen's numeral formatting), and `sources.yaml` authors are stale for the two re-attributions.
