---
layout: post
title: "Counting reads into genes"
date: 2026-07-22 08:00:00 -0500
tags: [paper]
paper:
  title: "featureCounts: an efficient general purpose program for assigning sequence reads to genomic features"
  authors: "Liao, Smyth & Shi"
  venue: "Bioinformatics, 2014"
  link: "https://doi.org/10.1093/bioinformatics/btt656"
  verdict: "The quiet step between alignment and differential expression — turning mapped reads into a gene-by-sample count matrix, fast and by well-defined rules."
---

**The problem.** After alignment, you still have to decide which gene (or exon) each read belongs to and tally the totals — the count matrix every differential-expression tool consumes. It sounds trivial, but reads overlap multiple features, span exon boundaries, and come in pairs; the rules for assignment and the speed of applying them across billions of reads matter a great deal.

**The idea.** featureCounts assigns each aligned read (or fragment) to genomic features using explicit, configurable overlap rules, with efficient chromosome hashing and feature blocking that make it roughly an order of magnitude faster than earlier counters while using far less memory. It handles single- and paired-end data, strandedness, and multi-overlap policies, emitting the tidy counts-by-sample matrix that feeds edgeR, DESeq2, or limma.

**Why it matters.** This is a literal component of my own RNA-seq pipeline — the bridge from STAR alignments to a DESeq2 count matrix — and it pairs naturally with the alignment-free quantifiers (kallisto, Salmon) I read earlier as the two philosophies of "how many reads per gene." The assignment rules are a quiet source of results differences, so understanding them is real pipeline hygiene.

**Verdict.** A fast, standard counter and a default in count-based RNA-seq workflows; its choices (multi-mappers, overlaps) shape the numbers, so set them deliberately. Read it as the unglamorous, load-bearing step upstream of every DE result.
