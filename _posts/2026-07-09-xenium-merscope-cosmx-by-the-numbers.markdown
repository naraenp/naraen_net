---
layout: post
title: "Xenium vs. MERSCOPE vs. CosMx, by the numbers"
date: 2026-07-09 11:50:00 -0500
tags: [paper]
paper:
 title: "Systematic benchmarking of imaging spatial transcriptomics platforms in FFPE tissues"
 authors: ""
 venue: "Nature Communications, 2025"
 link: "https://doi.org/10.1038/s41467-025-64990-y"
 verdict: "The evidence base for 'given this sample, which platform?', a head-to-head on matched FFPE tissue."
---

**The problem.** The three imaging spatial platforms, 10x **Xenium**, Vizgen **MERSCOPE**, NanoString **CosMx**, all promise single-cell-resolution, in-situ transcript detection, and vendors all show their best case. The question a facility actually faces is empirical: on the *same* tissue, how do they compare on sensitivity, specificity, and cell calling?

**The idea.** A systematic head-to-head on matched FFPE samples. It compares the platforms on the metrics that decide real experiments: transcript detection sensitivity (counts per cell), specificity / background (false-positive signal), the number of cells recovered and segmentation quality, and concordance with reference measurements. It holds tissue and target genes as fixed as possible so the differences it reports are platform differences, not sample differences.

**Why it matters.** This is exactly the "which assay should we buy/run for this study?" decision a spatial core facility makes constantly, and it's the kind of standards-focused, orthogonal-comparison work that a data-and-reproducibility person can own. Reading it is how I'd form a defensible opinion instead of repeating vendor claims, and being able to say "it depends on your tissue and panel, and here's the benchmark" is the credible answer.

**Verdict.** A benchmark's value is its methodology, and the honest caveats are the usual ones: results depend on the specific tissue, panel, and software versions, and the field moves fast enough that today's ranking can shift with a chemistry update. So the durable takeaway is the *framework* for comparison, not a permanent winner. My plan: turn it into a one-page decision guide, updated as chemistries change.
