---
layout: post
title: "How cell2location puts cell types back on the map"
date: 2026-07-09 14:20:00 -0500
tags: [paper]
paper:
  title: "Cell2location maps fine-grained cell types in spatial transcriptomics"
  authors: "Kleshchevnikov et al."
  venue: "Nature Biotechnology, 2022"
  link: "https://doi.org/10.1038/s41587-021-01139-4"
  verdict: "A principled Bayesian answer to spot deconvolution — worth reading as the method, not just the leaderboard name."
---

**The problem.** A Visium spot is a bag of several cells' transcripts. To recover *which* cell types are where, you need to map a single-cell reference onto each spot — and do it in a way that survives technical noise and platform differences, not just curve-fit the counts.

**The idea.** Cell2location is a hierarchical **Bayesian** model. From an annotated single-cell reference it learns per-cell-type expression signatures, then models each spatial spot's observed counts as a combination of those signatures scaled by (absolute) cell-type abundances, with explicit terms for technical effects — sensitivity differences, additive background — and a negative-binomial likelihood for the count noise. Inference is variational, and the payoff is calibrated *absolute* abundance estimates with uncertainty, not just proportions.

**Why it matters.** This is one of the methods the benchmark crowns, so reading the actual model — rather than treating it as a black-box winner — is what lets me explain *why* it works: sharing information through the reference, and modeling technical variation instead of pretending it away. That's the same empirical-Bayes / hierarchical-modeling instinct that shows up in DESeq2 and scVI, which makes it a satisfying through-line across the reading list rather than an isolated tool.

**Verdict.** A genuinely principled method, and the Bayesian machinery is a feature (calibrated uncertainty) more than a cost. Honest limits: it needs a good matched single-cell reference and enough compute for variational inference, and like all deconvolution it's for spot assays — imaging data at single-cell resolution wants segmentation instead. Read it back-to-back with RCTD to see two coherent takes on the same problem.
