---
name: wiki-article-from-claims-v2
description: Draft a readable, encyclopedic Tibetan Wikipedia article from one consolidated claims topic page — wikivoice prose, at most 3 refs per statement, at most 2 commentary quotations per article, sentence-final shad / paragraph-final double shad (།།) with no commas, in-prose author names from the human-curated author_in_use key — plus a generated read-only footnote preview for reviewers; same claim-resolution chain and quotation verification as wiki-article-from-claims.
---

# wiki-article-from-claims-v2

Successor candidate to [`wiki-article-from-claims`](../wiki-article-from-claims/SKILL.md), created 2026-08-18 in response to the Tibetan-linguist review of the 43-article term-article batch. The reviewer found three problems with v1 output: (1) inline `<ref>` tags carrying full Tibetan author + title make the raw wikitext unreadable during review; (2) consensus statements carry more citations than they need; (3) the articles read as claims stitched together — "Commentator X says '…'. Commentator Y likewise says '…'" — a literature review, not an encyclopedia article. This skill keeps v1's entire trust machinery unchanged (claims-only drafting, the fixed claim-resolution chain, verbatim-or-absent quotations, character-for-character verification, the wikitext spec's blocking validators) and changes only the **register** of the prose and the **presentation** for reviewers. Correct output is an article a Tibetan reader experiences as connected encyclopedic prose in wikivoice, with commentator names appearing only where positions genuinely diverge; a `citations.md` that still lets a reviewer trace every ref to claim IDs and source blocks; and an `article-preview.md` the reviewer can read in Obsidian with citations collapsed to footnote superscripts.

A second linguist review round on 2026-08-18 (of the Mode B pilot output) added three requirements, carried here as Rules 15–17: the Tibetan punctuation contract (sentence-final shad, paragraph-final double shad, no commas anywhere) and in-prose author naming via the human-curated `author_in_use` frontmatter key.

v1 remains the skill of record until the human contributor retires it. This skill writes vault files only; it never publishes — publishing stays behind the pipeline's `/publish` gate.

---

## Inputs

1. **Topic ID(s)** — one of:
   - a spine slot ID from the registry in `4-SYSTEM/Guidelines/vault-annex.md` §2a (e.g. `tara-01`, `origin`; the two multi-topic cases `structure`+`benefits` and `origin` work exactly as in v1), **or**
   - a keyword/term topic (e.g. `mudra`, `lotus`) whose consolidated page exists at `2-RAILS/Claims/<topic>.md`.

   If the consolidated page for a requested topic does not exist, stop and report — never substitute another page.
2. **The consolidated page's raw sources** — every file listed in its `sources:` frontmatter (paths under `2-RAILS/Claims/raw/tree-guided/`). These resolve claim IDs to བོད་ཡིག, English gloss, and `Cite:` targets. If a listed file is missing, stop and report.
3. **The wikitext output contract** — `4-SYSTEM/Pipelines/wikipedia/docs/reference/wikitext-spec.md`. Read it in full before drafting; its blocking validator rules (V1–V12) are this skill's acceptance criteria, exactly as in v1.
4. **Commentary metadata** — from each raw claims file's own frontmatter (`author`, `title`, `author_in_use`, `author_in_english`/`title_in_english` where present). If a raw claims file predates the `author_in_use` key, read that one key from the frontmatter of the commentary named in its `source_file` — a metadata-only lookup, never a reason to reopen the commentary body. Never from memory.

## Output

Three files per article:

```
3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/<topic>/article.md          (keyword topics)
3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/<topic>/citations.md
3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/<topic>/article-preview.md

3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/article.md          (spine-slot topics)
3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/citations.md
3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/article-preview.md
```

`article.md` keeps v1's Obsidian-viewability convention: YAML frontmatter (`topic`, `article_kind`, `format`, `status`), an explanatory callout, and the publishable wikitext inside a single ```` ```wikitext ```` fence — byte-identical to what would be published. Reviewers who need the wiki markup edit **inside the fence only**.

`article-preview.md` is **generated, read-only output** — produced by `scripts/make_preview.py` from `article.md`, never hand-edited, regenerated after every edit to `article.md`. It exists solely so a human reviewer can read the article in Obsidian's reading view with citations rendered as clickable footnote superscripts (`[^sungrab-tulku]`) instead of inline `<ref>` blocks. It is not published, not cited from anywhere, and carries `generated: true` frontmatter plus a warning callout. The script also runs standalone on any existing v1 `article.md`, so previews can be produced for already-drafted articles without redrafting them.

