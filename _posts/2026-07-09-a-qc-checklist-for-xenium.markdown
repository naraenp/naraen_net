---
layout: post
title: "A QC checklist for Xenium"
date: 2026-07-09 13:10:00 -0500
tags: [paper]
paper:
  title: "Optimizing Xenium In Situ data utility by quality assessment and best-practice analysis workflows"
  authors: ""
  venue: "Nature Methods, 2025"
  link: "https://doi.org/10.1038/s41592-025-02617-2"
  verdict: "An independent, end-to-end QC and best-practice workflow for Xenium — the 'how I'd analyze this dataset' sketch, made real."
---

**The problem.** Vendor pipelines get you from a Xenium run to a cell-by-gene matrix, but they don't tell you whether to *trust* it, or what to check before analysis. This paper is the independent best-practice workflow — the QC discipline a facility needs and vendors under-specify.

**The idea.** It lays out quality assessment and an analysis workflow specific to Xenium in-situ data: evaluating transcript detection and background, assessing **segmentation** quality (the step where transcripts get assigned to cells — the dominant error source in imaging assays), filtering low-quality cells, and the normalization/clustering/annotation choices that follow, with the pitfalls called out at each stage. The through-line is that imaging-assay QC is *different* from sequencing-assay QC, because the failure modes (missegmentation, transcript misassignment, optical crowding) are different.

**Why it matters.** This is the paper I'd turn into a personal one-page workflow — "here's how I'd analyze a Xenium dataset end to end, and here's what I'd QC first." That deliverable is precisely what a spatial core facility values: a reproducible, defensible pipeline with the checks made explicit. It also reinforces that segmentation is the make-or-break step, which is where the next two days of the reading list are headed.

**Verdict.** Being platform-specific (Xenium) is both its strength and its ceiling — the QC principles generalize, but the specifics won't all transfer to MERSCOPE or CosMx, and chemistry updates will move details. Read it for the *workflow skeleton* and the QC mindset, then adapt. My plan: reproduce its checklist on a public Xenium dataset and post the worked version.
