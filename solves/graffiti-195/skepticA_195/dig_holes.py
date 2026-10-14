#!/usr/bin/env python3
"""Dig into proof holes and non-bipartite cases for Graffiti 195."""
import math
import random
import networkx as nx
import numpy as np
from verify195 import check_graph, even_odd_counts, odd_distance_graph, spectral_radius

rng = random.Random(42)

def summarize(r):
    return {k: (round(r[k], 6) if isinstance(r[k], float) else r[k])
            for k in ["n","m","lam","max_ev","max_od","sum_od","sum_ev","lam_p","hong","deg_bound",
                      "hyp","concl","hong_le_maxev","deg_le_maxev","lamp_le_maxev"]}

print("=== Cases where hyp & max_od > max_ev (WoW) ===")
count = 0
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, include_self=True)
    if r and r["hyp"] and r["max_od"] > r["max_ev"]:
        count += 1
        if count <= 8:
            print(summarize(r), "bip" if nx.is_bipartite(G) else "nonbip", "edges", list(G.edges())[:12])
print("total atlas deg>maxev:", count)

print("\n=== Non-bipartite hyp graphs: conclusion gaps (WoW) ===")
gaps = []
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    if nx.is_bipartite(G):
        continue
    r = check_graph(G, include_self=True)
    if r and r["hyp"]:
        gaps.append(r["max_ev"] - r["lam"])
print(f"nonbip hyp={len(gaps)} min_gap={min(gaps):.6f} median={sorted(gaps)[len(gaps)//2]:.6f}")

print("\n=== Is hyp ALWAYS true for bipartite under WoW? ===")
bad = 0
for G in nx.graph_atlas_g():
    if 1 <= G.number_of_nodes() <= 7 and nx.is_connected(G) and nx.is_bipartite(G):
        r = check_graph(G, include_self=True)
        if not r["hyp"]:
            bad += 1
print("bipartite atlas with hyp false:", bad)

print("\n=== Code reading: bipartite hyp frequency ===")
hyp_b = tot_b = 0
for a in range(1, 12):
    for b in range(a, 12):
        G = nx.complete_bipartite_graph(a, b)
        r = check_graph(G, include_self=False)
        tot_b += 1
        if r["hyp"]:
            hyp_b += 1
            gap = r["max_ev"] - r["lam"]
            if gap < 0:
                print("VIOL bip code", a, b, r)
print(f"K_a,b code hyp {hyp_b}/{tot_b}")

print("\n=== Search for near-counterexamples (maximize lam - max_ev among hyp) ===")
for include_self, tag in [(True, "WoW"), (False, "code")]:
    best = None
    # random search
    for n in range(6, 22):
        for _ in range(400):
            # prefer dense-ish or triangle-rich
            p = rng.choice([0.15, 0.25, 0.4, 0.6])
            G = nx.erdos_renyi_graph(n, p, seed=rng.randint(0, 10**9))
            if not nx.is_connected(G):
                continue
            r = check_graph(G, include_self=include_self)
            if not r["hyp"]:
                continue
            score = r["lam"] - r["max_ev"]
            if best is None or score > best[0]:
                best = (score, r, list(G.edges())[:20])
        for _ in range(200):
            G = nx.random_regular_graph(min(4, n-1), n, seed=rng.randint(0, 10**9)) if n * min(4, n-1) % 2 == 0 else nx.erdos_renyi_graph(n, 0.3, seed=rng.randint(0,10**9))
            if not nx.is_connected(G):
                continue
            r = check_graph(G, include_self=include_self)
            if not r["hyp"]:
                continue
            score = r["lam"] - r["max_ev"]
            if best is None or score > best[0]:
                best = (score, r, list(G.edges())[:20])
    print(tag, "best lam-max_ev among hyp:", best[0], summarize(best[1]))

print("\n=== Alleged proof: does Hong ever work as universal step? ===")
# Count fraction where hyp & hong > max_ev
for include_self, tag in [(True, "WoW"), (False, "code")]:
    h = f = 0
    for G in nx.graph_atlas_g():
        if 1 <= G.number_of_nodes() <= 7 and nx.is_connected(G):
            r = check_graph(G, include_self=include_self)
            if r["hyp"]:
                h += 1
                if r["hong"] > r["max_ev"] + 1e-9:
                    f += 1
    print(tag, f"hong exceeds max_ev in {f}/{h} hyp graphs")

print("\n=== Can we prove bipartite WoW case cleanly? ===")
# λ1(G) <= sqrt(ab) <= max(a,b) = max Ev for connected bipartite
ok = True
for a,b in [(1,5),(3,3),(2,7),(10,10),(1,1)]:
    G = nx.complete_bipartite_graph(a,b)
    Ev,_ = even_odd_counts(G, True)
    print(f"K_{a},{b}: lam={spectral_radius(G):.4f} sqrt(ab)={math.sqrt(a*b):.4f} maxEv={max(Ev.values())}")

print("\n=== Non-bipartite: is G' related to something with λ1 <= max Ev? ===")
# For triangle: Ev=1 (self only? wait dist to others=1 odd, so Ev=1, Odd=2 each). sum od=6, sum ev=3. hyp FALSE.
# Add pending edges analysis for odd-distance complement
for name, G in [("triangle+pendant", None)]:
    G = nx.Graph([(0,1),(1,2),(2,0),(0,3)])
    r = check_graph(G, True)
    print("C3+pendant WoW", summarize(r), "bip", nx.is_bipartite(G))
    r2 = check_graph(G, False)
    print("C3+pendant code", summarize(r2))

# bull graph, diamond, etc.
for edges, name in [
    ([(0,1),(1,2),(2,0),(2,3),(3,4)], "P2-on-triangle"),
    ([(0,1),(1,2),(2,3),(3,0),(0,2)], "diamond"),
    ([(0,1),(1,2),(2,3),(3,4),(4,0),(0,2),(2,4)], "C5+chords"),
]:
    G = nx.Graph(edges)
    for inc, tag in [(True,"WoW"),(False,"code")]:
        r = check_graph(G, inc)
        print(name, tag, summarize(r))
