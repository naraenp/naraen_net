---
layout: post
title: "Aligning the long reads"
date: 2026-07-22 06:30:00 -0500
tags: [paper]
paper:
 title: "Minimap2: pairwise alignment for nucleotide sequences"
 authors: "Li, H."
 venue: "Bioinformatics, 2018"
 link: "https://doi.org/10.1093/bioinformatics/bty191"
 verdict: "The aligner that made long-read sequencing practical, one fast, accurate tool for noisy ONT/PacBio reads, spliced mRNA, and whole-genome alignment, from the author of BWA."
---

**The problem.** Short-read aligners like BWA were built for accurate ~100 bp reads. Nanopore and PacBio produce reads tens of kilobases long with much higher error rates, and the alignment problem changes shape: you need to seed and chain across long, error-riddled sequences, handle large structural gaps, and do it fast enough for whole genomes. The old tools didn't fit.

**The idea.** Minimap2 seeds alignments with minimizers, chains them with a concave gap cost that tolerates long indels, and only then fills in base-level alignment where needed. One code path handles long genomic reads, spliced long-read mRNA, short reads, and genome-to-genome alignment, configured by preset rather than rewritten. It's several times faster than short-read mappers and dozens of times faster than earlier long-read tools at comparable or better accuracy.

**Why it matters.** This is the aligner underneath the long-read world I read about earlier, the Nanopore and PacBio HiFi papers, and the assemblers that consume its output. It's the natural successor to BWA in my own variant-calling instincts: same author, same minimizer-and-chain lineage, extended to the reads that break short-read tools. If you touch long reads, this is the first step.

**Verdict.** The de facto standard for long-read alignment; presets matter, and base-level accuracy still depends on read quality. Read it as the workhorse that turned long, noisy reads into usable alignments.
