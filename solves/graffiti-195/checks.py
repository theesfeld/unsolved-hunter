import sympy as sp, networkx as nx, numpy as np, subprocess
n,d=sp.symbols('n delta'); x=sp.symbols('x')
disc=lambda m:(d+1)**2+4*(2*m-d*n)
for name,M,T in [("incl",n**2/4,n-d),("excl",n*(n-1)/4,n-1-d)]:
    diff=sp.expand((2*T-d+1)**2-disc(M))
    print(name, sp.factor(diff), "| in x:", sp.factor(sp.expand(diff.subs(d,(n-x)/2))))
G=nx.from_graph6_bytes(b"IQjUjqm]O"); print("n10 wow-best: bipartite",nx.is_bipartite(G),"degs",sorted(set(dict(G.degree()).values())),"diam",nx.diameter(G))
def ev(G,incl):
    D=dict(nx.all_pairs_shortest_path_length(G))
    E=[sum(1 for u in G if D[v][u]%2==0 and (incl or u!=v)) for v in G]
    O=[sum(1 for u in G if D[v][u]%2==1) for v in G]
    return sum(O),sum(E),max(E),max(np.linalg.eigvalsh(nx.to_numpy_array(G)))
print("prism (so,se,maxEv_i,lam1)",ev(nx.circular_ladder_graph(3),True))
for k,incl in [(4,True),(6,True),(8,True),(5,False),(9,False)]:
    out=subprocess.run(["nauty-geng","-cq",str(k)],capture_output=True,text=True).stdout.split()
    eq=[]
    for g in out:
        G=nx.from_graph6_bytes(g.encode()); so,se,mx,l=ev(G,incl)
        if so<=se and abs(l-mx)<1e-9: eq.append((g,nx.is_bipartite(G),sorted(set(dict(G.degree()).values())),nx.diameter(G)))
    print("incl" if incl else "excl","eq n=",k,len(eq),eq,flush=True)
