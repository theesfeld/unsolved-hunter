# Statistical invalidity of Gisclon (2026) "CERTAIN" Voynich partial-decipherment claim

**Status:** CONFIRMED methodological kill (passed the skeptic gate: 2/2 ACCEPT). **Novelty: MINOR.**
**Date:** 2026-10-15 · **Author:** theesfeld <william@theesfeld.net>
**Short name:** `voynich-gisclon-certain-kill`
**Folder:** [solves/voynich-gisclon-certain-kill](https://github.com/theesfeld/unsolved-hunter/tree/main/solves/voynich-gisclon-certain-kill)
**Target:** Gisclon (2026), *First Statistically Demonstrated Partial Decipherment…*, [doi:10.5281/zenodo.20835400](https://doi.org/10.5281/zenodo.20835400). The PDF is not redistributed here.

## Statement
Gisclon reads the Voynich word families qok\* as *herba sicca* and fachys as *herba humida*. The claim is labelled CERTAIN on the basis of a Fisher combination of four tests (T1–T4), giving p = 1.31×10⁻⁸. **That label is not earned under the paper's own rule (α = 0.003):**

1. **T1 is circular.** It treats fachys' observed rate 5/22 as a known null p0. The correct conditional test is hypergeometric C(22,5)/C(64,5) = 0.003454, which is T2 itself. T1 overstates that evidence by about 174×.
2. **The tests are not independent.** All four use the same 64 folio labels. T2 and T3 are collapses of T4's 2×4 table, and T1 duplicates T2. So the Fisher df = 8 combination is invalid. This contradicts the paper's statement that the tests are "fully independent: different data subsets".
3. **A valid omnibus test fails the threshold.** An exact 2×4 test (conditioned on margins, χ²-ordered) gives **p = 0.00330 > 0.003**.

## p-values (all from the paper's §4.1 table: A = 16/0/11/15, B = 3/5/4/10 over CS/CH/FS/FH)
| Test | p | Valid? |
|---|---|---|
| T1 (paper) | 1.98e-5 | No (circular p0) |
| T2 one-sided Fisher (CH) | 0.003454 | Yes, but fails α |
| T3 Fisher S/H | 0.01329 | Yes, but fails α |
| T4 asymptotic χ² df=3 | 0.00422 | Approximate |
| Paper's Fisher combination, df=8 | 1.31e-8 | **No (dependent tests)** |
| Combination without T1 | 2.6e-5 | No (still dependent) |
| Monte Carlo permutation 2×4 (1e5) | 0.0031 | Yes (MC) |
| **Exact 2×4 omnibus** | **0.00330** | **Yes: fails CERTAIN** |
| Bonferroni ×3, best of T2–T4 | 0.0104 | Yes: fails |

## Skeptic verdicts
- Skeptic A: **ACCEPT**, novelty MINOR ([skeptics/skepticA.md](skeptics/skepticA.md))
- Skeptic B: **ACCEPT**, novelty MINOR, with its own independent script `skB.py` ([skeptics/skepticB.md](skeptics/skepticB.md))

Both skeptics asked for the exact 0.00330 to be quoted in place of the MC 0.0031. That correction is applied here.

## Honest caveats
- **Thin margin:** 0.0033 vs 0.003. This kill shows that CERTAIN is not earned by the author's own criterion. It does **not** show that there is no association.
- **Residual association:** a weak association near p ≈ 0.003 (roughly "STRONG" on the paper's scale) may remain. It is confounded with Currier A/B: qok\* is 69/72 Currier A and fachys is 31/31 Currier B. It could reflect a scribe, section, or plant-selection effect. The plant IDs and humor codings are author-assigned and were not made blind. So this is **not** evidence for a decipherment.
- **PRE_REG was written post hoc** (after the first recompute). The corrections used are the standard ones and were not tuned.
- **Not tested:** no swap to Sherwood's alternative plant IDs. The folio table was not re-derived from IVTFF. Every number comes from the paper's own table.
- **Novelty:** no prior critique of this paper was found. Lux (doi:10.5281/zenodo.22850757) audits generic Voynichese statistics and does not cover it. The search was not exhaustive. Follow-up records that build on this claim: zenodo 21027864, 21215108.

## Reproduce
```
python3 recompute.py   # reproduces T1–T4 and the paper's combination
python3 perm.py        # Monte Carlo permutation 2x4 (~0.0031)
python3 exact.py       # exact 2x4 enumeration -> 0.0033024
python3 skB.py         # Skeptic B's independent recheck
```
These need Python 3 with numpy and scipy.

## Suggested comment
See [VENUE_COMMENT.md](VENUE_COMMENT.md). It is a draft and has **not been sent**.
