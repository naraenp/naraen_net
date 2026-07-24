---
layout: post
title: "Cleaning reads before anything else"
date: 2026-07-15 02:30:00 -0500
tags: [paper]
paper:
 title: "fastp: an ultra-fast all-in-one FASTQ preprocessor"
 authors: "Chen et al."
 venue: "Bioinformatics, 2018"
 link: "https://doi.org/10.1093/bioinformatics/bty560"
 verdict: "The first step in almost every run I do, adapter trimming, quality filtering and QC in one fast pass over the FASTQs."
---

**The problem.** Raw sequencing reads carry adapter contamination, low-quality tails, and other artefacts. Historically you chained several tools, one to trim adapters, one to filter by quality, one (FastQC) to report, each re-reading the whole file. It works, but it's slow and fiddly, and it's the very first thing standing between raw data and analysis.

**The idea.** fastp does adapter trimming, quality filtering, read pruning, and quality reporting in a single multi-threaded pass over the FASTQ, with sensible auto-detection (including adapters) and a built-in before/after QC report. One fast tool replaces a small pipeline of them.

**Why it matters.** This is the literal first step of both `aml_rnaseq_nf` and `variant_calling_nf`, garbage in, garbage out, so read cleaning gates everything downstream. Reading the paper is a reminder that pipeline quality starts before alignment: a bad adapter-trim quietly corrupts every count and every variant call after it. fastp's popularity is the same story as MultiQC, the right tool removing friction from a step you must not skip.

**Verdict.** Foundational to practical workflows and a near-universal default; its speed is the point at scale. Not glamorous, but it's the hygiene step everything else depends on. Read it for what good preprocessing actually checks for.
