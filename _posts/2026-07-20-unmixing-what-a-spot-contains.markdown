---
layout: post
title: "Unmixing what a spot contains"
date: 2026-07-20 09:00:00 -0500
tags: [paper]
paper:
  title: "SPOTlight: seeded NMF regression to deconvolute spatial transcriptomics spots with single-cell transcriptomes"
  authors: "Elosua-Bayes et al."
  venue: "Nucleic Acids Research, 2021"
  link: "https://doi.org/10.1093/nar/gkab043"
  verdict: "Capture-based spatial spots hold several cells each; SPOTlight uses a single-cell reference to estimate what cell types make up each spot — deconvolution as the price of Visium's low resolution."
---

**The problem.** Capture-based spatial transcriptomics — the Ståhl/Visium lineage — measures expression at spots that each contain several cells, not one. So a spot's profile is a mixture. Without knowing the cell-type composition of each spot, you can't say whether a signal comes from one rare cell type or a blend, and downstream spatial analysis is built on sand.

**The idea.** SPOTlight deconvolves each spot against a single-cell RNA-seq reference. It learns cell-type signatures with a seeded non-negative matrix factorization — initialised from marker genes so the factors map to known cell types — then uses non-negative least squares to estimate each spot's mixture of those types. The output is a composition per spot: how much of each cell type is present.

**Why it matters.** This is the method that makes Visium-style data interpretable at the cell-type level, and it explicitly marries the two modalities the earlier days built up — a single-cell atlas (the reference) and spatial capture (the target). It's the practical counterpart to the deconvolution-benchmark and cell2location entries in the STU reading — the exact analysis the unit runs on spot-based platforms.

**Verdict.** A widely-used, interpretable deconvolution method; results depend heavily on how well the single-cell reference matches the tissue. Read it as the bridge that gives resolution-limited spots a cell-type identity.
