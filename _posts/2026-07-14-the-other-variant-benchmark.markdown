---
layout: post
title: "The other variant benchmark"
date: 2026-07-14 14:30:00 -0500
tags: [paper]
paper:
 title: "A reference data set of 5.4 million phased human variants (Platinum Genomes, NA12878)"
 authors: "Eberle et al."
 venue: "Genome Research, 2017"
 link: "https://doi.org/10.1101/gr.210500.116"
 verdict: "A second, independently constructed truth set, and a lesson in why validation shouldn't lean on a single benchmark."
---

**The problem.** A truth set is only as trustworthy as the assumptions behind it. If everyone validates variant callers against one reference (say, GIAB), systematic blind spots in that reference become invisible, the whole field agrees on the same wrong answers. Independent benchmarks, built differently, are how you check.

**The idea.** Platinum Genomes derives a high-confidence variant set for NA12878 using a fundamentally different principle: pedigree consistency. By sequencing a family and requiring variants to segregate according to Mendelian inheritance, it flags calls that violate the pedigree as suspect, yielding millions of phased, validated variants with an orthogonal notion of "confident."

**Why it matters.** For validating `variant_calling_nf`, having Platinum alongside GIAB means I can check a caller against two independently constructed answer keys. Where they agree, I'm confident; where they differ, there's something to understand about the benchmark, not just the caller. Reading it reinforces a habit that generalises well beyond variants: never trust a single gold standard.

**Verdict.** Foundational for rigorous variant-calling evaluation, and a neat demonstration of using inheritance as a validation signal, the same Mendelian logic from day 5, put to work. Read it paired with GIAB as the two-benchmark discipline.
