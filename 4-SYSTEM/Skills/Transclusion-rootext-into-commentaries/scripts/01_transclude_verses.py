#!/usr/bin/env python3
"""STAGE 1 - Insert root-verse transclusions into a Tibetan commentary.

For each root-text verse stanza, find its first FULL inline quotation in the
commentary and insert  ![[<link-base>#^N-V]]  on the line immediately before it
(short Obsidian link form). Full stanza is preferred over a partial/illustrative
quotation; a verse quoted in passing (single line + closer) is matched
only when no fuller quotation exists.

Matching tolerates minor orthographic variants via a character-overlap ratio.
Also handles commentaries that quote the full stanza on a single bold line
(**line1 line2 line3 line4**).

Usage:
  python3 01_transclude_verses.py \\
      --root  1-SOURCES/Translations/<root>.md \\
      --commentary 1-SOURCES/Commentaries/Raw/<comm>.md \\
      --link-base "bo-blo-ldan-shes-rab" \\
      [--chapter N | --chapter all] [--apply]

Without --apply it prints a per-verse placement report (dry run). With --apply it
writes the transclusions into the commentary in place. Re-running is safe: verses
already transcluded are skipped.
"""
import re, sys, io, argparse, unicodedata
from difflib import SequenceMatcher
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r'!\[\[.*?\]\]', '', s)
    s = re.sub(r'\^[\w-]+', '', s)
    s = s.replace('**', '')          # strip Markdown bold markers
    for ch in ['།','༎','་',' ','༅','༄','༈']:
        s = s.replace(ch, '')
    return s.strip()

def ratio(a, b):
    if not a or not b: return 0.0
    return SequenceMatcher(None, a, b).ratio()

def line_match(v, c):
    if not v or not c: return False
    if v == c: return True
    if ratio(v, c) >= 0.80: return True
    if len(v) >= 8 and v in c: return True
    return False

# Citation closers in NORMALISED form -- norm() has already removed ་ ། ༎ and
# spaces, so these are bare letter runs. A citation frame in Tibetan commentary
# opens with ཞེས / ཅེས (ཞེས་སོགས་ལ།, ཅེས་པ་ནི།, ཞེས་གསུངས་སོ།, ཞེས་པས་བསྟན་ཏེ།)
# or with a bare སོགས.
#
# These were previously Latin transliterations ('zespa ni', 'cespani') compared
# against Tibetan text, so is_closer() could never return True and the
# single-line-citation path below was dead code. See the skill's Provenance note.
CLOSERS = ('ཞེས', 'ཅེས', 'སོགས')

#: Normalised characters of the opening pada that must be present before a
#: one-line hit counts. Twelve letters of Tibetan is a phrase, not a collision.
MIN_INCIPIT = 12
#: How far past the quoted run to look for the closer. Non-zero because editions
#: disagree on the pada's last syllable (དཔའ་མོ / དབའ་མོ), which truncates the
#: matched prefix a few characters early.
CLOSER_WINDOW = 16

def is_closer(cn):
    cn = cn.strip()
    return any(cn.startswith(c) for c in CLOSERS)

def longest_prefix_in(head, cn):
    """(length, position) of the longest prefix of `head` occurring in `cn`."""
    lo, hi, pos = 0, len(head), -1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        at = cn.find(head[:mid])
        if at >= 0: lo, pos = mid, at
        else: hi = mid - 1
    return lo, pos

def incipit_citation(stanza, cn):
    """True if `cn` cites the stanza by its opening pada inside a closer frame.

    The dominant citation shape in a བསྟོད་འགྲེལ: the commentator quotes the first
    pada only and frames it -- `ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། ཞེས་སོགས་ལ།` -- all on one
    line, then expounds. Requiring two of four padas (the default rule) never
    matches it, so a whole genre of commentary places nothing at all.

    The closer is what makes this safe: an opening pada echoed in passing mid-
    prose has no `ཞེས` after it, and is not accepted.
    """
    if not stanza or not cn: return False
    head = stanza[0]
    if len(head) < MIN_INCIPIT: return False
    matched, pos = longest_prefix_in(head, cn)
    if pos < 0 or matched < MIN_INCIPIT: return False
    tail = cn[pos + matched:][:CLOSER_WINDOW]
    return any(c in tail for c in CLOSERS)

