---
layout: post
title: "A clock built from three genes"
date: 2026-07-07 10:05:00 -0500
tags: [paper]
published: false
paper:
  title: "A synthetic oscillator network of transcriptional regulators (the repressilator)"
  authors: "Elowitz & Leibler"
  venue: "Nature, 2000"
  link: "https://doi.org/10.1038/35002125"
  verdict: "Designed dynamics in a living cell — and an honest first look at how noisy biology makes them."
---
<!-- DRAFT — AI-generated sample review for the paper-a-day comparison exercise. Held at published:false; verify against your own reading before shipping. -->

**The problem.** The toggle switch showed a cell could *hold* a state. Elowitz and Leibler asked the harder dynamical question: could you make a cell *cycle* through states on a schedule you designed, with no natural clock to borrow from?

**The idea.** Three repressors in a ring — LacI represses TetR, TetR represses λ cI, cI represses LacI — a cyclic negative-feedback loop with an odd number of inversions, so it can never settle. On a plasmid in *E. coli*, with GFP reporting one node, the network oscillates with a period of roughly 150 minutes, *longer* than the cell-division time. Again the design came first, from a continuous model that said sustained oscillation needs strong promoters, tight repression, and comparable protein/mRNA lifetimes.

**Why it matters.** Two things. First, it completes the toggle switch's argument: cells are programmable not just in memory but in *time*. Second — and more interesting in hindsight — the oscillations are **noisy**. Period and amplitude vary between sibling cells and drift over generations. That failure to be a clean clock is arguably the paper's most durable contribution: it made stochasticity in gene expression a first-class engineering problem, the thread Elowitz pulled for the next decade. Anyone who has watched a single-cell dataset fan out into unexpected variance recognizes the lesson.

**Verdict.** A founding paper that also, quietly, opened a second field (noise biology). The engineered dynamics are real but fragile — an argument *for* feedback control, later delivered by more robust synthetic oscillators. Post it back-to-back with Gardner as "the two papers that turned cells into circuits."
