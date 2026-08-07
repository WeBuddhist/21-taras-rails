---
name: claims-consolidation-audit
description: Adversarial attribution audit of a consolidated claims topic page — a fresh agent re-checks every citation against the raw claims files for attribution fidelity, quote fidelity, divergence reality, and epistemic strength. Report-only.
---

# claims-consolidation-audit

The second verification gate of the `claims-consolidation` skill, also runnable
standalone on any existing topic page. A deterministic script can prove a cited claim
*exists*; only a reader can prove the claim actually *says* what the page attributes
to it. This skill exists because the 2026-08-07 retrospective audit of the three pilot
pages found exactly the failure a smart consolidator produces: a real corpus idea
attached to the wrong claim ID — a "corroboration" by a claim containing nothing of
the sort — which no existence check can catch. Correct output is a findings report
precise enough that every finding can be fixed by editing one identified span of the
page, with no re-research.

**The auditor must be a fresh context that did not write the page.** An agent auditing
its own consolidation re-reads its own intentions, not the text.

---

## Inputs

- **The topic page to audit**: `2-RAILS/Claims/<topic-slug>.md`.
- **The raw claims files** it cites: `2-RAILS/Claims/raw/tree-guided/<registered_id>.md`
  (ground truth — claims appear as `#### c-… title` blocks with **བོད་ཡིག**,
  **English**, **Type**, **Referent**, **Cite** fields, and as `⚑ **c-… title**`
  bold blocks for internal tensions).
- Run the deterministic checker first if it has not been run —
  `4-SYSTEM/Skills/claims-consolidation/verify_consolidation.py <page>` — so the audit
  spends model judgment only on what the script cannot decide.

## Output

A structured findings report, delivered as the audit's response (report-only — this
skill **never edits the page or any other file**). When the human contributor wants
the findings preserved, write the report to
`0-INBOX/claims-audit-<topic-slug>-<YYYY-MM-DD>.md` — never anywhere in `2-RAILS/`.

---

## Output file format

```markdown
# Audit report — <topic-slug>.md (<date>)

## VERIFIED
<N of M unique citations checked and found accurate. State plainly what was
confirmed in full — consensus lists, divergence positions, quotes, review-section
reasons.>

## ERRORS
<One entry per citation whose attribution is wrong or distorted:>
1. **`registered_id:claim_id` — <severity>.**
   - Page says: <what the page attributes, quoted>
   - Raw claim says: <what the claim actually contains, quoted>
   - <If identifiable: the claim ID the page probably meant.>

## QUOTE MISMATCHES
<Each Tibetan string presented as a quote from a specific claim that differs from
the raw བོད་ཡིག, with both versions. "None found." if clean.>

## OTHER INTEGRITY ISSUES
<Count-label arithmetic, coverage-table mislabels, omitted in-corpus attestations
that would change a divergence's shape, raw-file inconsistencies worth a human
source check.>

**Bottom line:** <one paragraph: is the page trustworthy, and what must change.>
```

Severity scale: **critical** = a statement attributed that the claim does not make, a
fabricated corroboration, or a wrong-way divergence; **moderate** = real overstretch
that changes what a reader would believe is attested; **minor** = nuance loss,
interpolated framing, slightly-off gloss, arithmetic slips.

---

## Rules

1. **Read-only.** The audit changes nothing — not the page, not the raw files, not
   even typos. Findings go in the report; fixes are the consolidation skill's job.
2. **Ground truth is the raw claims file, only.** Judge the page against the cited
   claim's own བོད་ཡིག and English gloss — never against the auditor's knowledge of
   the tradition, and never against `1-SOURCES/` directly (if the raw claim itself
   looks wrong against its source, flag it as a raw-file issue for a human; do not
   re-litigate the extraction).
3. **Every citation, not a sample.** All unique citations on the page are checked,
   including the "Claims reviewed, not separately cited" reasons and any
   ambiguous-claims sections. (Consensus lists ≤6 entries: check all; larger lists:
   check at least half, and all entries of any list whose statement bundles multiple
   propositions.)
4. **Check the specific failure classes** the pilot audit proved real:
   a. claims cited for content they do not contain (especially "X and Y independently
      attest…" — verify both);
   b. consensus statements bundling propositions their attestation lists only
      partially support;
   c. the same claim cited on both sides of one divergence;
   d. page-level harmonizations presented as a claim's own reading;
   e. epistemic upgrades (tentative → "endorses");
   f. Tibetan quote elisions/normalizations against the raw བོད་ཡིག;
   g. divergences whose *other side* is attested in-corpus but omitted, flattening
      the disagreement.
5. **Cite exact claim IDs in every finding** and quote both sides (page wording vs
   raw wording) so the fix is mechanical.
6. **Do not pad.** If a section is clean, one sentence saying so. Findings ranked
   most severe first.

---

## Procedure

1. Read the topic page in full. List every unique `registered_id:claim_id` citation
   and note which section each appears in.
2. Read each cited raw claims file **once**, extracting the full content (བོད་ཡིག,
   English, Type, Referent) of every claim the page cites — including ⚑ bold-block
   tension claims, which are not heading blocks.
3. Work through the page section by section:
   a. **Consensus sections** — for each attestation (per Rule 3's sampling floor),
      confirm the claim supports the *full* statement; note partial-support padding.
   b. **⚑ Divergence sections** — confirm each position is genuinely in its cited
      claim, attributed to the right authority, and that the two sides actually
      disagree; check whether any omitted in-corpus claim attests a listed
      "external" reading.
   c. **Unique sections** — confirm the claim says what is summarised and that no
      second commentary in the corpus attests the same content.
   d. **Quotes** — compare every Tibetan string attributed to a specific claim
      character-by-character against the raw བོད་ཡིག.
   e. **Review/excluded sections** — confirm each one-line reason accurately
      describes the raw claim (a "pure heading" really is one, etc.).
   f. **Coverage table** — spot-check "Contributed to" labels against where the
      claims were actually used (a divergent claim labeled as Consensus is a
      finding).
4. Assemble the report in the format above, severity-ranked, and deliver it.
5. If the audit was invoked as gate 2 of `claims-consolidation`: after the
   consolidator fixes the findings, re-audit the changed sections (only) and confirm
   the fixes; the page passes when no critical or moderate finding remains.

---

## Completion check

- [ ] Every unique citation on the page was checked against its raw claim (sampling
      floor of Rule 3 met or exceeded; review-section reasons included)
- [ ] Every finding cites an exact `registered_id:claim_id` and quotes page wording
      vs raw wording
- [ ] Every finding carries a severity (critical / moderate / minor)
- [ ] All seven failure classes of Rule 4 were explicitly checked
- [ ] No file was modified anywhere in the vault (report written to `0-INBOX/` only
      if the human asked for it)
- [ ] Bottom line states plainly whether the page is trustworthy and what must change
