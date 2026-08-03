# Related Work and Landscape

All URLs in [[09 - Reading List and Bibliography]]. Verified 2026-07-24.

## 1. LLM → Wikipedia article systems (the paradigm we extend)

| System | What it does | What we borrow | Why it doesn't cover us |
|---|---|---|---|
| **STORM** (Stanford, NAACL 2024) | Perspective-guided question asking + simulated expert conversation → outline → cited article. FreshWiki benchmark; +25% organization vs RAG baseline | The research→outline→draft→cite architecture; the editor-rubric evaluation | English-first stack; positioned as *pre-writing assistance*, no publication path |
| **Co-STORM** (EMNLP 2024) | Human joins the agent discourse; mixed-initiative; dynamic mind map | The human-in-the-loop model: humans *steer*, not just post-edit | English; no low-resource support |
| **WikiChat** (EMNLP 2023; v2.1 Apr 2025) | Generate → keep only facts grounded in retrieved Wikipedia passages; 97%+ factual accuracy | The grounding filter — decouple fluent generation from what sources support | 25 languages, **Tibetan not among them** |
| **WikiCrow / PaperQA2** (FutureHouse 2024) | Auto-generated cited articles for all 15,616 unnamed human genes (~8 min each) | Proof machine drafts can *out-cite* humans (86.1% vs 71.2% citation precision); the citation-audit evaluation | English, biomedical; 9% incorrect statements ⇒ validates mandatory human review |
| **WikiAutoGen** (ICCV 2025), **WINELL** (UIUC) | Multimodal generation; never-ending article updating | Multi-perspective self-reflection idea | English/high-resource |
| **XWikiGen** (WWW 2023), **OutlineGen** (ASONAM 2024) | Cross-lingual Wikipedia section/outline generation for low-resource (mostly Indic) languages | The closest *low-resource* precedents; cite as the pre-LLM lineage | No Tibetan; no citation grounding; no human loop |

**Novelty statement:** no published system does LLM-based, citation-aligned article generation for Tibetan. The contribution is the combination: low-resource Tibetan × retrieval-grounded cited generation × human editorial publication × a living community channel (bo.wikipedia).

**The incumbent inside Wikipedia:** Content Translation + MinT covers Tibetan via NLLB-200 (enabled June 2023) — but Tibetan MT quality is documented near-zero (zh→bo BLEU 0.046 off-the-shelf; chrF ~2). Translation-in ≠ sourced original synthesis. Complementary, not competing.

## 2. Low-resource language precedents (the comparative frame — pick 5)

1. **Welsh** — the killer precedent. Welsh Government policy (2017): grow Wicipedia to make Welsh visible to tech companies — the paper's exact argument, a decade earlier, with results (91k → 280k+ articles; most-viewed Welsh-language website; growth credited with improving Welsh MT). Plus: UK's first permanent National Wikimedian; Wici-Iechyd health-articles project; and currently the National Library of Wales runs a *government-funded "responsible AI content" Wikipedia project* (1,000 Welsh biographies).
2. **Masakhane** (Nekoto et al., EMNLP Findings 2020) — participatory research: speakers as content creators, curators, evaluators. The academic legitimation of OpenPecha's community model.
3. **Content Translation / NLLB / MinT** — machine-assisted, human-reviewed creation scales (2.4M+ articles) and CX articles have *lower* deletion rates than from-scratch ones. The empirical defense of semi-automation. Also the model for the virtuous cycle: corrected translations feed back into open training corpora (OPUS).
4. **Dzongkha Wikipedia Education Program** (Bhutan, Aug–Dec 2025) — the closest Tibetic-script precedent, fully manual: dozens of participants, 5 months → **80 new articles**. The benchmark a semi-automatic pipeline should beat by an order of magnitude on effort-per-article.
5. **Scots Wikipedia / Lsjbot / Greenlandic closure** — the anti-patterns. Scots: one non-speaker, ~23k articles, credibility destroyed. Cebuano: 6M bot stubs, repeated closure proposals. Greenlandic: **closed by LangCom in 2025** over machine-generated content. These motivate every human-in-the-loop design choice.

