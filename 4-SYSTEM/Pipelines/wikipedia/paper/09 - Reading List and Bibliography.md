# Reading List and Bibliography

All sources verified 2026-07-24 unless noted. Organized by paper section. ★ = read in full before writing; others are cite-and-skim.

## Systems (related work core)

- ★ **STORM** — Shao, Jiang, Kanell, Xu, Khattab, Lam. "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models." NAACL 2024. https://aclanthology.org/2024.naacl-long.347/ · https://arxiv.org/abs/2402.14207 · code: https://github.com/stanford-oval/storm · demo: https://storm.genie.stanford.edu
- ★ **Co-STORM** — Jiang, Shao, Ma, Semnani, Lam. "Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations." EMNLP 2024. https://aclanthology.org/2024.emnlp-main.554.pdf · https://arxiv.org/abs/2408.15232
- **WikiChat** — Semnani, Yao, Zhang, Lam. Findings of EMNLP 2023. (v2.1 Apr 2025: 25 languages, no Tibetan.) https://aclanthology.org/2023.findings-emnlp.157/ · https://github.com/stanford-oval/WikiChat
- ★ **WikiCrow / PaperQA2** — FutureHouse. "Language agents achieve superhuman synthesis of scientific knowledge." https://arxiv.org/abs/2409.13740 · https://www.futurehouse.org/research-announcements/wikicrow · Signpost review: https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2024-09-26/Recent_research
  - Numbers: 15,616 gene articles, ~8 min each; 2023 demo: 9% incorrect statements; 2024 eval: citation precision 86.1% vs 71.2% (human), cited-but-unsupported 13.5% vs 24.9%, uncited 3.5% vs 13.6%.
- **WikiAutoGen** — ICCV 2025 (multimodal). https://arxiv.org/html/2503.19065v2
- **WINELL** — UIUC Blender Lab (article updating). https://blender.cs.illinois.edu/paper/winell.pdf
- **XWikiGen** — Taunk et al., WWW 2023 (cross-lingual low-resource Wikipedia generation). https://dl.acm.org/doi/10.1145/3543507.3583405
- **OutlineGen** — Subramanian et al., ASONAM 2024 (outline generation, 10 languages). https://link.springer.com/chapter/10.1007/978-3-031-78538-2_13
- **Citation-needed detection, 18 languages** — Quaremba et al., 2026. https://arxiv.org/abs/2605.31136

## Evaluation methodology

- **ALCE** (citation recall/precision) — Gao et al., EMNLP 2023. https://aclanthology.org/2023.emnlp-main.398/ · https://github.com/princeton-nlp/ALCE
- **FActScore** (atomic facts) — Min et al., EMNLP 2023. https://aclanthology.org/2023.emnlp-main.741/
- **AIS** (human attribution protocol) — Rashkin et al., Computational Linguistics 49(4), 2023. https://aclanthology.org/2023.cl-4.2/
- **ExpertQA** — Malaviya et al., NAACL 2024. https://aclanthology.org/2024.naacl-long.167/
- **SAFE/LongFact** — Wei et al., NeurIPS 2024. https://arxiv.org/pdf/2403.18802
- **Human-eval best practices** — van der Lee et al., INLG 2019. https://aclanthology.org/W19-8643/
- **Best-worst scaling** — Kiritchenko & Mohammad, ACL 2017. https://aclanthology.org/P17-2074/
- **HTER** — Snover et al., AMTA 2006. https://aclanthology.org/2006.amta-papers.25/
- **DivEMT** (post-editing effort across languages) — https://arxiv.org/pdf/2205.12215 · NMT productivity +36%: https://www.frontiersin.org/journals/digital-humanities/articles/10.3389/fdigh.2018.00009/full
- **Wikimedia language-agnostic quality model** (works for bo) — https://meta.wikimedia.org/wiki/Machine_learning_models/Proposed/Language-agnostic_Wikipedia_article_quality · Lift Wing API: https://api.wikimedia.org/wiki/Lift_Wing_API/Reference · ORES gap: https://www.mediawiki.org/wiki/ORES/Support_table
- **WP:Good Article criteria** — https://en.wikipedia.org/wiki/Wikipedia:Good_article_criteria
- **FLORES-200 incl. `bod_Tibt`** — https://github.com/facebookresearch/flores/blob/main/flores200/README.md · chrF for extreme-LR MT: (comparative study, ResearchGate 400970950)
- **COMET unusable for Tibetan** (XLM-R/CC-100 exclude it) — https://data.statmt.org/cc-100/

## Wikipedia policy & governance (names/dates verified on-wiki)

