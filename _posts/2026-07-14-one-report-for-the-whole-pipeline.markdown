---
layout: post
title: "One report for the whole pipeline"
date: 2026-07-14 10:00:00 -0500
tags: [paper]
paper:
  title: "MultiQC: summarize analysis results for multiple tools and samples in a single report"
  authors: "Ewels et al."
  venue: "Bioinformatics, 2016"
  link: "https://doi.org/10.1093/bioinformatics/btw354"
  verdict: "The tool that turns a directory of QC logs into one readable report — the summary step I actually run at the end of both my pipelines."
---

**The problem.** A modern bioinformatics run scatters quality metrics across dozens of files: FastQC per sample, alignment stats from the aligner, duplication rates, counts summaries. Inspecting them one by one, per sample, doesn't scale — and problems (a bad lane, an outlier sample) hide in the pile.

**The idea.** MultiQC crawls an analysis directory, recognises the output formats of a long list of tools, and aggregates their metrics into a single interactive HTML report with per-sample plots. You see all samples side by side for every metric at once, so outliers jump out immediately.

**Why it matters.** This one isn't abstract — MultiQC is the reporting step in my nf-core-style `aml_rnaseq_nf` and `variant_calling_nf` pipelines. Reading the paper explains *why* it's a near-universal default: it standardises the "did this run go okay?" question across tools, which is exactly the reproducibility discipline the pipelines are built for. It's small, but it's the QC habit made frictionless.

**Verdict.** Foundational to practical workflow hygiene and ubiquitous in nf-core. Not a method so much as glue — but the right glue, and the reason I catch a bad sample before it reaches DESeq2 or GATK. Read it for how much friction good aggregation removes.
