---
layout: post
title: "The genome, finally complete"
date: 2026-07-17 10:15:00 -0500
tags: [paper]
paper:
 title: "The complete sequence of a human genome (T2T-CHM13)"
 authors: "Nurk et al. (Telomere-to-Telomere Consortium)"
 venue: "Science, 2022"
 link: "https://doi.org/10.1126/science.abj6987"
 verdict: "The reference genome without gaps, the culmination of the long-read arc, and the map my variant pipeline aligns against."
---

**The problem.** The human reference genome, for two decades, had holes: centromeres, segmental duplications, and repeat arrays that short reads (and even ordinary long reads) couldn't resolve were left as gaps. Roughly 8% of the genome was missing or wrong, including regions that matter, silently distorting every alignment and variant call made against them.

**The idea.** The Telomere-to-Telomere Consortium used ultra-long nanopore and accurate PacBio HiFi reads (days 9–10) to assemble CHM13 gaplessly, telomere to telomere, adding nearly 200 million bases and correcting errors in the prior reference. The hard regions that defeated short reads, resolved at last by combining length and accuracy.

**Why it matters.** This is the payoff of the whole long-read thread I've been reading. Days 9–10 built the sequencing and assembly tools; this is what they finally delivered, a complete reference. For `variant_calling_nf`, it reframes the foundation: the genome my reads align to was incomplete, and calls in newly-resolved regions were previously impossible. A better reference silently improves everything built on it.

**Verdict.** Foundational, a genuine milestone, the "finished" human genome. Its implications (new genes, corrected variants, updated references) are still propagating through tools and databases. Read it as the destination the nanopore and HiFi papers were travelling toward.
