---
layout: post
title: "The embedding that replaced t-SNE"
date: 2026-07-15 03:50:00 -0500
tags: [paper]
paper:
 title: "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction"
 authors: "McInnes, Healy & Melville"
 venue: "arXiv, 2018"
 link: "https://arxiv.org/abs/1802.03426"
 verdict: "The default single-cell embedding today, faster than t-SNE, better at global structure, and the plot behind most scRNA-seq figures I read."
---

**The problem.** t-SNE (day 6) gave the field a way to see high-dimensional single-cell data, but at a cost: it's slow on large datasets, scales awkwardly to millions of cells, and distorts global structure, distances between clusters aren't meaningful. As cell counts exploded (see: droplet single-cell), that became limiting.

**The idea.** UMAP builds a fuzzy topological representation of the data, a weighted neighbour graph grounded in manifold theory, then optimises a low-dimensional layout to match it. In practice it runs much faster than t-SNE, handles large datasets gracefully, and preserves more of the global arrangement while keeping local neighbourhoods intact. The math is heavier; the payoff is speed and better structure.

**Why it matters.** UMAP is now *the* standard embedding in Scanpy and single-cell workflows, the plot I see in nearly every scRNA-seq paper. Reading it after t-SNE completes the visualisation arc: same goal (see the neighbourhoods), better engineering. And it carries t-SNE's caution forward, it's still a projection, so over-reading exact distances and cluster sizes remains a trap.

**Verdict.** Foundational for modern single-cell visualisation and dimensionality reduction, and the natural successor the t-SNE post pointed toward. Read it for the neighbour-graph framing, and keep treating the picture as a lens, not a measurement.
