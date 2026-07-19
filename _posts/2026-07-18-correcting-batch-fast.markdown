---
layout: post
title: "Correcting batch, fast"
date: 2026-07-18 10:15:00 -0500
tags: [paper]
paper:
  title: "Fast, sensitive and accurate integration of single-cell data with Harmony"
  authors: "Korsunsky et al."
  venue: "Nature Methods, 2019"
  link: "https://doi.org/10.1038/s41592-019-0619-0"
  verdict: "The lightweight batch-correction workhorse — integration in the embedding space, fast enough to be a default step."
---

**The problem.** Combining single-cell datasets (Seurat's anchors, day 10, solve this too) means removing batch effects without erasing biology. Anchor- and MNN-based methods work but can be heavy on large datasets, and you often want to integrate *after* dimensionality reduction, iterating quickly rather than reprocessing from raw counts.

**The idea.** Harmony operates in PCA space. It iteratively clusters cells in the embedding, computes batch-specific correction factors that pull cells of the same soft cluster together across batches, and repeats until batches are mixed but clusters preserved. Because it works on the low-dimensional embedding rather than the full matrix, it's fast and scales to large atlases — while a soft-clustering penalty guards against over-correcting away real differences.

**Why it matters.** Harmony is one of the most-used integration tools and a standard Scanpy/Seurat step, so it's a default I should understand rather than invoke blindly. It's the fast, embedding-space counterpart to Seurat's anchors and Scanorama's stitching — three answers to the same batch problem, differing in where and how aggressively they correct. Knowing the trade-offs is knowing when to trust the integrated space.

**Verdict.** Foundational for practical single-cell integration; its speed made routine integration feasible. As with all batch correction, over-integration is the risk to watch. Read it as the efficient, widely-defaulted member of the integration toolkit.
