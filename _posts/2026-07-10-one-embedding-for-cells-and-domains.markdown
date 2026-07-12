---
layout: post
title: "One embedding for cells and domains"
date: 2026-07-10 10:00:00 -0500
tags: [paper]
paper:
  title: "BANKSY unifies cell typing and tissue domain segmentation"
  authors: "Singhal et al."
  venue: "Nature Genetics, 2024"
  link: "https://doi.org/10.1038/s41588-024-01664-3"
  verdict: "A clever single trick — encode the neighborhood into each cell's feature vector — that does two jobs at once."
---

**The problem.** Spatial analysis usually splits into two tasks with two toolchains: *cell typing* (what is this cell?) and *domain segmentation* (what tissue region is it in?). Standard clustering ignores space entirely; the fix has been bespoke methods for each question.

**The idea.** BANKSY augments every cell's own expression with two extra blocks: the *mean* expression of its spatial neighbors, and the *azimuthal gradient* of that neighborhood (which direction expression is changing). Cluster on the augmented vector and, by tuning how much neighborhood weight you add, the *same* algorithm gives you cell types at one setting and tissue domains at another. One embedding, one clustering step, two answers.

**Why it matters.** The elegance is the point: it slots into the standard Scanpy/Squidpy workflow instead of demanding a new framework, and the neighborhood-augmentation idea is intuitive enough to trust and explain. For a facility that has to justify its choices, a method you can reason about beats a black box. It also connects cleanly to the deconvolution reading — both are ways of putting *spatial context* back into single-cell thinking.

**Verdict.** Genuinely neat, and its lightweight feature-engineering framing is a strength. The honest caveat is that the neighborhood-scale parameter matters and wants tuning per tissue, and "domain" is only as meaningful as your neighborhood radius. Read it as the practical default for spatially-aware clustering.
