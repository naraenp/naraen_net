---
layout: post
title: "Deconvolution, robustly"
date: 2026-07-09 14:55:00 -0500
tags: [paper]
paper:
  title: "Robust decomposition of cell type mixtures in spatial transcriptomics (RCTD / spacexr)"
  authors: "Cable et al."
  venue: "Nature Biotechnology, 2022"
  link: "https://doi.org/10.1038/s41587-021-00830-w"
  verdict: "The other workhorse deconvolution method — its whole point is correcting the platform gap between reference and spatial data."
---

**The problem.** Deconvolution leans on a single-cell reference, but the reference and the spatial assay are measured on *different platforms*, with different biases. Ignore that gap and you get confident, wrong cell-type maps. RCTD's central claim is that handling this **platform effect** is what separates a robust method from a fragile one.

**The idea.** RCTD (Robust Cell Type Decomposition, shipped as **spacexr**) fits a statistical model that learns cell-type profiles from a reference and estimates each spot's mixture while *explicitly* estimating and correcting the systematic platform difference between reference and spatial data. It runs in modes suited to the assay's resolution — from near-single-cell (one or two cell types per pixel) to lower-resolution spots — so it degrades gracefully rather than assuming one cells-per-spot regime.

**Why it matters.** Read alongside cell2location, this is the instructive contrast: cell2location leans on full hierarchical Bayesian modeling of technical variation; RCTD foregrounds the *reference-vs-spatial platform mismatch* as the thing to correct. Same problem, two philosophies — and understanding both is what lets me pick, and justify, one for a given dataset rather than defaulting to whatever's popular. That "know why, not just which" is the standard I want for every pipeline choice.

**Verdict.** Robust and widely used for good reasons, and unusually clear about *what* it's correcting for, which I appreciate in a method. Same honest ceiling as all deconvolution — it needs a decent reference and is aimed at spot/near-spot data, with segmentation the better frame for true single-cell imaging. This closes the deconvolution cluster; segmentation is where the reading goes next.
