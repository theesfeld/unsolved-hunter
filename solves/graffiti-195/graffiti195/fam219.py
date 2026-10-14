import numpy as np, networkx as nx
from inv import eval219
def T(name, G):
    A = nx.to_numpy_array(G); r = eval219(A)
    print(f"{name:28s} n={G.number_of_nodes():3d} lam2={r[1]:10.3f} nonedges={r[2]:8.1f} margin={r[0]:10.3f}")
for n in [10, 20, 40, 80, 160]:
    K = nx.complete_graph(n)
    G = K.copy(); G.remove_edge(0, 1); T("K_n - e", G)
    G = K.copy(); G.remove_edges_from([(0, i) for i in range(1, n//2)]); T("K_n - star(n/2)", G)
    G = K.copy(); G.remove_edges_from([(2*i, 2*i+1) for i in range(n//2)]); T("cocktail party", G)
    G = nx.complete_multipartite_graph(n//2, n - n//2); T("K_{n/2,n/2}", G)
    G = nx.barbell_graph(n//2, 0); T("barbell(n/2,0)", G)
    G = nx.complete_graph(n//2); H = nx.relabel_nodes(nx.complete_graph(n - n//2), lambda x: x + n//2); G = nx.union(G, H)
    G.add_edges_from([(i, n//2 + i) for i in range(n//4)]); T("2K_{n/2}+partial matching", G)
    G = nx.union(nx.complete_graph(n//2), nx.relabel_nodes(nx.complete_graph(n - n//2), lambda x: x + n//2)); T("2K_{n/2} disconnected", G)
    G = nx.union(nx.complete_bipartite_graph(n//4, n//4), nx.relabel_nodes(nx.complete_bipartite_graph(n//4, n - 3*(n//4)), lambda x: x + n//2)); T("2K_{n/4,n/4} disconnected (tf)", G)
