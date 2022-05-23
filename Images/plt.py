import numpy as np
import matplotlib.pyplot as plt

t = np.arange(1,26)
t2 = t.astype("float")
t2[0] = 5/3

vcd = 2 * t2 - 3
stb = 4/5 * t2 - 1

moritaC = np.array([(4,4),(6,8),(8,12)])
morita = np.array([(10,16),(12,20),(14,24)])
bartholdi = np.array([(7,8),(7,11)])

fig = plt.figure(figsize=2.5*np.array([3.74,2.4]))
plt.rcParams.update({
  "text.usetex": True,
  "text.latex.preamble": "\\usepackage{amsmath,amssymb}",
  "font.family": "serif",
  "font.serif": ["Computer Modern Roman"],
  "font.size": 16
})

#orange = [1.0,0.7,0.627,0.6]
orange = [1.0,0.627,0.0,0.45]
plt.fill_between(t2[:7],vcd[:7],stb[:7],color=orange,zorder=1.0)
plt.fill_between(t2[6:],vcd[6:],stb[6:],color=[0.7,0.7,0.7,0.3],zorder=1.0)

plt.plot(t2,vcd,":",c='black',zorder=2.0)
plt.plot(t2,stb,c='black',zorder=2.0)
plt.plot(t,np.zeros_like(t),"--",c='black',zorder=2.0)

plt.scatter(morita[:,0], morita[:,1], s=11**2, color=[0,0,0,0], marker='o', edgecolor='black', zorder=3.0)
plt.scatter(moritaC[:,0], moritaC[:,1], s=11**2, c='black', marker='o', edgecolor='black', zorder=3.0)
plt.scatter(bartholdi[:,0], bartholdi[:,1], s=13**2, c='gray', marker='v', zorder=3.0)

plt.text(13.25,1,"$H_0(\operatorname{Out}(F_n)) = \mathbb{Q}$",backgroundcolor="white",zorder=4.0)
plt.text(3.5,12,"$H_k(\operatorname{Out}(F_n)) = 0$\nabove vcd\n$k > 2n-3$",ha="center",backgroundcolor="white", zorder=4.0)
plt.text(15.5,6,"$H_k(\operatorname{Out}(F_n)) = 0$ below\nstable range $k \leq \\frac{4}{5} n - 1$",ha="center",backgroundcolor="white", zorder=4.0)

x = [1,20]
y = [0,17]
plt.xlim([x[0]-1,x[1]])
plt.ylim([y[0]-1,y[1]])
plt.xticks(np.arange(x[0], x[1]+1),np.arange(x[0], x[1]).tolist() + ['n'])
plt.yticks(np.arange(y[0], y[1]+1),np.arange(y[0], y[1]).tolist() + ['k'])
plt.grid(True,zorder=-1.0)
ax = plt.gca()
ax.set_axisbelow(True)
#ax.set_aspect('equal')
#plt.xlabel("n",labelpad = -14.5, loc='right')
#plt.ylabel("k",labelpad = -14.5, loc='top',rotation=0)
plt.savefig("OutFnHomology.pdf",bbox_inches='tight')

