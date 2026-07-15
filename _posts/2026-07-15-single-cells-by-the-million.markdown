---
layout: post
title: "Single cells by the million"
date: 2026-07-15 02:00:00 -0500
tags: [paper]
paper:
  title: "Massively parallel digital transcriptional profiling of single cells"
  authors: "Zheng et al."
  venue: "Nature Communications, 2017"
  link: "https://doi.org/10.1038/ncomms14049"
  verdict: "The droplet platform that made single-cell routine — the 10x Chromium method behind most scRNA-seq data I'll ever touch."
---

**The problem.** Early single-cell RNA-seq was low-throughput and expensive — hundreds of cells, plate-based, laborious. To see cell-type heterogeneity in a real tissue you need thousands to millions of cells profiled cheaply and reproducibly. The bottleneck was a scalable way to barcode individual cells.

**The idea.** Zheng and colleagues describe the droplet microfluidic system (commercialised as 10x Genomics Chromium) that encapsulates single cells with barcoded gel beads: each cell's transcripts get a shared cell barcode and unique molecular identifiers, so a whole pooled sequencing run can be demultiplexed back to individual cells and de-duplicated to molecule counts. Throughput jumps by orders of magnitude.

**Why it matters.** This is the data-generating engine behind the single-cell world the reading list keeps circling — scVI, scANVI, Scanpy, the best-practices bible all assume data shaped like this. Understanding the assay explains the analysis: why UMIs exist, why droplets create doublets and empty drops (hence Scrublet, EmptyDrops), why counts are sparse. The method defines the downstream problems.

**Verdict.** Foundational — arguably the paper that made single-cell genomics mainstream. Read it to connect the analysis tools I study to the physical experiment that produces their input, and to see where the artefacts those tools correct actually come from.