### `citations.md` — the audit trail

Same format as v1 (reference map table, claims used but not quoted, unresolvable attestations, warnings, verification), with one addition — because the article now cites only representative sources, the full support must be preserved here:

```markdown
## Full attestation beyond in-article refs

<for each consensus statement cited to 2–3 representative refs: the claim IDs of every OTHER
commentary that also attests it, so no attestation is lost by the citation cap>
```

---

## Output file format

The wikitext skeleton is unchanged from v1: the doctrinal-term skeleton of the wikitext spec §1 for keyword topics, v1's deity-profile adaptation for `tara-01`…`tara-21`, and v1's work-article adaptation for `structure`+`benefits`. Section headings remain a menu, not a quota — emit a section only when the consolidated page attests material for it. The lead has no heading; the last three sections are fixed and ordered: `འབྲེལ་ཡོད་ཤོག་ངོས།` → `ལུང་ཁུངས།` → `དཔྱད་གཞིའི་ཡིག་ཆ།`.

### `article-preview.md` format (written by the script, shown for reference)

```markdown
---
topic: <topic>
article_kind: term-article-preview
generated: true
generated_from: article.md
generated_by: 4-SYSTEM/Skills/wiki-article-from-claims-v2/scripts/make_preview.py
---

> [!warning] Generated preview — do not edit
> This file is rendered from `article.md` for review reading only. Citations appear as
> footnotes. Any correction belongs in `article.md` (inside the wikitext fence); then
> regenerate this preview. This file is never published.

**<NAME>**ནི་ … <lead prose>[^sungrab-tulku]

## ངེས་ཚིག
… <body prose with footnote markers> …

[^sungrab-tulku]: འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ། སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་རྣམ་བཤད།
```

---

## Rules

Rules 1–4 and 10–14 are v1's machinery, unchanged. Rules 5–9 are this skill's reason to exist — the style delta. Rules 15–17 are the 2026-08-18 second-round linguist feedback: the punctuation contract and the author-naming rule.

