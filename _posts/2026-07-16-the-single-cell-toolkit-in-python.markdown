---
layout: post
title: "The single-cell toolkit in Python"
date: 2026-07-16 07:30:00 -0500
tags: [paper]
paper:
 title: "SCANPY: large-scale single-cell gene expression data analysis"
 authors: "Wolf et al."
 venue: "Genome Biology, 2018"
 link: "https://doi.org/10.1186/s13059-017-1382-0"
 verdict: "The framework that made Python the default for single-cell, the substrate scVI, Squidpy and half this reading list are built on."
---

**The problem.** By 2018 single-cell datasets (see: Zheng's droplet method) were exploding in size, but the analysis ecosystem was fragmented and largely R-based. Python needed a scalable, memory-efficient toolkit that could take raw counts through QC, normalisation, dimensionality reduction, clustering, and visualisation without choking on hundreds of thousands of cells.

**The idea.** Scanpy provides exactly that, built around the AnnData object, a single annotated matrix holding expression plus per-cell and per-gene metadata. It implements the standard workflow (PCA, neighbour graphs, Leiden/Louvain clustering, UMAP/t-SNE) with an emphasis on scalability, so the same code runs on a laptop dataset or a million-cell atlas.

**Why it matters.** Scanpy is the substrate. Squidpy (the "Scanpy of spatial," from day 4) extends it; scVI and scANVI produce AnnData; the best-practices bible assumes it. Reading it makes the ecosystem legible, AnnData is the shared container, and most single-cell tools I've read are plugins around this core. It's the Python counterpart to Seurat (next).

**Verdict.** Foundational infrastructure and the de facto Python standard. Not a single method but a well-designed framework, which is arguably more consequential. Read it to understand the object model (AnnData) that everything downstream passes around.
