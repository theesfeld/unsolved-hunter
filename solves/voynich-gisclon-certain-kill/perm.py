import numpy as np;from scipy import stats
rng=np.random.default_rng(1)
lab=np.array([0]*16+[1]*0+[2]*11+[3]*15+[0]*3+[1]*5+[2]*4+[3]*10);grp=np.array([0]*42+[1]*22)
def chi(l):
  t=np.array([[np.sum((grp==g)&(l==k)) for k in range(4)] for g in range(2)]);return stats.chi2_contingency(t,correction=False)[0]
o=chi(lab);print("obs chi",o,stats.chi2.sf(o,3))
N=100000;c=sum(chi(rng.permutation(lab))>=o for _ in range(N));print("perm p",(c+1)/(N+1))
