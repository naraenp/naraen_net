---
layout: post
title: "Assembling both haplotypes"
date: 2026-07-22 12:30:00 -0500
tags: [paper]
paper:
 title: "Haplotype-resolved de novo assembly using phased assembly graphs with hifiasm"
 authors: "Cheng et al."
 venue: "Nature Methods, 2021"
 link: "https://doi.org/10.1038/s41592-020-01056-5"
 verdict: "The HiFi-era assembler that keeps both parental copies apart, building a phased assembly graph so a diploid genome comes out as two haplotypes, not one blended consensus."
---

**The problem.** Most assemblers collapse a diploid genome into a single mosaic consensus, discarding which variant came from which parent, exactly the haplotype information that matters for structural variation and allele-specific biology. Accurate long HiFi reads finally make phasing feasible, but you need an algorithm designed to preserve, not average away, both haplotypes.

**The idea.** hifiasm exploits the low error rate of PacBio HiFi reads to build a *phased* assembly graph in which heterozygous differences are retained rather than smoothed over. Instead of maintaining the contiguity of just one haplotype, it strives to keep all haplotypes contiguous, resolving the graph into two haplotype-resolved assemblies (or handling trios and polyploids). Demonstrated from human to a ~30-Gb hexaploid redwood, it routinely beat existing tools on haplotype-resolved contiguity.

**Why it matters.** This closes the long-read assembly thread I've been reading, the Nanopore genome papers, PacBio HiFi, and now the assembler that turns HiFi reads into finished, phased genomes. It's the technology behind the complete diploid and T2T-style assemblies, and phasing is what makes structural and allele-specific analysis possible. For anyone moving from resequencing to real de novo work, it's the current default.

**Verdict.** The leading HiFi assembler; it depends on high-quality HiFi input and phasing is hardest in low-heterozygosity or highly repetitive regions. Read it as the tool that made routine haplotype-resolved genome assembly real.
