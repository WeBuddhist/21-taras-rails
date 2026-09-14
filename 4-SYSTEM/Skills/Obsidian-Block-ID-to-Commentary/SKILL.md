---
name: Obsidian-Block-ID-to-Commentary
description: Stamp Obsidian block IDs onto a Tibetan commentary's ###/#### sub-headings and body-text blocks, keyed off a label the human contributor has already written by hand on each ## heading. The skill never generates, edits, or guesses a ## heading's own id — it must already be there (e.g. "^I-0", "^1-0", "^a-0") before anything else in that section gets tagged; body-text blocks then number sequentially off that same label (^I-1, ^I-2, ... or ^1-1, ^1-2, ... or ^a-1, ^a-2, ...). Use when the user wants to "add block IDs", "add Obsidian block IDs", or "tag a commentary with block IDs" — see commentary-verse-id for the narrower verse/prose-only case.
creator: Tigerboy
---

# Obsidian-Block-ID-to-Commentary

This skill stamps every `###`/`####` sub-heading and body-text block of a Tibetan commentary file with a trailing Obsidian block-reference id, keyed off a label the human contributor has already written by hand on the enclosing `##` heading — so each becomes individually linkable and transcludable. The `##` heading's own id is never generated, edited, or guessed by this skill: it must already be there, written by hand, before the skill will touch anything else in that section. Sub-headings get their own hierarchical id built from that label; body-text blocks (a verse stanza, a prose paragraph — whatever a blank line sets off) are numbered sequentially off the same label within the section, restarting at each new `##`. Root-text transclusion lines (`![[...]]`) are structural navigation, not commentary content, so they are always skipped: never tagged, and never counted against the body-block sequence.

---

## Inputs

- `file` — path to a commentary markdown file, typically under `1-SOURCES/Commentaries/`. It must contain at least one `##` heading, and **every `##` heading must already end in a manually-added `^{label}-0` id** (see Rule 1) before the skill will tag anything else. It may optionally contain `###` and `####` sub-headings and root-text transclusions (`![[...]]`); it does not need any of these to run.

## Output

- The same `file` modified in place (or a caller-specified output path), with a block id appended to the end of every qualifying `#`/`###`/`####` heading and body-text-block line. `##` heading lines are never modified. No lines are added or removed; total line count is unchanged.

---

## Output file format

Given input where the `##` headings already carry hand-written labels:

```
# ༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ། །

## མཆོད་བརྗོད། ^I-0

ཨོཾ་སྭ་སྟི།

## དང་པོ་སྦྱོར་བ་ཚོགས་བསགས། ^1-0

### ཚོགས་ཞིང་སྤྱན་འདྲེན་པ།

དེའང་རྗེ་བཙུན་སྒྲོལ་མའི་ཡོན་ཏན་...

![[bo-root-text#^1-1]]

ཨོཾ་ནི་མགོ་འདྲེན། རྒྱལ་བ་ཀུན་གྱི་...
```

Output:

```
# ༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ། ། ^0

## མཆོད་བརྗོད། ^I-0

ཨོཾ་སྭ་སྟི། ^I-1

## དང་པོ་སྦྱོར་བ་ཚོགས་བསགས། ^1-0

### ཚོགས་ཞིང་སྤྱན་འདྲེན་པ། ^1-1-0

དེའང་རྗེ་བཙུན་སྒྲོལ་མའི་ཡོན་ཏན་... ^1-1

![[bo-root-text#^1-1]]

ཨོཾ་ནི་མགོ་འདྲེན། རྒྱལ་བ་ཀུན་གྱི་... ^1-2
```

Note three things: the `##` headings (`^I-0`, `^1-0`) are exactly what the contributor wrote — untouched — and everything underneath is built from that label, not from a running section count; the title still gets an auto-generated `^0`; and the transclusion line is untouched and did not consume a body-counter value.

A section nested four deep, off a heading manually labeled `^5-0`, follows the same pattern:

```
## ... ^5-0
### ... ^5-1-0
#### ... ^5-1-1-0

body text segment ^5-1

body text segment ^5-2

body text segment ^5-3
```

A section whose contributor used a Roman-numeral label instead:

```
## ... ^II-0
### ... ^II-1-0

body text segment ^II-1

body text segment ^II-2
```

---

## Rules

1. **`##` heading ids are always manual — this skill never generates, edits, or guesses one.** Every `##` heading must already end in a block id of the form `^{label}-0`, written by hand by the human contributor. `{label}` can be anything the contributor is using to key that section (a plain running number, a Roman numeral, a letter, or any other short token) — this skill does not care what scheme it follows, only that it's already there. Before tagging anything, the skill scans every `##` heading in the file:
   - If **any** `##` heading is missing a `^{label}-0` id, the skill stops immediately, writes nothing, and tells the human contributor exactly which heading(s) (by line number and text) need an id added by hand. It does not invent a fallback numeric id for the missing ones, even to keep going on the rest of the file.
   - Only once **every** `##` heading in the file already carries a manual `^{label}-0` id does the skill proceed to tag the title, sub-headings, and body-text blocks.
   - The `#` title (at most one per file) is the one exception: it is still auto-generated as `^0`, exactly as before.
