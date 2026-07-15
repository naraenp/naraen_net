---
layout: post
title: "Deep learning, in one review"
date: 2026-07-14 07:45:00 -0500
tags: [paper]
paper:
  title: "Deep learning"
  authors: "LeCun, Bengio & Hinton"
  venue: "Nature, 2015"
  link: "https://doi.org/10.1038/nature14539"
  verdict: "The three architects' own summary of the field — the conceptual map behind every biology-ML paper on this list."
---

**The problem.** By 2015 deep networks had gone from fringe to dominant across vision and speech, but the ideas were scattered across a decade of conference papers. The field needed an authoritative synthesis: what actually makes deep learning work, from the people who built it.

**The idea.** LeCun, Bengio and Hinton lay out the core: representation learning through stacked layers, backpropagation as the training engine, convolutional networks for images, and recurrent networks for sequences. The unifying claim is that depth lets a model learn features at multiple levels of abstraction automatically — replacing the hand-engineering that machine learning used to require.

**Why it matters.** This is the map for the territory I keep entering in this reading list. AlphaFold2, ESM-2, scVI, Geneformer, scGPT — all of them assume the machinery this review consolidates. Reading it after AlexNet (the proof it worked) gives the conceptual vocabulary behind the biology-ML papers I actually care about: what "representation," "embedding," and "end-to-end training" mean, stated by the source.

**Verdict.** Foundational as orientation, and a clean read. It predates the transformer revolution (coming up on this list), so treat it as the pre-attention consensus — the base layer the sequence models were about to rebuild. Read it for the shared language, not the latest architectures.
