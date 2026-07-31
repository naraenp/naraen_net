---
layout: post
title: "A standard tree for bacteria"
date: 2026-07-31 11:00:00 -0500
tags: [paper]
paper:
 title: "GTDB-Tk: a toolkit to classify genomes with the Genome Taxonomy Database"
 authors: "Chaumeil et al."
 venue: "Bioinformatics, 2020"
 link: "https://doi.org/10.1093/bioinformatics/btz848"
 verdict: "Once you have a draft genome, what is it? GTDB-Tk places it on a standardized, sequence-based tree of life and gives it a name that means the same thing to everyone."
---

**The problem.** Microbial names grew up piecemeal, and ranks were assigned inconsistently, so the same word could cover very different amounts of diversity. When metagenomics started recovering thousands of genomes from uncultured organisms, this got worse: many had no clear place in the old taxonomy, and naming them by hand did not scale.

**The idea.** The Genome Taxonomy Database rebuilds bacterial and archaeal taxonomy from genome sequence, using a concatenated set of conserved marker proteins to infer one reference tree, then normalizing the ranks so that a given level reflects a consistent amount of evolutionary divergence. GTDB-Tk is the tool that classifies a new genome against it. It identifies the markers, aligns them, places the genome in the reference tree, and confirms the assignment with average nucleotide identity to the nearest reference. The output is a full, standardized lineage.

**Why it matters.** This closes the metagenomic arc: reads became contigs, contigs became bins, bins passed a quality check, and now each genome gets a name in a common frame that lets studies be compared. A sequence-defined taxonomy is also the honest one when most organisms will never be cultured.

**Verdict.** The standard way to name a genome now. Read it for how divergence-normalized ranks fix the inconsistency in the old taxonomy.
