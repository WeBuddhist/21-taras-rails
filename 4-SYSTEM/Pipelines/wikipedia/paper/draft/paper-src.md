%TITLE Expanding the Digital Footprint of Tibetan: A Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs
%AUTHOR Tashi Tsering — The OpenPecha Project · tashitsering@dharmaduta.in
%DATE Working draft, 10 August 2026 — single-file version for review; evaluation slots that await team data are marked [TO FILL]

**Abstract.** Tibetan is spoken by some seven million people and carries one of the largest classical literatures in Asia, yet it is nearly absent from the open digital text that modern language technology learns from: its Wikipedia holds roughly 8,000 articles, and large language models score below the random-guessing baseline on Tibetan understanding benchmarks. This paper presents a working, semi-automatic pipeline that turns a Tibetan root text and its commentaries into cited Tibetan-language Wikipedia articles, with machine drafting bounded on every side by verification and a human editor — not a model — as the sole publishing agent. The pipeline covers the full chain: conservative cleaning, normalisation, no-loss segmentation, structural-tree extraction under dual deterministic quality gates, verse alignment, atomic claims extraction, question-driven consolidation with adversarial audits, claims-only article drafting, and a character-exact quotation gate that no model verdict can waive. As a case study we process the *Praise to the Twenty-One Tārās* with sixteen Tibetan commentaries, producing 2,975 typed, source-anchored claims, 24 consolidated topic pages, and six drafted articles. In the audited pilot, all 81 quotations across three generated articles verify character-for-character against their cited sources, and an independent cross-model audit caught five blocking errors that a same-model audit had passed — four confirmed by hand. We argue that the difference between machine content that degrades small-language wikis and machine content that revives them is a single variable: verification before publication, with a human hand on the gate. The pipeline's by-product — a typed, school-tagged, block-located claims database over a verse-aligned commentarial corpus — is a research artifact for Tibetan studies independent of Wikipedia.

**Keywords:** Tibetan · low-resource languages · Wikipedia · large language models · grounded generation · citation verification · digital humanities

## 1. Introduction

Tibetan is spoken by some seven million people and carries one of the largest classical literatures in Asia, yet its digital footprint is out of all proportion to both facts. As of July 2026 the Tibetan Wikipedia holds roughly 8,000 content articles — against hundreds of thousands for comparable-population European languages — with about 31 active editors in a given month, two administrators, and on the order of 350 new articles a year (bo.wikipedia statistics, verified July 2026). The consequences now compound in a new place: large language models. On the TLUE benchmark, most large models score *below the 25% random-guessing baseline* on Tibetan multiple-choice understanding — GPT-4 at 17.5%, Qwen-2.5-72B falling from 84.7% in Chinese to 16.5% in Tibetan — and byte-level tokenizers make Tibetan text roughly four times as expensive to process as Chinese (Petrov et al. 2023). Ask a commercial AI assistant a basic question about Tibetan culture *in Tibetan* and it fails, not because Tibetan knowledge is obscure, but because the open digital text those systems learn from barely includes it. Kornai (2013) called the endpoint of this trajectory *digital language death*; recent surveys of under-represented mid-size languages call them "invisible giants."

The dynamic is cyclical, and that is the point of this paper. Wikipedia is, by the Wikimedia Foundation's own account, almost always the largest source of training data in a language model's corpus; per-language model performance correlates measurably with a language's share of pretraining text. A language with a rich Wikipedia becomes a language that machines can serve — search, translation, question-answering — which in turn lowers the cost of producing more content in it. A language without one is locked out of the loop entirely. The cycle can be entered deliberately: Wales did it as government policy from 2017, growing Wicipedia from 91,000 to over 280,000 articles precisely so that Welsh would be visible to technology companies, and Welsh machine translation improved on the back of it.

This paper presents a working, semi-automatic pipeline built to enter that cycle for Tibetan: from a root text and its commentaries to cited Tibetan-language Wikipedia articles, with machine drafting bounded on every side by verification — and a human editor, not a model, as the sole publishing agent. As a case study we run it over the *Praise to the Twenty-One Tārās* (སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ, Tōh. 438) together with sixteen Tibetan commentaries spanning Sakya, Geluk, Jonang, Nyingma, and Kagyü authors from Drakpa Gyaltsen to living teachers. The choice is deliberate on methodological grounds: a bounded, heavily commented classical text with a living interpretive tradition yields a corpus in which every generated statement can be checked against named human sources — the property the whole design depends on.

We are aware — and §3 makes it the paper's spine — that "AI content for small Wikipedias" currently names a disaster, not a hope. The mechanism this paper celebrates is the same one that filled small-language wikis with machine-translated debris and got Greenlandic Wikipedia closed. Our claim is not that automation helps small languages. It is that *the sign of the feedback loop is determined by verification*: unverified machine content degrades the corpus and the models downstream of it; human-gated, citation-audited content upgrades both. The pipeline exists to hold that line, and the paper reports — including its failures — how the line held in practice. The scope of the evidence is stated up front: a complete pipeline; a deeply audited three-article pilot; a rails-side corpus of 2,975 extracted claims, 24 consolidated topic pages, and a 418-citation adversarial audit; three further articles drafted from the consolidated pages; and, as of writing, **nothing yet published to the live wiki** — these are early outputs, not a revived encyclopedia.

*[Figure 1 near here: the feedback loop with its sign — the doom spiral (unverified machine content → degraded corpus → degraded models) against the verified cycle (cited articles → digital footprint → better tools → faster articles).]*

**Contributions.**

1. A working end-to-end pipeline: raw OCR → cleaned, block-addressable sources → structural trees → atomic claims → consolidated topic pages → cited Tibetan wikitext, with a deterministic character-exact verification gate (§5).
2. A measured negative result about self-evaluation: a same-model audit returned "publish, no findings" on drafts in which an independent cross-model audit found five blocking errors, four confirmed by manual adjudication (§8).
3. An adversarial-audit error taxonomy — from a re-check of every one of 418 citations on three consolidated pages — converted wholesale into executable consolidation rules and two standing verification gates (§5.10, §8).
4. The claims database itself as a dataset: 2,975 typed, school-tagged, block-located claims over a verse-aligned commentarial corpus (§7).
5. A transferable design pattern for under-resourced languages: model judgment everywhere, model authority nowhere (§9).

**Research questions.** RQ1 (*fidelity*): can an LLM pipeline produce Tibetan encyclopedic text whose every quotation and locator is verifiably real — by construction, not by sampling? RQ2 (*layered verification*): what do independent verification layers — a deterministic gate, a cross-model audit, an adversarial consolidation audit — catch that a single check, especially a same-model check, misses? RQ3 (*economics*): does supervised automation change the review-time arithmetic enough to make a small-language encyclopedia reachable within a generation? §8 answers them in order; RQ1 and RQ2 with measured results, RQ3 with the measured machine side and a boxed **[TO FILL]** for the human side.

## 2. Related work

**LLM-to-Wikipedia systems.** STORM (Shao et al. 2024) established the research→outline→draft→cite architecture and the editor-rubric evaluation we borrow; Co-STORM added the human steering the discourse. WikiChat (Semnani et al. 2023) demonstrated the grounding filter — generate freely, keep only what retrieved sources support — reaching 97%+ factual accuracy in 25 languages, Tibetan not among them. WikiCrow (FutureHouse 2024) generated cited articles for all 15,616 unnamed human genes and showed machine drafts can *out-cite* human baselines: 86.1% citation precision against 71.2% for human Wikipedia articles in the 2024 PaperQA2 evaluation, with 13.5% of cited statements unsupported (its December 2023 demo separately reported a 9% incorrect-statement rate — a different metric from a different year). XWikiGen and OutlineGen are the closest low-resource precedents, without citation grounding or a human loop. No published system does citation-aligned LLM article generation for Tibetan; the contribution here is the combination — a severely under-resourced language, retrieval-grounded cited generation, hard verification, and a direct path to community publication.

**Attribution and grounding evaluation.** The evaluation literature distinguishes whether a citation *exists*, whether it *resolves*, and whether the cited source *supports* the statement — the AIS family of "attributable to identified sources" protocols, and the rater-judged citation-precision numbers reported for systems like WikiCrow, all measure the last of these. This paper's deterministic gate measures something stricter and narrower: character-level identity of the quoted evidence and resolution of its block-level locator. Fidelity and support are complementary, not competing, and we keep them strictly separate in §8. One background fact shapes the design: no NLI or attribution model supports Tibetan, so support judgment is manual by necessity — itself a datum for §1's gap argument.

**Wikipedia and under-resourced languages.** The honest half of this literature is a failure catalogue, and we cite it before our reviewers do. Scots Wikipedia: roughly 23,000 articles written by one enthusiastic non-speaker, credibility destroyed. Cebuano: six million bot stubs and recurring closure proposals. Greenlandic Wikipedia: *closed by the Language Committee in 2025* over machine-generated content; Inuktitut estimated two-thirds MT-contaminated; several African-language wikis at 40–60% uncorrected machine translation (MIT Technology Review, September 2025). Thompson et al. (2024) found a startling share of all low-resource web text is already multi-way machine-translation junk, and Shumailov et al. (2024) showed models collapse when trained recursively on synthetic data (with the nuance that *replacement*, not accumulation, drives collapse). Against this: Content Translation articles — machine draft plus mandatory human edit — show *lower* deletion rates than from-scratch articles across 2.4M+ creations, and curated synthetic corpora approach real-data quality. The failure mode and the working mode differ in exactly one variable: verification before publication. The positive precedents — Welsh policy, the Dzongkha Wikipedia Education Program (dozens of participants, five months, ~80 new articles, fully manual — the closest Tibetic-script effort and the effort-per-article baseline to beat), Masakhane's participatory model — all keep speakers in charge of what ships.

