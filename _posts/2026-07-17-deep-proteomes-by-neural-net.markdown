---
layout: post
title: "Deep proteomes by neural net"
date: 2026-07-17 11:00:00 -0500
tags: [paper]
paper:
  title: "DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput"
  authors: "Demichev et al."
  venue: "Nature Methods, 2020"
  link: "https://doi.org/10.1038/s41592-019-0638-x"
  verdict: "The tool that made data-independent acquisition proteomics deep and high-throughput — deep learning arriving in the mass-spec workflow."
---

**The problem.** Classic proteomics (data-dependent acquisition) picks precursors to fragment one at a time, missing many peptides stochastically. Data-independent acquisition (DIA) fragments everything in wide windows — comprehensive, but the resulting spectra are a tangled mixture of co-eluting peptides that are hard to deconvolve reliably, especially at high throughput.

**The idea.** DIA-NN uses neural networks to identify and quantify peptides from these convoluted DIA spectra, with explicit interference correction to handle overlapping signals. The learned models improve both the number of confident identifications and the accuracy of quantification, making short-gradient, high-throughput DIA runs yield deep, reproducible proteomes.

**Why it matters.** This is where the deep-learning thread (AlexNet → LeCun → Transformer, days 7–9) reaches proteomics — the same "learn the pattern instead of hand-coding it" move I saw in DeepVariant, now applied to spectral deconvolution. It rounds out the proteomics tools I've read (MaxQuant, Percolator, MSFragger, MaxLFQ) with the DIA branch, which is increasingly the default for large studies.

**Verdict.** Foundational for modern high-throughput proteomics and the DIA workflow. Read it as proteomics' deep-learning inflection — and as another instance of the cross-modal pattern where a learned model replaces a hand-built one once the training data exists.
