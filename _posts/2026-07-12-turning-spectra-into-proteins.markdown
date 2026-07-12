---
layout: post
title: "Turning spectra into proteins"
date: 2026-07-12 11:10:00 -0500
tags: [paper]
paper:
  title: "MaxQuant enables high peptide identification rates, individualized ppb-range mass accuracies and proteome-wide protein quantification"
  authors: "Cox & Mann"
  venue: "Nature Biotechnology, 2008"
  link: "https://doi.org/10.1038/nbt.1511"
  verdict: "The pipeline that made shotgun proteomics routine — the field's DESeq-equivalent, turning raw mass spectra into quantified proteins."
---

**The problem.** A mass spectrometer emits raw spectra, not proteins. Between them sits a gauntlet: calibrate masses, identify peptides, control error, roll peptides up to proteins, and *quantify* across samples — each step a source of noise. Before MaxQuant, stitching this together was bespoke and hard to reproduce.

**The idea.** MaxQuant is an integrated computational pipeline for high-resolution proteomics. It recalibrates masses to squeeze out sub-ppm accuracy, drives peptide identification with a search engine (Andromeda), applies target-decoy FDR control, and — its signature contribution — quantifies proteins across runs, later formalized as the MaxLFQ label-free algorithm. One coherent workflow from `.raw` file to a protein-by-sample matrix.

**Why it matters.** This is to proteomics what an aligner-plus-DESeq stack is to transcriptomics: the standard route from instrument output to analyzable numbers. It ties together today's other proteomics thread — Percolator-style FDR, decoy databases — into a tool people actually run, and it's the reference point behind the metabolomics/proteomics notes in my reading list.

**Verdict.** Foundational and enormously adopted, and a good model of *integration* as a contribution — the value is the reliable end-to-end pipeline, not any single clever step. Its ceiling is the usual one: opinionated defaults you must understand before trusting the output. Read it as the workhorse that made quantitative proteomics accessible.
