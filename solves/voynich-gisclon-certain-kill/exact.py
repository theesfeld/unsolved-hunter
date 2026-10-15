from math import comb
from scipy import stats
import numpy as np
col=[19,5,15,25];A=[16,0,11,15];nA=42
def chi(a):
  t=np.array([a,[c-x for c,x in zip(col,a)]]);return stats.chi2_contingency(t,correction=False)[0]
o=chi(A);tot=comb(64,42);p=0
for a in range(20):
 for b in range(6):
  for c in range(16):
   d=nA-a-b-c
   if 0<=d<=25:
    w=comb(19,a)*comb(5,b)*comb(15,c)*comb(25,d)
    if chi([a,b,c,d])>=o-1e-9:p+=w
print("exact 2x4 chi-ordered p",p/tot)
