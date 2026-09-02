# Batch reporting checklist — where the numbers go when the batch lands

*Created 2026-08-02, when the corpus-wide batch was decided on. The draft
(`paper.md`) is already restructured as **pilot (N=3, deep) + batch (N≈96,
distributional)**; this file is the exhaustive list of `[TO FILL]` slots the batch
feeds, so nobody has to re-read the paper hunting for stale threes.*

**The rule this file exists to protect:** a number enters the paper only after its
artifacts are on disk and a human has looked at them. Every row below is blocked on a
real run. Do not fill a slot from a projection.

## Before the batch can run — three prerequisites

1. **The term list does not exist locally.** `corpora/tara21/terms.yaml` holds only
   the pilot's 3 terms. Session 2's 105-candidate list (`work/term_candidates.md`) is
   among the cloud-only artifacts STATE.md lists as unrecoverable. It *is*
   regenerable: `scripts/enrich_tara21_terms.py` carries the full en→bo mapping inline
   (**96 distinct Tibetan terms across the 23 root units**, 16 of them in more than one
   verse). Two repairs needed: the hardcoded `/tmp/iats` paths, and the missing YAKE
   input (`root.en-keyword_verses_yake.json` is not in `vendor/skills/`) — the
   ENRICH dict makes the YAKE pass skippable if ranking is done from `aligned.json`
   support alone, which is what the script's own ranking section does anyway.
2. **No batch runner exists.** `kwiki article` takes one term. A driver is needed that
   loops terms, tolerates per-term failure (a failed term must not abort the batch),
   records per-term wall-clock and model-call counts, and leaves the ledger resumable.
3. **The extraction tuning pass is still owed.** Capture was 45% / 19% / **1.1%** in
   the pilot, worst on the largest offer. Running the batch first is a legitimate
   choice — it produces the capture-vs-offer curve that tells you what to tune — but
   know that articles generated pre-tuning may need regenerating, and decide up front
   which run is the one the paper reports.

## The slots, section by section

| § | Slot | What fills it |
|---|---|---|
| 1 | "a corpus-wide batch over the Tārā term list" | Nothing — stands as written once the batch exists. If the batch is abandoned, revert §1 to pilot-only wording. |
| 8 | Batch N in the two-scale list | Terms attempted / articles reaching `verified`, both counts |
| 8 | **Pipeline statistics — batch** | Per-article distribution: claims, claim types, distinct commentaries cited, tshegbar length (median + range, and how many clear the 1,500 threshold) |
| 8 | Zero majority-with-dissent | Whether the batch's claim-type distribution still shows 0 — genre property vs. three lucky terms |
| 8 | Gate first-pass failure rate | How often the deterministic gate fails a *first* draft across the batch (the pilot has no clean number for this) |
| 8 | Per-stage: capture curve | Capture rate against offer size across all terms — the tunable form of the 45/19/1.1 observation |
| 8 | Citation verifiability | Total quotations across the batch, character-exact count, locator-resolution count |
| 8 | Audit pass rates | Rate over repeated runs per article; same-model comparison on a **stratified subsample**, not assumed |
| 8 | Attribution integrity | Attribution-loss findings per 100 sub-consensus claims |
| 8 | Cost | Measured per-article distribution incl. the retry factor; reconcile against `cost-and-scalability.md`'s $0.33–1.42 estimate and update that file if the batch contradicts it |
| 9 | Limitations | Keep the human-legs-sample-the-batch framing; update only if human coverage changes |

## Things the batch does *not* fix — do not let the bigger N imply otherwise

- **Human review still samples.** Rating, citation-support judgment, and
  reviewer-minutes scale with reviewers, not with articles. §8 and §9 say this; keep
  them saying it.
- **Notability is still per-topic and human.** 96 machine-proposed keywords are not 96
  notable topics. §6's double gate (corpus breadth proposes, secondary-source check
  disposes) applies to every one of them, and the batch makes the curation backlog
  bigger, not smaller.
- **Terms remain `status: candidate`** until a human approves the list. A batch of
  unapproved candidates is a research artifact, not a publication queue.
- **The citation-URL debt (W2) is unchanged.** Still blocks mainspace for every
  article in the batch.
- **N=96 machine articles ≠ 96 published articles.** §1/§10's "not a revived
  encyclopedia" wording stays honest regardless of batch size.

## Reviewer-minutes: the one measurement the batch makes possible

The paper's lead metric (§3, §8) is reviewer-hours per audit-passed article, and it is
still `[TO FILL]`. The batch is the first chance to measure it on a real queue rather
than assume 30–60 minutes. **Log wall-clock review time per article from the first
article reviewed** — retrospective estimates are unreliable (`06 - Evaluation Plan`
says this explicitly), and this single number is what converts §3's trilemma from
rhetoric into a finding.
