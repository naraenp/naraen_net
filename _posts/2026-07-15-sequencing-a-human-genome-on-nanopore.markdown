---
layout: post
title: "Sequencing a human genome on nanopore"
date: 2026-07-15 03:00:00 -0500
tags: [paper]
paper:
  title: "Nanopore sequencing and assembly of a human genome with ultra-long reads"
  authors: "Jain et al."
  venue: "Nature Biotechnology, 2018"
  link: "https://doi.org/10.1038/nbt.4060"
  verdict: "The proof that long-read nanopore could assemble a human genome — the technology that reaches the regions short reads can't."
---

**The problem.** Short reads (the Illumina data my pipelines assume) map beautifully to unique sequence but fail in repeats, segmental duplications, and structural rearrangements — regions longer than a read. Whole stretches of the genome stayed effectively unresolvable. The question was whether a different sequencing chemistry could read long enough to span them.

**The idea.** Jain and colleagues sequenced the reference human sample NA12878 on Oxford Nanopore, generating ultra-long reads — some spanning hundreds of kilobases — and used them to assemble the genome, close gaps, and resolve structural and repetitive regions inaccessible to short reads. It demonstrated nanopore at whole-human-genome scale, error profile and all.

**Why it matters.** This marks the boundary of the short-read world I work in. BWA + GATK excel where reads map uniquely; this paper is about everything past that frontier — the structural variation and repeats that need length, not depth. Reading it frames my own variant pipeline honestly: it's superb for SNVs and small indels, and blind to a class of variation that long reads exist to catch.

**Verdict.** Foundational for long-read genomics and the completeness push that culminated in T2T (later on this list). Read it for the trade-off — long reads' length versus their per-base error — and for the reminder that read length, not just accuracy, decides what you can see.
