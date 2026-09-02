# Paper Argument and Structure

## Thesis (one sentence)

Grounded, citation-first LLM drafting plus mandatory native-speaker editorial review can turn Tibetan's scattered but rich source landscape into durable encyclopedic content — and the sign of the "AI content feedback loop" flips from *doom spiral* to *virtuous cycle* precisely and only under that human gate.

This is stronger than "we built a pipeline": it takes the biggest current objection (MT/AI content is destroying small-language Wikipedias — see the MIT Tech Review "doom spiral" reporting) and makes answering it the paper's central contribution.

## Suggested framing line for related work

> STORM and WikiChat proved the machinery for English; WikiCrow proved it scales to a specialist domain; the open problem — and this paper's contribution — is making that machinery work for a low-resource, non-Latin-script language with human editorial oversight and a direct path to community publication.

## Claim-by-claim evidence map

Each claim in the submitted abstract, with the evidence now in hand (details + URLs in [[09 - Reading List and Bibliography]]):

| # | Abstract claim | Evidence we have | Still needed |
|---|---|---|---|
| 1 | Tibetan underrepresented in NLP / small digital footprint | bo.wikipedia = 8,072 articles vs 7M+ speakers; TLUE: frontier LLMs below random (GPT-4 17.5%); tokenizer cost 4×+ vs Chinese (Petrov et al. 2023); "Invisible Giants" framing (Khanna & Li 2025); Kornai's <5% digital ascent | Nothing — this is fully cited |
| 2 | Semi-automatic pipeline generating cited Tibetan Wikipedia articles | 2 finished Tibetan articles (multi-commentary, block-cited); 79 English term articles; term-extractor skill; ingestion pipeline with ledger | Scale to 10–15 Tibetan articles; convert citations to Wikipedia-ready external refs; MediaWiki output; actual upload |
| 3 | Human-in-the-loop for accuracy/appropriateness/reliability | Architecturally enforced in the vaults: read-only sources, human-only `status: complete`, review checkpoints, divergence flags, bilingual editorial guidelines | Log the review work (time, edits) so oversight is measured, not asserted |
| 4 | Automates extraction, structuring, citation alignment | Term-extractor skill ("raw extraction only, verbatim, with block IDs"); 90 KB term × commentary tables; verse context packages; glossaries | Citation alignment to *external* citable IDs (BDRC, 84000, Treasury of Lives, academic) |
| 5 | Footprint → NLP training data → LLM-app visibility | WMF: every LLM trains on Wikipedia, usually its largest source; LLaMA mix ~4.5% Wikipedia; per-language performance correlates with pretraining share (Language Ranker; Glot500 r≈.34–.44); Wikimedia's paid data deals incl. Perplexity | Nothing — fully citable |
| 6 | Sustainable cyclical model for under-resourced languages | Welsh precedent (gov policy: grow Wikipedia → tech-company support; 91k→280k articles); MinT's corrected-translations-feed-OPUS loop; API cost ≈ $0.12–0.60/article; Wikimedia Rapid Fund $500–5k | Measured reviewer-minutes per article (the real cost); the counter-argument rebuttal (below) |
| 7 | Demo + evaluation of early outputs | Two demo-ready articles; eval design ready | Run the evaluation ([[06 - Evaluation Plan]]); build offline demo ([[08 - Presentation and Demo Plan]]) |

## The counter-argument the paper must answer head-on

**"Your cycle is the doom spiral."** Thompson et al. 2024 showed a shocking share of low-resource web text is already machine-translated junk; Shumailov et al. 2024 (Nature) showed models collapse on recursive synthetic data; MIT Tech Review documented Greenlandic Wikipedia being *closed* and African-language wikis at 40–60% uncorrected MT. The identical mechanism the abstract celebrates.

**The answer (make it the thesis, not a footnote):** the feedback loop's sign depends on verification. Raw MT dumping degrades the corpus; human-verified, citation-audited text upgrades it. Evidence that curation flips the sign: Content Translation articles (machine draft + mandatory human edit) have *lower* deletion rates than from-scratch articles; Sangraha Synthetic and TransWebEdu show curated synthetic data approaches real-data quality. Our pipeline's every design choice (citation audit, native review, bounded throughput) exists to stay on the right side of that line.

## Honest-framing rules (credibility with this audience)

- Say "**machine-drafted, human-published**" — never "AI-generated articles."
- Report what is demonstrated vs what is scaled: extraction/structuring scale today (79 terms); Tibetan article drafting is demonstrated (2 articles), being scaled (target 10–15 by August).
- State what cannot be measured for Tibetan (no COMET/BERTScore, no ORES, no NLI-based citation checking) and use each gap as further evidence of claim 1.
- Quote WikiCrow's numbers precisely — they are two different metrics from two different years: 9% = incorrect-statement rate (Dec 2023 demo); 13.5% = cited-but-unsupported rate in the 2024 PaperQA2 evaluation (vs 24.9% for human Wikipedia articles).

## Proposed paper outline

1. **Introduction — the digital footprint problem.** Kornai's digital language death; Joshi et al.'s resource classes; "Invisible Giants"; the bo.wikipedia numbers; the political moment (RFA/VOA Tibetan shutdowns 2025; China's DeepZang LLM, March 2026 — *who builds digital Tibetan?*).
2. **Related work.** STORM/Co-STORM/WikiChat/WikiCrow; XWikiGen/OutlineGen (low-resource pre-LLM); Content Translation/MinT (the incumbent, weak for Tibetan); Welsh/Basque/Dzongkha precedents; Wikipedia AI governance 2023–2026.
3. **The pipeline.** The Railroad citation chain as the backbone ([[03 - Pipeline Design]]); the five stages; where humans sit; "cite, don't copy" licensing design.
4. **Early outputs.** The Heart Sutra local wiki; walk one term through all stages; the new article batch.
5. **Evaluation.** Small-N design and results ([[06 - Evaluation Plan]]); productivity numbers; comparison anchors (STORM rubric, WikiCrow citation audit, Dzongkha manual baseline: ~80 new articles from a 5-month human-only program).
6. **The cyclical model.** Footprint→capability evidence; the doom-spiral rebuttal; economics (API cost negligible; reviewer-minutes are the currency; Rapid Fund path); community capacity (the 31 editors, the OpenPecha admin, capacity-building à la Dzongkha program).
7. **Implications.** For Tibetan studies (a citable Tibetan reference layer); for digital humanities (the commentary tradition as machine-readable interpretive infrastructure); for computational linguistics (a replicable recipe for Class-0/1 languages).

## Title/positioning note

The abstract is already submitted, so the title stands. In the talk, define "semi-automatic" early and precisely: *the machine does retrieval, structuring, drafting, and citation-candidate alignment; a fluent human holds Wikipedia's burden of verifiability and is the sole publishing agent.*