- **Guideline:** Wikipedia:Writing articles with large language models (content guideline; amendments RfC closed 2026-03-20, 44–2, WP:SNOW). https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models
- **Info page:** Wikipedia:Large language models (not policy). https://en.wikipedia.org/wiki/Wikipedia:Large_language_models
- **CSD G15** (RfC closed 2025-07-21; adopted 2025-08-04). https://en.wikipedia.org/wiki/Wikipedia:Criteria_for_speedy_deletion
- **WikiProject AI Cleanup** + "Signs of AI writing." https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup
- **WP:MASSCREATE / ArbCom article-creation-at-scale** — https://en.wikipedia.org/wiki/Wikipedia:Bot_policy · https://en.wikipedia.org/wiki/Wikipedia:Arbitration_Committee/Requests_for_comment/Article_creation_at_scale
- **Per-project AI policies inventory** (bo absent) — https://meta.wikimedia.org/wiki/Artificial_intelligence/Policies_by_project
- **Global bot policy** (bo adopted 2011) — https://meta.wikimedia.org/wiki/Bot_policy
- **WMF AI strategy, Apr 2025** — https://wikimediafoundation.org/news/2025/04/30/our-new-ai-strategy-puts-wikipedias-humans-first/
- **AI summaries pause, Jun 2025** — https://www.404media.co/wikipedia-pauses-ai-generated-summaries-after-editor-backlash/
- **Governance history paper** — "Failed comprehensiveness, successful minimalism…" AI & SOCIETY 2026. https://link.springer.com/article/10.1007/s00146-026-03046-1
- **Verifiability** — https://en.wikipedia.org/wiki/Wikipedia:Verifiability

## Cautionary precedents

- **Scots Wikipedia** — https://en.wikipedia.org/wiki/Scots_Wikipedia · https://slate.com/technology/2020/09/scots-wikipedia-language-american-teenager.html
- **Lsjbot/Cebuano** — https://en.wikipedia.org/wiki/Lsjbot · closure proposals: https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Cebuano_Wikipedia
- **Greenlandic Wikipedia closed (2025)** — https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Greenlandic_Wikipedia
- ★ **MIT Tech Review "doom spiral" (2025-09-25)** — https://www.technologyreview.com/2025/09/25/1124005/ai-wikipedia-vulnerable-languages-doom-spiral/
- **en-wiki MT purge (2016) / X2** — https://en.wikipedia.org/wiki/Wikipedia:Content_translation_tool
- **Indonesian 95% threshold** — https://phabricator.wikimedia.org/T219851
- **Thompson et al. 2024** (MT-polluted low-resource web) — https://aclanthology.org/2024.findings-acl.103/
- **Shumailov et al. 2024** (model collapse, Nature) — https://www.nature.com/articles/s41586-024-07566-y · nuance: https://arxiv.org/abs/2410.12954
- **Brooks et al. 2024** (>5% of new en-wiki articles AI-flagged) — https://aclanthology.org/2024.wikinlp-1.12/

## Low-resource precedents

- ★ **Welsh Government Wikipedia strategy (2017)** — https://digitalanddata.blog.gov.wales/2017/08/07/using-technology-to-promote-welsh-language-wikipedia/ · NLW "responsible AI content" project: https://www.library.wales/news/article/developing-responsible-approaches-to-ai-generated-content-in-the-welsh-language · Wici-Iechyd: https://wikimedia.org.uk/2018/02/3000-new-articles-added-to-the-welsh-wicipedia/
- ★ **Masakhane / Nekoto et al.** Findings-EMNLP 2020 — https://aclanthology.org/2020.findings-emnlp.195/
- **Content Translation 2.4M+ articles, lower deletion rates** — https://diff.wikimedia.org/2025/05/08/a-decade-of-consistent-improvements-to-the-content-translation-tool-yields-over-two-million-wikipedia-articles/
- **MinT** — https://www.mediawiki.org/wiki/MinT · Tibetan enabled via NLLB-200 (T326578/T337290, Jun 2023): https://phabricator.wikimedia.org/T326578
- **NLLB-200** — https://ai.meta.com/research/no-language-left-behind/
- ★ **Dzongkha Wikipedia Education Program** (Diff, 2026-01-31) — https://diff.wikimedia.org/2026/01/31/where-knowledge-fuels-gross-national-happiness-dzongkha-wikipedia-education-program-in-bhutan/
- **Basque** — https://meta.wikimedia.org/wiki/Basque_Wikimedians_User_Group/Strategy/2024-2027 · **Catalan AINA** — https://www.bsc.es/news/bsc-news/aina-born-the-project-will-guarantee-the-survival-the-catalan-language-the-digital-age · **Iceland × OpenAI** — https://openai.com/index/government-of-iceland/
- **AI4Bharat Sangraha (Wikipedia-derived synthetic Indic data)** — https://github.com/AI4Bharat/IndicLLMSuite

## Digital-divide framing

- ★ **Joshi et al. 2020** "State and Fate…" ACL 2020 — https://aclanthology.org/2020.acl-main.560/
- ★ **Kornai 2013** "Digital Language Death" — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0077056
- **Khanna & Li 2025** "Invisible Languages of the LLM Universe" — https://arxiv.org/abs/2510.11557
- **State of the Internet's Languages** — https://internetlanguages.org/en/
- **Language Ranker** (per-language performance ∝ pretraining share) — https://arxiv.org/abs/2404.11553 · **Glot500** — https://arxiv.org/pdf/2305.12182 · **FineWeb2** (uses botok for Tibetan) — https://arxiv.org/abs/2506.20920
- **WMF: Wikipedia in the age of generative AI** (2023) — https://wikimediafoundation.org/news/2023/07/12/wikipedias-value-in-the-age-of-generative-ai/ · data deals incl. Perplexity: https://www.techspot.com/news/110216-wikipedia-helped-train-favorite-ai-now-wiki-foundation.html

