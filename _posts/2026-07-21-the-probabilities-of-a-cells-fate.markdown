---
layout: post
title: "The probabilities of a cell's fate"
date: 2026-07-21 08:30:00 -0500
tags: [paper]
paper:
 title: "Characterization of cell fate probabilities in single-cell data with Palantir"
 authors: "Setty et al."
 venue: "Nature Biotechnology, 2019"
 link: "https://doi.org/10.1038/s41587-019-0068-4"
 verdict: "Treats differentiation as a stochastic process and assigns each cell a probability of reaching each terminal fate, plus an entropy that measures how committed it still is."
---

**The problem.** Trajectory methods (Monocle, Slingshot, PAGA from the single-cell day) order cells along lineages, but a progenitor doesn't follow one predetermined path, it faces branching choices with uncertain outcomes. What you want isn't just a position on a tree; it's, for a given cell, the probability it ends up in each terminal state, and a measure of how much freedom it retains.

**The idea.** Palantir models differentiation as a Markov (stochastic) process over a nearest-neighbour graph of cells. From a chosen start cell it computes a high-resolution pseudotime and the absorption probabilities into each terminal state, each cell's likelihood of each fate. It also derives a differentiation-entropy per cell: high early when many fates remain open, falling as the cell commits. Applied to human bone-marrow data, it recovers hematopoietic branch points.

**Why it matters.** This reframes trajectories probabilistically, which is the more honest picture of fate decisions and connects to the stochastic-process thread that CellRank will push further. Entropy-as-plasticity is a genuinely useful readout. For developmental or regenerative questions, and tumor plasticity, near the STU's interests, quantifying commitment beats a single ordering.

**Verdict.** A widely-used, elegant fate-probability method; results depend on start-cell choice and graph construction, and it assumes the sampled cells capture the continuum. Read it as differentiation told in probabilities rather than a fixed path.
