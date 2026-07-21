---
layout: post
title: "Direction for the trajectory"
date: 2026-07-21 09:15:00 -0500
tags: [paper]
paper:
  title: "CellRank for directed single-cell fate mapping"
  authors: "Lange et al."
  venue: "Nature Methods, 2022"
  link: "https://doi.org/10.1038/s41592-021-01346-6"
  verdict: "Marries trajectory inference with RNA velocity's arrow of time to map fates when you don't know the direction in advance — a robust, uncertainty-aware Markov model of where cells are going."
---

**The problem.** Trajectory methods need you to tell them the direction (a start cell); RNA velocity gives direction but is noisy and can point wrong in messier systems. Regeneration, reprogramming, and disease are exactly the cases where you *don't* know the direction beforehand and the velocity signal is unreliable. You want the robustness of trajectories with the directional information of velocity, plus honesty about uncertainty.

**The idea.** CellRank builds a Markov transition matrix over cells that combines a similarity kernel (trajectory-style) with a velocity kernel (directional), explicitly propagating the uncertainty in velocity vectors rather than trusting them blindly. From this it identifies initial, intermediate, and terminal states automatically, computes fate probabilities toward each terminal population, and traces smooth gene-expression trends along lineages — data-view agnostic, so it works with or without velocity.

**Why it matters.** This unifies two threads from the single-cell day — pseudotime (Monocle, Palantir) and RNA velocity (scVelo) — into one directed framework, and its uncertainty handling is what makes it hold up on real, noisy data. For studying how cells transition in disease, which is close to translational questions the STU engages, robust directed fate mapping is the tool that turns dynamics into testable structure.

**Verdict.** A leading fate-mapping method; it inherits whatever biases the input velocity or kernel carry, and terminal-state calls still need biological sanity checks. Read it as trajectory inference that finally knows which way time runs.
