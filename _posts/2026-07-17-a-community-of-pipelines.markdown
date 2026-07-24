---
layout: post
title: "A community of pipelines"
date: 2026-07-17 07:15:00 -0500
tags: [paper]
paper:
 title: "The nf-core framework for community-curated bioinformatics pipelines"
 authors: "Ewels et al."
 venue: "Nature Biotechnology, 2020"
 link: "https://doi.org/10.1038/s41587-020-0439-x"
 verdict: "The standards and community my pipelines are modelled on, how reproducibility scales from one person's workflow to a shared ecosystem."
---

**The problem.** Nextflow (previous post) gives you portable pipelines, but everyone still wrote their own from scratch, with idiosyncratic structure, no shared testing, and wildly varying quality. The reproducibility gains were real but siloed, a thousand incompatible RNA-seq pipelines, each subtly different.

**The idea.** nf-core is a community framework layered on Nextflow: a set of curated, peer-reviewed pipelines that all follow the same conventions, standardised parameters, bundled containers, continuous-integration tests, documentation, and versioned releases. Contributors build to a shared template and lint against it, so any nf-core pipeline is recognisable, tested, and reproducible by construction.

**Why it matters.** This is the model I deliberately follow. `aml_rnaseq_nf` and `variant_calling_nf` mirror the nf-core template and its reproducibility discipline on purpose, reading the paper is reading the rationale behind my own repo conventions. Ewels (also behind MultiQC, day 8) keeps showing up at exactly the "make good practice frictionless" layer, which is the layer I care most about as a pipeline builder.

**Verdict.** Foundational to how modern bioinformatics is shared and trusted; the template-plus-CI approach is why nf-core pipelines are safe to reuse. Read it as the community standard my own work is built to match, reproducibility as a social, not just technical, achievement.
