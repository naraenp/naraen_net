---
layout: post
title: "A Bayesian take on variant calling"
date: 2026-07-24 03:00:00 -0500
tags: [paper]
paper:
 title: "Haplotype-based variant detection from short-read sequencing"
 authors: "Garrison & Marth"
 venue: "arXiv, 2012"
 link: "https://doi.org/10.48550/arXiv.1207.3907"
 verdict: "Calls variants as haplotypes under one Bayesian model and handles any copy number, which is why it stays a common alternative to GATK."
---

**The problem.** A variant caller has to weigh noisy reads and decide which differences from the reference are real. Many early callers looked at one base at a time. That misses the fact that nearby changes travel together on the same DNA molecule. It also assumes two copies at every site, which fails for pooled samples or non-diploid regions.

**The idea.** FreeBayes models short haplotypes, the actual sequences the reads support over a small window, rather than isolated bases. It puts these under one Bayesian model that estimates genotypes across a set of samples at once, and it allows any copy number instead of assuming two. The output is a posterior probability for each call, so the confidence comes from the model, not a hand-tuned score.

**Why it matters.** FreeBayes is the haplotype-based cousin of GATK's HaplotypeCaller, and knowing both shows the shared idea: assemble the local sequence, then genotype. It is a caller I can drop into `variant_calling_nf` when I want a second opinion next to GATK. The copy-number flexibility also makes it useful for pooled or somatic settings where the two-copy assumption breaks.

**Verdict.** A widely used, open caller with a clean statistical core. It can be slower and needs good filtering afterward, but the model is easy to reason about. Read it next to GATK as the other way to call haplotypes.
