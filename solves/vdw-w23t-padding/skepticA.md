# Skeptic A — w(2;3,32) ≥ 1012, w(2;3,36) ≥ 1260

**Verdict: ACCEPT (valid). Novelty: MINOR, leaning NONE as a research result.**

## 1. Independent check (skA_check.py, written from scratch)
Convention: '0' = blue, must have no 3-AP; '1' = red, must have no t-AP. This matches the AKS certificates (§A.2 of main.tex: runs like 1^{15}0…, sparse 0s = the 3-AP-free class, as in Marcano's README).
- NEW_t32_n1011.txt: length 1011, alphabet {0,1}. No 3-AP in 0s, no 32-AP in 1s → **OK**. So w(2;3,32) > 1011, i.e. ≥ 1012.
- NEW_t36_n1259.txt: length 1259. No 3-AP in 0s, no 36-AP in 1s → **OK**. So w(2;3,36) ≥ 1260.
- Each file ends with the AKS certificate (aks_t32: 1006 cells, aks_t36: 1257). The prefixes are all red: 5 cells and 2 cells.
- Planted-violation tests: adding one more red cell at the front gives a red 32-AP (start 0, d=5) and a red 36-AP (start 0, d=34). Adding '000' at the front gives a blue 3-AP. The checker flags all three, so it works, and both pads are already as long as they can go.

## 2. Previous records
main.tex line 548 (Table 3): w(2;3,t) > 930, 1006, 1063, 1143, 1204, 1257, … for t = 31…39. The arXiv/ScienceDirect abstract pages show the same values. "w > n" means a valid colouring of {1..n} exists. Old: w32 ≥ 1007, w36 ≥ 1258. New: +5 and +2.

## 3. Novelty search (2026-10-16)
- OEIS A171081: improvements listed only for a(31) ≥ 954 and a(33) ≥ 1072 (Marcano, Aug 21 2026). Nothing for t=32 or t=36.
- Marcano, Zenodo 21943190 (open): w(2;3,31) ≥ 941. His paper says outright "we did not surpass t = 32 and t = 33". His later t=33 bound seems to be only in OEIS-linked files. No t=32 or t=36.
- Luo Zixuan, Zenodo 21718186: "Machine-Checkable Lower Bound Certificate: w(2;3,39) ≥ 1421". It is **restricted**, files not visible. It covers t=39, not 32/36.
- Luo Zixuan, Zenodo 21855349: **HTTP 410, deleted**. Contents unknown. This is the one residual risk.
- Web search found nothing else from 2024–2026 for t=32/36.
→ As far as anything visible shows, both bounds are new.

## 4. Worth publishing?
The bounds are valid and apparently new, but the method is trivial: put red cells in front of the AKS certificate until it breaks. Anyone with a checker could have done this. It is not a research result, and the novelty for a paper is NONE. A short OEIS A171081 comment ("a(32) ≥ 1012, a(36) ≥ 1260 by extending AKS certificates; certificates at <link>") is reasonable and in the same style as Marcano's entry, as long as it says plainly that the method is padding. Better to first try real search seeded from these padded certificates (local search, palindromic seeds) and fold any larger gain into the same comment. Do not present this as a MAJOR hunt result.
