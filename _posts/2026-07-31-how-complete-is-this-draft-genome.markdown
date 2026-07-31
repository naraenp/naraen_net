---
layout: post
title: "How complete is this draft genome"
date: 2026-07-31 10:00:00 -0500
tags: [paper]
paper:
 title: "CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes"
 authors: "Parks et al."
 venue: "Genome Research, 2015"
 link: "https://doi.org/10.1101/gr.186072.114"
 verdict: "A binned genome is a claim, not a fact. CheckM measures how complete it is and how much foreign sequence crept in, using genes that every genome in a lineage should carry exactly once."
---

**The problem.** Binning produces draft genomes, but some are missing half their content and some are two organisms merged by mistake. Before you build on a metagenome-assembled genome you need to know two things: how complete it is, and how contaminated. Without a reference for an uncultured organism, there is nothing obvious to compare against, so the quality question looks unanswerable.

**The idea.** CheckM uses marker genes that are expected in single copy across a lineage. It places a genome on a reference tree, picks the set of single-copy markers appropriate to that lineage, and counts them. Markers that are present measure completeness. Markers that appear more than once measure contamination, since a clean single genome should carry each exactly once. Reporting both as percentages gives every draft a pair of numbers that the field now quotes as standard.

**Why it matters.** These two numbers are the gate that separates a usable genome from an artifact, and they made large MAG collections filterable and comparable. Using conserved single-copy genes as an internal ruler is a clean idea that reappears wherever you need to judge completeness without a reference.

**Verdict.** The quality check every MAG passes through. Read it for the lineage-specific single-copy marker sets.
