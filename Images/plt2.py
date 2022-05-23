import numpy as np
import matplotlib.pyplot as plt

t = np.arange(1,26)

vcd = 1/2 * t + 1
stb = 5/4 * (t+1)

moritaC = np.array([(4,4),(8,6),(12,8)])
morita = np.array([(16,10),(20,12),(24,14)])
bartholdi = np.array([(8,7),(11,7)])
fig = plt.figure(figsize=2.5*np.array([3.74,2.4]))
plt.rcParams.update({
  "text.usetex": True,
  "text.latex.preamble": "\\usepackage{amsmath,amssymb}",
  "font.family": "serif",
  "font.serif": ["Computer Modern Roman"],
  "font.size": 16
})

orange = [1.0,0.7,0.627,0.5]
plt.fill_between([1,23/5,11],[2.5,7,7],[2,3.8,7],color=orange,zorder=1.0)
plt.fill_between([23/5,11,25],[7,15,32.5],[7,7,14],color=[0.7,0.7,0.7,0.3],zorder=1.0)
plt.plot(t,vcd,c='black',zorder=2.0)
plt.plot(t,stb,":",c='black',zorder=2.0)
plt.plot(np.zeros_like(t),t,"--",c='black',zorder=2.0)
plt.scatter(morita[:,0], morita[:,1], s=11**2, color=[0,0,0,0], marker='s', edgecolor='black', zorder=3.0)
plt.scatter(moritaC[:,0], moritaC[:,1], s=11**2, c='black', marker='s', edgecolor='black', zorder=3.0)
plt.scatter(bartholdi[:,0], bartholdi[:,1], s=17**2, c='gray', marker='H', zorder=3.0)
plt.text(0.5,14,"$H_0(\operatorname{Out}(F_n)) = \mathbb{Q}$",backgroundcolor="white",zorder=4.0)
plt.text(18,6,"$H_k(\operatorname{Out}(F_n)) = 0$ above vcd\n$k > 2n-3$",ha="center",backgroundcolor="white", zorder=4.0)
plt.text(3.5,10,"$H_k(\operatorname{Out}(F_n)) = 0$\nin stable range\n$n \geq \\frac{5 (k+1)}{4}$",ha="center",backgroundcolor="white", zorder=0.9)

x = [0,24]
y = [1,14]
plt.xlim([-1,25])
plt.ylim([0,15])
plt.xticks(np.arange(x[0], x[1]+1, 1.0))
plt.yticks(np.arange(y[0], y[1]+1, 1.0))
plt.grid(True,zorder=-1.0)
ax = plt.gca()
ax.set_axisbelow(True)
ax.set_aspect('equal')
plt.xlabel("k",labelpad = -14.5, loc='right')
plt.ylabel("n",labelpad = -14.5, loc='top',rotation=0)
plt.savefig("OutFnHomology.pdf",bbox_inches='tight')

