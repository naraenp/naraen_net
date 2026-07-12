---
layout: post
title: "Finding communities in a graph"
date: 2026-07-12 10:20:00 -0500
tags: [paper]
paper:
  title: "Fast Unfolding of Communities in Large Networks (the Louvain algorithm)"
  authors: "Blondel, Guillaume, Lambiotte & Lefebvre"
  venue: "J. Statistical Mechanics, 2008"
  link: "https://doi.org/10.1088/1742-5468/2008/10/P10008"
  verdict: "The community-detection method that, years later, became how we cluster single cells — the 'graph' half of every UMAP-and-clusters figure."
---

**The problem.** Given a network — nodes and weighted edges — how do you find its communities: groups of nodes more connected to each other than to the rest? On large graphs this is computationally brutal, and most methods didn't scale.

**The idea.** Louvain optimizes *modularity* (how much denser a group's internal connections are than chance) with a greedy two-phase loop. First, move each node to the neighboring community that most increases modularity. Then collapse each community into a super-node and repeat on the smaller graph. Iterating this "unfolds" a hierarchy of communities in near-linear time, on graphs with millions of nodes.

**Why it matters.** This is the clustering engine under modern single-cell analysis, even though it was born in network science. Scanpy and Seurat build a k-nearest-neighbor graph of cells and run Louvain (or its successor Leiden) to call cell populations — the clusters I then annotate. Every single-cell figure I've read this fortnight has this algorithm somewhere in its methods. It's another case of a general-purpose idea becoming genomics infrastructure.

**Verdict.** Foundational and fast, which is exactly why it spread. Its known flaw — it can produce poorly-connected or fragmented communities — is what motivated Leiden, later in this reading list. Read it as the origin of graph-based clustering, then read Leiden to see the fix.
