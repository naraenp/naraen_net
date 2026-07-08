---
layout: post
title: "What DESeq2 is actually doing to my counts"
date: 2026-07-08 13:00:00 -0500
tags: [paper]
paper:
  title: "Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2"
  authors: "Love, Huber & Anders"
  venue: "Genome Biology, 2014"
  link: "https://doi.org/10.1186/s13059-014-0550-8"
  verdict: "The differential-expression engine under my own pipelines — worth reading from the inside, not just calling."
---

**The problem.** RNA-seq counts are discrete, over-dispersed, and — with two or three replicates per group — desperately under-powered per gene. Naive per-gene tests either miss real signal or drown in false positives. DESeq2 is the standard answer, and it runs inside both my bulk RNA-seq pipelines (via the pydeseq2 port), so I wanted to understand what it does to my numbers rather than trust the volcano plot.

**The idea.** Three moves. **Median-of-ratios normalization** corrects for library size *robustly*, so a handful of highly differential genes don't skew the size factors. **Empirical-Bayes dispersion shrinkage** fits a smooth mean–dispersion trend across all genes and pulls each gene's noisy dispersion estimate toward it — borrowing strength across the transcriptome to survive tiny replicate counts. **Log-fold-change shrinkage** does the same for effect sizes, pulling low-count genes' wild LFCs toward zero so the ranking isn't dominated by noise. A Wald test and Benjamini–Hochberg FDR finish it.

**Why it matters.** Reading the source changes how I present my *own* results. That "shrinkage" is why a gene with a huge raw fold change can rank *below* one with a modest, well-measured change — and being able to explain that is the difference between running a tool and understanding it. It's also a clean lesson in empirical Bayes: share information across features to stabilize per-feature estimates, an idea that recurs everywhere in genomics.

**Verdict.** Deservedly canonical, and honest about its model assumptions (negative binomial, a fitted dispersion trend that can misbehave for very low counts or unusual designs). Next time I'll annotate one of my pipeline's volcano plots with the pre- and post-shrinkage LFCs as the worked example.
