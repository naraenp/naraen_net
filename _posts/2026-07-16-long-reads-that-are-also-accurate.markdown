---
layout: post
title: "Long reads that are also accurate"
date: 2026-07-16 10:00:00 -0500
tags: [paper]
paper:
  title: "Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome (PacBio HiFi)"
  authors: "Wenger et al."
  venue: "Nature Biotechnology, 2019"
  link: "https://doi.org/10.1038/s41587-019-0217-9"
  verdict: "The read type that dissolves the old trade-off — long *and* accurate — and a big part of why finishing genomes became routine."
---

**The problem.** Long reads (day 9's nanopore) reach the repetitive, structural regions short reads can't, but historically at a cost: high per-base error. Short reads were accurate but short; long reads were long but noisy. That trade-off shaped every pipeline — you picked your weakness. Could a method deliver both?

**The idea.** PacBio HiFi uses circular consensus sequencing: the polymerase reads the same molecule many times in a circle, and averaging those passes collapses random errors into a highly accurate long read (tens of kilobases at short-read-level accuracy). Wenger and colleagues show this improves both variant detection and de novo assembly of a human genome.

**Why it matters.** This resolves the tension running through days 9–10. Sniffles needs long reads for structural variants; DeepVariant/GATK want accuracy for small ones — HiFi gives both, so one data type serves the whole variant spectrum. It's the technology that made complete assemblies (T2T, later on this list) achievable, and it reframes the long-vs-short choice my own short-read pipeline currently assumes.

**Verdict.** Foundational — HiFi reset expectations for long-read accuracy and underpins modern finished genomes. Its costs are throughput and price versus short reads. Read it as the paper that ended "long or accurate, pick one."
