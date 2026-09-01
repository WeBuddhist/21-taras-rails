# Wikipedia Policy and Community Strategy

The paper will be judged partly on whether the pipeline is *community-legitimate*. This note has the verified rules, the failure modes, and the concrete bo.wikipedia plan. (Policy facts verified directly on-wiki 2026-07-24 — several press accounts are wrong; use these names/dates.)

## The rules as they actually stand (July 2026)

**English Wikipedia** (doesn't bind bo.wikipedia, but it's the reference standard reviewers apply):
- **"Wikipedia:Writing articles with large language models"** — a **content guideline** (Nov 2025; amendments RfC closed 20 Mar 2026, 44–2 under WP:SNOW): don't use LLMs to generate or rewrite article content. Two exceptions: copyediting your own writing; LLM-assisted translation with human verification. Persistent misuse → blocks.
- **"Wikipedia:Large language models"** — an information page, explicitly *not* policy. (Do not cite a "Large language model policy" page — that name is wrong.)
- **CSD G15** (RfC closed 21 Jul 2025; adopted 4 Aug 2025): speedy deletion of LLM pages *without human review*, triggered by objective tells — leftover chatbot text, or non-existent/nonsensical references (fabricated sources, dead links, invalid ISBNs/DOIs, wrong metadata). "Sounding like AI" is not enough.
- **WikiProject AI Cleanup** (~286 participants): tags and removes AI text; publishes the "Signs of AI writing" guide. Stated purpose is verification, not prohibition.
- **WP:MASSCREATE / ArbCom "Article creation at scale":** mass creation needs prior community consensus, and every mass-created article must cite ≥1 independent, reliable, **secondary** source with significant coverage.
- Other editions moved the same way in 2025–26: FR, IT, PT, ES, DE, RU all restrict LLM generation. **bo.wikipedia has no AI policy at all** — but the policy vacuum is not permission; the global bot policy (which bo.wiki adopted in 2011) requires local community approval for anything automated, and "no local community" means *stop*, not *proceed*.

**Wikimedia Foundation:** April 2025 AI strategy — AI to *support* editors, never replace them; explicitly names "automating translation and adaptation of common topics" for underserved languages. The pipeline aligns with this — cite it. Counter-lesson: WMF's own AI article-summaries trial (June 2025) was killed by editor backlash *within days* even though outputs were labeled. Labels don't buy forgiveness; prior consent does. (Context: community–WMF trust is currently strained — 2026 layoffs triggered an 800+ editor strike pledge. That dispute is about WMF governance, not LLM policy — don't conflate them.)

## What "proper citations" means operationally

From WP:V + G15: (1) the source exists and resolves; (2) metadata correct; (3) the cited passage actually supports the sentence; (4) the source is reliable — published, independent, fact-checked; non-English sources explicitly permitted; **open wikis are not reliable sources** (Rigpa Wiki, Buddha-Nature, Tibetan Buddhist Encyclopedia — research aids only); **AI-generated sources are unreliable by policy**. The burden of verifiability lies with the human who clicks publish — which is exactly our design ([[03 - Pipeline Design]]).

## The failure modes we must be visibly different from

| Case | What happened | Our design answer |
|---|---|---|
| Scots Wikipedia (2020) | Non-speaker wrote ⅓ of the wiki; credibility of wiki *and language* damaged | Native-speaker review is mandatory, named, and measured |
| Lsjbot / Cebuano | Millions of bot stubs, ~no human community; repeated closure proposals | Throughput bounded by review capacity; quality over count |
| **Greenlandic Wikipedia — closed 2025** | MT-flooded, no native contributors; LangCom shut the whole project | Community capacity-building is part of the project, not an afterthought |
| en-wiki MT purge (2016) | 95% of raw-MT articles unacceptable; tool restricted | We are not MT; grounding + review by construction |
| Indonesian MT revolt | Community demanded MT removal; resolved by a negotiated 95%-modification threshold | Community-negotiated limits — propose them ourselves, first |

## bo.wikipedia reconnaissance (via MediaWiki API, July 2026) — and the surprise

- 8,072 articles; 31 active users; 25 bots; **2 admins: `Abuse filter` (system) and `Pecha-G.Dhargyal`** — i.e., **the wiki's only human administrator is an OpenPecha-affiliated account**, active (last edit 25 Jun 2026; sandbox drafting activity Apr 2026).
- Second OpenPecha footprint: `Pecha-Tsewang` went through RfA (July 2025), credited with leading a "Tibetan Buddhist Studies Wiki Project" and mentoring editors.
- The wiki is small but alive: daily Recent Changes activity; most active editor `Tsampaeater`.

**How to play this:** it flips the Greenlandic-style consent objection — OpenPecha doesn't merely "have contact with" the community; it *is* the community's stewardship. But insider position must read as stewardship, not circumvention. So:

## The community-consent plan (do this before August — it becomes a slide)

1. **Post a public project proposal on the bo.wikipedia village pump** (bilingual bo/en): scope (10–15 fully-cited articles on Buddhist-studies topics), method (machine-drafted, human-published), disclosure plan, named reviewers, invitation to object/join. Have it posted by `Pecha-G.Dhargyal` or the project account with explicit OpenPecha affiliation.
2. **Create an on-wiki project page** listing every pipeline-assisted article, its reviewer, and its sources — the Content Translation trackability model.
3. **Disclose in every edit summary** and with a talk-page template on each article.
4. **Engage the active editors by name** (`Tsampaeater` and other recent contributors) — invite them as reviewers/raters (they're also candidates for the evaluation panel, see [[06 - Evaluation Plan]]).
5. **Voluntarily adopt the en-wiki mass-creation standard**: ≥1 independent secondary source per article. Strongest defensible stance, and it feeds topic selection.
6. Longer-term: propose a lightweight local guideline for machine-assisted content on bo.wikipedia (threshold model à la Indonesian CX) — a deliverable *beyond* the paper that makes OpenPecha the policy steward, not just a content producer.

## ⚠ Topic notability check (open item)

No independent secondary coverage was found for **ཟབ་མོ་སྣང་བ།** ("zab mo snang ba") as a standalone topic — searches only surface the *similar* «Zab mo nang don» (Rangjung Dorje's Profound Inner Meaning, which HAS coverage). Two actions: (a) verify the vault title isn't actually Zab mo nang don; (b) if it is genuinely the Heart Sutra samādhi, it may still work as a *section* of the Heart Sutra article rather than a standalone page — or keep it as the *pipeline demo* while choosing better-covered topics for upload. Every planned article needs its Treasury of Lives / academic citation identified **before** drafting.

## Do's and don'ts (compressed for the talk)

**Do:** consent before content · bound generation by review capacity · G15-proof citations by construction · disclose everything · align with WMF's 2025 AI strategy · report deletion-rate-vs-baseline as the legitimacy metric.
**Don't:** publish unreviewed output (even labeled) · optimize article count · run translation-shaped generation without native fluency in the loop · claim the training-data cycle is automatically virtuous (it flips sign only under verification) · treat bo.wiki's policy vacuum as permission.
