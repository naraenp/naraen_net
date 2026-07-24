---
layout: post
title: "A field map for spatial transcriptomics"
date: 2026-07-09 09:10:00 -0500
tags: [paper]
paper:
 title: "Statistical and machine learning methods for spatially resolved transcriptomics data analysis"
 authors: "Zeng et al."
 venue: "Genome Biology, 2022"
 link: "https://doi.org/10.1186/s13059-022-02653-7"
 verdict: "The fastest way to load the whole spatial-analysis vocabulary in one sitting, the Khalil & Collins of this field."
---

**The problem.** Spatial transcriptomics adds coordinates to expression, and with them a new stack of computational problems that don't exist in dissociated single-cell data. Before touching any one method I wanted the map, what are the *questions*, and what families of methods answer them?

**The idea.** This review organizes the field by task. **Spatial clustering / domain detection**, grouping spots or cells into tissue regions using expression *and* neighborhood. **Deconvolution**, for spot-based assays (Visium), estimating the cell-type mixture inside each spot from a single-cell reference. **Spatially variable genes**, finding genes whose expression depends on location, not just cell type. **Cell–cell interaction / communication**, inferring signalling from spatial co-occurrence. For each it lays out the statistical and ML approaches and their assumptions.

**Why it matters.** This is the orientation read for the spatial track, the one that gives me the shared vocabulary a core-facility conversation assumes (domains, deconvolution, SVGs, niches). It also frames spatial analysis the way I already think about single-cell: a pipeline of decision points, each with defensible defaults and failure modes, which is exactly the reproducibility-and-standards lens a facility cares about.

**Verdict.** As a review there's no single result to stress-test, and being 2022 it predates the imaging-platform benchmarks and the newest domain methods (BANKSY, the 2025 comparisons), so it's the map, not the frontier. But for loading the concepts in one pass it's ideal, and it's the natural first post of a spatial series before zooming into deconvolution or segmentation. Read it the way I read the synbio field-map: to place everything that follows.
