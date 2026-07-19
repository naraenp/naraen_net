---
layout: post
title: "Ordering cells in time"
date: 2026-07-18 06:30:00 -0500
tags: [paper]
paper:
  title: "The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells (Monocle)"
  authors: "Trapnell et al."
  venue: "Nature Biotechnology, 2014"
  link: "https://doi.org/10.1038/nbt.2859"
  verdict: "The paper that turned a snapshot of cells into a trajectory — the origin of pseudotime, and the start of the single-cell dynamics thread."
---

**The problem.** A single-cell experiment is a snapshot: all cells captured at one instant. But biology is a process — cells differentiate, transition, progress. If a population is asynchronous, the snapshot secretly contains cells at every stage of a process. Can you recover the *order* — the trajectory — from a static sample?

**The idea.** Monocle assumes that cells caught mid-process trace a path through expression space. It embeds cells, builds a graph, and orders them along it to assign each a "pseudotime" — a position along the inferred trajectory rather than real clock time. Genes that change along pseudotime reveal the regulators of the transition, turning one timepoint into a reconstructed movie of cell fate.

**Why it matters.** This launched trajectory inference, a pillar of single-cell analysis and directly relevant to the developmental and tissue questions the STU-adjacent spatial work cares about. It's also a beautiful idea: heterogeneity, usually a nuisance, becomes the signal. Everything later this day (Slingshot, RNA velocity, PAGA) refines or challenges the pseudotime concept Monocle introduced.

**Verdict.** Foundational — pseudotime is now standard vocabulary. Its assumptions (a continuous process, a sensible embedding) don't fit every dataset, and later methods handle branching and dynamics better. Read it as the conceptual seed of single-cell trajectories.
