---
layout: post
title: "Tracing lineages through clusters"
date: 2026-07-18 07:15:00 -0500
tags: [paper]
paper:
 title: "Slingshot: cell lineage and pseudotime inference for single-cell transcriptomics"
 authors: "Street et al."
 venue: "BMC Genomics, 2018"
 link: "https://doi.org/10.1186/s12864-018-4772-0"
 verdict: "Trajectory inference that handles branching cleanly, pseudotime built on top of the clusters I already have."
---

**The problem.** Monocle showed you could order cells in pseudotime, but real differentiation *branches*: a progenitor becomes several fates. Inferring these branching lineages robustly, deciding where paths split and which cells belong to which branch, is harder than ordering a single line, and sensitive to noise in the embedding.

**The idea.** Slingshot works in two stages. First it identifies the global lineage structure by connecting clusters with a minimum spanning tree, using the clustering I've already done rather than starting from scratch. Then it fits smooth principal curves through the cells along each branch to assign continuous pseudotime. Separating "which lineages exist" from "where is each cell along them" makes the branching inference stable.

**Why it matters.** Slingshot is a standard trajectory tool and a clean example of building on existing structure, it takes clusters (Leiden, from day 10) and a low-dimensional embedding (UMAP, day 9) as input, rather than reinventing them. That composability is exactly how the single-cell toolkit fits together: each method consumes the previous one's output. It's the branching-aware successor to Monocle's linear idea.

**Verdict.** Foundational for trajectory inference and often a first choice for its robustness. It still needs a reasonable embedding and clustering to build on, so its output inherits those choices. Read it as the practical, branching-aware pseudotime method.
