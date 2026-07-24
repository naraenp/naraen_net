---
layout: post
title: "Aligning RNA reads across splice junctions"
date: 2026-07-13 12:15:00 -0500
tags: [paper]
paper:
 title: "STAR: ultrafast universal RNA-seq aligner"
 authors: "Dobin et al."
 venue: "Bioinformatics, 2013"
 link: "https://doi.org/10.1093/bioinformatics/bts635"
 verdict: "The splice-aware aligner that made RNA-seq mapping fast, the step upstream of every count DESeq2 later touches."
---

**The problem.** DNA aligners like BWA assume a read maps to one contiguous stretch of genome. RNA reads don't: a read can straddle a splice junction, with its two halves landing on exons thousands of bases apart. Force a contiguous aligner onto that and you either miss junction-spanning reads or misplace them.

**The idea.** STAR is built for spliced alignment. It uses a suffix-array-based search to find maximal mappable seeds within a read, then stitches seeds across introns, discovering splice junctions in the process rather than requiring them up front. It's aggressively engineered for speed, aligning reads far faster than earlier spliced aligners at the cost of a large in-memory index.

**Why it matters.** STAR (or a pseudo-aligner) is the mapping step that produces the counts my `aml_rnaseq_nf` pipeline feeds to DESeq2. Reading it clarifies that RNA alignment is a genuinely different problem from DNA alignment, the splice-awareness is the whole point, and why the choice of aligner shapes what junctions I can even see. It's the RNA counterpart to the BWA paper from yesterday.

**Verdict.** Foundational and a default to this day; HISAT2 and pseudo-aligners (kallisto, Salmon, coming up) offer different speed/memory trade-offs. Read it as the splice-aware half of the alignment story.
