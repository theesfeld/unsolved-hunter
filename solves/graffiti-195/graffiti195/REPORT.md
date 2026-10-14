# Graffiti 195 / 219 — refutation attempt, 2026-10-14

## Sources and statements
- Roucairol–Cazenave, arXiv 2409.18626 (ECAI 2025), Table 1: 195 is open (searched "any" graphs up to n=50); 219 is open (searched K3-free graphs up to n=50). Neither was refuted.
- Brewster–Dinneen–Faber, Discrete Math 147 (1995), glossary (bdf.txt):
  - Even vector: the number of vertices at even distance from v, **including v itself**. The Rust code excludes v.
  - Gravity matrix: Gr[u,v] = (1/(n-1)) · deg(u)·deg(v) / d(u,v).
- 195 (as in the code, GenerateGraph.rs:432): if Σ odd_vec ≤ Σ even_vec, then λ1(A) ≤ max even_vec. I checked two readings:
  - 195c: the code's version, which excludes v.
  - 195w: the WoW glossary version, which includes v (+1 per vertex, +n to the sum).
- 219 (code, l.1530): λ2(Gr) ≤ n(n-1)/2 − m, i.e. at most the number of non-edges. The paper searched K3-free graphs, so the original statement presumably carries a triangle-free hypothesis. I did not obtain the WoW page itself.

## 195 — PROOF FOUND (both readings); no counterexample can exist
Let G' be the odd-distance graph (u~v iff d(u,v) is odd). Then G ⊆ G' (edges have distance 1), so λ1(G) ≤ λ1(G').
G' has δ' = min Od(v) and m' = #odd pairs.

The hypothesis gives:
- code reading: 4m' ≤ n(n-1)
- WoW reading: 4m' ≤ n²

Hong–Shu–Fang (JCTB 2001; Nikiforov 2002 for all graphs): λ1(G') ≤ (δ'−1+√((δ'+1)²+4(2m'−δ'n)))/2.

Squaring and substituting x = n−2δ':
- code: RHS² − LHS = 2x(x−1) ≥ 0 for every integer x, so λ1 ≤ n−1−δ' = max Ev_excl.
- WoW: RHS² − LHS = 2x(x+2). This is negative only when x = −1, and that case violates m' ≤ n²/4. So λ1 ≤ n−δ' = max Ev_incl.

The "RHS negative" case would need δ' > (2n−1)/3, which contradicts the m' bound.

Equality cases: (n−1)/2-regular diameter-2 graphs (Paley, C5) for the code reading; K_{a,a} for WoW.

Numeric check (verify_proof195.py): every link of the chain held on all 290,627 connected graphs with n ≤ 9 plus random G(n,p) with n = 10–60. No assertion failed.

Search margins (λ1 − maxEv, condition satisfied), all ≤ 0, as the proof requires:
- Exhaustive, n ≤ 10, code reading (exh.c + geng): best 0 at n=5 and 9 (equality); n=10 best −0.349.
- WoW reading: equality only (n = 6, 8, 10: K_{a,a}).
- n=11 exhaustive was stopped once the proof was found.
- Simulated annealing, diameter ≥ 3: best −0.48 (n=12), −0.58 (n=14).
- Asymptotic blow-up relaxation (k ≤ 5 patterns): sup = 0.
- Named and structured families (fam195.py: Paley, circulants, Kneser, coronas, atlas): ≤ 0.

Novelty is unchecked. A web search found no published proof.

## 219
- **Triangle-free (the intended scope): PROOF.**
  - If λ2 ≥ 0, then 2λ2² ≤ λ1² + λ2² ≤ ‖Gr‖_F² ≤ (Σd²)²/(n−1)².
  - Triangle-free gives Σd² = Σ_{uv∈E}(d_u+d_v) ≤ mn, so λ2 ≤ mn/((n−1)√2).
  - This is ≤ n(n−1)/2 − m whenever m ≤ n²/4 (Mantel) and n ≥ 10.
  - n ≤ 9: exhaustive check of all triangle-free graphs, including disconnected ones (best margin −16.9 at n=9).
  - Connected triangle-free graphs, exhaustive to n = 13: best −36.8. Annealing: −35 (n=12), −48.6 (n=14). The bound is very loose.
- **All graphs (no hypothesis): CANDIDATE COUNTEREXAMPLE**, recorded as a lead because the reading is uncertain.
  - G = K_n minus the edges of K_{a,a}: two a-cliques A and B, joined to a c-clique C, with no A–B edges.
  - Smallest found: n=25 (a=3, c=19), λ2 ≈ 9.1875 vs 9 non-edges; and (a=4, c=17), λ2 = 16.6667 vs 16, margin +0.667. Confirmed with two independent codes (inv.py, networkx). Family script: km219.py.
  - Margins grow with a: a=7, c=20, n=34 gives +2.21.
  - Exhaustive general connected n ≤ 9: all ≤ −2.1. The family needs n ≥ 25.
  - **Caveat:** the graph has 1980 triangles. If 219 is stated for triangle-free graphs (which the paper's K3-free search suggests), this is NOT a refutation. Someone needs to check the exact WoW text of 219.

## 292 / 295
- AGNT (agnt.gg/whitepapers) claims machine-checked proofs of both 292 and 295 (2026), plus 290 (proved) and 284 (refuted).
- The 292 archive is dated Jul 23, 2026. I skipped both as already settled.

## Status
- 195: nothing (no refutation possible). Byproduct: a short proof, novelty unverified.
- 219 triangle-free: nothing (proved).
- 219 unrestricted: lead, pending the exact statement. Not CONFIRMED.

## Files
exh.c, inv.py, sa.py, campaign.sh, fam195.py, blowup.py, verify_proof195.py, fam219.py, km219.py; out/ (raw results); paper.txt, bdf.txt.
