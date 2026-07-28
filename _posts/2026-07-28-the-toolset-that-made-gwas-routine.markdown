---
layout: post
title: "The toolset that made GWAS routine"
date: 2026-07-28 02:00:00 -0500
tags: [paper]
paper:
 title: "PLINK: a tool set for whole-genome association and population-based linkage analyses"
 authors: "Purcell et al."
 venue: "American Journal of Human Genetics, 2007"
 link: "https://doi.org/10.1086/519795"
 verdict: "The single program most genome-wide association work ran through for a decade: quality control, association tests, and stratification checks in one fast tool."
---

**The problem.** By 2007 arrays could genotype hundreds of thousands of variants across thousands of people, but the analysis was a mess of one-off scripts. Testing every variant against a trait, filtering bad genotypes, and checking for population structure each needed different code, and none of it scaled to whole-genome data cleanly.

**The idea.** PLINK put the whole workflow in one fast C/C++ program. It handles the unglamorous but essential quality control first: drop variants with too many missing calls, low frequency, or departures from Hardy-Weinberg. It then runs the association tests that make up a genome-wide scan, and it computes relatedness and identity-by-descent between samples so hidden family structure and population stratification, the classic sources of false signal, can be found and controlled. It reads and writes compact binary genotype files that keep large cohorts manageable.

**Why it matters.** This is the practical backbone of a whole era of human genetics, and it sits one step past where my own reading has gone. Day 18 was about calling variants; PLINK is what you reach for once you have genotypes across many people and want to ask which variant tracks a trait. The stratification checks are the same worry that gnomAD and 1000 Genomes exist to inform.

**Verdict.** A foundational tool paper, still the default entry point to association analysis. Read it for the standard QC-then-test pipeline every GWAS still follows.
