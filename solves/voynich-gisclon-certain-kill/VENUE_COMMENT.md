# Draft Zenodo / community comment: NOT SENT (for user review)

**On:** Gisclon (2026), doi:10.5281/zenodo.20835400
**From:** theesfeld <william@theesfeld.net>

I re-ran the four tests using the counts in your §4.1 table (qok*: CS16/CH0/FS11/FH15; fachys: CS3/CH5/FS4/FH10). Every individual number reproduces. The combination step does not hold up, for two reasons:

1. T1 takes p0 = 5/22 from the comparison group and treats it as a known rate. The valid conditional test of "0/42 vs 5/22" is the hypergeometric P = 0.003454, which is exactly T2. T1 overstates that same evidence by about 174×.
2. T2 and T3 are collapses of the T4 2×4 table, and all four tests use the same 64 folios. They are not independent, so Fisher's df = 8 combination (p = 1.31e-8) is not valid.

A single exact test on the 2×4 table (conditioned on margins, χ²-ordered) gives p = 0.00330. Bonferroni on the best of T2–T4 gives 0.0104. Both are above the paper's own CERTAIN threshold of α = 0.003. A residual association near p ≈ 0.003 may be real. However, qok*/fachys line up almost exactly with Currier A/B, and the plant/humor codings were not assigned blind. So that association does not support the semantic reading.

Scripts and full write-up: https://github.com/theesfeld/unsolved-hunter/tree/main/solves/voynich-gisclon-certain-kill
