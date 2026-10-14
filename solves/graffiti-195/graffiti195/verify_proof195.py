# Numerically verify the proof chain for Graffiti 195:
#  G' = odd-distance graph (u~v iff d(u,v) odd) contains G, so lam1(G) <= lam1(G')
#  HSF(G') = (d'-1+sqrt((d'+1)^2+4(2m'-d'n)))/2 >= lam1(G')       [Hong-Shu-Fang 2001]
#  if 4m' <= n(n-1)  (code version)  then HSF(G') <= n-1-d' = max Ev_excl
#  if 4m' <= n^2     (WoW version)   then HSF(G') <= n-d'   = max Ev_incl
import numpy as np, networkx as nx, subprocess, sys
from inv import dist
def check(A):
    n = len(A); D = dist(A).astype(int)
    Gp = ((D % 2) == 1).astype(float)
    l1 = np.linalg.eigvalsh(A)[-1]; l1p = np.linalg.eigvalsh(Gp)[-1]
    dp = Gp.sum(1).min(); mp = Gp.sum() / 2
    hsf = (dp - 1 + np.sqrt((dp + 1)**2 + 4*(2*mp - dp*n))) / 2
    evx = (((D % 2) == 0) & ~np.eye(n, dtype=bool)).sum(1).max()
    assert l1 <= l1p + 1e-9, "monotonicity"
    assert l1p <= hsf + 1e-9, ("HSF", l1p, hsf)
    bad = 0
    if 4*mp <= n*(n-1): assert hsf <= n-1-dp + 1e-9 and n-1-dp == evx, "code"; bad |= (l1 > evx + 1e-9)
    if 4*mp <= n*n: assert hsf <= n-dp + 1e-9, "wow"
    return hsf - l1p
cnt = 0; gap = []
for k in range(3, 10):
    out = subprocess.run(["nauty-geng", "-cq", str(k)], capture_output=True, text=True).stdout.split()
    for g in out:
        A = nx.to_numpy_array(nx.from_graph6_bytes(g.encode())); gap.append(check(A)); cnt += 1
    print("n", k, "ok", len(out), flush=True)
rng = np.random.default_rng(0)
for t in range(20000):
    n = rng.integers(10, 60); p = rng.uniform(0.02, 0.9)
    G = nx.gnp_random_graph(n, p, seed=int(rng.integers(1e9)))
    if not nx.is_connected(G): continue
    check(nx.to_numpy_array(G)); cnt += 1
print("all checks passed on", cnt, "graphs; min HSF slack", min(gap))
