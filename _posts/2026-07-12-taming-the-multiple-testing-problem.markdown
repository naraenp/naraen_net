---
layout: post
title: "Taming the multiple-testing problem"
date: 2026-07-12 07:00:00 -0500
tags: [paper]
paper:
 title: "Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing"
 authors: "Benjamini & Hochberg"
 venue: "J. Royal Statistical Society B, 1995"
 link: "https://doi.org/10.1111/j.2517-6161.1995.tb02031.x"
 verdict: "The statistical idea that makes genomics possible, every 'adjusted p-value' in my differential-expression output is this paper doing its job."
---

**The problem.** Test one hypothesis at p < 0.05 and you accept a 5% chance of a false positive. Test 20,000 genes at once and you'd expect a thousand false positives by chance alone. The old fix, Bonferroni, controlling the chance of *any* false positive, is so conservative on genome-scale data that it throws away nearly every real signal.

**The idea.** Benjamini and Hochberg reframe the goal. Instead of controlling the probability of a single false positive (family-wise error), control the *expected proportion of false positives among the things you call significant*, the false discovery rate. Their procedure is almost trivially simple: rank the p-values, and find the largest one that still clears a step-up threshold. You tolerate some false positives, but you know roughly what fraction, and you keep far more real discoveries.

**Why it matters.** This is the statistical backbone of my RNA-seq work. DESeq2 reports BH-adjusted p-values; every volcano plot I've made draws its significance line here. FDR is the honest answer to "how much of this list do I believe?", and getting multiple testing right is table stakes for any pipeline I'd defend.

**Verdict.** Foundational and elegantly practical, one of those rare stats papers whose method you can do by hand and whose logic reshaped a whole field. Its assumptions (independence or particular dependence structures) matter, which is why later variants exist, but BH remains the default for good reason.
