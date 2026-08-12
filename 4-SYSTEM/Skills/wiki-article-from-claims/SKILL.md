---
name: wiki-article-from-claims
description: Draft a cited Tibetan Wikipedia article from one consolidated claims topic page, resolving every citation through raw claim IDs to verbatim commentary quotations and verifying each quotation against 1-SOURCES.
---

# wiki-article-from-claims

Produces a publish-ready Tibetan wikitext article for one canonical spine slot (e.g. `tara-01`) from its consolidated claims topic page in `2-RAILS/Claims/`. The consolidated page supplies the facts (consensus + ⚑ divergences + unique claims, in English, with attestation counts); the raw tree-guided claims files supply the verbatim Tibetan (**བོད་ཡིག**) and the `1-SOURCES/` block citations behind every attestation. The skill exists so that article prose is never drafted from source files directly and never from parametric knowledge — the failure modes it prevents are added facts, flattened divergences, and quotations that are not character-for-character real. Correct output is an `article.md` (fenced wikitext) whose fence body passes every blocking rule of the wikitext spec, plus a `citations.md` that lets a reviewer trace every `<ref>` back to claim IDs and source blocks without opening the model's head.

This skill writes vault files only. It never publishes — publishing stays behind the pipeline's `/publish` gate.

---

## Inputs

1. **Topic slot ID(s)** — one slot ID from the registry in `4-SYSTEM/Guidelines/vault-annex.md` §2a (e.g. `tara-01`, `origin`). The consolidated page `2-RAILS/Claims/<topic>.md` must exist. Two documented multi-topic cases:
   - `structure` + `benefits` together → one article on the root text itself (a *work* article, not a deity article).
   - `origin` (optionally with the origin material in `tara-01`) → the article on Tārā the deity.
   If the page for a requested topic does not exist, stop and report — do not substitute another page.
2. **The consolidated page's raw sources** — every file listed in its `sources:` frontmatter (paths under `2-RAILS/Claims/raw/tree-guided/`). These resolve claim IDs to བོད་ཡིག, English gloss, and `Cite:` targets. If a listed file is missing, stop and report.
3. **The wikitext output contract** — `4-SYSTEM/Pipelines/wikipedia/docs/reference/wikitext-spec.md`. Read it in full before drafting; its blocking validator rules (V1–V12) are this skill's acceptance criteria.
4. **Commentary metadata** — taken from each raw claims file's own frontmatter (`author`, `title`, and `author_in_english`/`title_in_english` where present). Never from memory.

## Output

Two files per article, in a dedicated folder that does not collide with the kwiki ledger's `articles/` layout:

```
3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/article.md
3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/citations.md
```

**Obsidian-viewability convention (2026-08-12, human contributor decision):** the article file is `.md`, not `.wiki`, so it is viewable and reviewable inside Obsidian. It consists of a small YAML frontmatter (`topic`, `article_kind`, `format`, `status`), a callout explaining the format, and the wikitext itself inside a single ```` ```wikitext ```` fence — verbatim, byte-identical to what would be published. A raw `.wiki` file is invisible to Obsidian, and raw wikitext in an unfenced `.md` misrenders and pollutes the vault graph with fake `[[…]]` links. Reviewers edit **inside the fence only**; the publish step extracts the fence body and ships exactly that.

For the multi-topic cases, `<topic>` is the joined slug (`structure-benefits`, `origin`).

---

## Output file format

### `article.md` — deity-profile skeleton (for `tara-01` … `tara-21`)

The fenced wikitext body (everything inside the ```` ```wikitext ```` fence — the file's own frontmatter/callout wrapper is vault furniture, never published): pure wikitext, Tibetan script and Tibetan numerals only in the body. The doctrinal-term skeleton in the wikitext spec §1 does not fit a deity; this deity profile adapts it while keeping the spec's lead rule, fixed tail, citation form, and every validator rule:

```wikitext
'''<NAME>'''ནི་ <identification and one-sentence summary, cited><ref>...</ref>

== མཚན་གྱི་ངེས་ཚིག ==
<etymology of the name(s), from the consolidated page's etymology material><ref>...</ref>

== སྐུ་ཡི་རྣམ་པ། ==
<iconography / form — emit only if attested><ref>...</ref>

== ཕྲིན་ལས་དང་ནུས་མཐུ། ==
<activity, function, powers — emit only if attested><ref>...</ref>

== ལོ་རྒྱུས། ==
<origin narrative — emit only if attested><ref>...</ref>

== གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ==
<the ⚑ divergence material: each position attributed by commentator, never synthesised><ref>...</ref>

== བསྡུས་དོན། ==
<optional short summary>

== འབྲེལ་ཡོད་ཤོག་ངོས། ==
* [[<related term>་]]

== ལུང་ཁུངས། ==
<references />

== དཔྱད་གཞིའི་ཡིག་ཆ། ==
* <AUTHOR>། <TITLE>།

[[རིགས་དབྱེ།:<category from the spec §5 allowlist>]]
```

