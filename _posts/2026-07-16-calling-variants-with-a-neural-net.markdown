---
layout: post
title: "Calling variants with a neural net"
date: 2026-07-16 06:30:00 -0500
tags: [paper]
paper:
 title: "A universal SNP and small-indel variant caller using deep neural networks (DeepVariant)"
 authors: "Poplin et al."
 venue: "Nature Biotechnology, 2018"
 link: "https://doi.org/10.1038/nbt.4235"
 verdict: "Variant calling reframed as image classification, the deep-learning alternative to GATK, and where AlexNet's lineage lands in my own pipeline."
---

**The problem.** GATK's best-practices caller (day 6) encodes hand-built statistical models of sequencing error, powerful, but each correction is a human-designed rule for a specific artefact. Could a model instead *learn* what a real variant looks like directly from data, without anyone hand-specifying the error modes?

**The idea.** DeepVariant turns each candidate site into an image: a pileup of reads stacked at that position, encoded as a tensor. A convolutional neural network, the AlexNet lineage, is then trained on truth sets (GIAB, day 8) to classify each pileup as homozygous reference, heterozygous, or homozygous variant. The error model isn't written down; it's learned from labelled examples.

**Why it matters.** This is a genuine fork for `variant_calling_nf`: GATK's explicit models versus DeepVariant's learned one. Reading it ties three threads of my reading together, deep learning (AlexNet/LeCun), the truth sets that make training possible (GIAB/Platinum), and my own calling step. It's also a clean case study in the pattern of the decade: replace hand-engineered features with a network trained on a good benchmark.

**Verdict.** Foundational for ML-based variant calling and often top of accuracy benchmarks, especially on newer chemistries. It trades interpretability for learned accuracy and needs representative training data. Read it as GATK's deep-learning counterpart, and as proof the benchmarks from day 8 were the enabling ingredient.
