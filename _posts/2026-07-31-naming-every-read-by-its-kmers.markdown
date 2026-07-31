---
layout: post
title: "Naming every read by its k-mers"
date: 2026-07-31 04:00:00 -0500
tags: [paper]
paper:
 title: "Improved metagenomic analysis with Kraken 2"
 authors: "Wood, Lu & Langmead"
 venue: "Genome Biology, 2019"
 link: "https://doi.org/10.1186/s13059-019-1891-0"
 verdict: "A shotgun metagenome is millions of reads from an unknown mix of species. Kraken 2 assigns each read to a taxon by matching short k-mers against a database, fast enough to run on a laptop."
---

**The problem.** Given raw reads from a soil or gut sample, the first question is which organisms are present and in what proportion. Aligning every read against every reference genome is far too slow at metagenomic scale, and assembly throws away the many reads that never assemble. The field needed a way to label reads directly, quickly, and with a sensible answer when a read could belong to several related species.

**The idea.** Kraken breaks each read into k-mers and looks them up in a precomputed map from k-mer to the lowest common ancestor of all genomes that contain it. A read is assigned by combining its k-mer hits along the taxonomy, so an ambiguous read lands at a higher, safer rank rather than a wrong species. Kraken 2 replaces the original exact k-mer index with minimizers and a compact probabilistic hash, which cuts memory and time by a large factor while keeping accuracy close.

**Why it matters.** This is exact-match classification, the same k-mer indexing idea that makes alignment-free quantification fast, turned toward taxonomy. It made read-level profiling of large cohorts routine.

**Verdict.** The default first pass on a shotgun metagenome. Read it for the lowest-common-ancestor trick, which is how it stays honest under ambiguity.
