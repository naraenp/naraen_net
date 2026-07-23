---
layout: post
title: "Searching millions of sequences"
date: 2026-07-23 04:45:00 -0500
tags: [paper]
paper:
  title: "MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets"
  authors: "Steinegger & Söding"
  venue: "Nature Biotechnology, 2017"
  link: "https://doi.org/10.1038/nbt.3988"
  verdict: "BLAST-level sensitivity at hundreds of times the speed — the search-and-cluster engine that made metagenomic- and atlas-scale protein comparison tractable."
---

**The problem.** Comparing protein sequences against huge databases is the bread-and-butter of bioinformatics — annotation, homology, clustering — but sequencing throughput outran search speed. Sensitive tools like PSI-BLAST are too slow for metagenomes with hundreds of millions of sequences; fast tools sacrifice the sensitivity needed to catch remote homologs. The speed–sensitivity trade-off was the bottleneck.

**The idea.** MMseqs2 (Many-against-Many sequence searching) uses a fast prefiltering stage built on consecutive short k-mer matches on the same diagonal to cheaply discard non-homologous pairs, then applies vectorized Smith–Waterman alignment only to survivors. A cascaded clustering mode groups massive sequence sets efficiently. The result spans the whole speed–sensitivity range, reaching sensitivity better than PSI-BLAST at more than 400 times the speed, and parallelizes across cores and machines.

**Why it matters.** This is infrastructure the rest of the field quietly runs on — including the protein-language-model world I read about, where MMseqs2 clustering builds the non-redundant training sets and MSAs behind ESM and AlphaFold-style methods. It's the same "make the fundamental operation fast enough to change what's possible" move as minimap2 for alignment (yesterday). Scale is the enabler.

**Verdict.** A foundational, ubiquitous search/clustering tool; sensitivity settings trade against speed, so tune to the task. Read it as the engine that made protein search keep pace with sequencing.
