---
layout: post
title: "RNA and protein in one model"
date: 2026-07-20 14:00:00 -0500
tags: [paper]
paper:
  title: "Joint probabilistic modeling of single-cell multi-omic data with totalVI"
  authors: "Gayoso et al."
  venue: "Nature Methods, 2021"
  link: "https://doi.org/10.1038/s41592-020-01050-x"
  verdict: "A deep generative model for CITE-seq that represents RNA and protein together, separating real signal from protein background and batch — the scVI family extended to multimodal, closing the day on a probabilistic note."
---

**The problem.** CITE-seq protein counts carry heavy background — ambient antibody, non-specific binding — on top of batch effects, and the RNA and protein measurements need to inform a single shared cell representation. A method that models both modalities jointly, and explicitly accounts for the technical noise in each, should give a cleaner latent space than stitching separate analyses together.

**The idea.** totalVI is a deep generative model (a variational autoencoder) that jointly represents a cell's RNA and protein as a composite of biological and technical factors, including an explicit protein-background component and batch. From the learned latent space it supports the standard tasks — integration, dimensionality reduction, clustering, differential expression, and imputation — all within one probabilistic framework, with denoised protein estimates as a bonus.

**Why it matters.** This is the direct multimodal extension of scVI, the deep-generative anchor in the STU reading, and it pairs with totalVI's siblings across the scvi-tools ecosystem. Where WNN fuses modalities at the graph level and MOFA+ at the linear-factor level, totalVI does it inside a generative model — the same negative-binomial-count lineage as stereoscope and DESeq2. A fitting close: multimodal single-cell analysis as one principled model.

**Verdict.** A foundational deep multimodal method, strong when its modelling assumptions hold and batches are well specified; like all deep models it wants enough data and careful validation. Read it as RNA and protein understood inside a single generative account of the cell.
