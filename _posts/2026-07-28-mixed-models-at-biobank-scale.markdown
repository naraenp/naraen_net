---
layout: post
title: "Mixed models at biobank scale"
date: 2026-07-28 05:00:00 -0500
tags: [paper]
paper:
 title: "Efficient Bayesian mixed-model analysis increases association power in large cohorts (BOLT-LMM)"
 authors: "Loh et al."
 venue: "Nature Genetics, 2015"
 link: "https://doi.org/10.1038/ng.3190"
 verdict: "A mixed model that scales to hundreds of thousands of samples and gains power by letting effect sizes follow a non-Gaussian prior, not just correcting for structure."
---

**The problem.** Mixed models control for relatedness well, but the standard version assumes every variant has a tiny normal-distributed effect and it still scales poorly to the largest cohorts. Real traits are often a mix of many small effects and a few larger ones, and biobanks were reaching sample sizes where both the speed and the modeling assumption started to cost real power.

**The idea.** BOLT-LMM keeps the mixed-model correction for structure but replaces the single-Gaussian assumption on effect sizes with a two-component prior, a mixture that allows both many small effects and some larger ones. That better match to how traits are actually built raises the power to detect associations. It also uses fast iterative computation instead of the expensive matrix operations, so it runs on cohorts far larger than earlier exact methods could handle.

**Why it matters.** This is the pairing of two threads in one tool: the structure control from GEMMA and the scaling problem PLINK 1.9 addressed, plus a modeling gain on top. It became a default for large-cohort association scans. The mixture-prior idea, letting the data have both small and large effects, is the same instinct that shows up in polygenic risk scoring later in this batch.

**Verdict.** A high-impact method for large-scale association analysis. Read it for how a better effect-size prior buys power, not just speed.
