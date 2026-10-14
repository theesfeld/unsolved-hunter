#!/usr/bin/env python3
"""Attempt to close a valid proof for Graffiti 195."""
import math
import networkx as nx
import numpy as np
from verify195 import check_graph, even_odd_counts, odd_distance_graph, spectral_radius

# Equality nonbipartite graph from atlas
for G in nx.graph_atlas_g():
    if G.number_of_nodes()==6 and G.number_of_edges()==9 and nx.is_connected(G):
        r = check_graph(G, True)
        if r["hyp"] and abs(r["lam"]-r["max_ev"])<1e-8 and not nx.is_bipartite(G):
            print("nonbip eq edges", list(G.edges()))
            print(r)
            Ev, Odd = even_odd_counts(G, True)
            print("Ev", Ev, "Odd", Odd)

print("\n=== Bound tests on hyp graphs where Delta(G') > max Ev ===")
# Try: λ1^2 <= max_v sum_{u adj' v} Odd(u)  (walk count / Hofmeister-ish)
# Also Nosal: if m > n^2/4 then triangle — converse under hyp m'<=n^2/4 so G' could be triangle-free
# Mantel: triangle-free => m <= n^2/4, λ1 <= sqrt(m) ? for bipartite yes λ1<=sqrt(m) for any graph? No λ1<=sqrt(2m).
# Actually for triangle-free, λ1 <= sqrt(m) by Nosal's theorem!

def nosal_check():
    """Nosal: triangle-free => λ1 <= sqrt(m). If G' triangle-free under hyp, λ1(G')<=sqrt(m')<=n/2<=max Ev?"""
    # Is G' triangle-free when hyp holds?
    # Odd-distance triangles: three vertices pairwise at odd distance.
    # In bipartite G, G'=K_a,b is triangle-free! Yes.
    # In non-bipartite, G' may have triangles.
    tri_free = tri = 0
    nosal_ok = hong_ok = 0
    hypn = 0
    for G in nx.graph_atlas_g():
        if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
            continue
        r = check_graph(G, True)
        if not r["hyp"]:
            continue
        hypn += 1
        Gp = odd_distance_graph(G)
        is_tf = nx.triangles(Gp)
        ntri = sum(is_tf.values())//3
        if ntri == 0:
            tri_free += 1
            # Nosal
            if math.sqrt(r["m_p"]) <= r["max_ev"] + 1e-9:
                nosal_ok += 1
        else:
            tri += 1
    print(f"hyp={hypn} G' triangle-free={tri_free} with_triangles={tri}")
    print(f"among triangle-free, sqrt(m')<=maxEv: {nosal_ok}/{tri_free}")

nosal_check()

print("\n=== When G' has triangles, does λ1(G') still ≤ max Ev? ===")
# Already empirically yes. Why?
# Use: spectral radius of G' <= max Odd * (something)

print("\n=== Perron idea: compare to Ev vector ===")
# Let x be all-ones. Then A' 1 = Odd (as vector). 
# Rayleigh: λ1 >= 1^T A' 1 / 1^T 1 = 2m'/n = sum Odd / n
# Upper: not from all-ones.

# Try bound of Favaron–Mahéo–Saclé / Hong–Shu–Fang sharper form:
# λ1 <= (d-1 + sqrt((d+1)^2 + 4(2m - d(d+1) - Delta something)))/2 ... complex

# Nikiforov: λ1^2 <= max_i sum_{j~i} d_j
def nik_walk(G):
    A = nx.to_numpy_array(G, dtype=float)
    deg = A.sum(axis=1)
    s = (A @ deg).max()
    return math.sqrt(s)

bad = 0
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if not r["hyp"]:
        continue
    Gp = odd_distance_graph(G)
    b = nik_walk(Gp)
    if b > r["max_ev"] + 1e-9:
        bad += 1
print(f"sqrt(max sum_{{u~v}} Odd(u)) > maxEv in {bad} hyp graphs")

# Another classical: λ1 <= max_{uv in E} sqrt(Odd(u)*Odd(v))
bad = 0
ex = None
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if not r["hyp"]:
        continue
    Gp = odd_distance_graph(G)
    Ev, Odd = even_odd_counts(G, True)
    mx = 0
    for u,v in Gp.edges():
        mx = max(mx, math.sqrt(Odd[u]*Odd[v]))
    if mx > r["max_ev"] + 1e-9:
        bad += 1
        if ex is None:
            ex = (r, mx, Odd, Ev, list(G.edges()))
print(f"max sqrt(Odd u Odd v) > maxEv in {bad}")
if ex:
    print("example", ex[0]["n"], "bound", ex[1], "maxev", ex[0]["max_ev"], "Odd", ex[2])

print("\n=== Key structural lemma attempt ===")
# Claim: under hyp, G' is bipartite? Then Nosal/Mantel + λ1<=sqrt(m')<=n/2, and maxEv>=n/2.
# Check if G' bipartite under hyp
bip_gp = nonbip_gp = 0
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if not r["hyp"]:
        continue
    Gp = odd_distance_graph(G)
    if nx.is_bipartite(Gp):
        bip_gp += 1
    else:
        nonbip_gp += 1
print(f"under hyp, G' bipartite: {bip_gp}, nonbipartite: {nonbip_gp}")
# If G is bipartite, G' is complete bipartite, hence bipartite.
# If G nonbipartite, G' often has odd cycles.

print("\n=== n/2 argument for triangle-free G' ===")
# Under hyp max Ev >= avg Ev = (n^2 - sum Odd)/n >= n/2
# If G' triangle-free, Nosal: λ1(G') <= sqrt(m') <= sqrt(sum Odd / 2) <= sqrt(n^2/4) = n/2 <= max Ev
# THIS WORKS when G' is triangle-free!
# So remaining case: G' has a triangle (pairwise odd distances).

print("Remaining hard case: hyp + G' contains a triangle.")

# Count how often
hard = 0
hard_ok = 0
min_gap = 999
for G in nx.graph_atlas_g():
    if not (1 <= G.number_of_nodes() <= 7 and nx.is_connected(G)):
        continue
    r = check_graph(G, True)
    if not r["hyp"]:
        continue
    Gp = odd_distance_graph(G)
    if sum(nx.triangles(Gp).values()) > 0:
        hard += 1
        gap = r["max_ev"] - r["lam"]
        min_gap = min(min_gap, gap)
        if r["concl"]:
            hard_ok += 1
print(f"hard case atlas: {hard_ok}/{hard} concl holds, min gap {min_gap}")

# Larger hard cases
import random
rng = random.Random(0)
hard = hard_ok = 0
min_gap = 999
worst = None
for _ in range(3000):
    n = rng.randint(6, 16)
    G = nx.erdos_renyi_graph(n, rng.uniform(0.2, 0.6), seed=rng.randint(0,10**9))
    if not nx.is_connected(G):
        continue
    r = check_graph(G, True)
    if not r["hyp"]:
        continue
    Gp = odd_distance_graph(G)
    if sum(nx.triangles(Gp).values()) == 0:
        continue
    hard += 1
    gap = r["max_ev"] - r["lam"]
    if gap < min_gap:
        min_gap = gap
        worst = r
    if r["concl"]:
        hard_ok += 1
print(f"hard random: {hard_ok}/{hard} min_gap={min_gap} worst={worst}")
