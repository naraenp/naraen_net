---
layout: post
title: "Finding domains with a graph net"
date: 2026-07-19 03:40:00 -0500
tags: [paper]
paper:
  title: "SpaGCN: Integrating gene expression, spatial location and histology to identify spatial domains and spatially variable genes by graph convolutional network"
  authors: "Hu et al."
  venue: "Nature Methods, 2021"
  link: "https://doi.org/10.1038/s41592-021-01255-8"
  verdict: "Spatial domain detection by graph neural network — expression, position, and the H&E image fused into one clustering."
---

**The problem.** Detecting spatial *domains* — coherent tissue regions like cortical layers or tumor niches — needs more than expression clustering, which ignores where cells are. Neighbouring spots should tend to share a domain, and the histology image carries structure too. How do you fuse expression, physical proximity, and tissue morphology into a single, spatially-aware clustering?

**The idea.** SpaGCN builds a graph over spots weighted by both spatial distance and histological similarity (from the H&E image), then runs a graph convolutional network that smooths each spot's expression over its spatial-histological neighbourhood before clustering. The result respects tissue geometry — domains come out spatially contiguous — and the method also identifies the spatially variable genes marking each domain.

**Why it matters.** This is the graph-neural-network arriving in spatial analysis, and it ties threads together: graph convolutions descend from the deep-learning arc (AlexNet → the broader neural-net toolkit), applied to the spatial-domain problem BANKSY (day 4) also tackles. Benchmarked on the Maynard DLPFC data (earlier today), it's a canonical spatial-domain method — exactly the kind the STU would evaluate for recovering known tissue architecture.

**Verdict.** Foundational for deep-learning-based spatial domain detection; fusing histology is its distinctive move. As with any GNN, results depend on graph construction and parameters. Read it as the image-plus-expression, graph-based answer to "what are the regions in this tissue."
