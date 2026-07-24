---
layout: post
title: "Segmentation as a graph problem"
date: 2026-07-10 08:20:00 -0500
tags: [paper]
paper:
 title: "Segger: fast and accurate cell segmentation for imaging-based spatial transcriptomics"
 authors: "Heidari et al."
 venue: "bioRxiv, 2025 (preprint)"
 link: "https://doi.org/10.1101/2025.03.14.643160"
 verdict: "A newer, graph-neural take on segmentation aimed squarely at Baysor's speed-and-scale ceiling, reading it as the 'what's next' after the baseline."
---

**The problem.** Baysor made molecule-level segmentation the right frame, but imaging panels keep growing, millions of transcripts, whole slides, and the probabilistic-model approach gets expensive. The open question is whether you can get boundaries that are as good, or better, at a fraction of the compute.

**The idea.** Segger reframes segmentation as a learning-on-graphs problem: transcripts and nuclei become nodes, spatial proximity becomes edges, and a graph neural network learns to assign each transcript to a cell. The pitch is that this scales to large datasets and exploits nuclear priors and molecular identity jointly, rather than running a slower per-dataset inference.

**Why it matters.** Segmentation is the make-or-break step, and the tooling is moving fast, so staying current on the *methods*, not just the vendor defaults, is exactly the value a facility person adds. Being able to say "here's the baseline, here's the newer graph method, here's when each wins" is the recommendation a core group actually needs.

**Verdict.** This is a 2025 preprint, so I'm reading it at the level of *approach and claim* rather than trusting specific benchmark numbers before it's peer-reviewed and independently reproduced. Promising direction; I'd want to see it evaluated head-to-head with Baysor on a public Xenium set, ideally my own, before recommending it. Flagged as one to verify carefully against the PDF.
