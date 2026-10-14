#!/usr/bin/env python3
"""Final fairness / triviality checks and code-reading edge cases."""
import math
import networkx as nx
from verify195 import check_graph, even_odd_counts, spectral_radius

print("=== WoW: fraction of graphs where hyp holds ===")
for n in range(1, 8):
    tot = hyp = bip = hyp_nonbip = 0
    for G in nx.graph_atlas_g():
        if G.number_of_nodes()!=n or not nx.is_connected(G):
            continue
        tot += 1
        r = check_graph(G, True)
        isb = nx.is_bipartite(G)
        if isb: bip += 1
        if r["hyp"]:
            hyp += 1
            if not isb: hyp_nonbip += 1
    print(f"n={n}: tot={tot} bip={bip} hyp={hyp} hyp_nonbip={hyp_nonbip}")

print("\n=== Code reading: same ===")
for n in range(1, 8):
    tot = hyp = hyp_bip = hyp_nonbip = 0
    for G in nx.graph_atlas_g():
        if G.number_of_nodes()!=n or not nx.is_connected(G):
            continue
        tot += 1
        r = check_graph(G, False)
        isb = nx.is_bipartite(G)
        if r["hyp"]:
            hyp += 1
            if isb: hyp_bip += 1
            else: hyp_nonbip += 1
    print(f"n={n}: tot={tot} hyp={hyp} hyp_bip={hyp_bip} hyp_nonbip={hyp_nonbip}")

print("\n=== Code reading: star S_n ===")
for n in range(2, 12):
    G = nx.star_graph(n-1)
    for inc, tag in [(True,"WoW"),(False,"code")]:
        r = check_graph(G, inc)
        print(f"S_{n} {tag}: hyp={r['hyp']} lam={r['lam']:.4f} maxEv={r['max_ev']} concl={r['concl']}")

print("\n=== Step-by-step hole summary on a concrete graph ===")
# Path P4: WoW hyp true, Hong(G') > max Ev
G = nx.path_graph(4)
r = check_graph(G, True)
Gp_edges = list(__import__('verify195').odd_distance_graph(G).edges())
print("P4 WoW", {k:r[k] for k in ['lam','max_ev','hong','niki','deg_bound','lam_p','sum_od','sum_ev','m_p']})
print("G' edges", Gp_edges)
print("Hong bound", r['hong'], "> maxEv", r['max_ev'], "?", r['hong']>r['max_ev'])
print("Yet conclusion holds:", r['concl'])

print("\n=== Is claim 'true' vs 'proof works'? ===")
print("Empirical support: strong. Alleged proof: HOLED.")
print("Bipartite WoW: trivial theorem, hyp vacuous.")
