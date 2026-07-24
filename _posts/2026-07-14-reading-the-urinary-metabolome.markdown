---
layout: post
title: "Reading the urinary metabolome"
date: 2026-07-14 08:30:00 -0500
tags: [paper]
paper:
 title: "Analysis of the human adult urinary metabolome variations with age, body mass index, and gender (sacurine)"
 authors: "Thévenot et al."
 venue: "J. Proteome Research, 2015"
 link: "https://doi.org/10.1021/acs.jproteome.5b00354"
 verdict: "A clean worked example of untargeted metabolomics, and the 'sacurine' dataset that teaches the whole analysis pipeline."
---

**The problem.** Metabolites, the small-molecule end products of cellular activity, vary with age, sex, and body mass, but untangling those effects from a noisy untargeted LC-MS dataset is a full analysis problem: normalisation, quality control, multivariate modelling, and honest validation, all before you trust a single association.

**The idea.** Thévenot and colleagues profiled urine from a healthy cohort and worked through that pipeline end to end, signal drift correction, sample/feature filtering, and PLS/OPLS modelling to relate the metabolome to age, BMI and gender with cross-validated performance. The value is as much the *methodology demonstrated* as the specific associations found.

**Why it matters.** This rounds out the omics tour: after genomics (variants), transcriptomics (RNA-seq), and proteomics (MaxQuant/MaxLFQ), metabolomics is the fourth layer, and it has the same shape, messy instrument data, systematic drift to correct, multivariate structure to model. The `sacurine` dataset became a teaching standard (Workflow4Metabolomics, ropls), so it's the on-ramp if I ever touch this modality.

**Verdict.** Solid and pedagogically valuable more than groundbreaking, its lasting role is as a reference dataset and a template for untargeted metabolomics QC. Read it for the pipeline discipline: drift correction and validation are where metabolomics analyses live or die.
