---
layout: post
title: "Which deconvolution tool should you trust?"
date: 2026-07-09 13:45:00 -0500
tags: [paper]
paper:
 title: "A comprehensive benchmarking with practical guidelines for cellular deconvolution of spatial transcriptomics"
 authors: "Li et al."
 venue: "Nature Communications, 2023"
 link: "https://doi.org/10.1038/s41467-023-37168-7"
 verdict: "The benchmark behind the folk wisdom that cell2location, RCTD, and CARD tend to win, with guidelines, not just a ranking."
---

**The problem.** Spot-based assays like Visium capture several cells per spot, so nearly every downstream question depends on **deconvolution**, estimating the cell-type mixture inside each spot from a single-cell reference. There are a dozen methods and strong opinions; this paper asks which actually hold up, and when.

**The idea.** A systematic benchmark of spatial-deconvolution methods across simulated and real datasets, scoring accuracy against known or reference-derived mixtures and varying the conditions that matter, reference quality, number of cell types, spot resolution, and platform. The recurring result behind the field's folk wisdom is that a handful of methods (notably **cell2location**, **RCTD**, and **CARD**) tend to lead, but the more useful contribution is the **practical guidelines**: which method to reach for given your reference, resolution, and tissue.

**Why it matters.** Deconvolution is the single most load-bearing step for spot assays, so a standards-minded facility prizes exactly this kind of method-evaluation, not "here's a new tool" but "here's which existing tool to trust, and under what conditions." Being able to point to a benchmark rather than a preference is the difference between an opinion and a recommendation, and it's the same evaluation discipline I'd apply to any pipeline component.

**Verdict.** The strongest kind of paper for practical work: it evaluates rather than advocates, and gives conditional guidance instead of a single winner. The honest caveat is that benchmark rankings depend on the simulation and reference choices, and imaging assays (single-cell resolution) shift the problem from deconvolution to segmentation. Read it as the decision guide for Visium-style data, paired with the cell2location and RCTD method papers.
