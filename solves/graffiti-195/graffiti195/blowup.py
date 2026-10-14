# Asymptotic (n->infinity) relaxation for Graffiti 195 via blow-ups of a pattern graph H.
# Each vertex class i of H becomes a clique or an independent set of size x_i*n.
# lam1/n -> lam1(diag(sqrt x)(A_H + diag(c)) diag(sqrt x)), Ev_i/n -> sum_j x_j [d_H(i,j) even] (+x_i if indep).
# Need: lam1 - max_i Ev_i > 0 and sum_i x_i Ev_i >= 1/2.
import numpy as np, networkx as nx, sys, itertools
from scipy.optimize import minimize
k = int(sys.argv[1]); part = int(sys.argv[2]); nparts = int(sys.argv[3])
rng = np.random.default_rng(part)
import subprocess
g6 = subprocess.run(["nauty-geng", "-cq", str(k)], capture_output=True, text=True).stdout.split()
def evalf(x, A, c, E):
    s = np.sqrt(x)
    S = s[:, None] * (A + np.diag(c)) * s[None, :]
    lam = np.linalg.eigvalsh(S)[-1]
    Ev = E @ x
    return lam, Ev
best = (-1e9,)
cnt = 0
for gi, g in enumerate(g6):
    if gi % nparts != part: continue
    H = nx.from_graph6_bytes(g.encode())
    A = nx.to_numpy_array(H, nodelist=range(k))
    D = nx.floyd_warshall_numpy(H, nodelist=range(k))
    if D.max() < 3: continue  # diameter-2 patterns: provably no asymptotic violation (HSF)
    for types in itertools.product([0, 1], repeat=k):
        c = np.array(types, float)  # 1 = clique
        E = ((D % 2 == 0) & ~np.eye(k, dtype=bool)).astype(float) + np.diag(1 - c)
        def obj(y):
            x = np.exp(y - y.max()); x /= x.sum()
            lam, Ev = evalf(x, A, c, E)
            cond = x @ Ev - 0.5
            return -(lam - Ev.max() + 5 * min(0, cond))
        for r in range(4):
            y0 = rng.normal(size=k) * 2
            res = minimize(obj, y0, method="Nelder-Mead", options={"maxiter": 3000, "xatol": 1e-9, "fatol": 1e-12})
            cnt += 1
            x = np.exp(res.x - res.x.max()); x /= x.sum()
            lam, Ev = evalf(x, A, c, E)
            cond = x @ Ev - 0.5
            if cond >= -1e-9:
                mg = lam - Ev.max()
                if mg > best[0]:
                    best = (mg, g, types, x.round(4).tolist(), lam, Ev.round(4).tolist(), cond)
print(k, part, cnt, best, flush=True)
