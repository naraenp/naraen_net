---
layout: post
title: "An encyclopedia of the genome"
date: 2026-07-13 10:00:00 -0500
tags: [paper]
paper:
 title: "An integrated encyclopedia of DNA elements in the human genome (ENCODE)"
 authors: "The ENCODE Project Consortium"
 venue: "Nature, 2012"
 link: "https://doi.org/10.1038/nature11247"
 verdict: "The project that filled in the 98% of the genome that isn't genes, and the reference layer half of functional genomics quietly leans on."
---

**The problem.** The human genome sequence told us the letters, but most of it doesn't code for protein. What is the rest *doing*? Which stretches are promoters, enhancers, transcription-factor binding sites, or regions of open chromatin, and in which cell types? Sequence alone doesn't say.

**The idea.** ENCODE was an industrial-scale annotation effort: ChIP-seq, DNase-seq, RNA-seq and more across many cell lines, integrated into genome-wide maps of functional elements. Its headline, that a large fraction of the genome shows some biochemical activity, was widely debated, but the lasting product is the atlas of regulatory annotations itself.

**Why it matters.** ENCODE is infrastructure. When SnpEff or a downstream filter asks whether a non-coding variant lands in a regulatory element, the answer traces back to catalogues like this. It's also the conceptual backdrop for the ATAC-seq and TF papers alongside it today, the "function" that accessibility and binding assays measure is the function ENCODE set out to map.

**Verdict.** Foundational as a resource; read the summary for the framing and treat the "80% functional" claim as the cautionary tale it became. The enduring value is the reference tracks, not the press release.
