# Presentation and Demo Plan

Audience: Tibetan-studies scholars (mostly non-NLP). Lead with language preservation and access; keep model architecture to one slide. Presenting in English or Tibetan is permitted at IATS — consider a Tibetan-language demo moment even in an English talk.

## Talk arc (20 min shape; adjust when session length is confirmed)

1. **The stakes** (3 min) — bo.wikipedia: 8,072 articles for 7M+ speakers; GPT-4 below random on Tibetan (TLUE); the 2025 RFA/VOA Tibetan shutdowns; DeepZang. *Who builds digital Tibetan?*
2. **The idea** (2 min) — the cycle: cited Tibetan content → training data → Tibetan-capable AI → visibility in Perplexity-class tools → more readers/editors. And the warning: the same loop unverified is the doom spiral (Greenlandic Wikipedia was *closed* in 2025). Our claim: **human verification flips the sign.**
3. **The pipeline** (5 min) — five stages ([[03 - Pipeline Design]]); where the humans sit; "cite, don't copy"; the Railroad citation chain (1-Human-Sources → context packages → article) with one concrete slide showing a block-cited passage flowing into an article sentence.
4. **The demo** (5 min) — below.
5. **Early evaluation** (3 min) — the numbers from [[06 - Evaluation Plan]]: citation precision vs WikiCrow/human-Wikipedia anchors, review minutes/article vs Dzongkha's manual baseline (5 months → 80 articles), cost/article.
6. **The model for other languages** (2 min) — Welsh precedent; Content Translation's lower-deletion-rate evidence; what a Class-0/1 language needs to replicate this (sources + a small editor community + one steward institution).

## Demo — offline-first (decision already made; don't relitigate at the venue)

**Why offline-first:** venue wifi at The Soaltee unconfirmed (IATS announcements say nothing about AV/internet; email sent — see [[07 - Roadmap to August]]); Nepal's Sept 2025 protest-era platform blocks show tail risk. APIs are reachable from Nepal in principle (Anthropic and OpenAI both list Nepal as supported), so a live run is a *bonus*, not the plan.

**Primary: recorded run-through (3–4 min video, no audio dependency)**
1. Start with a term stub (e.g. སྟོང་པ་ཉིད། — raw transclusions only).
2. Show the extraction table row for the term (verbatim commentary passages, block IDs).
3. Run the drafting step; show the article forming with layered citations.
4. Human review moment: show a real edit (a caught error is *gold* — it demonstrates the gate working).
5. Wikitext conversion → the article live on bo.wikipedia (uploaded in week 3).
6. Punchline: ask an AI answer-engine a question in Tibetan that the new article answers — show the article surfacing. (Pre-record; cache the result.)

**Cached fallbacks:** all intermediate files local; the two finished articles + the live bo.wikipedia URLs as screenshots; the full video also as a PDF slide sequence in case video playback fails.

## Tibetan rendering — known pitfalls (test everything before travel)

- **Slides:** PowerPoint font embedding is unreliable for complex scripts. Embed Noto Serif Tibetan or Jomolhari, then **export a PDF of every Tibetan-bearing slide** as the canonical backup. Test on the actual presentation laptop AND an external projector (different rendering path).
- **Known font bugs:** Noto Serif Tibetan v2.001 renders the stack དྡྷི incorrectly; Jomolhari renders ཨཱརྻ incorrectly on macOS specifically. Scan the demo articles for these stacks; swap font per-slide if needed.
- **Web/browser:** Tibetan line-breaking (break only after tsheg ་ U+0F0B) is poorly supported — Android fallbacks especially; Firefox only fixed non-wrapping in 2020. Check the uploaded bo.wikipedia articles on mobile; MediaWiki's Universal Language Selector serves Jomolhari as the default `bo` webfont but users may need to enable webfonts.
- If projecting a live browser: zoom to ≥150% — Tibetan stacks are vertically dense and unreadable at default sizes from the back of a room.

## Questions to expect (prepare one-slide answers in backup)

1. *"Isn't AI-generated content banned on Wikipedia now?"* → en-wiki guideline + G15 verified facts; our machine-drafted/human-published design is what those rules demand; bo.wiki plan in [[05 - Wikipedia Policy and Community Strategy]].
2. *"Did you ask the Tibetan Wikipedia community?"* → the village-pump proposal (posted, linked), and the fact that bo.wiki's only human admin is OpenPecha-affiliated — stewardship, formalized publicly.
3. *"Won't this pollute the training data for Tibetan?"* → doom-spiral rebuttal ([[01 - Paper Argument and Structure]]): verification flips the sign; CX deletion-rate evidence.
4. *"Can LLMs even write good Tibetan?"* → honest answer: frontier models are weak (TLUE); our pipeline compensates with grounding in Tibetan-language sources + native review; show HTER/acceptance numbers.
5. *"Why not just translate English Wikipedia?"* → MinT/NLLB Tibetan quality near zero; translation inherits English framing of Tibetan topics; our articles are born from the Tibetan commentary tradition — a Tibetan-studies-native argument the audience will like.
6. *"What about hallucinated citations?"* → G15-proof-by-construction checklist + citation-audit numbers.
7. *"Who pays for this long-term?"* → cost slide: ~$0.12–0.60 API/article; reviewer-minutes are the real cost; Rapid Fund + Welsh/Dzongkha funding precedents.
8. *"What about non-Buddhist topics?"* (fair!) → the pipeline is source-anchored; it extends wherever citable Tibetan-language or Tibetan-studies sources exist (Treasury of Lives biographies, geography, science topics from academic sources). Buddhist texts are the beachhead because the source infrastructure (BDRC, 84000) is richest there.

## Materials checklist

- [ ] Slides (PPTX + full PDF backup) — fonts embedded
- [ ] Demo video (MP4, local) + PDF slide sequence fallback
- [ ] Live URLs list (bo.wikipedia articles, project page) + screenshots
- [ ] Backup-answer slides (the 8 questions above)
- [ ] USB stick + cloud + email-to-self copies
- [ ] One-page handout with QR to the project page (optional but effective at IATS)
