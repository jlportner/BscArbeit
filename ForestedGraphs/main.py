from boundaries import *
from MoritaCycles import *
from plotting import *

n=5
path = "MCCycle" + str(n)
C = createAllMCOf(n)
C = resolveIsos(C)
C = resolveVanishing(C)
pltChain(C,lambda x: createMCPos(n,center=x),path,lineWidth=3)

dC = delta(C)
print(dC)