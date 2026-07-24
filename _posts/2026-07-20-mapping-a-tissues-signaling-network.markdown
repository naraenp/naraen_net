---
layout: post
title: "Mapping a tissue's signaling network"
date: 2026-07-20 07:20:00 -0500
tags: [paper]
paper:
 title: "Inference and analysis of cell–cell communication using CellChat"
 authors: "Jin et al."
 venue: "Nature Communications, 2021"
 link: "https://doi.org/10.1038/s41467-021-21246-9"
 verdict: "Cell–cell communication as a quantitative network, not just which pairs talk, but the dominant senders, receivers, and signaling patterns, and how they shift between conditions."
---

**The problem.** Listing enriched ligand–receptor pairs (yesterday's CellPhoneDB) tells you the edges but not the shape of the network. Which cell types are the hubs? Which pathways dominate? And when you compare disease to healthy, how does the whole communication structure reorganise? You want signaling analysed as a network, not a spreadsheet of pairs.

**The idea.** CellChat combines a curated interaction database (grouping ligand–receptor pairs into signaling pathways, including cofactors) with network-analysis and pattern-recognition tools. It quantifies communication probability between cell groups, then uses manifold learning and unsupervised pattern discovery to identify major signaling roles, senders, receivers, mediators, and to classify pathways. It also compares communication across datasets, flagging conserved versus context-specific signaling.

**Why it matters.** This is the network-biology lens applied to intercellular signaling: the same instinct as the community-detection and graph methods from earlier days, now over a signaling graph. For the STU, the comparative mode is the payoff, contrasting the communication network of a tumor niche against normal tissue is precisely the spatial-context question the unit works on, and CellChat makes it a structured analysis.

**Verdict.** A default for communication analysis, valued for its pathway-level view and cross-condition comparison; like all such tools it inherits the biases of its curated database and assumes co-expression implies signaling. Read it as the step from listing conversations to mapping the whole conversational network of a tissue.
