# IATS-2026 — Build Plan

**Goal:** one self-contained repo that (a) holds the IATS paper and (b) runs the pipeline. You give it a root text plus commentaries; it aligns them, picks key terms, extracts cited explanatory material, drafts Tibetan Wikipedia articles, and creates-or-updates them on bo.wikipedia — with a human review gate before anything is published. You should never need to open Obsidian.

**Status:** implemented through Phase 4 (see [STATE.md](STATE.md) — this file is the *plan*, kept as designed; STATE.md is what is actually true). Decisions marked ❓ need your answer before the affected behaviour is finalized (see [open-questions.md](docs/reference/open-questions.md)).

**Confirmed decisions (from you, 2026-07-29):** review gate then publish · repo at `~/Desktop/work/IATS-2026`, self-contained · pipeline does its own alignment · Gemini only.

---

## 1. What the research changed

Five research lenses plus an adversarial verification pass ran against live endpoints. Four findings changed the design materially — all are things that would have produced broken output if we had built on assumption.

**1. Your team's prompts were all recovered, verbatim.** The forum is fully public via Discourse's JSON/raw endpoints (`/raw/<topic_id>`, `/t/<id>.json`, `/posts/<id>.json` — no login). All 31 topics in the Wiki WG category are enumerated in [r-forum-prompts.md](research/reports/r-forum-prompts.md). The key ones: **topic 223** (your master 4-stage spec), **289** (key-term extraction, 3 versions), **236** (root–commentary alignment, 3 versions), **260** (article writing, 3 authors), **309** and **324** (citation markup + the flagship worked example on སཏྭ་). One correction to your message: the topic-324 slug is `new-prompt-sample`, not `prompt-sample`.

**2. bo.wikipedia DOES have CS1 citation templates** — `{{Cite book}}`, `{{Cite web}}`, `{{Cite journal}}`, `{{Cite encyclopedia}}`, `{{Reflist}}` and the full 164 KB `Module:Citation/CS1` all exist. I had expected them to be missing. But they emit **English furniture** (`2 ed.`, `pp.`, `Retrieved`) inside Tibetan prose, so we use them only for modern secondary sources with ISBNs, and hand-formatted `<ref>` for Kangyur/Tengyur primaries — which is also what your team's own published articles do.

**3. The `{{Reflist}}` trap — highest-value single finding.** bo.wikipedia's `Template:Reflist` **begins with its own `== ཡོང་ཁུངས། ==` heading**. So the standard English-Wikipedia idiom `== ལུང་ཁུངས། ==` + `{{Reflist}}` renders **two stacked headings**. Verified by rendering it live through `action=parse`. An LLM will produce exactly this broken pattern by default, because it is correct on en.wiki. The emitter must always produce `== ལུང་ཁུངས། ==` + `<references />`, and the linter must reject `{{Reflist}}` preceded by a heading.

**4. About 600 bo.wikipedia articles have orphaned footnotes** — `<ref>` tags with no `<references />` to display them. 1,289 pages have refs; only 682 have a display mechanism. Our articles must not join them; this is one lint rule away.

Also worth knowing: `ལུང་ཁུངས།` is the attested reference heading (738 articles) — your prompts' `དཔེ་ཁུངས།` appears **zero** times on the wiki. Titles fragment three ways (`སངས་རྒྱས་` with tsheg / `སངས་རྒྱས།` with shad / bare, all three exist as separate pages) so the publisher must probe variants before creating. And `google-genai` 2.14.0 is the current SDK with `gemini-3.5-flash` / `gemini-3.6-flash` as the stable model choices — the legacy `generateContent` path, not the new Interactions API, because only it supports explicit caching, batch, and safety settings, all of which we need.

---

## 2. Repo layout

