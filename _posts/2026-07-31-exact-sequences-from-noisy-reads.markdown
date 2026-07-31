---
layout: post
title: "Exact sequences from noisy reads"
date: 2026-07-31 03:00:00 -0500
tags: [paper]
paper:
 title: "DADA2: High-resolution sample inference from Illumina amplicon data"
 authors: "Callahan et al."
 venue: "Nature Methods, 2016"
 link: "https://doi.org/10.1038/nmeth.3869"
 verdict: "Marker-gene studies used to cluster reads at 97 percent identity and call the clusters species. DADA2 models the sequencing error instead and recovers the exact sequences, one base apart."
---

**The problem.** In 16S rRNA surveys, the old habit was to group similar reads into operational taxonomic units at a fixed 97 percent identity. That threshold is arbitrary. It merges organisms that differ by a single meaningful base and it hides real variation, while still letting sequencing errors through as spurious diversity. The unit of analysis was fuzzy, so counts were never quite comparable between studies.

**The idea.** DADA2 fits an error model to the run itself, learning how often each base is miscalled at each quality score. With that model it asks, for every read, whether it is better explained as a sequencing error off a more abundant sequence or as a genuinely new one. The output is a set of amplicon sequence variants, exact sequences resolved down to a single nucleotide, with per-sample counts. Because the variants are defined by sequence and not by a clustering run, they mean the same thing across datasets.

**Why it matters.** This reframed the basic feature of amplicon data from a fuzzy cluster to an exact sequence, which is the honest version of the measurement. It is also a clean example of modeling the noise instead of thresholding it away.

**Verdict.** The method that retired the 97 percent OTU. Read it for the error model, which is the whole idea.
