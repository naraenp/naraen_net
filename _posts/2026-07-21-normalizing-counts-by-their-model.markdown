---
layout: post
title: "Normalizing counts by their model"
date: 2026-07-21 10:45:00 -0500
tags: [paper]
paper:
  title: "Normalization and variance stabilization of single-cell RNA-seq data using regularized negative binomial regression (sctransform)"
  authors: "Hafemeister & Satija"
  venue: "Genome Biology, 2019"
  link: "https://doi.org/10.1186/s13059-019-1874-1"
  verdict: "Replaces ad-hoc log-normalization with a per-gene negative-binomial model of counts versus sequencing depth — the Pearson residuals stabilize variance and stop depth from masquerading as biology."
---

**The problem.** The routine single-cell workflow normalises counts by library size and log-transforms them, but this is a rough fix: highly-expressed and lowly-expressed genes end up with different variance, and sequencing-depth differences between cells leak into the "biological" signal. Downstream clustering and marker detection inherit these distortions.

**The idea.** sctransform models each gene's UMI counts with negative-binomial regression against cellular sequencing depth, then *regularizes* — pooling information across genes of similar abundance so parameter estimates don't overfit. The Pearson residuals from this model become the normalized values: technical depth effects are regressed out, variance is stabilized across the expression range, and biological heterogeneity is preserved without arbitrary transformation.

**Why it matters.** This is the negative-binomial count model — the same statistical backbone as DESeq2 for bulk RNA-seq and the scVI/stereoscope family for single cells — applied to the humble normalization step everyone runs and few examine. Getting normalization right is upstream of every result, the kind of pipeline-QC decision that quietly determines whether clusters are real. It became a default in the Seurat workflow for exactly that reason.

**Verdict.** A widely-adopted, principled normalization; it's heavier than log-normalization and its assumptions can strain on unusual protocols. Read it as counts normalized by a model of how they were generated, not by a convenient transform.
