---
layout: post
title: "How we learned to read DNA"
date: 2026-07-11 12:50:00 -0500
tags: [paper]
paper:
  title: "DNA Sequencing with Chain-Terminating Inhibitors"
  authors: "Sanger, Nicklen & Coulson"
  venue: "PNAS, 1977"
  link: "https://doi.org/10.1073/pnas.74.12.5463"
  verdict: "The method that turned DNA from a molecule you could study into a text you could read — the direct ancestor of everything in my pipelines."
---

**The problem.** You could know DNA carried a linear code (Crick) without being able to *read* it. Until the late 1970s, determining the actual base-by-base sequence of a piece of DNA was slow, brutal work — there was no general, scalable way to spell out a gene.

**The idea.** Sanger's trick is elegant: copy the template with DNA polymerase, but spike in a small fraction of chain-terminating dideoxynucleotides that stop extension whenever they're incorporated. You get a ladder of fragments ending at every position of a given base; run the four reactions side by side on a gel and read the sequence straight off the rungs. Controlled, random termination turns synthesis into a readout.

**Why it matters.** This is the headwater of my entire field. Every FASTQ I've ever touched, every alignment and variant call, exists because sequencing became routine — and it started here, then scaled through automation, capillary machines, and eventually massively-parallel and nanopore reads. The dideoxy logic even echoes forward: reversible terminators are how Illumina sequences-by-synthesis today.

**Verdict.** Foundational, and worth reading to see how simple the core idea is beneath decades of engineering. Its limits — short reads, manual gels, low throughput — are exactly what the next fifty years of sequencing technology set out to erase. Read it as the origin point of computational genomics.
