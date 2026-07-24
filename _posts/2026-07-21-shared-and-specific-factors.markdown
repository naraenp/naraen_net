---
layout: post
title: "Shared and dataset-specific factors"
date: 2026-07-21 11:15:00 -0500
tags: [paper]
paper:
 title: "Single-cell multi-omic integration compares and contrasts features of brain cell identity (LIGER)"
 authors: "Welch et al."
 venue: "Cell, 2019"
 link: "https://doi.org/10.1016/j.cell.2019.05.006"
 verdict: "Integrative NMF that splits variation into factors shared across datasets and factors specific to each, so you can align cells and, at the same time, keep what makes each dataset distinct."
---

**The problem.** Most integration aims to erase differences between datasets so cells line up. But sometimes the differences *are* the biology, a disease sample versus control, a different species, RNA versus a chromatin readout. You want a method that finds common structure to align on while explicitly preserving, not discarding, what's unique to each dataset.

**The idea.** LIGER uses integrative non-negative matrix factorization (iNMF): it factorizes multiple datasets into a set of shared metagene factors plus dataset-specific factors. Cells are then matched in the shared factor space (via a neighbour-graph step), giving joint clusters, while the dataset-specific factors quantify what each sample contributes on its own. Applied to brain data, it aligns cell types across modalities and highlights modality-specific signals.

**Why it matters.** This is the multi-view sibling of the factor and integration methods around it, it shares MOFA+'s decompose-into-factors instinct and the alignment goal of Harmony and Scanorama, but its shared-versus-specific split is the distinctive move. For comparative studies, and for the STU contrasting spatial modalities or conditions, keeping the differences interpretable is often the whole point.

**Verdict.** A widely-used integration method with a genuinely different philosophy; NMF factor counts and regularization need tuning, and interpretation takes care. Read it as integration that aligns without flattening, shared and specific held apart on purpose.
