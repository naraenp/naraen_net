---
layout: post
title: "Weighting each modality per cell"
date: 2026-07-20 12:20:00 -0500
tags: [paper]
paper:
  title: "Integrated analysis of multimodal single-cell data (Seurat v4 / WNN)"
  authors: "Hao et al."
  venue: "Cell, 2021"
  link: "https://doi.org/10.1016/j.cell.2021.04.048"
  verdict: "Weighted-nearest-neighbor analysis lets each cell decide how much to trust its RNA versus its protein — multimodal integration that adapts per cell, plus a reference atlas you can map onto."
---

**The problem.** CITE-seq gives every cell both a transcriptome and a surface-protein profile, but the two modalities aren't equally informative for every cell — protein resolves some cell states that RNA blurs, and vice versa. Concatenating them, or averaging, throws that away. You want an integration that learns, cell by cell, which modality to lean on.

**The idea.** Weighted-nearest-neighbor (WNN) analysis learns a per-cell weighting of each modality, then builds a single joint neighbour graph from the weighted combination. Clustering, visualization, and downstream analysis run on that shared graph. The paper also assembles a large multimodal PBMC reference atlas and a procedure to map new query datasets onto it, transferring annotations in the reference's coordinate system.

**Why it matters.** This extends the anchor-based integration of Seurat v3 (day 10) from batches to modalities, and it leans directly on CITE-seq (Stoeckius, day 9) as its data type. The reference-mapping half is the same "annotate the query from a reference" idea as SingleR and scANVI, now multimodal. For the STU, principled fusion of protein and RNA is a live question as spatial platforms add protein readouts.

**Verdict.** A field-standard for multimodal single-cell analysis and a workhorse reference-mapping tool; its weightings and mappings assume the reference is representative of the query. Read it as integration that lets each cell speak in whichever modality describes it best.
