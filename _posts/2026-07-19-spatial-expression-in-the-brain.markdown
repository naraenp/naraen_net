---
layout: post
title: "Spatial expression in the brain"
date: 2026-07-19 02:10:00 -0500
tags: [paper]
paper:
 title: "Transcriptome-scale spatial gene expression in the human dorsolateral prefrontal cortex (Visium DLPFC)"
 authors: "Maynard et al."
 venue: "Nature Neuroscience, 2021"
 link: "https://doi.org/10.1038/s41593-020-00787-0"
 verdict: "The benchmark spatial dataset, layered human cortex mapped with Visium, and the reference nearly every spatial-domain method is tested on."
---

**The problem.** The human dorsolateral prefrontal cortex has a clear laminar structure, cortical layers with distinct molecular identities. Recovering those layers *de novo* from spatial transcriptomics is an ideal test of whether a method can detect real spatial domains, because there's a known ground-truth anatomy to check against. But you need a carefully annotated dataset to serve as that benchmark.

**The idea.** Maynard and colleagues profiled DLPFC sections with 10x Visium (the commercial descendant of Ståhl), manually annotated the cortical layers and white matter, and released it as a reference. It's both a biological study of cortical spatial expression and, more consequentially for the field, a gold-standard labelled dataset for benchmarking spatial-domain detection.

**Why it matters.** This is the spatial equivalent of the `airway` or PBMC datasets: the labelled benchmark that spatial-clustering and domain methods (BANKSY from day 4, SpaGCN later today) are validated on. For STU work it's doubly relevant, a Visium dataset with trustworthy layer annotations is exactly what you reach for to test whether a domain-finding tool actually recovers known biology. I've almost certainly seen figures built on it.

**Verdict.** Foundational as a benchmark resource; its layered cortex is a recurring proving ground. Read it to know the dataset behind the spatial-domain comparisons, and as a model of pairing real biology with reusable ground truth.
