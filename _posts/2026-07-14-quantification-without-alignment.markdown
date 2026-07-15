---
layout: post
title: "Quantification without alignment"
date: 2026-07-14 09:15:00 -0500
tags: [paper]
paper:
  title: "Near-optimal probabilistic RNA-seq quantification (kallisto)"
  authors: "Bray et al."
  venue: "Nature Biotechnology, 2016"
  link: "https://doi.org/10.1038/nbt.3519"
  verdict: "The idea that you don't need to align reads to count transcripts — a faster path to the numbers DESeq2 consumes."
---

**The problem.** The classic RNA-seq route — align every read to the genome with STAR, then count — is accurate but heavy: full alignment is slow and produces information you throw away if all you want is transcript abundance. Do you actually need to know *where* each read maps, or just *which transcript* it came from?

**The idea.** kallisto introduces pseudoalignment: using a k-mer index of the transcriptome, it determines the set of transcripts compatible with each read without computing a base-level alignment. An expectation-maximisation step then resolves reads shared across isoforms into abundance estimates. The result is transcript quantification orders of magnitude faster than alignment, with comparable accuracy.

**Why it matters.** This is a genuine fork in the road for `aml_rnaseq_nf`: STAR-then-count versus pseudoalignment (kallisto or Salmon, next). Reading it clarifies the trade — you gain enormous speed and lose read-level positional information, which matters if you also want variants or novel junctions but not if you only want expression. Knowing when each is appropriate is real pipeline-design knowledge.

**Verdict.** Foundational — it reframed what RNA-seq quantification requires. Salmon (coming up) added bias modelling in a similar spirit. Read it for the core insight: for counting, compatibility is enough; you don't need the alignment.
