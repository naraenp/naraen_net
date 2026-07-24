---
layout: post
title: "Pseudotime, but in tissue space"
date: 2026-07-09 11:10:00 -0500
tags: [paper]
paper:
 title: "Spatial Transcriptomics Brings New Challenges and Opportunities for Trajectory Inference"
 authors: "Heitz et al."
 venue: "Annual Review of Biomedical Data Science, 2025"
 link: "https://doi.org/10.1146/annurev-biodatasci-040324-030052"
 verdict: "The bridge from the trajectory work I've already done to the spatial frontier, pseudotime with coordinates attached."
---

**The problem.** Trajectory inference in dissociated single-cell data reconstructs a *process*, differentiation, activation, from a static snapshot, but it throws away where the cells were. In tissue, position often *is* the axis of the process (a crypt–villus gradient, a tumor margin). Can trajectory methods use spatial coordinates instead of fighting them?

**The idea.** This review connects trajectory/pseudotime inference to spatial data directly. It lays out how spatial context changes the problem: neighborhood information can constrain or replace purely expression-based ordering, real physical gradients can anchor a trajectory, and the usual pseudotime pitfalls (over-interpreting noise, imposing a lineage where there's a continuum) take new forms when space is a variable. It surveys the emerging methods and the open challenges rather than crowning a winner.

**Why it matters.** This is a personal bridge: I did trajectory/pseudotime analysis in my AML single-cell project, so the leap to "the same analysis, but the cells keep their coordinates" is a natural extension of an existing strength rather than a cold start. For the spatial role it's the paper that connects what I've already built to where the field is going.

**Verdict.** A review, and an early-stage one, spatial trajectory inference is genuinely less settled than clustering or deconvolution, so this is more a map of open problems than a toolbox. That's fine; it's the right paper for framing, and the honesty about how easily pseudotime over-interprets carries straight over from the single-cell literature (and echoes the "noisy oscillator" caution from the repressilator). Read it to connect the AML trajectory work to tissue space.
