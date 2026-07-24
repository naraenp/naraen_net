---
layout: post
title: "One fast caller for germline and somatic"
date: 2026-07-24 04:00:00 -0500
tags: [paper]
paper:
 title: "Strelka2: fast and accurate calling of germline and somatic variants"
 authors: "Kim et al."
 venue: "Nature Methods, 2018"
 link: "https://doi.org/10.1038/s41592-018-0051-x"
 verdict: "Learns each sample's indel-error rate and calls fast, covering both germline and tumor-normal work in one tool."
---

**The problem.** Calling small variants has to fight the sequencer's own error pattern, and indels are the hardest part, since each sample and each context makes errors at a different rate. A fixed error assumption either misses real indels or lets false ones through. Speed matters too, because clinical and cohort work runs many genomes.

**The idea.** Strelka2 estimates the indel-error rate from each sample instead of assuming one. It uses a tiered strategy: an efficient first pass handles the easy sites, and a fuller haplotype model handles the hard ones. The same engine runs in two modes, a germline mode for a single sample and a somatic mode for a tumor paired with its matched normal, with a contamination model for the somatic case.

**Why it matters.** This is the fast, modern counterpart to the callers already in my reading: GATK for germline, MuTect for somatic. Strelka2 folds both jobs into one tool and runs quickly, which is what a facility wants when the genome count climbs. Its per-sample error model is the same "measure the noise, do not assume it" idea that runs through DESeq2 and GATK's recalibration.

**Verdict.** A fast, accurate caller that earned its place in production pipelines. It leans on a good matched normal for somatic calls and, like any caller, needs sensible filtering. Read it as germline and somatic calling under one efficient roof.
