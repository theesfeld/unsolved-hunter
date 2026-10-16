import sys
def chk(s,t):
    n=len(s); pos0=[i for i,c in enumerate(s) if c=='0']; S0=set(pos0)
    for a in range(len(pos0)):
        for b in range(a+1,len(pos0)):
            if 2*pos0[b]-pos0[a] in S0: return "3AP0 %d %d"%(pos0[a],pos0[b])
    for i in range(n):
        if s[i]!='1':continue
        for d in range(1,(n-1-i)//(t-1)+1):
            if all(s[i+k*d]=='1' for k in range(t)): return "tAP1 %d %d"%(i,d)
    return "OK"
for f,t in [("certs/NEW_t32_n1011.txt",32),("certs/NEW_t36_n1259.txt",36)]:
    s=open(f).read().strip(); assert set(s)<={'0','1'}
    print(f,len(s),chk(s,t),"| +1red",chk('1'+s,t),"| plant0",chk(s.replace('1','0',1).replace('1','0',1) if 0 else '000'+s,t))
    a=open(f.replace("NEW","aks").split("_n")[0]+".txt").read().strip() if 0 else None
