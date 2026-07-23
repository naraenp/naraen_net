---
layout: post
title: "Calling peaks from the pileup"
date: 2026-07-22 09:30:00 -0500
tags: [paper]
paper:
  title: "Model-based Analysis of ChIP-Seq (MACS)"
  authors: "Zhang et al."
  venue: "Genome Biology, 2008"
  link: "https://doi.org/10.1186/gb-2008-9-9-r137"
  verdict: "The peak caller that defined how we find protein-binding and open-chromatin regions from sequencing pileups — a local Poisson background and a tag-shift model, still the default two decades on."
---

**The problem.** ChIP-seq (and later ATAC-seq) produces a genome-wide pileup of reads; the signal you want is where reads *enrich* — binding sites or open regions — above a noisy, non-uniform background. Naïve thresholds fail because background varies locally with copy number, mappability, and chromatin. You need a principled test for "is this pileup a real peak?"

**The idea.** MACS models the fact that ChIP fragments produce reads offset on the two strands, empirically estimates that shift, and combines strands to sharpen resolution. It then tests enrichment against a *local* dynamic Poisson background — estimated from windows around each site — so the null adapts to regional biases rather than assuming a genome-wide constant. Significant regions become the called peaks, with control samples folded in when available.

**Why it matters.** This is the counterpart to the ATAC-seq paper I read earlier: ATAC-seq generates the open-chromatin signal, MACS is how you turn that signal into called regions. The local-background idea is the durable insight — it's why MACS2 remained standard for both ChIP and ATAC peak calling. For epigenomic pipelines it's the load-bearing step, the analog of variant calling for regulatory regions.

**Verdict.** The field-standard peak caller; parameters (shift, background window, whether you have input control) shape the calls, so they're worth setting deliberately. Read it as the model that made "where does this protein bind" a routine, testable question.