def stanza_score(stanza, comm_norm, start):
    n = len(stanza)
    if start < 0 or start >= len(comm_norm): return 0, 0
    matched = 0; ci = start; si = 0; misses = 0
    while si < n and ci < len(comm_norm):
        # A blank line is layout, not a mismatch. Some commentaries set each
        # pada of a quoted stanza as its own block, so blank lines sit *between*
        # the padas; consuming a miss for each one exhausts the budget after the
        # first pada and the stanza scores 1 out of 4. Skipping them costs
        # nothing -- an empty string can never line_match anything anyway.
        if not comm_norm[ci]:
            ci += 1
            continue
        if line_match(stanza[si], comm_norm[ci]):
            matched += 1; si += 1; ci += 1
        else:
            misses += 1
            if misses > 1: break
            si += 1; ci += 1
    return matched, ci - start

def build_cand_index(comm_norm):
    idx = {}
    for i, cn in enumerate(comm_norm):
        if len(cn) < 5: continue
        idx.setdefault(cn[:5], []).append(i)
        idx.setdefault(cn[1:6], []).append(i)
    return idx

def stanza_concat_match(stanza, comm_norm_line):
    """Return True if the stanza lines concatenated match a single commentary line.
    Handles commentaries that quote the full stanza on one bold line."""
    if not stanza or not comm_norm_line: return False
    cat = ''.join(stanza)
    if not cat: return False
    if cat == comm_norm_line: return True
    r = ratio(cat, comm_norm_line)
    if r >= 0.78: return True
    return False

