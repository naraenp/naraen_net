---
layout: post
title: "Spatial genes at scale"
date: 2026-07-23 07:45:00 -0500
tags: [paper]
paper:
  title: "nnSVG for the scalable identification of spatially variable genes using nearest-neighbor Gaussian processes"
  authors: "Weber et al."
  venue: "Nature Communications, 2023"
  link: "https://doi.org/10.1038/s41467-023-39748-z"
  verdict: "Finds genes whose expression varies across tissue space, but scales linearly to modern datasets — nearest-neighbor Gaussian processes making spatially-variable-gene detection practical at Visium/Xenium scale."
---

**The problem.** A core spatial question is which genes show spatial structure — expression patterns that track tissue anatomy rather than scattering randomly. Gaussian processes model this elegantly, but exact GP inference scales cubically with the number of locations, so it chokes on the tens of thousands of spots or cells that platforms like Visium and imaging methods now produce. Earlier tools (SpatialDE, and today's SPARK) either didn't scale or made stronger assumptions.

**The idea.** nnSVG replaces the full Gaussian process with a *nearest-neighbor* Gaussian process, which approximates the covariance using only each location's nearest neighbours. That drops the cost to scale linearly in the number of spatial locations, so per-gene spatial models fit across whole modern datasets. It also allows gene-specific length scales — different genes can vary smoothly or sharply — and ranks spatially variable genes within a slide or within defined domains.

**Why it matters.** This continues the spatially-variable-gene thread from SpatialDE (which I read on the spatial day) and sits beside SPARK (today's next read) as the scalable member of that family. Scalability is the recurring enabler across my reading — the same reason minimap2 and MMseqs2 mattered. For the STU's large imaging datasets, a linear-time spatial test is what makes the analysis run at all.

**Verdict.** A widely-used, scalable SVG method; the nearest-neighbour approximation trades a little exactness for tractability, and results depend on preprocessing. Read it as spatially-variable-gene detection built to survive dataset size.
