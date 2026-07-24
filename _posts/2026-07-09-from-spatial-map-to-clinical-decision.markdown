---
layout: post
title: "From spatial map to clinical decision"
date: 2026-07-09 09:50:00 -0500
tags: [paper]
paper:
 title: "Statistical and computational methods for enabling the clinical and translational application of spatial transcriptomics"
 authors: "Wu et al."
 venue: "Clinical and Translational Medicine, 2024"
 link: "https://doi.org/10.1002/ctm2.70119"
 verdict: "The same set of methods, reframed for the clinic, why robustness and standards, not novelty, are what a core facility sells."
---

**The problem.** Most spatial-methods reviews are written for method developers. This one asks a different question: what has to be true for spatial transcriptomics to inform *clinical and translational* decisions, and where do the current computational methods fall short of that bar?

**The idea.** It walks the analysis pipeline, QC, deconvolution, domain detection, cell–cell interaction, multi-sample integration, through a translational lens, emphasizing the parts that matter when a result might touch a patient: reproducibility across samples and batches, robustness of deconvolution and segmentation, benchmarking against orthogonal assays, and the standardization needed to compare studies. It's the "reverse translation" framing, taking clinical questions back to the bench readout, made concrete for spatial data.

**Why it matters.** This maps almost exactly onto the pitch a data/pipeline person brings to a spatial core facility: the value isn't a clever new algorithm, it's making the existing ones *trustworthy, reproducible, and comparable* across runs. It's also the clearest statement of why a facility obsesses over QC and standards, because the downstream consumer is a clinical decision, not a figure. That reframing is worth internalizing before any interview or collaboration in this space.

**Verdict.** A review, so orientation rather than evidence, but a well-aimed one, and current (2024). Its value is the framing: it turns "which method is best" into "which method is robust enough to stake a decision on," which is the right question for translational work. Pairs naturally with the platform benchmarks and the QC-workflow paper as the "how do we make this dependable" cluster.
