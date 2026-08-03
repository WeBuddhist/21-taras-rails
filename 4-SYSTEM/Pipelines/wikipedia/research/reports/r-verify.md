# Verification Report — OpenPecha Tibetan Wikipedia Pipeline Research

All probes run 2026-07-29 against live endpoints. Raw artifacts in `/private/tmp/claude-501/-Users-tashitsering-Desktop-work-Obsidian/73add4a1-148e-4256-9607-eeb709eeb75a/scratchpad/`.

---

## VERIFIED FACTS

### 1. The OpenPecha forum content WAS retrieved — verbatim, and by three independent public routes

The `forum-prompts` report's prompt transcriptions are **real, not reconstructed**. I re-fetched them myself:

| Endpoint | Result |
|---|---|
| `https://forum.openpecha.org/t/prompt-sample/324.json` | **HTTP 301** → `https://forum.openpecha.org/t/new-prompt-sample/324.json` (the task-supplied slug is stale; the report was right) |
| `https://forum.openpecha.org/t/new-prompt-sample/324.json` | **200**, 50,328 B. `title: "New Prompt Sample"`, 3 posts. Posts carry `cooked` (rendered HTML) — **no `raw` key** — but the prompt survives inside `<pre><code class="lang-auto">` fences, including the literal string `14)` and `dummy.com` |
| `https://forum.openpecha.org/t/324.json` (**id only, no slug**) | **200**, byte-identical 50,328 B — the slug is optional |
| `https://forum.openpecha.org/raw/324` | **200**, `text/plain`, 10,991 chars. Un-rendered Markdown of all 3 posts with `author \| timestamp \| #post_num` headers |
| `https://forum.openpecha.org/posts/386.json` | **200** — **has a `raw` key**, 10,387 chars of un-rendered Markdown for that single post |
| `https://forum.openpecha.org/c/wg/wiki-wg/35.json` | **200**, 34,757 B. **30 topics** on page 0, `more_topics_url: /c/wg/wiki-wg/35?page=1` — pagination confirmed |

No auth, no login wall, no rate limiting encountered. The `14)` numbering defect (no item 13, only item in Latin numerals) is confirmed present in both `raw` and `cooked`. Post #3's English caveat ("this sample is just for temporary use for a presentation purpose… I'm sure you can get better prompts, with which you can let AI get the link address for you") is confirmed verbatim.

**Conclusion: (c) is answered — the forum reports got real verbatim text. Nothing needs re-harvesting.**

### 2. bo.wikipedia citation templates — the "no cite templates" premise is definitively FALSE

`action=query&prop=info` on `https://bo.wikipedia.org/w/api.php`:

```
EXISTS  pageid=3080   དཔེ་པང་།:Reflist
EXISTS  pageid=21165  དཔེ་པང་།:Cite web
EXISTS  pageid=21167  Module:Citation/CS1
EXISTS  pageid=24090  དཔེ་པང་།:Cite book
EXISTS  pageid=24581  དཔེ་པང་།:Cite encyclopedia
EXISTS  pageid=25566  དཔེ་པང་།:Cite journal
MISSING               དཔེ་པང་།:Citation
MISSING               དཔེ་པང་།:Sfn
MISSING               དཔེ་པང་།:Cite wikisource
```

`Template:Cite book` source is the standard CS1 wrapper: `<includeonly>{{#invoke:citation/CS1|citation |CitationClass=book }}</includeonly>`.

### 3. The `{{Reflist}}` double-heading trap is REAL — highest-value single finding, confirmed at source

`https://bo.wikipedia.org/w/index.php?title=Template:Reflist&action=raw` begins, literally, with a heading:

```wikitext
== ཡོང་ཁུངས། ==
<div class="references-small" {{#if: {{{colwidth|}}}| style="...">
{{#tag:references||group={{{group|}}}}}</div><noinclude>[[Category:སྒྲོམ་གཞི།]]
</noinclude>
```

I rendered `== ལུང་ཁུངས། ==\n{{Reflist}}` through `action=parse` on live bo.wiki. Output text:

```
ལུང་ཁུངས།[རྩོམ་སྒྲིག | མ་ངོས་ཞུ་དག]
ཡོང་ཁུངས།[མ་ངོས་ཞུ་དག]
↑ ཀློང་ཆེན་པ། (1990). ཡིད་བཞིན་མཛོད། (2 ed.). ཟི་ལིང་།: x. pp. 12–14.
```

