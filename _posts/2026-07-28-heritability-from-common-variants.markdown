---
layout: post
title: "Heritability from common variants"
date: 2026-07-28 06:00:00 -0500
tags: [paper]
paper:
 title: "GCTA: a tool for genome-wide complex trait analysis"
 authors: "Yang et al."
 venue: "American Journal of Human Genetics, 2011"
 link: "https://doi.org/10.1016/j.ajhg.2010.11.011"
 verdict: "Instead of asking which variants are significant, ask how much of a trait all common variants explain together. GCTA turned the missing-heritability debate into a measurement."
---

**The problem.** Early genome-wide scans found real associations, but the significant variants together explained only a small slice of the heritability that twin studies implied. This gap, called missing heritability, had two readings: either the rest is rare variants and other mechanisms, or it is spread across many common variants each too weak to reach significance one at a time.

**The idea.** GCTA estimates how much trait variance all the genotyped common variants explain jointly, without asking any single one to be significant. It builds a genetic relatedness matrix across unrelated people and fits a mixed model that treats the total genetic contribution as a variance component. The method, often called GREML, gives a number: the share of variance captured by common variants as a whole. Applied to height and other traits, it showed much of the missing heritability was simply hiding in many small common effects.

**Why it matters.** This reframes what a GWAS is measuring. It reuses the relatedness matrix from the mixed-model papers, but points it at estimation rather than testing. Understanding this is what keeps you from reading a short list of hits as the whole genetic story, since most of the signal is spread thin below the significance line.

**Verdict.** A field-shaping method that made polygenicity quantitative. Read it as the answer to where the missing heritability went.
