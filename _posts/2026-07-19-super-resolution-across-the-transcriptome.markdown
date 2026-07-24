---
layout: post
title: "Super-resolution across the transcriptome"
date: 2026-07-19 00:40:00 -0500
tags: [paper]
paper:
 title: "Transcriptome-scale super-resolved imaging in tissues by RNA seqFISH+"
 authors: "Eng et al."
 venue: "Nature, 2019"
 link: "https://doi.org/10.1038/s41586-019-1049-y"
 verdict: "Imaging-based spatial pushed toward whole-transcriptome, the attempt to have both resolution and breadth at once."
---

**The problem.** Imaging methods like MERFISH give single-molecule resolution but on targeted panels; capture methods give whole-transcriptome coverage but coarse resolution. The obvious wish is both, thousands of genes *and* subcellular precision. The obstacle is optical crowding: image ten thousand genes at once and the fluorescent spots overlap into an unreadable blur.

**The idea.** seqFISH+ beats the crowding limit by spreading signals across many more pseudocolours read out over sequential rounds, so at any instant only a sparse subset of molecules fluoresces and spots stay separable. Combined with super-resolution, this scales in-situ imaging toward the whole transcriptome (~10,000 genes) while keeping single-molecule, subcellular localisation.

**Why it matters.** This directly addresses the core spatial trade-off from MERFISH, resolution *versus* breadth, by attacking the physical bottleneck (crowding) rather than accepting it. For the STU's evaluation of platforms, seqFISH+ marks how far the imaging branch can push toward transcriptome scale, and what it costs (imaging rounds, time, complexity). It's the ambitious end of imaging-based spatial.

**Verdict.** Foundational as a proof that imaging can approach transcriptome scale; throughput and complexity keep it more a research method than a routine platform. Read it as the "have it both ways" attempt on the spatial spectrum, and the context for why commercial platforms still choose targeted panels.
