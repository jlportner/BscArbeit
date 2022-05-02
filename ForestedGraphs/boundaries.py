import numpy as np
import networkx as nx
from networkx.algorithms import isomorphism as nxiso
from sympy.combinatorics import Permutation

def getForest(G):
    o = nx.get_edge_attributes(G, 'order')
    return {key: val for key, val in o.items() if val != -1}


def contractEdge(G, e):
    H = G.copy()
    H.remove_edges_from([e])
    return nx.contracted_nodes(H, e[0], e[1])


edgeEquality = nx.isomorphism.categorical_multiedge_match("forest", False)


def deltaC(C):
    dC = []
    for k,G in C:
        F = getForest(G)
        dG = []
        for e, i in F.items():
            H = contractEdge(G, e)
            FH = getForest(H)
            for a, j in FH.items():
                if j > i:
                    H.edges[a]['order'] = j - 1
            dG.append([(-1) ** i * k, H])
        dC += dG
    return dC


def deltaR(C):
    dC = []
    for k,G in C:
        F = getForest(G)
        dG = []
        for e, i in F.items():
            H = G.copy()
            H.edges[e]['forest'] = False
            H.edges[e]['order'] = -1
            FH = getForest(H)
            for a, j in FH.items():
                if j > i:
                    H.edges[a]['order'] = j - 1
            dG.append([(-1) ** i * k, H])
        dC += dG
    return dC


def getForestPerm(F1, F2, g):
    F1 = {(k[0], k[1]): v for k, v in F1.items()}
    F2 = {(k[0], k[1]): v for k, v in F2.items()}
    sig = np.zeros(len(F1))
    for e, i in F1.items():
        se = (g[e[0]], g[e[1]])
        if se in F2:
            sig[i - 1] = F2[se]
        else:
            sig[i - 1] = F2[(se[1], se[0])]
    perm = Permutation(sig - 1.0)
    return (-1) ** perm.parity()


def resolveIsos(dG):
    i = 0
    n = len(dG)
    while i < n - 1:
        H1 = dG[i]
        j = i + 1
        while j < n:
            H2 = dG[j]
            GM = nxiso.GraphMatcher(H1[1], H2[1], edge_match=edgeEquality)
            if GM.is_isomorphic():
                sgn = getForestPerm(getForest(H1[1]), getForest(H2[1]), GM.mapping)
                H1[0] += sgn * H2[0]
                del dG[j]
                n += -1
            else:
                j += 1
        i += 1

    # remove 0s
    result = [G for G in dG if G[0] != 0]
    return result

def resolveVanishing(dG):
    def hasOddAuto(H):
        GM = nxiso.GraphMatcher(H, H, edge_match=edgeEquality)
        for g in GM.isomorphisms_iter():
            F = getForest(H)
            if getForestPerm(F, F, g) == -1:
                return 1
        return 0

    result = [G for G in dG if not hasOddAuto(G[1])]
    return result


def delta(G):
    dGC = deltaC(G)
    dGR = deltaR(G)
    dGC = resolveIsos(dGC)
    dGR = resolveIsos(dGR)

    dGR = np.array(dGR, dtype=object)
    dGR[:, 0] *= -1
    dG = dGC + dGR.tolist()
    return resolveVanishing(dG)
