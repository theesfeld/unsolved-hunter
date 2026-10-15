# SKEPTIC B: VERDICT on Natal & Al-saadi, arXiv:2610.16266v1 (12 Oct 2026)

**Verdict on "T(99) ≤ 55" (Conjecture 5 / Fig. 2): REJECT (the bound is false)**
**Verdict on "this paper proves Conway's 99-graph srg(99,14,1,2) does not exist": REJECT**

## What I checked
I read the paper (paper.pdf / paper.txt here). Its argument: (i) every srg(99,14,1,2) is diamond-free and
K_{2,3}-free (Lemma 1; correct). (ii) Such a graph has exactly 231 triangles (Thm 3 / Cor 4; correct: 693 edges,
each in exactly one triangle, 693/3 = 231). (iii) A numerical SOS/Lasserre computation gives T(99) ≤ 55, where T(n) is the max number of
triangles in a {diamond, K_{2,3}}-free graph on n vertices (labelled "Conjecture 5", with no certificate). (iv) 55 < 231, so the graph does not exist.

Step (iii) is false. I wrote my own code and built explicit graphs on 99 vertices satisfying both constraints with more than 55 triangles.

Constraint tests used: no diamond ⇔ every adjacent pair has ≤1 common neighbour; no K_{2,3} ⇔ every pair has ≤2 common neighbours.
I checked both on all 4851 vertex pairs. Triangle counts were cross-checked with networkx.

## Building blocks (verified from scratch)
- Paley(9) built over GF(9)=GF(3)[i]/(i²+1): srg parameters computed = (9, 4, 1, 2). 6 triangles.
- Hamming graph H(4,3) = K3□K3□K3□K3: n=81, 8-regular, 324 edges, **108 triangles**; adjacent pairs have 1 common neighbour, non-adjacent pairs have ≤2.

## Counterexamples (n = 99)
| Graph | triangles | max common nbrs (adjacent) | max common nbrs (non-adjacent) | diamond | K_{2,3} | connected |
|---|---|---|---|---|---|---|
| A: 11 × Paley(9) | **66** | 1 | 2 | no | no | no |
| D: A + 10 bridge edges | **66** | 1 | 2 | no | no | yes |
| B: H(4,3) + 2 × Paley(9) | **120** | 1 | 2 | no | no | no |
| **C: B + 2 bridge edges (main counterexample)** | **120** | 1 | 2 | no | no | **yes** |

So T(99) ≥ 120 > 55. (Edge list of C: counterexample_C_edges.txt, 362 edges, vertices 0..98.)

Extra: the Fig. 2 caption says the bound is the same using only the K_{2,3} constraint. That is also false: 24 disjoint K4 + 3 isolated
vertices is K_{2,3}-free and has 96 triangles (k23_only.py). Graph C also satisfies each constraint separately.

## Why the paper's conclusion fails
The whole nonexistence argument depends on the numerical bound T(99) ≤ 55. The paper itself calls it a "Conjecture" and gives no certificate.
An explicit graph with 120 triangles disproves it, so the SOS/Lasserre output must come from a modelling or solver error. A valid upper bound
cannot be below a value that is actually achieved. Without that bound the paper only re-derives known facts (diamond/K_{2,3}-freeness and 231 triangles).
**Whether Conway's 99-graph exists is still open; this paper does not settle it.**

## Scripts (my own code only)
- /workspace/unsolved/skepticB_conway99sos/verify.py — builds Paley(9), H(4,3) and graphs A–D, checks every pair, cross-checks with networkx, writes results.json and the edge list
- /workspace/unsolved/skepticB_conway99sos/k23_only.py — K_{2,3}-only variant check
- /workspace/unsolved/skepticB_conway99sos/results.json, counterexample_C_edges.txt
- Reproduce: `python3 verify.py && python3 k23_only.py` (pure Python, under 1 s)

## Plain summary
The paper's key number is wrong. Taking the 81-vertex Hamming graph H(4,3) plus two copies of the 9-vertex Paley graph, joined by two edges,
gives a connected 99-vertex graph with no diamond and no K_{2,3}, and it has 120 triangles. The paper says 55 is the maximum.
So the computer bound is invalid, and the paper does not prove Conway's 99-graph is impossible.
