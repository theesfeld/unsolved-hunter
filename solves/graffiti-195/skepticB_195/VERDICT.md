# Skeptic B verdict — Graffiti 195

Independent check. Did **not** read `graffiti195/REPORT.md` or `skepticA_195/`.

## Statement (two Ev conventions)

For a connected simple graph \(G\) on \(n\ge 2\) vertices, write
\(\mathrm{Od}(v)=\#\{u\neq v:d(u,v)\text{ odd}\}\).

- **Excl (Roucairol / code):** \(\mathrm{Ev}_x(v)=\#\{u\neq v:d(u,v)\text{ even}\}=n-1-\mathrm{Od}(v)\).  
  Claim: \(\sum\mathrm{Od}\le\sum\mathrm{Ev}_x \implies \lambda_1(A(G))\le\max\mathrm{Ev}_x\).
- **Incl (Brewster glossary / WoW-style):** \(\mathrm{Ev}_i(v)=\mathrm{Ev}_x(v)+1=n-\mathrm{Od}(v)\) (counts distance 0).  
  Claim: \(\sum\mathrm{Od}\le\sum\mathrm{Ev}_i \implies \lambda_1(A(G))\le\max\mathrm{Ev}_i\).

Brewster–Dinneen–Faber (Discrete Math. 1995) glossary: *“Even vector … number of vertices an even distance (**including zero**) from vertex \(i\).”*  
Roucairol–Cazenave refutation code (`even_vec`) **excludes** the vertex. Both theorems are checked below; both hold.

Historical Graffiti 195 is the open row in Roucairol–Cazenave (arXiv:2409.18626 / ECAI 2025): still open under search up to size 50, “any graph.” Exact WoW wording was not recovered here; the claim above matches that codebase’s conjecture 195 and the parent’s formulation.

## Proof chain (stress-tested)

Let \(G'\) be the **odd-distance graph**: \(V(G')=V(G)\), \(uv\in E(G')\) iff \(d_G(u,v)\) is odd.

1. **Monotonicity.** Every edge of \(G\) has length 1 (odd), so \(A(G)\le A(G')\) entrywise. Spectral radius is monotone for nonnegative matrices, hence \(\lambda_1(G)\le\lambda_1(G')\). Also \(G'\) is simple (no loops) and connected (contains connected \(G\)). Degrees in \(G'\): \(\deg_{G'}(v)=\mathrm{Od}(v)\), so \(\delta':=\delta(G')=\min\mathrm{Od}\), \(\max\mathrm{Ev}_x=n-1-\delta'\), \(\max\mathrm{Ev}_i=n-\delta'\). Edge count \(m'=|E(G')|\) satisfies \(\sum\mathrm{Od}=2m'\).

2. **Hong–Shu–Fang (JCTB 2001).** For connected simple \(H\) with \(n\) verts, \(m\) edges, min degree \(\delta\),
   \[
   \lambda_1(H)\le\frac{\delta-1+\sqrt{(\delta+1)^2+4(2m-\delta n)}}{2}.
   \]
   (Equivalently Nikiforov’s form \(\frac{\delta-1}{2}+\sqrt{2m-n\delta+(\delta+1)^2/4}\).) Apply to \(G'\).

3. **Hypothesis → edge bound on \(G'\).**  
   - Excl: \(\sum\mathrm{Od}\le\sum\mathrm{Ev}_x\iff 4m'\le n(n-1)\).  
   - Incl: \(\sum\mathrm{Od}\le\sum\mathrm{Ev}_i\iff 4m'\le n^2\).

4. **Algebraic close.** Let \(\mathrm{HSF}(n,m,\delta)\) be the HSF upper bound.  
   - **Excl:** Under \(4m\le n(n-1)\) and the handshaking constraint \(\delta\le(n-1)/2\) (forced at that edge count),  
     \(\mathrm{rhs}^2-\Delta\big|_{m=n(n-1)/4}=2(2\delta-n)(2\delta-n+1)\ge 0\),  
     so \(\mathrm{HSF}\le n-1-\delta=\max\mathrm{Ev}_x\). Equality at \(n\) odd, \(\delta=(n-1)/2\), \(m=n(n-1)/4\).  
   - **Incl:** At \(m=n^2/4\), \(\mathrm{rhs}^2-\Delta=2n(n-2)\ge 0\) for \(n\ge 2\), and \(n^2\le 2n(n-1)\) for \(n\ge 2\), so \(\mathrm{HSF}\le n-\delta=\max\mathrm{Ev}_i\).

Therefore \(\lambda_1(G)\le\lambda_1(G')\le\mathrm{HSF}(G')\le\max\mathrm{Ev}\).

**No gap found** in the reduction or the HSF step. \(\delta'\ge 1\) for connected \(n\ge 2\) (neighbors lie at odd distance).

## Prior art

- Listed **open** in Roucairol–Cazenave 2024/25 (no counterexample ≤50).  
- HSF bound is classical (2001); odd-/even-distance graphs appear elsewhere, but no prior published closure of Graffiti 195 was found (searches: Aouchiche–Hansen survey lineage, Brewster et al., Nikiforov spectral-radius notes, “odd-distance graph” + spectral radius).  
- So this is a **new short proof**, not a rediscovery of a famous named theorem.

## Numeric adversarial search (independent)

| Battery | Result |
|--------|--------|
| Random connected (GNP, trees, bipartite±edges, lollipops, BA), \(n\le 29\), 24710 graphs | excl feas. 7860, max margin \(\approx 0\), **0 hits**; incl feas. 18328, max margin \(\approx 0\), **0 hits**; **0 proof-chain failures** |
| Near-threshold \(K_{a,b}+\) same-part edges | best excl margin \(\approx -0.76\) |
| Pineapple / kite family | best incl margin \(\approx -0.83\) |
| Exhaustive `geng -c` \(n=3..8\) | 0 hits either convention |
| Prior campaign in tree (exh \(n\le 10\), SA \(n\le 14\)) | consistent: no refutation |

Margins approach 0 (e.g. some \(n=4,5,6,8\) incl cases) but do not go positive.

## “Solved” — fair or stretched?

**Fair.** Unlike Graffiti 322 (near-trivial classical spread + InverseEven \(\le n\)), this needs a real spectral bound plus the odd-distance reduction; it was still open in 2025 search work. Ev include-vs-exclude is an ambiguity of the historical wording, but **both** precise theorems are true, so the claim is not propped up by a definitional trick.

Caveat only: if some WoW copy used a different third reading of “maximum of even / sum condition,” that copy was not checked; the statement as used by Roucairol and as stated in the task is settled.

VERDICT: ACCEPT