**Tibetan digital infrastructure.** The pipeline consumes, rather than duplicates, two decades of Tibetan digital philology: BDRC's catalogue and scans, OpenPecha's e-text corpus work, ACIP, Adarsha, and the translation libraries (84000, Lotsawa House). These are the citation targets of §7's data model; none of them, however, licenses its *text* for the CC BY-SA reuse Wikipedia requires — a constraint that §5 turns into a design principle.

**LLM-assisted encyclopedic writing risks.** Hallucination, citation fabrication, and close paraphrase are the known failure classes; English Wikipedia's G15 speedy-deletion criterion (August 2025) now deletes LLM pages with fabricated or unresolvable references on sight. §5 describes how each class is answered *by construction* — including a deterministic check no prompt can talk its way past.

## 3. Why automation at all: the three options

There are only three ways to grow a small-language Wikipedia to a useful size, and two of them are measured failures.

**By hand.** The manual mode's throughput on the Tibetan Wikipedia is a matter of public record: roughly 350 new articles a year since 2020, 31 active editors in a typical month, two administrators — and, eighteen years after founding, a total the size of a single English-language WikiProject. Organized effort does not escape the arithmetic: the Dzongkha Wikipedia Education Program, the closest Tibetic-script precedent, took institutional backing, dozens of trained participants, and five months to produce about eighty articles. The authors' own editor-training programs for Tibetan Wikipedia point the same way **[TO FILL: workshop counts, dates, cohort sizes, retention]**. At the measured rate, a minimally serviceable encyclopedia — call it 100,000 articles — is more than two centuries away. This is not a criticism of the editors; it is the measured capacity of the manual-only mode under real conditions.

**Unsupervised automation.** Demonstrated at scale, and demonstrably catastrophic: Scots, Cebuano, Greenlandic (§2). It reaches volume by destroying the property — trustworthiness — that makes volume worth having, and it poisons the training corpora downstream.

**Supervised automation.** Machine drafting under hard verification, throughput bounded by human review capacity, a named human as publisher. This paper's pipeline is an existence proof of the third option, and the rest of the paper is its mechanism and its measurements.

We claim no demonstrated alternative to the third option reaches critical mass within a generation. The number that turns this from rhetoric into a finding is **reviewer-minutes per audit-passed article versus historical editor-hours per article, projected to a target encyclopedia size**. The machine side of that fraction is now measured (§8); the human side is being measured with the planned evaluation batch **[TO FILL: reviewer time logs]**, and §8 states exactly which cells of the table are real today.

## 4. Corpus and case study

The corpus is the *Praise to the Twenty-One Tārās* — the opening invocation, the twenty-one homage stanzas, the closing couplet, and the benefits section (ཕན་ཡོན) — together with sixteen commentaries totalling ~540,000 characters, from a curated dkar-chag supplied by the team with titles, authors, genres, and school attributions (Table 1). In the alignment run reported below, 23 root units are alignable (invocation plus 22 stanzas), each with a stable block ID.

*Table 1. The sixteen commentaries.*

| # | Siglum | Author | School | Genre |
|---|--------|--------|--------|-------|
| 1 | TARAC02_DGT | Jetsün Drakpa Gyaltsen | Sakya | rnam bshad |
| 2 | TARAC03_GDD | Gendün Drub (1st Dalai Lama) | Geluk | ṭīkkā |
| 3 | TARAC04_GDG | Gendün Gyatso (2nd Dalai Lama) | Geluk | rnam bshad |
| 4 | TARAC05_TRN | Tāranātha | Jonang | rnam bshad |
| 5 | TARAC06_NDB | Ngülchu Dharmabhadra | Geluk | rnam bshad |
| 6 | TARAC07_KTK | Könchok Tabkhé | Geluk | ṭīkkā |
| 7 | TARAC08_DTG | Dorlop Tenga Tulku | Sūryagupta lineage | commentary on benefits |
| 8 | TARAC09_ANON | anonymous (no colophon) | Sūryagupta lineage | bstod 'grel |
| 9 | TARAC10_DPN | Dombu Pema Namgyal | — | commentary |
| 10 | TARAC11_KMT | Karma Maitri | — | condensed commentary |
| 11 | TARAC12_PDS | Khenchen Palden Sherab | Nyingma | word commentary |
| 12 | TARAC13_TDZ | Sermé Tsang Geshé Tendzin Dönzang | Geluk | bstod 'grel |
| 13 | TARAC14_LZD | Geshé Lobzang Dawa (ed.) | Geluk | interlinear notes |
| 14 | TARAC15_SNT | Sangyé Nyentrul | — | word commentary + visualization |
| 15 | TARAC16_PSR | Draphar Dramé Sungrab Tulku | Geluk (contemporary, 2023) | rnam bshad |
| 16 | TARAC17_TSN | Khenpo Tsültrim Namdak | Kagyü | commentary |

The school composition is skewed — seven Geluk commentaries, one or two for each other tradition, three unattributed — and §6 and §9 treat that skew as data the pipeline must respect, not noise.

The root text is a **critical edition**, and the editorial act matters downstream. It replaced an OCR export because the OCR's verse segmentation was wrong — homages were split across two or three blocks each instead of one block per four-line stanza — and because the export stopped mid-clause at the end of the twenty-first homage, omitting the entire benefits section that every commentary in the corpus comments on. The edition's own metadata records that its two witnesses differ in reading at **17 of the 21 homages** (e.g., homage 3 གསེར་སྔོ vs. སེར་སྔོ; homage 12 ཟླ་བའི་རྩེ་མོས vs. ཟླ་བའི་དུམ་བུས), and the superseded witness is retained alongside. Because the pipeline is *sic*-faithful to whatever the ingested edition says (§5.12), textual correction happens here, at the source layer, or not at all.

Every verse and discrete prose block carries a stable block ID — the corpus-wide citation primitive:

```
ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་ཕྱེ་བ་ལས་ནི་བྱུང་མ། ། ^1-1
```

Ingest is deterministic and reproducible: conservative cleaning (Unicode NFC normalisation, U+0F0C→U+0F0B, page-number lines dropped — stored Tibetan punctuation is otherwise never "fixed"), then segmentation through production scripts, no-loss-gated. Re-running the ingest script reproduces every source file byte-for-byte — a property verified by rebuilding the corpus from the raw upload on a second machine and obtaining byte-identical verification reports (§8).

One honesty note the paper keeps visible: the corpus currently exists in **two annotated copies** — a rails-side copy carrying structural sa-bcad headings, and a pipeline-side copy carrying flat block IDs plus root-verse transclusion anchors. The two annotation conventions have not yet been unified on one copy; the citation chain is intact in both, and the duplication is scheduled to collapse into a single set of source files.

## 5. The pipeline

### 5.0 Design frame

The pipeline is a set of *skills* — versioned, step-by-step procedures, one specification file per operation — driven by a tested Python command-line tool (547 passing tests) and a family of small deterministic scripts. Three principles repeat at every stage:

1. **The model judges; the script verifies.** Linguistic judgment — what is a structural announcement, what does a passage claim — is model work; everything checkable (byte identity, count arithmetic, ID resolution, structural invariants) is done or re-done by deterministic code that fails closed. Every stage ends in a gate a model cannot talk its way past.
2. **Isolation over context.** Wherever precision matters, work is split into single-purpose model calls that see only their own input — one chunk, one node, one commentary, one topic packet — so an error cannot propagate by contamination and a task cannot drift into its neighbour's instructions.
3. **Nothing interpretive touches the source layer.** Source files receive only structure: block boundaries, IDs, headings, navigation links. Every script that writes near a source file carries a no-loss assertion that aborts if a single non-whitespace character changed.

*[Figure 2 near here: pipeline diagram — ingest (5.1–5.6) → claims and consolidation (5.7–5.10) → articles and verification (5.11–5.12) → publication (5.13).]*

*Table 2. The stage map.*

| # | Stage | Skill / module | Deterministic gate | Output |
|---|-------|----------------|--------------------|--------|
| 1 | Cleaning | clean-raw-text | profile shown before any change; never overwrites raw | cleaned working copy |
| 2 | Normalisation | tibetan/normalize.py | NFC on ingest; comparison keys only | — |
| 3 | Segmentation | format-tibetan-root-text; commentary-segmentation | no-loss assertion (whitespace-squeeze equality) | block-ID'd source files |
| 4 | Structural annotation | tag-inline-toc | prose-integrity diff-back | headings + inline wikilinks |
| 5 | TOC-tree extraction | toc-tree-extraction (4 isolated passes) | two QC checkers, both zero-issue | per-commentary sa-bcad tree |
| 6 | Alignment | transclusion skill; stages/align.py | span-existence verification | verse↔commentary span map |
| 7 | Claims extraction | tree-guided-claims (per-node agents) | verify_claims.py (4 hard checks) | per-commentary claims file |
| 8 | Spine mapping | spine-map (one agent per commentary) | verify_spine_map.py (disposition completeness) | per-commentary routing table |
| 9 | Packet assembly | assemble_packet.py (script, no model) | non-zero exit on any gap | per-topic packet + manifest |
| 10 | Question generation + consolidation | claims-consolidation (one agent per topic) | manifest-diff coverage check | consolidated topic page |
| 11 | Consolidation audits | verify_consolidation.py; claims-consolidation-audit | gate 1 zero-error; gate 2 no critical/moderate | audit report |
| 12 | Article generation | article chain / wiki-article-from-claims | claims-only invariant enforced in code | article wikitext + citations |
| 13 | Verification | tibetan/verify.py; wiki/validator.py | character-exact quotations; rules V1–V12 | verify report |
| 14 | Publication | publish command | dry-run default; ledger must be verified | live edit (none yet) |

