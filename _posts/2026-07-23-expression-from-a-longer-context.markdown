---
layout: post
title: "Expression from a longer context"
date: 2026-07-23 04:00:00 -0500
tags: [paper]
paper:
  title: "Effective gene expression prediction from sequence by integrating long-range interactions (Enformer)"
  authors: "Avsec et al."
  venue: "Nature Methods, 2021"
  link: "https://doi.org/10.1038/s41592-021-01252-x"
  verdict: "Brings the transformer's long-range attention to regulatory genomics — predicting expression and chromatin from up to 100 kb of sequence, capturing enhancers that act far from their genes."
---

**The problem.** Regulation is long-range: enhancers can sit tens of kilobases from the gene they control. Convolutional models like DeepSEA see only a short window, so they miss distal regulatory interactions — precisely the ones that explain much of gene-expression variation and many noncoding variant effects. You need a model whose receptive field spans the regulatory neighbourhood.

**The idea.** Enformer replaces deep convolutions' limited range with transformer self-attention, letting the model integrate information across ~100 kb of DNA. Trained to predict thousands of genomic tracks (expression, chromatin, TF binding) from sequence, its attention can link a gene to distant enhancers. The longer context substantially improves expression prediction and, importantly, sharpens variant-effect prediction and enhancer–gene assignment over shorter-range predecessors.

**Why it matters.** This is the Transformer — the architecture I read about in the attention paper — arriving in regulatory genomics, the third step in today's DeepBind → DeepSEA → Enformer arc from short motifs to genome-scale context. It's also the lineage that leads to DNA foundation models (Evo, on my earlier list). For interpreting the noncoding variants my pipelines produce, long-range context is what makes the predictions credible.

**Verdict.** A landmark sequence model, influential and widely benchmarked; it's still correlative, computationally heavy, and imperfect on truly long-range or cell-type-specific effects. Read it as attention giving genomics the long context regulation actually uses.