Two stacked headings, exactly as `bo-wiki-conventions` predicted. `parsewarnings: []`, no `cite-error`, all 9 CS1 modules loaded. Also confirmed in the same render: **ref markers auto-localize to Tibetan numerals (`[༡]`)**, and **CS1 furniture stays English (`2 ed.`, `pp.`)** inside Tibetan prose.

### 4. `google-genai` is the correct package; current model IDs confirmed

PyPI JSON API:
- **`google-genai` 2.14.0**, uploaded **2026-07-22**, `requires_python >=3.10`. Import is `from google import genai`.
- `google-generativeai` latest is **0.8.6**, uploaded **2025-12-16**.

`https://ai.google.dev/gemini-api/docs/models` — **stable** text models: `gemini-3.6-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemini-2.5-pro`, `gemini-embedding-2`. **Preview**: `gemini-3.1-pro-preview`, `gemini-3-flash-preview`, `gemini-omni-flash`. **Shut down**: `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-3-pro-preview`, `gemini-3.1-flash-lite-preview`.

Deprecations page: `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.5-flash-lite` all shut down **2026-10-16** — before IATS Aug 2026 is safely past. `gemini-3.1-flash-lite` deprecated 2026-05-07, shutdown 2027-05-07, replacement `gemini-3.5-flash-lite`.

Pricing page (paid, per 1M): `gemini-3.6-flash` $1.50 / $7.50, cache read $0.15; `gemini-3.5-flash` $1.50 / $9.00, cache read $0.15. Both confirmed as the `gemini-api` report stated.

**Safe model choice: `gemini-3.5-flash` or `gemini-3.6-flash`, pinned exactly, never a `-preview` id.**

### 5. Interactions API feature gaps — confirmed and WIDER than reported

`https://ai.google.dev/gemini-api/docs/interactions-overview` lists as **not yet available in the Interactions API**: Batch API, **explicit caching**, automatic function calling (Python), video metadata, and — not flagged by any report — **custom safety settings**. `generateContent` is "considered legacy" but "remains fully supported", with **no shutdown date published**.

This settles the biggest architectural question: **the primary generation path must be legacy `generateContent`**, because explicit caching, Batch, *and* safety-threshold control all live there and this project needs all three.

### 6. bo.wikipedia site state and Tibetan title fragmentation

`siteinfo`: **22,734 pages / 8,072 articles / 161,834 edits / 35,568 users / 31 active users / 2 admins**, MediaWiki `1.47.0-wmf.12`. All numbers in all three wiki reports match exactly.

The three-way title split is real:
```
སངས་རྒྱས་  (U+0F0B tsheg)  pageid=7060  len=3,981
སངས་རྒྱས།  (U+0F0D shad)   pageid=7061  len=10,414
སངས་རྒྱས   (bare)          → redirect → "སངས་རྒྱས། (གོ་ལོག་སེལ་བ།)" which is MISSING (broken redirect)
```

`Wikipedia:Bot policy` on bo is a **39-byte redirect**: `#redirect[[Wikipedia:Community Portal]]`. `Wikipedia:Village pump` (45,903 B) and `Wikipedia:Village pump (policy)` (**1,783 B — nearly empty**) exist. `Wikipedia:Sandbox` exists but has **length 0**.

### 7. Live `སཏྭ་` article structure — re-fetched and counted

Headings in order: lead → `== གོ་དོན། ==` → `== ངེས་ཚིག ==` → `== དབྱེ་བ། ==` → `== དགག་བཞག་རྩོད་སྤོང་། ==` → `== གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ==` → `== འབྲེལ་ཡོད་བརྗོད་གཞི། ==` → `== ཁུངས། ==` → `<references>` (whitespace only) `</references>`. `[[Category:ནང་བསྟན།]]` on line 1. **Exactly 8 `<ref>` tags**, all of form `<ref>[https://wikisource.org/wiki/<pct-encoded>#:~:text=<pct-encoded quote> author. title. ]</ref>`. No named refs, no CS1. Wikilinks include a piped synonym form `[[བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་|བྱང་ཆུབ་སེམས་དཔའ།]]`. All matches `forum-prompts` §13.

### 8. Sitewide heading and citation counts (CirrusSearch, ns0)

