# independent checker: numpy, enumerates by difference d over all starts (vectorised), 0=blue(3-AP free), 1=red(t-AP free)
import sys, numpy as np
s=open(sys.argv[1]).read().strip(); t=int(sys.argv[2])
x=np.frombuffer(s.encode(),dtype=np.uint8)-48; n=len(x); assert set(np.unique(x))<={0,1}
B=(x==0); R=(x==1); bad=0
for d in range(1,n):
    m=n-2*d
    if m>0 and np.any(B[:m]&B[d:d+m]&B[2*d:2*d+m]): print('blue 3AP d',d); bad=1;break
for d in range(1,n):
    m=n-(t-1)*d
    if m<=0: break
    acc=R[:m].copy()
    for i in range(1,t): acc&=R[i*d:i*d+m]
    if acc.any(): print('red AP d',d,'start',int(np.argmax(acc))+1); bad=1;break
print(n,'VALID' if not bad else 'INVALID', 't=',t)
