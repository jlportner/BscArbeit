import os
import networkx as nx
from boundaries import *

def pltFG(H, pos,path = "out"):
    G = H.copy()
    forest = getForest(G)
    nx.set_edge_attributes(G,{key: {"color": "red", "label": val} for key, val in forest.items()})
    for n, npos in pos.items():
        if(G.has_node(n)):
            G.nodes[n]['pos'] = '"%d,%d"'%(npos[0],npos[1])
            G.nodes[n]['shape'] = "point"
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write(path + ".dot")
    os.system("neato -n2 -Tpng " + path + ".dot -o " + path + ".png")

def pltChain(C,posFunction,path="out",lineWidth=5):
    masterG = nx.MultiGraph()
    hPos = 0
    for j, (count,H) in enumerate(C):
        if j!= 0 and j % lineWidth == 0:
            hPos -= 3.0
        vPos = 6 * (j % lineWidth)
        pos = posFunction((vPos, hPos))
        G = H.copy()
        nx.set_edge_attributes(G,2.0,name="penwidth")
        forest = getForest(G)
        nx.set_edge_attributes(G, {key: {"color": "#ffa000", "penwidth": 3, "label": val} for key, val in forest.items()})

        for node, nodePos in pos.items():
            if(G.has_node(node)):
                G.nodes[node]['pos'] = '"%d,%d"' % (nodePos[0], nodePos[1])
                G.nodes[node]['shape'] = "point"
                G.nodes[node]['width'] = "0.15pt"
        masterG = nx.disjoint_union(masterG,G)
        cof = str(j) + "coef"
        masterG.add_node(cof)
        if j == 0:
            masterG.nodes[cof]['label'] = "  " + str(count)
        elif count >= 0:
            masterG.nodes[cof]['label'] = "+ " + str(count)
        else:
            masterG.nodes[cof]['label'] = "− " + str(abs(count))
        masterG.nodes[cof]['shape'] = "plaintext"
        masterG.nodes[cof]['fontsize'] = "26pt"
        if j % lineWidth == 0:
            masterG.nodes[cof]['pos'] = '"%d,%d"' %(100*(-2.5 + vPos), hPos*100)
        else:
            masterG.nodes[cof]['pos'] = '"%d,%d"' % (100 * (-3.0 + vPos), hPos * 100)


    p = nx.drawing.nx_pydot.to_pydot(masterG)

    p.write(path + ".dot")
    os.system("neato -n2 -Tpdf " + path + ".dot -o " + path + ".pdf")
