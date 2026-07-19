---
layout: post
title: "Clusters and trajectories, reconciled"
date: 2026-07-18 09:30:00 -0500
tags: [paper]
paper:
  title: "PAGA: graph abstraction reconciles clustering with trajectory inference through a topology preserving map of single cells"
  authors: "Wolf et al."
  venue: "Genome Biology, 2019"
  link: "https://doi.org/10.1186/s13059-019-1663-x"
  verdict: "The bridge between discrete clusters and continuous trajectories — a coarse map of how cell states connect, from the Scanpy authors."
---

**The problem.** Single-cell analysis splits into two worldviews: clustering says cells fall into discrete types; trajectory inference says they lie on continuous paths. Real tissue is both — distinct types *and* transitions between them. Forcing one view loses the other, and full trajectory methods can overreach on data that's mostly discrete.

**The idea.** PAGA (partition-based graph abstraction) computes a coarse-grained graph where nodes are clusters and edges are weighted by how strongly two clusters are connected in the single-cell neighbour graph. The result is a topology-preserving map: it shows which cell states are linked (and might transition) without committing to a false continuous ordering where none exists. You can then run pseudotime *within* the connected parts.

**Why it matters.** PAGA is a standard Scanpy step and a pragmatic resolution of a real tension — it lets me see global structure (which types relate) before deciding whether a continuous trajectory is even warranted. From the same group as Scanpy and scVelo, it reflects a consistent, sober design philosophy: give an honest coarse map rather than an over-confident fine one.

**Verdict.** Foundational for connecting clustering and trajectories, and a sensible default for surveying structure. Read it as the reconciliation of the field's two default lenses — discrete and continuous — into one graph.
