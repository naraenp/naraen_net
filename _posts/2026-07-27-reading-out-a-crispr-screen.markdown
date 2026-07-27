---
layout: post
title: "Reading out a CRISPR screen"
date: 2026-07-27 08:00:00 -0500
tags: [paper]
paper:
 title: "MAGeCK enables robust identification of essential genes from genome-scale CRISPR-Cas9 knockout screens"
 authors: "Li et al."
 venue: "Genome Biology, 2014"
 link: "https://doi.org/10.1186/s13059-014-0554-4"
 verdict: "A screen is only as good as the count analysis behind it. MAGeCK models guide counts and ranks the genes whose loss actually shifted the population."
---

**The problem.** A pooled screen ends as a table of guide RNA counts before and after selection. Turning that into a trustworthy list of hit genes is harder than it looks: each gene has several guides that disagree, counts are noisy at low depth, and you need genes, not guides, as the final answer. Naive fold-change ranking gives false hits.

**The idea.** MAGeCK models the guide counts with a negative binomial distribution, the same family used for RNA-seq counts, then normalizes and tests each guide for enrichment or depletion. It aggregates a gene's guides with a robust rank method, so one noisy guide does not sink or inflate a gene, and reports genes ranked by how consistently their guides moved. It handles both positive-selection and dropout screens.

**Why it matters.** This is the analysis half of the screen story, and it sits squarely in my own stack. The negative binomial and the multiple-testing care are the exact tools I use for differential expression in `aml_rnaseq_nf` with DESeq2 and edgeR, reused here for guide counts. Seeing the same statistics carry across assays is the point.

**Verdict.** The standard analysis method for pooled CRISPR screens, and open access. Read it right after GeCKO to close the loop from design to called genes.
