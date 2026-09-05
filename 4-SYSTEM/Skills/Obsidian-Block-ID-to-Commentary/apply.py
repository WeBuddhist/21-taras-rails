#!/usr/bin/env python3
r"""
apply.py — Obsidian-Block-ID-to-Commentary skill

Adds Obsidian-style block IDs to every heading and body-text block in a
Tibetan commentary file, following the vault's blank-line block convention.

Numbering scheme:
- Headings are numbered hierarchically, independent of body content:
    # Title              -> ^0                (at most one per file)
    ## Section            -> ^0-{h2}           (h2 = 1, 2, 3, ... in order)
    ### Sub-section        -> ^0-{h2}-{h3}      (h3 resets to 1 at each new ##)
- Body-text blocks (a run of consecutive non-blank, non-heading,
  non-transclusion lines, terminated by a blank line or a heading) are
  numbered ^{h2}-{n}, where h2 is the index of the most recently seen ##
  heading and n is a running counter that starts at 1 under each ## and is
  NOT reset by ### sub-headings within it.
- Root-text transclusion lines (![[...]]) are never modified and never
  receive an id, and they do not consume a body counter value — they are
  invisible to the numbering.
- The block id is appended to the END of the block's LAST line only
  (" ^id"), never inserted as a new line.

Assumptions / limitations (see SKILL.md §Rules):
- No body content may appear between the `#` title and the first `##`
  heading. If any is found, the script aborts rather than guessing a
  numbering for it (front matter of that shape has never been validated).
- Only heading levels 1–3 (#, ##, ###) are supported. A #### or deeper
  heading aborts the script — flag it for human review instead of
  inventing a fourth numbering tier.
- A heading line always starts a new block, even if it directly abuts the
  previous line with no blank line between them (a known formatting
  inconsistency in some raw commentary files).
- YAML frontmatter (a file that opens with a `---` line) is passed through
  untouched, matching the sibling `commentary-verse-id` skill.

Usage:
    python apply.py audit <path-to-file.md>
    python apply.py apply <path-to-file.md> [output.md]

`audit` reports the heading count and, per ## section, the first id, last
id, and block count that would be tagged — without writing anything.
`apply` writes the tagged output. If output.md is omitted, the input file
is overwritten in place.
"""
import re
import sys

HEADING_RE = re.compile(r'^(#{1,6})\s+\S')
TRANSCLUSION_RE = re.compile(r'^!\[\[.*\]\]\s*$')
EXISTING_ID_RE = re.compile(r'\s\^[0-9]+(?:-[0-9]+){0,2}\s*$')


class AbortError(Exception):
    pass


def read_lines(path):
    data = open(path, encoding='utf-8', newline='').read()
    eol = '\r\n' if '\r\n' in data else '\n'
    return data.split(eol), eol


def segment_blocks(lines, frontmatter_end):
    """Return a list of (start, end, kind) over lines[frontmatter_end:],
    kind in {'heading', 'transclusion', 'body'}. A heading line always
    forces its own block boundary, even without a blank line around it.
    """
    blocks = []
    i = frontmatter_end
    n = len(lines)
    current_start = None
    while i < n:
        stripped = lines[i].strip()
        if stripped == '':
            if current_start is not None:
                blocks.append((current_start, i - 1, 'body'))
                current_start = None
            i += 1
            continue
        if HEADING_RE.match(stripped):
            if current_start is not None:
                blocks.append((current_start, i - 1, 'body'))
                current_start = None
            level = len(stripped) - len(stripped.lstrip('#'))
            if level >= 4:
                raise AbortError(
                    f"Line {i+1}: heading level {level} (####+) is not "
                    f"supported by this skill — stop and flag for human "
                    f"review instead of guessing a fourth numbering tier.\n"
                    f"  {lines[i]!r}"
                )
            blocks.append((i, i, 'heading'))
            i += 1
            continue
        if TRANSCLUSION_RE.match(stripped) and current_start is None:
            # A transclusion line is its own block only when it is not
            # already glued to a preceding body block by a missing blank
            # line; that situation does not occur in validated input, so
            # if it happens, fall through and let it join the body block
            # (still never tagged individually — see tag_blocks).
            blocks.append((i, i, 'transclusion'))
            i += 1
            continue
        if current_start is None:
            current_start = i
        i += 1
    if current_start is not None:
        blocks.append((current_start, n - 1, 'body'))
    return blocks


