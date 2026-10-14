# Skeptic A — Graffiti 195 verdict (independent)

Workdir only. Did **not** read `graffiti195/REPORT.md` or `skepticB_195/`.

## Statement

For connected simple \(G\) on \(n\ge 2\):
- \(\mathrm{Od}(v)=\#\{u:d(u,v)\text{ odd}\}\)
- **Incl (WoW / Brewster glossary):** \(\mathrm{Ev}_i(v)=\#\{u:d(u,v)\text{ even}\}\) including \(u=v\); claim \(\sum\mathrm{Od}\le\sum\mathrm{Ev}_i\implies\lambda_1(A(G))\le\max\mathrm{Ev}_i\)
- **Excl (Roucairol code):** \(\mathrm{Ev}_x(v)=\mathrm{Ev}_i(v)-1\); same claim with \(\mathrm{Ev}_x\)

Both match the open Graffiti 195 row in Roucairol–Cazenave (arXiv:2409.18626): refute when \(\mathrm{index}-\max\mathrm{Ev}>0\) and \(\mathrm{odd}\le\mathrm{pair}\).

## Proof chain (re-audited)

Let \(G'\) be the odd-distance graph: \(uv\in E(G')\) iff \(d_G(u,v)\) is odd. Then \(\deg_{G'}(v)=\mathrm{Od}(v)\), \(m'=|E(G')|\), \(\delta'=\min\mathrm{Od}\).

| Step | Claim | Verdict |
|------|--------|---------|
| 1 | Every edge of \(G\) has odd length 1 ⇒ \(G\subseteq G'\) | **TRUE** |
| 2 | \(\lambda_1(G)\le\lambda_1(G')\) (monotone spectral radius) | **TRUE** |
| 3 | Hong–Shu–Fang (JCTB 2001): \(\lambda_1(G')\le\mathrm{HSF}=\frac{\delta'-1+\sqrt{(\delta'+1)^2+4(2m'-\delta'n)}}{2}\) | **TRUE** (classical; \(G'\) connected simple) |
| 4a | Hyp Incl \(\Leftrightarrow 4m'\le n^2\); Excl \(\Leftrightarrow 4m'\le n(n-1)\) | **TRUE** |
| 4b | Under hyp + handshaking \(2m'\ge\delta'n\): \(\mathrm{HSF}\le\max\mathrm{Ev}\) | **TRUE** (see algebra) |

**Algebra (Incl).** Want \(\mathrm{HSF}\le n-\delta'\). Equivalent (when RHS of the sqrt step is nonnegative) to \(\mathrm{Disc}\le(2n-3\delta'+1)^2\). At the worst edge count \(m'=n^2/4\),
\[
(2n-3\delta'+1)^2-\mathrm{Disc}=2(2\delta'-n)(2\delta'-n-2).
\]
This is nonnegative for every integer \(\delta'\) feasible under handshaking (\(\delta'\le n/2\)): the only integer root of a negative product would be \(\delta'=(n+1)/2\) (odd \(n\)), which violates \(\delta'\le n/2\). Under hyp, \(\delta'\le n/2\) also forces \(2n-3\delta'+1\ge n/2+1>0\), so squaring is valid. Hence \(\mathrm{HSF}\le n-\delta'=\max\mathrm{Ev}_i\).

**Algebra (Excl).** Same argument at \(m'=n(n-1)/4\): difference factors as \(2(2\delta'-n)(2\delta'-n+1)\ge 0\) for all integer \(\delta'\), and \(\mathrm{HSF}\le n-1-\delta'=\max\mathrm{Ev}_x\).

**Important correction to an earlier hole note.** The crude bound \(\sqrt{2m'-n+1}\) is exactly HSF at \(\delta'=1\). It fails on easy graphs (e.g. \(P_4\): \(\sqrt5>2=\max\mathrm{Ev}_i\)) and is **not** the HSF theorem used above. Full HSF on \(P_4\) gives exactly \(2\). Early scripts that only tested the \(\delta'=1\) special case incorrectly flagged a proof gap.

Therefore \(\lambda_1(G)\le\lambda_1(G')\le\mathrm{HSF}(G')\le\max\mathrm{Ev}\).

## Numerics (own code)

| Battery | Incl (WoW) | Excl (code) |
|---------|------------|-------------|
| Atlas connected \(n\le 7\) | 511 hyp, **0 viol**; HSF\(\le\max\mathrm{Ev}\) on all 510 (\(n\ge2\)) | 66 hyp, **0 viol**; HSF ok on all 65 |
| Families ~2500 graphs | 1998 hyp, **0 viol** | 711 hyp, **0 viol** |
| Random GNP hyp sample (~2200) | HSF chain **0 fails**; concl **0 viol** | same |
| Equality (Incl HSF\(=\max\mathrm{Ev}\)) | even \(n\), \(\delta'=n/2\), \(m'=n^2/4\) (e.g. \(C_4\), \(K_{3,3}\)-type) | odd \(n\), \(\delta'=(n-1)/2\) |

No counterexample found; consistent with Roucairol–Cazenave (open under search to size 50, no refutation).

## Fairness: fair vs stretched

**Fair.** Unlike Graffiti 322 (classical distance spread \(\ge n\) plus the trivial \(\mathrm{InverseEven}\le n\)), this needs a nontrivial spectral bound (HSF 2001) plus the odd-distance reduction. The conjecture was still listed open in 2024/25 search work. Ev include-vs-exclude is ambiguous in historical wording, but **both** precise theorems are proved by the same chain — not propped up by a definitional trick.

Caveat (not a stretch): under Incl, every connected bipartite graph satisfies the hypothesis automatically (\(\sum\mathrm{Od}=2ab\le a^2+b^2=\sum\mathrm{Ev}_i\)), and \(\lambda_1\le\sqrt{ab}\le\max(a,b)\) is elementary — so the bipartite slice is easy. The uniform HSF argument still covers it, and the non-bipartite / triangle-in-\(G'\) content is genuine.

VERDICT: ACCEPT
