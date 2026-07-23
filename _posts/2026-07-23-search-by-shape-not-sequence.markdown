---
layout: post
title: "Search by shape, not sequence"
date: 2026-07-23 05:30:00 -0500
tags: [paper]
paper:
  title: "Fast and accurate protein structure search with Foldseek"
  authors: "van Kempen et al."
  venue: "Nature Biotechnology, 2024"
  link: "https://doi.org/10.1038/s41587-023-01773-0"
  verdict: "Turns 3D structure into a sequence over a structural alphabet, so structural search becomes fast sequence search — the tool that made the AlphaFold flood of structures searchable."
---

**The problem.** AlphaFold and its kin produced hundreds of millions of predicted protein structures. Structure captures homology that sequence alone misses — distant relatives fold alike long after their sequences diverge — but structural aligners like DALI and TM-align are orders of magnitude too slow to search databases at that scale. The data existed; the search didn't.

**The idea.** Foldseek describes each residue's local 3D environment — the tertiary interactions around it — as a letter in a learned *structural alphabet* (3Di). A protein structure becomes a string over this alphabet, so comparing structures reduces to fast sequence search, powered by the MMseqs2 machinery (today's previous read). This drops structural-search time by four to five orders of magnitude while retaining most of the sensitivity of the slow gold-standard aligners.

**Why it matters.** This is the search layer for the AlphaFold era — the counterpart to what BLAST/MMseqs2 did for sequence, now for the structure universe I read about in the AlphaFold2 and protein-design papers. Encoding structure as sequence to reuse mature, fast sequence algorithms is an elegant reduction, and it makes structure-based annotation and remote-homology detection routine at database scale.

**Verdict.** A field-changing tool that turned a data deluge into a searchable resource; the structural alphabet is lossy, so it complements rather than fully replaces detailed structural alignment. Read it as protein search finally working in the language of shape.
