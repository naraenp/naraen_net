---
layout: post
title: "Many proteins, one microscope"
date: 2026-07-21 07:00:00 -0500
tags: [paper]
paper:
 title: "Deep profiling of mouse splenic architecture with CODEX multiplexed imaging"
 authors: "Goltsev et al."
 venue: "Cell, 2018"
 link: "https://doi.org/10.1016/j.cell.2018.07.010"
 verdict: "Multiplexed protein imaging on an ordinary fluorescence microscope, DNA-barcoded antibodies revealed in cycles, making spatial proteomics accessible without a mass spectrometer."
---

**The problem.** Metal-tag imaging (imaging mass cytometry, MIBI) achieves high multiplexing but needs specialised, slow, destructive mass-spectrometry instruments. Most labs have a fluorescence microscope, not an ion beam. Could you reach comparable marker counts using standard optics, so highly-multiplexed tissue imaging isn't gated on rare hardware?

**The idea.** CODEX (co-detection by indexing) tags each antibody with a unique DNA barcode. Rendering is iterative: fluorescent nucleotide analogues are polymerised to reveal a few barcodes at a time, imaged, stripped, and repeated over many cycles. The tissue stays intact on a normal microscope while dozens of proteins are read out in sequence, then computationally stacked into one high-dimensional image, here used to dissect the cellular architecture of the mouse spleen.

**Why it matters.** CODEX brought spatial proteomics within reach of ordinary labs, which is why it spread quickly and why the STU cares, accessibility decides which platform a unit can actually run. It completes the spatial-proteomics trio (imaging mass cytometry, MIBI, CODEX) that mirrors the RNA-imaging methods from the spatial day, and its neighbourhood analysis of the spleen prefigures the niche and domain questions the earlier reading raised.

**Verdict.** A widely-adopted, hardware-friendly multiplexed imaging method; cyclic imaging is time-consuming and demands careful antibody and registration workflows. Read it as spatial proteomics for the rest of us, many proteins, one microscope.
