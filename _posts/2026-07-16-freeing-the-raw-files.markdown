---
layout: post
title: "Freeing the raw files"
date: 2026-07-16 11:00:00 -0500
tags: [paper]
paper:
 title: "ThermoRawFileParser: Modular, Scalable, and Cross-Platform RAW File Conversion"
 authors: "Hulstaert et al."
 venue: "J. Proteome Research, 2020"
 link: "https://doi.org/10.1021/acs.jproteome.9b00328"
 verdict: "The unglamorous converter that lets proteomics pipelines run anywhere, open formats as a reproducibility act."
---

**The problem.** Mass spectrometers write proprietary, vendor-specific binary files (Thermo's `.raw`). Historically, converting these to open formats (mzML) for analysis required the vendor's Windows-only software, a hard dependency that blocks reproducible, cross-platform, cloud, or containerised proteomics workflows. The data is locked behind an OS.

**The idea.** ThermoRawFileParser is an open, cross-platform tool that reads Thermo RAW files and converts them to open standards without the proprietary stack, runnable on Linux, in containers, and in automated pipelines. Modular and scriptable, it removes the Windows-only bottleneck at the very start of the analysis chain.

**Why it matters.** This is small but load-bearing, and it rhymes with everything I value about pipeline design: open formats (like OpenMS's mzML), containerisability, and reproducibility from the first step. It's the proteomics analogue of insisting on open, portable inputs in my Nextflow pipelines, you can't have a reproducible workflow if step one needs a specific desktop OS. Format freedom is infrastructure.

**Verdict.** Foundational to reproducible, cross-platform proteomics, a utility, but the kind that quietly unblocks entire workflows. Read it as the on-ramp that makes the rest of the open MS toolchain (OpenMS, MSFragger) usable in a modern, containerised pipeline. A fitting, infrastructural close to the arc.
