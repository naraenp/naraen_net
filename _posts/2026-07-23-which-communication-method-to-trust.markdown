---
layout: post
title: "Which communication method to trust"
date: 2026-07-23 06:15:00 -0500
tags: [paper]
paper:
 title: "Comparison of methods and resources for cell–cell communication inference from single-cell RNA-seq data (LIANA)"
 authors: "Dimitrov et al."
 venue: "Nature Communications, 2022"
 link: "https://doi.org/10.1038/s41467-022-30755-0"
 verdict: "A sober benchmark of the cell–cell communication field, showing how much the method and the ligand–receptor resource you pick change the answer, wrapped in a framework that runs them all."
---

**The problem.** After the wave of cell–cell communication tools (CellPhoneDB, CellChat, NicheNet, and more, which I read last week), a practical worry surfaced: do they agree? Each pairs a different inference method with a different ligand–receptor resource, and if those choices drive the predictions, then any single tool's output is hard to trust on its own.

**The idea.** LIANA systematically compares many CCC methods and resources on common footing, decoupling the scoring method from the interaction database so their separate effects are visible. The finding is cautionary: resources share surprisingly few interactions and cover pathways unevenly, and both the method and the resource strongly shape which interactions are called. To make comparison and consensus practical, LIANA provides a single framework that runs the methods together and aggregates them, checked against spatial colocalisation and other modalities.

**Why it matters.** This is the critical-evaluation counterweight to the CCC methods I already reviewed, the reminder that tool choice is a hidden variable, and that consensus beats any one caller. It's the same benchmarking instinct as the spatial-deconvolution and integration comparisons on my list. For the STU, where niche signaling is a core readout, knowing how fragile a single method's calls can be is essential hygiene.

**Verdict.** A valuable, widely-cited benchmark and a practical consensus tool; aggregation reduces but doesn't erase resource bias. Read it as the field auditing itself, and a better default than trusting one CCC method alone.
