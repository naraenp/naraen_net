---
layout: post
title: "Linking omics through a graph"
date: 2026-07-23 09:15:00 -0500
tags: [paper]
paper:
  title: "Multi-omics single-cell data integration and regulatory inference with graph-linked embedding (GLUE)"
  authors: "Cao & Gao"
  venue: "Nature Biotechnology, 2022"
  link: "https://doi.org/10.1038/s41587-022-01284-4"
  verdict: "Integrates unpaired single-cell modalities — RNA, ATAC, methylation — by using a prior knowledge graph of regulatory links to connect their different features, and infers regulation as it goes."
---

**The problem.** Integrating single-cell RNA with ATAC or methylation is harder than integrating batches of the same modality: the feature spaces differ (genes vs. peaks vs. methylation sites), and often the cells are unpaired — measured in separate experiments. Methods that assume shared features or paired cells don't apply. You need something that can bridge fundamentally different measurement types.

**The idea.** GLUE (graph-linked unified embedding) encodes each modality with its own autoencoder into a shared latent space, and ties the modalities together through a *guidance graph* encoding prior regulatory relationships — which peaks plausibly regulate which genes, and so on. Adversarial alignment matches the modalities in latent space while the graph keeps the links biologically grounded. Because those regulatory links are explicit and refined during training, GLUE also outputs inferred regulatory interactions, scaling to millions of cells across triple-omics integration.

**Why it matters.** This is the frontier of the integration thread I've been building — from MNN and Harmony (same-modality batches) through Seurat's WNN and totalVI (paired multimodal) to GLUE (unpaired, cross-modality via prior knowledge). Folding a regulatory graph into the model connects it to the network-inference thread (SCENIC) too. For building multi-omic cell atlases, which the STU's kind of work increasingly needs, this is a key capability.

**Verdict.** A powerful, scalable cross-modality integration framework; it depends on the quality of the guidance graph and adversarial training can be finicky. Read it as single-cell integration reaching across modalities by leaning on what we already know about regulation.
