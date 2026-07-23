---
layout: post
title: "Significance for a gene set"
date: 2026-07-22 10:15:00 -0500
tags: [paper]
paper:
  title: "Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles (GSEA)"
  authors: "Subramanian et al."
  venue: "PNAS, 2005"
  link: "https://doi.org/10.1073/pnas.0506580102"
  verdict: "Stop staring at single-gene p-values and ask whether a whole pathway shifts coherently — the enrichment test that turned differential-expression lists into biological interpretation."
---

**The problem.** A differential-expression analysis hands you a ranked list of thousands of genes. Individually, many real effects are modest and don't clear a genome-wide threshold after multiple-testing correction, so the biology hides. Worse, a list of significant gene names isn't interpretation. What you actually want to know is whether a coherent *group* — a pathway, a regulon, a signature — moves together.

**The idea.** GSEA ranks all genes by their association with the phenotype, then walks the ranked list computing a running enrichment score that rises when it hits members of a predefined gene set and falls otherwise. A set concentrated near the top or bottom yields a high-magnitude score; significance comes from permuting sample labels. The result: pathways and signatures, not just genes, flagged as coordinately up- or down-regulated — even when no single gene is individually significant.

**Why it matters.** This is the interpretation layer that sits on top of every DE analysis I run — the step after DESeq2/edgeR/voom that says what the changes *mean* biologically. Its reliance on curated gene sets connects to the enrichment and pathway resources broadly, and the "test a set, not a point" logic echoes through to spatial and single-cell signature scoring. It reshaped how expression results are reported.

**Verdict.** A foundational, ubiquitous method; results depend on the gene-set collection and the ranking metric, and permutation choice matters. Read it as the move from significant genes to significant biology.
