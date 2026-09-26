import sys, itertools
from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(xmax, kmax=None):
    """count tree length sets by order, and collect orders per k; DFS over the move tree."""
    Nn = defaultdict(int); Ak = defaultdict(set); examples = []
    def rec(L, o):          # L sorted-desc tuple, o = 1+sum(L) = order
        Nn[o] += 1
        Ak[len(L)].add(o)
        if o <= 40 and len(L) >= 3: examples.append((o, L))
        # superincreasing assertion
        for j in range(len(L)):
            assert L[j] >= 1 + sum(L[j+1:]), (o, L)
        for s in list(L) + [0]:
            L2 = tuple(sorted((set(L) - {s}) | {o}, reverse=True))
            if kmax is not None and len(L2) > kmax: continue
            o2 = 1 + sum(L2)
            if o2 <= xmax: rec(L2, o2)
    rec((), 1)
    return Nn, Ak, examples

def is_tree(n, S):
    par = list(range(n+1))
    def find(a):
        while par[a] != a: par[a] = par[par[a]]; a = par[a]
        return a
    e = 0
    for t in S:
        for i in range(1, n-t+1):
            a, b = find(i), find(i+t)
            if a == b: return False
            par[a] = b; e += 1
    return e == n-1

Nn, Ak, ex = dfs(220)
print("N(n), n=1..26:", [Nn[n] for n in range(1, 27)])

# brute-force completeness for small n
for n in range(2, 19):
    cnt = 0
    for k in range(1, 6):
        for S in itertools.combinations(range(1, n), k):
            if is_tree(n, set(S)): cnt += 1
    tag = "OK" if cnt == Nn[n] else "MISMATCH"
    if tag != "OK": print("  n=", n, "brute", cnt, "moves", Nn[n], tag)
print("brute-force completeness n=2..18: OK")

ex.sort()
print("smallest Toeplitz trees with >= 3 jumps (order, lengths, jumps):")
for o, L in ex[:5]:
    print("   n=%d  L=%s  S=%s" % (o, list(L), sorted(o-s for s in L)))

# thresholds, restricted DFS
N2, A2, _ = dfs(700, kmax=4)
o3, o4 = sorted(A2[3]), sorted(A2[4])
def thr(os):
    have = set(os); n = max(os)
    while n-1 in have: n -= 1
    return n
print("3-jump orders <= 40:", [n for n in o3 if n <= 40])
print("n_3 =", thr(o3), "| 25 present?", 25 in set(o3))
print("n_4 =", thr(o4), "| 67 present?", 67 in set(o4))

def phi(m):
    r, mm, p = m, m, 2
    while p*p <= mm:
        if mm % p == 0:
            while mm % p == 0: mm //= p
            r -= r // p
        p += 1
    if mm > 1: r -= r // mm
    return r
print("n : N(n) : N(n)-phi(n+1)/2+1  for n=2..18")
print("  ", [(n, Nn[n], Nn[n]-phi(n+1)//2+1) for n in range(2, 19)])
import json
json.dump({str(n): Nn[n] for n in range(1, 221)}, open("Nn.json", "w"))
print("saved N(n) up to 220")


# ---------------------------------------------------------------
# Figure: the census on base-2 logarithmic axes.
# This is the same figure, and the same code, as fig-census.pdf in the
# manuscript working folder, rendered here to PNG for the post.
# ---------------------------------------------------------------

from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.setrecursionlimit(100000)

XMAX = 260

def census(xmax):
    """N(n) for n <= xmax, by the move L -> (L\\{s}) u {ord L}, s in L u {0}."""
    Nn = defaultdict(int)
    def rec(L, o):
        Nn[o] += 1
        for s in list(L) + [0]:
            L2 = tuple(sorted((set(L) - {s}) | {o}, reverse=True))
            o2 = 1 + sum(L2)
            if o2 <= xmax:
                rec(L2, o2)
    rec((), 1)
    return Nn

N = census(XMAX)
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullFormatter

matplotlib.rcParams.update({
    "font.family": "serif", "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "cm", "font.size": 9,
    "pdf.fonttype": 42, "axes.linewidth": 0.7,
})

ns = np.array([n for n in sorted(N) if n >= 2]); vals = np.array([N[n] for n in ns])
run = np.maximum.accumulate(vals)

fig, ax = plt.subplots(figsize=(5.6, 3.3))
ax.set_xscale("log", base=2); ax.set_yscale("log", base=2)

xr = np.array([2.0, 300.0])
ax.plot(xr, xr, color="0.6", lw=0.8, ls=(0, (6, 4)), zorder=1)
ax.plot(xr, xr**2, color="0.6", lw=0.8, ls=(0, (2, 3)), zorder=1)
ax.text(300, 300, r"  $n$", color="0.45", fontsize=8, va="center")
ax.text(70, 70**2 * 0.7, r"$n^{2}$", color="0.45", fontsize=8)

ax.plot(ns, vals, lw=0.5, color="0.82", zorder=2)
ax.scatter(ns, vals, s=4.5, color="0.25", zorder=3, label=r"$N(n)$")
ax.plot(ns, run, lw=1.2, color="black", zorder=4, label=r"$\max_{m\leq n}N(m)$")

ax.annotate(r"$N(240)=1781$", xy=(240, 1781), xytext=(120, 5600), fontsize=7.5,
            arrowprops=dict(arrowstyle="->", lw=0.6))
ax.annotate(r"$N(60)=116$", xy=(60, 116), xytext=(20, 500), fontsize=7.5,
            arrowprops=dict(arrowstyle="->", lw=0.6))
ax.annotate(r"$N(61)=25$", xy=(61, 25), xytext=(95, 5.0), fontsize=7.5,
            arrowprops=dict(arrowstyle="->", lw=0.6))

ax.xaxis.set_major_locator(FixedLocator([2**k for k in range(1, 9)]))
ax.set_xticklabels([r"$2^{%d}$" % k for k in range(1, 9)])
ax.xaxis.set_minor_formatter(NullFormatter())
ax.yaxis.set_major_locator(FixedLocator([2**k for k in range(0, 15, 2)]))
ax.set_yticklabels([r"$2^{%d}$" % k for k in range(0, 15, 2)])
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_xlim(1.8, 330); ax.set_ylim(0.8, 2**14)
ax.grid(which="major", color="0.93", lw=0.6, zorder=0)
ax.set_xlabel(r"order $n$"); ax.set_ylabel(r"$N(n)$")
ax.legend(frameon=False, loc="upper left", fontsize=8, handlelength=1.6)
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.4)
fig.savefig(os.path.join(HERE, "toeplitz_tree_census.png"), dpi=300)
print("wrote fig-census.pdf")
