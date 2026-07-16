---
layout: post
title: "Catching the doublets"
date: 2026-07-16 10:30:00 -0500
tags: [paper]
paper:
  title: "Scrublet: Computational Identification of Cell Doublets in Single-Cell Transcriptomic Data"
  authors: "Wolock, Lopez & Klein"
  venue: "Cell Systems, 2019"
  link: "https://doi.org/10.1016/j.cels.2018.11.005"
  verdict: "The other droplet artefact — two cells in one drop — and how to spot the fake 'cell type' they create."
---

**The problem.** Droplet single-cell occasionally traps *two* cells in one droplet. The result is a barcode whose expression is a blend of two real cell types — and that blend can masquerade as a novel intermediate cell state, inventing biology that doesn't exist. Unlike empty drops (high counts, not low), doublets hide among the real cells.

**The idea.** Scrublet detects them by simulation: it computationally generates synthetic doublets by adding together pairs of observed transcriptomes, then scores each real barcode by how similar it is to these simulated blends. Barcodes that look like artificial doublets get flagged, so suspected doublets can be removed before clustering and annotation.

**Why it matters.** Together with EmptyDrops, this completes the pair of QC steps that follow directly from how droplet data is generated — empty drops and doublets are the two failure modes of one-cell-per-drop, and both must be handled before Scanpy/Seurat clustering is trustworthy. Reading it reinforces the theme of the day: the single-cell toolchain is largely a set of principled corrections for known assay artefacts.

**Verdict.** Foundational for single-cell QC and a standard step; DoubletFinder and others solve the same problem similarly. Read it for the neat simulate-then-compare trick, and as the doublet half of droplet QC.
