Run the tree-guided claims extraction (method 3) for one commentary. Arguments: $ARGUMENTS

Expected form: `<registered-id> [--ingest-headings]`, e.g. `/extract-claims karma-maitri`.

This is the vault's third claims-extraction method, alongside the two already compared in
`3-TRANSFORMATIONS/Wikipedia/tara21/claims/_comparison-report.md`: direct extraction
(`opus`/`sonnet`, one file each) and the discredited `toc-scaffolded` run (which turned out
to be Sonnet's claims re-bucketed, not a real third extraction — read that report's headline
finding before running this if you have not). Method 3 is a genuinely independent
extraction: read one TOC-tree node's own text in isolation and extract claims fresh from it,
never re-using or consulting another method's output.

## Step 1 — Resolve the commentary

Find the `1-SOURCES/Commentaries/*.md` file whose frontmatter carries
`registered_id: <registered-id>`. If none exists, stop and say so — do not guess a filename.

## Step 2 — Ensure a TOC tree exists, and that it is checked against THIS file

Look for `0-INBOX/toc-tree-<registered-id>.md` or
`0-INBOX/temp/TOC-<registered-id>/toc-tree-<registered-id>.md`.

- **If no tree exists**, run `4-SYSTEM/Skills/toc-tree-extraction/SKILL.md` on the resolved
  file first (its own four-pass, isolated-subagent orchestration — read it in full before
  running it).
- **If a tree exists**, check whether it was built against the *current* file. This vault's
  own 2026-08-04 migration resegmented every commentary, so the three trees shipped before
  it (`gendun-gyatso`, `karma-maitri`, `lobsang-dawa`) were built against the pre-migration
  body, backed up at `0-INBOX/migration-backups/2026-08-04/`. A tree's `[[N]]` pointers only
  mean something against the exact file version `chunk_file.py` chunked — if the tree
  predates the current file, **rebuild it** against the current file rather than trusting
  stale pointers. Do not silently proceed with a mismatched tree.

## Step 3 — Deterministic QC gate, with repair loop

Run **both** checkers (`toc-tree-extraction`'s Pass 4 — read it for the exact commands and
the repair-subagent loop):

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_check_tree.py \
  <tree-file> --corpus <candidates-file> <enumerations-file> \
  --out 0-INBOX/toc-tree-qc-<registered-id>.md

python 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_tree_vs_source.py \
  <tree-file> --source <the-resolved-commentary-file> \
  --out 0-INBOX/toc-tree-qc-source-<registered-id>.md
```

If either reports issues, dispatch the isolated pass-4 repair subagent (per that skill's
Procedure), re-run both checkers, and iterate until clean or until only genuinely-ambiguous
issues remain — note those for the human rather than proceeding past them silently. **Do
not extract claims against a tree either checker flagged**, except for issues explicitly
noted as human-reviewed-and-accepted.

## Step 4 — Optional: ingest the tree as headings into the source

Only if `--ingest-headings` was given. This is a **separate, consequential step** — it
writes into `1-SOURCES/`, which is otherwise frozen ground truth:

1. `4-SYSTEM/Skills/toc-tree-ingest/SKILL.md` — inserts the tree's headings into a copy of
   the commentary at `1-SOURCES/Commentaries/commentaries_with_toc/<registered-id>.toc.md`.
   Heading block IDs use the tree's **full decimal path, no segment cap** (e.g.
   `^1-2-2-1-0` at five levels) — this vault's `4-SYSTEM/Guidelines/vault-annex.md` §2
   states this explicitly, overriding `4-SYSTEM/CLAUDE.md` §5a's four-segment cap for this
   specific case, matching the proven convention from the sibling
   `bodhisattvacharyavatara-rails` vault.
2. `4-SYSTEM/Skills/tag-inline-toc/SKILL.md` — tags the inline sa-bcad announcement
   sentences as wikilinks pointing at the new headings.
3. Read both `SKILL.md`s in full before running either. Report what changed and where.

Skip this step entirely if not asked for it — `tree-guided-claims` does not require headed
source text; it reads by line window regardless.

## Step 5 — Run the extraction

Read `4-SYSTEM/Skills/tree-guided-claims/SKILL.md` in full and follow its Procedure exactly:
one isolated subagent per TOC-tree node, each given only its own line window and this
commentary's own file — never another node's output, never `opus`/`sonnet`/
`toc-scaffolded`'s files. This is what makes the extraction structurally independent rather
than independent by discipline alone; do not shortcut it by reading the whole file yourself
and writing all the claims in this context.

Output lands at:
```
3-TRANSFORMATIONS/Wikipedia/<corpus>/claims/tree-guided/<registered-id>.md
```

## Step 6 — Deterministic verification gate

```bash
python 4-SYSTEM/Skills/tree-guided-claims/scripts/verify_claims.py \
  3-TRANSFORMATIONS/Wikipedia/<corpus>/claims/tree-guided/<registered-id>.md \
  --source 1-SOURCES/Commentaries/<filename>.md
```

Checks quote containment (NFC + tsheg/shad-stripped, ellipsis fragments tested
individually), `claim_count` recomputation, claim-ID well-formedness and uniqueness, and
`stated`-referent validity (the name must occur in *that claim's own* quotation, not just
somewhere in the source). Fix every issue by dispatching a fresh per-node subagent for the
offending node — never by hand-editing a claim to make the checker pass — and re-run until
clean, or log remaining issues for human review. The info-level coverage summary at the end
is not gated on; read it and cross-check it against the file's own Coverage log by hand.

## Step 7 — Report honestly

Tell the human: how many nodes were extracted, the total claim count (and how it compares
to `opus`'s and `sonnet`'s counts for the same commentary, if those exist), how many
verifier issues were found and fixed vs. left open, and the Unanchored/Internal-tensions
rollup counts. If this is the first tree-guided run for a commentary that also has
`opus`/`sonnet`/`toc-scaffolded` files, note that a fair comparison needs the same kind of
adversarial read `_comparison-report.md` gave the first three methods — offer to run one,
do not claim method 3 "wins" or "loses" without it.
