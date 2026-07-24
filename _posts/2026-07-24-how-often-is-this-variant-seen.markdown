---
layout: post
title: "How often is this variant seen"
date: 2026-07-24 10:30:00 -0500
tags: [paper]
paper:
 title: "The mutational constraint spectrum quantified from variation in 141,456 humans"
 authors: "Karczewski et al."
 venue: "Nature, 2020"
 link: "https://doi.org/10.1038/s41586-020-2308-7"
 verdict: "The population frequency reference that lets a pipeline ask 'is this rare?', and ranks genes by how badly they tolerate being broken."
---

**The problem.** Most variants a pipeline calls are common and harmless. To find the few that matter, you need to know how often each one appears in the general population, and that needs a large, carefully filtered reference. Without it, every rare-looking call is a false lead.

**The idea.** gnomAD aggregates about 141,000 exomes and genomes into one filtered resource of allele frequencies. Beyond the frequencies themselves, the paper builds a model of the expected mutation rate per gene and compares it to what is actually observed. Genes seen with far fewer damaging variants than expected are under constraint, meaning that breaking them is not tolerated. This gives a per-gene score for how essential a gene is, alongside the raw frequency data.

**Why it matters.** gnomAD is the frequency database that annotation tools such as VEP and ANNOVAR query, so it is the reference behind the filtering step in `variant_calling_nf`. The constraint scores also help rank candidate genes in disease work, including which AML-relevant genes are least tolerant of loss. It turns "is this variant rare" into a number I can filter on.

**Verdict.** A reference that reshaped how variants get interpreted. It reflects the populations it sampled, so frequencies are less complete for under-represented groups. Read it as the population baseline every variant pipeline now leans on.
