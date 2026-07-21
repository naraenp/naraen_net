---
layout: post
title: "A workbench for spatial data"
date: 2026-07-20 10:40:00 -0500
tags: [paper]
paper:
  title: "Giotto: a toolbox for integrative analysis and visualization of spatial expression data"
  authors: "Dries et al."
  venue: "Genome Biology, 2021"
  link: "https://doi.org/10.1186/s13059-021-02286-2"
  verdict: "An end-to-end, platform-agnostic toolbox for spatial data — domains, spatial genes, cell-cell interactions, and visualization in one place, the spatial analogue of SCANPY or Seurat."
---

**The problem.** Spatial analysis had become a scatter of single-purpose scripts: one tool to find spatial domains, another for spatially variable genes, another for neighbourhood interactions, each with its own data format. Practitioners needed a coherent workbench — one object model, one set of interoperable steps — that worked across the many spatial platforms rather than locking to one.

**The idea.** Giotto is a comprehensive toolbox spanning the spatial workflow: preprocessing, clustering, spatial-domain detection, spatially variable gene identification, cell-neighbourhood and interaction analysis, and rich visualization — all on a common data structure and deliberately platform-agnostic, from spot-based to imaging-based data. It aims to be the general-purpose environment for spatial expression, not a single algorithm.

**Why it matters.** This is infrastructure, and infrastructure is what decides whether an analysis is reproducible — the same reason nf-core and the pipeline day mattered. Giotto sits alongside Squidpy and SpatialData in the STU reading as a candidate backbone; choosing the environment shapes everything built on top. It's the spatial counterpart to the SCANPY/Seurat ecosystems that anchored the single-cell days.

**Verdict.** A broad, widely-adopted framework; breadth means any single module may be bettered by a specialist tool, and the ecosystem moves fast. Read it as the spatial workbench — the environment the individual methods from this week plug into.
