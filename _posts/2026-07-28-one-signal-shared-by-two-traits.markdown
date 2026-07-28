---
layout: post
title: "One signal shared by two traits"
date: 2026-07-28 09:00:00 -0500
tags: [paper]
paper:
 title: "Bayesian test for colocalisation between pairs of genetic association studies using summary statistics (coloc)"
 authors: "Giambartolomei et al."
 venue: "PLoS Genetics, 2014"
 link: "https://doi.org/10.1371/journal.pgen.1004383"
 verdict: "A GWAS peak and a gene-expression peak sit at the same place. Are they the same causal variant or two different ones nearby? Coloc answers with a probability from summary data."
---

**The problem.** A disease association often overlaps a locus that also controls a gene's expression. It is tempting to conclude the disease acts through that gene, but overlap is not sameness: the two signals could be driven by one shared causal variant, or by two distinct variants that happen to sit close together in the same linkage block. Guessing wrong points mechanism work at the wrong gene.

**The idea.** Coloc frames the question as a choice among five hypotheses for a locus: no signal, signal in only one trait, signal in both but from different variants, or one shared causal variant. Using only the summary statistics from each study, it computes the posterior probability of each. The case everyone cares about is the shared-variant hypothesis, and coloc reports how strongly the data support it. It needs no individual genotypes, only the per-variant association numbers.

**Why it matters.** This is the join between a GWAS hit and a functional readout like an eQTL, and it is the honest version of that join, since it can say the two signals are merely neighbors. It builds directly on the fine-mapping logic from SuSiE, and it is the kind of integration that turns a statistical peak into a testable biological hypothesis.

**Verdict.** A widely used, well-posed integration method. Read it for the five-hypothesis framing, which makes the ambiguity explicit.