Two invariants govern the article chain, stated as such in the project's canonical pipeline document:

> **Invariant 1.** Nothing downstream ever touches source wording after the claims stage — the claims table is the only drafting input; passages remain in the corpus as verification material.
> **Invariant 2.** Nothing is published that hasn't survived the audit and the pre-publication review. Everything else is replaceable machinery around those two rules.

Because the paper's argument is layered defense, Table 3 gives the layers in one view — each known failure class, the layer that catches it, and the on-disk evidence that the layer has actually fired at least once.

*Table 3. Failure classes × catching layer × evidence.*

| Failure class | Catching layer | Evidence it fired |
|---|---|---|
| Misquotation / quote drift | deterministic gate (exact/collapsed tiers only) | tsheg→shad substitution caught at similarity 0.974; 81/81 quotations verified |
| Citation fabrication | ref-resolution rule + citation-existence check | 0 fabricated claim IDs in 418 audited citations; placeholder catalogue blocks dummy URLs |
| Wrong block locator | locator resolution against the named block | 81/81 locators resolve; an earlier 0/81 report traced to an environment fault, not the artifacts |
| Added fact | audit category, blocking in code | "and none dispute it" caught and blocked |
| Attribution loss | audit category, blocking in code | commentator named beyond what the claim stated — caught, blocked |
| Consensus exaggeration | audit (dropped-qualifier) + consolidation rule 9 | "many scholars" for three — caught; 7-of-11 partial-support padding caught |
| Silent claim loss | disposition completeness + packet assembler + coverage check | assembler exits non-zero on gaps; 5–12% per-page gaps caught and closed |
| Count errors | deterministic recomputation of every count label | five of five hand-tallied labels wrong on one page — all caught |
| Invented structure (TOC nodes) | attestation checks in both tree QC gates | misattachment and lost-cursor cases on early trees — recorded, then caught by the second checker |
| Close paraphrase | audit reading + human pre-publication review | named residual risk — not fully mechanized (§9) |

Finally, "semi-automatic" is not a mood; it is an enumerable set of human decision points (Table 4).

*Table 4. Human checkpoints.*

| # | Checkpoint | What the human decides |
|---|---|---|
| 1 | Cleaning profile | approves the debris profile before any cleaning script runs |
| 2 | Segmentation residue | hand-places boundaries the rule engine flags as unresolvable |
| 3 | Tree QC sign-off | accepts or rejects genuinely-ambiguous checker findings |
| 4 | Term/topic list | approves machine-proposed candidate terms before article work |
| 5 | Rails promotion | only a domain specialist sets status: complete — never the model |
| 6 | Pre-publication review | checklist over references, voice, synthesis, notability |
| 7 | Publication | the explicit --execute; dry-run is the default everywhere |

### 5.1 Cleaning

The cleaning skill does not clean directly: it *profiles* the raw OCR/PDF text, reports the profile to the human before touching anything, then generates and runs a bespoke cleaner limited to eight mechanical transformations — page markers, running headers (lines repeating verbatim more than five times), non-breaking-tsheg replacement, mid-word spaces, orphaned-fragment joins, and blank-line collapse. The skill's rules are the contract:

> 1. **Never overwrite the raw file.** Output goes to a working copy only.
> 2. **Do not interpret text.** Do not fix spelling, do not paraphrase, do not add or remove content beyond the mechanical issues listed.
> 7. **Non-breaking tshegs (U+0F0C ༌) are always replaced** with the standard inter-syllable tsheg (U+0F0B ་). This is never ambiguous.
> 8. **Extra mid-word spaces** are removed — the space is deleted, not replaced.

Verse lines (heuristic: ending in །། or ། །) are never collapsed into prose; ambiguous repeated lines are flagged and asked about, never silently removed. The generated cleaner's core constants show how narrow the permitted surface is:

```
PAGE_MARKER = re.compile(r'^\s*-\d+-\s*$')
MID_SPACE   = re.compile(r'([ༀ-࿿]) +([ༀ-࿿])')
NBT, STD_TSHEG = '༌', '་'
```

The worked example bundled with the skill records the false-positive discipline that makes header-stripping safe: the running header also occurs legitimately mid-sentence as a title reference, so the script strips a line only when the string is the *entire* stripped line content, never a substring. What cleaning explicitly does not do — repair broken syllables, restructure headings, fix OCR readings — is deferred to later stages or to the human edition (§4).

### 5.2 Normalisation

Normalisation is a shared library, not a stage that edits files. Its module documentation is the design statement:

> Every guarantee this pipeline makes about a quotation is really a claim about *which* normalisation was compared, so the verifier, the aligner and the term selector must not each grow their own — that drift is exactly how a citation ends up looking checked when it is not.

The ladder has four rungs, loosest last: **nfc** (canonical composition — the storage form of everything on disk); **collapse** (NFC minus whitespace — line wrapping legitimately differs between a source file and the article quoting it, and nothing else may; this is the verbatim-comparison key); **strip_markup** (NFC minus the editorial furniture inside source files — transclusions, block IDs, wikilink wrappers); and **fuzzy_key** (all of the above minus every shad, tsheg, and head mark — tolerant of orthographic variation between editions, and therefore *a warning, never a pass*). The characters fuzzy_key drops are exactly the six that editions disagree about more often than they disagree about letters:

```
FUZZY_DROP = frozenset("།༎་༅༄༈")
```

Each reduction also returns an offset map back into the canonical text, so a match found in a reduced view is reported at its true character offset in the stored file. Nothing in the module edits stored data: these functions build comparison keys; the Tibetan punctuation in the corpus is never touched.

### 5.3 Segmentation