```
IATS-2026/
├── README.md                    quickstart: install, configure, run one term end-to-end
├── CLAUDE.md                    agent entry point (mirrors OpenPecha/data-pipeline)
├── pyproject.toml               uv-managed, python >=3.10
├── .env.example                 GEMINI_API_KEY, WIKI_USERNAME, WIKI_BOT_PASSWORD
│
├── paper/                       the IATS paper (migrated from Obsidian, already here)
│   ├── 00 - START HERE.md … 09 - Reading List
│   ├── draft/                   the paper itself
│   └── slides/
│
├── docs/
│   ├── 00-overview.md           the pipeline story end to end
│   ├── 01-ingest.md … 08-publish.md    one doc per stage
│   └── reference/
│       ├── wikitext-spec.md     ★ canonical output format — everything depends on this
│       ├── citation-spec.md     ★ how a quotation becomes a verifiable <ref>
│       ├── conventions.md       block IDs, segment IDs, file naming
│       └── open-questions.md    decisions needed from you
│
├── prompts/                     one ACTIVE version per stage (finalized 2026-08-02;
│   │                            superseded versions staged in _to_delete/, history in git.
│   │                            Canonical home: docs/reference/cowork-pipeline.md — patch
│   │                            there first, then a NEW version file here)
│   ├── 01-toc/         v1.md                      sa-bcad headings (kwiki commentaries)
│   ├── 04-extract/     v2-block-locators.md       proven on tara21
│   ├── 04b-claims/     v1.md                      ← atomic claims (the hinge)
│   ├── 05-organize/    v2-claims-outline.md       outline from claims only
│   ├── 06-draft/       v3-claims-only.md          drafter never sees source wording
│   ├── 06a-polish/     v1-gemini-handoff.md       optional literary rewrite
│   ├── 06b-audit/      v1.md                      sentence-vs-claims check, blocking
│   ├── 07-update/      v1.md                      update path (still passage-based)
│   └── 08-review/      v1-prepublication.md       gates the publication layer
│
├── research/                    harvested forum content + all research reports
│   ├── forum/                   raw topic dumps with provenance (id, author, edit date)
│   └── reports/                 the 6 research reports (already here)
│
├── src/kangyur_wiki/
│   ├── cli.py                   typer CLI — every stage is a subcommand
│   ├── config.py, ledger.py
│   ├── stages/                  ingest align terms extract organize draft publish
│   ├── llm/gemini.py            pinned model, caching, structured output, retries
│   ├── wiki/
│   │   ├── client.py            Action API (not REST — see §5)
│   │   ├── wikitext.py          the emitter
│   │   ├── validator.py         ★ hard lint gate
│   │   └── merge.py             the update path
│   └── tibetan/
│       ├── segment.py           botok
│       ├── keyness.py           log-likelihood
│       └── verify.py            ★ verbatim-quotation checker
│
├── corpora/<corpus-id>/         per-corpus working dir (the unit of work)
│   ├── source/                  root.md + commentaries/*.md + sources.yaml
│   ├── work/                    aligned.json, terms.json, extracts/, sections/
│   ├── articles/<term>/         draft.md, article.wiki, citations.json, report.md
│   ├── review/                  ★ human gate: pending/ → approved/ → published/
│   └── ledger.json              status per term, resumable
└── tests/                       golden-file fixtures; no network
```

**The `corpora/<corpus-id>/` contract mirrors `data-pipeline`'s `texts/<text-id>/`:** raw input never overwritten, intermediates in `work/`, a `ledger.json` tracking every term's status, and nothing under `work/` hand-edited (it is all reproducible).

---

## 3. The pipeline — eight stages

Each maps to a step in your forum spec (topic 223). `👨‍💻` deterministic code, `✨` Gemini, `😓` human checkpoint.

| # | Command | Your step | Kind | In → Out |
|---|---|---|---|---|
| 1 | `ingest` | — | 👨‍💻 | raw files → `source/` normalized, segment IDs stamped, `sources.yaml` metadata |
| 2 | `align` | 2.1 | 👨‍💻✨😓 | root + commentaries → `work/aligned.json` (per-śloka commentary spans) |
| 3 | `terms` | 1.2 | 👨‍💻✨😓 | aligned → `work/terms.json` (ranked key terms) |
| 4 | `extract` | 2.3 | ✨ | per term → `work/extracts/<term>.json` (cited passages) |
| 5 | `organize` | 3.2 | ✨ | extracts → `work/sections/<term>.json` (grouped into sections) |
| 6 | `draft` | 3.5 | ✨ | sections → `articles/<term>/draft.md` + `article.wiki` |
| 7 | `verify` | 3.6 | 👨‍💻 | ★ hard gate: every quote verbatim, every ref resolves, wikitext valid |
| 8 | `publish` | 4.x | 👨‍💻😓 | approved → bo.wikipedia (create or update) |

### Stage 2 — alignment (the highest-risk stage)

You chose full auto-alignment. Alignment errors propagate silently into every downstream citation, so this is built as **deterministic first, LLM only for the remainder**:

