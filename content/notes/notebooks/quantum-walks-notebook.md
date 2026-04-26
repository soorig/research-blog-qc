---
title: "Notebook: Quantum walks on graphs"
date: 2026-04-25
tags:
  - notebooks
  - quantum-walks
draft: false
---

The Jupyter notebook accompanying [[index|Continuous-time quantum walks on line graphs of tensor products]]. It contains every computation behind the figures in that post — drawing graphs from adjacency matrices, the tensor / Cartesian / line-graph constructions, CTQW simulation via $U(t) = e^{i t A}$, and the audience-friendly edge-wave figures for $L(G)$ and $L(G_1 \otimes G_2)$, plus a section verifying Godsil's closed form $\widehat{M}_\infty = \frac{1}{2n}(2J + I + T)$ for $L(P_n)$.

## Run it

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/soorig/research-blog-qc/blob/main/content/notes/notebooks/quantum_walks_on_graphs.ipynb)

One click — Colab boots a Python kernel with `numpy`, `scipy`, `matplotlib`, and `networkx` already installed. `Runtime → Run all` reproduces every figure end-to-end.

## Download or view statically

- [Download `quantum_walks_on_graphs.ipynb`](./quantum_walks_on_graphs.ipynb) — right-click → save as
- [View rendered on GitHub](https://github.com/soorig/research-blog-qc/blob/main/content/notes/notebooks/quantum_walks_on_graphs.ipynb)
- [Render via nbviewer](https://nbviewer.org/github/soorig/research-blog-qc/blob/main/content/notes/notebooks/quantum_walks_on_graphs.ipynb)

## What's inside

1. Drawing graphs from adjacency matrices.
2. Kronecker product, Cartesian product $A_1 \otimes I + I \otimes A_2$, and line graph $A_{L(G)} = B^\top B - 2I$.
3. CTQW evolution $|\psi(t)\rangle = e^{i t A}|\psi_0\rangle$ via direct `expm` and via cached spectral decomposition.
4. Probability snapshots, time–vertex heatmaps, and the average mixing matrix $\widehat{M}_\infty$.
5. Edge-wave figures for $L(G)$ — `initial.pdf`, `mixing.pdf`.
6. Edge-wave figures for $L(G_1 \otimes G_2)$ — `initial_tensor.pdf`, `mixing_tensor.pdf`. Three example pairs covering the three regimes of Weichsel's theorem.
7. Path graphs $P_n$: numerical verification of Godsil's formula and figures `path_initial.pdf`, `path_mixing.pdf`, `path_return.pdf` for arbitrary $n \geq 3$.

The notebook is self-contained — no `requirements.txt` needed, every dependency is part of a standard scientific Python install.