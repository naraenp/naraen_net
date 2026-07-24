---
layout: post
title: "Beads that map the tissue"
date: 2026-07-19 01:10:00 -0500
tags: [paper]
paper:
 title: "Highly sensitive spatial transcriptomics at near-cellular resolution with Slide-seqV2"
 authors: "Stickels et al."
 venue: "Nature Biotechnology, 2020"
 link: "https://doi.org/10.1038/s41587-020-0739-1"
 verdict: "Capture-based spatial at near-single-cell resolution, closing the gap between Visium's spots and imaging's precision."
---

**The problem.** Spot-based capture (Ståhl/Visium) is whole-transcriptome but coarse, 55-micron spots spanning several cells. Imaging is precise but targeted. Could a *capture* method, keeping the unbiased whole-transcriptome advantage, reach near-cellular resolution, getting the best of both branches without imaging's panel limits?

**The idea.** Slide-seq packs a surface with 10-micron barcoded beads, each bead's spatial position determined in advance by sequencing. Tissue laid on top releases mRNA captured by the nearest bead, so transcripts get near-cellular spatial coordinates while retaining whole-transcriptome capture. Slide-seqV2 improves the sensitivity (capture efficiency) enough to make the approach genuinely usable.

**Why it matters.** Slide-seqV2 sits right between the two poles I've read today, capture-based like Visium, but approaching imaging's resolution. For the STU, it's a key point on the platform trade-off curve: whole-transcriptome and fine-grained, at the cost of per-bead sensitivity and some deconvolution still needed. It shows the "capture vs. image" dichotomy is really a continuum.

**Verdict.** Foundational for high-resolution capture-based spatial; sensitivity per bead remains the practical constraint. Read it as the resolution upgrade to the Ståhl/Visium lineage, and as evidence that the capture branch can chase single-cell resolution too.
