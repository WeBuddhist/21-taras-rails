# TOC tree QC report

issues: 1

## Issues

- L10: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1 དང་པོ་གླེང་གཞི [[26]]

## Human note — checker/format artifact, not a real hallucination

`qc_check_tree.py`'s `_TREE_LINE_RE` regex only strips a trailing `^toc-N-N` block-ID
suffix; it does not know about this vault's `[[N]]` line-pointer convention (the format
`qc_tree_vs_source.py` and the promoted `karma-maitri`/`gendun-gyatso`/`lobsang-dawa` trees
actually use — see those trees' own QC reports for the same documented artifact). With the
trailing `[[26]]` left unstripped in the matched title text, the fuzzy bigram-coverage
check compares `གླེང་གཞི26` against the corpus; the topic word `གླེང་གཞི` is real but rare
(attested exactly once, as a Pass-1 `ITEMS:` entry), so the two extra digit-derived bigrams
from `26` are enough to sink a title this short below the 50% coverage floor.

Verified as a false positive by re-running the identical checker against a copy of this
same tree with only the `[[N]]` suffixes stripped (content otherwise byte-identical):

```
$ sed -E 's/ \[\[[0-9?]+\]\]//' 0-INBOX/toc-tree-gendun-drub.md > /tmp/gendun-drub-nopointer.md
$ python3 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_check_tree.py \
    /tmp/gendun-drub-nopointer.md \
    --corpus 0-INBOX/toc-candidates-gendun-drub.md 0-INBOX/toc-enumerations-gendun-drub.md
✓ 0 issues — tree is clean.
```

`གླེང་གཞི` is genuinely attested in `0-INBOX/toc-candidates-gendun-drub.md`'s first block
(`ITEMS: 1. གླེང་གཞི`), and the top-level enumeration itself
(`0-INBOX/toc-enumerations-gendun-drub.md`, Block 1: "འདི་ལ་གཉིས། གླེང་གཞི་དང་། དངོས་བཤད་པའོ།
།"). Treated as **0 real corpus-attestation issues** for promotion purposes.
