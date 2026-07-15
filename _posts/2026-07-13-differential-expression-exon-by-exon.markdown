---
layout: post
title: "Differential expression, exon by exon"
date: 2026-07-13 08:30:00 -0500
tags: [paper]
paper:
  title: "Conservation of an RNA regulatory map between Drosophila and mammals"
  authors: "Brooks et al."
  venue: "Genome Research, 2011"
  link: "https://doi.org/10.1101/gr.108662.110"
  verdict: "The pasilla study — better known now as the dataset behind DEXSeq than for its biology, and a reminder that a gene can change without changing its total count."
---

**The problem.** Standard differential-expression asks whether a *gene* goes up or down. But regulation often happens at finer grain: a splicing factor can shift which exons are included while leaving total transcript output roughly flat. Gene-level counting is blind to that.

**The idea.** Brooks and colleagues knocked down the splicing regulator pasilla in Drosophila and used RNA-seq to map differential *exon usage* — testing each exon's inclusion relative to its gene, rather than summing the gene. This exposed a conserved regulatory map of alternative splicing that gene-level analysis would have missed entirely.

**Why it matters.** The pasilla dataset became the canonical example for DEXSeq and exon-level analysis, so it's one I'll meet the moment I move beyond gene-level DESeq2 in `aml_rnaseq_nf`. Conceptually it's a useful widening of the lens: the same negative-binomial machinery I already use, re-pointed from genes to exons. The statistics carry over; the question changes.

**Verdict.** Foundational for splicing analysis and quietly ubiquitous as a teaching dataset. Read it to internalise that "no change in expression" and "no change in isoform" are different claims — and that my current pipeline only answers the first.
