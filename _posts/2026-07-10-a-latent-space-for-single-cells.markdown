---
layout: post
title: "A latent space for single cells"
date: 2026-07-10 13:20:00 -0500
tags: [paper]
paper:
 title: "Deep generative modeling for single-cell transcriptomics (scVI)"
 authors: "Lopez et al."
 venue: "Nature Methods, 2018"
 link: "https://doi.org/10.1038/s41592-018-0229-2"
 verdict: "The paper that put single-cell analysis on a principled probabilistic footing, a VAE that does normalization, batch correction, and imputation in one model."
---

**The problem.** Single-cell counts are sparse, noisy, and shot through with technical variation, dropout, library-size differences, batch effects. The usual pipeline patches each with a separate ad-hoc step. What you want is one model that treats the noise as noise and hands you a clean, low-dimensional representation.

**The idea.** scVI is a variational autoencoder for scRNA-seq. It models raw counts with a zero-inflated negative binomial likelihood, learns a latent embedding of each cell, and folds batch as a covariate so the latent space is corrected by construction. From that one fit you get denoised expression, batch-integrated coordinates for clustering, and a generative model you can sample from, all with calibrated uncertainty rather than point estimates.

**Why it matters.** This is the hierarchical/empirical-Bayes instinct again, the same thread running through DESeq2 and cell2location, now in deep-learning form, and it became the backbone of the whole `scvi-tools` ecosystem. For me it's a satisfying convergence point: the probabilistic modeling I trust from bulk RNA-seq, scaled to single cell, and directly relevant to the spatial deconvolution methods that borrow its machinery.

**Verdict.** A genuine foundation, and the modeling is principled rather than a black box. Costs: it needs enough cells and compute, and the latent space is only as trustworthy as the model's assumptions about your data. Read it back-to-back with scANVI, which adds labels to exactly this framework.
