---
layout: post
title: "Two recipes for a single-cell foundation model"
date: 2026-07-08 11:10:00 -0500
tags: [paper]
paper:
  title: "scGPT: toward building a foundation model for single-cell multi-omics using generative AI"
  authors: "Cui et al."
  venue: "Nature Methods, 2024"
  link: "https://doi.org/10.1038/s41592-024-02201-0"
  verdict: "The generative-pretraining take on single cells — same ambition as Geneformer, different recipe, and a good head-to-head."
---

**The problem.** If Geneformer showed pretraining *can* work for single cells, the next question is *how* — what objective, what tokenization, and does the design choice change which tasks benefit?

**The idea.** scGPT pretrains a generative transformer on 33 million+ human cells (from CELLxGENE). Where Geneformer ranks genes, scGPT bins expression *values* into tokens and trains with a generative, masked-attention objective adapted for the fact that genes aren't a sequence — the model predicts held-out expression from the rest of the cell. One backbone then serves cell-type annotation, batch integration, multi-omic integration (RNA + ATAC + protein), perturbation-response prediction, and gene-network inference.

**Why it matters.** Read back-to-back with Geneformer, this is the clean comparison: **rank encoding + masked-rank objective** vs. **value binning + generative objective**, both at ~30M cells. That contrast is the useful part — it isolates what the pretraining *recipe* buys you, separate from just "more data." For someone who works with both LLMs and single-cell data, it's the clearest bridge between the two: the same generative-pretraining idea, ported to a genes-per-cell matrix.

**Verdict.** Impressive scope, and I'll believe the multi-omic and perturbation results are the most genuinely new. But the skeptic's read still applies: independent benchmarks have found single-cell FMs matching but not clearly beating scVI-class methods on core tasks, and results can be sensitive to fine-tuning and preprocessing. My takeaway isn't "which model wins" but "which *tasks* actually need a foundation model" — and that answer is still being written.
