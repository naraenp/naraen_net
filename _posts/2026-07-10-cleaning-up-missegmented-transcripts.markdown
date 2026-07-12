---
layout: post
title: "Cleaning up missegmented transcripts"
date: 2026-07-10 09:10:00 -0500
tags: [paper]
paper:
  title: "MisTIC: correcting missegmentation-induced transcript contamination"
  authors: "Yang et al."
  venue: "bioRxiv, 2025 (preprint)"
  link: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12724677/"
  verdict: "The 'even good segmentation leaks' paper — a correction layer for the contamination that survives the boundary step."
---

**The problem.** No segmentation is perfect. Transcripts from one cell get assigned to its neighbor, and the result is *contamination*: a cell's expression profile is polluted by whatever was next to it. This inflates spurious co-expression and blurs cell-type boundaries — and it persists no matter which segmenter you used.

**The idea.** MisTIC treats missegmentation as something to *detect and correct after the fact*, rather than a problem you can only solve upstream. The approach identifies transcripts likely to have been misassigned — using spatial and expression context to flag molecules that don't fit their assigned cell — and corrects the resulting contamination in the cell-by-gene matrix.

**Why it matters.** This completes the segmentation cluster: Baysor draws the boundaries, Segger tries to draw them faster, and MisTIC accepts that whatever you drew still leaks and cleans up after it. For a facility, that layered view — *and a QC step for the QC step* — is exactly the reproducibility mindset. Contamination is a quiet source of false biology; naming and correcting it is worth a slot.

**Verdict.** A 2025 preprint, so I'm holding its specific claims loosely until peer review and independent testing. Conceptually it fills a real gap. I'd want to see how much correction changes real cell-type calls — and whether it ever over-corrects genuine signal — before leaning on it. One to read closely against the manuscript.