## Tibetan NLP & ecosystem

- ★ **TLUE** (LLMs below random in Tibetan) — https://arxiv.org/abs/2503.12051
- ★ **"Tibetan Language and AI: A Comprehensive Survey"** (2025, 22 authors) — https://arxiv.org/abs/2510.19144
- **Tokenizer unfairness** — Petrov et al., NeurIPS 2023 — https://arxiv.org/abs/2305.15425
- **Sino-Tibetan NLP survey** — NAACL 2025 — https://aclanthology.org/2025.naacl-long.396/
- **TIB-STC / Sun-Shine** — https://arxiv.org/abs/2503.18288 · **TJUNLP 72GB corpus** — https://arxiv.org/abs/2507.09205 · **T-LLaMA** — (DOAJ 2693417246c046dd9201b988300ece81) · **TiBERT** — https://arxiv.org/abs/2205.07303 · **TibetanQA** — https://github.com/CMLI-NLP/TibetanQA
- **botok** — https://github.com/OpenPecha/Botok · **OpenPecha** — https://openpecha.org · https://github.com/OpenPecha-Data
- **BDRC** — https://www.bdrc.io/ · OCR program: https://www.bdrc.io/blog/2024/08/28/transforming-tibetan-text-digitization-bdrcs-groundbreaking-ocr-project/
- **Monlam AI** — https://monlam.ai/ · Melong claims: https://tibetexpress.net/at-2025-monlam-manifest-centre-declares-melong-outperforms-global-ai-in-tibetan/ · Dictionary at Library of Congress: https://www.rfa.org/english/tibet/2024/12/18/tibet-dictionary-library-of-congress/
- **DeepZang** (China's Tibetan LLM, Mar 2026) — https://phayul.com/chinas-first-tibetan-ai-claim-contested-as-dharamshalas-monlam-ai-predates-deepzang/
- **Google Translate added Tibetan (2024-06-27)** — https://blog.google/products/translate/google-translate-new-languages-2024/
- **Tibetan MT near-zero baseline** (zh→bo BLEU 0.046→0.261 with CPT+SFT) — https://arxiv.org/abs/2512.03976
- **bo.wikipedia stats** — https://bo.wikipedia.org/wiki/Special:Statistics · https://www.wikidata.org/wiki/Q2091593

## Sources for citations in generated articles (licensing verified)

- **84000** — text CC BY-NC-ND 4.0; **glossary/metadata CC BY 4.0**. https://84000.co/documents/terms-of-use
- **Lotsawa House** — CC BY-NC 4.0. https://www.lotsawahouse.org/about/
- **Treasury of Lives** — peer-reviewed, 1,500+ biographies; non-commercial full text, **metadata CC0** (verify terms manually — site blocks robots). https://treasuryoflives.org/
- **BDRC access policies** — mixed PD/fair-use. https://www.bdrc.io/access-policies/
- **Wikipedia licensing requirement** (CC BY-SA 4.0) — https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
- NOT citable (open wikis): Rigpa Wiki, Buddha-Nature (Tsadra), Tibetan Buddhist Encyclopedia.
- Tibetan-language news (with 2025 fragility caveat): RFA/VOA Tibetan shutdowns — https://phayul.com/rfa-to-shut-down-tibetan-service-amid-budget-cuts-and-legal-battle/

## Venue & logistics

- **17th IATS Seminar** — 23–29 Aug 2026, The Soaltee Kathmandu (moved from Hyatt/Boudha) — https://www.iats.info/17th-iats-seminar-2026/ · fifth announcement: https://www.iats.info/2026/04/fifth-announcement-17th-iats-seminar/ · ConfTool: https://www.conftool.com/iats2026 · contact: iats2026@conftool.com
- **Nepal connectivity** — median fixed ~78 Mbps (2025); Sept 2025 platform-block precedent: https://pulse.internetsociety.org/en/shutdowns/internet-services-banned-in-nepal-september-2025/
- **API reachability from Nepal** — Anthropic: https://www.anthropic.com/supported-countries · OpenAI: https://developers.openai.com/api/docs/supported-countries
- **Tibetan rendering** — W3C Tibetan layout: https://www.w3.org/TR/tlreq/ · MediaWiki webfonts (Jomolhari default for bo): https://www.mediawiki.org/wiki/Universal_Language_Selector/WebFonts · font bugs: https://digitaltibetan.github.io/DigitalTibetan/docs/tibetan_fonts.html
- **Funding** — Wikimedia Rapid Fund ($500–5k): https://meta.wikimedia.org/wiki/Grants:Project/Rapid · LLM pricing (Jul 2026): https://platform.claude.com/docs/en/about-claude/pricing
