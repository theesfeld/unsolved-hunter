#!/usr/bin/env python3
"""Independent verification of Graffiti conjecture 195."""
import itertools
import math
import random
from collections import deque

import networkx as nx
import numpy as np

# ---------- definitions ----------
def even_odd_counts(G, include_self=True):
    """Return Ev[v], Odd[v] for each node (as dicts)."""
    nodes = list(G.nodes())
    Ev, Odd = {}, {}
    for v in nodes:
        ev = 1 if include_self else 0
        od = 0
        dist = nx.single_source_shortest_path_length(G, v)
        for u in nodes:
            if u == v:
                continue
            d = dist[u]
            if d % 2 == 0:
                ev += 1
            else:
                od += 1
        Ev[v] = ev
        Odd[v] = od
    return Ev, Odd


def spectral_radius(G):
    if G.number_of_nodes() == 0:
        return 0.0
    A = nx.to_numpy_array(G, dtype=float)
    # symmetric real
    w = np.linalg.eigvalsh(A)
    return float(w[-1])


def odd_distance_graph(G):
    """G': edge uv iff dist_G(u,v) is odd."""
    nodes = list(G.nodes())
    Gp = nx.Graph()
    Gp.add_nodes_from(nodes)
    dist = dict(nx.all_pairs_shortest_path_length(G))
    for i, u in enumerate(nodes):
        for v in nodes[i + 1 :]:
            if dist[u][v] % 2 == 1:
                Gp.add_edge(u, v)
    return Gp


def check_graph(G, include_self=True, tol=1e-9):
    """Return dict with hypothesis, conclusion, and proof-step quantities."""
    if not nx.is_connected(G):
        return None
    n = G.number_of_nodes()
    Ev, Odd = even_odd_counts(G, include_self=include_self)
    sum_ev = sum(Ev.values())
    sum_od = sum(Odd.values())
    max_ev = max(Ev.values())
    max_od = max(Odd.values())
    lam = spectral_radius(G)
    hyp = sum_od <= sum_ev + tol
    concl = lam <= max_ev + tol
    Gp = odd_distance_graph(G)
    lam_p = spectral_radius(Gp)
    m_p = Gp.number_of_edges()
    # Hong–Shu–Fang (connected graphs with n>=1): λ1 <= sqrt(2m-n+1)
    hong = math.sqrt(max(0.0, 2 * m_p - n + 1)) if n >= 1 else 0.0
    # Nikiforov-style crude: λ1 <= sqrt(2m)
    niki = math.sqrt(2 * m_p)
    # degree bound on G'
    deg_bound = max((d for _, d in Gp.degree()), default=0)
    return {
        "n": n,
        "m": G.number_of_edges(),
        "sum_ev": sum_ev,
        "sum_od": sum_od,
        "max_ev": max_ev,
        "max_od": max_od,
        "lam": lam,
        "hyp": hyp,
        "concl": concl,
        "violates": hyp and not concl,
        "lam_p": lam_p,
        "m_p": m_p,
        "hong": hong,
        "niki": niki,
        "deg_bound": deg_bound,
        "G_subseteq_Gp": set(G.edges()).issubset(set(Gp.edges())) or set(tuple(sorted(e)) for e in G.edges()).issubset(set(tuple(sorted(e)) for e in Gp.edges())),
        "lam_le_lamp": lam <= lam_p + tol,
        "hong_le_maxev": hong <= max_ev + tol,
        "niki_le_maxev": niki <= max_ev + tol,
        "deg_le_maxev": deg_bound <= max_ev + tol,
        "lamp_le_maxev": lam_p <= max_ev + tol,
    }


def graph_label(G):
    return f"n={G.number_of_nodes()} m={G.number_of_edges()}"


