---
layout: post
title: "Factors across many omics layers"
date: 2026-07-20 13:10:00 -0500
tags: [paper]
paper:
  title: "MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data"
  authors: "Argelaguet et al."
  venue: "Genome Biology, 2020"
  link: "https://doi.org/10.1186/s13059-020-02015-1"
  verdict: "An unsupervised factor analysis across modalities and groups — it finds the shared axes of variation and tells you which come from which data layer, a multi-view PCA with interpretable weights."
---

**The problem.** When a study measures several modalities across several groups of cells, you want the major axes of variation that structure the whole dataset — and, crucially, to know which modality each axis is driven by. Analysing each layer separately misses shared structure; naïve concatenation loses the ability to attribute variation to its source.

**The idea.** MOFA+ is an unsupervised factor-analysis framework: it infers a small set of latent factors that explain variation across all modalities and sample groups, with per-modality weight matrices that make each factor interpretable — you can read off whether a factor is expressed in the RNA layer, the protein layer, or shared. It scales to large single-cell datasets and handles missing modalities gracefully.

**Why it matters.** This is the linear, interpretable end of the dimensionality-reduction spectrum that runs through the reading — the same reduce-to-latent-factors instinct as PCA, t-SNE, UMAP, and the scVI latent space, but designed to attribute variance across data types. Interpretability is the selling point: for translational work like the STU's, knowing *which layer* a signal lives in is often the finding, not a footnote.

**Verdict.** A widely-used, interpretable integration method; being essentially linear, it can miss the nonlinear structure deep models capture, and factor interpretation still needs care. Read it as the interpretable factor decomposition of a multi-omics dataset.
