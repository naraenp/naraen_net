---
layout: post
title: "The single-cell checklist"
date: 2026-07-08 14:45:00 -0500
tags: [paper]
paper:
 title: "Current best practices in single-cell RNA-seq analysis: a tutorial"
 authors: "Luecken & Theis"
 venue: "Molecular Systems Biology, 2019"
 link: "https://doi.org/10.15252/msb.20188746"
 verdict: "The reference everyone cites for scRNA-seq QC-to-annotation, and a mirror to hold up to my own AML workflow."
---

**The problem.** Single-cell analysis has a dozen decision points before you ever see a UMAP, and most of them silently determine the result. This tutorial is the field's shared answer to "what should the pipeline actually be," and it underpins my AML scRNA-seq project, so I read it as a retro of my own choices.

**The idea.** It's a stage-by-stage workflow with defensible defaults. **Preprocessing**: quality filtering (counts, genes, mitochondrial fraction), correcting ambient RNA and removing doublets, then normalization, highly-variable-gene selection, scaling, and dimensionality reduction, with the standing warning that *how you filter changes everything downstream*. **Downstream**: clustering, cluster **annotation** (the genuinely hard, human-judgment part), marker/differential expression, compositional analysis, and trajectory/pseudotime inference. It closes with a reproducible worked example so the advice is executable, not just prose.

**Why it matters.** The value is the audit. Reading it, the questions write themselves: did I filter too aggressively on mito percentage? Did I validate cluster annotations against markers or just trust the algorithm? Is my trajectory analysis reading real biology or over-interpreting noise (the exact caution the repressilator's variability taught)? Turning those into an honest retrospective is worth more than any single new method.

**Verdict.** Still the best on-ramp, with the caveat that it predates the current wave, scVI-class integration and single-cell foundation models have matured since, and a modern reader should pair it with the 2023 best-practices update. But for the fundamentals of *not fooling yourself*, it holds. Next: a candid "what I'd change in my AML workflow with hindsight."
