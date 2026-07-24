---
layout: post
title: "Imaging transcripts in place"
date: 2026-07-19 00:10:00 -0500
tags: [paper]
paper:
 title: "Spatially resolved, highly multiplexed RNA profiling in single cells (MERFISH)"
 authors: "Chen et al."
 venue: "Science, 2015"
 link: "https://doi.org/10.1126/science.aaa6090"
 verdict: "The imaging-based branch of spatial transcriptomics, single-molecule resolution, the complement to Visium's spots and the STU's other half."
---

**The problem.** Spot-based spatial transcriptomics (Ståhl, day 8) captures the whole transcriptome but at spot resolution, each spot is several cells. To see *which individual cell* expresses what, and exactly where each transcript sits, you need to image molecules directly in tissue, not capture them on a grid. But imaging one gene at a time can't scale to hundreds.

**The idea.** MERFISH images RNA in place with error-robust barcoding: each target gene gets a binary barcode read out over successive rounds of hybridization and imaging, with the code designed so errors can be detected and corrected. This multiplexes hundreds to thousands of genes at single-molecule, single-cell, subcellular resolution, a map of individual transcripts in intact tissue.

**Why it matters.** This is the imaging-based pole of the spatial field the BIDMC STU works across, the high-resolution complement to Visium's whole-transcriptome-but-coarse spots. The two branches (imaging vs. capture) trade resolution against gene-panel breadth, and understanding that trade-off is central to the role. MERFISH is also the conceptual ancestor of commercial platforms like Xenium (later today).

**Verdict.** Foundational, it opened imaging-based spatial transcriptomics. Its limits are panel size (targeted, not whole-transcriptome) and imaging throughput. Read it as the resolution end of the spatial spectrum, opposite Ståhl's spots, and the root of the imaging platforms the STU evaluates.
