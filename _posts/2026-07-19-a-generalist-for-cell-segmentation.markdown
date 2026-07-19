---
layout: post
title: "A generalist for cell segmentation"
date: 2026-07-19 04:40:00 -0500
tags: [paper]
paper:
  title: "Cellpose: a generalist algorithm for cellular segmentation"
  authors: "Stringer et al."
  venue: "Nature Methods, 2021"
  link: "https://doi.org/10.1038/s41592-020-01018-x"
  verdict: "The deep-learning segmentation that just works across cell types — the step that decides where each cell is before imaging-based spatial can count anything."
---

**The problem.** Imaging-based spatial (MERFISH, Xenium) and microscopy in general hit the same first obstacle: drawing accurate boundaries around each cell. Cells vary wildly in shape, size, and staining, so classical segmentation needed hand-tuning per dataset, and earlier neural nets needed retraining for each new cell type. Segmentation errors then propagate into every downstream count — the missegmentation problem MisTIC (day 4) tries to clean up after.

**The idea.** Cellpose trains a neural network to predict, for each pixel, spatial gradients pointing toward its cell's center; following those gradients groups pixels into cells. Trained on a large, diverse image set, it generalises across cell types and imaging modalities without per-dataset retraining — a "generalist" model that segments images it never saw during training.

**Why it matters.** Segmentation is upstream of everything in imaging-based spatial: get the boundaries wrong and transcripts get assigned to the wrong cells, corrupting the whole analysis. Cellpose is a default for this step, and it closes several threads — it's the deep-learning/U-Net lineage (the CNN arc from AlexNet) applied to the exact segmentation problem that Baysor and MisTIC (day 4) also address. A fitting close: the pixel-level foundation the entire spatial-single-cell stack rests on.

**Verdict.** Foundational for bioimage segmentation and heavily used in spatial pipelines; generalist models still benefit from occasional fine-tuning on hard tissue. Read it as the deep-learning segmentation workhorse — where the spatial map literally begins, one cell boundary at a time.
