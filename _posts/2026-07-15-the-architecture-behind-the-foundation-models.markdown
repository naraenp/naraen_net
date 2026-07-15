---
layout: post
title: "The architecture behind the foundation models"
date: 2026-07-15 01:30:00 -0500
tags: [paper]
paper:
  title: "Attention Is All You Need (the Transformer)"
  authors: "Vaswani et al."
  venue: "NeurIPS (NIPS), 2017"
  link: "https://arxiv.org/abs/1706.03762"
  verdict: "The single most consequential architecture on this list — every protein and single-cell language model I've read runs on this."
---

**The problem.** Sequence models built on recurrence (RNNs, LSTMs) process tokens one after another, which is slow to train and struggles to link distant positions — the gradient has a long way to travel. For sequences where far-apart elements interact (language, and as it turns out proteins and genomes), that's a real limitation.

**The idea.** The Transformer drops recurrence entirely and relies on *self-attention*: every position attends directly to every other, weighting their relevance in one step. This makes long-range dependencies cheap to model and the whole computation parallelisable across the sequence — so training scales to enormous data and model sizes.

**Why it matters.** This is the taproot for the biology-ML papers I actually care about. ESM-2 treats proteins as language; Geneformer and scGPT treat cells as sequences of genes; Evo models genomes — all of them are Transformers. Reading the original clarifies what "attention," "tokens," and "context" mean in those papers, and *why* the foundation-model era became possible: an architecture that both captures long-range structure and scales. It's the missing piece between AlexNet (day 7) and the sequence models of days 1–2.

**Verdict.** Foundational beyond argument. Read it as the architecture underneath nearly all of modern ML-for-biology — the classics-to-frontier thread of this whole reading list runs straight through this paper.
