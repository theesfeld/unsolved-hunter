# structured families for Graffiti 195
import numpy as np, networkx as nx, itertools, sys
from inv import eval195
res = []
def test(name, G):
    if G.number_of_nodes()<2: return
    if not nx.is_connected(G): return
    A = nx.to_numpy_array(G)
    r = eval195(A)
    mg, ev, od, _ = r
    res.append((mg, ev - od, name, G.number_of_nodes(), nx.diameter(G)))

for s in range(3, 30):
    K = nx.complete_graph(s)
    G=nx.complete_graph(s)
    for i in range(s): G.add_edge(i, s+i)
    test(f"corona K{s}oK1", G)
for n in range(5, 60):
    test(f"C{n}", nx.cycle_graph(n)); test(f"P{n}", nx.path_graph(n))
for q in [5,9,13,17,25,29,37,41,49,53]:
    try: test(f"Paley{q}", nx.paley_graph(q).to_undirected())
    except Exception as e: pass
for a in range(1, 15):
    for b in range(a, 15):
        test(f"K{a},{b}", nx.complete_bipartite_graph(a, b))
for n1 in range(3, 12):
    for k in range(1, n1//2):
        test(f"Kneser{n1},{k}", nx.kneser_graph(n1, k))
for d in range(2, 8):
    test(f"Q{d}", nx.hypercube_graph(d))
for a in range(2, 9):
    for b in range(2, 9):
        test(f"grid{a}x{b}", nx.grid_2d_graph(a, b)); test(f"torus{a}x{b}", nx.grid_2d_graph(a, b, periodic=True) if a>2 and b>2 else nx.empty_graph(1))
        test(f"rook{a}x{b}", nx.cartesian_product(nx.complete_graph(a), nx.complete_graph(b)))
for name in ["petersen_graph","heawood_graph","dodecahedral_graph","icosahedral_graph","mobius_kantor_graph","pappus_graph","desargues_graph","tutte_graph","coxeter_graph" if hasattr(nx,'coxeter_graph') else "petersen_graph","chvatal_graph","frucht_graph","truncated_tetrahedron_graph","sedgewick_maze_graph","hoffman_singleton_graph","octahedral_graph","cubical_graph","krackhardt_kite_graph","bull_graph","house_graph","house_x_graph","moebius_kantor_graph" if hasattr(nx,'moebius_kantor_graph') else "petersen_graph"]:
    if hasattr(nx, name): test(name, getattr(nx, name)())
# lollipops, barbells, windmills, friendship
for a in range(3, 15):
    for b in range(1, 10):
        test(f"lollipop{a},{b}", nx.lollipop_graph(a, b)); test(f"barbell{a},{b}", nx.barbell_graph(a, b))
# kite/pineapple: clique K_s + pendants on one vertex
for s in range(3, 20):
    for t in range(1, 20):
        G = nx.complete_graph(s); 
        for i in range(t): G.add_edge(0, s+i)
        test(f"pineapple{s},{t}", G)
# circulants
for n in range(6, 30):
    for k in range(1, 5):
        for S in itertools.combinations(range(1, n//2+1), k):
            test(f"circ{n}{S}", nx.circulant_graph(n, S))
# random geometric / strongly regular from atlas
for i in range(1, 1253):
    G = nx.graph_atlas(i)
    if G.number_of_nodes() > 2: test(f"atlas{i}", G)
ok = [r for r in res if r[1] >= 0]
ok.sort(reverse=True)
print("best with condition even>=odd (margin, even-odd, name, n, diam):")
for r in ok[:15]: print(r)
nc = sorted(res, reverse=True)
print("best ignoring condition:")
for r in nc[:10]: print(r)
print("best diam>=3 with condition:")
for r in [r for r in ok if r[4] >= 3][:10]: print(r)
