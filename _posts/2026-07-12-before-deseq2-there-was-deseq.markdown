---
layout: post
title: "Before DESeq2, there was DESeq"
date: 2026-07-12 13:40:00 -0500
tags: [paper]
paper:
  title: "Differential Expression Analysis for Sequence Count Data (DESeq)"
  authors: "Anders & Huber"
  venue: "Genome Biology, 2010"
  link: "https://doi.org/10.1186/gb-2010-11-10-r106"
  verdict: "The original of the method I use every week — the paper that got the count statistics right before DESeq2 refined them."
---

**The problem.** RNA-seq gives you *counts* of reads per gene, and counts don't behave like the continuous, normally-distributed data of the microarray era. They're discrete, and their variance grows with the mean — worse, biological replicates are overdispersed relative to a simple Poisson. Testing differential expression naively gives wildly anti-conservative results, especially for the low-count genes that dominate the table.

**The idea.** Anders and Huber model counts with the *negative binomial* distribution, which separates shot noise from biological variability. Their key move is estimating the mean-variance relationship by pooling information *across genes* — borrowing strength so that a gene with few replicates gets a sensible variance estimate instead of a noisy one. Normalization handles differing library sizes, and the NB model then gives calibrated tests.

**Why it matters.** This is the direct ancestor of DESeq2, the engine of my `aml_rnaseq_nf` pipeline. Reading the original clarifies *why* the method works — the negative binomial, the shared-information variance estimation — which is exactly the empirical-Bayes instinct that also shows up in scVI and cell2location. Same statistical idea, recurring across the whole reading list.

**Verdict.** Foundational, and worth reading even though DESeq2 (better shrinkage, the Wald test, `apeglm` LFC estimation) is what I actually run. The lineage matters: understanding the first version is understanding what the current one improved. Pairs naturally with the FDR paper from this morning — count model plus multiple-testing control is the whole DE story.
