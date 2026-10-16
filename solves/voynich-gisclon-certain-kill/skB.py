import numpy as np, itertools
from scipy import stats
from math import comb, log
A=[16,0,11,15];B=[3,5,4,10];C=[a+b for a,b in zip(A,B)]
p1=(1-5/22)**42;print("T1",p1)
p2=stats.fisher_exact([[0,42],[5,17]],alternative='less')[1];print("T2",p2)
p3=stats.fisher_exact([[27,15],[7,15]],alternative='greater')[1];print("T3",p3)
chi=lambda t:stats.chi2_contingency(t,correction=False)[0]
c0=chi([A,B]);print("T4",c0,stats.chi2.sf(c0,3))
ps=[p1,p2,p3,stats.chi2.sf(c0,3)];X=-2*sum(map(log,ps));print("comb",X,stats.chi2.sf(X,8))
X2=-2*sum(map(log,ps[1:]));print("noT1",stats.chi2.sf(X2,6))
# exact multivariate hypergeometric: B row given margins
tot=comb(64,22);pe=0
for b in itertools.product(*[range(min(c,22)+1) for c in C]):
  if sum(b)!=22:continue
  a=[c-x for c,x in zip(C,b)]
  if chi([a,list(b)])>=c0-1e-9:
    pr=1
    for c,x in zip(C,b):pr*=comb(c,x)
    pe+=pr/tot
print("exact perm chi2",pe,"bonf min",3*min(ps[1:]))
# T1 exact binomial alternative: CH rate pooled 5/64
print("T1 pooled p0",(1-5/64)**42, "ratio T1 overstate vs T2",p2/p1)
