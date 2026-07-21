---
layout: post
title: "Regulatory networks from single cells"
date: 2026-07-21 07:45:00 -0500
tags: [paper]
paper:
  title: "SCENIC: single-cell regulatory network inference and clustering"
  authors: "Aibar et al."
  venue: "Nature Methods, 2017"
  link: "https://doi.org/10.1038/nmeth.4463"
  verdict: "Defines cell states by the transcription-factor programs driving them, not just marker genes — inferring regulons and scoring their activity per cell, a network view of identity."
---

**The problem.** Clustering cells by raw expression groups them by correlated genes, but the biology that defines a cell state is the regulatory program behind it — which transcription factors are active and what they switch on. Two cells can look similar gene-by-gene yet be governed by different regulators, and expression noise (dropout) blurs the picture further.

**The idea.** SCENIC infers, per transcription factor, a *regulon*: the set of genes it plausibly regulates, found by co-expression (GENIE3/GRNBoost) and then filtered to keep only targets whose promoters carry the TF's binding motif (RcisTarget). AUCell then scores each regulon's activity in each cell, yielding a cells-by-regulons matrix. Clustering on that activity groups cells by shared regulatory programs, which is more robust to dropout than raw counts.

**Why it matters.** This is network biology at single-cell resolution — the same instinct as Geneformer's network framing and the human-TF catalogue from an earlier day, made operational. Motif filtering grounds the inferred edges in sequence, not correlation alone. For any lineage question, and for the STU when asking what regulatory state a spatial niche imposes, defining identity by active regulators is a deeper handle than marker genes.

**Verdict.** A field-standard for regulatory-network inference; the regulons are hypotheses bounded by motif databases and co-expression, so they warrant validation. Read it as identity redefined by the transcription factors in control.