| Query | Hits |
|---|---:|
| `insource:/\{\{ *[Cc]ite book/` | **19** |
| `insource:"Cite book"` (quoted form) | **19** |
| `insource:/\{\{ *[Cc]ite web/` | 66 |
| `insource:/\{\{ *[Rr]eflist/` | **554** |
| `insource:/\<ref/` | **1,289** |
| `insource:/\<references/` | **128** |
| `== ལུང་ཁུངས། ==` | **738** |
| `== དཔྱད་གཞིའི་ཡིག་ཆ། ==` | 614 |
| `== ཟིན་ཐོ་འམ་དཔྱད་གཞི། ==` | 2,790 |
| `== ད་དུང་གཟིགས། ==` | 3,834 |
| `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` (prompt form) | **13** |
| `== ཁུངས། ==` | **1** |
| `== འབྲེལ་ཡོད་བརྗོད་གཞི། ==` | **1** |
| `== ཡོང་ཁུངས། ==` literal | 2 |
| `ལུང་ཁུངས།` heading **and** `{{Reflist}}` in same page | **1** |

Derived: 1,289 pages have `<ref>` but only 128 + 554 = 682 have a display mechanism → **≈600 pages have orphaned footnotes**. The scale of the "no citation display" problem is larger than any report stated.

### 9. botok `kangyur` dialect pack is genuinely empty

`unzip -l kangyur.zip` → **14 entries, all 0 bytes**, all `.keep` placeholders. `Config(dialect_name="kangyur")` yields an empty trie. Confirmed.

### 10. OpenPecha API v2 is live and unauthenticated

`GET https://api-aq25662yyq-uc.a.run.app/v2/texts?type=root&language=bo&limit=2` → 200, real JSON with `bdrc`, `wiki`, `type`, `contributions[].person_bdrc_id`, `title.bo`, `id`. The `wiki` field is present and `null` on both records — the Wikipedia back-link slot exists but is unpopulated.

### 11. en.wikipedia LLM policy — the guideline is `WP:Writing articles with LLMs`

- `Wikipedia:Writing articles with large language models` — **content guideline** ("Editors should generally follow it"), prohibition traced to a **March 2026 RfC**; a further March–May 2026 RfC made persistent LLM use blockable. Exceptions: copyediting one's own writing; translation from other-language Wikipedias. Last edited 2026-07-25.
- `Wikipedia:Large language models` — **information page, not policy or guideline**. Carries the edit-summary disclosure expectation.

Not binding on bo.wikipedia, which has no equivalent — but it is the movement's live consensus, and it is a content *guideline*, not an essay.

### 12. The three companion Google Docs are NOT public

All three doc IDs (`1WOX6PG2…`, `1M3N85dI…`, `1AlNyCSS…`) return **HTTP 307** to login on `/export?format=txt`. Any content behind them is unretrieved and unverifiable.

---

## CORRECTIONS

**C1 — `forum-prompts`: "`.json` returns `cooked`, no `raw` key — worse for prompt fidelity." Half wrong, and it matters for the ingestion design.**
Code fences survive intact in `cooked` (I extracted `14)` and `dummy.com` from it). More importantly, **`/posts/<post_id>.json` *does* return a `raw` key** with un-rendered Markdown. The report's implementation recommendation ("use `/raw/<topic_id>` as the ingestion endpoint, do not use `.json`") is fine but under-specified: `/raw/` concatenates all posts of a topic into one blob with `author | ts | #n` separators, so per-post provenance requires splitting on those headers. `/posts/<id>.json` gives per-post `raw` + `created_at` + `updated_at` + `version` cleanly. **Prefer `/t/<id>.json` (works without slug) to enumerate post ids, then `/posts/<id>.json` for each.**

**C2 — `forum-prompts`: "Take section names from the live wiki, not from the prompts." This is an n=1 recommendation and should not be adopted as written.**
The live-wiki headings it recommends canonicalizing — `== ཁུངས། ==` and `== འབྲེལ་ཡོད་བརྗོད་གཞི། ==` — each occur in **exactly 1 article on the entire wiki** (the `སཏྭ་` article the report sampled). The prompt-specified `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` occurs in **13**, and `== ལུང་ཁུངས། ==` in **738**. The report generalized a single article into "the deployed reality." The correct canonical choice is `bo-wiki-conventions`' recommendation: **`== ལུང་ཁུངས། ==` for references** (738, and 121 in-corpus), **`== འབྲེལ་ཡོད་ཤོག་ངོས། ==` or `== ད་དུང་གཟིགས། ==`** for see-also.

