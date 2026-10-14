---
title: "A short proof of Graffiti conjecture 195"
subtitle: "Spectral radius versus the even vector, under both even-vector conventions"
date: "Release notes, 14 October 2026"
geometry: margin=1in
fontsize: 11pt
numbersections: true
header-includes:
  - \usepackage{amsmath,amssymb,amsthm}
  - \usepackage{booktabs}
---

# Abstract {.unnumbered}

Graffiti conjecture 195 asks the following. Let $G$ be a connected graph whose sum of odd vector is at most its sum of even vector. Then the largest adjacency eigenvalue of $G$ is at most the maximum of its even vector. Roucairol and Cazenave (arXiv:2409.18626) list this conjecture as open. Their computer search over arbitrary graphs up to 50 vertices found no counterexample. There are two common conventions for the even vector, $\mathrm{Ev}(v)$: one counts $v$ itself (distance $0$) and one does not. We prove the conjecture under both.

The proof is a three-step chain:

1. $G$ is a spanning subgraph of its *odd-distance graph* $G'$.
2. Hence $\lambda_1(G)\le\lambda_1(G')$.
3. The Hong--Shu--Fang (2001) upper bound applied to $\lambda_1(G')$ is at most $\max\mathrm{Ev}$. This step uses the hypothesis, rewritten as an edge bound on $G'$, together with the handshake inequality.

The final step reduces to $2x(x+2)\ge 0$ when $v$ is counted and to $2x(x-1)\ge 0$ when it is not, where $x=n-2\delta(G')$.

We characterise the equality cases. Equality holds exactly for the $n/2$-regular graphs when $v$ is counted, and exactly for the $(n-1)/2$-regular graphs when it is not.

Each link of the chain was checked numerically on 290,627 connected graphs, with no failure. Two independent skeptic reviews accepted the proof. The result has **not** been externally peer reviewed. Also, the original "Written on the Wall" (WoW) wording of conjecture 195 was not recovered.

# Background

*Graffiti* is S. Fajtlowicz's conjecture-generating computer program. Its conjectures were collected in the document "Written on the Wall" (WoW). Brewster, Dinneen and Faber (Discrete Math. 147 (1995) 35--55; see [REFERENCES.md](../../REFERENCES.md#brewster-dinneen-faber-1995)) give a glossary of Graffiti invariants. That glossary defines:

> **Even vector.** The vector whose $i$th component is the number of vertices an even distance (including zero) from vertex $i$.

Roucairol and Cazenave, *Refutation of Spectral Graph Theory Conjectures with Search Algorithms* (arXiv:2409.18626v1, 27 Sep 2024; ECAI 2025; file `paper.txt`), applied search algorithms to a selection of Graffiti conjectures.

- In their Table 1, conjecture 195 is listed as open ("O"), searched up to size 50 in the "any graph" space, with no refutation.
- The text says: "For Graffiti 189 and 195, we first searched in the 'any graph' search space ... and then verified if the graph in question complied with the conjecture definition."
- Their public code (`refutationGBR`, `GenerateGraph.rs`, line 432 onward) counts a refutation when `index - max_ev > 0` and `odd <= pair`. Here `pair` and `odd` are the sums of `even_vec` and `odd_vec`.
- `even_vec` (`invariants.rs`, line 187) skips `vert == vert2`. That is, the code **excludes** the vertex itself, unlike the glossary.

This disagreement between conventions is why we prove both versions.

# Precise statement

Let $G$ be a finite, simple, connected graph on $n$ vertices with distance function $d$. Let $\lambda_1(G)$ be the largest eigenvalue of its adjacency matrix. For $v\in V(G)$ define
$$
\mathrm{Od}(v)=\#\{u: d(u,v)\ \text{odd}\},\qquad
\mathrm{Ev}_i(v)=\#\{u: d(u,v)\ \text{even}\}\ (\text{including } u=v),
$$
$$
\mathrm{Ev}_x(v)=\#\{u\ne v: d(u,v)\ \text{even}\}=\mathrm{Ev}_i(v)-1 .
$$
Since $G$ is connected, every $u$ has a finite distance from $v$, so
$$
\mathrm{Ev}_i(v)=n-\mathrm{Od}(v),\qquad \mathrm{Ev}_x(v)=n-1-\mathrm{Od}(v).
$$

**Theorem A (including the vertex; WoW/glossary convention).** If $\sum_v \mathrm{Od}(v)\le\sum_v\mathrm{Ev}_i(v)$, then $\lambda_1(G)\le\max_v \mathrm{Ev}_i(v)$.

**Theorem B (excluding the vertex; Roucairol--Cazenave code convention).** If $\sum_v \mathrm{Od}(v)\le\sum_v\mathrm{Ev}_x(v)$, then $\lambda_1(G)\le\max_v \mathrm{Ev}_x(v)$.

For $n=1$ both theorems are trivial ($\lambda_1=0$). From now on, $n\ge 2$.

# Proof

## The odd-distance graph

Let $G'$ be the graph on $V(G)$ in which $uv$ is an edge if and only if $d(u,v)$ is odd. Write $m'=|E(G')|$ and $\delta'=\delta(G')$.

1. $G'$ is simple, since $d(v,v)=0$ is even, so $G'$ has no loops.
2. $\deg_{G'}(v)=\mathrm{Od}(v)$. Hence $\sum_v\mathrm{Od}(v)=2m'$ and $\delta'=\min_v\mathrm{Od}(v)$.
3. Every edge of $G$ has length $1$, which is odd. So $G\subseteq G'$, and $G'$ is a spanning supergraph of $G$. In particular $G'$ is connected and $\delta'\ge 1$.
4. $\max_v\mathrm{Ev}_i(v)=n-\delta'$ and $\max_v\mathrm{Ev}_x(v)=n-1-\delta'$.

## The hypothesis as an edge bound

Using $\sum_v\mathrm{Ev}_i=n^2-2m'$ and $\sum_v\mathrm{Ev}_x=n(n-1)-2m'$:
$$
\text{(A)}\ \ \textstyle\sum\mathrm{Od}\le\sum\mathrm{Ev}_i \iff 4m'\le n^2,\qquad
\text{(B)}\ \ \textstyle\sum\mathrm{Od}\le\sum\mathrm{Ev}_x \iff 4m'\le n(n-1).
$$
The handshake inequality $n\delta'\le 2m'$ then gives
$$
\text{(A)}\ \ \delta'\le n/2,\qquad \text{(B)}\ \ \delta'\le (n-1)/2 .
$$
Write $x=n-2\delta'$, an integer. Then $x\ge 0$ in case (A) and $x\ge 1$ in case (B).

## Spectral monotonicity

The adjacency matrices satisfy $0\le A(G)\le A(G')$ entrywise. The spectral radius of a nonnegative matrix is monotone under entrywise domination (Perron--Frobenius). Hence
$$
\lambda_1(G)\le\lambda_1(G'). \tag{1}
$$

## The Hong--Shu--Fang bound

**Theorem (Hong--Shu--Fang, J. Combin. Theory Ser. B, 2001; extended to all graphs by Nikiforov, 2002).** Let $H$ be a connected simple graph with $n$ vertices, $m$ edges and minimum degree $\delta$. Then
$$
\lambda_1(H)\le \frac{\delta-1+\sqrt{(\delta+1)^2+4(2m-\delta n)}}{2}.
$$
Nikiforov's equivalent form is $\frac{\delta-1}{2}+\sqrt{2m-n\delta+(\delta+1)^2/4}$.

Write $\mathrm{HSF}(n,m,\delta)$ for the right-hand side. Since $2m\ge\delta n$, the radicand is at least $(\delta+1)^2>0$. Also, HSF is strictly increasing in $m$. Applying the theorem to the connected graph $G'$ gives
$$
\lambda_1(G')\le \mathrm{HSF}(n,m',\delta'). \tag{2}
$$

## The algebraic step

Let $T$ be the target: $T=n-\delta'$ in case (A) and $T=n-1-\delta'$ in case (B). Let $\Delta(m)=(\delta'+1)^2+4(2m-\delta' n)$ be the radicand. Then
$$
\mathrm{HSF}(n,m',\delta')\le T \iff \sqrt{\Delta(m')}\le 2T-\delta'+1 .
$$

**Case (A).** Here $2T-\delta'+1=2n-3\delta'+1\ge 2n-\tfrac32 n+1=\tfrac n2+1>0$. Squaring is therefore an equivalence, and it is enough to show $\Delta(m')\le(2n-3\delta'+1)^2$. Because $\Delta$ is increasing in $m$ and $m'\le n^2/4$, it suffices to check $m=n^2/4$:
$$
(2n-3\delta'+1)^2-\big[(\delta'+1)^2+2n^2-4n\delta'\big]
=2n^2-8n\delta'+8\delta'^2+4n-8\delta'
=2x^2+4x=2x(x+2).
$$
This is $\ge 0$ because $x\ge 0$. Hence $\mathrm{HSF}\le n-\delta'=\max\mathrm{Ev}_i$.

**Case (B), checked carefully.** Here $2T-\delta'+1=2(n-1-\delta')-\delta'+1=2n-3\delta'-1$. Since $\delta'\le(n-1)/2$, this is at least $2n-\tfrac32(n-1)-1=\tfrac{n+1}{2}>0$, so squaring is again an equivalence. With $m'\le n(n-1)/4$, the worst case is $m=n(n-1)/4$:
$$
(2n-3\delta'-1)^2-\big[(\delta'+1)^2+2n(n-1)-4n\delta'\big]
=2n^2-8n\delta'+8\delta'^2-2n+4\delta'
=2x^2-2x=2x(x-1).
$$
This is $\ge 0$ because $x\ge 1$. It is in fact $\ge 0$ for every integer $x$. Hence $\mathrm{HSF}\le n-1-\delta'=\max\mathrm{Ev}_x$.

We double-checked both identities symbolically with SymPy. The factored forms are $2(n-2\delta')(n-2\delta'+2)$ and $2(n-2\delta')(n-2\delta'-1)$. These match Skeptic A's factorisations $2(2\delta'-n)(2\delta'-n-2)$ and $2(2\delta'-n)(2\delta'-n+1)$.

## Conclusion

Combining (1), (2) and the algebraic step:
$$
\lambda_1(G)\le\lambda_1(G')\le\mathrm{HSF}(n,m',\delta')\le\max_v\mathrm{Ev}(v)
$$
under either convention, provided the corresponding hypothesis holds. This proves Theorems A and B. In fact the chain proves the stronger bound $\lambda_1(G')\le\max\mathrm{Ev}$. $\blacksquare$

**Remark (bipartite slice; noted by Skeptic A).** Under convention (A), every connected bipartite graph with parts of sizes $a,b$ satisfies the hypothesis automatically, because $\sum\mathrm{Od}=2ab\le a^2+b^2=\sum\mathrm{Ev}_i$. For such graphs the conclusion is elementary: $\lambda_1\le\sqrt{ab}\le\max(a,b)$. The content of the theorem lies in the non-bipartite case, which the uniform argument above also covers.

# Equality cases

**Proposition.** Suppose the hypothesis holds and $n\ge 2$.

- (A) $\lambda_1(G)=\max\mathrm{Ev}_i$ if and only if $n$ is even and $G$ is $n/2$-regular.
- (B) $\lambda_1(G)=\max\mathrm{Ev}_x$ if and only if $n$ is odd and $G$ is $(n-1)/2$-regular. Such graphs exist only when $n\equiv 1\pmod 4$.

*Proof.* **Necessity.** Equality forces every inequality in the chain to be tight.

- Tightness in the algebraic step requires $m'$ to be at its maximum, since $\Delta$ is strictly increasing in $m$. It also requires $2x(x+2)=0$, that is $x=0$, in case (A), or $2x(x-1)=0$ with $x\ge1$, that is $x=1$, in case (B).
- In either case $\delta'=2m'/n$, so the minimum degree of $G'$ equals its average degree, and $G'$ is regular.
- $G$ is a connected spanning subgraph of $G'$. If it were a proper subgraph, the Perron--Frobenius theorem would give $\lambda_1(G)<\lambda_1(G')$. Hence $G=G'$, so $G$ is regular of degree $n/2$ in case (A) or $(n-1)/2$ in case (B).

**Sufficiency.** Let $G$ be $k$-regular on $n$ vertices with $k=n/2$ in case (A) or $k=(n-1)/2$ in case (B).

- Two non-adjacent vertices have $2k\ge n-1>n-2$ neighbour slots among the other $n-2$ vertices. So they share a neighbour, and $G$ is connected with diameter at most $2$.
- Therefore $\mathrm{Od}(v)=k$ for every $v$, and $\mathrm{Ev}=k$ under the relevant convention.
- The hypothesis holds with equality, and $\lambda_1=k=\max\mathrm{Ev}$.

Finally, a $(n-1)/2$-regular graph on odd $n$ needs $n(n-1)/4$ to be an integer, which forces $n\equiv1\pmod 4$. $\square$

Examples:

- (A): $K_2$, $C_4$, $K_{a,a}$, and also non-bipartite graphs such as the triangular prism $C_3\square K_2$ on 6 vertices.
- (B): $C_5$, Paley graphs.

In an enumeration done for this release (`checks.py`, included), the equality graphs among all connected graphs were:

| Convention | $n$ | Equality graphs | Of which non-bipartite |
|---|---|---|---|
| (A) | 4 | 1 | 0 |
| (A) | 6 | 2 | 1 |
| (A) | 8 | 6 | 5 |
| (B) | 5 | 1 | -- |
| (B) | 9 | 16 | -- |

In each case these are exactly all the $n/2$- or $(n-1)/2$-regular graphs, as the proposition predicts. The exhaustive search's $n=10$ equality witness for (A), `IQjUjqm]O`, is a non-bipartite 5-regular graph of diameter 2.

# Computational evidence

All of this evidence comes from files in the release. None of it is needed for the proof.

**Proof-chain verification (`verify_proof195.py`).** The script asserts each link on every tested graph:

- $\lambda_1(G)\le\lambda_1(G')$;
- $\lambda_1(G')\le\mathrm{HSF}(G')$;
- the hypothesis implies $\mathrm{HSF}\le\max\mathrm{Ev}$, under both conventions.

The test set was all connected graphs with $3\le n\le 9$ (273,191 graphs: 2, 6, 21, 112, 853, 11,117, 261,080) plus 20,000 random $G(n,p)$ draws with $10\le n\le 59$, keeping only connected ones. That makes 290,627 graphs in total. We re-ran it for this release on 14 Oct 2026. Output: "all checks passed on 290627 graphs; min HSF slack -7.1e-15", which is floating-point zero. Runtime was about 3 minutes.

**Counterexample searches.** Margins are $\lambda_1-\max\mathrm{Ev}$ over graphs satisfying the hypothesis. All are $\le 0$, as the theorem requires.

| Search | Convention (B), code | Convention (A), WoW |
|---|---|---|
| `exh.c`, $n=10$ (file `out/195_n10.txt`) | best $-0.3487$ | best $0$ (equality) |
| `exh.c`, $n\le 9$ | best $0$ at $n=5,9$ (equality) | equality only at even $n$ |
| `exh.c`, $n=11$, 2 completed shards | $-0.5938$, $-0.5926$ | $-0.2583$ |
| Simulated annealing, diameter $\ge3$, $n=12$ / $14$ | $-0.483$ / $-0.583$ | $-0.755$ / $-0.816$ |
| Blow-up relaxation, patterns $k\le5$ | sup $=0$ | -- |
| Structured families (`fam195.py`) | $\le 0$ | -- |

The structured families in `fam195.py` are Paley, circulants, Kneser, coronas, grids, lollipops, pineapples and the graph atlas.

**Independent skeptic batteries** (their own code) found 0 violations and 0 proof-chain failures:

- Skeptic A: atlas $n\le7$, about 2,500 family graphs, and about 2,200 random graphs satisfying the hypothesis.
- Skeptic B: 24,710 random connected graphs with $n\le 29$, exhaustive `geng -c` for $n=3..8$, and near-threshold families. Best margins were about $-0.76$ (B) and $-0.83$ (A) on the targeted families.

# Independent skeptic verdicts

Two reviewers audited the proof chain step by step. Each states that it did not read `REPORT.md` or the other reviewer's folder.

- **Skeptic A (`skepticA_195/VERDICT.md`): ACCEPT.** It marked every step TRUE and gave the factorisations of both algebraic steps. It judged the solve "fair", meaning it is not a definitional trick: the proof needs a nontrivial spectral bound, and both conventions are proved. An earlier note in `NOTES.md` flagged a gap. That note tested only the special case $\sqrt{2m-n+1}$ ($\delta'=1$) of HSF, which fails on $P_4$. The verdict explicitly retracts it: the full HSF bound gives exactly $2$ on $P_4$.
- **Skeptic B (`skepticB_195/VERDICT.md`): ACCEPT.** It found "no gap" in the reduction or in the HSF step, and also judged the solve "fair". Its prior-art search found no published closure of conjecture 195.

# Reproduction

The requirements are `python3` with `numpy`, `scipy`, `networkx` and `sympy`; nauty (`nauty-geng`); and `gcc`.
```
cd graffiti195
python3 verify_proof195.py          # proof-chain check, ~3 min
python3 fam195.py                   # structured families
gcc -O2 -o exh exh.c -lm
nauty-geng -cq 9 | ./exh 195        # exhaustive margins, both conventions
python3 sa.py 195c 12 240 12 d3     # annealing (195w = WoW convention)
python3 blowup.py 5 0 2             # blow-up relaxation (k, part, nparts)
python3 ../checks.py                # symbolic identities + equality enumeration
```
The skeptics' scripts are in `skepticA_195/`. Skeptic B's folder contains only its verdict.

# Caveats

1. **Not externally peer reviewed.** The proof has been checked only by the internal workflow and two automated skeptic reviews.
2. **Original WoW wording not recovered.** The statements above follow the Brewster--Dinneen--Faber glossary (A) and the Roucairol--Cazenave code (B). If some copy of WoW states 195 in a third form, that form has not been checked.
3. **Novelty unverified.** `REPORT.md` marks novelty as unchecked. Skeptic B's search found no published proof, but a quick search cannot rule one out.
4. **Cited theorem.** The proof relies on the Hong--Shu--Fang bound as stated in the source files, and the files give only "JCTB 2001". The bound was not re-derived here, although every numerical test above agrees with it.
5. **Bookkeeping discrepancies in the computational record.** None of these affects the proof.
   - `out/195_n10.txt` reports 9,388,405 graphs processed. `nauty-geng -c 10` generates 11,716,571 connected graphs. So the "$n=10$ exhaustive" run was either a subset or its input was cut short.
   - The $n=11$ run has only 2 nonempty shards. Simulated annealing at $n\ge16$ and blow-up patterns with $k=6$ were terminated without output.
   - `REPORT.md` describes the 290,627 as "connected graphs with $n\le9$ plus random". In fact the total *includes* the random graphs, and the random sizes run from 10 to 59, not to 60.
6. **Equality description corrected.** `REPORT.md` gives the equality cases under (A) as "$K_{a,a}$". The correct class is all $n/2$-regular graphs, which includes non-bipartite ones (see the Equality cases section).
7. **Skeptic B's algebra for (A).** Skeptic B writes the worst-case difference as $2n(n-2)$. That is only its value at $\delta'=1$; the general expression is $2x(x+2)$. B's conclusion is still correct.
8. **Removed files.** Two unrelated files from the original bundle (`graffiti195/survey.pdf`, a 9-byte "Not found" stub, and `survey.txt`, an unrelated GERAD report) are not included in this repository. The Brewster--Dinneen--Faber article is not redistributed; see [REFERENCES.md](../../REFERENCES.md). The `graffiti195` folder also contains work on Graffiti 219, which is outside the scope of this release.
