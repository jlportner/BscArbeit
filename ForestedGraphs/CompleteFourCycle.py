import numpy as np
import networkx as nx

def createCompleteCircle():
    H1 = nx.cycle_graph(np.arange(n))

    H2 = nx.cycle_graph(np.arange(n, 2 * n))
    H3 = nx.cycle_graph(np.arange(2*n,3*n))
    H4 = nx.cycle_graph(np.arange(3*n, 4 * n))
    G = nx.MultiGraph(nx.compose_all([H1,H2,H3,H4]))
    G.add_edges_from([(0,3,0),(1,10,0),(2,6,0),(4,7,0),(5,11,0),(8,9,0)])
    nx.set_edge_attributes(G, False, 'forest')
    nx.set_edge_attributes(G, -1, 'order')

    forest = np.array([(0,1,0),(1,2,0),(3,4,0),(4,5,0),(6,7,0),(7,8,0),(9,10,0),(10,11,0)])

    for i, e in enumerate(forest):
        G.edges[e]['forest'] = True
        G.edges[e]['order'] = i + 1

    return G

def createCompleteCirclePos(center = (0,0)):
    scale = 100
    n = 3
    ulAng = np.linspace(0.0, -np.pi / 2, n)
    ulPoints = scale*np.vstack((np.cos(ulAng) - 2.0 + center[0], np.sin(ulAng) + 2.0 + center[1])).T
    ulPos = dict(enumerate(ulPoints.tolist(), 0))

    urAng = np.linspace(-np.pi, -np.pi / 2, n)
    urPoints = scale*np.vstack((np.cos(urAng) + 2.0 + center[0], np.sin(urAng) + 2.0 + center[1])).T
    urPos = dict(enumerate(urPoints.tolist(), n))

    dlAng = np.linspace(np.pi / 2, 0, n)
    dlPoints = scale*np.vstack((np.cos(dlAng) - 2.0 + center[0], np.sin(dlAng) - 2.0 + center[1])).T
    dlPos = dict(enumerate(dlPoints.tolist(), 2*n))

    drAng = np.linspace(np.pi, np.pi /2, n)
    drPoints = scale*np.vstack((np.cos(drAng) + 2.0 + center[0], np.sin(drAng) - 2.0 + center[1])).T
    drPos = dict(enumerate(drPoints.tolist(), 3*n))
    return ulPos | urPos | dlPos | drPos
