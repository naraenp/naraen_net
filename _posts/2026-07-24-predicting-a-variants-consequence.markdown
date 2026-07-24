---
layout: post
title: "Predicting a variant's consequence"
date: 2026-07-24 09:00:00 -0500
tags: [paper]
paper:
 title: "The Ensembl Variant Effect Predictor"
 authors: "McLaren et al."
 venue: "Genome Biology, 2016"
 link: "https://doi.org/10.1186/s13059-016-0974-4"
 verdict: "Ensembl's annotation engine: maps each variant to the genes and transcripts it hits, predicts the effect, and takes plugins for extra evidence."
---

**The problem.** A VCF gives you positions and alleles, not meaning. To act on a variant you need to know which gene and transcript it lands in, whether it changes a protein, hits a splice site, or falls in a regulatory region. Doing this by hand against the current gene models is slow and easy to get wrong.

**The idea.** VEP takes a set of variants and reports their consequences against Ensembl's transcript models. For each variant it lists every overlapping transcript and the predicted effect on each, since one position can be coding in one isoform and not in another. A plugin system adds outside evidence: pathogenicity scores, population frequencies, and conservation. It runs at the command line inside a pipeline or through a web interface.

**Why it matters.** This is the annotation step, the same job SnpEff does (day 7), and knowing both means I can justify which one a pipeline uses. VEP sits right after variant calling in `variant_calling_nf`, turning coordinates into biology I can prioritize. Its transcript-by-transcript output is the honest version of "what does this variant do," since the answer depends on the isoform.

**Verdict.** A thorough, well-maintained annotator tied to the Ensembl release cycle. That thoroughness makes it heavier and slower than lighter tools. Read it next to SnpEff as the two main ways to turn a VCF into consequences.
