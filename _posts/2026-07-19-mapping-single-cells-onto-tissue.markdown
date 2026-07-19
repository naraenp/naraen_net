---
layout: post
title: "Mapping single cells onto tissue"
date: 2026-07-19 04:10:00 -0500
tags: [paper]
paper:
  title: "Deep learning and alignment of spatially resolved single-cell transcriptomes with Tangram"
  authors: "Biancalani et al."
  venue: "Nature Methods, 2021"
  link: "https://doi.org/10.1038/s41592-021-01264-7"
  verdict: "The bridge between single-cell and spatial data — place dissociated single cells back onto tissue coordinates, filling in what each platform lacks."
---

**The problem.** Single-cell RNA-seq gives deep, whole-transcriptome cell-type detail but throws away location. Spatial methods keep location but are either coarse (capture) or targeted (imaging). Each has what the other lacks. Can you combine them — use rich single-cell data to annotate spatial data, or use spatial data to give single cells a position?

**The idea.** Tangram learns an alignment: it optimises a mapping of single-cell profiles onto spatial locations so that predicted spatial expression matches the measured spatial data. Once learned, that mapping transfers whatever the single-cell data has — fine cell types, genes outside a targeted panel, annotations — onto the tissue coordinates, and conversely gives single cells spatial context. It's a deep-learning optimisation over the correspondence between the two modalities.

**Why it matters.** This is the integration capstone for the spatial day: it explicitly unites the single-cell world (yesterday) with the spatial world (today), which is precisely the analytical core of STU-style work — deconvolving spots, imputing unmeasured genes, annotating spatial data from a single-cell reference. It's the same "transfer from reference to target" theme (scANVI, SingleR, Seurat) now spanning modalities rather than batches.

**Verdict.** Foundational for single-cell–to–spatial integration and widely used for deconvolution and annotation transfer. Its mappings are inferred, so they warrant validation against known markers. Read it as the method that makes single-cell and spatial data one analysis instead of two.
