---
layout: post
title: "Annotating variants against many databases"
date: 2026-07-24 09:45:00 -0500
tags: [paper]
paper:
 title: "ANNOVAR: functional annotation of genetic variants from high-throughput sequencing data"
 authors: "Wang, Li & Hakonarson"
 venue: "Nucleic Acids Research, 2010"
 link: "https://doi.org/10.1093/nar/gkq603"
 verdict: "Cross-references variants against gene models and a stack of annotation databases, fast, which made it a filtering staple."
---

**The problem.** Knowing a variant's effect on a gene is only the first question. The next ones are practical: is it already in dbSNP, how common is it in the population, does it sit in a conserved region, and what score do prediction tools give it. Each answer lives in a different database, and joining them by hand does not scale to a whole exome.

**The idea.** ANNOVAR runs three kinds of annotation. Gene-based annotation tells you the effect on transcripts. Region-based annotation asks whether a variant falls in a feature such as a conserved element. Filter-based annotation checks each variant against databases of known variation and precomputed scores. It is built to run fast over millions of variants and to accept new databases as they appear, so the same tool keeps up as resources grow.

**Why it matters.** ANNOVAR is the filtering layer that turns a raw call set into a short list worth looking at, downstream of VEP or SnpEff in a variant pipeline. For AML work, filtering against population frequency is how you separate a rare candidate driver from common background variation. It taught a generation of pipelines the habit of annotating against many sources at once.

**Verdict.** A fast, flexible annotator that became a default despite its many-database setup. Keeping its reference data current is the real maintenance cost. Read it as the tool that made large-scale variant filtering routine.