1. **Deterministic pass.** Split the root into ślokas. For each, search every commentary for a verbatim occurrence of the root text (the BCA vault's `Transclusion-rootext-into-commentaries` skill already does exactly this, variant-tolerant, and is being ported). Most Tibetan commentaries quote the root before commenting, so this resolves the majority with certainty.
2. **LLM pass** (prompt = forum topic 236-v3) only for ślokas the deterministic pass could not anchor.
3. **Verifier.** Every aligned span must be a *contiguous span of the actual commentary file* — offsets checked, not trusted. Any span that isn't is rejected, not repaired.
4. **Human checkpoint** (your step 2.4): a coverage report — which ślokas got commentary from which sources, which are unanchored — before anything downstream runs.

### Stage 3 — key terms

Two signals combined, not one:
- **Statistical** (your step 1.2, "frequency and keyness"): botok tokenizes; log-likelihood keyness (Rayson & Garside) against a reference corpus scores each candidate. ❓ *no standard Tibetan reference corpus was found — we may need to build one from the rest of the Kangyur/Tengyur; see open questions.*
- **LLM** (forum topic 289-v3): must appear in **both** root and commentary, 3–4 ཚེག་བར long, complete terms never truncated, top 20 ranked.

The intersection is proposed; you approve/edit the list before extraction runs. Your prompt 289 was **built and tested on Claude only** — its author says so explicitly — so it needs a re-tuning pass on Gemini (see §7).

### Stages 4–5 — extract and organize

**No forum topic exists for either** (steps 2.2 and 3.1 are unwritten in your own spec). We author them, modelled on the constraints your other prompts already establish: verbatim extraction only, per-source attribution, no invention. Output is structured JSON (Gemini `response_schema`), not prose, so the verifier can check it mechanically.

### Stage 6 — draft

Prompt built from topic 324 (the flagship) + topic 260's rubrics + the 27-rule prompt you pasted. Emits the canonical structure in [wikitext-spec.md](docs/reference/wikitext-spec.md). The Tengyur_Wikiarticle_Generator gem you shared becomes a **second prompt profile** — it is shaped for *works and authors* (catalog numbers, translation lineage), not doctrinal terms, so it keys on entity type rather than replacing the term prompt.

### Stage 7 — verify (the gate)

Deterministic, blocking, no LLM. This is the mechanism the paper's central argument rests on:
- every quotation appears **character-for-character** in its cited source file;
- every `<ref>` resolves to a real source with correct metadata;
- wikitext is valid: balanced refs, `<references />` present iff `<ref>` present, ≥1 `==` heading, ≥1 allowlisted category, **no `{{Reflist}}` under a heading**;
- tsheg-boundary check at every `'''`/`[[` boundary;
- Tibetan-script-only check (your prompts' rule 11).

This is the same class of checker that caught the one bad citation in the BCA run last session. It is what makes the output G15-proof by construction.

### Stage 8 — publish

Review gate, as you chose. `review/pending/` → you approve → `review/approved/` → `publish` command:
1. **Probe title variants** — bare, +tsheg, +shad (the `སངས་རྒྱས` three-way split is live).
2. **Wikidata lookup** — the concept may exist under a different bo title.
3. **Create** (`createonly=1`, so a race can't duplicate) or **update** (`basetimestamp` for conflict detection).
4. Section-targeted edits for updates, never whole-page rewrites — keeps diffs reviewable.
5. `--dry-run` is the **default**; `--execute` requires explicit confirmation, mirroring `data-pipeline`'s uploader rule.

---

## 4. The update path (your stage 4)

Your spec's stage 4 has **zero published prompt** — it is the least-specified part and needs the most design. Plan:

1. Fetch current wikitext + section index (`action=parse&prop=sections`); target sections by **anchor**, never by string-matching headings.
2. For each new claim from the new text, classify against existing content: **duplicate** (→ append a citation to the existing sentence), **new** (→ insert sentence with citation into the right section), **conflicting** (→ flag for human, never auto-merge — this is the ⚑ divergence rule from the Railroad method).
3. Emit a **diff**, not a rewrite. The review gate shows you the diff.
4. Verify the merged article as a whole before publishing.

---

## 5. Technical decisions, made

| Decision | Choice | Why |
|---|---|---|
| Wiki write API | **Action API** (`action=edit`) | REST has no `createonly`/`nocreate`/`bot`/`minor`. `createonly` is the only real guard against creating a duplicate at a title variant. |
| Auth | **Bot password** (`Special:BotPasswords`) in `.env` | Works with plain `requests`; OAuth 2.0 owner-only is the alternative but forecloses pywikibot. |
| Wiki library | **`requests` + thin client**, not pywikibot | We need ~6 API calls; pywikibot's config/family machinery is overhead, and a thin client is testable offline. |
| Model | **`gemini-3.5-flash`, pinned**, via legacy `generateContent` | Interactions API lacks explicit caching, batch, *and* safety settings. Never a `-preview` id. |
| Cost control | **Explicit context caching** of the commentary corpus across all terms | The corpus is the same for every term in a run; cache reads are $0.15/MTok vs $1.50. |
| Citations | Hand-formatted `<ref>` for canonical sources; `{{Cite book}}` only for modern secondaries | CS1 emits English furniture inside Tibetan prose. |
| Refs display | `== ལུང་ཁུངས། ==` + `<references />`, **never `{{Reflist}}`** | The double-heading trap, verified live. |
| Categories | Curated allowlist, model may not invent | Live category namespace contains misspellings and shad typos. |
| Packaging | **uv** + `pyproject.toml` | Single-command setup on macOS. |
| CLI | **typer** | Subcommand per stage, good `--help` for a non-programmer. |

### The dummy-link resolver — the largest unbuilt component

Your topic-324 prompt emits `https://dummy.com` and its author flags automatic link resolution as the missing piece. Design:

- `sources.yaml` declares, per source: author, title, year, `wikisource_page`, `bdrc_id`, `base_url`.
- The extract stage records `source_id` + `segment_id` + the exact quoted string for every passage.
- The resolver maps `source_id` → URL and appends a **text fragment** (`#:~:text=<first-6-syllables>,<last-6-syllables>`, percent-encoded) so the link lands on the quoted passage — this is precisely what your team's published `སཏྭ་` article does by hand.
- No URL available → emit `<ref>author། title།</ref>` unlinked **and** flag it in the review report, so the gap is visible rather than silent.

This is what makes each citation independently checkable by a reader, which is the difference between "AI slop" and a defensible article.

---

## 6. Phasing — what gets built in what order

Given IATS is **23–29 August** and today is 29 July, the ordering is by what the paper needs, not by pipeline order.

**Phase 1 — walking skeleton (days 1–3).** Repo scaffold, config, ledger, CLI, Gemini client, and stages 4→8 running on the **BCA corpus, which is already aligned** — bypassing stages 2–3. Produces one published-shaped article end to end. This proves the hard half (draft → verify → wikitext → publish) first.

**Phase 2 — the output spec is right (days 4–6).** Wikitext emitter + validator hardened against the real bo.wikipedia conventions; dry-run publish to your userspace sandbox; visually confirm rendering (the Reflist trap, tsheg boundaries, ref markers).

**Phase 3 — the front half (days 7–11).** Stages 1–3: ingest, alignment (deterministic + LLM + verifier + coverage report), keyness-based term selection. Now a raw root text + commentaries can enter the pipeline.

**Phase 4 — the update path (days 12–14).** Stage 4 merge logic, diff review, section-targeted edits.

**Phase 5 — run + evaluate (days 15–20).** Generate the article batch, measure everything ([06 - Evaluation Plan](paper/06%20-%20Evaluation%20Plan.md)), publish the approved set, log cost and human-review minutes per article.

**Phase 6 — paper and talk (days 21–25).** Write the paper against real numbers; build the offline demo.

If time compresses, Phases 1–2 plus a small evaluation still fulfil the abstract; Phase 4 is the first thing to cut.

---

## 7. Known risks

| Risk | Mitigation |
|---|---|
| **Your prompts were tuned on Claude, not Gemini** — topic 289's author says so explicitly; 309/324's outputs are labelled Claude Opus 4 | Budget a re-tuning + eval pass on pinned Gemini before any batch run. Golden-file tests catch drift. |
| **Auto-alignment errors poison every downstream citation** | Deterministic-first, verifier on span offsets, human coverage checkpoint before extraction. |
| **Gemini invents citations** | The verify gate is deterministic and blocking; a quote that is not character-for-character in the source fails the build. |
| **Bot account lead time** — a flagged bot may take weeks to approve on a wiki with 2 admins | ❓ decide now: new bot account vs. existing account with disclosure. Publishing works either way at human pace. |
| **Your own specs contradict each other** — gloss length (<10 vs >10 ཚེག་བར), sub-heading markup (`'''` vs `==`), reference heading (`ལུང་ཁུངས།` vs `དཔེ་ཁུངས།`) | Resolved in [wikitext-spec.md](docs/reference/wikitext-spec.md) with evidence; you confirm or override. Validator can't be written until these are pinned. |
| **bo.wikipedia may have no functioning consensus mechanism** — Village pump (policy) is 1,783 bytes, 2 admins | Post the proposal now, in parallel with the build; it is also a paper result either way. |

---

## 8. What I need from you

Full list with context in [open-questions.md](docs/reference/open-questions.md). The four that block work:

1. **The Google Sheet link** — you mentioned it twice; it never came through. Those published articles are the best format exemplars available.
2. **Which corpus for v1?** Your forum prompts are written around འཕགས་པ་སྡུད་པ + 4 commentaries; the published articles are about ཡིག་བརྒྱ commentaries; the aligned data I have locally is the Bodhicaryāvatāra. Phase 1 uses BCA regardless (it is aligned already), but Phase 3 needs the real target.
3. **Bot account** — new one, or an existing account with disclosure?
4. **The three Google Docs** linked from the forum topics are login-walled. If drafts of the missing prompts (extract / organize / update) exist there, that saves authoring them from scratch.
