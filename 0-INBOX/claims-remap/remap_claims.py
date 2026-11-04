"""Map tree-guided claims from the old commentary segmentation onto the library edition.

The raw claims in 2-RAILS/Claims/raw/tree-guided/ cite the "used for wiki" commentary files,
whose blocks are ^0-N / ^I-N. The human-annotated, resegmented versions in
1-SOURCES/Commentaries/New raw data/ are what the WeBuddhist library holds (their frontmatter
carries text_id / edition_id), and their block IDs are the library segments' `reference`.

Each claim is located in the new file two independent ways:
  1. cite map  - its old block(s) -> new block(s), by aligning the two files' syllable streams
  2. quote     - its verbatim བོད་ཡིག quote searched in the new file's syllable stream
and the two are compared. Read-only: writes JSON + a markdown report under out/.

Usage (from the vault root):
    python3 0-INBOX/claims-remap/remap_claims.py            # all commentaries with a new version
    python3 0-INBOX/claims-remap/remap_claims.py dharmabhadra
"""

import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
CLAIMS = VAULT / "2-RAILS/Claims/raw/tree-guided"
OLD_DIR = VAULT / "1-SOURCES/Commentaries/used for wiki"
NEW_DIR = VAULT / "1-SOURCES/Commentaries/New raw data"
OUT = Path(__file__).resolve().parent / "out"

# registered_id -> resegmented file uploaded to the library
NEW_FILES = {
    "karma-maitri": "bo-ཀརྨ་མཻ་ཏྲི།.md",
    "taranatha": "bo-ཏཱ་ར་ན་ཐ།.md",
    "dharmabhadra": "bo-དངུལ་ཆུ་དྷརྨ་བྷ་དྲ།.md",
    "pema-namgyal": "bo-པདྨ་རྣམ་རྒྱལ།.md",
    "tenga-tulku": "bo-བསྟན་དགའ་སྤྲུལ་སྐུ།.md",
    "gendun-drub": "bo-རྒྱལ་བ་དགེ་འདུན་གྲུབ།.md",
    "drakpa-gyaltsen": "bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md",
    "sangye-nyentrul": "bo-སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ།.md",
}

ANCHOR = re.compile(r"\s\^([A-Za-z0-9-]+)\s*$")
TOKEN_SPLIT = re.compile(r"[་༌།༎༏༐༑༔༄༅༈\s ]+")


def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.index("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            fm[m[1]] = m[2].strip().strip('"')
    return fm, text[end + 4:]


def clean(s):
    s = re.sub(r"!\[\[[^\]]*\]\]", " ", s)               # transclusions are the root's text, not ours
    s = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", s)    # [[target|label]] -> label
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"^#+\s*", "", s, flags=re.M)
    s = re.sub(r"[*_>`]", "", s)
    s = re.sub(r"(?<=\s)\^[A-Za-z0-9-]+(?=\s|$)", " ", s)
    return s


def tokens(s):
    return [t for t in TOKEN_SPLIT.split(clean(s)) if t]


def blocks(path):
    """[(block_id, text)] in file order; a block is the paragraph ending in its anchor."""
    fm, body = frontmatter(path.read_text(encoding="utf-8"))
    out, buf = [], []
    for line in body.splitlines():
        if not line.strip():
            continue
        if line.lstrip().startswith("![["):
            continue
        m = ANCHOR.search(line)
        buf.append(line[: m.start()] if m else line)
        if m or line.lstrip().startswith("#"):
            out.append((m[1] if m else None, "\n".join(buf)))
            buf = []
    if buf:
        out.append((None, "\n".join(buf)))
    return fm, out


def stream(blks):
    toks, owner = [], []
    for i, (_, text) in enumerate(blks):
        t = tokens(text)
        toks += t
        owner += [i] * len(t)
    return toks, owner


def align(old_toks, new_toks):
    """old token index -> new token index, for matched syllables."""
    sm = SequenceMatcher(None, old_toks, new_toks, autojunk=False)
    m = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            m[a + k] = b + k
    return m


def find_quote(q, new_toks, new_owner, cited, near):
    """Exact syllable-run search. Root lines and heading labels recur, so an occurrence inside
    the cite-mapped blocks wins; otherwise the one nearest `near` (a new token index)."""
    if not q:
        return None
    hits, first = [], q[0]
    for i, t in enumerate(new_toks):
        if t == first and new_toks[i : i + len(q)] == q:
            hits.append(i)
    if not hits:
        return None
    inside = [i for i in hits if cited & {new_owner[j] for j in range(i, i + len(q))}]
    if inside:
        return inside[0]
    return min(hits, key=lambda i: abs(i - near)) if near is not None else hits[0]


def fuzzy_quote(q, new_toks, lo, hi):
    sm = SequenceMatcher(None, q, new_toks[lo:hi], autojunk=False)
    got = [(b + lo, n) for _, b, n in sm.get_matching_blocks() if n]
    matched = sum(n for _, n in got)
    return matched / len(q), got


def parse_claims(path):
    text = path.read_text(encoding="utf-8")
    fm, _ = frontmatter(text)
    claims, cur = [], None
    for line in text.splitlines():
        h = re.match(r"^#+\s+(c-[0-9a-zA-Z-]+)\s*(.*)$", line)
        if h:
            cur = {"claim_id": h[1], "label": h[2], "quote": "", "cites": []}
            claims.append(cur)
        elif cur and line.startswith("**བོད་ཡིག:**"):
            cur["quote"] = line.split("**བོད་ཡིག:**", 1)[1].strip()
        elif cur and line.startswith("**Cite:**"):
            cur["cites"] = re.findall(r"\^([A-Za-z0-9-]+)", line)
    return fm, claims