# ---------- exhaustive small connected graphs ----------
def exhaustive(n_max=7, include_self=True):
    viol = []
    tight = []
    hyp_count = 0
    checked = 0
    proof_hong_fail = []
    proof_niki_fail = []
    proof_deg_fail = []
    for n in range(1, n_max + 1):
        # all nonisomorphic connected graphs
        for G in nx.graph_atlas_g():
            if G.number_of_nodes() != n:
                continue
            if n >= 1 and (G.number_of_nodes() == 0 or not nx.is_connected(G)):
                continue
            if n == 0:
                continue
            # atlas includes empties; skip disconnected
            r = check_graph(G, include_self=include_self)
            if r is None:
                continue
            checked += 1
            if r["hyp"]:
                hyp_count += 1
                gap = r["max_ev"] - r["lam"]
                if r["violates"]:
                    viol.append((G.copy(), r))
                if abs(gap) < 1e-8:
                    tight.append((G.copy(), r))
                # proof step failures (among hyp graphs)
                if not r["hong_le_maxev"]:
                    proof_hong_fail.append((G.copy(), r))
                if not r["niki_le_maxev"]:
                    proof_niki_fail.append((G.copy(), r))
                if not r["deg_le_maxev"]:
                    proof_deg_fail.append((G.copy(), r))
    return {
        "checked": checked,
        "hyp_count": hyp_count,
        "viol": viol,
        "tight": tight,
        "proof_hong_fail": proof_hong_fail,
        "proof_niki_fail": proof_niki_fail,
        "proof_deg_fail": proof_deg_fail,
    }


# ---------- random / structured families ----------
def families(include_self=True, seed=0):
    rng = random.Random(seed)
    viol = []
    hyp_ok = 0
    hyp_total = 0
    hong_fail = 0
    niki_fail = 0
    deg_fail = 0
    samples = []

    def consider(G, tag):
        nonlocal hyp_ok, hyp_total, hong_fail, niki_fail, deg_fail
        if G.number_of_nodes() < 1 or not nx.is_connected(G):
            return
        # simplify to simple undirected
        G = nx.Graph(G)
        G.remove_edges_from(nx.selfloop_edges(G))
        r = check_graph(G, include_self=include_self)
        if r is None:
            return
        samples.append((tag, r))
        if r["hyp"]:
            hyp_total += 1
            if r["concl"]:
                hyp_ok += 1
            else:
                viol.append((tag, G.copy(), r))
            if not r["hong_le_maxev"]:
                hong_fail += 1
            if not r["niki_le_maxev"]:
                niki_fail += 1
            if not r["deg_le_maxev"]:
                deg_fail += 1

    # paths, cycles, stars, complete, complete bipartite
    for n in range(2, 31):
        consider(nx.path_graph(n), f"P_{n}")
        consider(nx.cycle_graph(n), f"C_{n}")
        consider(nx.star_graph(n - 1), f"S_{n}")
        consider(nx.complete_graph(n), f"K_{n}")
        consider(nx.wheel_graph(n), f"W_{n}")
    for a in range(1, 16):
        for b in range(a, 16):
            consider(nx.complete_bipartite_graph(a, b), f"K_{a},{b}")
    # trees random
    for n in range(3, 25):
        for t in range(30):
            consider(nx.random_labeled_tree(n, seed=rng.randint(0, 10**9)), f"tree_{n}_{t}")
    # Erdős–Rényi connected
    for n in range(4, 20):
        for p in (0.1, 0.2, 0.3, 0.5, 0.8):
            for t in range(20):
                G = nx.erdos_renyi_graph(n, p, seed=rng.randint(0, 10**9))
                if nx.is_connected(G):
                    consider(G, f"ER_{n}_{p}_{t}")
    # Barabasi–Albert
    for n in range(5, 25):
        for m in (1, 2, 3):
            if m < n:
                for t in range(10):
                    consider(nx.barabasi_albert_graph(n, m, seed=rng.randint(0, 10**9)), f"BA_{n}_{m}_{t}")
    # Petersen, Heawood, etc.
    for name, G in [
        ("petersen", nx.petersen_graph()),
        ("dodecahedral", nx.dodecahedral_graph()),
        ("icosahedral", nx.icosahedral_graph()),
        ("cubical", nx.cubical_graph()),
        ("octahedral", nx.octahedral_graph()),
        ("moebius_kantor", nx.moebius_kantor_graph()),
        ("heawood", nx.heawood_graph()),
        ("pappus", nx.pappus_graph()),
        ("desargues", nx.desargues_graph()),
        ("tutte", nx.tutte_graph()),
    ]:
        consider(G, name)

    # blowups / strong products-ish: complement of matching etc.
    for n in range(4, 16, 2):
        G = nx.complete_graph(n)
        # remove a perfect matching
        for i in range(0, n, 2):
            if G.has_edge(i, i + 1):
                G.remove_edge(i, i + 1)
        consider(G, f"K_n-matching_{n}")

    return {
        "hyp_total": hyp_total,
        "hyp_ok": hyp_ok,
        "viol": viol,
        "hong_fail": hong_fail,
        "niki_fail": niki_fail,
        "deg_fail": deg_fail,
        "n_samples": len(samples),
    }


