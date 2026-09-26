import os
HERE = os.path.dirname(os.path.abspath(__file__))
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

Ns = [11, 12, 15, 18]
labels = {11: r"$N=11$   ($P_{10}$, $N$ prime)",
          12: r"$N=12$   ($P_{11}$, $12\mid N$)",
          15: r"$N=15$   ($P_{14}$)",
          18: r"$N=18$   ($P_{17}$, $N\equiv 6 \; (12)$)"}
cols = {11:"#2e7d5b", 12:"#c0392b", 15:"#3b6ea5", 18:"#7d5ba6"}

fig, ax = plt.subplots(figsize=(10,3.8))
for i,N in enumerate(Ns):
    th = 2*np.cos(np.pi*np.arange(1,N)/N)
    y = len(Ns)-1-i
    ax.hlines(y, -2.15, 2.15, color="#dddddd", lw=1, zorder=0)
    ax.plot(th, np.full_like(th, y), "o", ms=7, color=cols[N], zorder=2)
    ax.text(-2.3, y, labels[N], ha="right", va="center", fontsize=10)

for x, lab in [(0,"0"), (1,"1"), (-1,"-1"), (np.sqrt(2), r"$\sqrt{2}$"),
               (-np.sqrt(2), r"$-\sqrt{2}$"), (np.sqrt(3), r"$\sqrt{3}$"), (-np.sqrt(3), r"$-\sqrt{3}$")]:
    ax.vlines(x, -0.35, 3.35, color="#c0392b", lw=1.0, ls=":", alpha=.55, zorder=1)
    ax.text(x, 3.42, lab, ha="center", va="bottom", fontsize=9, color="#c0392b")

ax.set_xlim(-3.5, 2.35); ax.set_ylim(-0.6, 3.95)
ax.set_yticks([]); ax.set_xticks([-2,-1,0,1,2])
ax.set_xlabel(r"eigenvalues $2\cos(k\pi/N)$ of the path $P_{N-1}$")
for s in ("top","right","left"): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "spectra_paths.png"), dpi=170)
print("N=12 spectrum:", np.round(2*np.cos(np.pi*np.arange(1,12)/12),4))
