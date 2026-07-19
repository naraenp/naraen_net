---
layout: post
title: "Containers that run anywhere"
date: 2026-07-17 08:45:00 -0500
tags: [paper]
paper:
  title: "Singularity: Scientific containers for mobility of compute"
  authors: "Kurtz et al."
  venue: "PLoS ONE, 2017"
  link: "https://doi.org/10.1371/journal.pone.0177459"
  verdict: "The container runtime built for shared clusters — how a pinned software environment actually travels to HPC, where Docker can't go."
---

**The problem.** Containers (Docker) solved "ship the exact environment," but Docker needs root-level daemon privileges — a non-starter on shared academic HPC systems, where you're an unprivileged user among thousands. The very places that run big pipelines couldn't use the standard container tool. Reproducible environments needed a runtime that respects multi-tenant security.

**The idea.** Singularity (now Apptainer) is a container runtime designed for shared computing: containers run as the invoking user with no privilege escalation, images are single portable files, and it integrates cleanly with HPC schedulers and MPI. You build once, then run the identical environment on a laptop or a national supercomputer without a daemon or root.

**Why it matters.** This is the piece that lets my pipelines' pinned environments actually reach a cluster. Nextflow orchestrates, Bioconda/containers pin the tools, and Singularity is how those containers execute where the compute lives. Reading it closes the reproducibility stack: without an HPC-safe runtime, portability stops at my laptop. It's the unglamorous reason "runs anywhere" is literally true.

**Verdict.** Foundational to reproducible HPC bioinformatics and the default container runtime on academic clusters. A systems paper more than a science one, but essential plumbing. Read it as the "mobility of compute" layer my pipelines depend on to leave my machine.
