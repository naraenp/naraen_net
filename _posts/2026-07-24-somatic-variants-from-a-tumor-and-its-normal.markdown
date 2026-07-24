---
layout: post
title: "Somatic variants from a tumor and its normal"
date: 2026-07-24 06:00:00 -0500
tags: [paper]
paper:
 title: "VarScan 2: somatic mutation and copy number alteration discovery in cancer by exome sequencing"
 authors: "Koboldt et al."
 venue: "Genome Research, 2012"
 link: "https://doi.org/10.1101/gr.129684.111"
 verdict: "A heuristic tumor-normal caller that finds both point mutations and copy-number change from the same read pileup."
---

**The problem.** Cancer exomes carry two kinds of signal at once: point mutations that appear in the tumor but not the normal, and larger gains and losses of whole regions. Early tools handled one or the other. A lab wants both from the same data, without heavy per-site modeling that is slow to run and hard to explain.

**The idea.** VarScan 2 compares the tumor and normal read pileups position by position with straightforward rules. It classifies each site as germline, somatic, or loss of heterozygosity from the allele fractions in the two samples. For copy number, it reads the depth ratio between tumor and normal across the exome and segments it into gained and lost regions. The logic is heuristic, not a probabilistic model, which makes it fast and transparent.

**Why it matters.** VarScan 2 was a workhorse of early cancer-genome studies, including AML, so it sits close to the leukemia track I care about. Reading it next to Mutect2 and Strelka2 shows the design spread: a simple, readable rule-based caller against full statistical models. Knowing the simple one clarifies what the complex ones buy you.

**Verdict.** Foundational for cancer sequencing and still used for its copy-number output. Its heuristics make it less sensitive at very low tumor fraction than modern callers. Read it as the plain-spoken tumor-normal caller that covered both mutations and copy number.
