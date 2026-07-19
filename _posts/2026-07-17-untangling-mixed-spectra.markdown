---
layout: post
title: "Untangling mixed spectra"
date: 2026-07-17 14:15:00 -0500
tags: [paper]
paper:
  title: "DecoID improves identification rates in metabolomics through database-assisted MS/MS deconvolution"
  authors: "Stancliffe et al."
  venue: "Nature Methods, 2021"
  link: "https://doi.org/10.1038/s41592-021-01195-3"
  verdict: "The deconvolution step that rescues identifications from mixed metabolite spectra — the metabolomics echo of every 'separate overlapping signals' problem I've read this week."
---

**The problem.** In metabolomics MS/MS, co-eluting compounds get fragmented together, so a single spectrum is often a blend of ions from several metabolites. Trying to match that chimeric spectrum to a single database entry fails — the mixture looks like nothing in the reference, and real compounds go unidentified.

**The idea.** DecoID computationally deconvolves these mixed MS/MS spectra with help from a spectral database: it models an observed spectrum as a combination of database components plus residual, and solves for which known compounds (and how much of each) best explain the mixture. Pulling the blend apart recovers identifications that a naive one-to-one match would miss.

**Why it matters.** This is the same problem, one modality over, that I keep meeting: DIA-NN deconvolves co-eluting peptides, EmptyDrops separates ambient from real, molecular networking relates unknowns — all variations on "the measurement is a mixture; recover the components." Seeing the pattern recur across proteomics, single-cell, and metabolomics is the real lesson of this toolchain day: interference is universal, and good methods model it.

**Verdict.** A solid, focused methods contribution that meaningfully raises identification rates in untargeted metabolomics. Read it as the deconvolution capstone to the metabolomics thread — and as one more instance of modelling mixtures instead of pretending they're pure.
