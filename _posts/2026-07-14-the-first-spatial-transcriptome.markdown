---
layout: post
title: "The first spatial transcriptome"
date: 2026-07-14 11:30:00 -0500
tags: [paper]
paper:
  title: "Visualization and analysis of gene expression in tissue sections by spatial transcriptomics"
  authors: "Ståhl et al."
  venue: "Science, 2016"
  link: "https://doi.org/10.1126/science.aaf2403"
  verdict: "Where the whole STU field starts — the barcoded-slide method that became Visium and put transcriptomes back onto tissue coordinates."
---

**The problem.** Bulk and single-cell RNA-seq tell you *what* is expressed and, for single-cell, in which cell type — but both discard *where* the cells were. Tissue is organised; function depends on position. How do you measure genome-wide expression while keeping each measurement's location in the section?

**The idea.** Ståhl and colleagues printed a glass slide with spatially barcoded oligo-dT capture spots. A tissue section laid on top releases mRNA that binds the nearest spot, so every captured transcript carries a barcode encoding its coordinate. Sequence it all and you reconstruct a genome-wide expression map registered to the histology image — transcriptomics with an address.

**Why it matters.** This is the founding paper of the field the BIDMC Spatial Technologies Unit works in — it became the basis for 10x Visium, and everything I've read on the spatial track (Squidpy, SpatialData, deconvolution, segmentation, BANKSY) sits downstream of the data type this method created. Reading the origin clarifies the spot-based platform's core trade-off: whole-transcriptome coverage, but spot-level (multi-cell) resolution — the exact reason deconvolution methods exist.

**Verdict.** Foundational, full stop — the spot-based branch of spatial transcriptomics begins here, complementary to the imaging-based branch (Xenium/MERSCOPE). Read it as the root of the STU reading arc.
