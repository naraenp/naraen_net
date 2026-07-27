---
layout: post
title: "Knocking out every gene at once"
date: 2026-07-27 07:00:00 -0500
tags: [paper]
paper:
 title: "Genome-scale CRISPR-Cas9 knockout screening in human cells"
 authors: "Shalem et al."
 venue: "Science, 2014"
 link: "https://doi.org/10.1126/science.1247005"
 verdict: "Point CRISPR at every gene in the genome at the same time and let selection tell you which ones matter. The GeCKO library turned editing into a screening method."
---

**The problem.** Editing one gene tells you about one gene. Biology often asks the reverse question: out of all genes, which ones are needed for a cell to survive, or which ones, when lost, let a cell escape a drug? Testing genes one at a time does not scale to a whole genome.

**The idea.** The authors built GeCKO, a library of tens of thousands of guide RNAs covering every human gene with several guides each, delivered so that each cell receives one guide and knocks out one gene. Grown as a pool under a selective pressure, cells with useful knockouts grow out and cells with harmful ones drop away. Sequencing the guides before and after reads which genes changed a cell's fate. They demonstrated it on essential genes and on resistance to a melanoma drug.

**Why it matters.** This is functional genomics at genome scale, and it inverts the usual workflow: instead of studying a gene you suspect, you let the screen nominate genes for you. It leans directly on the multiplex editing from Cong 2013, and it sets up the next paper, which is about how you actually analyze the counts a screen produces.

**Verdict.** A field-defining method that made pooled CRISPR screens routine. Read it for the design, then read MAGeCK for the statistics.
