---
layout: post
title: "Does RNA-seq beat the microarray?"
date: 2026-07-13 07:45:00 -0500
tags: [paper]
paper:
  title: "Evaluating gene expression in C57BL/6J and DBA/2J mouse striatum using RNA-Seq and microarrays"
  authors: "Bottomly et al."
  venue: "PLoS ONE, 2011"
  link: "https://doi.org/10.1371/journal.pone.0017820"
  verdict: "The head-to-head that helped justify the switch to sequencing — and a benchmark dataset I've seen recycled in half the DE tutorials since."
---

**The problem.** Around 2010 the field was mid-transition from microarrays to RNA-seq, and the honest question was empirical: does sequencing actually detect more, and more reliable, differential expression than the array it was replacing? You can't answer that with theory alone — you need the same biological samples run on both.

**The idea.** Bottomly and colleagues profiled striatum from two well-characterised inbred mouse strains on both platforms. They compared how many differentially expressed genes each technology found, how concordant the calls were, and how sensitivity scaled with the number of replicates — showing RNA-seq's advantage but also how much it depends on adequate replication.

**Why it matters.** Two things. First, it's a clean illustration of *why* the pipelines I run are sequencing-based. Second, the Bottomly dataset became a standard teaching and benchmarking set — if you've compared DE methods, you've probably met these mice. Recognising the provenance of a benchmark is part of reading its results critically.

**Verdict.** Solid, of-its-moment, and more useful now as a reference dataset than as news. Read it for the replication lesson — sensitivity is bought with replicates, not just read depth — which is exactly the design trade-off my own RNA-seq runs live under.
