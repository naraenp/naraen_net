---
layout: post
title: "The airway dataset everyone learns on"
date: 2026-07-13 14:30:00 -0500
tags: [paper]
paper:
 title: "RNA-Seq transcriptome profiling identifies CRISPLD2 as a glucocorticoid responsive gene in airway smooth muscle cells (airway)"
 authors: "Himes et al."
 venue: "PLoS ONE, 2014"
 link: "https://doi.org/10.1371/journal.pone.0099625"
 verdict: "The 'airway' dataset, the one every DESeq2 tutorial runs on, so worth reading as the biology behind the example I've typed a hundred times."
---

**The problem.** Glucocorticoids are frontline asthma drugs, but which genes they act on in airway smooth muscle, and how, wasn't fully mapped. Himes and colleagues used RNA-seq to profile treated versus untreated cells and find the responsive genes, landing on CRISPLD2 as a mediator.

**The idea.** A clean, small, paired design: four cell lines, treated and control, RNA-seq, standard differential expression. Nothing methodologically novel, which is exactly why it became a teaching fixture. The processed counts ship as the Bioconductor `airway` dataset, the default example for DESeq2 and countless RNA-seq tutorials.

**Why it matters.** I've almost certainly run DESeq2 on these counts while learning the tool, without registering the underlying study. Reading the paper puts biology back under the example: the numbers in the tutorial are a real asthma-drug experiment, not abstract test data. It's a small correction to how I think about "toy" datasets, they're someone's actual result.

**Verdict.** Modest as biology, outsized as infrastructure, its second life as `airway` is why it's on this list. Read it to connect the workflow I practice on to the question it was answering, and to respect that benchmark datasets carry real experimental design worth understanding.
