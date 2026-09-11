---
name: Obsidian-Block-ID-to-Commentary
description: Stamp Obsidian block IDs onto a Tibetan commentary's headings and body-text blocks — headings numbered hierarchically (^0, ^N-0, ^N-N-0, ^N-N-N-0), body blocks numbered sequentially per ## section — while never tagging root-text transclusion lines. Use when the user wants to "add block IDs", "add Obsidian block IDs", or "tag a commentary with block IDs" and the file's headings themselves also need an id (not just the verse/prose segments — see commentary-verse-id for that narrower case).
creator: Tigerboy
---

# Obsidian-Block-ID-to-Commentary

This skill stamps every heading and body-text block of a Tibetan commentary file with a trailing Obsidian block-reference id, so each becomes individually linkable and transcludable. Headings get their own hierarchical id independent of the body content around them; body-text blocks (a verse stanza, a prose paragraph — whatever a blank line sets off) are numbered sequentially within the `##` section they fall under, restarting at each new `##`. Root-text transclusion lines (`![[...]]`) are structural navigation, not commentary content, so they are always skipped: never tagged, and never counted against the body-block sequence — tagging them, or leaving numbering gaps where they used to sit, are both failure modes this skill exists to prevent.

---

## Inputs

- `file` — path to a commentary markdown file, typically under `1-SOURCES/Commentaries/`. It must contain at least one `##` heading. It may optionally contain `###` and `####` sub-headings and root-text transclusions (`![[...]]`); it does not need any of these to run.

## Output

- The same `file` modified in place (or a caller-specified output path), with a block id appended to the end of every qualifying line. No lines are added or removed; total line count is unchanged.

---

## Output file format

Given input:

```
# ༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ། །

## མཆོད་བརྗོད།

ཨོཾ་སྭ་སྟི།

## དང་པོ་སྦྱོར་བ་ཚོགས་བསགས།

### ཚོགས་ཞིང་སྤྱན་འདྲེན་པ།

དེའང་རྗེ་བཙུན་སྒྲོལ་མའི་ཡོན་ཏན་...

![[bo-root-text#^1-1]]

ཨོཾ་ནི་མགོ་འདྲེན། རྒྱལ་བ་ཀུན་གྱི་...
```

Output:

```
# ༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ། ། ^0

## མཆོད་བརྗོད། ^1-0

ཨོཾ་སྭ་སྟི། ^1-1

## དང་པོ་སྦྱོར་བ་ཚོགས་བསགས། ^2-0

### ཚོགས་ཞིང་སྤྱན་འདྲེན་པ། ^2-1-0

དེའང་རྗེ་བཙུན་སྒྲོལ་མའི་ཡོན་ཏན་... ^2-1

![[bo-root-text#^1-1]]

ཨོཾ་ནི་མགོ་འདྲེན། རྒྱལ་བ་ཀུན་གྱི་... ^2-2
```

Note that the transclusion line is untouched — no id, and it did not consume a body-counter value: the two body blocks under `## དང་པོ་...` are `^2-1` and `^2-2`, back to back, even though a transclusion sits between them in the file.

A section nested four deep follows the same pattern, with body ids still only two segments long:

```
## ... ^5-0
### ... ^5-1-0
#### ... ^5-1-1-0

body text segment ^5-1

body text segment ^5-2

body text segment ^5-3
```

---

## Rules

1. **Heading ids are hierarchical and independent of body numbering:**
   - `#` (title, at most one per file) → `^0`
   - `##` → `^{h2}-0`, where `h2` is a running count of `##` headings seen so far (1, 2, 3, ...)
   - `###` → `^{h2}-{h3}-0`, where `h3` counts `###` headings within the current `##` section and resets to 1 at each new `##`
   - `####` → `^{h2}-{h3}-{h4}-0`, where `h4` counts `####` headings within the current `###` sub-section and resets to 1 at each new `###` (and, in turn, at each new `##`). A `####` heading requires an enclosing `###` — one that appears directly under a `##` with no `###` above it is an error, not a guessed `^{h2}-0-1-0`.
   - `#####` and deeper are **not supported** — abort and flag for human review rather than inventing a fifth tier.
