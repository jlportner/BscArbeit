import numpy as np
import networkx as nx
from itertools import permutations
from sympy.combinatorics import Permutation

def createMC(n,i=0,j=0, perm = 0):
    H1 = nx.cycle_graph(np.arange(n))
    H2 = nx.cycle_graph(np.arange(n, 2 * n))
    G = nx.MultiGraph(nx.compose(H1, H2))
    if perm == 0:
        G.add_edges_from(np.arange(2 * n).reshape((2, -1)).T)
    else:
        G.add_edges_from(np.vstack((np.arange(n),perm)).T)
    nx.set_edge_attributes(G, False, 'forest')
    nx.set_edge_attributes(G, -1, 'order')

    forest = np.hstack((np.vstack((np.vstack((np.arange(n - 1), np.arange(1, n))).T,
                        np.vstack((np.arange(n, 2 * n - 1), np.arange(n + 1, 2 * n))).T)),np.zeros((2*n-2,1))))
    if i != n-1:
        forest[i] = [0, n - 1,0]
    if j != n-1:
        forest[n-1 + j] = [n,2*n-1,0]

    for i, e in enumerate(forest):
        G.edges[e]['forest'] = True
        G.edges[e]['order'] = i + 1

    return G

def createAllMCOf(n):
    dG = []
    for perm in permutations(np.arange(n,2*n)):
        G = createMC(n,n-1,n-1,perm)
        perm = Permutation(np.array(perm)-n)
        dG += [[(-1) ** perm.parity(),G]]
    return dG

def createMCPos(n,center=(0,0)):
    scale = 100.0
    lAng = np.linspace(np.pi / 2, -np.pi / 2, n)
    lPoints = scale*np.vstack((np.cos(lAng) - 2.0 + center[0], np.sin(lAng) + center[1])).T
    lPos = dict(enumerate(lPoints.tolist(), 0))

    rAng = np.linspace(np.pi / 2, 3 * np.pi / 2, n)
    rPoints = scale*np.vstack((np.cos(rAng) + 2.0 + center[0], np.sin(rAng) + center[1])).T
    rPos = dict(enumerate(rPoints.tolist(), n))
    return lPos | rPos

def rotateMCPos(pos,r):
    n = int(len(pos)/2)
    pos = np.array(list(pos.values()))
    lPos = np.roll(pos[:n],r,axis=0)
    rPos = np.roll(pos[n:], r, axis=0)
    return dict(enumerate(lPos.tolist(), 0)) | dict(enumerate(rPos.tolist(), n))

