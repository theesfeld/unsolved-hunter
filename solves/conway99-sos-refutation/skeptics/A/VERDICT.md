# Skeptic A Verdict — Natal & Al-saadi arXiv:2610.16266 Conjecture 5

**Reviewer:** Skeptic A (independent; no files read from `/workspace/unsolved/conway99-sos/`)  
**Paper:** Natal & Al-saadi, *Towards a Sum-of-Squares Proof for the Nonexistence of Conway’s 99-graph*, arXiv:2610.16266v1 (12 Oct 2026)  
**Date:** 2026-10-15 (America/New_York)

---

## Verdict lines (verbatim for parent)

**REJECT** on the paper's claim "T(99)≤55 for D-free and K2,3-free graphs"

**REJECT** on "this proves Conway 99 nonexistent"

---

## What the paper actually claims

Fetched from `https://arxiv.org/pdf/2610.16266.pdf` (local: `paper.pdf`, text: `paper.txt`).

- **Lemma 1:** Any srg(99,14,1,2) is diamond-free and K_{2,3}-free (as subgraphs).
- **Theorem 3:** Any such srg has exactly **231** triangles.
- **Conjecture 5 (experimental):** For simple graphs on n vertices with no diamond and no K_{2,3} subgraph,
  \[
  T(99) \le 55.
  \]
  Obtained via Lasserre level-5 / flag-algebra style SDP (Brosch); residuals claimed \(O(10^{-9})\). Authors state the SoS certificate **still needs formalizing**, and that the bound is a **loose upper bound** from a relaxation.
- They infer nonexistence: 55 < 231 ⇒ no Conway 99-graph.

The SDP maximizes triangle density subject only to the two forbidden-subgraph constraints — **not** 14-regularity or full strong regularity.

---

## Own triangle count and forbidden-subgraph checks

### Characterizations used (as specified)

- Diamond-free ⇔ no two **adjacent** vertices have ≥2 common neighbors.
- K_{2,3}-free (as a subgraph) ⇔ no two vertices have ≥3 common neighbors.

### Brick: srg(9,4,1,2) reconstructed from scratch

3×3 lattice / rook’s graph: vertices \((r,c)\in\{0,1,2\}^2\), edge iff same row or same column.

| Check | Result |
|-------|--------|
| Parameters via \(A^2 = kI + \lambda A + \mu(J-I-A)\) | srg(9,4,1,2) ✓ |
| Triangles \(\mathrm{tr}(A^3)/6\) | **6** (= \(9\cdot4\cdot1/6\)) |
| Diamond-free | True (max common neighbors on edges = 1) |
| K_{2,3}-free | True (max common neighbors any pair = 2) |

### Counterexample on 99 vertices

**Construction:** disjoint union of **11** copies of the lattice graph (exactly 99 vertices).

| Check | Result |
|-------|--------|
| \(n\) | 99 |
| Edges | 198 |
| Degrees | all 4 |
| Triangles | **66** (= \(11 \times 6\)) |
| Diamond-free | **True** |
| K_{2,3}-free | **True** |
| Max common neighbors (adj / non-adj) | (1, 2) |

Also verified: 10 copies + 9 isolates ⇒ **60** triangles, still D-free and K_{2,3}-free, still \(> 55\).

**Conclusion:** \(T(99) \ge 66 > 55\). Conjecture 5 is **false**.

(Disconnected graphs are allowed: the paper’s \(\mathcal{G}_n\) is “simple graphs on \(n\) vertices,” with no connectedness hypothesis.)

Constructive lower bound along this family: \(T(n) \ge 6\lfloor n/9\rfloor\) (so already at \(n=90\), LB = 60 > 55).

---

## Does the argument settle Conway 99 even if the bound were true?

**Logically, almost:** any srg(99,14,1,2) is in the D-free + K_{2,3}-free class (Lemma 1) and needs 231 triangles (Theorem 3). An upper bound of 55 on **all** such graphs would rule out the srg. Omitting degree-regularity / strong regularity from the SDP is fine for that style of argument (a larger feasible set can only raise the max).

**In reality, no:**

1. The claimed bound \(T(99)\le 55\) is **false** (counterexample above).
2. The paper itself labels this **Conjecture 5** and says the SoS certificate still needs formalizing — so even on their own terms it is not a completed nonexistence proof.
3. The numerical SDP (if it truly returned ≤55) cannot be a valid upper bound on the stated feasible set, since a feasible point with 66 triangles exists; residual claims do not override an explicit construction.

**Honesty note:** Disproving Conjecture 5 does **not** construct an srg(99,14,1,2). Our counterexample is 4-regular, not 14-regular, and is disconnected. Conway’s 99-graph remains open from this reviewer’s work.

---

## Code filenames written

| File | Role |
|------|------|
| `verify_counterexample.py` | Full reconstruction, SRG check, triangle count, diamond / K_{2,3} checks, builds and asserts the 99-vertex counterexample |
| `counterexample_99.npy` | Saved 99×99 adjacency matrix of the counterexample |
| `paper.pdf` / `paper.txt` / `paper.html` | Local copy of the arXiv paper |
| `VERDICT.md` | This document |

Run: `python3 verify_counterexample.py` (numpy only; seconds; niced).

---

## One-paragraph plain-language summary

Natal & Al-saadi conjecture that any diamond-free, K_{2,3}-free graph on 99 vertices has at most 55 triangles, and treat that as killing Conway’s 99-graph (which would need 231). Independently reconstructing the unique 9-vertex strongly regular graph with parameters (9,4,1,2) and taking eleven disjoint copies yields a perfectly legal 99-vertex graph under their two forbidden-subgraph rules with **66** triangles — so the ≤55 claim is false, and their experimental SoS bound cannot prove nonexistence. Even if the bound had been true, they still owe a formal certificate; as written, Conjecture 5 does not settle Conway 99.
