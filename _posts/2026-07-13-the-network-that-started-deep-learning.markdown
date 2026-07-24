---
layout: post
title: "The network that started deep learning"
date: 2026-07-13 10:45:00 -0500
tags: [paper]
paper:
 title: "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)"
 authors: "Krizhevsky, Sutskever & Hinton"
 venue: "NeurIPS (NIPS), 2012"
 link: "https://doi.org/10.1145/3065386"
 verdict: "The result that made deep learning credible, and the ancestor of every protein and single-cell model earlier in this reading list."
---

**The problem.** For decades, image classification meant hand-engineered features fed to a classifier, and progress was incremental. Neural networks were an old idea widely considered impractical at scale. The open question was whether a large, deep network could actually be trained to beat that pipeline, and whether the hardware existed to try.

**The idea.** AlexNet was a deep convolutional network trained on ImageNet's million-plus images using two GPUs, ReLU activations to speed learning, and dropout to fight overfitting. It cut the benchmark error rate dramatically, enough to end the debate. The design choices here (conv layers, ReLU, GPU training) became the template.

**Why it matters.** This is the taproot. Every model earlier in my reading, AlphaFold2, ESM-2, scVI, Geneformer, scGPT, descends from the moment deep networks started working. Reading AlexNet is reading *why* the biology-ML papers I care about were even possible: the compute and the training tricks came first, the applications followed. It grounds the foundation-model hype in a concrete origin.

**Verdict.** Foundational, full stop, arguably the most consequential ML paper of the decade. Convolutional specifics have since given way to transformers, but the lesson (scale + GPUs + the right regularisation) is the through-line to today. Read it as history that's still load-bearing.
