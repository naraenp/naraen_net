---
layout: post
title: "Silencing genes without cutting"
date: 2026-07-27 05:00:00 -0500
tags: [paper]
paper:
 title: "Repurposing CRISPR as an RNA-guided platform for sequence-specific control of gene expression"
 authors: "Qi et al."
 venue: "Cell, 2013"
 link: "https://doi.org/10.1016/j.cell.2013.02.022"
 verdict: "Break Cas9's scissors and it becomes a programmable roadblock: dCas9 that blocks transcription without changing the DNA. This is CRISPRi, the start of CRISPR as a control knob."
---

**The problem.** Cas9 cuts DNA, which is powerful but permanent. Often you do not want to destroy a gene, you want to turn it down and study what happens, or dial it back up. Could the same easy targeting be used to control expression rather than to break the sequence?

**The idea.** The authors disabled the two nuclease domains of Cas9, making a "dead" Cas9 (dCas9) that still binds wherever its guide RNA points but no longer cuts. Parked on or near a gene, dCas9 physically blocks RNA polymerase, so transcription stalls. This is CRISPR interference, CRISPRi. Because targeting is set by a short guide RNA, you can silence any gene by swapping the guide, and the effect is reversible since the DNA is untouched.

**Why it matters.** This turns CRISPR from a cutter into a general control platform. Fuse an activator instead of a repressor and you get CRISPRa; the dCas9 chassis is the same idea behind base and prime editing later, where the payload changes but the targeting stays. For synthetic biology it means you can tune a circuit without rewriting the DNA.

**Verdict.** A foundational method that reframed what CRISPR is for. Read it as the pivot from editing to programmable gene control.
