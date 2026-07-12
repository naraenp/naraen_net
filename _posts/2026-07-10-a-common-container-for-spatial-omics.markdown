---
layout: post
title: "A common container for spatial omics"
date: 2026-07-10 12:30:00 -0500
tags: [paper]
paper:
  title: "SpatialData: an open and universal data framework for spatial omics"
  authors: "Marconato et al."
  venue: "Nature Methods, 2024"
  link: "https://doi.org/10.1038/s41592-024-02212-x"
  verdict: "The unglamorous, essential layer — one on-disk format that makes Visium, Xenium, MERSCOPE, and CosMx speak the same language."
---

**The problem.** Every spatial platform ships its own file layout, its own coordinate conventions, its own idea of what an "image" and a "cell" are. Before you analyze anything you burn hours wrangling formats, and cross-platform comparison — exactly what the benchmarks demand — becomes a data-plumbing nightmare.

**The idea.** SpatialData defines a common, standards-based representation: images, labels, shapes (segmentation polygons), points (transcripts), and annotation tables, all stored on-disk in the Zarr / OME-NGFF ecosystem and tied together by explicit coordinate transformations. Load any supported technology into the *same* object model, keep everything spatially aligned, and hand it cleanly to Squidpy and Scanpy downstream.

**Why it matters.** This is the least flashy paper of the week and possibly the most facility-relevant. Data infrastructure *is* reproducibility — a shared format is what lets a core group standardize pipelines, archive results, and compare platforms without rewriting loaders each time. It's the same instinct as CRAM/BAM standards in genomics: the format is the quiet foundation everything else stands on.

**Verdict.** Important precisely because it's boring in the right way. The cost is real — adopting it means buying into the Zarr/NGFF stack and its still-maturing tooling — but for a lab that lives across platforms, that's the price of not drowning in format conversions. Read it as the storage layer under the whole spatial workflow.
