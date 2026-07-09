---
layout: post
title: "Cross-checking spatial platforms against the references"
date: 2026-07-09 12:30:00 -0500
tags: [paper]
paper:
  title: "Comparison of imaging-based single-cell resolution spatial transcriptomics profiling platforms using FFPE tumor samples"
  authors: ""
  venue: "Nature Communications, 2025"
  link: "https://doi.org/10.1038/s41467-025-63414-1"
  verdict: "A tumor-focused companion benchmark that also anchors the imaging platforms against bulk, GeoMx, and multiplex IF."
---

**The problem.** Head-to-head imaging benchmarks tell you how the platforms compare *to each other*, but not whether any of them is *right*. On tumor tissue especially — heterogeneous, clinically important — you want the imaging assays checked against independent references.

**The idea.** This comparison profiles matched **FFPE tumor** samples across the imaging platforms and, unlike a pure three-way bake-off, brings in orthogonal measurements as ground-truth anchors: bulk RNA-seq for expression concordance, GeoMx (region-based) profiling, and multiplex immunofluorescence for protein-level cell identity. That lets it ask not just "which platform detects more" but "which platform *agrees* with the references, and where they systematically disagree."

**Why it matters.** The cancer-core-facility setting is the closest to where the spatial role actually lives, so a tumor-focused, reference-anchored comparison is the most directly relevant of the benchmarks. The methodological move — validate a new assay against established orthogonal ones before trusting it — is exactly the reproducibility discipline I'd bring to a facility, and it's the same instinct as benchmarking a variant caller against a truth set.

**Verdict.** Pairs with the other 2025 imaging benchmark as the "how do these assays behave on real tumors, and do they agree with what we already trust" cluster. Same honest limits — sample, panel, and version dependence — so read the two together for the *pattern* of agreement and disagreement rather than a single verdict. The reference-anchoring is what makes this one worth reading closely.
