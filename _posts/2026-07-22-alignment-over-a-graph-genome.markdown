---
layout: post
title: "Alignment over a graph genome"
date: 2026-07-22 07:15:00 -0500
tags: [paper]
paper:
 title: "Graph-based genome alignment and genotyping with HISAT2 and HISAT-genotype"
 authors: "Kim et al."
 venue: "Nature Biotechnology, 2019"
 link: "https://doi.org/10.1038/s41587-019-0201-4"
 verdict: "A spliced aligner that maps against a genome graph carrying known variants, not just one linear reference, faster and less reference-biased, and it doubles as a genotyper."
---

**The problem.** Aligning reads to a single linear reference bakes in reference bias: reads carrying an alternate allele map worse, or to the wrong place, precisely where the biology is interesting. RNA-seq adds spliced alignment across introns. You want a fast aligner that knows about population variation and handles splicing without ballooning memory.

**The idea.** HISAT2 builds a graph FM-index that folds millions of known variants and haplotypes into the reference structure, so reads align against a graph of alternatives rather than one sequence. A hierarchical index (global plus many local indexes) keeps it fast and memory-light while supporting spliced alignment. The same machinery drives HISAT-genotype for HLA typing and DNA fingerprinting, alignment and genotyping from one graph.

**Why it matters.** This sits right next to STAR in my RNA-seq stack as the spliced-aligner alternative, and it carries the FM-index/Burrows–Wheeler lineage, the same indexing idea from the foundations reading, into a graph reference. The reference-bias problem it addresses is the same one that motivated graph pangenomes and DeepVariant's re-examination of alignments. For anyone building a variant or expression pipeline, it's a core design choice.

**Verdict.** A widely-used, memory-efficient graph aligner; the graph helps most where good variant catalogues exist, and splicing accuracy still depends on annotation. Read it as alignment that treats the reference as a population, not a single string.