**C3 — `bo-wiki-conventions`: "the quoted form `insource:"..."` is tokenizer-inflated and gave numbers 2–30× too high."** For `Cite book` I get **19 both ways** — quoted and strict-regex agree exactly. The methodological warning is over-broad; it may hold for Tibetan-script queries (where CirrusSearch tokenization does inflate) but not for Latin template names. Consequently `mediawiki-bot`'s "19 hits" figure was correct, not inflated, and the two reports do not actually conflict here.

**C4 — `gemini-api`: "`safety_settings` is also a top-level field on `CreateInteraction`." Wrong.** The Interactions overview lists **custom safety settings as not supported in the Interactions API**. This strengthens (not weakens) that report's own conclusion to stay on `generateContent`, but the code sample it offers for Interactions + safety would fail.

**C5 — `gemini-api`: `gemini-3.5-flash-lite` cache read `$0.03` / cache storage `$1.00/1M/hr`.** The pricing page states **context caching is "Not available"** for `gemini-3.5-flash-lite`. If term extraction is routed to flash-lite as recommended, it **cannot share the cached commentary corpus** — the two-model split and the caching strategy are in tension. Re-verify before designing around it.

**C6 — `gemini-api`: "`gemini-3.5-flash-lite` and `gemini-3.1-flash-lite` do have free batch."** The pricing page now shows **batch unavailable on free tier for all four flash models**. Any plan that assumes free-tier batch for a dry run is wrong.

**C7 — Google's own docs are internally inconsistent on `gemini-3.1-flash-lite`.** The models page lists it under **stable**; the deprecations page lists it as **deprecated 2026-05-07 / shutdown 2027-05-07**. `gemini-api` reported the deprecation correctly; `pipeline-engineering` listed it as a current stable option with pricing, without the deprecation. Treat it as deprecated.

**C8 — `pipeline-engineering`: cites `Wikipedia:Large language models` as the operative rule.** That page is an **information page**, explicitly "not a Wikipedia policy or guideline." The binding artifact is `Wikipedia:Writing articles with large language models`, which `mediawiki-bot` identified correctly. The quoted prohibition sentence appears on both, so the substance stands, but a Village-pump proposal citing the wrong page is an avoidable own-goal.

**C9 — `pipeline-engineering` pricing block** ("`gemini-3.1-pro-preview` $2/$12, `gemini-3-flash-preview` $0.50/$3, `gemini-3.1-flash-lite` $0.25/$1.50") mixes preview and deprecated models and does not cover its own recommended default (`gemini-3.6-flash`, actually $1.50/$7.50). The `gemini-api` report's pricing table is the accurate one.

**C10 — `gemini-api`: "`google-generativeai` … All support for this repository ended permanently on November 30, 2025."** The repo notice may say that, but PyPI shows **0.8.6 uploaded 2025-12-16**, after that date. The conclusion (do not use it) is right; the date is not load-bearing but is not clean either.

**C11 — `forum-prompts` topic 324 date.** The report gives `2025-06-24`. That is `created_at`; the `/raw/324` header shows `Tsewang | 2025-07-12 14:40:07 UTC | #1` (last edit). Any provenance record must capture both — the prompt text on file today is the *edited* version, not what was posted on 2025-06-24.

---

## Contradictions between reports, ranked by how much a build plan trips on them

**X1 — Wiki write API: Action API vs REST. Unresolved and load-bearing.**
`mediawiki-bot` says use `action=edit` because **REST has no `bot` flag, no `minor`, no `createonly`/`nocreate`** — and it verified `createonly`→`articleexists` / `nocreate`→`missingtitle` live, which is the TOCTOU guard. `pipeline-engineering` says use REST because `latest.id` gives free optimistic concurrency and the POST/PUT split maps onto create/update. **`mediawiki-bot` is right for a bot.** Losing `createonly` means an existence-check race can create a duplicate at a variant title — which on a wiki with three `སངས་རྒྱས་` pages is a live hazard, not a theoretical one. Recommend Action API for writes; REST is fine for reads.

