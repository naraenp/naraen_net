---
layout: post
title: "An atlas of immune response"
date: 2026-07-18 14:15:00 -0500
tags: [paper]
paper:
  title: "Single-cell transcriptomic atlas of human PBMC responses to LPS"
  authors: "Erbon et al."
  venue: "Scientific Data, 2023"
  link: "https://doi.org/10.1038/s41597-023-02348-z"
  verdict: "A worked single-cell dataset of immune cells reacting to a stimulus — the biology all this day's machinery exists to read."
---

**The problem.** Methods are only worth as much as the biology they reveal. PBMCs (peripheral blood mononuclear cells) responding to LPS — a bacterial endotoxin that triggers innate immune activation — are a canonical model of a coordinated immune response. Capturing that response at single-cell resolution means seeing which cell types react, how, and along what trajectory.

**The idea.** This is a data-descriptor paper: a curated single-cell RNA-seq atlas of human PBMCs stimulated with LPS, processed and shared as a reference resource. Rather than a new algorithm, it provides the raw material — a well-annotated dataset of immune cell states and their stimulus response — for others to analyse, benchmark, and reuse.

**Why it matters.** It's the payoff for the day's toolchain: this is exactly the kind of dataset you'd run STARsolo → Scanpy QC → Harmony → SingleR → velocity/PAGA over to dissect an immune response cell-type by cell-type. PBMCs are also the workhorse of single-cell (the 10x reference datasets are PBMCs), so it grounds the abstract pipeline in a concrete, immunologically meaningful example — the kind of question the methods were built to answer.

**Verdict.** Valuable as a reference dataset more than a conceptual advance — its worth is in reuse and benchmarking. Read it as the biological anchor for the day: real immune cells, real stimulus, the substrate every method here is designed to interpret.
