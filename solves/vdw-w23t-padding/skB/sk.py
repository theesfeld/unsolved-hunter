import re,sys
tex=open('tex/main.tex').read()
def cert(t,n):
    m=re.search(r'\\paragraph\{\$\\vdw\(2; 3, %d\) > %d\$\}\s*\\begin\{gather\*\}(.*?)\\end\{gather\*\}'%(t,n),tex,re.S)
    body=m.group(1).replace('\\\\','').replace(' ','').replace('\n','')
    out=[];i=0
    for tok in re.finditer(r'([01])(?:\^\{(\d+)\})?',body):
        out.append(tok.group(1)*int(tok.group(2) or 1))
    s=''.join(out); assert set(body)<=set('01^{}0123456789'); return s
def ok(s,t):
    R={i for i,c in enumerate(s) if c=='0'}; B={i for i,c in enumerate(s) if c=='1'}; n=len(s)
    for a in R:
        for b in R:
            if b>a and 2*b-a in R: return False,('0-3AP',a,b)
    for a in B:
        for d in range(1,(n-1-a)//(t-1)+1):
            if all(a+k*d in B for k in range(t)): return False,('1-tAP',a,d)
    return True,None
for t,n in [(32,1006),(36,1257)]:
    s=cert(t,n); print(t,len(s),ok(s,t))
    f=open('certs/NEW_t%d_n%d.txt'%(t,{32:1011,36:1259}[t])).read().strip()
    print(' new len',len(f),ok(f,t),'endswith AKS',f.endswith(s),'prefix',f[:len(f)-len(s)], 'startswith',f.startswith(s))
    print(' AKS +1 either end:',[ok(x,t)[0] for x in ['0'+s,'1'+s,s+'0',s+'1']])
    for k in range(1,8):
        p='1'*k+s
        if ok(p,t)[0]: best=k
    print(' max 1-prefix',best, 'next fails:',ok('1'*(best+1)+s,t))
# planted
s=cert(32,1006); x=list(s); x[0]=x[1]=x[2]='0'; print('plant3AP',ok(''.join(x),32))
print('plant tAP',ok('1'*32,32), ok('1'*31,32))
print('t=36 cert as t=35',ok(cert(36,1257),35)[0])
