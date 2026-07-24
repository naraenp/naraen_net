---
layout: post
title: "The arrow of a cell"
date: 2026-07-18 08:00:00 -0500
tags: [paper]
paper:
 title: "RNA velocity of single cells"
 authors: "La Manno et al."
 venue: "Nature, 2018"
 link: "https://doi.org/10.1038/s41586-018-0414-6"
 verdict: "The trick that gives each cell a direction, not just a position, future state read from the ratio of unspliced to spliced mRNA."
---

**The problem.** Pseudotime (Monocle, Slingshot) orders cells along a trajectory, but the *direction* of travel is assumed or inferred from side information, the data itself doesn't say which end is "before." Can a single snapshot tell you not just where a cell sits, but which way it's heading?

**The idea.** RNA velocity exploits a biological clock hidden in the data: reads spanning introns mark *unspliced* (newly transcribed) pre-mRNA, while spliced reads mark mature mRNA. When a gene is being switched on, unspliced runs ahead of spliced; when switched off, it lags. Modelling that ratio per gene yields a velocity vector predicting each cell's near-future state, an arrow, not just a dot.

**Why it matters.** This is a genuinely clever use of information already sitting in standard RNA-seq reads (the same intron-spanning reads STAR handles). It gives trajectories a built-in arrow of time, resolving Monocle's directionality ambiguity from first principles. It also reframes what a single-cell snapshot contains, dynamics, if you know where to look. scVelo (next) generalises it.

**Verdict.** Foundational and influential, if not infallible, the underlying kinetic assumptions can mislead, which later work (and scVelo's dynamical model) addresses. Read it for the core insight: splicing state encodes direction, and it was in the data all along.