**X2 — Citation form: CS1 templates vs hand-formatted `<ref>`.** `mediawiki-bot` says design the citation layer around `{{Cite book}}`/`{{Reflist}}`; `bo-wiki-conventions` says default to hand-formatted `<ref>` for Kangyur/Tengyur primaries because CS1 emits English furniture, and reserve CS1 for modern secondary sources. My render test confirms the English-furniture problem (`2 ed.`, `pp.`). The **live articles the team already published use neither** — they use `<ref>[wikisource-URL#:~:text=… author. title.]</ref>`. Three candidate schemes, no decision recorded.

**X3 — Model default: `gemini-3.6-flash` (pipeline-engineering) vs `gemini-3.5-flash` (gemini-api).** Both stable, both 1M context. 3.6 is cheaper on output ($7.50 vs $9.00); 3.5 is argued to be stronger on sustained reasoning. Nobody has tested either on Tibetan for this task. Needs an A/B, not a report.

**X4 — Gloss length: 289-v3 says **fewer than 10** ཚེག་བར; 289-v2 and topic 239 (the editor charter) say **more than 10**.** This is a contradiction *inside the team's own published specs*, not between reports. A validator cannot be written until a human picks one.

**X5 — Sub-heading markup:** 260-རབ་བརྟན rule #9 says `'''bold'''`; 260-ཡེ་ཤེས rule 3 says `==` for subheadings too; the live `སངས་རྒྱས།` article uses bold-as-pseudo-heading; the numbered Tengyur skeleton uses `=== '''…''' ===`. Four conventions in the wild, zero decisions.

