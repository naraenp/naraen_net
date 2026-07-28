---
layout: post
title: "From a locus to a gene"
date: 2026-07-28 11:00:00 -0500
tags: [paper]
paper:
 title: "Functional mapping and annotation of genetic associations with FUMA"
 authors: "Watanabe et al."
 venue: "Nature Communications, 2017"
 link: "https://doi.org/10.1038/s41467-017-01261-5"
 verdict: "A GWAS ends as a list of significant variants. FUMA is the platform that turns that list into candidate genes and functional context by joining it to annotation and regulatory data."
---

**The problem.** A finished GWAS gives significant variants, but most sit in noncoding regions and none come labeled with a gene or a mechanism. Pulling together the many resources needed to interpret them, linkage structure, effects on gene expression, chromatin state, and gene-set enrichment, meant stitching together separate tools and databases by hand for every study.

**The idea.** FUMA is a web platform that automates that interpretation. Its first stage groups the associated variants into independent loci and annotates each with predicted effects, expression-QTL links, and chromatin information, then nominates candidate genes. Its second stage takes the prioritized genes and tests them for enrichment in pathways and tissues, running a gene-level association step along the way. The point is integration: many annotation sources joined to the association result in one reproducible pass.

**Why it matters.** This is the last mile of a GWAS, the move from a statistical hit to a biological hypothesis, and it leans on the same annotation layer I read about for variant calling, VEP and the databases behind it, reused at population scale. It closes the arc of this batch: call variants, associate them, fine-map and colocalize, then annotate the survivors into genes.

**Verdict.** A widely used interpretation platform that saved the field a lot of manual joining. Read it as the annotation and prioritization end of the GWAS pipeline.
