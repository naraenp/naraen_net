---
layout: post
title: "Semi-supervised cell annotation"
date: 2026-07-10 14:10:00 -0500
tags: [paper]
paper:
  title: "Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models (scANVI)"
  authors: "Xu et al."
  venue: "Molecular Systems Biology, 2021"
  link: "https://doi.org/10.15252/msb.20209620"
  verdict: "scVI plus labels — the semi-supervised version that turns the latent space into a principled label-transfer engine."
---

**The problem.** You often have *some* annotated cells — a reference atlas, a few labeled samples — and a pile of unlabeled ones. Purely unsupervised embedding (scVI) ignores the labels you have; purely supervised classification ignores the structure in the cells you don't. You want a model that uses both.

**The idea.** scANVI extends scVI into a semi-supervised generative model: the latent space is still learned from all cells, but known labels are woven in so the representation is shaped by both the data's structure and the annotations you trust. The payoff is label transfer with uncertainty — annotate a new dataset from a reference, and get a calibrated sense of where the model is unsure rather than a hard, overconfident call.

**Why it matters.** Annotation is where single-cell analysis meets *judgment*, and "here's the label, and here's how confident I am" is exactly what a facility should hand back to a collaborator. It also generalizes: the same reference-plus-query, uncertainty-aware framing is what the spatial deconvolution methods are doing when they map a single-cell reference onto tissue. Consistent machinery across the whole stack.

**Verdict.** The natural companion to scVI and the more directly useful of the pair for day-to-day annotation. Same honest limits — it inherits scVI's assumptions and needs a decent reference — plus the usual caution that transferred labels are only as good as the reference's granularity. Read the two together; this is scVI with a job to do.
