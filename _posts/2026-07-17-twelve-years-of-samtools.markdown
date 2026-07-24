---
layout: post
title: "Twelve years of SAMtools"
date: 2026-07-17 09:30:00 -0500
tags: [paper]
paper:
 title: "Twelve years of SAMtools and BCFtools"
 authors: "Danecek et al."
 venue: "GigaScience, 2021"
 link: "https://doi.org/10.1093/gigascience/giab008"
 verdict: "The file formats and utilities every sequencing pipeline is plumbed with, the SAM/BAM/VCF layer my own pipelines pass data through at every step."
---

**The problem.** Sequencing generates enormous alignments and variant sets, and without shared, efficient formats every tool would speak its own dialect. Aligners, callers, and viewers need a common language, and fast, indexed access to slices of huge files, or the whole ecosystem fragments.

**The idea.** SAMtools defined SAM/BAM (alignments) and BCFtools defined VCF/BCF (variants), together with the htslib library underneath and a suite of utilities: sort, index, view, filter, call, merge. This retrospective marks twelve years of that toolkit, the formats becoming universal standards, and the library becoming the shared engine other tools build on. It's less a single method than the connective tissue of sequencing analysis.

**Why it matters.** Both my pipelines are plumbed with these. BWA emits SAM, SAMtools sorts and indexes to BAM, GATK and BCFtools produce and manipulate VCFs, every stage of `variant_calling_nf` speaks htslib formats. Reading this makes the invisible standard visible: the reason my tools interoperate at all is that they all agreed on SAM/BAM/VCF. It's the sequencing counterpart to htslib-as-lingua-franca.

**Verdict.** Foundational infrastructure, arguably as consequential as any single algorithm, standards enable everything downstream. Read it for the format definitions and the reminder that a shared file format is a quiet act of field-building.
