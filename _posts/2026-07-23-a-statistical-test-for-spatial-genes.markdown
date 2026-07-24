---
layout: post
title: "A statistical test for spatial genes"
date: 2026-07-23 08:30:00 -0500
tags: [paper]
paper:
 title: "Statistical analysis of spatial expression patterns for spatially resolved transcriptomic studies (SPARK)"
 authors: "Sun, Zhu & Zhou"
 venue: "Nature Methods, 2020"
 link: "https://doi.org/10.1038/s41592-019-0701-7"
 verdict: "Spatially-variable-gene detection with rigorous error control, a generalized linear spatial model on raw counts that delivers calibrated p-values and real statistical power."
---

**The problem.** Identifying spatially variable genes is a hypothesis test, and tests are only trustworthy if they control false positives. Early approaches modeled transformed data or leaned on approximations that could inflate type-I error, so a gene flagged as "spatial" might just be noise. You want a method built on the actual count distribution that gives well-calibrated significance, not just a ranking.

**The idea.** SPARK models spatial count data directly through generalized linear spatial models, placing spatial correlation structure on the counts and testing multiple spatial kernels to capture different pattern shapes. Using established statistical formulas for hypothesis testing and a computationally efficient penalized quasi-likelihood algorithm, it yields properly calibrated p-values with effective type-I error control, and, on published datasets, up to ten times the power of earlier methods at finding genuine spatial patterns.

**Why it matters.** SPARK is the statistically-rigorous member of the spatially-variable-gene family, next to SpatialDE (spatial day) and nnSVG (today's previous read, which chases scalability). The emphasis on calibrated error control is the same discipline as the FDR and multiple-testing thread running through my reading (Benjamini–Hochberg, GSEA permutations). For clinical/translational spatial work like the STU's, defensible p-values aren't optional.

**Verdict.** A foundational, well-calibrated SVG method; testing several kernels and count modeling makes it heavier than approximate methods, and very large datasets pushed the field toward nnSVG. Read it as the spatially-variable-gene test that takes statistical rigor seriously.