Section headings are a menu, not a quota: emit a section only when the consolidated page attests material for it, and never invent a section the sources do not support. A body section whose material the topic page organises differently may take a different Tibetan heading, provided it ends with a shad and its content is claim-backed. The lead has no heading. The last three sections are fixed and ordered: `འབྲེལ་ཡོད་ཤོག་ངོས།` → `ལུང་ཁུངས།` → `དཔྱད་གཞིའི་ཡིག་ཆ།`.

For the *work* article (`structure` + `benefits`), the body sections become: identification of the text (lead), its structure (སྟོད་ཆའི་ས་བཅད། or as attested), the benefits section (ཕན་ཡོན།), and transmission/colophon (ལོ་རྒྱུས། or as attested) — same lead rule, same fixed tail.

### `citations.md` — the audit trail

```markdown
---
topic: <topic>
article: article.md
method: wiki-article-from-claims
context_packages:
  - 2-RAILS/Claims/<topic>.md
rails_status: <status of the consolidated page at generation time>
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/<registered-id>.md
date: <YYYY-MM-DD>
status: draft
---

# Citations — <topic>

## Reference map

| Ref | Commentary | Claim ID(s) | Quotation (verbatim བོད་ཡིག, if quoted) | Source block |
|---|---|---|---|---|
| 1 | taranatha | c-1-5 | ཐུགས་དམིགས་པ་མེད་པའི་... | 1-SOURCES/Commentaries/<file>.md#^0-4 |

## Claims used but not quoted

<claim IDs whose content entered the prose paraphrased, listed per section>

## Unresolvable attestations

<any consolidated-page attestation whose claim ID could not be found in its raw file — each one dropped from the article, never guessed>

## Warnings

<rails_status not `complete`; refs missing year/page; refs with no public URL; article under ~1,500 Tibetan syllables; anything else a reviewer must see>

## Verification

<result of the quotation check: every quotation located character-for-character in its cited 1-SOURCES file — list each quote → PASS/FAIL>
```

---

## Rules

1. **Claims-only drafting.** Every statement in the article body must trace to a claim on the consolidated topic page. No parametric knowledge — no dates, Sanskrit forms, iconographic details, or doctrinal framings that are not in a claim, however standard they seem. If it cannot be cited, it does not go in.
2. **The resolution chain is fixed.** Consolidated attestation `commentary:claim-id` → that commentary's file under `2-RAILS/Claims/raw/tree-guided/` → the claim's **བོད་ཡིག**, English gloss, and `Cite:` target. An attestation that does not resolve is dropped and logged under *Unresolvable attestations* — never guessed, never cited anyway.
3. **Quotations are verbatim or absent.** Direct quotations come only from the **བོད་ཡིག** field of a resolved claim, character-for-character, wrapped in `" "`, each followed immediately by its `<ref>`. Never quote from memory of the source, never smooth a quotation's spelling or punctuation.
4. **Every quotation is verified before completion.** Each quotation must be located character-for-character (whitespace-collapsed) in the `1-SOURCES/` file its claim's `Cite:` names. A quotation that fails is removed or corrected from the བོད་ཡིག field, and the failure is recorded. This mirrors the kwiki pipeline's deterministic gate V1 and is not optional.
5. **Due weight follows attestation counts.** Consensus claims (high attestation) form the unattributed backbone prose, cited to 2–4 representative commentaries. Unique claims are attributed inline by commentator name. ⚑ divergences present every position with attribution — never flattened, never adjudicated.
6. **Never `{{Reflist}}`.** The references section is always `== ལུང་ཁུངས། ==` followed by `<references />`.
7. **Ref form is the spec's hand-formatted form**, built from the raw file's frontmatter: `<ref><AUTHOR>། <TITLE>།</ref>` (year/page appended when attested in frontmatter). No URLs exist for these sources yet: never fabricate one, never emit `dummy.com` — the missing URL goes in *Warnings*. Repeat citations of the same commentary use named refs (`<ref name="...">` full form first, `<ref name="..." />` after).
8. **The body is Tibetan only.** Tibetan script and Tibetan numerals throughout; Latin appears only inside ref URLs (of which there are currently none). English on the consolidated page is a drafting aid — where the resolved claim's བོད་ཡིག supplies the tradition's own wording for a concept, prefer that terminology in the prose.
9. **Spec mechanics are blocking**: tsheg at every `'''` and `[[` boundary; wikilink targets end in tsheg, never shad; every section contains ≥1 citation; sections only where attested; ≥1 category from the spec §5 allowlist and no invented category names; last-three-section order fixed.
10. **Read-only outside the output folder.** This skill never modifies `1-SOURCES/`, `2-RAILS/`, or anything in `4-SYSTEM/`. It writes only under `3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/`.
11. **Output is always `status: draft`**, and the consolidated page's own `status` is recorded as `rails_status` in `citations.md`. If the consolidated page is not `status: complete`, say so prominently in *Warnings* — the vault rule is that transformations generate from complete rails, and a human contributor accepts that risk explicitly when running this skill on a draft page.
12. **No publishing, no network.** The skill ends at the vault files. `/publish` and its pre-publication review remain the only road to bo.wikipedia.

