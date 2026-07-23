---
layout: post
title: "Communication by optimal transport"
date: 2026-07-23 07:00:00 -0500
tags: [paper]
paper:
  title: "Screening cell–cell communication in spatial transcriptomics via collective optimal transport (COMMOT)"
  authors: "Cang et al."
  venue: "Nature Methods, 2023"
  link: "https://doi.org/10.1038/s41592-022-01728-4"
  verdict: "Cell–cell communication done in space and with competition — optimal transport matches ligand supply to receptor demand across real distances, respecting that signals are finite and contested."
---

**The problem.** Communication tools built for dissociated single cells ignore two facts that spatial data restores: signaling is local (a ligand reaches nearby cells, not the whole tissue), and it's competitive (a limited pool of ligand is shared among competing receptors). Simply applying non-spatial methods to spatial data, cell by cell, misses both the geometry and the competition.

**The idea.** COMMOT casts communication as a *collective optimal transport* problem: it moves ligand "mass" to receptor "mass" across cells, constrained by spatial distance and by the competition among multiple ligand and receptor species for the same partners. The transport plan yields spatially-resolved signaling between cells, and downstream machine-learning models infer signaling directionality and the genes each signal regulates — communication as a physically-constrained allocation, not independent pairwise scores.

**Why it matters.** This unites two threads I've been reading: cell–cell communication (CellChat, LIANA) and the spatial/STU track. Optimal transport — the same mathematical tool behind some trajectory and integration methods — arriving in spatial signaling is notable. For the STU, where the question is literally which cells signal to their neighbours in a tissue, a method that honours distance and competition is far closer to the biology than expression co-occurrence.

**Verdict.** A strong spatially-aware CCC method; results depend on the ligand–receptor database and distance assumptions, and optimal transport is computationally heavier. Read it as cell–cell communication that finally accounts for where cells are and what they compete for.