def analyze_proof_steps(include_self=True):
    """Check each alleged proof step on families where hyp holds."""
    rows = []
    graphs = []
    for n in range(2, 20):
        graphs.append(nx.path_graph(n))
        graphs.append(nx.cycle_graph(n))
        graphs.append(nx.star_graph(n - 1))
        graphs.append(nx.complete_graph(n))
    for a in range(1, 10):
        for b in range(a, 10):
            graphs.append(nx.complete_bipartite_graph(a, b))
    for G in nx.graph_atlas_g():
        if 1 <= G.number_of_nodes() <= 7 and nx.is_connected(G):
            graphs.append(G)

    step1_ok = step2_ok = 0
    step3_hong_ok = step3_niki_ok = step3_deg_ok = 0
    hyp_n = 0
    hong_counterexamples = []
    for G in graphs:
        r = check_graph(G, include_self=include_self)
        if r is None or not r["hyp"]:
            continue
        hyp_n += 1
        if r["G_subseteq_Gp"]:
            step1_ok += 1
        if r["lam_le_lamp"]:
            step2_ok += 1
        if r["hong_le_maxev"]:
            step3_hong_ok += 1
        else:
            if len(hong_counterexamples) < 5:
                hong_counterexamples.append(r)
        if r["niki_le_maxev"]:
            step3_niki_ok += 1
        if r["deg_le_maxev"]:
            step3_deg_ok += 1
    return {
        "hyp_n": hyp_n,
        "step1_G_subseteq_Gp": step1_ok,
        "step2_lam_le_lamp": step2_ok,
        "step3_hong_le_maxev": step3_hong_ok,
        "step3_niki_le_maxev": step3_niki_ok,
        "step3_deg_le_maxev": step3_deg_ok,
        "hong_counterexamples": hong_counterexamples,
    }


if __name__ == "__main__":
    print("=== Atlas exhaustive ===")
    for inc in (True, False):
        tag = "Ev includes self (WoW)" if inc else "Ev excludes self (code)"
        print(f"\n--- {tag} ---")
        ex = exhaustive(7, include_self=inc)
        print(f"checked={ex['checked']} hyp={ex['hyp_count']} viol={len(ex['viol'])} tight={len(ex['tight'])}")
        print(f"hong_fail={len(ex['proof_hong_fail'])} niki_fail={len(ex['proof_niki_fail'])} deg_fail={len(ex['proof_deg_fail'])}")
        if ex["viol"]:
            G, r = ex["viol"][0]
            print("FIRST VIOLATION:", r)
            print("edges", list(G.edges()))
        if ex["proof_hong_fail"]:
            G, r = ex["proof_hong_fail"][0]
            print("HONG FAIL sample:", {k: r[k] for k in ['n','lam','max_ev','hong','sum_od','sum_ev','m_p','lam_p']})

    print("\n=== Families ===")
    for inc in (True, False):
        tag = "Ev includes self (WoW)" if inc else "Ev excludes self (code)"
        print(f"\n--- {tag} ---")
        fam = families(include_self=inc)
        print(f"samples={fam['n_samples']} hyp={fam['hyp_total']} ok={fam['hyp_ok']} viol={len(fam['viol'])}")
        print(f"hong_fail={fam['hong_fail']} niki_fail={fam['niki_fail']} deg_fail={fam['deg_fail']}")
        if fam["viol"]:
            tag, G, r = fam["viol"][0]
            print("FIRST VIOLATION:", tag, {k: r[k] for k in ['n','lam','max_ev','sum_od','sum_ev']})

    print("\n=== Proof step analysis ===")
    for inc in (True, False):
        tag = "Ev includes self (WoW)" if inc else "Ev excludes self (code)"
        print(f"\n--- {tag} ---")
        pr = analyze_proof_steps(include_self=inc)
        print(pr["hyp_n"], pr["step1_G_subseteq_Gp"], pr["step2_lam_le_lamp"],
              pr["step3_hong_le_maxev"], pr["step3_niki_le_maxev"], pr["step3_deg_le_maxev"])
        if pr["hong_counterexamples"]:
            print("hong cx sample", pr["hong_counterexamples"][0])
