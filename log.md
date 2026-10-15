# Unsolved Hunter Log

One target per day. Status: nothing / lead / CONFIRMED.


## 2026-10-14 — Erdős–Straus conjecture (4/n = 1/x+1/y+1/z for all n≥2)
- Research: open. Prior computer checks reach about 10^17 (Salez 2014 and later work). Mordell's identities reduce the problem to primes p ≡ 1,121,169,289,361,529 (mod 840).
- Approach: counterexample search over those hard-class primes. Take the smallest x ≥ ceil(p/4), split a/b = (4x−p)/(px) into two unit fractions using divisor pairs of b, and check each solution exactly with Fraction.
- Code: /workspace/unsolved/erdos_straus.py (run: python3 erdos_straus.py N)
- Results: all 6628 hard-class primes below 3×10^6 solved; x never more than ceil(p/4)+14. The run to 10^8 was interrupted.
- Status: nothing. This is far below the known 10^17 bound, so it is not new. Pending skeptic review under the new rule; no lead or CONFIRMED claimed.

## 2026-10-14 — Dorabella cipher (Elgar, 1897; 87 symbols)
- Research: still unsolved. Hauer et al. (HistoCrypt 2021) found plain monoalphabetic English decipherment fails. The same group (2021, arXiv 2509.17950) produced a "musical" decipherment. Dearcipher.space proposes a rotating-key reading (rotation driven by dots and date digits) that gives "IMATH PENDO..."; that is not accepted as a solution.
- Data: majority-consensus transcription (A–H orientation + 1–3 arcs) taken from aclanthology.org/2021.smp-1.5.pdf, saved in dorabella.txt.
- Code: /workspace/unsolved/dorabella/ (mkq.py builds quadgrams from 4 Gutenberg books; mono.c is an injective substitution annealer; anneal.c is a homophonic variant, which overfits on 87 symbols and is unusable; run.py, periodic.py run the tests).
- Tests: direct, reversed, progressive orientation rotation k=1..7 (with and without an arc shift), periodic orientation keys of period 2–3 (72 keys). Controls: 4 English 87-letter texts under a 24-symbol substitution, all recovered exactly (scores −332 to −348). Nulls: shuffled Dorabella, −424 to −444.
- Results: every Dorabella hypothesis scored −409 to −482, inside or below the shuffle-null range. Outputs are gibberish.
- Status: nothing (dead end for these cipher types).

## 2026-10-14 — Kryptos K4 (97 chars)
- Research: Sanborn's archive (with the K4 plaintext) sold Nov 2025 for $962,500. The buyer, Paradigm (revealed Jun 2026), has not published it. Instead it runs a hashed submission checker at $1 per guess, plus 10 CTF puzzles. Kobek & Byrne derived the plaintext from Smithsonian papers in Sep 2025 and will not publish it. So K4 is solved privately but not publicly. Public cribs: EASTNORTHEAST (positions 22–34), BERLINCLOCK (64–74).
- Ciphertext: from the Wikipedia raw page, ...KUHUAUEKCAR (97 letters). Crib alignment checked: FLRVQQPRNGKSS / NYPVTTMZFPK.
- Code: /workspace/unsolved/kryptos/k4.py (args W P).
- Test: complete columnar transposition, width 1–9, all column orders, in both orders (substitute then transpose, and transpose then substitute). Substitution: periodic Vigenère / Beaufort / variant Beaufort, standard or KRYPTOS alphabet, period ≤13. Check: exact consistency of the key against the cribs.
- Control: a synthetic cipher built with w=5, KRYPTOS-alphabet Vigenère, period 7 was recovered exactly (2 hits, both the true setting).
- Result: 0 consistent configurations for K4 (res_w9.txt). This family is ruled out, which matches prior community results.
- Status: nothing (dead end). Not worth more effort: the answer exists privately, and checking a guess costs money.

## 2026-10-14 — Zodiac Z32 (Stampher "IN THREE AND THREE EIGHTHS RADIANS TEN")
- Research: Stampher Dec 2025 / whitepaper Feb 2026. Same plaintext proposed by DMW on the Zodiac forum in 2019 (not unique). Not accepted by Oranchak/Blake/FBI.
- Approach: Independent reproduction of the generator + skeptic battery (lock nulls, lexicon widening, homophonic likelihood, geography-first ranking).
- Code: /workspace/unsolved/z32/mine/ and REPORT.md
- Results: Claim reproduces numerically, but only 3 letter-equalities constrain the cipher; uniqueness is geographic ranking. Null tests ~8–18% hit nearby scenes by chance. Widened lexicon finds closer survivors. Inconsistent with Z408-style homophone cycling.
- Status: nothing (failed-skeptic / underdetermined).

