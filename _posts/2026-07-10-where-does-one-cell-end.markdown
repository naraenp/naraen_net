---
layout: post
title: "Where does one cell end?"
date: 2026-07-10 07:30:00 -0500
tags: [paper]
paper:
 title: "Cell segmentation in imaging-based spatial transcriptomics (Baysor)"
 authors: "Petukhov et al."
 venue: "Nature Biotechnology, 2022"
 link: "https://doi.org/10.1038/s41587-021-01044-w"
 verdict: "The paper that made segmentation a first-class problem in imaging spatial data, and the tool most people reach for first."
---

**The problem.** In imaging assays you don't get cells, you get a cloud of transcript coordinates. Assigning each molecule to the right cell is *the* load-bearing step, and doing it off nuclear stains alone throws away the molecular signal and misassigns transcripts at every boundary.

**The idea.** Baysor segments from the molecules themselves. It models the joint distribution of transcript positions and identities as a Markov random field, so a molecule's neighbors and its expression *type* both inform which cell it belongs to. Nuclear or membrane stains, when available, enter as a prior rather than the sole truth. The output is cell boundaries that respect the actual RNA, not just the DAPI.

**Why it matters.** This is the step where a Xenium or MERSCOPE dataset silently goes wrong, over- or under-segmentation contaminates every downstream count, cluster, and cell-type call. For a facility, owning segmentation quality is non-negotiable, and Baysor is the reference point I'd benchmark any newer method against. It's also the natural sequel to yesterday's QC reading: QC tells you *if* segmentation failed, this tells you how to do it better.

**Verdict.** Foundational and still the default, though it's compute-hungry and its priors need tuning per assay. Read it as the segmentation baseline; the newer graph-based methods are the next two entries, and this is what they're trying to beat.
