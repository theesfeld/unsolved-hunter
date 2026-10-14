# Skeptic A — Graffiti conjecture 195 (independent)

Workdir only. Did **not** read graffiti195/REPORT.md or proof notes.

## 1. Formalization

**Glossary (Brewster–Dinneen–Faber / WoW):**
- `Odd(v)` = #{u : d(u,v) odd}
- `Ev(v)` = #{u : d(u,v) even} **including u=v (distance 0)**
- For connected G on n vertices: `Ev(v)+Odd(v)=n`, and `Σ_v Ev(v)+Σ_v Odd(v)=n²`.

**Reading A (WoW / usual):** Ev includes self.
**Reading B (Roucairol refutationGBR code):** `even_vec` skips `vert==vert2`, so Ev_code(v)=Ev_WoW(v)−1; Σ Ev_code = Σ Ev_WoW − n. Odd unchanged.

**Conjecture 195 (both readings):**
> If G is connected and `Σ Odd(v) ≤ Σ Ev(v)`, then `λ₁(A(G)) ≤ max_v Ev(v)`.

Matches Roucairol score for 195: refute when `index - max_ev > 0` and `odd ≤ pair`.

## 2. Alleged proof — step audit

**Setup:** G′ = odd-distance graph on V(G): uv∈E(G′) iff d_G(u,v) odd.
- deg_{G′}(v)=Odd(v), m(G′)=(1/2)Σ Odd.

| Step | Claim | Verdict |
|------|--------|---------|
| 1 | Every edge of G has odd length 1 ⇒ G ⊆ G′ (spanning subgraph) | **TRUE** |
| 2 | Hence λ₁(G) ≤ λ₁(G′) | **TRUE** (monotonicity of spectral radius under edge addition) |
| 3a | Bound λ₁(G′) by Hong–Shu–Fang: λ₁ ≤ √(2m−n+1) | Bound is valid, but... |
| 3b | ...and show √(2m′−n+1) ≤ max Ev under hyp | **FALSE** as a universal step |
| 3c | Same with Nikiforov-style √(2m) or degree bound Δ(G′)=max Odd | **FALSE** as universal steps |

### Concrete hole (Reading A)
P₄: Σ Odd=Σ Ev=8 (hyp holds), max Ev=2, λ₁(P₄)=φ≈1.618 ≤ 2 (concl holds).
G′ ≅ C₄, m′=4: Hong √(8−4+1)=√5≈2.236 **> 2 = max Ev**. Nikiforov √8≈2.828 > 2.
So “Hong/Nikiforov under hyp ⇒ ≤ max Ev” **does not hold**.

Atlas ≤7, Reading A, among hyp graphs:
- Hong(G′) > max Ev in **141/511**
- √(2m′) > max Ev in **192/511**
- max Odd > max Ev in **50/511**
Yet λ₁(G)≤max Ev in **all** 511; also λ₁(G′)≤max Ev empirically in all tested.

### Partial salvage (not in alleged proof)
Under hyp, m′ ≤ n²/4 and avg Ev ≥ n/2 so max Ev ≥ n/2.
If G′ is **triangle-free**, Nosal ⇒ λ₁(G′) ≤ √(m′) ≤ n/2 ≤ max Ev. **Closes** that subcase.
When G is bipartite, G′=K_{a,b} is triangle-free — covered.
**Hard residue:** hyp + G′ contains a triangle (typical non-bipartite). Alleged degree-size bounds still overshoot; no closed estimate from Hong/Nikiforov.

### Reading B
Same logical hole (rarer hyp). Atlas hyp 66/996; Hong fail 1/66; deg fail 46/66; no λ₁ violations found.

## 3. Code checks

Script: `verify195.py`, `dig_holes.py`, `try_proof.py`, `close_proof.py`, `final_checks.py`.

| Battery | Reading A (WoW) | Reading B (code) |
|---------|-----------------|------------------|
| Atlas connected n≤7 | 511 hyp, **0 viol** | 66 hyp, **0 viol** |
| Families (paths, cycles, stars, K_n, wheels, K_{a,b}, random trees, ER, BA, named cages, …) ~2500 graphs | 1998 hyp, **0 viol** | 711 hyp, **0 viol** |
| Targeted random / bipartite+chords | best (λ₁−max Ev) ≈ 0 (equality), **0 viol** | same |

Equality examples (WoW): K₂; C₄; K_{3,3}; and a 6-vertex non-bipartite 3-regular-ish graph with λ₁=max Ev=3.

## 4. Fairness

**Reading A (WoW) — large trivial slice:**
For connected bipartite G with parts a,b:
- Ev(v)=size of own part, Odd(v)=size of other;
- Σ Odd=2ab, Σ Ev=a²+b² ⇒ hyp ⇔ (a−b)²≥0 **always**;
- λ₁(G)≤λ₁(K_{a,b})=√(ab)≤max(a,b)=max Ev.

So under WoW, **every connected bipartite graph** is an instance, and the inequality is elementary. Hypothesis adds nothing on bipartite graphs. Nontrivial content is only non-bipartite.

**Alleged “resolution”:** Stretch. Core reduction G⊆G′ is fine, but citing Hong–Shu–Fang/Nikiforov does **not** finish the proof; those bounds exceed max Ev on easy graphs (e.g. P₄). Bipartite case is near-trivial and does not need that machinery. Non-bipartite/triangle-in-G′ case remains unproved by this idea.

**Reading B:** Less vacuous on bipartite graphs (hyp selective), still no proof via cited bounds; empirically plausible.

## 5. Status vs literature
Roucairol–Cazenave (arXiv:2409.18626): Graffiti 195 listed **open**, no counterexample to size 50. Consistent with our checks; does **not** constitute a proof.

## Verdict rationale
Claim “195 is TRUE” as established by the alleged Hong/Nikiforov-on-G′ argument: **not accepted**. Proof has a clear gap; only a proper subset is rigorously settled (bipartite / triangle-free G′). Empirics do not replace a proof for skeptic acceptance of a resolution.
