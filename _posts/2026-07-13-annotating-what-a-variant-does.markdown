---
layout: post
title: "Annotating what a variant does"
date: 2026-07-13 09:15:00 -0500
tags: [paper]
paper:
 title: "A program for annotating and predicting the effects of single nucleotide polymorphisms, SnpEff"
 authors: "Cingolani et al."
 venue: "Fly, 2012"
 link: "https://doi.org/10.4161/fly.19695"
 verdict: "The step that turns GATK's coordinates into biology, the annotation layer that sits directly downstream of my variant pipeline."
---

**The problem.** A variant caller hands you a position and an allele, chr7, this base is A not G. That's a coordinate, not a consequence. Is it in a gene? Does it change an amino acid, hit a splice site, or fall in an untranslated region? Without that layer, a VCF is a list you can't prioritise.

**The idea.** SnpEff takes a VCF and a genome annotation and predicts each variant's functional effect, synonymous vs. missense vs. nonsense, the affected transcript, the protein change, and bins them by predicted impact. It's fast enough to annotate whole-genome call sets and standardised enough to feed downstream filtering.

**Why it matters.** This is the natural next step after `variant_calling_nf`: GATK produces the calls, SnpEff tells me which ones might *matter*. Reading it makes the pipeline's end-to-end logic concrete, align (BWA), call (GATK), annotate (SnpEff), prioritise, each stage answering a different question about the same base change. It's the bridge from "where does this sample differ" to "so what."

**Verdict.** Foundational and practical; VEP is the common alternative with a similar role. Read it for the vocabulary of variant effects, the categories every clinical or research filter downstream is built on.
