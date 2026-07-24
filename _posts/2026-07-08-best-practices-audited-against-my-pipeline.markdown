---
layout: post
title: "Best practices, audited against my own pipeline"
date: 2026-07-08 14:00:00 -0500
tags: [paper]
paper:
 title: "A survey of best practices for RNA-seq data analysis"
 authors: "Conesa et al."
 venue: "Genome Biology, 2016"
 link: "https://doi.org/10.1186/s13059-016-0881-8"
 verdict: "Essentially an annotated map of the exact stages in my RNA-seq pipeline, a checklist to grade my own DAG against."
---

**The problem.** Everyone builds an RNA-seq workflow; far fewer can defend each choice. This review is the field's consensus map, QC through interpretation, and I read it as an audit of my own `plant_rnaseq_nf` DAG rather than as new material.

**The idea.** It walks the whole pipeline and states the defensible default at each stage. **Design** first: biological replicates beat sequencing depth for detecting differential expression (three-plus replicates over more reads). **QC** at the read level (FastQC), then **alignment**, spliced aligners (STAR, HISAT) versus alignment-free quantification (kallisto, Salmon) and when each is appropriate. **Quantification and normalization** (why within- and between-sample normalization differ), **differential expression** (edgeR / DESeq2 / limma-voom and their assumptions), and **functional interpretation** (enrichment). Then the frontier: isoform-level analysis, fusion detection, eQTL, and integration with other omics.

**Why it matters.** Going stage by stage against my own pipeline is the most useful thing I can do with a review like this, it turns "I used STAR and DESeq2" into "here's *why*, and here's where the review says I could do better." The replicates-over-depth point in particular is the kind of design wisdom that's cheap to state and expensive to relearn.

**Verdict.** A few years on, the scaffold is still right even as specific tools moved (Salmon/kallisto now routine, single-cell exploded into its own literature). As a primary source it's a review, so there's no result to stress-test, but as a self-audit instrument it's ideal. My plan: grade each node of my DAG against its recommendations in a follow-up post.