## 2026-10-14 — Graffiti 322 (InverseEven ≤ range of distance eigenvalues; usual max−min range)
- Research: Listed open in Roucairol–Cazenave arXiv:2409.18626 under usual range. Alternate "# distinct eigenvalues" reading makes C4 look like a counterexample only with a self-excluding InverseEven count.
- Approach: Proof that for every connected simple G on n≥2: λ_max(D)≥n−1 (D≥J−I, PF monotonicity), λ_min(D)≤−1 (Cauchy interlacing on an edge), InverseEven≤n (Ev includes v), hence range≥n≥InverseEven. Stronger than triangle-free-only 322. Distance spread ≥n is classical (e.g. Yu et al. 2012); combining with InverseEven closes 322.
- Code: /workspace/unsolved/graffiti322/PROOF.md; verify scripts under graffiti322/ and skeptic*_322/
- Results: No counterexample in exhaustive connected graphs through n=9 and triangle-free through n=11; named cages/bipartite/trees all satisfy. Equality on K_n (and K2 among triangle-free).
- Skeptic A: ACCEPT on the inequalities, but explicitly says calling the original Graffiti conjecture "resolved" is a stretch (trivial under usual-range + Ev-includes-v; likely not Graffiti's intent).
- Skeptic B: ACCEPT on the inequalities; notes spread≥n is classical and InverseEven≤n is trivial.
- Status: failed-skeptic (stretched "solved"). Inequalities hold; do not claim CONFIRMED resolution of historical Graffiti 322.

## 2026-10-14 — Graffiti 129 / 698 / 195 / 219 (partial; workers still running or incomplete)
- Research: Open in 2025 search survey (129, 698, 195, 219). 290/292 later proved elsewhere; 143/154/197/284 already refuted by others.
- Approach: Hill-climb / exhaustive geng searches under /workspace/unsolved/graffiti129/ and graffiti195/.
- Results (interim): 129 best gaps still negative (no refutation through n≈10–13 exhaustive/ILS). 195 best margin negative under coded condition; 219 far from violation. No lead this run.
- Status: nothing (dead-end / incomplete for a full-day bound extension; no skeptic-worthy claim).


## 2026-10-14 — Graffiti 129 / 698 / 252
- Research: Open in Roucairol–Cazenave 2025 survey (129, 698). 252 likewise open there.
- Approach: Exhaustive geng through n=11 for 129; ILS to n=50; degree-identity Var(Lap)=Var(deg)+mean(deg); classopt continuous relaxation. 698 as coded uses negative Laplacian eigenvalues (vacuous on PSD L). 252: short proof min gap ≤ n/(n−1) ≤ sum 1/dual.
- Code: /workspace/unsolved/graffiti129/ (REPORT.md)
- Results: 129 never beats the star; gap → 0⁻ like −1/√n. 698 vacuous. 252 proved true (trivialish).
- Status: nothing (129 unrefuted; 698/252 not claimed as CONFIRMED solves).

## 2026-10-14 — Graffiti 195 / 219
- Research: Both open in 2025 survey. Ev include/exclude ambiguity.
- Approach: Search + claimed odd-distance-graph + Hong–Shu–Fang proof for 195; Mantel/Frobenius for triangle-free 219; family for unrestricted 219.
- Code: /workspace/unsolved/graffiti195/
- Results: Proof via odd-distance graph G′ ⊇ G, Hong–Shu–Fang bound on λ₁(G′), closed under the odd/even sum hypothesis. Holds for both Ev-include (WoW) and Ev-exclude (Roucairol code) readings. Exhaustive/atlas/random searches: 0 counterexamples. Equality on C₄, K_{a,a}, etc.
- Skeptic A: ACCEPT (/workspace/unsolved/skepticA_195/VERDICT.md) — fair (nontrivial HSF + reduction; not like trivial 322). Corrected earlier δ′=1-special-case false alarm.
- Skeptic B: ACCEPT (/workspace/unsolved/skepticB_195/VERDICT.md) — fair; both Ev readings settled; was open in 2025 search survey.
- 219 triangle-free: no counterexample. Unrestricted 219: triangle-rich candidates, scope unclear without WoW text.
- Status: CONFIRMED for Graffiti 195 (both precise Ev readings). 219: nothing.

## 2026-10-15 — Natal–Al-saadi SoS claim on Conway's 99-graph (arXiv:2610.16266) — CONFIRMED REFUTATION
- Research: Preprint claims T(99)≤55 for diamond-free + K_{2,3}-free graphs via Lasserre, hence srg(99,14,1,2) impossible (needs 231). Labelled Conjecture 5; no formal certificate.
- Approach: Explicit counterexamples under the paper's exact constraints; two independent skeptic rebuilds.
- Code: solves/conway99-sos-refutation/ (build_counterexample.py; skeptics/A, skeptics/B).
- Results: 11×srg(9,4,1,2) → 66 triangles; connected Hamming H(4,3)+2×Paley(9) → **120** triangles. Both diamond-free and K_{2,3}-free. Bound 55 is false.
- Skeptic A: REJECT bound; REJECT "proves nonexistent".
- Skeptic B: REJECT bound; REJECT "proves nonexistent" (120-triangle connected C).
- Status: **CONFIRMED** refutation of the paper's nonexistence argument. Conway 99 existence remains open. Local Z3 SAT still undecided separately.
