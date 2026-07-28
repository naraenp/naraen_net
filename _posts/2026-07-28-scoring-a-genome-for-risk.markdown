---
layout: post
title: "Scoring a genome for risk"
date: 2026-07-28 10:00:00 -0500
tags: [paper]
paper:
 title: "Modeling linkage disequilibrium increases accuracy of polygenic risk scores (LDpred)"
 authors: "Vilhjálmsson et al."
 venue: "American Journal of Human Genetics, 2015"
 link: "https://doi.org/10.1016/j.ajhg.2015.09.001"
 verdict: "A polygenic score adds up many small effects into one number, but naive sums double-count correlated variants. LDpred reweights effects for linkage and improves the prediction."
---

**The problem.** A polygenic risk score sums the effect of many variants to predict a person's liability for a trait. The simplest version takes the GWAS effect sizes, thresholds by significance, and adds them up. That mishandles linkage disequilibrium: nearby variants are correlated, so their effects get counted several times, and the arbitrary significance cutoff throws away real signal sitting just below the line.

**The idea.** LDpred puts a Bayesian model over the true effect sizes and corrects the observed GWAS effects using a reference panel's linkage structure. It assumes a prior in which some fraction of variants are causal, then updates each effect given its neighbors' correlations, shrinking and reweighting so correlated variants are not double-counted. The result is a set of adjusted weights that make a more accurate score, and it uses summary statistics plus a reference panel rather than raw genotypes.

**Why it matters.** Polygenic scores are how GWAS results reach an individual prediction, and their accuracy hinges on handling linkage and the many sub-threshold effects that GCTA showed carry most of the heritability. The reference-panel dependence is the same reliance on population resources like 1000 Genomes that runs through this whole area.

**Verdict.** A key step in making polygenic scores usable. Read it for why modeling linkage, not just thresholding, is what raises accuracy.
