---
layout: post
title: "From who is there to what they do"
date: 2026-07-31 06:00:00 -0500
tags: [paper]
paper:
 title: "Species-level functional profiling of metagenomes and metatranscriptomes (HUMAnN2)"
 authors: "Franzosa et al."
 venue: "Nature Methods, 2018"
 link: "https://doi.org/10.1038/s41592-018-0176-y"
 verdict: "Knowing which species are present is half the story. HUMAnN2 measures which gene families and pathways are active, and attributes each one back to the species carrying it."
---

**The problem.** A taxonomic profile says who is in a community but not what it can do. Two samples with different species can run the same metabolism, and the same species can behave differently between sites. Answering the functional question by aligning every read against a full protein database is slow, and a plain functional table loses track of which organism contributes each capability.

**The idea.** HUMAnN2 uses a tiered search. It first identifies the species present, pulls their known pangenomes, and maps reads against just those, which is fast and specific. Reads that do not map there fall through to a translated search against a broad protein database, so novel or unclassified content is still counted. The result is abundances of gene families and metabolic pathways, stratified by the species that supply them. The same machinery runs on metatranscriptomes, so expression can be compared against gene content.

**Why it matters.** This is the step that turns a census into a function map, and the species stratification is what makes it mechanistic rather than a bulk average. It connects the community back to metabolism, which is where microbiome work meets engineering questions.

**Verdict.** The standard functional profiler for shotgun data. Read it for the tiered search, which balances speed against catching the unknown.
