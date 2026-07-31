---
layout: post
title: "Sorting contigs into genomes"
date: 2026-07-31 09:00:00 -0500
tags: [paper]
paper:
 title: "MetaBAT 2: an adaptive binning algorithm for robust and efficient genome reconstruction from metagenome assemblies"
 authors: "Kang et al."
 venue: "PeerJ, 2019"
 link: "https://doi.org/10.7717/peerj.7359"
 verdict: "Assembly gives thousands of contigs with no labels. Binning groups the contigs that came from the same organism, and MetaBAT 2 does it from sequence composition and coverage."
---

**The problem.** A metagenome assembly is a pile of contigs, and the genomes are hidden in it, cut into pieces and mixed together. To recover a draft genome you have to decide which contigs belong to the same organism, without a reference to match them against. The signal is indirect, and a binning tool has to work across the huge range of contig lengths and coverages that a real sample produces.

**The idea.** MetaBAT 2 scores every pair of contigs on two features: tetranucleotide frequency, a compositional fingerprint that tends to be consistent within a genome, and abundance, meaning how contig coverage rises and falls together across samples. Contigs from one organism share both a fingerprint and a coverage pattern. It combines these into a distance, then clusters, with thresholds that adapt to the data rather than being set by hand. The output is a set of bins, each a candidate metagenome-assembled genome.

**Why it matters.** Binning is what turns anonymous contigs into genomes for organisms nobody has cultured, which is how the tree of life has been filling in from environmental data. Coverage across many samples is the strongest single clue, and using it well is the core of the method.

**Verdict.** A fast, widely used binner. Read it for the pairing of composition with cross-sample coverage.
