import os
HERE = os.path.dirname(os.path.abspath(__file__))
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def one_point_union(a, b):
    n = a + b - 1; A = np.zeros((n,n))
    for C in (list(range(a)), [0]+list(range(a,n))):
        for x in range(len(C)):
            for y in range(x+1, len(C)): A[C[x],C[y]] = A[C[y],C[x]] = 1
    return A

def glued_by_path(n, k):
    N = 2*n + (k-1); A = np.zeros((N,N))
    for C in (list(range(n)), list(range(n,2*n))):
        for x in range(len(C)):
            for y in range(x+1, len(C)): A[C[x],C[y]] = A[C[y],C[x]] = 1
    chain = [0] + list(range(2*n, 2*n+k-1)) + [n]
    for x,y in zip(chain, chain[1:]): A[x,y] = A[y,x] = 1
    return A

def amm_diag(A, q, tol=1e-8):
    w, V = np.linalg.eigh(A); tot = 0.0; i = 0
    while i < len(w):
        j = i
        while j+1 < len(w) and w[j+1]-w[i] < tol: j += 1
        tot += (V[q, i:j+1]**2).sum()**2; i = j+1
    return tot

def ret(A, q, ts):
    w, V = np.linalg.eigh(A); c = V[q]**2
    keep = c > 1e-12; w, c = w[keep], c[keep]
    return np.abs((c[None,:]*np.exp(1j*np.outer(ts, w))).sum(axis=1))**2

def ret_min(A, q, T=3000.0, N=600000, chunk=20000):
    w, V = np.linalg.eigh(A); c = V[q]**2
    keep = c > 1e-12; w, c = w[keep], c[keep]
    grid = np.linspace(0, T, N); best = 1.0
    for s in range(0, N, chunk):
        ts = grid[s:s+chunk]
        best = min(best, np.abs((c[None,:]*np.exp(1j*np.outer(ts, w))).sum(axis=1)).min()**2)
    return best

# ---------------- Figure 1: the two constructions ----------------
def ring(cx, cy, m, r, start=0.0):
    ang = np.linspace(0, 2*np.pi, m, endpoint=False) + start
    return np.stack([cx + r*np.cos(ang), cy + r*np.sin(ang)], axis=1)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.0))
RED, BLU, GRY = "#c0392b", "#3b6ea5", "#666666"

# left: one-point union K_5 v_q K_8, both drawn as regular polygons with q as a vertex
ax = axes[0]
qp = np.array([0.0, 0.0])
ra, rb = 1.30, 1.85
La = ring(-ra, 0, 5, ra, 0.0)      # vertex 0 sits exactly at the origin
Lb = ring( rb, 0, 8, rb, np.pi)    # vertex 0 sits exactly at the origin
for L, col in ((La, RED), (Lb, BLU)):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            ax.plot(*zip(L[i], L[j]), color="#cccccc", lw=0.9, zorder=1)
    ax.scatter(L[1:,0], L[1:,1], s=80, color=col, zorder=3)
ax.scatter([0],[0], s=150, color="black", zorder=4)
ax.text(0, 0.26, r"$q$", ha="center", fontsize=13)
ax.text(-ra, -2.20, r"$K_a$", ha="center", fontsize=13, color=RED)
ax.text( rb, -2.55, r"$K_b$", ha="center", fontsize=13, color=BLU)
ax.set_title(r"$G_{a,b}=K_a \vee_q K_b$, one shared vertex", fontsize=11.5, pad=14)

# right: G_{n,k}, two K_5 joined by a path with k=3 edges
ax2 = axes[1]
n, k = 5, 3
Pa = ring(-2.5, 0, n, 1.15, 0.0); Pb = ring(2.5, 0, n, 1.15, np.pi)
w0, wk = Pa[0], Pb[0]
mids = np.stack([np.linspace(w0[0], wk[0], k+1)[1:-1], np.zeros(k-1)], axis=1)
for L, col in ((Pa, RED), (Pb, BLU)):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            ax2.plot(*zip(L[i], L[j]), color="#cccccc", lw=0.9, zorder=1)
    ax2.scatter(L[1:,0], L[1:,1], s=80, color=col, zorder=3)
chain = np.vstack([w0, mids, wk])
for x, y in zip(chain, chain[1:]):
    ax2.plot(*zip(x, y), color=GRY, lw=1.6, zorder=2)
