from scipy import stats;import numpy as np
print("T1",stats.binom.pmf(0,42,5/22))
print("T2",stats.fisher_exact([[0,42],[5,17]],alternative='less'))
print("T3",stats.fisher_exact([[27,15],[7,15]],alternative='greater'))
ps=[2.0e-5,0.003454,0.01329,0.00422];X=-2*np.log(ps).sum();print("comb",X,stats.chi2.sf(X,8))
ps2=[0.003454,0.01329,0.00422];X=-2*np.log(ps2).sum();print("noT1",X,stats.chi2.sf(X,6))
# Brown-like: T2 alone dominates; minimal honest = T2 or T4 with Bonferroni
print("bonf min of T2..T4",min(ps2)*3)
# permutation null for exact T1/T2 conditional: total 5 CH of 64, P(all in B)
from math import comb;print("hypergeom 5CH all in B",comb(22,5)/comb(64,5))
