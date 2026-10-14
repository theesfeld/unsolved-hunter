# Family: K_n minus the edges of K_{a,a} (two cliques A,B of size a, both joined to a clique C of size c; no A-B edges)
import numpy as np, networkx as nx
from inv import eval219, triangle_free
def build(a, c):
    n = 2*a + c; A = np.ones((n, n)) - np.eye(n)
    A[:a, a:2*a] = 0; A[a:2*a, :a] = 0
    return A
best = {}
for a in range(1, 9):
    for c in range(1, 60):
        A = build(a, c); r = eval219(A)
        if r[0] > 0 and a not in best: best[a] = (c, 2*a + c, r)
for a, v in best.items(): print("a", a, "first c", v[0], "n", v[1], "lam2 %.4f nonedges %.0f margin %.4f" % (v[2][1], v[2][2], v[2][0]))

# smallest n overall
cands = sorted((2*a+c, a, c) for a in range(1, 12) for c in range(1, 80) if eval219(build(a, c))[0] > 1e-9)
print("smallest n:", cands[:5])
