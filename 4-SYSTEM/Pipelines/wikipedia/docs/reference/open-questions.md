# Open Questions — decisions needed from Tashi

Grouped by whether they block work. Each has my recommendation, so you can say "go with your recommendation" and I'll proceed.

---

## Blocking — needed before the affected stage is built

### Q1. The Google Sheet link
You referenced it twice ("you can refer to this google sheet ... there are some articles generated") but the link didn't come through. Those already-published articles are the best format exemplars available — better than any spec, because they are what the community actually accepted.

*Blocks:* final calibration of the drafting prompt and few-shot examples.

### Q2. Which corpus for v1?
Three candidates are in play and they are not the same:
- **འཕགས་པ་སྡུད་པ** (Ratnaguṇasaṃcayagāthā) + 4 named commentaries — what your forum prompts 236 and 289 are written around, with commentary names hardcoded.
- **ཡིག་བརྒྱ** (hundred-syllable mantra) commentaries — what the published `སཏྭ་` article is drawn from.
- **Bodhicaryāvatāra** — what is aligned and ready on this machine right now (8 commentaries, block IDs, verse transclusions).

*Recommendation:* Phase 1 uses **BCA** regardless, because it's already aligned and proves the back half of the pipeline immediately. Phase 3 (when alignment is built) should target whichever of the other two is the real project deliverable — that's your call.

*Blocks:* Phase 3. Also determines whether topic 236-v3's hardcoded commentary names can be reused or must be templated.

### Q3. Bot account
Options: (a) create a new `OpenPechaBot`-style account and request a bot flag — clean separation of human and machine edits, but flag approval on a wiki with 2 admins could take weeks; (b) publish under an existing account (`Pecha-G.Dhargyal` is bo.wikipedia's only human admin, and several `Pecha-*` accounts already have 300+ edits) with disclosure in every edit summary — available today.

*Recommendation:* **(b) for now**, since the review gate means every edit is human-approved anyway and the volume is ~15 articles, not thousands. Start a flag request in parallel for later scale.

*Blocks:* stage 8 testing. Everything up to it can be built without this.

### Q4. The three login-walled Google Docs
The forum topics link three companion docs (`1WOX6PG2…`, `1M3N85dI…`, `1AlNyCSS…`). All return a login redirect. If they contain drafts of the **three missing prompts** — extract-per-term (your step 2.2), organize-into-sections (3.1), compare-and-update (4.2) — that saves authoring them from scratch, and more importantly means we build on what your team already validated.

*Recommendation:* open them yourself and either paste the contents or make them link-viewable. Five minutes, and it changes whether stages 4/5/7 are integration work or original work.

---

## Blocking — small, quick answers

### Q5. Gloss length
Your own specs contradict: topic 289-v3 says explanations must be **fewer than 10 ཚེག་བར**; topic 289-v2 and topic 239 (the editor charter) say **10 or more**.

*Recommendation:* **fewer than 10** for the term-list gloss (289-v3 is the most refined version), with no limit on prose in the article body. The validator can't be written until this is pinned.

### Q6. Title variant to create at
`སངས་རྒྱས་` (tsheg), `སངས་རྒྱས།` (shad), and bare `སངས་རྒྱས` all exist as separate pages on bo.wikipedia today — one of them a broken redirect. We probe all three before creating; the question is which one we *write* to.

*Recommendation:* **shad form** (`སངས་རྒྱས།`) as the article title, since that is the citation form of a Tibetan term and the longer of the two live articles uses it — and create redirects from the other variants. Worth a second opinion from a bo.wikipedia editor.

---

## Non-blocking — can be decided during the build

### Q7. Reference corpus for keyness
Log-likelihood keyness (your step 1.2) needs a reference corpus to compare against. No standard Tibetan one surfaced in the research. Options: build one from the rest of the Kangyur/Tengyur via OpenPecha data (best fit, some work), or use a general modern-Tibetan corpus (easier, worse fit for classical texts).

*Recommendation:* build from OpenPecha canonical texts. If time is short, ship frequency-only ranking for Phase 3 and add keyness later — the LLM pass carries most of the selection quality anyway.

### Q8. Wikisource dependency
The Wikimedia project page for your group says contributions should be backed by texts *available on Wikisource*. Many commentaries won't be. Does an article get blocked if its sources aren't on Wikisource, or do we cite BDRC and proceed?

*Recommendation:* **proceed with BDRC IDs**, and maintain an "upload to Wikisource" queue as a separate track. Blocking on Wikisource availability would stall almost everything.

### Q9. Prompt re-tuning budget
Topic 289's author states in Tibetan that it was built and tested **in Claude only**, and topics 309/324 label their outputs `Claude Opus4` with an explicit warning that other models give different results. You've chosen Gemini. The prompts need a re-tuning and evaluation pass on a pinned Gemini model before any batch run.

*Recommendation:* budget 1–2 days in Phase 3 for this, and report it in the paper — "prompts tuned on one model do not transfer" is a genuinely useful finding for the IATS audience.

### Q10. What counts as "conflicting" in the update path
When new commentary material contradicts what an existing Wikipedia article says, the pipeline flags rather than merges (the Railroad ⚑ divergence rule). But who resolves it, and does the article record the divergence or pick a reading?

*Recommendation:* **record both, attributed** — this is the Railroad method's core commitment and it is also what makes the articles scholarly rather than flattening. Flag for your review either way.

---

## Answered already (2026-07-29)

| Question | Your answer |
|---|---|
| How far does the pipeline go on its own? | Review gate, then publish |
| Repo location | `~/Desktop/work/IATS-2026`, self-contained |
| Alignment | Pipeline does it |
| LLM | Gemini only |
