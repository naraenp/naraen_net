---
layout: post
title: "A probabilistic take on spot deconvolution"
date: 2026-07-20 09:50:00 -0500
tags: [paper]
paper:
  title: "Single-cell and spatial transcriptomics enables probabilistic inference of cell type topography (stereoscope)"
  authors: "Andersson et al."
  venue: "Communications Biology, 2020"
  link: "https://doi.org/10.1038/s42003-020-01247-y"
  verdict: "The same spot-deconvolution goal as SPOTlight, but built on an explicit negative-binomial count model — a generative view of how the mixture was produced."
---

**The problem.** Deconvolving spatial spots into cell types (SPOTlight) can be done by regression, but count data from sequencing is noisy and over-dispersed. A method that models the actual statistics of how counts are generated — rather than treating them as continuous quantities to fit — should estimate proportions more faithfully, especially for low-count spots and rare types.

**The idea.** Stereoscope models both the single-cell reference and the spatial data with the negative binomial distribution, the natural model for over-dispersed counts. It learns cell-type-specific expression parameters from the single-cell data, then does probabilistic inference of the cell-type proportions that best explain each spot's counts under that generative model. The result is a principled, uncertainty-aware composition estimate per spot.

**Why it matters.** The negative-binomial framing is the same statistical backbone that runs through this whole reading — it's what DESeq2 uses for RNA-seq and what the scVI family uses for single cells — now applied to spatial mixtures. For the STU, having a generative model means the deconvolution carries a notion of confidence, not just a point estimate, which matters when calls feed clinical interpretation.

**Verdict.** A foundational probabilistic alternative to regression-based deconvolution; heavier to run and, like all reference methods, only as good as the single-cell atlas behind it. Read it as the count-model view of what's inside a spot — the statistically-principled sibling of SPOTlight.
