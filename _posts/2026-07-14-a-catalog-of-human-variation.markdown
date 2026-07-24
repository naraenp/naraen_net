---
layout: post
title: "A catalog of human variation"
date: 2026-07-14 07:00:00 -0500
tags: [paper]
paper:
 title: "A global reference for human genetic variation (1000 Genomes Project, phase 3)"
 authors: "The 1000 Genomes Project Consortium"
 venue: "Nature, 2015"
 link: "https://doi.org/10.1038/nature15393"
 verdict: "The reference panel that tells you whether a variant is common or novel, background knowledge my variant pipeline is implicitly measured against."
---

**The problem.** A variant caller tells you where a sample differs from the reference, but not whether that difference is a mundane common polymorphism or something rare and interesting. Without a population-scale catalogue of normal human variation, you can't tell signal from the ordinary churn of allele frequencies.

**The idea.** The 1000 Genomes Project sequenced thousands of individuals across many populations and assembled a map of human genetic variation, SNPs, indels, and structural variants, with allele frequencies by population. It became the reference against which "is this variant known?" and "how common is it?" get answered.

**Why it matters.** This is the frequency backdrop my `variant_calling_nf` calls live against. Annotation and filtering steps lean on panels like this (and its successors, gnomAD) to flag common variants and surface rare ones. Reading it clarifies that variant *calling* is only half the job, interpretation needs a population context, and this project built the first version of that context at scale.

**Verdict.** Foundational infrastructure, since extended by gnomAD's far larger cohorts. Read it for the design of a population reference and for the sampling caveats (which populations, which frequencies are well estimated) that quietly shape every downstream filter I run.
