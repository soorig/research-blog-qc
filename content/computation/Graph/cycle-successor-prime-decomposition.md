---
title: "Cycle Successors and a Prime-Decomposition Theorem for Graph Automorphisms"
date: 2026-04-26
tags:
  - graph-theory
  - automorphism-group
  - permutation-group
  - cycle-decomposition
  - research-note
draft: false
---

# Cycle Successors and a Prime-Decomposition Theorem for Graph Automorphisms

This note introduces a relation $\succ$ on the cycles of a graph automorphism group and proves a number-theoretic constraint: **if $\sigma \succ \tau$, then their lengths share a common factor**. The relation captures forced co-occurrence of cycles within individual automorphisms, and its arithmetic behavior opens a path toward a prime-decomposition view of automorphism structure.

## Motivation

Standard tools — the cycle index, Pólya enumeration, the Rota–Smith period lattice — all collapse cycle decomposition data to *cycle types* (multisets of lengths). They forget which specific subsets of $V(F)$ realized those lengths. The relation introduced below operates one level finer: it tracks which cycles must appear together in a single group element.

The surprising part is that a number-theoretic constraint emerges from this finer view, even though the definition is purely combinatorial.

## Definitions

### Cycle decomposition

Let $F$ be a simple graph and $\mathrm{Aut}(F) \le S_n$ its automorphism group, where $n = |V(F)|$. For $f \in \mathrm{Aut}(F)$, write $\mathrm{cyc}(f)$ for the set of disjoint cycles in the cycle decomposition of $f$. For a cycle $\sigma \in \mathrm{cyc}(f)$, write $[\sigma]$ for the underlying set of vertices,
$$[(v_1\, v_2\, \cdots\, v_p)] = \{v_1, v_2, \ldots, v_p\},$$
and define the cardinality of $\sigma$ as $|\sigma| := |[\sigma]|$.

### Cycle successor

The cycle **successor relation** $\succ$ on $\mathrm{Aut}(F)$ is defined by
$$\sigma \succ \tau \iff \forall f \in \mathrm{Aut}(F) \colon\ \sigma \in \mathrm{cyc}(f) \implies \tau \in \mathrm{cyc}(f).$$

We say $\tau$ is a **successor** of $\sigma$ if there is a chain $\sigma \succ \cdots \succ \tau$.

### Unrelated cycles

A cycle $\sigma \in \mathrm{Perm}(V(F))$ is **unrelated** if there is no $\epsilon \neq \sigma$ with $\sigma \succ \epsilon$.

## The Prime-Decomposition Theorem

> **Theorem.** *Let $\sigma \succ \tau$. Then $\gcd(|\sigma|, |\tau|) > 1$.*

**Proof.** Suppose for contradiction that $\sigma \succ \tau$ and $\gcd(|\sigma|, |\tau|) = 1$. Let $a = |\sigma|$ and $b = |\tau|$. By Bézout, there exist integers $x, y$ with $ax + by = 1$.

Take any $f \in \mathrm{Aut}(F)$ with $\sigma \in \mathrm{cyc}(f)$. Then $\tau \in \mathrm{cyc}(f)$ by the definition of $\succ$.

Consider the power $f^{1-by} = f^{ax}$. Since $\sigma$ has length $a$, the cycle $\sigma$ becomes trivial in $f^{ax}$ — that is, $\sigma \notin \mathrm{cyc}(f^{ax})$. On the other hand, since $1 - by \equiv 1 \pmod{b}$, the cycle $\tau$ persists in $f^{1-by}$, so $\tau \in \mathrm{cyc}(f^{1-by})$.

This contradicts $\sigma \succ \tau$: we have a power of $f$ in which $\tau$ appears but $\sigma$ does not, and powers of automorphisms are automorphisms. $\blacksquare$

The theorem says that $\succ$-edges respect divisibility: coprime-length cycles cannot have a $\succ$-relationship.

## A Proposition on Unrelated Cycles

> **Proposition.** *Let $\sigma$ be an unrelated cycle of length $p$. Then:*
> 1. *If $|\sigma|$ is composite, then $\sigma^k$ is unrelated for $\gcd(k, p) = 1$.*
> 2. *If $|\sigma|$ is prime, then $\sigma^k$ is unrelated for all $k \notin p\mathbb{Z}$.*
> 3. *If $N^\tau \subseteq N^\sigma$, then $\tau = \sigma$.*

This proposition begins to organize unrelated cycles into orbits under the power operation, controlled by the prime structure of the length.

## What This Buys

A few consequences worth noting.

**Cycle-length compatibility is necessary for $\succ$.** In a graph where all realized cycle lengths in $\mathrm{Aut}(F)$ are pairwise coprime, $\succ$ degenerates: only reflexive relations remain. Symmetric graphs with many compatible cycle lengths have rich $\succ$-structure.

**Prime decomposition becomes the natural index.** The relation $\succ$ respects divisibility, so it interacts naturally with the divisor lattice. Define $\succ_p$ as $\succ$ restricted to cycles whose length is divisible by the prime $p$. The theorem above implies
$$\succ = \bigcup_p \succ_p,$$
giving a prime-by-prime decomposition of the relation.

**Distance from the standard frameworks.** The relation $\succ$ does not appear in the period lattice of Rota–Smith (1977) or in the more recent $G$-invariant partition framework of Anagnostopoulou-Merkouri–Bailey–Cameron (2024). Both of those collapse to invariant-partition data, which averages out the per-element cycle structure that $\succ$ depends on.

## Open Directions

These are questions I plan to develop in coming posts.

1. **Sharpness.** Is the coprime-threshold tight? That is, when $\gcd(|\sigma|, |\tau|) > 1$, are there obstructions beyond divisibility?

2. **Converse on special classes.** Is there a class of graphs (Cayley graphs of abelian groups? distance-regular graphs?) where the converse holds — every pair of cycles with non-coprime lengths is $\succ$-related?

3. **The $\succ$-poset as a graph invariant.** Two graphs with different edge sets can have the same $\mathrm{Aut}$-action on vertices (and hence the same $\succ$-poset). What additional structure on $\succ$ distinguishes them? The candidate is a graph-aware refinement using adjacency.

4. **Rank and cycle-length profile.** Express the maximum chain length of the $\succ$-poset in terms of the prime factorization profile of cycle lengths realized in $\mathrm{Aut}(F)$.

## References

- G. Pólya, "Kombinatorische Anzahlbestimmungen für Gruppen, Graphen und chemische Verbindungen," *Acta Mathematica* **68** (1937), 145–254.
- G.-C. Rota and D. A. Smith, "Enumeration Under Group Action," *Annali della Scuola Normale Superiore di Pisa* **IV.4** (1977), 637–646. [[numdam](https://www.numdam.org/item/ASNSP_1977_4_4_4_637_0.pdf)]
- M. Anagnostopoulou-Merkouri, R. A. Bailey, P. J. Cameron, "Permutation groups, partition lattices and block structures," arXiv:2409.10461 (2024).
- C. Godsil and G. Royle, *Algebraic Graph Theory*, Springer GTM 207, 2001.

---

*This is a research note. Comments, corrections, and counterexamples are welcome.*
