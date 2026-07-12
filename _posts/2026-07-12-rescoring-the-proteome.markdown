---
layout: post
title: "Rescoring the proteome"
date: 2026-07-12 09:30:00 -0500
tags: [paper]
paper:
  title: "Semi-supervised learning for peptide identification from shotgun proteomics datasets (Percolator)"
  authors: "Käll et al."
  venue: "Nature Methods, 2007"
  link: "https://doi.org/10.1038/nmeth1113"
  verdict: "The paper that taught proteomics search engines to trust machine learning — turning a pile of weak scores into calibrated confidence."
---

**The problem.** A shotgun proteomics run produces hundreds of thousands of spectra, each matched to a candidate peptide by a search engine. But any single score is a noisy signal, and picking a fixed threshold either loses real identifications or lets false ones through. How do you separate true peptide-spectrum matches from decoys reliably?

**The idea.** Percolator learns the boundary instead of fixing it. It takes the search engine's many features per match, trains a semi-supervised classifier against a *decoy* database (sequences known to be wrong), and rescores every match on the learned discriminant. Because decoys give an empirical null, it can convert scores into q-values — calibrated FDR-controlled confidence — recovering far more true peptides at the same error rate.

**Why it matters.** This is FDR thinking (today's first paper) applied to proteomics, and it's why the target-decoy plus machine-learning pattern is now standard across the field. It connects to the mass-spec tooling in my reading list — MaxQuant, the search engines — and reinforces a theme: the smartest step in an omics pipeline is often the *statistics of confidence*, not the raw measurement.

**Verdict.** Foundational for proteomics and a clean case study in using a decoy null to calibrate a learned score. Its assumptions (representative decoys, informative features) are the usual caveats. Read it as the confidence layer that makes shotgun proteomics quantitative rather than anecdotal.
