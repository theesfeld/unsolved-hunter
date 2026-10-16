# Hunt 58 — New lower bounds for van der Waerden numbers w(2;3,32) and w(2;3,36)

**Result:** w(2;3,32) ≥ 1012 (was ≥ 1007) and w(2;3,36) ≥ 1260 (was ≥ 1258).
**Novelty: MINOR.** Valid and, as far as we can find, not previously published, but elementary.

## What this means
w(2;3,t) is the smallest n such that every 2-colouring of {1..n} contains a 3-term arithmetic progression (AP) in colour 0 or a t-term AP in colour 1. Exhibiting a colouring of length n with neither proves w(2;3,t) > n.

## Method (honest)
Ahmed, Kullmann & Snevily (2014, arXiv:1102.5433, Table 3 / App. A.2) published certificate colourings: w(2;3,32) > 1006, w(2;3,36) > 1257. We noticed they are not maximal at the left end: prepending colour-1 cells keeps them valid, 5 cells for t=32 and 2 for t=36. One more cell creates a colour-1 t-AP. That is the whole improvement.
We then ran a seeded local search (tabu/WalkSAT-style, ls.c; extending at the end, prefix-padded and reversed seeds) — see "Search" below.

## Search
Seeded tabu/WalkSAT local search (ls.c, colour-0/colour-1 clause violations, tabu flips with random perturbation on stall), 4 niced processes:
- earlier pass: ~25 min x 4 at t=32 n=1012, t=36 n=1260, t=38 n=1379, t=39 n=1420;
- 10:09-~10:59 ET: t=32 and t=36 one cell past the new bounds, from prefix-padded and reversed seeds;
- 11:13-12:02 ET: t=32, t=36, and t=34 n=1144 / t=37 n=1339 seeded from the AKS certificates.
Best state at every target: 1 violated clause. **No further improvement.** Unbounded follow-up runs were relaunched (logs run4/long_*); any gain will be reported separately.

## Verification
Two skeptics wrote independent checkers (skA_check.py brute force; skB/sk.py re-parsing the AKS TeX). Both ACCEPT; both confirm pads are maximal and planted violations are caught. Novelty check: OEIS A171081 lists only Marcano's a(31), a(33); Marcano (Zenodo 21943190) states t=32 not surpassed; Luo Zixuan records cover t=39 (Zenodo 21718186, restricted); residual risk: deleted Zenodo 21855349 (contents unknown).

## Certificates (sha256)
- NEW_t32_n1011.txt  4b3b2305b7e65ac73e99211078e7891e834a44bfc2b372adf50a8f29d0d9e3c6
- NEW_t36_n1259.txt  f26c9eb66cbb5b6405b1bd884f051be92472affa22ee26ad66165ff1d8965ed1
Convention: '0' has no 3-AP, '1' has no t-AP; position i of file = element i.

## Reproduce
    unzip vdw-w23t-hunt58.zip && cd vdw-w23t-hunt58
    python3 skA_check.py        # expect OK for both
    sha256sum certs/NEW_*.txt

Author: theesfeld (william@theesfeld.net)
