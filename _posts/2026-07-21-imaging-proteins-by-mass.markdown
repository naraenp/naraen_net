---
layout: post
title: "Imaging proteins by mass"
date: 2026-07-21 05:30:00 -0500
tags: [paper]
paper:
 title: "Highly multiplexed imaging of tumor tissues with subcellular resolution by mass cytometry (imaging mass cytometry)"
 authors: "Giesen et al."
 venue: "Nature Methods, 2014"
 link: "https://doi.org/10.1038/nmeth.2869"
 verdict: "Antibodies tagged with metal isotopes, read out by mass spectrometry as a laser rasters the tissue, dozens of proteins imaged in place, opening the spatial-proteomics half of the field."
---

**The problem.** Fluorescence microscopy is limited by spectral overlap: you can stain only a handful of proteins at once before their colours collide. Tissue biology is driven by many proteins interacting in space, so a readout capped at four or five markers can't capture a microenvironment. The bottleneck is the reporter, not the microscope.

**The idea.** Imaging mass cytometry swaps fluorophores for metal-isotope tags, the same chemistry that let mass cytometry (CyTOF) measure ~40 parameters in suspension. A laser ablates the tissue spot by spot; the vaporised material goes to a mass spectrometer that counts each isotope, so every pixel carries a high-dimensional protein profile. The result is subcellular-resolution images of 30-plus proteins simultaneously, with no spectral overlap.

**Why it matters.** This is the imaging counterpart to the RNA-imaging methods from the spatial day (MERFISH, seqFISH+), proteins, not transcripts, mapped in situ, and it's foundational to the STU's remit, where spatial *proteomics* sits beside spatial transcriptomics. It also connects to the proteomics thread running through this reading (MaxQuant, mass spec): the same detector principle, now imaging tissue.

**Verdict.** A landmark that founded highly-multiplexed tissue proteomics; throughput is slow and destructive, and marker panels need antibody validation. Read it as the paper that made "many proteins, in place" possible, the technique CODEX and MIBI would race alongside.
