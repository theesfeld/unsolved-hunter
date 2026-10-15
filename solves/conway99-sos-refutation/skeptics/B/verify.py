#!/usr/bin/env python3
"""Skeptic B: independent counterexamples to 'T(99) <= 55' (Natal & Al-saadi, arXiv:2610.16266).
Pure-Python checks (no external graph library needed); networkx used only as an optional cross-check."""
import itertools, json, sys

def make(n): return [set() for _ in range(n)]
def add(adj, u, v):
    assert u != v; adj[u].add(v); adj[v].add(u)

def paley9():
    # GF(9) = GF(3)[i]/(i^2+1). Elements (a,b) = a+b i. x~y iff x-y is a nonzero square.
    els = [(a, b) for a in range(3) for b in range(3)]
    mul = lambda x, y: ((x[0]*y[0] - x[1]*y[1]) % 3, (x[0]*y[1] + x[1]*y[0]) % 3)
    squares = {mul(x, x) for x in els if x != (0, 0)}
    assert len(squares) == 4
    adj = make(9)
    for i, x in enumerate(els):
        for j, y in enumerate(els):
            if i < j and ((x[0]-y[0]) % 3, (x[1]-y[1]) % 3) in squares:
                add(adj, i, j)
    return adj

def hamming(d, q):
    verts = list(itertools.product(range(q), repeat=d))
    idx = {v: i for i, v in enumerate(verts)}
    adj = make(len(verts))
    for v in verts:
        for c in range(d):
            for a in range(q):
                if a != v[c]:
                    w = list(v); w[c] = a; add(adj, idx[v], idx[tuple(w)])
    return adj

def disjoint_union(blocks):
    adj, offs, off = [], [], 0
    for b in blocks:
        offs.append(off)
        for nb in b: adj.append({x + off for x in nb})
        off += len(b)
    return adj, offs

def stats(adj):
    n = len(adj)
    edges = sum(len(s) for s in adj) // 2
    tri = sum(1 for u in range(n) for v in adj[u] if v > u for w in adj[u] & adj[v] if w > v)
    max_adj = max_non = 0
    for u in range(n):
        for v in range(u+1, n):
            c = len(adj[u] & adj[v])
            if v in adj[u]: max_adj = max(max_adj, c)
            else: max_non = max(max_non, c)
    degs = sorted({len(s) for s in adj})
    return dict(n=n, edges=edges, triangles=tri, max_common_adjacent=max_adj,
                max_common_nonadjacent=max_non, degrees=degs)

def srg_params(adj):
    n = len(adj); k = {len(s) for s in adj}
    lam = {len(adj[u] & adj[v]) for u in range(n) for v in adj[u]}
    mu = {len(adj[u] & adj[v]) for u in range(n) for v in range(n) if v != u and v not in adj[u]}
    return n, k, lam, mu

def brute_diamond_k23(adj):
    """Literal subgraph search (independent of common-neighbour shortcut)."""
    n = len(adj)
    diamond = any(len(adj[u] & adj[v]) >= 2 for u in range(n) for v in adj[u])  # edge uv + 2 apexes = diamond
    # K_{2,3}: two vertices a,b (any adjacency) with 3 distinct common neighbours
    k23 = any(len(adj[a] & adj[b]) >= 3 for a in range(n) for b in range(a+1, n))
    return diamond, k23

def connected(adj):
    seen, st = {0}, [0]
    while st:
        u = st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen) == len(adj)

def bridge(adj, offs):
    """Chain the components with single edges, each bridge using fresh endpoints."""
    adj = [set(s) for s in adj]
    used = set()
    for a, b in zip(offs, offs[1:]):
        u = next(x for x in range(a, b) if x not in used and x != a)  # pick some vertex in comp a
        v = b  # first vertex of next comp
        add(adj, u, v); used |= {u, v}
    return adj

def report(name, adj):
    s = stats(adj); d, k = brute_diamond_k23(adj)
    s.update(diamond=d, K23=k, connected=connected(adj),
             valid=(not d and not k and s['max_common_adjacent'] <= 1 and s['max_common_nonadjacent'] <= 2))
    print(name, json.dumps(s)); return s

if __name__ == "__main__":
    out = {}
    P = paley9(); print("Paley(9) srg params:", srg_params(P))
    H2 = hamming(2, 3); print("H(2,3)=K3xK3 srg params:", srg_params(H2))
    H4 = hamming(4, 3); print("H(4,3):", stats(H4))
    # sanity: the paper's own D-free/K23-free claim for srg(.,.,1,2) blocks
    out['A_11xPaley9'] = report("A: 11 x Paley(9)", disjoint_union([P]*11)[0])
    G, offs = disjoint_union([H4, P, P]); out['B_H43_plus_2Paley9'] = report("B: H(4,3) + 2 x Paley(9)", G)
    out['C_B_bridged'] = report("C: B + 2 bridges (connected)", bridge(G, offs))
    GA, offsA = disjoint_union([P]*11); out['D_A_bridged'] = report("D: A + 10 bridges (connected)", bridge(GA, offsA))
    try:
        import networkx as nx
        for key, g in [('B', G), ('C', bridge(G, offs))]:
            X = nx.Graph(); X.add_nodes_from(range(len(g)))
            X.add_edges_from((u, v) for u in range(len(g)) for v in g[u] if u < v)
            print("networkx cross-check", key, "triangles =", sum(nx.triangles(X).values()) // 3,
                  "connected =", nx.is_connected(X))
    except ImportError: pass
    # write edge list of best connected example
    C = bridge(G, offs)
    with open("counterexample_C_edges.txt", "w") as f:
        for u in range(len(C)):
            for v in sorted(C[u]):
                if u < v: f.write(f"{u} {v}\n")
    json.dump(out, open("results.json", "w"), indent=1)
