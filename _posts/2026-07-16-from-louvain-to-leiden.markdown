---
layout: post
title: "From Louvain to Leiden"
date: 2026-07-16 09:00:00 -0500
tags: [paper]
paper:
  title: "From Louvain to Leiden: guaranteeing well-connected communities"
  authors: "Traag, Waltman & van Eck"
  venue: "Scientific Reports, 2019"
  link: "https://doi.org/10.1038/s41598-019-41695-z"
  verdict: "The fix for a subtle bug in the clustering algorithm behind every single-cell paper — including one I've almost certainly run."
---

**The problem.** Louvain (day 6) is the community-detection method underneath most single-cell clustering. But it has a hidden flaw: it can produce communities that are internally *disconnected* — a "cluster" that isn't actually one connected group. In single-cell terms, a cell type could be split or mixed in ways the algorithm silently permits, and nobody notices because the modularity score still looks fine.

**The idea.** Leiden refines Louvain with a guarantee: it adds a refinement phase that ensures every community it returns is well-connected, and it converges faster to better partitions. Same modularity-optimisation spirit, but with the connectivity defect fixed and improved efficiency on large graphs.

**Why it matters.** This is a quietly important correction to a tool I use without thinking — Scanpy switched its default clustering from Louvain to Leiden, so my single-cell clusters are probably Leiden clusters. Reading it is a reminder that "standard method" doesn't mean "flawless," and that the defaults in my toolkit encode specific, improvable algorithmic choices. It directly upgrades the day-6 Louvain paper.

**Verdict.** Foundational as the current default for graph clustering in single-cell. A focused, well-motivated improvement rather than a new paradigm — which is exactly why it matters. Read it right after Louvain to see the bug and its fix.
