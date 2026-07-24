---
layout: post
title: "Picking peaks from the noise"
date: 2026-07-17 13:00:00 -0500
tags: [paper]
paper:
 title: "XCMS: processing mass spectrometry data for metabolite profiling using nonlinear peak alignment, matching, and identification"
 authors: "Smith et al."
 venue: "Analytical Chemistry, 2006"
 link: "https://doi.org/10.1021/ac051437y"
 verdict: "The foundational preprocessing for untargeted metabolomics, turning raw LC-MS signal into aligned, comparable features. The step everything downstream assumes."
---

**The problem.** Raw LC-MS metabolomics data is a mess of noisy peaks whose retention times drift between runs. Before you can compare samples, you must detect real peaks, correct that drift so the same metabolite lines up across runs, and assemble a clean feature-by-sample table. Get this wrong and every downstream analysis is comparing apples to shifted apples.

**The idea.** XCMS performs peak detection, then *nonlinear* retention-time alignment to correct drift, then matches features across samples into a consistent table. The nonlinear alignment is the key move, drift isn't a constant offset, so a flexible warping is needed to register runs. The output is the quantitative feature matrix that tools like feature-based molecular networking (previous post) then interpret.

**Why it matters.** This is the metabolomics analogue of read alignment and QC in my sequencing pipelines, the unglamorous first step that determines whether anything after it is trustworthy. Reading it alongside GNPS completes the metabolomics workflow shape: XCMS builds the features, networking makes sense of them, exactly mirroring "align/quantify, then analyse" from the RNA and protein sides.

**Verdict.** Foundational and long-standing, XCMS remains a default for untargeted metabolomics preprocessing. An older paper, but the problem (drift, peak detection) is timeless. Read it as the metabolomics counterpart to the QC-and-quantify step I already respect on every other modality.
