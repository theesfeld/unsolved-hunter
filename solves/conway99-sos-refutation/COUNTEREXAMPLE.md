# Counterexample to Natal–Al-saadi (arXiv:2610.16266) Conjecture 5

Claim: every simple graph on 99 vertices with no diamond subgraph and no K_{2,3} subgraph has ≤ 55 triangles.
They compare to the 231 triangles forced by srg(99,14,1,2) and conclude nonexistence.

## Counterexample (disconnected)
Take 11 disjoint copies of the unique srg(9,4,1,2) (the 3×3 lattice / H(2,3) Hamming graph / 3×3 rook's graph).
- Each copy has λ=1 ⇒ diamond-free, μ=2 ⇒ no pair has 3 common neighbors ⇒ K_{2,3}-free, and exactly 6 triangles.
- Disjoint union: still diamond-free and K_{2,3}-free (cross-component pairs have 0 common neighbors).
- Total triangles: 11 × 6 = **66 > 55**.

## Connected strengthening
Join the 11 blocks into a path by 10 bridge edges between distinct blocks.
Verified: still diamond-free, K_{2,3}-free, 66 triangles, connected.

## Conclusion
Conjecture 5 is **false**. The paper does **not** prove that Conway's 99-graph is nonexistent.
The experimental SoS/Lasserre bound of 55 is erroneous (or the constraints were mis-coded).
Our local Conway SAT attack on prescribed Z3 remains relevant.

Verified numerically: triangles=66 (disjoint), 66 (connected).