ax2.scatter(mids[:,0], mids[:,1], s=70, color=GRY, zorder=3)
ax2.scatter([wk[0]],[wk[1]], s=80, color=BLU, zorder=3)
ax2.scatter([w0[0]],[w0[1]], s=150, color="black", zorder=4)
ax2.text(w0[0]-0.15, w0[1]-0.50, r"$q=w_0$", ha="center", fontsize=12)
ax2.text(0, 0.35, r"$k$ edges", ha="center", fontsize=11, color=GRY)
ax2.text(-2.5, -1.85, r"$K_n$", ha="center", fontsize=13, color=RED)
ax2.text( 2.5, -1.85, r"$K_n$", ha="center", fontsize=13, color=BLU)
ax2.set_title(r"$G_{n,k}$, two cliques joined by a path", fontsize=11.5, pad=14)

for a_ in axes:
    a_.set_aspect("equal"); a_.axis("off"); a_.set_ylim(-2.9, 2.2)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "gluing_schematic.png"), dpi=170)

# ---------------- Figure 2: asymmetric limits ----------------
bs = [2,3,4,6,8,12,18,26,40,60,90,140,220,340]
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.2))
cols = {3:"#c0392b", 5:"#3b6ea5", 9:"#2e7d5b"}
for a in (3,5,9):
    xs = [b for b in bs if b >= a]
    m = [amm_diag(one_point_union(a,b), 0) for b in xs]
    r = [ret_min(one_point_union(a,b), 0, T=800.0, N=200000) for b in xs]
    axes[0].plot(xs, m, "o-", ms=4, color=cols[a], label=fr"$a={a}$")
    axes[0].axhline((a+1)/(a+3), color=cols[a], ls="--", lw=1.1, alpha=.7)
    axes[1].plot(xs, r, "o-", ms=4, color=cols[a], label=fr"$a={a}$")
    axes[1].axhline((a-1)/(a+3), color=cols[a], ls="--", lw=1.1, alpha=.7)
axes[0].set_ylabel(r"$\widehat{M}_{q,q}$")
axes[0].set_title(r"average mixing at the shared vertex", fontsize=11.5)
axes[0].axhline(1/3, color="#999999", ls=":", lw=1.3)
axes[0].text(340, 1/3+0.012, r"$1/3$ bound", ha="right", fontsize=9, color="#777777")
axes[1].set_ylabel(r"$\inf_t\,|U(t)_{q,q}|^2$")
axes[1].set_title(r"worst-case return probability", fontsize=11.5)
for ax_, lim in zip(axes, [r"$(a+1)/(a+3)$", r"$(a-1)/(a+3)$"]):
    ax_.set_xscale("log"); ax_.set_xlabel(r"$b$, size of the larger clique")
    ax_.legend(frameon=False, loc="lower right", fontsize=9.5, title=f"dashed: {lim}",
               title_fontsize=9)
    ax_.set_ylim(0, 1)
    for s in ("top","right"): ax_.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "asymmetric_limits.png"), dpi=170)

# ---------------- Figure 3: one bridge destroys sedentariness ----------------
ts = np.linspace(0, 40, 16001)
A_union = one_point_union(8, 8)
A_k1 = glued_by_path(8, 1)
p_u, p_1 = ret(A_union, 0, ts), ret(A_k1, 0, ts)
floor_u = ret_min(A_union, 0, T=1500.0, N=400000)
fig, ax = plt.subplots(figsize=(10, 4.4))
ax.plot(ts, p_1, lw=1.1, color="#aaaaaa", label=r"$G_{8,1}$, one bridge edge")
ax.plot(ts, p_u, lw=1.4, color="#c0392b", label=r"$G_{8,8}=K_8 \vee_q K_8$, shared vertex")
ax.axhline(floor_u, color="#c0392b", ls=":", lw=1.3)
ax.text(40.3, floor_u, r"$\inf_t \approx %.2f$" % floor_u, color="#c0392b", va="center", fontsize=9)
ax.set_xlabel(r"$t$"); ax.set_ylabel(r"$|U(t)_{q,q}|^2$")
ax.set_xlim(0, 40); ax.set_ylim(-0.02, 1.06)
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2, fontsize=10)
for s in ("top","right"): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "bridge_destroys.png"), dpi=165)
print("union floor", floor_u, " k=1 floor", ret_min(A_k1, 0, T=1500.0, N=400000))
print("Mhat union(8,8)", amm_diag(A_union,0), " formula", 64/(64+32-4))
print("Mhat G_{n,1} n=8", amm_diag(A_k1,0))
