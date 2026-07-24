---
layout: post
title: "Mapping reads to the genome"
date: 2026-07-12 12:50:00 -0500
tags: [paper]
paper:
 title: "Fast and Accurate Short Read Alignment with Burrows–Wheeler Transform (BWA)"
 authors: "Li & Durbin"
 venue: "Bioinformatics, 2009"
 link: "https://doi.org/10.1093/bioinformatics/btp324"
 verdict: "Where the last two days converge, the aligner in my own variant pipeline, built on the BWT and FM-index I just read about."
---

**The problem.** Next-gen sequencing produces tens of millions of short reads per run; every one has to be placed against a three-billion-base reference, tolerating sequencing errors and real variants. Doing that fast enough, and accurately enough, was the bottleneck standing between raw reads and any biology.

**The idea.** BWA indexes the reference genome with a Burrows–Wheeler transform and FM-index (yesterday's and this morning's papers, now doing real work), then aligns reads by backward search over that index, extended to allow mismatches and gaps for sequencing error and variation. The compressed index fits in memory, and lookups scale with read length, not genome size. Later modes (BWA-MEM) handle longer reads with seed-and-extend, but the core is that same self-index.

**Why it matters.** This isn't abstract for me, BWA is the alignment step in my `variant_calling_nf` pipeline. Reading the algorithm behind a tool I *run* closes a satisfying loop: the compression theory from days ago is literally what maps my FASTQs before GATK ever sees them. Understanding it is the difference between running a black box and owning the pipeline.

**Verdict.** Foundational and still ubiquitous, BWA-MEM remains a default aligner more than a decade on. Its limits are those of short-read mapping itself (repetitive regions, structural variants) that long reads later addressed. Read it as the practical payoff of the BWT/FM-index thread.
