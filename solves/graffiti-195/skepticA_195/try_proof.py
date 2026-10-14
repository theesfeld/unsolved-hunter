#!/usr/bin/env python3
"""Try alternate proof routes; seek counterexamples more aggressively."""
import math
import random
import networkx as nx
import numpy as np
from verify195 import check_graph, even_odd_counts, spectral_radius, odd_distance_graph

rng = random.Random(123)

def hong_G(G):
    n, m = G.number_of_nodes(), G.number_of_edges()
    return math.sqrt(max(0, 2*m - n + 1))

print("=== Does Hong(G) ≤ max Ev under hyp (WoW)? ===")
fail = 0
hypn = 0
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if r["hyp"]:
        hypn += 1
        if hong_G(G) > r["max_ev"] + 1e-9:
            fail += 1
            if fail <= 3:
                print("fail", r["n"], r["m"], "hongG", hong_G(G), "maxev", r["max_ev"], "lam", r["lam"])
print(f"Hong(G)>maxEv in {fail}/{hypn}")

print("\n=== Does Δ(G) ≤ max Ev under hyp? ===")
fail = 0
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if r["hyp"]:
        Delta = max(d for _, d in G.degree())
        if Delta > r["max_ev"]:
            fail += 1
print(f"Delta>maxEv in {fail} hyp graphs")

print("\n=== Code reading: seek counterexample with targeted search ===")
# Under code reading, hyp is rarer. Try to maximize lam/max_ev
best = (-999, None)
viol = []
for trial in range(5000):
    n = rng.randint(6, 24)
    # construction: bipartite-ish with a few odd-cycle chords carefully?
    a = rng.randint(1, n//2)
    b = n - a
    G = nx.complete_bipartite_graph(a, b)
    # randomly delete edges and/or add edges within parts (making nonbip)
    for _ in range(rng.randint(0, a*b//3)):
        u = rng.randrange(a)
        v = a + rng.randrange(b)
        if G.has_edge(u, v):
            G.remove_edge(u, v)
    if rng.random() < 0.5:
        # add a few within-part edges
        for _ in range(rng.randint(1, 5)):
            if a >= 2 and rng.random() < 0.5:
                u, v = rng.sample(range(a), 2)
                G.add_edge(u, v)
            elif b >= 2:
                u, v = rng.sample(range(a, n), 2)
                G.add_edge(u, v)
    G = nx.Graph(G)
    if not nx.is_connected(G):
        # reconnect
        comps = list(nx.connected_components(G))
        for i in range(len(comps)-1):
            G.add_edge(next(iter(comps[i])), next(iter(comps[i+1])))
    for include_self, tag in [(True, "WoW"), (False, "code")]:
        r = check_graph(G, include_self)
        if not r["hyp"]:
            continue
        score = r["lam"] - r["max_ev"]
        if score > best[0]:
            best = (score, (tag, r))
        if r["violates"]:
            viol.append((tag, r, list(G.edges())))

print("best score", best[0], best[1][0] if best[1] else None, best[1][1] if best[1] else None)
print("violations found", len(viol))
if viol:
    print(viol[0])

print("\n=== Equality cases WoW: when lam ≈ max_ev ===")
eq = []
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if r["hyp"] and abs(r["lam"] - r["max_ev"]) < 1e-8:
        eq.append((r["n"], r["m"], r["lam"], r["max_ev"], nx.is_bipartite(G), list(G.edges())))
print("equality count", len(eq))
for e in eq[:10]:
    print(e)

print("\n=== Theoretical check: for WoW bipartite, hyp always & concl via sqrt(ab) ===")
print("For connected bipartite parts A,B: Ev(v)=|own part|, Odd=|other|")
print("sum Odd=2|A||B|, sum Ev=|A|^2+|B|^2, hyp iff (a-b)^2>=0 always")
print("λ1<=sqrt(ab)<=max(a,b)=max Ev. PROVED for all connected bipartite.")

print("\n=== Non-bipartite WoW: try Nosal / Nikiforov triangle bounds ===")
# If G has triangles, λ1^2 could relate to edges differently
# Perhaps use: λ1 <= max_v sqrt(sum_{u~v} d(u)) etc.

print("\n=== Is lamp ≤ max_ev always under hyp? (stronger claim) ===")
for include_self, tag in [(True,"WoW"),(False,"code")]:
    bad = 0
    tot = 0
    worst = 0
    for G in nx.graph_atlas_g():
        if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
            continue
        r = check_graph(G, include_self)
        if r["hyp"]:
            tot += 1
            if r["lam_p"] > r["max_ev"] + 1e-8:
                bad += 1
            worst = max(worst, r["lam_p"] - r["max_ev"])
    # also random
    for _ in range(2000):
        n = rng.randint(5, 18)
        G = nx.erdos_renyi_graph(n, rng.uniform(0.1, 0.5), seed=rng.randint(0,10**9))
        if not nx.is_connected(G):
            continue
        r = check_graph(G, include_self)
        if r["hyp"]:
            tot += 1
            if r["lam_p"] > r["max_ev"] + 1e-8:
                bad += 1
            worst = max(worst, r["lam_p"] - r["max_ev"])
    print(tag, f"lam_p>max_ev: {bad}/{tot} worst_gap={worst}")