def tag_blocks(lines, blocks):
    h2 = 0
    h3 = 0
    body_counter = 1
    seen_h2 = False
    stats = []  # (section_label, first_id, last_id, count)
    current_section = None  # [label, first, last]
    heading_count = 0

    for (s, e, kind) in blocks:
        if kind == 'heading':
            stripped = lines[s].strip()
            level = len(stripped) - len(stripped.lstrip('#'))
            heading_count += 1
            if level == 1:
                bid = "^0"
            elif level == 2:
                if not seen_h2 and body_counter > 1:
                    raise AbortError(
                        "Body content was found between the # title and "
                        "the first ## heading — this skill does not have "
                        "a validated numbering for that case. Stop and "
                        "ask the human contributor how to number it."
                    )
                seen_h2 = True
                h2 += 1
                h3 = 0
                if current_section is not None:
                    stats.append(tuple(current_section))
                current_section = [f"^0-{h2}", None, None]
                body_counter = 1
                bid = f"^0-{h2}"
            elif level == 3:
                if not seen_h2:
                    raise AbortError(
                        f"Line {s+1}: a ### heading appeared before any "
                        f"## heading — cannot assign ^0-{{h2}}-{{h3}}."
                    )
                h3 += 1
                bid = f"^0-{h2}-{h3}"
            else:
                raise AbortError(f"Unreachable heading level {level} at line {s+1}")

            if EXISTING_ID_RE.search(lines[e]):
                continue  # idempotent: already tagged, leave untouched
            lines[e] = lines[e] + " " + bid
            continue

        if kind == 'transclusion':
            continue  # never tagged, never consumes a counter

        # body block
        if not seen_h2:
            raise AbortError(
                f"Line {s+1}: body content appears before the first ## "
                f"heading — this skill does not have a validated "
                f"numbering for that case. Stop and ask the human "
                f"contributor how to number it."
            )
        bid = f"^{h2}-{body_counter}"
        if EXISTING_ID_RE.search(lines[e]):
            continue  # idempotent: already tagged, leave untouched, no counter bump
        if current_section[1] is None:
            current_section[1] = body_counter
        current_section[2] = body_counter
        lines[e] = lines[e] + " " + bid
        body_counter += 1

    if current_section is not None:
        stats.append(tuple(current_section))
    return lines, heading_count, stats


def process(lines):
    frontmatter_end = 0
    if lines and lines[0].strip() == '---':
        for j in range(1, len(lines)):
            if lines[j].strip() == '---':
                frontmatter_end = j + 1
                break
    blocks = segment_blocks(lines, frontmatter_end)
    return tag_blocks(lines, blocks)


def print_stats(heading_count, stats):
    print(f"Headings tagged: {heading_count}")
    if not stats:
        print("No body blocks found — nothing to tag.")
        return
    print(f"{'section':<10}{'first_id':<14}{'last_id':<14}{'count'}")
    for label, first, last in stats:
        if first is None:
            print(f"{label:<10}{'(none)':<14}{'(none)':<14}0")
            continue
        h2 = label.split('-')[-1]
        count = last - first + 1
        print(f"{label:<10}^{h2}-{first:<12}^{h2}-{last:<12}{count}")


def cmd_audit(path):
    lines, eol = read_lines(path)
    _, heading_count, stats = process(lines)
    print_stats(heading_count, stats)


def cmd_apply(infile, outfile):
    lines, eol = read_lines(infile)
    new_lines, heading_count, stats = process(lines)
    new_data = eol.join(new_lines)
    open(outfile, 'w', encoding='utf-8', newline='').write(new_data)
    print(f"Wrote {outfile}")
    print_stats(heading_count, stats)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    mode = sys.argv[1]
    infile = sys.argv[2]
    try:
        if mode == 'audit':
            cmd_audit(infile)
        elif mode == 'apply':
            outfile = sys.argv[3] if len(sys.argv) > 3 else infile
            cmd_apply(infile, outfile)
        else:
            print(__doc__)
            sys.exit(1)
    except AbortError as exc:
        print(f"ABORTED — nothing written.\n{exc}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
