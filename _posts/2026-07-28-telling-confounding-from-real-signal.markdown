---
layout: post
title: "Telling confounding from real signal"
date: 2026-07-28 07:00:00 -0500
tags: [paper]
paper:
 title: "LD Score regression distinguishes confounding from polygenicity in genome-wide association studies"
 authors: "Bulik-Sullivan et al."
 venue: "Nature Genetics, 2015"
 link: "https://doi.org/10.1038/ng.3211"
 verdict: "When association statistics look inflated, is it real polygenic signal or bias from structure? LD Score regression separates the two using only the summary numbers."
---

**The problem.** Genome-wide scans often show test statistics larger than expected under no association. That inflation has two very different causes. It can be true polygenic signal, many real small effects, or it can be confounding from population structure and technical bias. Telling them apart used to need the raw genotypes, which are often not shareable.

**The idea.** The method rests on a clean insight. A variant in a region of high linkage disequilibrium tags many nearby variants, so under real polygenic signal its test statistic should be larger. Confounding, by contrast, inflates everything roughly equally regardless of how much a variant tags. So regressing each variant's chi-square statistic on its LD score separates the two: the slope measures true heritable signal, and the intercept measures the flat inflation from confounding. It runs on published summary statistics alone.

**Why it matters.** This is a rare case where a simple regression answers a question that looks like it needs the full data. Working from summary statistics made it usable across studies that cannot share genotypes, which is most of them. The intercept became a standard sanity check for whether a GWAS is well controlled, the same worry PLINK and GEMMA handle at the design stage.

**Verdict.** A foundational summary-statistics method. Read it for the LD-tagging argument, which is genuinely elegant.
