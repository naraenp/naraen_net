---
layout: post
title: "Seeing high-dimensional data"
date: 2026-07-12 12:00:00 -0500
tags: [paper]
paper:
  title: "Visualizing Data using t-SNE"
  authors: "van der Maaten & Hinton"
  venue: "J. Machine Learning Research, 2008"
  link: "https://www.jmlr.org/papers/v9/vandermaaten08a.html"
  verdict: "The method behind a decade of scatter plots — how you squash 20,000 gene dimensions onto a page and still see structure."
---

**The problem.** A single cell is a point in tens of thousands of dimensions (one per gene). You cannot see that, and naive projections (like PCA) preserve global variance but smear the local neighborhoods — the very cell-to-cell similarities you care about. How do you get a 2-D picture that keeps *who is near whom*?

**The idea.** t-SNE converts pairwise distances into probabilities: for each point, which others are likely its neighbors. It then arranges points in 2-D so that a similar neighbor-probability structure holds, minimizing the divergence between the high-D and low-D neighbor distributions. Using a heavy-tailed (Student-t) distribution in the low-D space prevents crowding, letting distinct clusters separate cleanly. The result preserves local structure strikingly well.

**Why it matters.** For years, *the* single-cell figure was a t-SNE plot colored by cluster — it's how the field learned to look at its data, and it's paired with the Louvain clustering from earlier today. It's also a cautionary tool: distances *between* clusters and their sizes aren't meaningful, a trap I've learned to respect. Reading the original clarifies exactly what the plot does and doesn't say.

**Verdict.** Foundational for visualization, later largely supplanted by UMAP (coming up in the reading list) for speed and better global structure. Its danger is over-interpretation — it's a lens, not a measurement. Read it to understand what every embedding plot is actually optimizing.
