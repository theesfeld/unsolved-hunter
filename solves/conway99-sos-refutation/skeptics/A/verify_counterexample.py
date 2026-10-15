#!/usr/bin/env python3
"""
Skeptic A — independent verification of Natal & Al-saadi (arXiv:2610.16266)
Conjecture 5: T(99) <= 55 for diamond-free and K_{2,3}-free simple graphs.

We reconstruct the unique srg(9,4,1,2) (3x3 rook/lattice graph) from scratch,
verify its parameters and forbidden-subgraph freeness, then form the disjoint
union of 11 copies on 99 vertices. That graph is D-free and K2,3-free with
exactly 66 triangles, contradicting T(99) <= 55.
"""
from __future__ import annotations

import numpy as np


def lattice_9() -> np.ndarray:
    """Adjacency of the 3x3 lattice / rook's graph L_2(3).

    Vertices are cells (r,c) in {0,1,2}^2; edge iff same row or same column.
    This is the unique srg(9,4,1,2).
    """
    verts = [(r, c) for r in range(3) for c in range(3)]
    A = np.zeros((9, 9), dtype=np.int8)
    for i, (r1, c1) in enumerate(verts):
        for j, (r2, c2) in enumerate(verts):
            if i < j and (r1 == r2 or c1 == c2):
                A[i, j] = A[j, i] = 1
    return A


def check_srg(A: np.ndarray, v: int, k: int, lam: int, mu: int) -> None:
    """Assert A realizes srg(v,k,lambda,mu) via the standard equation."""
    n = A.shape[0]
    assert n == v
    degrees = A.sum(axis=1)
    assert np.all(degrees == k), f"bad degrees: {degrees}"
    A64 = A.astype(np.int64)
    I = np.eye(n, dtype=np.int64)
    J = np.ones((n, n), dtype=np.int64)
    lhs = A64 @ A64
    rhs = k * I + lam * A64 + mu * (J - I - A64)
    assert np.array_equal(lhs, rhs), "A^2 equation failed"


def count_triangles(A: np.ndarray) -> int:
    """K3 count = trace(A^3) / 6."""
    A64 = A.astype(np.int64)
    return int(np.trace(A64 @ A64 @ A64) // 6)


def common_neighbors(A: np.ndarray) -> np.ndarray:
    return A.astype(np.int64) @ A.astype(np.int64)


def is_diamond_free(A: np.ndarray) -> bool:
    """Diamond-free <=> no adjacent pair has >= 2 common neighbors."""
    C = common_neighbors(A)
    n = A.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j] and C[i, j] >= 2:
                return False
    return True


def is_K23_free(A: np.ndarray) -> bool:
    """K_{2,3}-free as a subgraph <=> no pair has >= 3 common neighbors."""
    C = common_neighbors(A)
    n = A.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if C[i, j] >= 3:
                return False
    return True


def max_common(A: np.ndarray) -> tuple[int, int]:
    """Max common neighbors over adjacent / non-adjacent pairs."""
    C = common_neighbors(A)
    n = A.shape[0]
    mx_adj, mx_non = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            cn = int(C[i, j])
            if A[i, j]:
                mx_adj = max(mx_adj, cn)
            else:
                mx_non = max(mx_non, cn)
    return mx_adj, mx_non


def block_diag_copies(A: np.ndarray, copies: int) -> np.ndarray:
    m = A.shape[0]
    n = m * copies
    out = np.zeros((n, n), dtype=np.int8)
    for t in range(copies):
        out[t * m : (t + 1) * m, t * m : (t + 1) * m] = A
    return out


def main() -> None:
    A9 = lattice_9()
    check_srg(A9, 9, 4, 1, 2)
    t9 = count_triangles(A9)
    assert t9 == 6
    assert is_diamond_free(A9) and is_K23_free(A9)
    assert max_common(A9) == (1, 2)

    A99 = block_diag_copies(A9, 11)
    assert A99.shape == (99, 99)
    t99 = count_triangles(A99)
    d_free = is_diamond_free(A99)
    k_free = is_K23_free(A99)
    mx = max_common(A99)

    print(f"srg(9,4,1,2) triangles={t9}, diamond_free={is_diamond_free(A9)}, "
          f"K23_free={is_K23_free(A9)}, max_common={max_common(A9)}")
    print(f"11 disjoint copies: n=99, triangles={t99}, diamond_free={d_free}, "
          f"K23_free={k_free}, max_common={mx}")
    print(f"edges={int(A99.sum() // 2)}, degrees={sorted(set(A99.sum(axis=1).tolist()))}")

    assert t99 == 66
    assert d_free and k_free
    assert mx == (1, 2)
    assert t99 > 55

    np.save("counterexample_99.npy", A99)
    print("COUNTEREXAMPLE OK: T(99) >= 66 > 55. Saved counterexample_99.npy")


if __name__ == "__main__":
    main()
