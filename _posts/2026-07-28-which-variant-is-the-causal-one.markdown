---
layout: post
title: "Which variant is the causal one"
date: 2026-07-28 08:00:00 -0500
tags: [paper]
paper:
 title: "A simple new approach to variable selection in regression, with application to genetic fine mapping (SuSiE)"
 authors: "Wang et al."
 venue: "Journal of the Royal Statistical Society: Series B, 2020"
 link: "https://doi.org/10.1111/rssb.12388"
 verdict: "A GWAS points at a region, not a variant. SuSiE fine-maps by returning credible sets, small groups that each likely contain one causal variant, honest about the ambiguity linkage creates."
---

**The problem.** An association peak covers many variants in tight linkage disequilibrium, all rising and falling together. Any one of them could be the real driver, and the rest just correlated passengers. Standard model selection struggles here: it either picks one variant with false confidence or fails to converge when several are nearly interchangeable.

**The idea.** SuSiE models the trait as a sum of a small number of single effects, each contributed by exactly one variant, and fits them with a fast iterative procedure. The useful output is not a single winner but credible sets: each set is a small group of variants that together are likely to hold one causal signal. When two variants are statistically indistinguishable, they land in the same set, which reports the uncertainty honestly instead of hiding it. It handles multiple causal signals in a region at once.

**Why it matters.** Fine-mapping is the step between a locus and a mechanism, and doing it well means admitting when linkage makes the answer ambiguous. The credible-set idea mirrors the Bayesian reasoning I have seen elsewhere in this reading, and it sets up colocalization, which asks whether two traits share one of these fine-mapped signals.

**Verdict.** A clean, widely used fine-mapping method with a general statistical core. Read it for the sum-of-single-effects idea and the honesty of credible sets.
