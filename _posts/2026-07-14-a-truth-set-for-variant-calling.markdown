---
layout: post
title: "A truth set for variant calling"
date: 2026-07-14 12:15:00 -0500
tags: [paper]
paper:
  title: "Extensive sequencing of seven human genomes to characterize benchmark reference materials (GIAB)"
  authors: "Zook et al."
  venue: "Scientific Data, 2016"
  link: "https://doi.org/10.1038/sdata.2016.25"
  verdict: "The answer key — how you actually know whether a variant caller is right. The benchmark my pipeline should be measured against."
---

**The problem.** You can run GATK and get a VCF, but how do you know it's *correct*? Variant calling has no ground truth in a typical sample — you can't independently confirm millions of calls. Without a trusted reference set of high-confidence variants and the regions where you can trust them, benchmarking a caller is guesswork.

**The idea.** Genome in a Bottle sequenced reference samples (notably HG002 and family) with many technologies and integrated them into a high-confidence truth set: a curated list of variants plus the genomic regions where calls can be trusted. Compare your caller's output to this inside those regions and you get real precision/recall numbers.

**Why it matters.** This is how I'd validate `variant_calling_nf` honestly. GATK produces calls; GIAB tells me how many are right. Reading it reframes variant calling from "run the tool" to "measure the tool against a standard," which is the difference between using a pipeline and trusting it. It pairs directly with the Platinum Genomes benchmark alongside it today.

**Verdict.** Foundational infrastructure for the whole variant-calling field — GIAB truth sets underpin nearly every caller benchmark. Read it for the confident-regions idea: knowing *where* you can trust a call matters as much as the calls themselves.