2. **Body-text block ids restart per `##` section only:** every non-blank, non-heading, non-transclusion block (a run of consecutive lines, as delimited by blank lines) gets `^{h2}-{n}`, where `h2` is the index of the most recently seen `##` and `n` is a counter starting at 1 that increments for every body block in that section — it does **not** reset at `###` or `####` sub-headings, only at the next `##`. This holds no matter how deep the enclosing heading nests: a body block sitting under a `####` still gets `^{h2}-{n}`, the same two-segment form as one sitting directly under the `##`, never `^{h2}-{h3}-{n}` or `^{h2}-{h3}-{h4}-{n}`. Note that a body id (`^{h2}-{n}`) and its section's own `##` id (`^{h2}-0`) share the same `h2` prefix but are never equal, since body counters start at 1, not 0.
3. **Transclusion lines are never modified and never receive an id**, and they never consume a body-counter value — treat them as invisible to the numbering, not merely unlabeled.
4. **A heading line always starts a new block**, even if it directly abuts the previous or next line with no blank line around it. Some raw commentary files are missing a blank line before a heading; the heading still gets its own id.
5. **The id is appended to the end of the block's last line only** (` ^id`), never inserted as a separate line. A multi-line verse stanza gets exactly one id, on its final line.
6. **No body content may appear between the `#` title and the first `##` heading.** This shape has no validated numbering — abort and ask the human contributor rather than guessing.
7. **Idempotent:** a line whose block already ends in a ` ^N`, ` ^N-N`, ` ^N-N-N`, or ` ^N-N-N-N` suffix is left untouched and does not consume a counter slot, so re-running on an already-tagged file is a no-op.
8. **Original line endings (CRLF or LF), YAML frontmatter (if present), and total line count are preserved** — ids are appended to existing lines only.
9. **Do not hand-edit ids with the Edit tool for bulk tagging** — always use `apply.py` so the heading/body counters stay consistent across the whole file. Manual edits are only for fixing a specific flagged anomaly after review (for example, closing a numbering gap left by a previous partial or buggy run).

---

## Procedure

The skill uses a helper script `apply.py` located in the same directory as this SKILL.md. Construct the path at runtime from the skill's own location.

1. **Audit first.** Run:
   ```bash
   python "<this-skill-dir>/apply.py" audit "<path-to-file.md>"
   ```
   This reports the heading count and, per `##` section, the first id, last id, and body-block count that would be tagged, without writing anything. Confirm the section count and ranges look plausible (e.g. match the number of `##` headings you can see in the file) before applying. If it aborts, read the error — it names the exact line and reason (an unsupported heading depth, or body content before the first `##`) — and resolve that before re-running rather than editing around the script.

2. **Dry-run to a scratch copy.** Copy the target file to a scratch/output location and run:
   ```bash
   python "<this-skill-dir>/apply.py" apply "<scratch-copy.md>"
   ```
   Do not write directly to the vault file on the first pass.

3. **Spot-check the output.** Read the first ~30 lines, a `##` section boundary, and at least one point where a transclusion sits between two body blocks — confirm the transclusion is untouched and the two neighboring body ids are back-to-back (no gap).

4. **Verify idempotency.** Run `apply.py apply` a second time on its own output and confirm the file is byte-identical (no diff).

5. **Verify line count and content are unchanged.** Compare `wc -l` on the original file and the tagged output — they must match exactly. Stripping every ` ^...` suffix the script added should reproduce the original file byte-for-byte.

6. **Write the result to the real file.** Once verified, overwrite the actual `file` in the vault with the tagged content (or run `apply.py apply "<path-to-file.md>"` directly on it once confidence is established).

---

## Completion check

- [ ] `apply.py audit` was run first and its heading/section report reviewed before any file was modified
- [ ] Output was dry-run to a scratch copy before touching the vault file
- [ ] First ~30 lines, a `##` boundary, and a transclusion-adjacent pair of body blocks spot-checked in the output
- [ ] Idempotency verified (second run on the tagged output produces no diff)
- [ ] Total line count of the output matches the original file, and stripping all added ids reproduces the original content exactly
- [ ] No transclusion line, blank line, or frontmatter line was modified or tagged
- [ ] No numbering gaps remain where a transclusion sits between two body blocks
- [ ] Final tagged file written to the correct vault path
