---
layout: post
title: "Bias-aware transcript quantification"
date: 2026-07-15 00:40:00 -0500
tags: [paper]
paper:
  title: "Salmon provides fast and bias-aware quantification of transcript expression"
  authors: "Patro et al."
  venue: "Nature Methods, 2017"
  link: "https://doi.org/10.1038/nmeth.4197"
  verdict: "kallisto's cousin, with explicit bias correction — the quantifier I'd reach for when the systematic artefacts actually matter."
---

**The problem.** Fast pseudoalignment (kallisto, yesterday) gives you transcript abundances cheaply, but RNA-seq has systematic biases — GC content, fragment-length distribution, positional and sequence-specific effects from library prep — that distort counts. Ignore them and your abundances carry reproducible errors that no amount of replication removes.

**The idea.** Salmon combines fast (quasi-)mapping with an explicit statistical model of these biases, learned from the data, inside its abundance estimation. It corrects for GC and sequence-specific effects while retaining the speed advantage of alignment-free methods. The output is transcript-level estimates that are both fast to compute and debiased.

**Why it matters.** For `aml_rnaseq_nf`, Salmon is the third option next to STAR-then-count and kallisto — and the one that takes library artefacts seriously. Reading it alongside kallisto sharpens the choice: same alignment-free speed, but with a bias model that can matter for cross-sample comparisons. It's the same "model the systematic error rather than ignore it" discipline I keep meeting, from DESeq to MaxLFQ, now in quantification.

**Verdict.** Foundational and a very common default; pairs with `tximport` into DESeq2. Read it for the bias-modelling — the reminder that "fast" and "unbiased" are separate properties, and good tools chase both.
