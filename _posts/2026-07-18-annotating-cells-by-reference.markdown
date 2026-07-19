---
layout: post
title: "Annotating cells by reference"
date: 2026-07-18 11:00:00 -0500
tags: [paper]
paper:
  title: "Reference-based analysis of lung single-cell sequencing reveals a transitional profibrotic macrophage (SingleR)"
  authors: "Aran et al."
  venue: "Nature Immunology, 2019"
  link: "https://doi.org/10.1038/s41590-018-0276-y"
  verdict: "Automated cell-type labelling by correlation to reference profiles — how you avoid annotating every cluster by hand."
---

**The problem.** After clustering, someone has to say *what each cluster is* — which cell type. Done manually, that means hunting marker genes cluster by cluster: slow, subjective, and inconsistent between analysts. As datasets grew to hundreds of clusters across many samples, hand-annotation stopped scaling.

**The idea.** SingleR automates it by correlation. Given reference transcriptomes of known cell types, it scores each single cell (or cluster) against every reference profile and assigns the best-matching label, with a fine-tuning step to resolve close calls. The annotation becomes reproducible and reference-driven rather than a judgment call — and the paper demonstrates it by uncovering a transitional macrophage state in fibrotic lung.

**Why it matters.** Automated annotation is a standard step, and SingleR's reference-correlation approach connects to the recurring "transfer labels from reference to query" theme — scANVI (day 4) and Seurat anchors (day 10) do versions of the same thing. It also foreshadows the foundation-model framing (Geneformer, scGPT) where a pretrained reference does the labelling. Different mechanisms, one goal: stop annotating by hand.

**Verdict.** Foundational for automated cell-type annotation and widely used; its labels are only as good as the reference, so reference choice matters. Read it as the correlation-based answer to "what is this cluster," and part of the label-transfer family running through the reading list.
