---
layout: post
title: "Matching neighbors across batches"
date: 2026-07-21 10:00:00 -0500
tags: [paper]
paper:
 title: "Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors"
 authors: "Haghverdi et al."
 venue: "Nature Biotechnology, 2018"
 link: "https://doi.org/10.1038/nbt.4091"
 verdict: "The mutual-nearest-neighbors idea that anchored modern batch correction, find cells that are each other's closest match across datasets and use them to compute the correction, without assuming shared population sizes."
---

**The problem.** Combine single-cell datasets from different runs, labs, or technologies and batch effects dominate: cells cluster by experiment, not biology. Earlier correction methods assumed the batches shared the same population composition, a bad assumption when one sample is enriched for a cell type the other lacks. You need a correction that works even when the mixtures differ.

**The idea.** Two cells form a mutual nearest-neighbour (MNN) pair if each is among the other's closest neighbours across batches, a signal that they're the same underlying cell type. The differences across many such pairs estimate the batch-effect vector, which is then subtracted to align the datasets. Because MNNs are found locally, the method tolerates different population compositions between batches, unlike global approaches.

**Why it matters.** MNN is the conceptual ancestor of the anchor- and neighbour-based integration that runs through the single-cell reading, Seurat's anchors, Scanorama, and the batch correction inside Harmony all echo this mutual-neighbour logic. Integration is the unglamorous step that decides whether a multi-sample atlas means anything, and for pipeline-minded work it's the QC gate before downstream analysis. It's where "combine these datasets" became a solved-enough problem.

**Verdict.** A landmark that reframed batch correction and seeded a family of methods; the correction assumes at least some shared cell types exist to anchor on. Read it as the mutual-neighbour insight the whole integration toolkit was built on.
