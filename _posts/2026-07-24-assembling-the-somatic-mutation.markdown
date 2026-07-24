---
layout: post
title: "Assembling the somatic mutation"
date: 2026-07-24 05:00:00 -0500
tags: [paper]
paper:
 title: "Calling Somatic SNVs and Indels with Mutect2"
 authors: "Benjamin et al."
 venue: "bioRxiv, 2019"
 link: "https://doi.org/10.1101/861054"
 verdict: "The assembly-based successor to MuTect: local reassembly plus filters that work with or without a matched normal."
---

**The problem.** Somatic mutations sit at low fraction in a mixed tumor sample, buried under sequencing error and normal contamination. The first MuTect found substitutions well but treated bases one at a time. Indels and clustered changes need the reads reassembled into whole haplotypes to be seen clearly.

**The idea.** Mutect2 brings GATK's local assembly to somatic calling. It rebuilds candidate haplotypes from the reads in a window, then scores each against models for a real mutation, a sequencing artifact, and germline variation. A set of filters handles the ways somatic calls go wrong: strand and orientation artifacts, contamination, and germline leakage. It runs with a matched normal, with a panel of normals, or on the tumor alone, trading confidence for flexibility.

**Why it matters.** This is the caller I would reach for on AML tumor-normal data, and it sits right next to MuTect (day 16) and Strelka2 in my reading. The assembly step is the same idea as GATK's germline HaplotypeCaller, reused for cancer. Understanding its filters explains why raw somatic calls always need a second cleaning pass before I trust them.

**Verdict.** The current standard for somatic small-variant calling, and the reason MuTect's name persists. It depends heavily on its filters and a good normal or panel. Read it as germline haplotype assembly turned toward cancer.
