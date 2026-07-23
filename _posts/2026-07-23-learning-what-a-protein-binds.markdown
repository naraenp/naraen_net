---
layout: post
title: "Learning what a protein binds"
date: 2026-07-23 02:30:00 -0500
tags: [paper]
paper:
  title: "Predicting the sequence specificities of DNA- and RNA-binding proteins by deep learning (DeepBind)"
  authors: "Alipanahi et al."
  venue: "Nature Biotechnology, 2015"
  link: "https://doi.org/10.1038/nbt.3300"
  verdict: "One of the first convolutional nets aimed at regulatory genomics — learning binding specificities directly from sequence, and showing deep learning could read the genome's grammar."
---

**The problem.** A transcription factor or RNA-binding protein prefers certain sequence motifs, but the classic representation — a position weight matrix — is rigid: it assumes independence between positions and struggles with the messy, context-dependent reality of binding. Meanwhile experimental data (protein binding microarrays, ChIP, CLIP) was piling up. Could a model learn specificity from that data without hand-built motif assumptions?

**The idea.** DeepBind trains a convolutional neural network on sequences labeled by binding, letting convolutional filters learn motif-like detectors and downstream layers combine them nonlinearly. One unified architecture handles diverse assay types, trains on millions of sequences, and — notably — generalizes from in vitro training data to in vivo prediction. It even scores how single-nucleotide variants perturb binding, connecting sequence changes to regulatory consequence.

**Why it matters.** This is where deep learning entered regulatory genomics, the bridge from the AlexNet CNN moment I read about to biological sequence — and the direct ancestor of DeepSEA and Enformer (today's next reads). The variant-effect scoring foreshadows how ML now interprets noncoding mutations, a question my variant pipelines raise but classic annotation (SnpEff) answers only crudely.

**Verdict.** A foundational proof-of-concept, now surpassed by deeper and longer-context models; CNN motif detectors are interpretable but limited in range. Read it as the paper that showed the genome's regulatory code is learnable from sequence.
