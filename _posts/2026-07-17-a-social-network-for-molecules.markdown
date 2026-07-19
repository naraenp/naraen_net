---
layout: post
title: "A social network for molecules"
date: 2026-07-17 11:45:00 -0500
tags: [paper]
paper:
  title: "Feature-based molecular networking in the GNPS environment"
  authors: "Nothias et al."
  venue: "Nature Methods, 2020"
  link: "https://doi.org/10.1038/s41592-020-0933-6"
  verdict: "How you make sense of thousands of unknown metabolites — by their spectral relationships, not just their names — with quantitative feature data attached."
---

**The problem.** Untargeted metabolomics detects thousands of small-molecule features, and most can't be identified by matching to a reference spectrum — the databases are too incomplete. You're left with a vast list of unknowns, and no way to organise them or reason about which ones relate to which.

**The idea.** Molecular networking clusters spectra by similarity: molecules with related structures fragment similarly, so a network of spectral edges groups a known compound with its unknown analogues, letting identity propagate across the graph. Feature-based networking adds the crucial upgrade — linking that network to *quantitative* feature-detection output (from tools like XCMS, next), so you get abundance across samples, not just connectivity.

**Why it matters.** This extends the metabolomics arc (sacurine, day 8) from "measure the metabolome" to "make sense of its unknowns." Conceptually it's a graph/community approach — the same relational thinking as Louvain/Leiden clustering, applied to spectra instead of cells. It's also a nice example of coupling qualitative structure (the network) with quantitative data (the features), which is exactly what makes a method usable for real comparisons.

**Verdict.** Foundational for untargeted metabolomics interpretation and the GNPS ecosystem. Read it for the networking idea — organise unknowns by relationship — and as the analysis counterpart to the peak-picking that feeds it.
