---
layout: post
title: "Stitching single-cell datasets together"
date: 2026-07-16 08:30:00 -0500
tags: [paper]
paper:
 title: "Comprehensive Integration of Single-Cell Data (Seurat v3)"
 authors: "Stuart et al."
 venue: "Cell, 2019"
 link: "https://doi.org/10.1016/j.cell.2019.05.031"
 verdict: "The R counterpart to Scanpy, and the anchor-based answer to batch effects, how you merge datasets without erasing biology."
---

**The problem.** Real single-cell studies combine many samples, batches, technologies, even species. Naively pooling them, batch effects dominate: cells cluster by *where they were run*, not by cell type. But over-correct and you scrub out real biological differences. Integration has to align shared cell states across datasets while preserving genuine variation.

**The idea.** Seurat v3 introduces "anchors": pairs of cells across datasets identified (via shared nearest neighbours in a common space) as the same biological state. These anchors define a transformation that harmonises datasets, letting you transfer labels from a reference onto a query or co-embed disparate datasets. It's a principled, correspondence-based approach to batch correction.

**Why it matters.** Seurat is the R half of the single-cell world whose Python half is Scanpy, knowing both is knowing the field's two default toolkits. The anchor idea also connects to scANVI's label transfer (day 4): reference-to-query annotation is a recurring theme, solved here geometrically. Integration is the step that makes atlas-scale single-cell analysis possible at all.

**Verdict.** Foundational and enormously influential; anchors became a standard integration paradigm. Its corrections need care, aggressive integration can hide real differences, but the framework is central. Read it as Scanpy's sibling and the batch-effect workhorse.