**Root text.** A cleaned root text becomes one-stanza-per-paragraph verse with chapter-relative block IDs, driven by a small grammar of Tibetan punctuation: ། ། (shad, space, shad) is the verse-line separator; a single shad flanked as ག །ན marks two half-verses merged onto one physical line and must be split (the regex carries a negative-lookbehind so the second shad of a ། ། pair never matches); a stanza is typically four verse-lines, one block ID per stanza; and the double-shad །། appears *only* in chapter colophons, never in regular verse — which is what makes colophon detection, and hence chapter-boundary detection, reliable. Two deterministic formatters implement the grammar (one auto-detects chapters from the text's own colophon formula; one is table-driven).

**Commentaries.** A commentary is broken into citation-sized blocks — one to two sentences of prose, one stanza per verse block, one quotation per quote block; a prose block over roughly forty tsheg-delimited syllables is split unless it is a single indivisible clause. The stage-1 segmenter is a rule engine over seven lexical boundary cues: terminal particles (འོ/ནོ/དོ/སོ… plus །), quotation closers (ཞེས་སོ། ། and variants), quotation openers (…ལས།), enumeration heads (…ལ་གསུམ་སྟེ།), ordinal openers (དང་པོ་…), the objection pair (…ཞེ་ན། / འོ་ན་…), and a protected verse-stanza detector — a run of two to four clause units of six to eleven syllables each, uniform in length, is peeled out whole and never re-cut. What makes the stage safe to run at all is the no-loss gate, in code:

```
def assert_no_loss(original, segmented):
    if _squeeze(original) != _squeeze(segmented):
        sys.exit("ABORT: segmentation altered non-whitespace content. No file written.")
```

The residue no lexical cue can cut is flagged for a human, whose hand-edit rules insert paragraph breaks only at genuine topic shifts and end with the stage's stated bias: "When a passage genuinely cannot be cut without breaking sense, leave it whole. Over-long is safer than wrong."

### 5.4 Structural annotation

Tibetan commentaries announce their own structure inline: the author enumerates the coming sections (the sa-bcad) before elaborating each. The pipeline makes that structure navigable in two coordinated layers. Editorial headings carry block IDs that always end in a reserved zero slot (^1-0, ^1-2-0, …), so a heading ID can never collide with a content ID; the convention scales to real depth — one commentary in this corpus nests to seven levels (^1-2-2-1-1-3-1-0). And each announced term is wrapped in a wikilink pointing at the heading it announces, so the enumeration sentence links forward to its section:

```
ལེའུ་དང་པོ་ལ་[[#^1-1-0|མདོར་བསྟན་པ་]]དང་[[#^1-2-0|རྒྱས་པར་བཤད་པ་]]གཉིས་ཡོད་པ་ལས།
```

The annotation skill's architecture is the paper's clearest statement of the model/script division of labour. Detection is *model-only* — the skill forbids regex extraction, on recorded experience: sa-bcad surface variants are too many, "every rule spawns three exceptions, and tuning it is an endless loop." Rendering is *script-only*: block IDs are derived from depth by code, so numbering bugs are impossible by construction; wraps are exact substrings; and the result is diffed back against the source —

> Because wraps are exact-substring and the result is diffed back against the source, silent transcription drift is caught and the run fails loudly. **The model never retypes prose** — it only points at substrings that already exist.

The renderer's gate raises "PROSE INTEGRITY VIOLATION" with the first divergent line if any wrap or heading insertion altered a character of prose. The skill's change log also records a corpus-driven design lesson: this corpus's commentaries open sections with bare ordinals (དང་པོ་ནི།, གཉིས་པ་ནི།) recurring up to forty times per file with no unique substring anywhere on the line — which forced line-number anchors into the annotation contract, because a purely context-based contract left those sections unannotatable. Annotation contracts must be corpus-tested, not assumed.

### 5.5 Structural-tree extraction

Each commentary then receives a complete nested decimal tree of its sa-bcad — the scaffold that claims extraction, spine mapping, and consolidation all lean on. The extraction is explicitly an *orchestrator*, and the reason is a finding about prompt design:

> The precision comes from task isolation: each pass is a separate call with only that one task's prompt and only the relevant input. The candidate-extraction call never sees the tree-building instructions, so it cannot drift into tree-building; the verbatim-copy call never sees the "interpret and reconcile" instructions, so it stays literal. Merging the four jobs into one prompt collapses that isolation and precision drops.

**Pass 0** chunks the file deterministically — 150-line windows with 25-line overlap, so every candidate appears whole in at least one window. **Pass 1** (one isolated call per chunk) extracts section candidates of three types — announcements (དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།), node headers (གཉིས་པ་འགྱུར་ཕྱག་ནི།), and closing counts (ཞེས་རྣམ་པ་གསུམ་མོ།) — with the precision dial set explicitly: "when you are not confident that something is a structural section rather than incidental text, LEAVE IT OUT." **Pass 2** (one isolated call per chunk) copies out enumeration announcements *verbatim* under a strict start/stop rule:

> START at the topic word being divided. STOP the instant the division is closed: at the closing particle (ཏེ། / ལས། / འོ། / མོ། / ནོ། །) of the count clause. DO NOT continue into the next sentence. The sentence that begins elaborating the first part is commentary body. It must NOT appear in your output.

**Pass 3** (one isolated call) builds the tree, treating the author's own enumerations as *more authoritative than individual candidates* — used both to eliminate false positives (a candidate matching no enumerated part is suspect) and to fill gaps (every part of a genuine division must appear as a child; the child count must match the declared count) — with the counter-rule that doctrinal lists (items enumerated as subject matter, not as divisions of the text) must never become nodes. Titles are matched by meaning, not string equality (an enumeration's …མཚན་དོན་བཤད་པའོ། ། and a node header's གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ་ལ་གཉིས་ཏེ། are the same section); ordinals are kept but never fabricated; and the Tibetan ordinal must agree with the decimal's final segment.

**Pass 4** is the gate: two deterministic checkers, looped with fresh repair calls until zero issues. The first checks the tree against the model's own extraction corpus — indentation, ordinal↔decimal agreement, duplicate decimals, gap-free sibling sequences, and three-tier title attestation (exact match, then ordinal verification, then syllable-bigram coverage with a 0.5 floor below which a title is flagged as a possible hallucination). The second checks the tree against *the commentary itself*, and its own documentation is the most instructive paragraph in the project — an honest record of why self-consistency checking is insufficient:

> All three trees shipped [early in the project] reported zero issues from the first checker while carrying, between them: a top-level misattachment (twenty homage children filed under "explaining the benefits" instead of "the praise proper"), an unresolved anchor with an obvious textual anchor one line away, and seven collided line pointers (the value 130 repeated four times — the extractor lost its cursor). This script is the check that would have caught those, because it reads the one thing the other checker cannot: the commentary itself.

Its four checks: line-pointer validity (an unresolved pointer is *always* an issue), title attestation within ±3 lines of the pointer, document-order monotonicity plus a repeated-pointer collision signature (three or more nodes sharing one pointer = the lost cursor), and sibling-count congruence against the announcing text's own cardinal — the last flagged for human review rather than asserted as error, because Tibetan division phrasing is too varied to parse exhaustively. Promotion requires both checkers clean; the skill's gate rule: "never declare the tree clean on a subagent's say-so, and never report zero issues when a checker was not actually run." A finished tree, excerpted:

```
* 1. ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ [[22]]
   * 1.1 དང་པོ་མདོར་བསྟན་པ་ [[24]]
   * 1.2 གཉིས་པ་རྒྱས་པར་བཤད་པ་ [[31]]
      * 1.2.2 གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ [[45]]
         * 1.2.2.1.1.3.1 དང་པོ་སངས་རྒྱས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ་ [[71]]
```

All sixteen commentaries have promoted, QC-clean trees. One residual defect is recorded honestly *inside the affected downstream file* rather than hidden: one tree's line pointers drifted because its source file was re-stamped minutes after the tree's QC ran; the drift is documented in the claims file that inherited it and flagged for human follow-up.

### 5.6 Alignment

Two mechanisms, deliberately ordered — deterministic first, because alignment errors are silent: a verse anchored to the wrong span produces a citation that looks perfectly well-formed and is simply wrong. "Deterministic matching can fail to find a verse, but it cannot invent a location."

**Transclusion anchors.** Where a commentary quotes the stanza, an anchor line is inserted above the quotation, dry-run first, with variant-tolerant matching: lines match on a character-overlap ratio of at least 0.80, absorbing orthographic variants (བསྒོམ/སྒོམ, ཟློག/བཟློག); a fully quoted stanza beats a passing two-line citation; a single-line match is accepted only inside a citation frame (ཞེས་པ་ནི།). The skill's change record is a measured recall result on this corpus: **116 → 209 anchored verses (33% → 59%)** across sixteen commentaries × 22 verses, from three named root-cause fixes — a comparison that tested Tibetan against Latin transliterations and so could never return true (dead code on the single-line path), blank lines counted as mismatches (a fully quoted stanza scored one line of four), and no path for incipit citations. It also records the structural limit: the three commentaries still at zero are the word-commentaries (བསྡུས་འགྲེལ, མཆན་འགྲེལ), which dissolve the stanza into glosses and genuinely never quote it.

**Lexical clustering** handles the remainder. Instead of searching for the stanza as a string, the aligner asks where *fragments cluster*: each verse contributes probes (its whole lines, heavily weighted; short character n-grams, individually fragile but telling in aggregate); the densest windows of *distinct* probes are scored; and one cluster per verse is chosen under a monotonicity constraint:

> Commentaries follow their root text in order. Treating that as a constraint rather than a coincidence resolves the ambiguity that sinks naive matching: a phrase recurring in chapters 1 and 9 is pinned to the right one by its neighbours. This is a longest increasing subsequence weighted by cluster score.

On a benchmark chapter with ground-truth anchors, the method's precision/recall is 95–96% / 51–59% on prose commentaries and 58% / 19% on a word-commentary — a split the documentation calls "structural, not a tuning problem," and the reason recall is treated as a budget for LLM assistance rather than a target to tune upward. Any model-proposed span is re-verified to exist verbatim in its file before use: "we accept its *judgement* about which passage is relevant, never its *reproduction* of the text."

Result on this corpus (verified in review): **314 aligned spans over the 23 root units — 209 by transclusion anchor, 105 by clustering — with seven of sixteen commentaries at 100% coverage**, the lowest being exactly the condensed and interlinear genres the documentation predicts.

### 5.7 Claims extraction

The claims layer converts commentary prose into atomic, citable rows, under a principle fixed before any prompt was written: **extract first, merge later.** Extraction reads one commentary in isolation and records what *it* says; consolidation compares finished files and is disposable. Merge decisions made during reading are made with incomplete information — the first commentary read silently defines the topic space, and later commentaries of different granularity (a 24 KB condensed gloss versus a 400 KB treatise) map onto it badly.

Three extraction methods were run and compared as genuinely different techniques: a one-pass inventory under nine fixed categories (framing, glosses, iconography, doctrine, activity, ritual, benefits, external attributions, internal tensions); a re-bucketing of an existing extraction under the commentary's own tree, with a typed entity index added; and a fresh extraction guided node-by-node by the tree. The comparison's negative findings are why the third method is now the standard, and they are quantified: the "re-bucketed" run was not an independent extraction at all — **114 of 118 Tibetan strings in one file byte-identical** to the earlier run's, claim counts copied rather than recomputed, transcription errors inherited — and presenting a re-organisation as a second extraction hid real defects, including a cross-document contamination and a fabricated mantra promoted to canonical status. Five load-bearing guards came out of that audit, each traceable to a measured failure:

> 1. **Claim IDs are never node IDs** — the earlier files had 1.1 denoting both a claim and a section, five such collisions in one file alone.
> 2. **claim_count is computed by counting, at the end — never inherited or estimated.**
> 3. **A node-boundary check backs every claim's placement** — each node is read from its own line window alone, never the whole file, so a claim cannot be extracted under the wrong node by construction rather than by discipline.
> 4. **"stated" means the referent's verbatim name occurs in this claim's own quoted Tibetan** — on the earlier run, 7 of 14 claims so tagged in one file contained no form of the referent's name at all.
> 5. **Every claim is independently re-derived, never re-bucketed.**

Claim IDs take the form c-⟨node-decimal⟩-⟨n⟩ (node 1.2.3's third claim is c-1-2-3-3 — a string that cannot be mistaken for a heading number). Each per-node extraction call receives *only* the extraction rules, its node's line window, and its node's decimal and title — never another node's output, never another commentary's file. A real claim from the corpus:

```
#### c-1-1-4 Gloss: "Swift" (མྱུར་མ)
བོད་ཡིག: དམན་ཏན་ཇི་ལྟ་བུ་དང་ལྡན་ཞེ་ན། མྱུར་མ་སོགས་ཏེ། ཐུགས་རྗེས་སེམས་ཅན་གྱི་དོན་ལ་
སྐད་ཅིག་ཀྱང་གཡེལ་བ་མེད་པའི་འཕྲིན་ལས་བྱུང་བས་ན་ཕྱུརམ།
English: because her compassionate activity for the welfare of sentient beings
never lags even for an instant, she is called "the swift one."
Type: word-gloss · Referent: FIG-1 (section-opener)
Cite: (1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-5)
```

Disagreement *inside* one commentary is preserved, never averaged — a real internal-tension entry records both explanations of the "seven worlds" (one attributed to Drakpa Gyaltsen, one anonymous, both cited to the same block) side by side under a ⚑ flag. Each file also carries a typed grounding index (figures, persons, places, texts, events — source-attested only: "If the commentary says only 'the protector,' the registry entry is 'the protector,' not the deity the tradition means by it"), which every claim's referent field points into.

The deterministic backstop enforces four hard checks, with the exit code equal to the issue count: quote containment (every claim's Tibetan, normalised, must be a literal substring of its cited block — ellipsis-joined fragments are tested individually, which is what catches a claim quoting one real phrase and one invented one); claim-count recomputation; an ID-collision scan; and stated-referent validation. Repair is by fresh per-node call, and the discipline is explicit: "never suppress a finding to make the count read zero."

**State on disk: 16 claims files, 2,975 claims (62–368 per commentary), all status: draft** — the model never marks its own extraction complete.

### 5.8 Spine maps

Consolidation needs to know, for every commentary, which of its own tree nodes hold which canonical slot of the root text (the twenty-one homages plus the global topics: benefits, origin, structure). The pilot answered that question inside every topic run — correct but quadratic in the wrong variable: with sixteen commentaries and ~22 slots, it implied roughly 400 full-file reads of an unchanged 3.8 MB corpus. The fix is a routing-index layer: one small table per commentary, built once, reused by every topic. Its defining constraints:

> **Routing only — never interpretation.** This file records addresses. Do not restate, summarise, paraphrase, or evaluate a claim's content anywhere in it.
> **Node numbering is never assumed uniform.** One commentary nests a homage at 1.1.N, another at top level N, another titles nodes by epithet instead of ordinal, another runs all twenty-one homages inside a single undivided node. A numbering rule that worked for the last commentary is evidence of nothing about this one.
> **Every claim gets exactly one disposition** — routed by node subtree, routed by claim ID, flagged ambiguous, or logged unmapped. Neither zero (silent loss) nor two (silent duplication) is acceptable. Silence is a finding, recorded with a reason.

The hard case shows why this is model work and not a formula: one commentary carries all twenty-one homages inside a single undivided node, so its map routes by *claim-ID range*, using the extraction's own "Verse N quoted" claims as boundary markers — against a regular commentary whose ordinal-titled nodes route directly (slot tara-05 → node 1.1.5, ལྔ་པ་ཕྱག་འཚལ་). A deterministic verifier recomputes every count and enforces disposition completeness. All sixteen maps exist.

### 5.9 Packet assembly, question generation, and consolidation

**Packet assembly is a script, not a model.** For one topic slot, it collects the routed claims out of every commentary's raw file, copying each claim block **character-for-character** — "a script cannot mis-transcribe བོད་ཡིག" — and emits a manifest of every claim ID included. Its failure modes are loud by design; the two hard errors, verbatim:

```
ERROR: {id} has no disposition for slot `{slot}` — add a Slot map row
       or a Silent slots row to its spine map
ERROR: {id} has a raw claims file but no spine map — it is missing from
       this packet entirely. Run the spine-map skill on it before consolidating.
```

The second error exists because a commentary with claims but no map would be silently absent from every topic page — the exact "silent claim loss" failure the layer exists to prevent.

**Questions are generated, not authored.** The methodology fixes this in so many words:

> No human writes the question list. Two free sources: (1) from the spine, mechanically — twenty-one homages × observed facets (name/etymology, colour, implements, stance, activity, mantra, benefit) plus global topics ≈ a scripted question grid; (2) from the extractions themselves — every raw claim implies a question: one commentary's "the left hand's three fingers symbolise the Three Jewels" becomes "what does each commentary say the left hand symbolises?", asked of all the others. The union of both is the question set. This makes question-driven consolidation a **derived completeness check**: free extraction first, then generated questions catch what free reading missed.

Real generated questions from one topic page show the three kinds — grid ("How does each commentary etymologise the three names of the homage — Tārā, Swift, Heroine?"), inversion ("Does any commentary dispute whose tears produced the lotus Tārā arose from?"), and a *negative control* probing whether a commentary's silence is real ("Is lobsang-dawa's silence on this slot a real gap, or is the same content routed elsewhere in that commentary?"). A question nobody answers is kept on the page and marked "no commentary addresses this," never deleted.

**Consolidation** is one model call per topic, working only from the packet, writing per facet: **Consensus** (with full per-commentary attestation lists), **⚑ Divergences** (never flattened — a hard rule of the whole system), and **Unique** (single-commentary claims), plus a coverage table in which silence is itself a finding; citations are always ⟨commentary⟩:⟨claim-id⟩. From the finished page for the first homage: a fifteen-commentary consensus on the origin narrative — Avalokiteśvara, seeing that however many beings he delivered their number never diminished, wept; from his tears a lotus grew, and Tārā arose from its opened blossom — "attested, independently, in each commentary's own words, by every one of the fifteen contributing commentaries," followed by the full attestation list. Beside it, a divergence in which one side exists only as a commentator's report of unnamed "earlier commentaries" glossing the tears as Tārā's own — recorded as exactly that, never inflated into a live two-sided dispute.

Consolidation even surfaces **root-text-level variants**: the same page's first divergence records that one commentary's own quotation of the verse reads དཔལ་མོ ("Glorious One") where the corpus reads དཔའ་མོ ("Heroine") — two readings that license different etymologies for the same syllable — while flagging a second apparent witness as a probable transcription slip inside its own extraction. Consolidation here is a philological instrument, not just an aggregator.

After writing, the **coverage check** diffs the packet manifest against every claim ID the page cites; every claim in the gap is either folded in or logged with a one-line reason under "Claims reviewed, not separately cited" — no third state. In the pilot this caught real gaps in roughly 5–12% of a topic's mapped claims per page. **State on disk: 24 consolidated topic pages, all status: draft.**

### 5.10 The consolidation audits

Three pilot topic pages were adversarially audited: a fresh model context per page — one that did not write the page — re-checked **every one of 418 unique citations** against the raw claims files. Headline: **zero fabricated claim IDs; one critical finding, one moderate, roughly sixteen minor.** The critical case is the audit design's whole justification:

> **CRITICAL — gendun-gyatso:c-1-2-1 (Face section).** Cited as independently corroborating another commentary's "three flaws" framing (dust, mist/haze, cloud). The raw claim contains no flaws framing — only "face supremely white and beautiful like stacked full autumn moons." Correct attestation is almost certainly a different claim ID.

A deterministic script can prove a cited claim *exists*; only a reader can prove it *says* what the page attributes to it. The consolidator had a real corpus idea attached to the wrong claim ID — a failure no existence check can catch. The minor findings formed a stable taxonomy: partial-support padding of consensus lists; the same claim cited on both sides of one divergence; page-level harmonizations presented as a claim's own reading; epistemic upgrades ("endorses" for a tentative སྙམ་མོ aside); silently elided syllables in Tibetan quotes; hand-tallied count labels (**five of five wrong** on the worst page); and consulted claims with no disposition.

That taxonomy was converted directly into machinery. Each error class became either a consolidation rule (full-statement support; corroboration re-read, not remembered; one side per divergence; verbatim quotes or marked ellipsis; harmonization attributed to the page, never the claim; epistemic strength copied, never upgraded; counts computed, never hand-tallied; every consulted claim dispositioned) or a check in one of two standing gates:

- **Gate 1 — deterministic:** citation existence, per-paragraph recomputation of every "(N commentaries)" label, both-sides-of-a-divergence flags, disposition completeness against the coverage table, and citation-prefix discipline. Zero errors required. Validated by reproducing every mechanical finding of the human audit — plus one undispositioned claim the human auditor had missed.
- **Gate 2 — adversarial:** a fresh context that did not write the page checks every attribution against the raw claims — "an agent auditing its own consolidation re-reads its own intentions, not the text." Ground truth is the raw claims file only, never the auditor's knowledge of the tradition. Severity: critical / moderate / minor; report-only; the consolidator fixes, the auditor re-checks; no critical or moderate finding may remain.

A Tibetan-language consolidation variant produces twin pages under identical rules and both gates (bilingual structural headings — e.g., མཐུན་སྣང (Consensus) — keep the deterministic checker parsing), with a strict independence rule: the Tibetan consolidator must not read the English counterpart. The pairs double as a controlled comparison of consolidation quality by working language.

### 5.11 Article generation

Term and topic selection precede drafting and are a human gate: candidate terms were machine-proposed by corpus keyness (frequency × distribution across the sixteen commentaries) and are marked as candidates in the term registry — the registry records who, or what, proposed each entry, and no human has yet approved the list; topics on the second route come from the canonical spine. Existence is double-gated by §6's breadth doctrine and by the requirement of at least one independent, reliable, secondary source per topic.

Two drafting routes share one doctrine — **claims-only drafting** — and one gate (§5.12).

**Route A: the per-term chain** (extract → claims → outline → draft → audit), which produced the audited pilot's three articles (སྒྲོལ་མ "Tārā"; འཇིག་རྟེན་གསུམ "the three worlds"; སྡུག་བསྔལ "suffering"). The extraction prompt is written in Tibetan; its seven rules are the contract — quote character-for-character (ཡི་གེ་གཅིག་ཀྱང་བསྒྱུར་བ་དང་། བསྡུ་བ་དང་། ཚིག་སྒྱུར་བྱེད་མི་ཆོག — "not one letter may be changed, condensed, or paraphrased"), with the stated warning that a machine will check every letter; take only passages that *explain* the term, not mere occurrences; echo the block's own segment ID; never truncate; never flatten disagreement; write "no explanation given" (འགྲེལ་བཤད་མེད།) rather than invent; add nothing from your own knowledge. The claims prompt then compresses passages into the atomic table:

> One verifiable fact per claim, written in Tibetan in your own words. A claim with no supporting passage must not exist. Conflicting positions get one claim each — never merge them into a compromise no source states. **Forbidden: synthesis.** No claim may require two sources combined to reach a conclusion neither states alone. Claim type is weighted by authority and response, not headcount: a commentator who is the sole representative of his school in this corpus is a school-position, never a single-commentator.

From that point the sources are closed. The drafting prompt receives **only** the outline, the claims table, and a locked glossary — verified in code: the drafting stage's prompt constructor passes nothing else — and its closing line tells the model exactly how little it is trusted with:

> citations are **claim indices** into the supplied claims list. The pipeline attaches the underlying source quotations and renders the refs — you never write a ref or a URL.

Code, not the model, expands each cited claim back to its passages and renders the references:

```
def render_draft_payload(term, data, claims, passages, registry, ...):
    """The model cites *claims*; this expands each claim to the passages
    behind it and renders the refs. Quotations therefore enter the article
    only from extract.json, never from the drafting model — which is what
    keeps the character-for-character gate meaningful under claims-only
    drafting."""
```

Voice follows claim type: a consensus claim may sit in the encyclopedia's neutral voice; everything below consensus — majority-with-dissent, school-position, single-commentator — receives mandatory in-text attribution naming the commentator or school. An optional stylistic polish pass is structurally fenced: its output is rejected by a code diff if any citations array, heading order, or paragraph count changed — "the stylist is never trusted with structure; that check is code, not prompt." The audit stage then reads the draft back sentence-by-sentence against the claims table, with six finding categories (added-fact, dropped-qualifier, terminology-drift, attribution-loss, wrong-claim, meaning-shift). Two categories block in code regardless of the model's verdict:

```
AUDIT_BLOCKING = frozenset({"added-fact", "attribution-loss"})
# "Belt and braces on purpose — a model that lists an added fact and
#  still says 'publish' is overruled by its own finding."
```

A real blocking finding from the pilot's audit rounds:

> ⛔ **dropped-qualifier** — The draft changes "three different scholars" (མཁས་པ་མི་འདྲ་བ་གསུམ་) to "many different scholars" (མཁས་པ་མི་འདྲ་བ་མང་པོ་), exaggerating the consensus.

**Route B: articles from consolidated pages.** A second skill turns one consolidated topic page into a full article — the route behind the three per-homage articles drafted so far. The consolidated page supplies the facts; the raw claims files supply the verbatim Tibetan and the block citations; parametric knowledge supplies nothing: "no dates, Sanskrit forms, iconographic details, or doctrinal framings that are not in a claim, however standard they seem — if it cannot be cited, it does not go in." The resolution chain is fixed (consolidated attestation → raw claim → Tibetan text + block citation); an attestation that does not resolve is dropped and logged under "Unresolvable attestations," never guessed. Section headings are a menu, not a quota — a section is emitted only when the page attests material for it; due weight follows attestation counts (consensus forms the unattributed backbone, cited to two to four representative commentaries; divergences present every position with attribution, never adjudicated). The lead of the second homage's article, as drafted:

```
'''བློ་གཏེར་དབྱངས་ཅན་མ་'''ནི་ སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་གཉིས་པའི་
ཕྱག་འཚལ་ཏེ<ref name="taranatha">ཏཱ་ར་ནཱ་ཐ། ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་
རྣམ་པར་བཤད་པ།</ref>…, རྩ་བའི་ཚིགས་བཅད་ལས་ "ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། །
གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །…" ཞེས་གསུངས་པ་ལྟར…
```

Each article ships with a citation-trail file: a reference map (named ref → commentary → claim IDs → verbatim quoted Tibetan → source blocks — the full provenance chain of every footnote in one table), unresolvable attestations, warnings, and a per-quotation verification table (13/13 and 8/8 quotation checks passed on the two articles carrying trails; the first article's trail is missing — a recorded defect).

### 5.12 The deterministic verification gate

Last in the chain, blocking, and LLM-free. The quotation checker's documentation states the tiering, and the tiering *is* the policy:

> Three tiers, deliberately unequal. **exact** — the quote is a substring of the source: a pass. **collapsed** — a substring once whitespace is removed from both: a pass; line wrapping is not part of the text. **fuzzy** — a substring once shads, tshegs, head marks and markup are also removed: **not** a pass; the letters agree but the punctuation does not, which means the article is not quoting what the file says. **missing** — a failure. Reporting a fuzzy hit as success would quietly reintroduce exactly the class of error this gate exists to catch, so *found* is not the gate: *passed* is.

The comparison runs through a **reading view** — the source file with every layer ingest added (block IDs, transclusion lines, inserted headings, wikilink wrappers) stripped back off, "not one Tibetan character touched," line structure preserved so offsets still land — because a faithful quotation spanning a block boundary must never fail on a caret the pipeline itself wrote. Independently, every block locator is resolved: the quotation must also appear inside the specific block its citation names.

A twelve-rule wikitext validator enforces the output contract, from citation resolution to script purity, including two rules idiosyncratic to the target wiki and learned from live renders: the local reference-list template injects its own heading, so the pipeline always emits the sources heading with a bare references tag (the idiom that is correct on English Wikipedia is exactly the one a model reaches for, and the validator makes the mistake impossible); and a tsheg must survive every bold and wikilink boundary — a Tibetan spelling error that the wiki software itself will never surface, visible only to the linter. The validator's rules are not hypothetical: of 677 sampled articles on the target wiki, 15% are raw model dumps with no markup at all, 75% have no citations, and about 126 carry reference tags with nothing to display them.

The strictness has a corollary adopted deliberately: articles are *sic-faithful* to the ingested edition. In an earlier session the gate caught a model silently promoting a tsheg to a shad inside a quotation — string similarity 0.974, invisible to a human skimming Tibetan prose, and exactly the class of drift that makes a quotation no longer a quotation. A transcription error in the source is reproduced in the quotation, never silently repaired; textual correction is an editorial act for the source layer — correct the edition, re-ingest, re-verify — never a liberty of the drafting model. There is no bypass flag, and an audit "publish" verdict does not skip the gate.

### 5.13 Publication path

Nothing writes to the live wiki without an explicit --execute; dry-run is the default on the MediaWiki client and on every publish path — a dry run plans the edit, writes a report, and touches nothing. Publication refuses any article whose ledger state is not *verified* (the create path runs pending → extracted → claimed → organized → drafted → audited → verified → approved → published), runs a pre-publication review checklist (every reference resolves; no sub-consensus position sits in the neutral voice; no sentence draws a conclusion that requires combining sources; the topic's independent-secondary-source case is restated), targets a userspace sandbox before mainspace, and carries an edit summary disclosing pipeline assistance — the Content Translation disclosure model, adopted voluntarily. Throughput is bounded by review capacity, not model capacity: paced publication, no mass creation.

Community consent precedes content. The target wiki has no local policy on machine-assisted content, and the project reads that vacuum as *stop*, not as permission: before any mainspace edit, the plan of record is a public, bilingual proposal on the community forum — scope, method, named reviewers, an explicit invitation to object — plus an on-wiki project page listing every pipeline-assisted article with its reviewer and sources, and a standing invitation to the wiki's active editors to join as reviewers and raters.

**As of this draft nothing has been published.** The pilot's three articles sit at *verified*, one step short of *approved*, and every citation still lacks a public URL (§7) — an article whose quotations a reader cannot check is the failure mode this pipeline exists to prevent, so the review queue holds until the source registry carries checkable links.

### 5.14 Execution model and provenance

One skill per step; immutable per-stage artifacts (extraction → claims → outline → draft → audit → article + citations + verification report); and, since this run, every artifact overwrite snapshots the prior version into a history folder — added after the run's own audit rounds were found to overwrite one another, an evidence-preservation lesson reported as such. A per-article model record captures model ID, timestamp, and exact prompt version for every stage, including a logged record of every post-audit edit — so any published sentence traces to the model and prompt that produced it. Prompt changes follow a fixed discipline: a shipped prompt version is never rewritten in place; the canonical pipeline document is patched first, then the skill, then a *new* version file.

The models behind the reported runs are stated plainly (Table 8, §8): pilot drafting, extraction, and claims ran on claude-sonnet-5 (via the project's stand-in route in a sandboxed environment); the cross-model audit ran on gemini-3.5-flash, with the same-model comparison run deliberately. The library is model-agnostic; the model asymmetry in Tibetan is reported as a finding (§8), not a design choice. One provenance gap is noted rather than hidden: the rails-side artifacts (trees, claims, consolidations) record method and date in their metadata, but per-stage model IDs are uniformly logged only in the article chain — closing that gap is scheduled work. The verification gate needs no API key and no network.

## 6. Editorial doctrine: breadth and reception

Which concepts deserve articles, and how much voice each position gets inside an article, are editorial questions. The pipeline operationalizes both from the corpus itself.

**Breadth decides existence.** A term explained across many commentaries is encyclopedic; a term one commentator happens to use is not. Terms are proposed statistically (frequency and distribution across the sixteen commentaries) and carry that provenance in the term registry; the pilot's three terms are explained by 5, 16, and 10 distinct commentaries respectively. But breadth is an editorial salience signal *within the corpus*; it is not notability in Wikipedia's sense. A term all sixteen commentaries explain may still lack the independent secondary coverage a standalone article needs, so existence is double-gated: corpus breadth proposes, and the publication layer disposes — no article is created without at least one independent, reliable, secondary source identified for its topic, with the human curator making the call.

**Reception decides weight.** Tibetan scholastic culture left a machine-readable reception record: commentaries quote, endorse, and — crucially — refute one another. The refutation-and-response (dgag lan) pattern is a due-weight signal: a position that drew rebuttals from rival colleges has demonstrated historical weight even where it lacks breadth; an idiosyncrasy nobody engaged gets a sentence. Every claim row carries a reception field alongside its school tag, and the outline stage weights sections by breadth adjusted by reception. The normalization rule matters in a skewed corpus: when a school has exactly one representative, that commentator's positions are typed *school-position*, never *fringe* — sole representation is a fact about the corpus, not about the tradition.

The case study also shows the honest limit of this doctrine: a praise-commentary corpus generates **no reception-contested claims at all** — zero of 47 in the pilot's claims tables, and no refutation signal anywhere in the 2,975-claim corpus. The genre explains and extols; it does not refute. The reception machinery is therefore demonstrated structurally here, not adversarially; the *Bodhicaryāvatāra* corpus already aligned behind this pipeline (7,279 spans across ten commentaries, including the textbook refutation exchanges) is where the weighting doctrine will be demonstrated at full strength. Claiming the demonstration from this genre would be overclaiming; we state the mechanism, the distribution it produced here, and where the contested case will come from.

The larger point is that the pipeline treats traditional Tibetan intellectual history — its citation practices, its polemical literature, its school structure — as *editorial policy*, executable and auditable.

## 7. Publication and data model

Publication is where small-wiki damage happens, so the path is deliberately narrow (§5.13). The data model beneath it routes by copyright.

**Cite, don't copy.** None of the canonical Tibetan source repositories licenses its text for the CC BY-SA reuse Wikipedia requires, so the pipeline generates original Tibetan prose over cited facts — facts are not copyrightable — and never translates, closely paraphrases, or excerpts source text into articles. What look like quotations in an article are renderer-inserted passages from the extraction record, each one character-verified (§5.12), kept within short attributed quotation. We state the limit as plainly as the strength: a claims table is still a paraphrase of its sources, so close paraphrase remains possible in principle; the audit reads for it, the pre-publication review checks it, and the human reviewer owns the final judgment.

**Copyright routing.** The source registry carries author dates and a copyright status per text: public-domain texts queue for Tibetan Wikisource with per-verse anchors, so a citation can deep-link to the passage; in-copyright texts cite to library catalogue entries. The honest current state: **every citation the pipeline has produced from this corpus is still unlinked** — the registry's only URLs are cloud-drive scans, which the citation resolver correctly refuses. This is a property of the registry, not of any one run; generating more articles does not improve it. Until the registry carries public URLs, these articles are research artifacts in a review queue, not published pages.

**The claims database as a dataset.** Every article leaves behind its by-product regardless: 2,975 claims over sixteen commentaries — each row carrying verbatim Tibetan, an English gloss, a type from a twelve-value vocabulary, a referent with attestation basis, and a block-level source citation — plus sixteen spine maps and twenty-four consolidated topic pages (Table 5). Release intent is stated with the open licensing question named honestly: the *facts* are free, but rows quote in-copyright commentaries verbatim, so the released form may need quote-truncated variants for some sources **[decision pending]**.

*Table 5. The claims database (all files status: draft, pending domain-specialist review).*

| Commentary | Claims | Commentary | Claims |
|---|---|---|---|
| taranatha | 368 | gendun-drub | 131 |
| tsultrim-namdak | 329 | sangye-nyentrul | 125 |
| tenzin-dhonzang | 327 | pema-namgyal | 104 |
| palden-sherab | 282 | lobsang-dawa | 87 |
| anon-trinle-char | 258 | gendun-gyatso | 62 |
| karma-maitri | 163 | **Total claims** | **2,975** |
| sungrab-tulku | 160 | Spine maps | 16 |
| tenga-tulku | 157 | Consolidated topic pages | 24 |
| anon-utpala | 148 | Drafted articles (two routes) | 3 + 3 |
| drakpa-gyaltsen | 142 | Konchok-thabkhe claims | 132 |

## 8. Evaluation

Evaluation is organised to answer RQ1–RQ3 in order, and it keeps three verification kinds strictly separate throughout: **fidelity** (is the quoted evidence real and correctly located — deterministic, measured), **support** (does the cited passage warrant the sentence — audit plus human judgment), and **notability** (should the article exist at all — human, policy-bound). Properties that hold *by construction* are separated from *empirical* ones, and every empirical cell that awaits team data is boxed **[TO FILL]**.

**RQ1 — citation fidelity (measured; the strongest form).** Across the pilot's three articles the deterministic gate re-read every quotation from its cited source file: **81 of 81 character-for-character exact; 81 of 81 block locators resolve to the named block, none wrong.** The result is reproducible in the strict sense: the corpus was rebuilt from the raw upload on a second machine and the verification reports came back byte-identical. On the second drafting route, the per-quotation verification tables show 13/13 and 8/8 passes on the two articles carrying citation trails. This measures a different thing than the statement-support rates reported for English-language systems — WikiCrow's 86.1% citation precision is a rater's judgment that a source supports a statement; ours is character-level identity of the quoted evidence. Fidelity, not support: the gate proves the quoted evidence is real and correctly located, never that it warrants the sentence citing it. The support judgment is the audit's job plus the pending human legs; no NLI model supports Tibetan, so it is manual by necessity.

**RQ2 — layered verification (measured; the run's most important finding).** The pilot's drafts were audited twice. The same-model audit returned "publish, no findings," three for three. The cross-model audit found **five blocking findings on two of the three articles**; manual adjudication against the claims tables confirmed four genuine and one borderline (Table 6). Six surgical edits later — each logged in the article's model record, with a code assertion that no citation array changed — the cross-model audit returns publish with zero findings on all three, and the deterministic gate still passes.

*Table 6. Cross-model audit findings and manual adjudication (pilot).*

| # | Article | Finding | Adjudication |
|---|---|---|---|
| 1 | སྒྲོལ་མ | lead says "many scholars agree" where claim 0 says **three** (མཁས་པ་མི་འདྲ་བ་གསུམ) | genuine — consensus exaggeration |
| 2 | སྒྲོལ་མ | "and none dispute it" asserted beyond the claim text | borderline — claim metadata says uncontested, claim text does not; tightened anyway |
| 3 | སྒྲོལ་མ | "a name for *each* verse" where claims support verses 2, 11, 17 only | genuine — overgeneralization |
| 4 | སྡུག་བསྔལ | lead said མཚན་ཉིད (defining characteristic) where claim 0 concerns མཚན་དོན (meaning of the name) | genuine — technical-term shift |
| 5 | སྡུག་བསྔལ | names Gendün Drub where the claim deliberately says "one commentary" | genuine in principle — right by luck; exactly the class that must block |

Two further observations belong in any honest report. The auditor shows round-to-round variance — re-auditing the fixed articles three times each gave pass rates of 0.67, 0.67, and 1.0, the dissenting runs each raising a single borderline finding — which is why audit outcomes are reported as pass rates over repeated runs, never single verdicts. And twice the auditor *misquoted the draft inside its own finding*, inventing typos the draft does not contain — model-written finding text is itself untrusted, which is why the blocking decision keys on categories and why the deterministic gate, which cannot hallucinate, sits beneath the audit. The two layers catch disjoint failure classes: the audit reads meaning; the gate reads characters. On sample size we are strict with ourselves: three articles and four audit rounds are an existence proof, not a rate estimate — enough for the design lesson (**never report a same-model audit as independent**), not enough to claim cross-model auditing dominates in general.

**RQ2, rails side — the consolidation audit (measured).** Every one of 418 unique citations across three consolidated topic pages was re-checked by a fresh context: **zero fabricated claim IDs; 1 critical, 1 moderate, ~16 minor findings** (§5.10) — a taxonomy converted wholesale into eight executable rules and two standing gates, with the deterministic gate subsequently reproducing every mechanical finding of the human audit plus one it had missed. Attribution integrity in the pilot articles: of 34 sub-consensus claims, attribution survived on all but the two cases in Table 6, both caught before publication; zero attribution errors remain in the verified articles.

**Per-stage instrumentation (measured).** A stage-evaluation harness measures each step against what the previous step offered it, and it localizes the pipeline's weakness precisely: **extraction capture.** Alignment offered 18k, 41k, and 165k characters of commentary for the three pilot terms; extraction captured 45%, 19%, and **1.1%** respectively — the model visibly budgets its answer against the size of the question. Measured directly: asked about སྒྲོལ་མ with 93,000 characters of context in one call, the extraction model returned ten passages totalling 873 characters; the same model on the same prompt with 12,000 characters returned twenty passages totalling 5,224. The fix is architectural, not rhetorical — batch the question smaller (a 25,000-character batching constant) rather than shout louder in the prompt. Everything downstream of extraction is tight: 100% of extracted quotes character-exact at extract time, 100% of passages used by at least one claim, zero claims dropped at parse, 100% of claims placed by the outline and cited in the draft, and every paragraph carrying at least one citation.

**Pipeline statistics (pilot, on disk).** Three articles, generated end-to-end in roughly 10–20 wall-clock minutes each: 81 extracted passages → 47 atomic claims (13 consensus / 13 school-position / 21 single-commentator / 0 majority-with-dissent) → 81 rendered citations; 5, 16, and 10 distinct commentaries cited per article; all 16 commentaries cited at least once across the three. Article lengths 642–1,358 syllables — all below the 1,500 target, a known extraction-volume limitation under active tuning, reported as such.

*Table 7. Pilot term articles (2 August 2026 run, reviewed).*

| Term | Passages | Claims | Citations | Distinct sources | Cross-model audit (final) | Deterministic gate |
|---|---|---|---|---|---|---|
| སྒྲོལ་མ | 18 | 13 | 18 | 5 | publish, 0 findings | PASS |
| འཇིག་རྟེན་གསུམ | 34 | 19 | 34 | 16 | publish, 0 findings | PASS |
| སྡུག་བསྔལ | 29 | 15 | 29 | 10 | publish, 0 findings | PASS |

*Table 8. Models and prompt versions in the reported runs.*

| Stage | Model | Prompt version |
|---|---|---|
| Extraction | claude-sonnet-5 (stand-in route) | 04-extract/v2-block-locators |
| Claims | claude-sonnet-5 | 04b-claims/v1 |
| Outline | claude-sonnet-5 | 05-organize/v2-claims-outline |
| Draft | claude-sonnet-5 | 06-draft/v3-claims-only |
| Polish | not run on a real draft | 06a-polish/v1 |
| Audit | gemini-3.5-flash (cross-model) + claude-sonnet-5 (same-model comparison) | 06b-audit/v1 |
| Verify | no LLM | — |

**Cost and sustainability (measured + projection).** The pilot's machine side: 22 model calls and roughly 435k input / 85k output characters for three articles — approximately **$0.33–1.42 per article** at current flash-tier prices (central estimate ≈ $0.71; roughly 2× on mid-tier rates), in 10–20 wall-clock minutes each. Projected, the machine cost of a 100,000-article encyclopedia is on the order of **$35k–140k (central ≈ $70k)** — one project grant, one-time, on falling prices. That figure prices the marginal article, not the system: building the pipeline and bringing a corpus into it is skilled up-front engineering that amortizes across every article and every corpus, where manual writing has no fixed-cost term to amortize. The scarce input is human review, by design: at an assumed 30–60 reviewer-minutes per article, 100,000 articles is 24–48 person-years of review spread across a community — against roughly 285 years of *writing* at the manual-only baseline rate. That is the §3 arithmetic; the reviewer-minutes assumption is the one number the planned batch must replace **[TO FILL]**.

**Planned legs — designed, not yet run; each boxed.** (i) Corpus-batch distributions over the full candidate term list: gate pass rate, audit pass rate over repeated runs, extraction capture against offer size as a curve, lengths, cost, retry factor **[TO FILL]**. (ii) Native-speaker rating: three named raters drawn from active community editors and Tibetan-studies institutions, a seven-dimension rubric, an AIS-style statement-support audit on a stratified sample (manual by necessity), and pairwise comparison against existing stubs **[TO FILL]**. (iii) Reviewer-minutes with a from-scratch writing-time control by the same editors — the RQ3 number **[TO FILL]**. (iv) A **zero-shot baseline ablation**: the same three terms drafted by the same model with no pipeline — no claims table, no gate — audited identically; the cheapest honest way to quantify what the machinery buys **[TO FILL]**. (v) A **guardrail before/after**: both consolidation gates re-run over all 24 current topic pages, reported against the 418-citation pre-guardrail taxonomy **[TO FILL]**. (vi) A **claims-quality sample audit**: the deterministic check proves the Tibetan is verbatim, but English glosses, claim types, and referent tags are model judgments with no direct human validation yet — a sampled human audit is the missing leg, and the paper says so.

**Community reception.** Nothing has been published to the live wiki yet — the review gate and the citation-URL debt come first. This is deliberate sequencing; the paper prefers a smaller honest table to a larger premature one.

## 9. Discussion

**Ethics.** The doom-spiral evidence (§2) is about *unaccountable volume*: content nobody fluent verified, at rates nobody could review, with no disclosure. Every design choice in this pipeline is the negation of one of those properties — a named human publisher, throughput bounded by review, on-wiki disclosure, verification that is deterministic where possible and adversarial (cross-model, fresh-context) where not, and an audit trail from every published sentence back through claims to block-located passages. We state the residual risk plainly: a fluent reviewer can still wave through a subtly wrong article; the pipeline reduces the surface a reviewer must distrust — quotations are machine-guaranteed, judgment calls are flagged and typed — it does not abolish editorial responsibility, and is not meant to.

**Limitations.** The corpus is sectarian-skewed (seven of sixteen commentaries from one school; three unattributed), and the weighting doctrine can only normalize what the registry records. The case-study genre yields no contested claims, so the reception machinery is demonstrated structurally, not adversarially. OCR quality upstream bounds everything — and the gate makes articles *sic*-faithful to whatever the ingested edition says, so textual correction is a curatorial prerequisite, not something the pipeline improvises. The model asymmetry in Tibetan is real and measured (§8's extraction-capture cliff), and both drafting and auditing in Tibetan currently ride on models trained mostly on other languages — the cyclical argument of §1, felt from inside the pipeline. The artifacts record their own defects, and we repeat them here rather than hide them: the corpus exists in two annotated copies pending unification; the three consolidated-page articles were drafted from pages still marked draft, with the responsible human accepting that risk explicitly; one article's citation trail is missing; one structural tree's line pointers drifted after a post-QC re-stamp and are flagged for follow-up; the two superseded claims-extraction methods have no surviving outputs on disk, so that comparison is documented but not re-runnable; claim-level judgments (glosses, types, referent tags) are not yet human-validated; and article lengths sit below the stub threshold pending the extraction tuning pass. Evaluation's human legs are pending, so every claim that depends on human judgment rests on a small annotated subset by design — scaling the machine does not scale the reviewing, which is the paper's own thesis turned on its evaluation.

**Generalization.** Nothing in the architecture is specific to this text: it requires a root text, commentaries, and a curated registry. The same machinery is already aligned over the *Bodhicaryāvatāra* (ten commentaries, 7,279 spans), and the pattern — layered canon, commentarial tradition, school structure — is the shape of Sanskrit, Pali, and classical Chinese scholasticism too. For under-resourced languages generally, the transferable design is §3's third option: machine volume, human authority, verification as the hinge — with the claims database, not the article count, as the durable asset.

## 10. Conclusion

The cycle this paper set out to enter — articles → digital footprint → training data → better tools → faster articles — is running today in the wrong direction for Tibetan: absence begetting absence, and, on other small wikis, machine junk begetting model junk. We have shown a working pipeline built to flip that sign, at full methods depth: a cleaning layer that touches nothing it cannot name; normalisation as comparison keys over an untouched corpus; segmentation behind a no-loss assertion; structure extracted in isolated passes and gated by two deterministic checkers; claims extracted node-by-node under five measured guards; routing separated from interpretation; questions generated rather than authored; consolidation audited twice — once by script, once by an adversarial fresh context; articles drafted from claims alone; a character-exact gate no model verdict can waive; and a human hand on the only switch that publishes. The per-article artifacts are small; the machine they came from is not: a reusable editorial system whose every safeguard is a testable invariant, and a growing claims database over the commentarial tradition — 2,975 typed, school-tagged, block-located rows and counting — that is a research object for Tibetan studies regardless of what Wikipedia becomes. The gap named in the opening is real and cyclical; the answer, on this evidence, is neither refusal nor flood, but verification with a human hand on the gate.

## Reproducibility and availability

The pipeline code, versioned prompts (each with provenance metadata recording what it derives from and why it changed), the wikitext validator, and the verification reports are maintained in the project repository; the corpus rebuild is scripted, and was reproduced byte-identically on a second machine as part of the reported review. The claims database, spine maps, and consolidated topic pages are release candidates pending one licensing decision: rows quote in-copyright commentaries verbatim, so the released form may carry quote-truncated variants for those sources (§7). Per-article model records document the exact model and prompt version behind every stage of the reported runs.

## Ethics statement

This work generates encyclopedic content for a small-language Wikipedia — a setting where machine-generated content has caused documented harm (§2). The design responds point-by-point: no autonomous publication (a human is the publisher, not a reviewer of last resort); throughput bounded by human review capacity; on-wiki disclosure of machine assistance planned for every article; community consultation before any mainspace edit, with the absence of local policy read as prohibition rather than permission; and verification that is deterministic wherever character-level checking suffices, adversarial where judgment is required. Sources are cited, never copied: no source text is republished beyond short attributed quotation, and copyright status routes every citation. The authors disclose the use of large language models both inside the pipeline (as reported throughout) and as drafting assistance in preparing this manuscript; all claims about artifacts were verified against the artifacts themselves.

## References — to be finalized against the project bibliography

- FutureHouse. 2024. WikiCrow: automated synthesis of cited Wikipedia-style articles for human genes. Project report.
- Kornai, A. 2013. Digital language death. PLoS ONE 8(10).
- Khanna, S. & Li, W. 2025. Invisible giants: under-represented mid-size languages on the web. Survey.
- MIT Technology Review. September 2025. Machine translation is flooding small-language Wikipedias.
- Nekoto, W. et al. 2020. Participatory research for low-resourced machine translation (Masakhane). Findings of EMNLP.
- Petrov, A., La Malfa, E., Torr, P., & Bibi, A. 2023. Language model tokenizers introduce unfairness between languages. NeurIPS.
- Semnani, S. et al. 2023. WikiChat: stopping the hallucination of large language model chatbots by few-shot grounding on Wikipedia. Findings of EMNLP.
- Shao, Y. et al. 2024. Assisting in writing Wikipedia-like articles from scratch with large language models (STORM). NAACL.
- Shumailov, I. et al. 2024. AI models collapse when trained on recursively generated data. Nature 631.
- Skarlinski, M. et al. 2024. Language agents achieve superhuman synthesis of scientific knowledge (PaperQA2). Preprint.
- Taunk, D. et al. 2023. XWikiGen: cross-lingual summarization for encyclopedic text generation in low-resource languages. WWW.
- Thompson, B. et al. 2024. A shocking amount of the web is machine translated: insights from multi-way parallelism. Findings of ACL.
- TLUE: a Tibetan language understanding evaluation benchmark. EMNLP 2025.
- Wikimedia Foundation. 2024. Language coverage and model performance (Language Ranker); Glot500 (ImaniGooghari et al. 2023, ACL).
- English Wikipedia. 2025. Criterion G15: LLM-generated pages without human review. Policy page.
- Dzongkha Wikipedia Education Program. Program report.
