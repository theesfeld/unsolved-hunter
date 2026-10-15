# Refutation of Natal–Al-saadi (arXiv:2610.16266) triangle bound for Conway's 99-graph

**Status:** CONFIRMED (passed the skeptic gate) — the paper's experimental claim is false. Conway's 99-graph existence problem remains **open**.

**Date:** 2026-10-15  
**Short name:** `conway99-sos-refutation`  
**Folder:** [solves/conway99-sos-refutation](https://github.com/theesfeld/unsolved-hunter/tree/main/solves/conway99-sos-refutation)  
**DOI:** [10.5281/zenodo.23399271](https://doi.org/10.5281/zenodo.23399271) · [Zenodo record](https://zenodo.org/records/23399271)

## Statement

Natal & Al-saadi (arXiv:2610.16266v1, 12 Oct 2026) claim that every simple graph on 99 vertices with no diamond subgraph and no \(K_{2,3}\) subgraph has at most 55 triangles (Conjecture 5 / Lasserre experiment). Since any \(\mathrm{srg}(99,14,1,2)\) has exactly 231 triangles, they conclude that Conway's 99-graph does not exist.

We give explicit counterexamples with **66** and **120** triangles obeying both constraints (including connected graphs). Conjecture 5 is false; the paper does **not** resolve Conway's problem.

## Background

Conway's $\$1000$ problem asks whether \(\mathrm{srg}(99,14,1,2)\) exists. The triangle count 231 is classical. As of 2026-10-15 the existence question remains open (Thakkar–Severini reductions; Labianco branch exclusions; ongoing SAT work). The Natal–Al-saadi manuscript labels the key inequality a *conjecture* and states that a formal sum-of-squares certificate remains future work.

Paper (do not redistribute the PDF here): [arXiv:2610.16266](https://arxiv.org/abs/2610.16266).

## Forbidden-subgraph dictionary

- **Diamond-free:** no adjacent pair has ≥2 common neighbors.
- **\(K_{2,3}\)-free (as a subgraph):** no pair of vertices has ≥3 common neighbors.

Necessary for \(\lambda=1\), \(\mu=2\), but not sufficient for strong regularity.

## Counterexamples

### Packing of \(\mathrm{srg}(9,4,1,2)\) (66 triangles)

Let \(L\) be the unique \(\mathrm{srg}(9,4,1,2)\) (3×3 lattice / Paley(9)). It has 6 triangles and is diamond-free and \(K_{2,3}\)-free. The disjoint union of **11** copies of \(L\) has 99 vertices and
\[
11\times 6 = 66 > 55
\]
triangles. Path-bridging the blocks with 10 edges yields a **connected** graph with the same triangle count and the same common-neighbor bounds \((1,2)\).

Reproduce: `python3 build_counterexample.py`

### Hamming packing (120 triangles, connected) — strongest

Let \(H=H(4,3)=K_3\square K_3\square K_3\square K_3\) (81 vertices, 108 triangles, max common neighbors 1 on edges and ≤2 off edges). Add two copies of Paley(9) and two bridge edges. The resulting connected graph \(C\) on 99 vertices has **120** triangles and remains diamond-free and \(K_{2,3}\)-free.

Reproduce (Skeptic B's independent code): `python3 skeptics/B/verify.py`

### Extra: Fig. 2 “\(K_{2,3}\)-only” claim

24 disjoint \(K_4\) plus 3 isolates is \(K_{2,3}\)-free with 96 triangles, so the caption claim that the bound is unchanged under only the \(K_{2,3}\) constraint is also false (`skeptics/B/k23_only.py`).

## Why the nonexistence implication fails

An upper bound cannot sit below a triangle count achieved by an explicit graph. Since \(T(99)\ge 120>55\), the reported SoS/Lasserre number cannot be a valid bound on the stated class. Without that bound, the paper only restates known facts (Lemma 1 and the 231-triangle count). Conway's problem stays open.

## Skeptic verdicts

### Skeptic A — REJECT bound; REJECT “proves nonexistent”

Independent rebuild: 11× lattice \(\mathrm{srg}(9,4,1,2)\) → 66 triangles, constraints verified. See `skeptics/A/VERDICT.md` and `skeptics/A/verify_counterexample.py`.

### Skeptic B — REJECT bound; REJECT “proves nonexistent”

Independent rebuild: connected Hamming+Paley graph \(C\) → **120** triangles; also confirms the 66-triangle packing. See `skeptics/B/VERDICT.md` and `skeptics/B/verify.py`.

Both skeptics started fresh, wrote their own code, and did not share workspaces with each other or with the hunt lead’s first draft directory during verification.

## Reproduction

```bash
python3 build_counterexample.py          # 66-triangle packing
python3 skeptics/B/verify.py             # 120-triangle connected C
python3 skeptics/B/k23_only.py           # K2,3-only side check
```

## Honest caveats

- This refutes the **triangle-bound nonexistence argument**, not the existence of \(\mathrm{srg}(99,14,1,2)\) itself.
- We did not re-run the authors’ Julia/Lasserre pipeline; a modelling or solver error is the likely source of “55”.
- Results here are **not externally peer reviewed** (internal skeptic gate only).
- Suggested next step for the community: notify the authors / leave an arXiv comment with the counterexamples (draft below for the repo owner — not sent automatically).

## Suggested author note (draft — not sent)

> We enjoyed your preprint arXiv:2610.16266. Conjecture 5 appears to be false: the connected graph formed from the Hamming graph H(4,3) plus two copies of Paley(9), joined by two bridges, is diamond-free and K_{2,3}-free on 99 vertices with 120 triangles (also: 11×Paley(9) gives 66). So the reported T(99)≤55 bound cannot hold, and the nonexistence conclusion for srg(99,14,1,2) does not follow. Happy to share code: https://github.com/theesfeld/unsolved-hunter/tree/main/solves/conway99-sos-refutation

## References

- J. Natal, O. Al-saadi, arXiv:2610.16266, 2026.
- A. E. Brouwer & H. Van Maldeghem, *Strongly Regular Graphs*, CUP, 2022.
- J. H. Conway, Five \$1000 problems (OEIS A248380 notes).
