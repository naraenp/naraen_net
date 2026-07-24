---
layout: post
title: "Cataloguing the switches"
date: 2026-07-15 03:35:00 -0500
tags: [paper]
paper:
 title: "The Human Transcription Factors"
 authors: "Lambert et al."
 venue: "Cell, 2018"
 link: "https://doi.org/10.1016/j.cell.2018.01.029"
 verdict: "The definitive census of the proteins that switch genes on and off, the regulators behind every expression change I measure."
---

**The problem.** Transcription factors are the master switches of gene expression, but the human set was surprisingly poorly defined: estimates of how many there are, which proteins qualify, and what each binds varied across databases. Without a curated, authoritative list, reasoning about gene regulation starts from shaky ground.

**The idea.** Lambert and colleagues systematically reviewed the human proteome for sequence-specific DNA-binding transcription factors, curating a definitive catalogue (~1,600) with their DNA-binding domains and, where known, their binding motifs and evidence quality. It's a reference work, the authoritative answer to "is this protein a TF, and what does it bind?"

**Why it matters.** This closes the regulatory loop running through this week: ENCODE mapped regulatory elements, ATAC-seq measures which are accessible, and transcription factors are what act on them to produce the expression changes DESeq2 quantifies. When a differential-expression result points upstream to a regulator, this catalogue is where you check what that regulator is and does. It connects the "what changed" of my RNA-seq to the "what drove it."

**Verdict.** Foundational as a reference resource rather than a method, its value is authority and curation. Read it to ground regulatory reasoning in a definitive list, and as the human-gene-regulation counterpart to the ENCODE/ATAC-seq assays from earlier this week.
