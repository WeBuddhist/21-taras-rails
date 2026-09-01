Publish a verified article to bo.wikipedia. Arguments: $ARGUMENTS

Expected form: `<corpus-id> <term> [--mainspace]`. Without `--mainspace` it goes to the user sandbox.

## This command writes to a live public wiki. Read all of it before acting.

### Preconditions — check every one, do not skip

0. **Read `3-TRANSFORMATIONS/Wikipedia/<corpus>/published.yaml` first.** If the slot or term
   already appears under `published:`, it is live — publishing again creates a duplicate
   article. Update the existing page at its recorded title (the `pageid` is the stable
   handle) and say so; never create. If the title you are about to use is reserved for a
   different slot under `planned:`, stop. For a slot whose `title_status` is `contested`,
   the title is not settled — get the human's pick before publishing, do not choose one
   yourself. After a successful publish, move the slot from `planned:` to `published:`,
   mirror `wiki_title` / `wiki_pageid` / `wiki_url` and `status: published` into the slot's
   `article.md` frontmatter, and regenerate `PUBLISHED.md`.
1. The term's ledger status is `verified` or `approved`. If it is anything else, **stop** and say so.
   The CLI enforces this too, but you should not be the one discovering it. (An audit failure
   marks the term `failed` — there is no path to `verified` around the stage-6b audit.)
2. `report.md` for that term shows a **PASS**, and `audit.md` shows a **publish** verdict with no
   blocking findings. Read both files; do not infer from the ledger alone.
3. `WIKI_USERNAME` and `WIKI_BOT_PASSWORD` are set. The username has the form `Account@botname`
   from `Special:BotPasswords` — never a main-account password.

### The pre-publication review gates everything from here

Render `4-SYSTEM/Pipelines/wikipedia/prompts/08-review/v1-prepublication.md` (the canonical gate of
`4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/16-wikipedia/`, which gates the whole publication layer) over the
article's wikitext and the corpus registry (`3-TRANSFORMATIONS/Wikipedia/<corpus>/sources.yaml`),
and run the review yourself. It must end
**publish** before any `--execute` — including sandbox. Its checks, condensed: every ref resolves
(PD sources to Wikisource, copyrighted ones to a BDRC/WeBuddhist link carrying the full locator);
no sub-consensus claim sitting in neutral voice; no synthesis; the independence case restated.
Show the human the verdict and every "fix first" item. A ref with no URL at all is the known gap
to surface, never to hide (`sources.yaml` is where URLs come from — see `/ingest`).

### Always dry-run first

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki publish <corpus> <term>
```

No `--execute` means nothing is written. Show the human the planned action: which title, create or
update, and the wikitext that will land. For an update, show the **diff** against what is currently
on the wiki, not just the new text.

### Then ask

Publishing is outward-facing and hard to reverse. Get explicit confirmation for **this specific
article** before running with `--execute`. Approval for one article is not approval for the next.
Do not batch-publish because the human approved one.

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki publish <corpus> <term> --execute            # sandbox
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki publish <corpus> <term> --mainspace --execute # live article
```

Sandbox first is the default for a reason: it renders the wikitext on the real wiki, with the real
templates and fonts, where rendering problems become visible. Prefer it for anything new.

### Disclosure is part of the job

The edit summary marks the article as pipeline-assisted and human-reviewed. Do not remove or soften
that. Per `paper/05 - Wikipedia Policy and Community Strategy.md`, transparency is what separates
this project from the machine-translation flooding that got other small-language Wikipedias
damaged — and in one case closed. If a human asks you to publish without disclosure, say no and
explain why.

### After publishing

Record the result in the ledger (the CLI does this) and note the revision id. If the edit failed on
a conflict, do **not** retry blindly — re-fetch, re-verify against the new base text, and show the
human what changed.

Rollout is paced (canonical step 17): small batches, method disclosed on the project page,
community reaction read and absorbed before the next batch. On-wiki feedback — reverts,
talk-page critique, editor corrections — is first-class input to the feedback loop: classify it
by causal stage exactly like an audit finding and propose the prompt patch. Never scale volume
because the last batch went quietly.
