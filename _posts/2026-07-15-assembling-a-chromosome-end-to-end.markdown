---
layout: post
title: "Assembling a chromosome, end to end"
date: 2026-07-15 03:20:00 -0500
tags: [paper]
paper:
 title: "Linear assembly of a human chromosome with nanopore ultra-long reads"
 authors: "Jain et al."
 venue: "Nature Biotechnology, 2018"
 link: "https://doi.org/10.1038/s41587-018-0001-7"
 verdict: "The companion result, using ultra-long reads to span a chromosome's hardest region, a preview of finishing the genome."
---

**The problem.** Even with long reads, some regions resist assembly: the human X chromosome's centromere is a vast array of near-identical repeats where reads can't be uniquely placed and assemblies fragment. Spanning it, walking from one side to the other without breaks, was a standing challenge that defined "unfinished" in the reference.

**The idea.** Jain and colleagues applied the very longest nanopore reads to traverse the centromeric satellite array of the X chromosome, producing a contiguous, linear assembly through a region short reads and even ordinary long reads couldn't resolve. The key ingredient is read *length* pushed to its extreme, reads long enough to anchor across the repeat.

**Why it matters.** This is the concrete demonstration of what the previous paper promised: not just more sequence, but *finishing* the parts that were structurally impossible before. It's the direct lineage to the complete T2T genome later on this list. For me, it draws the sharpest possible line around short-read variant calling, there are entire chromosomal features my `variant_calling_nf` reference can't even represent, which only assemblies like this fill in.

**Verdict.** Foundational as a milestone toward the complete human genome. Read it paired with the NA12878 nanopore paper, sequencing the genome, then conquering its single hardest region, as the two-step case for why long reads changed what "reference" means.
