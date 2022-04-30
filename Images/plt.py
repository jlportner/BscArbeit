import numpy as np
import matplotlib.pyplot as plt

msize = 18**2
t = np.arange(26)

vcd = 1/2 * t
stb = 5/3 * t

moritaC = np.array([(4,4),(8,6),(12,8)])
morita = np.array([(16,10),(20,12),(24,14)])
bartholdi = np.array([(8,7),(11,7)])
plt.figure(figsize=(3.74,2.4))
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "serif",
  "font.serif": ["Computer Modern Roman"],
  "font.size": 10
})


plt.fill_between(t,vcd,stb,color=[0.7,0.7,0.7,0.3])
plt.plot(t,vcd,c='black')
plt.plot(t,stb,":",c='black')
plt.plot(t,np.zeros_like(t),"--",c='black')
plt.scatter(morita[:,0],morita[:,1],s=12**2,color=[0,0,0,0],marker='s',edgecolor='black')
plt.scatter(moritaC[:,0],moritaC[:,1],s=12**2,c='black',marker='s',edgecolor='black')
plt.scatter(bartholdi[:,0],bartholdi[:,1],s=msize,c='gray',marker='H')

x = [0,24]
y = [0,14]
plt.xlim([0,25])
plt.ylim([-1,15])
plt.xticks(np.arange(x[0], x[1]+1, 1.0))
plt.yticks(np.arange(y[0], y[1]+1, 1.0))
plt.grid(True,zorder=-1.0)
ax = plt.gca()
ax.set_axisbelow(True)
ax.set_aspect('equal')
plt.xlabel("k",labelpad = -12.0, loc='right')
plt.ylabel("n",labelpad = -12.0, loc='top',rotation=0)
plt.show()
#plt.savefig("OutFnHomology.svg")
