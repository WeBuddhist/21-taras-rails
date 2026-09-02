# Roadmap to August — Week by Week

Today: **Thu 24 July 2026**. Conference: **23–29 August 2026, Kathmandu**. Four working weeks + travel.

## Week 1 — Jul 24–31: Decisions, consent, setup

**Security first (30 min):**
- [ ] Redact the hardcoded Obsidian REST API key + LAN host in `WeBuddhist/webuddhist-term-extractor-updated-SKILL.md` (line 27); rotate the key.
- [ ] Deal with the previously-flagged WeBuddhist credentials in the rails plan-uploader (rotation was already recommended 2026-07-19).

**Community + logistics (the long-lead items — start now):**
- [ ] Draft + post the bilingual village-pump proposal on bo.wikipedia (template in [[05 - Wikipedia Policy and Community Strategy]]). Coordinate with `Pecha-G.Dhargyal`.
- [ ] Email iats2026@conftool.com: session AV (projector, HDMI), wifi availability, session length/format.
- [ ] Begin rater recruitment (3 native speakers — RYI is the co-host, use that channel; also Monlam AI, Esukhia, `Tsampaeater`).
- [ ] Check Wikimedia Rapid Fund ($500–5k, 45-day turnaround) — even an *application in progress* is a sustainability slide bullet.

**Paper/pipeline decisions:**
- [ ] Finalize the 15-topic list; verify ≥1 independent secondary source each (resolve the ཟབ་མོ་སྣང་བ། question — verify spelling vs «Zab mo nang don»).
- [ ] Build the source→external-ID mapping table for the 16 Heart Sutra sources (BDRC IDs, 84000 URLs, ToL, academic editions) — a few hours of librarian work that upgrades every downstream citation.
- [ ] Instrument time logging in the drafting workflow (start of every productivity number).
- [ ] Draft the paper skeleton from [[01 - Paper Argument and Structure]].

## Week 2 — Aug 1–8: Generation sprint + last mile

- [ ] Run the pipeline: draft the ~13 new Tibetan articles (extraction layer already exists for Heart Sutra terms). Log times.
- [ ] Write the vault→wikitext converter (deterministic script: headers, wikilinks, `<ref>` citation templates, reflist, disclosure template). Test on the 2 finished articles.
- [ ] First human-review pass on drafts (log edit time; snapshot pre/post versions for HTER).
- [ ] Finalize rubric + audit sheets (bo/en); confirm the 3 raters and schedule their week-3 window.
- [ ] Paper: write Introduction, Related Work, Pipeline sections (material is ready in [[04 - Related Work and Landscape]] and [[03 - Pipeline Design]]).

## Week 3 — Aug 9–16: Evaluation + upload

- [ ] Raters run: rubric (all articles), pairwise A/B (stub topics), citation audit (~10 statements/article, AIS protocol, 30% double-coded).
- [ ] Compute: means ± sd, Krippendorff's α, citation precision, uncited rate, hallucination rate, HTER (botok syllables), time/article, acceptance rates, Lift Wing quality scores.
- [ ] **Upload the reviewed articles to bo.wikipedia** with full disclosure (edit summaries + talk-page template + project page). This is the moment the paper's title becomes literally true.
- [ ] Paper: Evaluation + Discussion sections; full draft complete by Aug 16.

## Week 4 — Aug 17–22: Talk, demo, travel prep

- [ ] Slides (structure in [[08 - Presentation and Demo Plan]]). Embed Jomolhari/Noto Serif Tibetan; **export PDF backup of every slide containing Tibetan** (PowerPoint font embedding is unreliable for complex scripts).
- [ ] Record the offline demo video (pipeline run-through, one term end-to-end); cache all outputs locally.
- [ ] Test Tibetan rendering on the actual presentation laptop + a projector; test the live bo.wikipedia articles on mobile.
- [ ] Dry-run the talk once with a timer.
- [ ] Print/backup: slides PDF on USB + cloud + email to self.

## Aug 23–29: 17th IATS Seminar, The Soaltee Kathmandu

- Live demo only if venue wifi proves solid; video is the primary plan ([[08 - Presentation and Demo Plan]]).
- Collect contacts: potential reviewers/editors among Tibetan-studies scholars are the recruitment pipeline for the post-conference phase.

## Scope guards (what NOT to attempt before August)

- No bot/API mass-upload tooling — manual uploads of ~15 reviewed articles are fine and *safer* optically.
- No new text corpora or new rails — Heart Sutra assets are sufficient.
- No perfect wikitext converter — handle the 15 articles, not the general case.
- If time collapses: the minimum viable evaluation (5 articles, statement audit) in [[06 - Evaluation Plan]] still fulfills the abstract.

## After the conference (parking lot)

- Wikimedia Rapid Fund application → funded pilot with recruited editors.
- Lightweight bo.wikipedia machine-assisted-content guideline (threshold model) — OpenPecha as policy steward.
- Scale beyond Heart Sutra terms (Tārā, BCA concepts, Treasury of Lives-backed biographies).
- Write up as a full paper (venue ideas: ACL workshop on NLP for under-resourced languages, Wiki Workshop, JIATS).