def find_best(stanza, comm_norm, taken, cand_idx, incipit=False, floor=0):
    cand_starts = set()
    # Candidate starts from individual stanza lines (multi-line match)
    for p, sl in enumerate(stanza):
        if len(sl) < 5: continue
        for k in (sl[:5], sl[1:6]):
            for ci in cand_idx.get(k, ()):
                st = ci - p
                if st >= 0: cand_starts.add(st)
    # Candidate starts from concatenated stanza (single-line bold match)
    cat = ''.join(stanza)
    if len(cat) >= 5:
        for k in (cat[:5], cat[1:6]):
            for ci in cand_idx.get(k, ()):
                cand_starts.add(ci)
    # Candidate starts for an incipit citation. The prefix index above only sees
    # line *openings*, and a framed citation is routinely embedded mid-line
    # (`དེ་ལ་ཚིགས་བཅད་དང་པོ་ ... ཞེས་པ་ལ་སོགས་པ་ལ།`), so those lines are invisible to it.
    # A containment scan is O(lines) per verse -- irrelevant at this scale.
    if incipit and stanza and len(stanza[0]) >= MIN_INCIPIT:
        probe = stanza[0][:MIN_INCIPIT]
        for ci, cn in enumerate(comm_norm):
            if probe in cn:
                cand_starts.add(ci)
    # With --in-order, a placement may not precede the previous verse's. A
    # commentary follows its root text in order, so a candidate that sits above
    # the last placement is a recurrence of the phrase, not this verse's citation.
    if floor:
        cand_starts = {s for s in cand_starts if s >= floor}
    best = None
    for start in cand_starts:
        if start in taken: continue
        # Try single-line (bold) match first
        if stanza_concat_match(stanza, comm_norm[start]):
            matched, reach = len(stanza), 1
            key = (matched, -start)
            if best is None or key > best[0]:
                best = (key, start, reach)
            continue
        matched, reach = stanza_score(stanza, comm_norm, start)
        need = max(2, (len(stanza) + 1) // 2)
        ok = matched >= need
        if not ok and matched >= 1:
            endc = start + reach
            if endc < len(comm_norm) and is_closer(comm_norm[endc]):
                ok = reach >= 1
        if not ok and incipit and incipit_citation(stanza, comm_norm[start]):
            # One-line incipit citation. Scored below a real multi-pada match
            # (matched = 1) so a fuller quotation elsewhere still wins.
            matched, reach, ok = 1, 1, True
        if not ok: continue
        if any((start + k) in taken for k in range(reach)): continue
        key = (matched, -start)
        if best is None or key > best[0]:
            best = (key, start, reach)
    if best is None: return None, 0
    return best[1], best[2]

def parse_root_verses(path, chapter):
    lines = open(path, encoding='utf-8').read().split('\n')
    verses = {}; cur = []
    for ln in lines:
        m = re.search(r'\^(\d+)-(\d+)\s*$', ln)
        tp = re.sub(r'\^[\d-]+\s*$', '', ln).strip()
        if tp and not tp.startswith('#') and not tp.startswith('!['):
            cur.append(tp)
        if m:
            ch, v = int(m.group(1)), int(m.group(2))
            stanza = [norm(x) for x in cur if norm(x)]
            if (chapter == 'all' or ch == int(chapter)) and stanza:
                verses["%d-%d" % (ch, v)] = (ch, v, stanza)
            cur = []
        if ln.strip() == '' and not m:
            cur = []
    return dict(sorted(verses.items(), key=lambda kv: (kv[1][0], kv[1][1])))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--commentary', required=True)
    ap.add_argument('--link-base', required=True,
                    help='base of the transclusion link')
    ap.add_argument('--chapter', default='all')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--incipit', action='store_true',
                    help='also accept a one-line citation of the opening pada '
                         'inside a ཞེས/ཅེས frame (the བསྟོད་འགྲེལ pattern)')
    ap.add_argument('--in-order', action='store_true',
                    help='refuse a placement that precedes the previous verse\'s')
    a = ap.parse_args()

    verses = parse_root_verses(a.root, a.chapter)
    comm_raw = open(a.commentary, encoding='utf-8').read().split('\n')
    comm_norm = [norm(x) for x in comm_raw]
    cand_idx = build_cand_index(comm_norm)

    existing = set()
    for ln in comm_raw:
        if '![[' in ln:
            for mm in re.finditer(r'\^(\d+-\d+)', ln):
                existing.add(mm.group(1))

    insertions = []; unplaced = []; taken = set(); floor = 0
    for vid, (ch, vn, stanza) in verses.items():
        if vid in existing:
            unplaced.append((vid, 'already-transcluded'))
            continue
        idx, span = find_best(stanza, comm_norm, taken, cand_idx,
                              incipit=a.incipit, floor=floor if a.in_order else 0)
        if idx is None:
            unplaced.append((vid, 'NO-MATCH (quoted with large variant / split / absent)'))
        else:
            insertions.append((idx, vid))
            for k in range(idx, idx + span):
                taken.add(k)
            floor = idx + span

    insertions.sort()
    print("verses=%d  placed=%d  unplaced=%d" % (len(verses), len(insertions), len(unplaced)))
    for li, vid in insertions:
        print("  ^%-7s -> line %d" % (vid, li + 1))
    if unplaced:
        print("UNPLACED (resolve by hand if a genuine quotation exists):")
        for vid, why in unplaced:
            print("  ^%s: %s" % (vid, why))

    if a.apply and insertions:
        out = comm_raw[:]
        for li, vid in sorted(insertions, reverse=True):
            ins = []
            prev = out[li-1] if li > 0 else ''
            if prev.strip() != '':
                ins.append('')
            ins.append("![[%s#^%s]]" % (a.link_base, vid))
            out[li:li] = ins
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate decode
        print("APPLIED %d insertions" % len(insertions))

if __name__ == '__main__':
    main()