def old_file(fm):
    name = Path(fm.get("source_file", "")).name
    for cand in (VAULT / fm.get("source_file", ""), OLD_DIR / name):
        if cand.is_file():
            return cand
    stem = name.rstrip("།། .md")[:30]
    hits = [p for p in OLD_DIR.glob("*.md") if p.name.startswith(stem) and "(v2)" not in p.name]
    return hits[0] if hits else None


def remap(rid):
    cfm, claims = parse_claims(CLAIMS / f"{rid}.md")
    ofile, nfile = old_file(cfm), NEW_DIR / NEW_FILES[rid]
    _, oblk = blocks(ofile)
    nfm, nblk = blocks(nfile)
    otoks, oown = stream(oblk)
    ntoks, nown = stream(nblk)
    tmap = align(otoks, ntoks)

    # old block -> {new block: matched syllables}
    oid_index = {bid: i for i, (bid, _) in enumerate(oblk) if bid}
    per_old = {}
    for oi, ni in tmap.items():
        per_old.setdefault(oown[oi], {}).setdefault(nown[ni], 0)
        per_old[oown[oi]][nown[ni]] += 1
    osize = {}
    for o in oown:
        osize[o] = osize.get(o, 0) + 1

    def nref(i):
        return nblk[i][0] or f"(unanchored #{i})"

    rows = []
    for c in claims:
        cite_new, cite_cov, near = {}, None, None
        known = [oid_index[x] for x in c["cites"] if x in oid_index]
        if known:
            tot = sum(osize.get(o, 0) for o in known)
            for o in known:
                for n, k in per_old.get(o, {}).items():
                    cite_new[n] = cite_new.get(n, 0) + k
            cite_cov = round(sum(cite_new.values()) / tot, 3) if tot else 0.0
            if cite_new:
                first = min(cite_new)
                near = nown.index(first)
        cited = {n for n in cite_new if cite_new[n] >= max(1, 0.1 * max(cite_new.values()))}
        cite_refs = [nref(n) for n in sorted(cited)]

        q = tokens(re.sub(r"…|\.\.\.", " ", c["quote"]))
        quote_refs, quote_score, how = [], 0.0, None
        pos = find_quote(q, ntoks, nown, cited, near)
        if pos is not None:
            quote_refs = sorted({nown[i] for i in range(pos, pos + len(q))})
            quote_score, how = 1.0, "exact"
        elif q:
            if near is not None:
                lo, hi = max(0, near - 400), min(len(ntoks), near + 400 + sum(cite_new.values()))
            else:
                lo, hi = 0, len(ntoks)
            quote_score, got = fuzzy_quote(q, ntoks, lo, hi)
            quote_score = round(quote_score, 3)
            touched = {}
            for b, n in got:
                if n >= (1 if len(q) <= 6 else 3):
                    for i in range(b, b + n):
                        touched[nown[i]] = touched.get(nown[i], 0) + 1
            quote_refs = sorted(touched)
            how = "fuzzy"
        quote_refs = [nref(i) for i in quote_refs]

        if how == "exact" and (not cite_refs or set(quote_refs) & set(cite_refs)):
            verdict = "confirmed"
        elif how == "exact":
            verdict = "quote-wins"          # quote found, but not where the old cite points
        elif quote_score >= 0.6 and quote_refs and set(quote_refs) & set(cite_refs):
            verdict = "confirmed-fuzzy"
        elif quote_score >= 0.6 and quote_refs:
            verdict = "quote-wins-fuzzy"
        elif cite_refs and (cite_cov or 0) >= 0.8:
            verdict = "cite-only"
        elif known and not cite_new:
            verdict = "absent-from-edition"   # the old block's text is not in the library edition
        else:
            verdict = "unresolved"

        # Was the quote in the cited old block to begin with? False = transcluded root verse,
        # a heading restated in the body, or an extraction slip in the original claim.
        old_hit = find_quote(q, otoks, oown, set(known), None) if q else None
        in_cited_old = old_hit is not None and oown[old_hit] in set(known)

        best = quote_refs if verdict.startswith(("confirmed", "quote")) else cite_refs
        rows.append({
            "claim_id": c["claim_id"],
            "label": c["label"],
            "old_cites": c["cites"],
            "new_refs": best,
            "verdict": verdict,
            "quote_match": how,
            "quote_score": quote_score,
            "cite_map_refs": cite_refs,
            "cite_coverage": cite_cov,
            "quote_in_cited_old_block": in_cited_old,
        })

    matched = len(tmap)
    result = {
        "registered_id": rid,
        "old_file": str(ofile.relative_to(VAULT)),
        "new_file": str(nfile.relative_to(VAULT)),
        "library": {k: nfm.get(k) for k in ("text_id", "edition_id", "toc_id", "commentary_of")},
        "syllables": {"old": len(otoks), "new": len(ntoks), "aligned": matched,
                      "old_aligned_share": round(matched / len(otoks), 3) if otoks else 0},
        "verdicts": {},
        "claims": rows,
    }
    for r in rows:
        result["verdicts"][r["verdict"]] = result["verdicts"].get(r["verdict"], 0) + 1
    return result


def main():
    ids = sys.argv[1:] or list(NEW_FILES)
    OUT.mkdir(exist_ok=True)
    summary = []
    for rid in ids:
        r = remap(rid)
        (OUT / f"{rid}.json").write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
        summary.append(r)
        print(f"{rid:16} claims={len(r['claims']):4} aligned={r['syllables']['old_aligned_share']:.1%} {r['verdicts']}")
    (OUT / "summary.json").write_text(
        json.dumps([{k: v for k, v in r.items() if k != "claims"} for r in summary], ensure_ascii=False, indent=1),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
