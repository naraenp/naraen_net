---
layout: post
title: "Calling variants across many samples at once"
date: 2026-07-24 02:00:00 -0500
tags: [paper]
paper:
 title: "Scaling accurate genetic variant discovery to tens of thousands of samples"
 authors: "Poplin et al."
 venue: "bioRxiv, 2018"
 link: "https://doi.org/10.1101/201178"
 verdict: "The GVCF workflow behind my pipeline: call each sample once, then genotype the cohort together, so adding a genome does not mean re-processing every genome."
---

**The problem.** Early joint calling needed the raw reads of every sample in memory at the same time. Add one genome to a cohort of a thousand and you re-ran the whole set. That does not scale. My variant pipeline needs a way to grow a cohort without paying the full cost each time.

**The idea.** GATK splits the work into two steps. HaplotypeCaller assembles each sample's reads into local haplotypes and writes a GVCF, a per-sample record that reports the evidence at every position, not only the variant ones. A second step, joint genotyping, reads all the GVCFs together and decides the final genotypes across the cohort. Because the expensive per-sample work happens once, adding a genome only means one more GVCF and a re-run of the cheap joint step.

**Why it matters.** This is the exact workflow inside `variant_calling_nf`, downstream of BWA. Reading it explains why the pipeline writes a GVCF per sample before it genotypes: the design is built for cohorts that grow. It also shows why the per-position reference model matters, since a confident "no variant here" is as useful as a call.

**Verdict.** The paper that made large-cohort calling practical and set the GVCF format everyone now uses. Read it for the two-step logic, and read the current GATK docs for the commands.
