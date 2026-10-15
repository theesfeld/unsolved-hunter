#!/usr/bin/env python3
# Paper's Fig.2 caption: bound identical with ONLY the K_{2,3} constraint. Check: 24 disjoint K4 + 3 isolated vertices.
from verify import make, add, disjoint_union, stats, brute_diamond_k23
K4 = make(4); [add(K4, u, v) for u in range(4) for v in range(u+1, 4)]
iso = make(3)
G, _ = disjoint_union([K4]*24 + [iso]); s = stats(G); d, k = brute_diamond_k23(G)
print("24xK4+3K1:", s, "diamond:", d, "K23:", k)
