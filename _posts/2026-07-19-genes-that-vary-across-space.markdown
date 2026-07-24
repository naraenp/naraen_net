---
layout: post
title: "Genes that vary across space"
date: 2026-07-19 03:10:00 -0500
tags: [paper]
paper:
 title: "SpatialDE: identification of spatially variable genes"
 authors: "Svensson, Teichmann & Stegle"
 venue: "Nature Methods, 2018"
 link: "https://doi.org/10.1038/nmeth.4636"
 verdict: "The spatial analogue of differential expression, which genes' expression actually depends on location, told apart from noise."
---

**The problem.** Once you have spatial transcriptomics data, the first analytical question is: which genes show *spatial* structure, expression that varies with position in a non-random way, versus genes that are just noisily scattered? Ordinary differential expression asks about conditions, not coordinates; you need a test built around location itself.

**The idea.** SpatialDE models expression as a function of spatial coordinates using Gaussian processes: it decomposes each gene's variance into a spatial component (explained by a covariance function over positions) and a residual, then tests whether the spatial component is significant. Genes whose expression covaries with location, beyond what noise would produce, are flagged as spatially variable, with a characteristic length scale.

**Why it matters.** This is the foundational statistical primitive for spatial data, the "which genes matter, spatially" step that precedes domain-finding and interpretation. It's a direct conceptual translation of a tool I know (differential expression) into the spatial setting, using the Gaussian-process machinery. For any spatial analysis, including the STU's, identifying spatially variable genes is an early, essential move, and this defined how to do it rigorously.

**Verdict.** Foundational for spatial statistics; later methods (SPARK, and domain-aware approaches) refine the model and scale it. Read it as the spatial counterpart to differential expression, the test that turns coordinates into a question about genes.
