---
layout: post
title: "Counting proteins without labels"
date: 2026-07-13 13:00:00 -0500
tags: [paper]
paper:
  title: "Accurate proteome-wide label-free quantification by delayed normalization and maximal peptide ratio extraction (MaxLFQ)"
  authors: "Cox et al."
  venue: "Molecular & Cellular Proteomics, 2014"
  link: "https://doi.org/10.1074/mcp.M113.031591"
  verdict: "The quantification algorithm that let you compare proteomes without chemical labels — the DESeq-equivalent problem, one field over."
---

**The problem.** To compare protein abundance across samples by mass spectrometry, the reliable route was chemical labelling (isotope tags), which is costly and limits sample number. Label-free quantification is cheaper and unlimited, but naive intensity comparison is noisy: run-to-run variation and missing values wreck the ratios you actually want.

**The idea.** MaxLFQ, built into MaxQuant, computes relative abundances from pairwise peptide ratios — extracting the maximum reliable ratio information across samples — and defers normalisation so it doesn't distort those ratios. The result is label-free quantities accurate enough to stand in for labelled methods across large sample sets.

**Why it matters.** This is the proteomics analogue of the count-normalisation problem I know from RNA-seq: how do you make abundances comparable across runs of differing total signal? Seeing DESeq's "model the systematic variation" instinct reappear in mass spec — different data, same discipline — is exactly the cross-modality pattern this reading list keeps surfacing. Proteomics has its own version of every RNA-seq problem.

**Verdict.** Foundational for quantitative proteomics and still the standard label-free approach. Read it right after MaxQuant (yesterday) — identification then quantification — and note how much it rhymes with the DE normalisation I already do on the RNA side.
