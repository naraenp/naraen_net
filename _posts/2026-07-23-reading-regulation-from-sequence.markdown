---
layout: post
title: "Reading regulation from sequence"
date: 2026-07-23 03:15:00 -0500
tags: [paper]
paper:
 title: "Predicting effects of noncoding variants with deep learning–based sequence model (DeepSEA)"
 authors: "Zhou & Troyanskaya"
 venue: "Nature Methods, 2015"
 link: "https://doi.org/10.1038/nmeth.3547"
 verdict: "Predicts chromatin state, TF binding, DNase sensitivity, histone marks, straight from DNA sequence at single-base resolution, then scores how noncoding variants shift it."
---

**The problem.** Most disease-associated variants from GWAS fall in noncoding regions, where their effect is regulatory and invisible to protein-centric annotation. Predicting whether a base change disrupts a regulatory element requires understanding the sequence determinants of chromatin, TF occupancy, accessibility, histone modification, across many cell types. That's a lot of context to learn from sequence alone.

**The idea.** DeepSEA trains a deep convolutional network to predict hundreds of chromatin features (from ENCODE-style profiling) directly from a window of DNA sequence, learning a regulatory-sequence code with single-nucleotide sensitivity. To score a variant, it predicts chromatin state for the reference and alternate alleles and takes the difference, a quantitative prediction of regulatory disruption that improves prioritization of functional eQTLs and disease variants.

**Why it matters.** DeepSEA extends DeepBind (today's first read) from single-protein specificity to genome-wide chromatin state, and it leans on the ENCODE catalogue I read earlier as training signal. It's the direct predecessor of Enformer (next), and it addresses the exact gap my variant pipelines hit: SnpEff tells me a variant is "intergenic," DeepSEA estimates whether it actually breaks regulation. That's the noncoding-interpretation frontier.

**Verdict.** A foundational sequence-to-chromatin model; its context window is short by today's standards and predictions are correlative, needing experimental follow-up. Read it as the step that made noncoding variants computationally interpretable.
