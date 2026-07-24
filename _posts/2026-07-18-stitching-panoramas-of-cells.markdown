---
layout: post
title: "Stitching panoramas of cells"
date: 2026-07-18 11:45:00 -0500
tags: [paper]
paper:
 title: "Efficient integration of heterogeneous single-cell transcriptomes using Scanorama"
 authors: "Hie, Bryson & Berger"
 venue: "Nature Biotechnology, 2019"
 link: "https://doi.org/10.1038/s41587-019-0113-3"
 verdict: "Integration by analogy to panorama stitching, merge only where datasets genuinely overlap, and a third answer to the batch problem."
---

**The problem.** Integrating many single-cell datasets risks a specific failure: forcing alignment between datasets that *don't* share cell types, blending distinct populations that should stay separate. You want to merge where datasets overlap in biology and leave them apart where they don't, but knowing which is which is the hard part.

**The idea.** Scanorama borrows from computer-vision panorama stitching. It searches for mutually-nearest-neighbour matches across all dataset pairs to find shared cell types, then merges only along those matched regions, like aligning photos only where they actually overlap. Datasets with no common cells simply aren't forced together, so heterogeneous collections integrate without inventing false correspondences.

**Why it matters.** Scanorama rounds out the integration trio with Harmony and Seurat's anchors, three geometrically different answers to batch correction, and a good illustration that "integrate the data" isn't one operation but a family with different failure modes. Its panorama analogy is also a reminder (echoing t-SNE/UMAP from vision, AlexNet's CNNs) of how often single-cell methods import ideas straight from computer vision.

**Verdict.** Foundational for scalable, heterogeneous integration; the overlap-aware design is its distinguishing strength. As always, the integrated space is a construct to interrogate, not take on faith. Read it as the panorama-stitching member of the integration toolkit.