Supporting cast if space allows: Basque (5,000 students, 10M words), Catalan AINA (€13.5M government corpus project), Iceland (govt + OpenAI GPT-4 partnership — first non-English RLHF partner).

## 3. The Tibetan landscape (audience's home turf — get the numbers right)

- **bo.wikipedia:** 8,072 content articles; 31 active users/month; 2 admins; 0 local media files; ~350 new articles/year since 2020; founded 2008. Tibetan Wiktionary effectively empty; no Tibetan Wikisource subdomain. (China's block of Wikipedia is part of this story.)
- **LLM failure evidence:** TLUE benchmark (EMNLP 2025) — most LLMs below the 25% random baseline in Tibetan; Qwen-2.5-72B 84.7%→16.5%, GPT-4 68.9%→17.5%. Tokenizer unfairness: Tibetan 4×+ byte cost (NeurIPS 2023).
- **But raw text exists:** OpenPecha-Data 9,500+ e-text repos; BDRC OCR program; TIB-STC 11B-token curated corpus; TJUNLP 72 GB corpus; Monlam Melong trained on ~24B tokens. **The data exists but is not encyclopedic or citation-structured — that is precisely the gap the pipeline fills.**
- **Ecosystem/collaborators:** OpenPecha (botok tokenizer, aligner, toolkit), BDRC (catalog authority), Monlam AI (MT/OCR/STT/TTS + Melong LLM + 223-volume dictionary), Esukhia (ACTib corpus). Tibetan-specific LLMs emerging from Chinese universities: T-LLaMA, Sun-Shine, TJUNLP MoE.
- **The political moment (IATS will care):** RFA Tibetan and VOA Tibetan shut down in 2025 (funding cuts; partial resumption later) — independent Tibetan-language information contracted sharply. China launched **DeepZang**, a state-backed "first Tibetan LLM" (March 2026), explicitly ideological; exile media contest the "first" (Monlam predates it). *Who builds digital Tibetan* is a live geopolitical question; a community-governed, citation-grounded Tibetan knowledge base is an answer.

## 4. Evidence for the cyclical claim (footprint → capability → visibility)

- WMF (2023): every LLM has trained on Wikipedia; it is "almost always the largest source of training data."
- LLaMA's mix: ~4.5% Wikipedia. Dolma, The Pile: Wikipedia as core high-quality component. FineWeb2 (1,000+ languages) is the live pipeline from per-language web text to model capability — and it uses OpenPecha's **botok** for Tibetan segmentation.
- Per-language correlation: Language Ranker (2024) — LLM per-language performance strongly correlates with pretraining share; Glot500 r≈.34–.44.
- Commercial visibility: Wikimedia's 2025–26 paid data deals with Microsoft, Meta, Amazon, Mistral **and Perplexity** — the abstract's "visible to Perplexity-class apps" claim, documented.
- Welsh micro-evidence: Wicipedia growth credited with improving Welsh MT.

## 5. The counter-literature (cite it before the audience does)

- Thompson et al. 2024 (ACL Findings): a shocking share of low-resource web text is already multi-way MT junk.
- Shumailov et al. 2024 (Nature): model collapse on recursively generated data (nuance: *replacement*, not accumulation, drives collapse).
- Brooks et al. 2024: >5% of new English Wikipedia articles already AI-flagged, skewing low-quality.
- MIT Tech Review (Sept 2025) "doom spiral": Greenlandic closed; Inuktitut ⅔ MT-contaminated; African wikis 40–60% uncorrected MT.
- Rebuttal assets: CX lower deletion rates; Sangraha Synthetic / TransWebEdu (curated synthetic ≈ real quality). **Curation and human verification flip the sign of the loop** — the paper's thesis ([[01 - Paper Argument and Structure]]).
