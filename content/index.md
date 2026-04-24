---
title: Category Start
---



A functor $F : \mathcal{C} \to \mathcal{D}$ between categories consists of the following data.

For each object $X \in \mathcal{C}$, an object $F(X) \in \mathcal{D}$, and for each morphism $f : X \to Y$, a morphism $F(f) : F(X) \to F(Y)$, such that:

$$F(\mathrm{id}_X) = \mathrm{id}_{F(X)}, \qquad F(g \circ f) = F(g) \circ F(f).$$

A natural transformation $\alpha : F \Rightarrow G$ is a family $\{\alpha_X : F(X) \to G(X)\}_{X \in \mathcal{C}}$ such that for all $f : X \to Y$,

$$G(f) \circ \alpha_X = \alpha_Y \circ F(f).$$