1. **Claims-only drafting.** Every statement in the article body traces to a claim on the consolidated topic page. No parametric knowledge — no dates, Sanskrit forms, iconographic details, or doctrinal framings that are not in a claim. If it cannot be cited, it does not go in.
2. **The resolution chain is fixed.** Consolidated attestation `commentary:claim-id` → that commentary's file under `2-RAILS/Claims/raw/tree-guided/` → the claim's **བོད་ཡིག**, English gloss, and `Cite:` target. An attestation that does not resolve is dropped and logged under *Unresolvable attestations* — never guessed, never cited anyway.
3. **Quotations are verbatim or absent.** Direct quotations come only from the **བོད་ཡིག** field of a resolved claim, character-for-character, wrapped in `" "`, each followed immediately by its `<ref>`.
4. **Every quotation is verified before completion** — located character-for-character (whitespace-collapsed) in the `1-SOURCES/` file its claim's `Cite:` names, PASS/FAIL recorded per quote in `citations.md`. A FAIL is fixed or the quotation removed.
5. **Wikivoice for consensus.** ⭐ Any claim the consolidated page marks as consensus (or majority-attested and uncontested) is stated as plain declarative fact — no commentator names, no "མཁས་པ་མང་པོས་…བཤད" / "…གིས་གསུངས" framing, no quotation. The sentence asserts; the `<ref>`s carry the support. Inline attribution ("ཏཱ་ར་ནཱ་ཐས་…") is **reserved** for ⚑ divergences (every position attributed, as in v1) and for unique claims worth including. Attribution-heavy material concentrates in `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`; the other sections stay in wikivoice.
6. **Quotation budget: at most 2 verbatim commentary quotations per article.** ⭐ Spend them only where the exact wording is itself the point (a contested formulation, a definition whose phrasing matters). Root-text verse quotation in the lead (v1's practice for deity articles) does not count against the budget. Everything else is paraphrased into prose — still claim-backed, still cited.
7. **Citation cap: at most 3 `<ref>`s on any statement.** ⭐ For consensus claims, cite 2–3 *representative* commentaries — prefer refs already named elsewhere in the article, so the reference list stays compact. Never attach the full attestation set to a sentence. Attestation breadth may be asserted in prose ("འགྲེལ་པ་བཅུ་དྲུག་ཀ་…") when the consolidated page's count supports it, backed by 2–3 refs; the complete list of supporting claim IDs goes in `citations.md` §*Full attestation beyond in-article refs*, so nothing is lost.
8. **Prose before fragments.** ⭐ Draft each section as connected paragraphs with topic sentences, not one-claim-one-sentence sequences. Merging several related claims into one flowing sentence is encouraged — the sentence then cites the union's representative refs (still ≤3). Connective tissue (discourse markers, transitions) needs no citation but must carry zero factual content.
9. **Readability is a completion criterion.** ⭐ Before verification, reread the whole article start to finish as a Tibetan encyclopedia reader: if any passage reads as a list of who-said-what outside the divergence section, redraft it under Rules 5–8.
10. **Due weight follows attestation counts** — consensus forms the backbone, unique claims are attributed inline, ⚑ divergences present every position with attribution, never flattened, never adjudicated.
11. **Ref form, spec mechanics, and tail are v1's**: hand-formatted `<ref><AUTHOR>། <TITLE>།</ref>` from raw-file frontmatter, named refs on reuse, `== ལུང་ཁུངས། ==` + `<references />` (never `{{Reflist}}`), Tibetan-only body, tsheg boundaries, ≥1 citation per section, allowlisted category, fixed last-three-section order, no fabricated URLs. Validator rules V1–V12 are blocking.
12. **The preview is derived, never authored.** `article-preview.md` is written only by `scripts/make_preview.py`. Never hand-edit it; never edit it in place of `article.md`; regenerate it after any change to `article.md`. It is excluded from the citation chain and from publishing.
13. **Read-only outside the output folder.** This skill never modifies `1-SOURCES/`, `2-RAILS/`, or anything in `4-SYSTEM/`. It writes only under the topic's output folder.
14. **Output is always `status: draft`**; the consolidated page's `status` is recorded as `rails_status` in `citations.md`, with a prominent warning when it is not `complete`. No publishing, no network.
15. **Sentence-final shad, paragraph-final double shad.** ⭐ Every Tibetan sentence in the body ends with a shad `།`. The final sentence of every paragraph — including the lead and single-sentence paragraphs — ends with a double shad `།།` (ཉིས་ཤད). Where classical orthography adjusts the shad after particular final letters (a bare ང takes tsheg + shad: `…ང་།`; a final ཀ or ག suppresses the immediately following shad), follow the practice attested in the source commentaries themselves — never improvise an orthographic rule. Punctuation always comes **before** the `<ref>` tag(s) it closes over: `…བཤད།<ref … />`, never `…བཤད<ref … />།`.
16. **No commas — the character does not exist in Tibetan.** ⭐ Neither ASCII `,` nor any comma variant (`，`, `、`) may appear anywhere in the fence body. At every point where a draft reaches for a comma: if the position is a genuine clause or sentence boundary, write a shad `།`; if it is not, write nothing and let the tsheg-joined syntax carry the connection. The pilot batch's `<ref name="…" />,` pattern is always wrong — delete the comma, and when a boundary is needed there, place the shad before the refs (Rule 15). Latin punctuation survives only inside `<ref>` content, per the spec.
17. **In-prose author names come from `author_in_use`.** ⭐ Wherever the prose names a commentator — unique claims, ⚑ divergence positions, `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།` — use that commentary's `author_in_use` frontmatter value: the human-curated, respectful in-article form of the name (e.g. རྒྱལ་བ་དགེ་འདུན་གྲུབ་, not the bare catalog name, not the `registered_id`, not a romanisation), with whatever grammatical particle the sentence requires appended after it. Never invent, translate, or upgrade an honorific — `author_in_use` is authored and reviewed by a human contributor in the source commentary's frontmatter, and the model's only job is to copy it. Resolution order: the raw claims file's `author_in_use` → (frontmatter-only lookup) the `source_file` commentary's own frontmatter → if absent in both, fall back to `author` verbatim **and** add a line to `citations.md` §Warnings naming the commentary whose `author_in_use` is missing. `<ref>` content and the `དཔྱད་གཞིའི་ཡིག་ཆ།` bullets keep the formal `author` + `title` unchanged — `author_in_use` is for prose mentions only.

---

## Procedure — Mode A (full draft from the consolidated claims page)

Use Mode A when no article exists yet for the topic, or when the consolidated claims page has changed materially since the last draft.

1. **Load the contracts.** Read `4-SYSTEM/Pipelines/wikipedia/docs/reference/wikitext-spec.md` in full. Read the consolidated page `2-RAILS/Claims/<topic>.md` in full; record its `status` and `sources:` list. For a multi-topic article, read every constituent page.
2. **Build the claim-resolution table** — exactly as v1: every attestation ID on the consolidated page resolved through its raw tree-guided file to བོད་ཡིག, English gloss, `Cite:` path + block ID, and author/title/`author_in_use` frontmatter (with the Input 4 fallback for raw files that predate the key). Record unresolvables before drafting a single sentence.
3. **Classify for register.** Mark each claim: **backbone** (consensus/majority, uncontested → wikivoice, Rule 5), **unique-attributed** (worth including, attributed inline), or **⚑ divergence** (destined for `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`, every position attributed). Select the ≤2 quotations the article will carry (Rule 6) and, for each backbone statement, its 2–3 representative refs (Rule 7) — preferring commentaries that recur across statements.
4. **Outline, then draft.** Map the consolidated page's sections onto the skeleton. Draft the lead (bold name, identification, one–two cited sentences). Draft each body section as connected wikivoice prose per Rules 5–8, attaching ≤3 refs per statement; put attributed material where Rule 5 sends it. Apply the punctuation contract (Rules 15–16) and the `author_in_use` naming rule (Rule 17) as you draft, not as an afterthought.
5. **Readability pass** (Rule 9): reread the full article; redraft any who-said-what passage outside the divergence section.
6. **Assemble the tail** — related pages (targets end in tsheg; red links expected), `ལུང་ཁུངས།` + `<references />`, `དཔྱད་གཞིའི་ཡིག་ཆ།` (one bullet per commentary actually cited), one allowlisted category.
7. **Write `citations.md`** — v1's format plus §*Full attestation beyond in-article refs* for every capped consensus statement.
8. **Verify** — (a) every quotation character-for-character against its cited `1-SOURCES/` file, PASS/FAIL recorded; (b) every `<ref>` appears in the reference map; (c) walk validator rules V1–V12 against the fence body; (d) style self-check: no statement carries >3 refs, ≤2 commentary quotations in the whole article, no inline attribution of consensus material; (e) punctuation walk: no comma character anywhere in the fence body, every paragraph ends with `།།`, no punctuation after a `<ref>` tag; (f) naming walk: every in-prose commentator name is an `author_in_use` value (or the logged `author` fallback).
9. **Generate the preview.** Run `python3 4-SYSTEM/Skills/wiki-article-from-claims-v2/scripts/make_preview.py <path-to-article.md>` — it writes `article-preview.md` beside the article. Confirm the preview opens clean in Obsidian terms: no `<ref>` tags remaining, no `[[…]]` vault links leaked from wikitext, footnotes present for every named ref.
10. **Report.** State the three files written, rails_status, counts (refs, quotations, backbone vs attributed statements), verification results, and every warning — the human reviewer decides what happens next.

---

## Procedure — Mode B (revision-in-place from an existing v1/v2 article)

Use Mode B when a verified `article.md` + `citations.md` already exists for the topic (produced by `wiki-article-from-claims` or this skill) and only the **register** needs to change — not the facts. Mode B never returns to `2-RAILS/Claims/` or the raw tree-guided files: the existing claim-resolution and quote-verification work is treated as settled, which is what makes it far cheaper than Mode A. One exception: resolving `author_in_use` (Rule 17) may read the **frontmatter only** of the raw claims files or their `source_file` commentaries — metadata lookup, never claim content.

**Inputs (replace Mode A's Inputs 1–2):** the existing `article.md` (fenced wikitext) and `citations.md` for the topic.

**Output, during piloting:** write to `3-TRANSFORMATIONS/Wikipedia/tara21/work/pilot-v2/<topic>/{article.md,citations.md,article-preview.md}` — never overwrite the source article while it is still under human review. Only after a human contributor approves a pilot does promoting the file to the topic's real `term-articles/`/`slot-articles/` path become an option, and that promotion is a human decision, not something this skill does on its own.

1. **Read the source.** Load the existing `article.md` fence body and `citations.md` reference map in full. Every claim ID, quotation, and `Cite:` target already there is verified ground truth — do not re-derive it.
2. **Classify existing statements** per Rule 5: content already in `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།` (or attributed to one commentator making a genuinely distinctive point) stays attributed; everything else is a candidate for wikivoice conversion.
3. **Rewrite for register.** Merge one-claim-one-sentence sequences into connected wikivoice prose (Rules 5, 8), applying the punctuation contract (Rules 15–16) and swapping every in-prose commentator name to its `author_in_use` form (Rule 17) as you go. The rewrite may only use claim IDs that already appear in the source `citations.md` — introducing a new claim ID in Mode B is not permitted; that requires Mode A.
4. **Apply the quotation budget (Rule 6).** Keep at most 2 verbatim quotations in the whole article. For every quotation cut, convert its content to paraphrase using the same claim's English gloss / meaning already on record — never invent phrasing not grounded in the existing claim.
5. **Apply the citation cap (Rule 7).** Where a statement carries more than 3 refs, keep the 2–3 most representative (prefer refs already reused elsewhere in the article) and move the rest into a new `citations.md` section, *Full attestation beyond in-article refs*, keyed by the statement they support.
6. **Spot-verify, don't re-verify from scratch.** For each of the ≤2 quotations retained, confirm it is an unchanged, exact substring of the quotation already marked PASS in the source `citations.md` — a text diff, not a fresh `1-SOURCES/` lookup. Do not touch quotations that are being removed; they need no re-check.
7. **Readability + punctuation pass (Rules 9, 15–17).** Reread start to finish; redraft any remaining who-said-what fragment sequence outside the divergence section. Then walk the punctuation contract: no comma anywhere, every paragraph closed with `།།`, no punctuation after a `<ref>` tag, every in-prose name an `author_in_use` value.
8. **Write the revised `citations.md`** — carry forward the source file's reference map and verification table unchanged for retained refs, add *Full attestation beyond in-article refs*, and add a header noting `revision_mode: B`, the source article's path, and revision date.
9. **Generate the preview**: `python3 4-SYSTEM/Skills/wiki-article-from-claims-v2/scripts/make_preview.py <path-to-revised-article.md>`.
10. **Report** the topic, source path, output path, ref-count and quotation-count before/after, and confirmation that no claim ID appears in the revision that wasn't already in the source `citations.md`.

---

## Completion check

- [ ] `article.md`, `citations.md`, and `article-preview.md` written under the topic's output folder; nothing outside it modified; nothing published
- [ ] Every statement traces to a claim on the consolidated page (no parametric additions); unresolvables listed and unused
- [ ] Every quotation verified character-for-character with PASS recorded; **at most 2 commentary quotations in the article**
- [ ] **No statement carries more than 3 refs**; capped consensus statements have their remaining attestations listed in `citations.md` §Full attestation beyond in-article refs
- [ ] **Consensus material is in wikivoice** — inline commentator attribution appears only on unique claims and in the divergence section; ⚑ divergences all-positions-attributed, never flattened
- [ ] Readability pass done: article reads as connected encyclopedic prose start to finish
- [ ] **Punctuation contract holds**: no comma character anywhere in the fence body; every sentence ends with a shad `།`; every paragraph ends with a double shad `།།`; punctuation precedes `<ref>` tags, never follows them
- [ ] **Every in-prose commentator name is that commentary's `author_in_use`** — or the `author` fallback with a warning line in `citations.md` naming the commentary whose key is missing
- [ ] Spec validator rules V1–V12 walked and passing; `<references />` present; allowlisted category; fixed tail order
- [ ] `article-preview.md` generated by the script (not hand-written), carries `generated: true` + warning callout, contains no `<ref>` tags and no wikitext `[[…]]` links
- [ ] `citations.md` frontmatter records `context_packages`, `rails_status`, `status: draft`; warnings list rails_status if not `complete` and every ref missing year/page/URL
