import numpy as np
from scipy.sparse.csgraph import shortest_path

def dist(A):
    return shortest_path(A, method='D', unweighted=True)

def eval195(A):
    """returns (margin=lam1-maxEv, even_pairs, odd_pairs, connected)"""
    n = len(A)
    D = dist(A)
    if np.isinf(D).any():
        return None
    Di = D.astype(int)
    off = ~np.eye(n, dtype=bool)
    evm = ((Di % 2 == 0) & off)
    ev = evm.sum(1)
    even = ev.sum() / 2
    odd = n*(n-1)/2 - even
    lam1 = np.linalg.eigvalsh(A)[-1]
    return lam1 - ev.max(), even, odd, ev

def gravity(A, D=None):
    n = len(A)
    if D is None: D = dist(A)
    d = A.sum(1)
    with np.errstate(divide='ignore'):
        G = np.outer(d, d) / ((n-1) * D)
    G[~np.isfinite(G)] = 0
    np.fill_diagonal(G, 0)
    return G

def eval219(A):
    n = len(A)
    D = dist(A)
    if np.isinf(D).any(): return None
    G = gravity(A, D)
    w = np.linalg.eigvalsh(G)
    m = A.sum() / 2
    other = n*(n-1)/2 - m
    return w[-2] - other, w[-2], other

def triangle_free(A):
    return np.trace(A @ A @ A) == 0
