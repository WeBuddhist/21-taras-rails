# TOC tree QC report

issues: 15

## Issues

- L18: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.1.2 གཉིས་པ་ [[34]]
- L19: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.1.3 གསུམ་པ་ [[36]]
- L20: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.1.4 བཞི་པ་ [[38]]
- L21: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.1.5 ལྔ་པ་ [[40]]
- L22: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.1.6 དྲུག་པ་ [[42]]
- L26: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.2.3 གསུམ་པ་ [[50]]
- L27: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.2.4 བཞི་པ་ [[52]]
- L28: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.2.5 ལྔ་པ་ [[54]]
- L29: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.2.6 དྲུག་པ་ [[56]]
- L30: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.2.1.2.7 བདུན་པ་ [[58]]
- L34: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.3.2 གཉིས་པ་ [[68]]
- L35: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.3.3 གསུམ་པ་ [[70]]
- L36: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.3.4 བཞི་པ་ [[72]]
- L37: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.3.5 ལྔ་པ་ [[74]]
- L38: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.3.6 དྲུག་པ་ [[76]]

## Human note — all 15 flags are a checker/format artifact, not real hallucinations

`qc_check_tree.py`'s `_TREE_LINE_RE` regex only strips a trailing `^toc-N-N` block-ID
suffix; it does not know about this vault's `[[N]]` line-pointer convention (the format
`qc_tree_vs_source.py` and the promoted `karma-maitri`/`gendun-gyatso` trees actually use).
Every one of the 15 nodes above is a **bare-ordinal-only title** (`དང་པོ་`, `གཉིས་པ་`, …)
— when the trailing `[[N]]` is included unstripped in the matched title text, the fuzzy
bigram-coverage check has nothing real left to match against (an ordinal + a bracketed
line number), so it always reports 0% coverage regardless of whether the ordinal is
genuinely attested.

Verified as a false positive by re-running the identical checker against a copy of this
same tree with only the `[[N]]` suffixes stripped (content otherwise byte-identical):

```
$ python3 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_check_tree.py \
    <pointer-stripped copy of toc-tree-lobsang-dawa.md> \
    --corpus 0-INBOX/toc-candidates-lobsang-dawa.md 0-INBOX/toc-enumerations-lobsang-dawa.md
✓ 0 issues — tree is clean.
```

All 15 titles are genuinely attested in `0-INBOX/toc-candidates-lobsang-dawa.md` (each is
a standalone Pass-1 candidate, e.g. `SECTION_TITLE: གཉིས་པ་` for the node at line 34 of
the source). Treated as **0 real corpus-attestation issues** for promotion purposes.
