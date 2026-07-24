---
layout: post
title: "The Scanpy of spatial"
date: 2026-07-10 11:40:00 -0500
tags: [paper]
paper:
 title: "Squidpy: a scalable framework for spatial omics analysis"
 authors: "Palla et al."
 venue: "Nature Methods, 2022"
 link: "https://doi.org/10.1038/s41592-021-01358-2"
 verdict: "The toolkit that gives spatial data the same batteries-included ergonomics Scanpy gave single-cell, this is the daily driver."
---

**The problem.** Single-cell analysis has Scanpy: a mature, composable toolkit everyone shares. Spatial analysis, for a while, was a pile of one-off scripts. What you want is the same thing, a common object and a standard set of *spatially aware* operations, so analyses are reproducible and comparable across labs.

**The idea.** Squidpy builds on the AnnData world and adds the spatial layer: a neighbors graph based on physical coordinates, and spatial statistics on top of it, neighborhood enrichment, co-occurrence, Moran's I for spatial autocorrelation, ligand–receptor analysis. It also carries an image container so histology and expression live together. The design goal is scalability and interoperability, not a new silo.

**Why it matters.** For a facility, the tool everyone already knows *is* the reproducibility win, shared vocabulary, shared object, less bespoke glue. Squidpy is where a lot of the earlier reading actually gets executed: the neighborhood graph here is the same spatial-context idea that BANKSY and the deconvolution methods each exploit differently. It's the practical hub of the spatial stack.

**Verdict.** The sensible default and the one I'd build a facility workflow around. Its ceiling is that it's a framework, not an answer, it gives you the operations, you still bring the biological questions and the QC judgment. Read it as the toolkit, then pair with SpatialData for the storage layer.