---

## Procedure

1. **Load the contracts.** Read `4-SYSTEM/Pipelines/wikipedia/docs/reference/wikitext-spec.md` in full. Read the consolidated page `2-RAILS/Claims/<topic>.md` in full; record its `status` and its `sources:` list. For a multi-topic article, read every constituent page.
2. **Build the claim-resolution table.** Collect every attestation ID cited anywhere on the consolidated page (`commentary:claim-id`). For each, open the commentary's raw file and extract: the claim's **བོད་ཡིག**, its English line, its `Cite:` path and block ID, and the raw file's `author`/`title` frontmatter. Record every ID that fails to resolve. Do this before drafting a single sentence — the unresolvables must be known up front so nothing is built on them.
3. **Plan the article.** Map the consolidated page's numbered sections onto the skeleton's body sections. Mark which claims are backbone (consensus), which are attributed-unique, and which are ⚑ divergences destined for `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`. Select at most 1–3 verbatim quotations per major section — the article is prose, not a quote chain. Take the article's title/lead name from the consolidated page's own Tibetan heading (e.g. སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ), never from an unattested variant.
4. **Draft the lead.** Bold name (tsheg surviving the `'''` boundary), identification, one or two sentences of summary — every assertion cited.
5. **Draft the body sections** in Tibetan, section by section, applying Rules 1–5 and 8. Attach a `<ref>` to every claim-bearing sentence or clause; attribute unique and divergent positions by commentator name in the prose.
6. **Assemble the tail.** `འབྲེལ་ཡོད་ཤོག་ངོས།` (for `tara-NN`: the adjacent Tārās in the series and the root text's article — red links are expected and correct; targets end in tsheg). `ལུང་ཁུངས།` + `<references />`. `དཔྱད་གཞིའི་ཡིག་ཆ།`: one bullet per commentary actually cited, `<AUTHOR>། <TITLE>།` from frontmatter. One category from the allowlist.
7. **Write `citations.md`** per the format above: the full reference map, claims-used list, unresolvables, warnings.
8. **Verify.** (a) Every quotation: locate it character-for-character (whitespace-collapsed) in the `1-SOURCES/` file its claim cites; record PASS/FAIL per quote in `citations.md` §Verification; a FAIL is fixed or the quotation removed before completion. (b) Every `<ref>`: appears in the reference map. (c) Walk the spec's validator table V1–V12 as a checklist against `article.md`'s fence body and fix anything that fails.
9. **Report.** State where the two files were written, the rails_status, the count of refs and quotations, verification results, and every warning — the human reviewer decides what happens next.

---

## Completion check

- [ ] `article.md` (frontmatter + callout + fenced wikitext) and `citations.md` written under `3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/<topic>/`
- [ ] Every statement in the article traces to a claim on the consolidated page (no parametric additions)
- [ ] Every attestation used was resolved through its raw tree-guided file; unresolvables are listed and unused
- [ ] Every quotation verified character-for-character against its cited `1-SOURCES/` file, with PASS recorded per quote
- [ ] ⚑ divergences appear with all positions attributed; no divergence flattened
- [ ] `== ལུང་ཁུངས། ==` + `<references />` present; no `{{Reflist}}` anywhere
- [ ] Spec validator rules V1–V12 walked and passing (Tibetan-only body, tsheg boundaries, fixed tail order, allowlisted category, no dummy URLs or placeholder text)
- [ ] `citations.md` frontmatter records `context_packages`, `rails_status`, `status: draft`
- [ ] Warnings section lists rails_status if not `complete`, plus every ref missing a URL/year/page
- [ ] Nothing outside the output folder was modified; nothing was published
