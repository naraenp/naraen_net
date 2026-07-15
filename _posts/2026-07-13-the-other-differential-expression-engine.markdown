---
layout: post
title: "The other differential-expression engine"
date: 2026-07-13 07:00:00 -0500
tags: [paper]
paper:
  title: "edgeR: a Bioconductor package for differential expression analysis of digital gene expression data"
  authors: "Robinson, McCarthy & Smyth"
  venue: "Bioinformatics, 2010"
  link: "https://doi.org/10.1093/bioinformatics/btp616"
  verdict: "The negative-binomial DE method I could have used instead of DESeq2 — same problem, a different flavour of shrinkage, and the reason it's worth knowing both."
---

**The problem.** Like DESeq, edgeR faces the fact that RNA-seq counts are discrete and overdispersed, and that most experiments have too few replicates to estimate each gene's variance on its own. Test naively and the low-count genes — the bulk of the table — throw false positives.

**The idea.** edgeR also uses the negative binomial, but its signature is *empirical-Bayes moderation of the dispersion*: it estimates a common trend across all genes, then shrinks each gene's noisy per-gene estimate toward it. The exact test (and later the GLM/quasi-likelihood framework) then gives calibrated p-values even from two or three replicates.

**Why it matters.** This is the sibling of DESeq2, the engine of my `aml_rnaseq_nf` pipeline. Reading edgeR next to yesterday's DESeq paper sharpens the point that the two dominant DE toolkits agree on the count model and differ mainly in *how they borrow strength* — trended dispersions here, fitted mean-variance shrinkage there. Knowing both is knowing the design space, not just one button.

**Verdict.** Foundational and still actively used — edgeR and DESeq2 remain the two default choices a decade on. Read it as the other half of a comparison, not a competitor to pick a winner from. Pairs directly with DESeq and the FDR paper.
