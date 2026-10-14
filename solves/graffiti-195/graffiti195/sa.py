# Simulated annealing / hill climb for Graffiti 195 and 219
# usage: python3 sa.py CONJ n seconds seed [tf]
import numpy as np, sys, time, json
from inv import dist, gravity
conj, n, secs, seed = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
flags = set(sys.argv[5:]); tf = 'tf' in flags; d3 = 'd3' in flags
rng = np.random.default_rng(seed)
off = ~np.eye(n, dtype=bool)

def score(A):
    D = dist(A)
    if np.isinf(D).any(): return None
    if tf and np.trace(A @ A @ A) > 0: return None
    if d3 and D.max() < 3: return None
    if conj in ('195c','195w'):
        Di = D.astype(int)
        ev = ((Di % 2 == 0) & off).sum(1)
        even = ev.sum() / 2; odd = n*(n-1)/2 - even
        lam1 = np.linalg.eigvalsh(A)[-1]
        mx = ev.max()
        if conj == '195c':
            margin = lam1 - mx; deficit = max(0.0, odd - even)
        else:  # WoW: even vector includes the vertex itself
            margin = lam1 - mx - 1; deficit = max(0.0, odd - even - n/2)
        # smooth tiebreak: number of vertices at max Ev
        s = margin - 0.3 * deficit / n - 0.02 * (ev == mx).sum()
        return s, margin, deficit
    else:
        G = gravity(A, D)
        w = np.linalg.eigvalsh(G)
        m = A.sum() / 2
        other = n*(n-1)/2 - m
        return (w[-2] - other) / other, w[-2] - other, 0.0

def rand_graph():
    while True:
        kind = rng.integers(4)
        if kind == 0:
            p = rng.uniform(0.1, 0.6)
            A = (rng.random((n, n)) < p).astype(float); A = np.triu(A, 1); A = A + A.T
        elif kind == 1:  # random tree
            A = np.zeros((n, n))
            for i in range(1, n):
                j = rng.integers(i); A[i, j] = A[j, i] = 1
        elif kind == 2:  # clique + pendants / paths
            s = rng.integers(3, max(4, n - 1))
            A = np.zeros((n, n)); A[:s, :s] = 1; np.fill_diagonal(A, 0)
            for i in range(s, n):
                j = rng.integers(i); A[i, j] = A[j, i] = 1
        else:  # bipartite random
            a = rng.integers(1, n); p = rng.uniform(0.3, 1)
            A = np.zeros((n, n)); B = (rng.random((a, n - a)) < p).astype(float)
            A[:a, a:] = B; A[a:, :a] = B.T
        if tf and np.trace(A @ A @ A) > 0:
            # remove triangle edges greedily
            for _ in range(n*n):
                T = (A @ A) * A
                if T.sum() == 0: break
                i, j = np.unravel_index(np.argmax(T), T.shape); A[i, j] = A[j, i] = 0
        if score(A) is not None: return A

best_global = (-1e18, None, None)
t0 = time.time(); restarts = 0; evals = 0
while time.time() - t0 < secs:
    A = rand_graph(); cur = score(A); restarts += 1
    T = 0.5; it = 0; stall = 0
    best_local = cur[0]
    while time.time() - t0 < secs and stall < 3000:
        it += 1
        B = A.copy()
        k = 1 if rng.random() < 0.7 else 2
        for _ in range(k):
            i, j = rng.choice(n, 2, replace=False); B[i, j] = B[j, i] = 1 - B[i, j]
        s = score(B); evals += 1
        if s is None: continue
        if s[0] >= cur[0] or rng.random() < np.exp((s[0] - cur[0]) / T):
            A, cur = B, s
        if cur[0] > best_local + 1e-12: best_local = cur[0]; stall = 0
        else: stall += 1
        T = max(1e-3, T * 0.999)
        # record only feasible (deficit 0)
        if cur[2] == 0 and cur[1] > best_global[0]:
            best_global = (cur[1], A.copy(), cur)
            if conj != '219' and cur[1] > 1e-9:
                print("POSSIBLE REFUTATION 195", cur, flush=True)
            if conj == '219' and cur[1] > 1e-9:
                print("POSSIBLE REFUTATION 219", cur, flush=True)
bm, BA, bc = best_global
edges = [] if BA is None else [(int(i), int(j)) for i in range(n) for j in range(i+1, n) if BA[i, j]]
print(json.dumps({"conj": conj, "n": n, "tf": tf, "d3": d3, "seed": seed, "best_margin": float(bm), "restarts": restarts, "evals": evals, "edges": edges}))
