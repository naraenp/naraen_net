---
layout: post
title: "Single-cell counts from STAR"
date: 2026-07-18 13:00:00 -0500
tags: [paper]
paper:
 title: "STARsolo: accurate, fast and versatile mapping/quantification of single-cell and single-nucleus RNA-seq data"
 authors: "Kaminow, Yunusov & Dobin"
 venue: "bioRxiv, 2021 (preprint)"
 link: "https://doi.org/10.1101/2021.05.05.442755"
 verdict: "An open, drop-in alternative to Cell Ranger's counting, single-cell quantification built into the STAR aligner I already know."
---

**The problem.** Turning droplet single-cell reads into a cell-by-gene count matrix means handling cell barcodes, UMIs, and multi-mapping, then de-duplicating molecules. The standard route (10x's Cell Ranger) is a capable but heavy, semi-closed pipeline, awkward to slot into a custom reproducible workflow, and a black box where I'd rather see the steps.

**The idea.** STARsolo extends the STAR aligner (day 7) to do all of it: barcode demultiplexing, UMI collapsing, and gene counting in one fast, open tool that reproduces Cell Ranger's output closely. Because it's built on STAR, the alignment logic is the same splice-aware engine I already use for bulk RNA-seq, now with the single-cell bookkeeping layered on.

**Why it matters.** This is the counting step that produces the matrices every other tool this day consumes, the input to Scanpy, Harmony, SingleR, velocity. It's also exactly the kind of open, pipeline-friendly component I'd want in a Nextflow single-cell workflow, versus a monolithic vendor tool. Reading it ties the bulk RNA-seq aligner from day 7 directly to the single-cell world, showing they share a core.

**Verdict.** A practical, well-adopted tool (still a preprint at time of writing, so cite as such); its value is openness and integration, not a new algorithm. Read it as the reproducible, STAR-native path from single-cell reads to the count matrix everything downstream needs.
