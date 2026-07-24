---
layout: post
title: "Finding the somatic mutation"
date: 2026-07-22 11:45:00 -0500
tags: [paper]
paper:
 title: "Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples (MuTect)"
 authors: "Cibulskis et al."
 venue: "Nature Biotechnology, 2013"
 link: "https://doi.org/10.1038/nbt.2514"
 verdict: "Somatic variant calling done right, a Bayesian tumor-versus-normal test tuned to catch low-frequency mutations in impure, heterogeneous samples where germline callers fail."
---

**The problem.** Calling somatic mutations isn't germline calling. A tumor sample is a mix, normal-cell contamination, subclones at low fractions, so the real mutation may sit at a 10% or lower allele fraction, indistinguishable by naïve thresholds from sequencing error. You need to separate true somatic variants from artifacts and from germline variation, at sensitivities germline callers were never built for.

**The idea.** MuTect applies a Bayesian classifier at each site, comparing the evidence for a variant against the sequencing-error model, then contrasts the tumor against a matched normal to remove germline variants. A second stage of carefully tuned filters, for strand bias, nearby indels, mapping artifacts, buys high specificity. The payoff is sensitivity down to allele fractions of 0.1 and below, where subclones and impure samples live.

**Why it matters.** This is the somatic counterpart to the germline GATK stack behind my variant_calling_nf pipeline, same alignment inputs, different statistical question, and it's directly relevant to AML, where tracking subclonal mutations matters clinically. The low-allele-fraction sensitivity is exactly what tumor evolution and the mutational-signatures analysis (today's other cancer paper) depend on upstream.

**Verdict.** A foundational somatic caller (later folded into GATK's Mutect2); tumor-normal design and panel-of-normals choices drive its accuracy, and very low fractions remain hard. Read it as the tool that made low-frequency somatic mutation detection reliable.
