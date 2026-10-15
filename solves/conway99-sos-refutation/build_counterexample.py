#!/usr/bin/env python3
"""Reproducible counterexample to Natal–Al-saadi arXiv:2610.16266 Conjecture 5.

Claim refuted: every D-free & K2,3-free simple graph on 99 verts has ≤55 triangles.
Construction: 11 disjoint copies of srg(9,4,1,2) → 66 triangles; optional path bridges → connected.
"""
import itertools
import numpy as np

def lattice_3x3():
    V = [(r, c) for r in range(3) for c in range(3)]
    idx = {v: i for i, v in enumerate(V)}
    A = np.zeros((9, 9), dtype=int)
    for r, c in V:
        i = idx[(r, c)]
        for c2 in range(3):
            if c2 != c:
                A[i, idx[(r, c2)]] = 1
        for r2 in range(3):
            if r2 != r:
                A[i, idx[(r2, c)]] = 1
    return A

def triangles(A):
    return int(np.trace(np.linalg.matrix_power(A.astype(object), 3)) // 6)

def max_cn(A):
    C = A @ A
    n = A.shape[0]
    mx_adj = mx_non = 0
    for i, j in itertools.combinations(range(n), 2):
        cn = int(C[i, j])
        if A[i, j]:
            mx_adj = max(mx_adj, cn)
        else:
            mx_non = max(mx_non, cn)
    return mx_adj, mx_non

def main():
    A9 = lattice_3x3()
    assert triangles(A9) == 6 and max_cn(A9) == (1, 2)
    blocks = 11
    n = 9 * blocks
    A = np.zeros((n, n), dtype=int)
    for b in range(blocks):
        A[b * 9:(b + 1) * 9, b * 9:(b + 1) * 9] = A9
    t = triangles(A)
    mx = max_cn(A)
    print(f"disjoint: n={n} triangles={t} max_cn_adj_non={mx}")
    assert t == 66 and mx[0] <= 1 and mx[1] <= 2
    Ac = A.copy()
    for b in range(blocks - 1):
        i, j = b * 9, (b + 1) * 9 + 1
        Ac[i, j] = Ac[j, i] = 1
    tc = triangles(Ac)
    mxc = max_cn(Ac)
    print(f"connected: triangles={tc} max_cn_adj_non={mxc}")
    assert tc == 66 and mxc[0] <= 1 and mxc[1] <= 2
    print("OK: refutes T(99)<=55")

if __name__ == "__main__":
    main()
