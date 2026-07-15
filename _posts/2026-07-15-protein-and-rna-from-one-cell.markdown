---
layout: post
title: "Protein and RNA from one cell"
date: 2026-07-15 01:00:00 -0500
tags: [paper]
paper:
  title: "Simultaneous epitope and transcriptome measurement in single cells (CITE-seq)"
  authors: "Stoeckius et al."
  venue: "Nature Methods, 2017"
  link: "https://doi.org/10.1038/nmeth.4380"
  verdict: "The trick that reads surface proteins and mRNA from the same cell — multimodal single-cell, made to fit existing droplet workflows."
---

**The problem.** Single-cell RNA-seq measures transcripts, but cell identity — especially for immune cells — is often defined by *surface proteins*, the markers flow cytometry has used for decades. Measuring both in the same cell used to mean separate assays on separate cells, losing the pairing that makes the comparison meaningful.

**The idea.** CITE-seq tags antibodies with DNA barcodes ("oligo-tagged antibodies"). Stain cells, run them through a standard droplet scRNA-seq platform, and the antibody barcodes get sequenced right alongside the mRNA — so each cell yields both its transcriptome and a readout of chosen surface proteins. It piggybacks on existing chemistry rather than inventing a new instrument.

**Why it matters.** This is an early, clean example of *multimodal* single-cell measurement — the direction the whole field, and the spatial/single-cell reading arc, keeps moving. It connects the transcriptomic view I know to the protein-level identity that clinicians and immunologists actually use. Methodologically it's elegant: convert a protein measurement into a sequencing readout so one machine captures both.

**Verdict.** Foundational for multimodal single-cell; the antibody-barcoding idea recurs everywhere (cell hashing, feature barcoding). Read it for the design move — turning proteins into sequenceable tags — and as context for why modern single-cell analysis expects more than one modality per cell.
