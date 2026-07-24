---
layout: post
title: "Workflows that reproduce themselves"
date: 2026-07-17 06:30:00 -0500
tags: [paper]
paper:
 title: "Nextflow enables reproducible computational workflows"
 authors: "Di Tommaso et al."
 venue: "Nature Biotechnology, 2017"
 link: "https://doi.org/10.1038/nbt.3820"
 verdict: "The framework my own pipelines are written in, the reason `aml_rnaseq_nf` and `variant_calling_nf` run the same way on my laptop and a cluster."
---

**The problem.** A bioinformatics analysis is a chain of a dozen tools, each with versions, parameters, and dependencies. Run it on a different machine, or six months later, and it quietly breaks or, worse, gives subtly different answers. Reproducibility, the whole point of a method, was the first casualty of real pipelines.

**The idea.** Nextflow models a pipeline as dataflow: processes connected by channels, where each process is an isolated task. It separates the workflow logic from the execution environment, so the same script runs unchanged on a laptop, an HPC scheduler, or the cloud, and it pairs with containers (Docker/Singularity) to pin every tool's exact version. Built-in caching means a failed run resumes instead of restarting.

**Why it matters.** This isn't background reading, it's the substrate I build on. Both my pipelines are Nextflow DSL2, and reading the founding paper articulates *why* the discipline I follow exists: portability and provenance aren't nice-to-haves, they're what make a pipeline trustworthy. The dataflow model is also just a clean way to think about analysis as connected, cacheable steps.

**Verdict.** Foundational to modern reproducible bioinformatics; Snakemake and WDL solve the same problem differently. Read it as the design philosophy behind my own tooling, and behind nf-core (next), the ecosystem that grew on top of it.
