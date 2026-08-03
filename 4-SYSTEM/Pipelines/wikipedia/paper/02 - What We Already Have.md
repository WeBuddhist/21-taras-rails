# What We Already Have — Vault Asset Inventory

Everything below exists on disk in this Obsidian folder (inventoried 2026-07-24). The paper's architecture diagram can be drawn directly from it.

## The end-to-end pipeline exists — as a relay across repos

```
Ingestion                     Context compilation            Term extraction           Article generation
webuddhist-library-           2-RAILS / 2-authoritative-     term-extractor skill      Tibetan local-wiki
data-pipeline                 context (verse packages,       (verbatim + block-ID      articles (2 finished,
(raw text → block-ID'd        term tables, glossaries)       discipline)               2 stubs, 79 English)
citable digital edition)
```

## 1. The core exhibit: the Heart Sutra Tibetan local wiki (`WeBuddhist/Hear Sutra Local Wiki from Wikipedia/`)

Five files that happen to display the pipeline's stages:

| File | State |
|---|---|
| བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ།.md (Bodhisattva Mahāsattva, 14.8 KB) | **Finished article** |
| ཟབ་མོ་སྣང་བ།.md ("Illumination of the Profound" samādhi, 12.4 KB) | **Finished article** |
| སྟོང་པ་ཉིད།.md (Emptiness) | Stub — raw transclusions awaiting drafting |
| མྱ་ངན་ལས་འདས་པ།.md (Nirvāṇa) | Stub |
| Untitled.md | Empty |

**Why the two finished articles are demo-ready:** high-register scholastic Tibetan; encyclopedic structure (lead → etymology → Indian commentators → per-school Tibetan presentations → conclusion → references); genuinely multi-perspectival (Nyingma vs Geluk readings kept distinct and attributed — the Railroad "no consensus flattening" rule visibly operating); three-layer citations (inline attribution to named commentaries, numbered reference list, raw block-transclusion appendix pinning every section to specific commentary passages).

**The honest limitation:** citations are vault-internal block references. For Wikipedia they need one more hop — external identifiers (BDRC, 84000, Treasury of Lives, academic literature) and MediaWiki `<ref>` markup. See [[03 - Pipeline Design]].

**The stubs are a feature for the talk:** they visibly show the intermediate state (raw cited material assembled, prose not yet drafted) — proof this is a pipeline, not hand-writing.

## 2. The machine layer beneath (`WeBuddhist/2-authoritative-context/heart-sutra/`)

- **79 English-analysis term articles** (local-wiki/, generated 2026-04-27), one per Heart Sutra term, uniform template, every paragraph cited to file+block with inline Tibetan quotations.
- **Two term-extraction tables** (~90 KB each): term × commentary matrix — one paraphrase variant, one verbatim-with-block-IDs variant.
- **Verse context package** for verse 1-2 (276 lines): Sanskrit + 4 parallel witnesses (bo, en-84000, zh-Facheng, zh-Xuanzang) + raw passages from 10 commentaries.
- **Word-aligned frequency glossaries** sk→tib/en/zh/hi.

**Scaling story:** extraction and structuring already scale (79 of ~80 terms); Tibetan drafting is demonstrated (2 of ~80). That is the honest sentence for the paper.

## 3. The corpus (`WeBuddhist/1-Human-Sources/`)

Heart Sutra: 16 commentary files (12 Tibetan — Vimalamitra, Praśāstrasena, Vairocana, Atiśa, Śrī Mahājana, Vajrapāṇi, Tāranātha, Rongtön, Ngawang Tendar, and more; 1 English; 2 Chinese) + 5 root versions. Plus 21 Praises to Tārā (4 commentaries), 8 Verses of Mind Training, Bodhicaryāvatāra root, Amitābha Sutra, Diamond Sutra, Abhidhamma, Ti Sarana/Vandana.

## 4. The automation (`webuddhist-term-extractor-updated-SKILL.md`)

A complete Claude skill: reads the vault via Obsidian Local REST API → enumerates commentaries → extracts all significant terms → builds the term × commentary table under the "Golden Rule" (raw extraction only, verbatim, block IDs, typed gap-notes, never an empty cell) → hands off to a wiki-creator skill. **This is abstract claim 4 in operational form.**

> [!danger] Redact before demo/publication
> The skill file contains a **hardcoded API key and LAN host** (line 27). Also the previously-flagged WeBuddhist credentials in the rails plan-uploader. Redact both before showing or publishing anything.

## 5. The methodology writing (`bodhisattvacharyavatara-rails/`)

The most mature Railroad instance — the paper's methods section can be lifted nearly verbatim from its README + 4-SYSTEM/CLAUDE.md: hallucination/consistency/traceability failure modes; the "two specialists" framing; descriptive-rails/prescriptive-transformations; one-way citation chain; block-ID addressing; human-only `status: complete` promotion; protected-file drift guard.

Contents: 112 source files (Sanskrit root, Tibetan root, 8 translations, commentaries); 89 verse packages in 2-RAILS (flagship: `1-1-ref.md` with a Tibetan-language AI Overview with per-bullet citations); 1,630 files in 3-TRANSFORMATIONS including the 365-day Bodhisattva Challenge in four language streams *shipping to the WeBuddhist app* — plus `chapter-eval/` files, an existing evaluation-artifact format to reuse.

## 6. The ingestion pipeline (`webuddhist-library-data-pipeline/`)

The cleanest expression of "semi-automatic": drop raw file in `input/` → `/annotate` (LLM stages: clean → segment → block-ID → TOC → frontmatter, with two human-review checkpoints) → `/upload` (deterministic Python lint → JSON payloads → POST). `ledger.json` gives an auditable `in_progress → annotated → uploaded` trail. Currently processing Dolma21 (21 Praises to Tārā). 13 skills, 9 stage docs, golden-fixture tests.

## 7. Breadth evidence (`abhidhamma-rails/`, `data-pipeline/`)

Same methodology applied to Pāli (Dhammasaṅgaṇī): 22 verse packages, 4 populated local-wiki term articles (the only populated Local-Wiki outside Heart Sutra), 3 translation tracks. Proves the method is text- and language-agnostic — the "model for under-resourced languages" claim (6).

## Gap list (what the 4 weeks must produce)

1. **Volume:** 2 → 10–15 finished Tibetan articles.
2. **External citations:** map vault block-refs to citable identifiers (BDRC IDs, 84000, Treasury of Lives, academic literature). The pipeline spec already has frontmatter fields for these; the articles don't use them yet.
3. **MediaWiki last mile:** wikitext conversion, `<ref>`/citation templates, upload path. Nothing exists yet.
4. **Evaluation:** none exists for the wiki articles (only translation evals in chapter-eval/). Design ready in [[06 - Evaluation Plan]].
5. **On-wiki presence:** zero articles uploaded to bo.wikipedia; village-pump proposal not yet posted. Plan in [[05 - Wikipedia Policy and Community Strategy]].
6. **Credential redaction** (see danger box above).
