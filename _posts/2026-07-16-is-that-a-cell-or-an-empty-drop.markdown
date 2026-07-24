---
layout: post
title: "Is that a cell or an empty drop?"
date: 2026-07-16 08:00:00 -0500
tags: [paper]
paper:
 title: "EmptyDrops: distinguishing cells from empty droplets in droplet-based single-cell RNA sequencing data"
 authors: "Lun et al."
 venue: "Genome Biology, 2019"
 link: "https://doi.org/10.1186/s13059-019-1662-y"
 verdict: "The QC step that decides which barcodes are real cells, a direct consequence of how droplet single-cell actually works."
---

**The problem.** In droplet single-cell (day 9's 10x method), most droplets contain no cell, just ambient RNA floating in the suspension. These empty drops still capture stray transcripts and get barcodes, so the raw data mixes real cells with thousands of low-count noise barcodes. A naive count threshold either discards small real cells or admits empty ones.

**The idea.** EmptyDrops models the ambient RNA profile explicitly: it estimates the background expression pattern from the clearly-empty droplets, then tests each barcode for whether its expression *deviates* from that ambient profile, not merely whether it has high counts. Small but genuine cells that differ from background are retained; high-count barcodes that just reflect ambient RNA are flagged.

**Why it matters.** This is the QC consequence of understanding the assay. Because I read how droplets generate the data, the need for this step is obvious rather than mysterious, ambient contamination is baked into the method. It's the same lesson as fastp and MultiQC: knowing where artefacts come from tells you which cleaning step to trust. Scanpy and Seurat both lean on this logic.

**Verdict.** Foundational for single-cell QC and a standard early step. Read it for the statistical move, test against the ambient profile, not a raw threshold, and as a model of QC that flows directly from assay mechanics.