**X6 — Reference-heading canon:** `ལུང་ཁུངས།` (738) vs `ཁུངས།` (1, live article) vs `དཔེ་ཁུངས།` (0 — the topic-309 prompt's form is **unattested anywhere on the wiki**) vs `དཔྱད་གཞིའི་ཡིག་ཆ།` (614). Resolved above in favor of `ལུང་ཁུངས།`.

**X7 — Chunk/context strategy:** `gemini-api` proposes File Search (Interactions) *plus* explicit caching (generateContent) as a deliberate two-API split. But File Search stores index at $0.15/1M and Interactions has no explicit caching — so the "both" architecture pays for two representations of the same corpus and straddles two request shapes. No report costed the combined version.

---

## STILL UNKNOWN

**U1 — The three missing prompts (steps 2.2 extract-per-term, 3.1 organize-into-sections, 4.2 compare-and-update).** No forum topic exists for any of them; topic 223's Tibetan mirror hyperlinks every *other* numbered step to a topic. The **entire UPDATE path (stage 4) has zero published prompt**. → *Resolution:* ask Trinley (topic 223 author) and gade directly whether drafts exist off-forum. The three companion Google Docs are **login-walled (307)** and cannot be checked from here — Tashi can open them with his own account and confirm in five minutes. If they don't exist, the repo must author them, and that should be scoped as original work in the build plan, not integration.

**U2 — None of the published prompts has been validated on Gemini.** Topic 289 states in Tibetan it was built and tested **in Claude AI only**; 309/324's worked output is labelled `Claude Opus4` with an explicit warning that Sonnet 4 gives different results; only 236 and 295 mention Gemini. The project mandates Gemini. → *Resolution:* a re-tuning + eval pass on all three prompts against a pinned Gemini model, budgeted before any article generation. Nothing on the web can answer this.

**U3 — Whether `gemini-3.5-flash-lite` supports context caching.** The pricing page says "Not available", which breaks the recommended two-model split. → *Resolution:* one `client.caches.create(model="gemini-3.5-flash-lite", …)` call with a real key; it either returns a cache name or a 400.

**U4 — Tibetan tokens-per-syllable on Gemini's tokenizer.** Google publishes no figure; the "fertility 19.9" number in `gemini-api` is explicitly flagged as un-attributed to a specific tokenizer. Every chunk size, context budget, and cost estimate downstream depends on it. → *Resolution:* run `client.models.count_tokens` over Kangyur, Tengyur, and modern-Tibetan samples. Needs an API key; ten minutes of work; genuinely publishable at IATS.

**U5 — Whether alignment layers are actually populated for the intended corpus.** `pipeline-engineering` hit `[]` from `/v2/instances/{id}/segment-related` on both instances it tried. `GET /v2/texts` works, `?content=true` works, `/related` returns `relationship: "commentary"` — but the segment-level alignment that stage 2 depends on is unproven. → *Resolution:* pick the actual v1 root text, walk root → instances → related → segment-related, and confirm non-empty. If empty, the alignment step is manual/Pecha-editor work, which changes the project's critical path.

**U6 — Which root text + four commentaries is the v1 corpus.** The forum prompts are all written around **འཕགས་པ་སྡུད་པ** (Ratnaguṇasaṃcayagāthā) + 4 named commentaries, and the published articles are about the **ཡིག་བརྒྱ** (hundred-syllable mantra) commentaries — a different corpus. The project brief names neither. → *Resolution:* Tashi decides; it determines whether topic 236-v3's hardcoded commentary names are reusable or must be templated.

**U7 — Whether a bot account exists, and its edit count.** All five reports assume `User:OpenPechaBot` is to be created. But `Pecha-Alalamo` (422 edits), `Pecha-Gade` (388), etc. are already doing stage-4 edits by hand, and topic 418 lists eight members with >500 edits. → *Resolution:* decide whether to run under a new flagged bot account (autoconfirm/flag lead time, ~weeks) or under an existing human account with disclosure (available today, but conflates human and machine edits). This is a governance decision with a schedule impact against Aug 2026.

**U8 — Whether bo.wikipedia will tolerate this at all.** `Wikipedia:Village pump (policy)` is **1,783 bytes** — effectively an empty page on a wiki with 2 admins. There may be no functioning consensus mechanism to obtain consensus from. → *Resolution:* post the proposal and see. Multi-week lead; start now, in parallel with the build.

**U9 — Gemini rate limits (RPM/TPM/RPD).** Google no longer publishes per-model tables; visible only in AI Studio for the specific project. → *Resolution:* read them off AI Studio once billing is enabled.

**U10 — Whether the OpenPecha PROD API is stable enough to build against.** `pipeline-engineering` found obvious test junk in PROD (`wiki: "ho how are youcom"`), and I confirmed `wiki: null` on live root texts. → *Resolution:* ask the backend owner whether PROD is authoritative or whether a data-cleaning pass is pending.

---

## Missing technical decisions the build plan will trip over

Each of these is currently undecided across all five reports, and each blocks code:

1. **One canonical section schema** for a term article — the four candidate schemes (topic 260 rubric, topic 324 rubric, live `སཏྭ་`, live `སངས་རྒྱས།`) do not agree on names, order, or count. Needed before the drafting prompt or the validator can be written.
2. **One citation form** (X2) and how the `#:~:text=` fragment is generated. The team's own published articles rely on it; no report specifies how to build it from an LLM-returned quote, and it is the thing that makes citations independently verifiable.
3. **Write API + auth pair** (X1). OAuth 2.0 owner-only forecloses pywikibot; that's fine, but it must be decided once, because `mediawiki-bot`'s `createonly`/`nocreate` guards only exist on the Action API.
4. **Gloss length and sub-heading markup** (X4, X5) — validator rules cannot be written until a human resolves the team's own internal contradictions.
5. **Where the "resolve `dummy.com` → real Wikisource URL + page + text-fragment" step lives.** Topic 324's author flagged this as the missing piece. No report specifies the resolver's algorithm or its failure behavior. It is the single largest unbuilt component.
6. **What happens when a commentary is not on Wikisource.** Meta project page rule: contributions must be backed by texts *available on Wikisource*. No report specifies the gate or the "upload first" queue.
7. **Which of `<references />` vs `{{Reflist}}` the emitter produces** — resolved by evidence above (`<references />` under an explicit `== ལུང་ཁུངས། ==`; never `{{Reflist}}` under a heading), but it must be written down and linted, since the enwiki idiom an LLM will produce is exactly the broken one.
8. **Title-variant normalization policy** — which of `{bare, +tsheg, +shad}` the pipeline *creates* at, given all three exist for `སངས་རྒྱས`. Probing all three is agreed; choosing one to write to is not.
9. **Category allowlist** — the live namespace contains misspellings (`ནང་པ་སངས་རྒྱངས་ཀྱི་ལྷ།`) and shad typos (`ནང་པ་སངས་རྒྱས།།`). The allowlist must be pinned and committed; no report proposes the specific list beyond a seed.
10. **Cost/latency instrumentation from run 1.** The IATS headline result is almost certainly "N articles at M cost with human QC rate R." Nothing captures R (the draft→approved diff) unless the ledger is designed for it on day one.