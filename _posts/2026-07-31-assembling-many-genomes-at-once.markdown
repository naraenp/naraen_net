---
layout: post
title: "Assembling many genomes at once"
date: 2026-07-31 08:00:00 -0500
tags: [paper]
paper:
 title: "metaSPAdes: a new versatile metagenomic assembler"
 authors: "Nurk et al."
 venue: "Genome Research, 2017"
 link: "https://doi.org/10.1101/gr.213959.116"
 verdict: "A metagenome is many genomes at different depths, tangled by shared and near-identical sequence. metaSPAdes adapts a proven single-genome assembler to that mess."
---

**The problem.** Assembling a community means assembling many genomes together when their coverage spans orders of magnitude and closely related strains share long stretches of sequence. A strain difference shows up in the graph as a bubble that a naive assembler either collapses, losing real variation, or keeps, breaking the contig. Doing this well, not just cheaply, is a different goal from raw speed.

**The idea.** metaSPAdes builds on the SPAdes assembly graph and reworks its steps for the metagenomic case. It treats low-coverage and strain-variant structures deliberately, deciding when to collapse related strains into a single consensus contig so the backbone stays long, while handling the uneven depth that would confuse a fixed-coverage model. The result is a consensus assembly of the dominant genomes that tends to be more contiguous and accurate on complex samples.

**Why it matters.** metaSPAdes and MEGAHIT are the two assemblers most metagenome studies choose between, one leaning toward quality, the other toward low memory. Good contigs are the raw material for binning genomes out of the mixture, so assembler choice shapes everything after it.

**Verdict.** The quality-first metagenome assembler. Read it for how it handles strain variation, which is the hard part of the problem.
