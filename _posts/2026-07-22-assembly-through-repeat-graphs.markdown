---
layout: post
title: "Assembly through repeat graphs"
date: 2026-07-22 13:15:00 -0500
tags: [paper]
paper:
  title: "Assembly of long, error-prone reads using repeat graphs (Flye)"
  authors: "Kolmogorov et al."
  venue: "Nature Biotechnology, 2019"
  link: "https://doi.org/10.1038/s41587-019-0072-8"
  verdict: "Tackles the hardest part of assembly — repeats — head-on, building a repeat graph from deliberately rough long-read fragments and resolving it, from Pevzner's assembly-theory lineage."
---

**The problem.** Repeats are why genome assembly is hard: sequences longer than a read, repeated across the genome, collapse or tangle, and even long error-prone reads don't trivially resolve them. Classic overlap-layout-consensus and de Bruijn approaches struggle when reads are both long and noisy. You need a representation that makes the repeat structure explicit and then untangles it.

**The idea.** Flye first assembles rough, error-riddled fragments it calls disjointigs — arbitrary paths through an unknown assembly graph — without worrying about accuracy. It concatenates them, then constructs an accurate *repeat graph* from these disjointigs, a structure that lays the genome's repeats bare. Resolving paths through that graph, using reads that span repeat copies, yields the final contigs. Facing repeats explicitly nearly doubled human-assembly contiguity over prior long-read assemblers.

**Why it matters.** Flye is a mainstay of the long-read assembly world alongside hifiasm (today's other assembler), and it descends directly from the de Bruijn/repeat-graph theory Pevzner has built for decades — the same algorithmic lineage as SPAdes. For Nanopore data especially, where reads are noisier than HiFi, its repeat-graph strategy is the go-to. Assembly is where sequencing becomes a genome, and repeats are the crux.

**Verdict.** A widely-used long-read assembler (with a metagenome mode, metaFlye); output still benefits from polishing, and very complex repeats remain hard. Read it as assembly that confronts the repeat problem by drawing it explicitly.
