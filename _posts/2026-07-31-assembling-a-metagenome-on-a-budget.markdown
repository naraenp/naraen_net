---
layout: post
title: "Assembling a metagenome on a budget"
date: 2026-07-31 07:00:00 -0500
tags: [paper]
paper:
 title: "MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph"
 authors: "Li et al."
 venue: "Bioinformatics, 2015"
 link: "https://doi.org/10.1093/bioinformatics/btv033"
 verdict: "Assembling a metagenome usually meant a compute cluster and a lot of memory. MEGAHIT fits the graph into a compact form and does the job on a single machine."
---

**The problem.** Profiling tells you what is in a sample, but to recover whole genes and genomes you have to assemble the reads into contigs. Metagenome assembly is harder than single-genome assembly: coverage is very uneven across species, closely related strains blur the graph, and the de Bruijn graph for a deep sample is enormous. The standard tools needed large memory nodes, which put assembly out of reach for many labs.

**The idea.** MEGAHIT stores the de Bruijn graph in a succinct data structure that represents the same graph in a fraction of the space. It assembles across a range of k-mer sizes, small k values to bridge low-coverage regions and larger k to resolve repeats, merging the results. The compact representation is what lets a complex soil or gut metagenome assemble on one server rather than a cluster, and quickly.

**Why it matters.** Making assembly cheap in memory is what put metagenome-assembled genomes within reach of ordinary hardware, and it is the same succinct-index thinking that makes read aligners small. Assembly is the gate to everything downstream: gene catalogs, binning, new genomes.

**Verdict.** The assembler you reach for when memory is the constraint. Read it for the succinct de Bruijn graph.
