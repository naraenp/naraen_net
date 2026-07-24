---
layout: post
title: "Reading open chromatin"
date: 2026-07-13 11:30:00 -0500
tags: [paper]
paper:
 title: "Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin (ATAC-seq)"
 authors: "Buenrostro et al."
 venue: "Nature Methods, 2013"
 link: "https://doi.org/10.1038/nmeth.2688"
 verdict: "The assay that made regulatory state easy to measure, accessibility from a few thousand cells, no antibody required."
---

**The problem.** Which parts of the genome are *available* to be read, nucleosome-free, bound by regulators, poised for transcription, is central to what a cell is doing. Earlier methods to map open chromatin (DNase-seq, FAIRE) needed large amounts of material and fussy protocols, putting accessibility profiling out of reach for small or precious samples.

**The idea.** ATAC-seq uses a hyperactive Tn5 transposase preloaded with sequencing adapters: it inserts itself preferentially into open chromatin and tags those regions in a single enzymatic step. From tens of thousands of cells, later, single cells, you get a genome-wide map of accessibility quickly and cheaply.

**Why it matters.** ATAC-seq is the accessibility counterpart to the expression assays I already run, and a pillar of the multi-omic single-cell world the reading list is heading toward. It measures the *regulatory* layer that ENCODE catalogued and that transcription factors act on, the "why" behind an expression change, not just the change. Understanding the assay is understanding what those peaks mean.

**Verdict.** Foundational and now everywhere, especially in single-cell (scATAC) and spatial variants. Read it for the elegance of the Tn5 trick, one enzyme replacing a whole protocol, and for how it slots accessibility into the omics stack.