2. **`###`/`####` and body-text ids are all keyed off the enclosing `##` heading's manual label, never off a running section count:**
   - `###` → `^{label}-{h3}-0`, where `h3` counts `###` headings within the current `##` section and resets to 1 at each new `##`.
   - `####` → `^{label}-{h3}-{h4}-0`, where `h4` counts `####` headings within the current `###` sub-section and resets to 1 at each new `###` (and, in turn, at each new `##`). A `####` heading requires an enclosing `###` — one that appears directly under a `##` with no `###` above it is an error, not a guessed `^{label}-0-1-0`.
   - Body-text blocks (a run of consecutive non-blank, non-heading, non-transclusion lines) get `^{label}-{n}`, where `n` is a counter starting at 1 that increments for every body block in that section — it does **not** reset at `###`/`####` sub-headings, only at the next `##`. A body block sitting under a `####` still gets the two-segment `^{label}-{n}` form, never `^{label}-{h3}-{n}` or deeper.
   - Concretely: a `##` heading manually tagged `^I-0` produces body ids `^I-1`, `^I-2`, …; one tagged `^1-0` produces `^1-1`, `^1-2`, …; one tagged `^a-0` produces `^a-1`, `^a-2`, ….
   - `#####` and deeper are **not supported** — abort and flag for human review rather than inventing a fifth tier.
3. **Transclusion lines are never modified and never receive an id**, and they never consume a body-counter value — treat them as invisible to the numbering, not merely unlabeled.
4. **A heading line always starts a new block**, even if it directly abuts the previous or next line with no blank line around it. Some raw commentary files are missing a blank line before a heading; the heading still gets its own id (or, for `##`, is still recognized and its label still extracted).
5. **The id is appended to the end of the block's last line only** (` ^id`), never inserted as a separate line. A multi-line verse stanza gets exactly one id, on its final line. `##` heading lines are never appended to, since their id is already there.
6. **No body content may appear between the `#` title and the first `##` heading.** This shape has no validated numbering — abort and ask the human contributor rather than guessing.
7. **Idempotent:** a `#`/`###`/`####`/body line whose block already ends in a ` ^{label}-...` suffix is left untouched and does not consume a counter slot, so re-running on an already-tagged file is a no-op. `##` heading lines are always left untouched regardless (see Rule 1) — this includes both a first run and every re-run.
8. **Original line endings (CRLF or LF), YAML frontmatter (if present), and total line count are preserved** — ids are appended to existing lines only, and never to `##` headings.
9. **Do not hand-edit ids with the Edit tool for bulk tagging** — always use `apply.py` so the heading/body counters stay consistent across the whole file. Manual edits are only for two things: (a) adding the required `^{label}-0` id to a `##` heading before running the skill, and (b) fixing a specific flagged anomaly after review (for example, closing a numbering gap left by a previous partial or buggy run).

---

## Procedure

The skill uses a helper script `apply.py` located in the same directory as this SKILL.md. Construct the path at runtime from the skill's own location.

1. **Check `##` heading labels first.** Every `##` heading in the target file must already end in a `^{label}-0` id. `apply.py audit` performs this check automatically and aborts with a line-numbered list if any are missing — but glance at the file yourself too. If any are missing, stop here and tell the human contributor which heading(s) need one added by hand; do not proceed until they've done so.

2. **Audit.** Run:
   ```bash
   python "<this-skill-dir>/apply.py" audit "<path-to-file.md>"
   ```
   This reports, per `##` section (identified by its manual label), the first id, last id, and body-block count that would be tagged, without writing anything. Confirm the labels and ranges look plausible (e.g. match the `##` headings you can see in the file) before applying.

3. **Dry-run to a scratch copy.** Copy the target file to a scratch/output location and run:
   ```bash
   python "<this-skill-dir>/apply.py" apply "<scratch-copy.md>"
   ```
   Do not write directly to the vault file on the first pass.

4. **Spot-check the output.** Read the first ~30 lines, a `##` section boundary (confirming the `##` line itself is byte-identical to the input, and that the first body id under it starts with `^{that heading's own label}-1`), and at least one point where a transclusion sits between two body blocks — confirm the transclusion is untouched and the two neighboring body ids are back-to-back (no gap).

5. **Verify idempotency.** Run `apply.py apply` a second time on its own output and confirm the file is byte-identical (no diff).

6. **Verify line count and content are unchanged.** Compare `wc -l` on the original file and the tagged output — they must match exactly. Stripping every ` ^...` suffix the script added (the pre-existing `##` ids were already there, so leave those alone when checking) should reproduce the original file byte-for-byte.

7. **Write the result to the real file.** Once verified, overwrite the actual `file` in the vault with the tagged content (or run `apply.py apply "<path-to-file.md>"` directly on it once confidence is established).

---

## Completion check

- [ ] Every `##` heading in the file already had a manually-added `^{label}-0` id before any tagging ran; if any were missing, the human contributor added them first
- [ ] `apply.py audit` was run first and its label/section report reviewed before any file was modified
- [ ] Output was dry-run to a scratch copy before touching the vault file
- [ ] First ~30 lines, a `##` boundary (heading line byte-identical to input, first body id under it matching that heading's own label), and a transclusion-adjacent pair of body blocks spot-checked in the output
- [ ] Idempotency verified (second run on the tagged output produces no diff)
- [ ] Total line count of the output matches the original file, and stripping all newly-added ids reproduces the original content exactly
- [ ] No transclusion line, blank line, frontmatter line, or `##` heading line was modified or tagged
- [ ] No numbering gaps remain where a transclusion sits between two body blocks
- [ ] Every `###`/`####`/body-text id shares its enclosing `##` heading's own manual label
- [ ] Final tagged file written to the correct vault path
