import os
HERE = os.path.dirname(os.path.abspath(__file__))
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def path_adj(n):
    A = np.zeros((n,n))
    for i in range(n-1):
        A[i,i+1]=A[i+1,i]=1.0
    return A

def avg_mixing(A):
    w,V = np.linalg.eigh(A)
    # eigenvalues of a path are simple
    P = V**2                      # P[u,r] = v_r(u)^2
    return P @ P.T                # sum_r v_r(u)^2 v_r(v)^2

n = 11
M = avg_mixing(path_adj(n))
print("row sums (should be 1):", np.allclose(M.sum(axis=1), 1.0))

fig, ax = plt.subplots(1,2, figsize=(11,4.2))
im = ax[0].imshow(M, cmap="magma", vmin=0)
ax[0].set_title(r"$\widehat{M}$ for $P_{11}$")
ax[0].set_xlabel("vertex $v$"); ax[0].set_ylabel("vertex $u$")
ax[0].set_xticks(range(0,n,2)); ax[0].set_xticklabels(range(1,n+1,2))
ax[0].set_yticks(range(0,n,2)); ax[0].set_yticklabels(range(1,n+1,2))
fig.colorbar(im, ax=ax[0], fraction=0.046)

ax[1].bar(np.arange(1,n+1), M[0], color="#3b6ea5", label=r"$\widehat{M}(1,\cdot)$")
ax[1].axhline(1.0/n, color="#c0392b", ls="--", lw=1.8, label=r"uniform $1/11$")
ax[1].set_xlabel("vertex $v$"); ax[1].set_ylabel("probability")
ax[1].set_title(r"row at the end vertex of $P_{11}$")
ax[1].legend(frameon=False)
for s in ("top","right"): ax[1].spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "avg_mixing_p11.png"), dpi=170, transparent=False)
print("max dev from uniform, row 1:", np.abs(M[0]-1/n).max())
print("diag:", np.round(np.diag(M),4))
