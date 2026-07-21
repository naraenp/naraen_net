---
layout: post
title: "From ligand to downstream gene"
date: 2026-07-20 08:10:00 -0500
tags: [paper]
paper:
  title: "NicheNet: modeling intercellular communication by linking ligands to target genes"
  authors: "Browaeys et al."
  venue: "Nature Methods, 2020"
  link: "https://doi.org/10.1038/s41592-019-0667-5"
  verdict: "Goes past 'these two cells could signal' to 'this ligand is actually changing these genes in the receiver' — communication tied to its downstream regulatory effect."
---

**The problem.** Ligand–receptor tools (CellPhoneDB, CellChat) infer that a signal *could* pass between two cell types from co-expression. But co-expression isn't proof of an active signal, and it says nothing about consequence. What you often want is the reverse inference: given genes that changed in a receiver cell, which ligands from neighbours best explain that change?

**The idea.** NicheNet builds a prior model linking ligands to downstream target genes by integrating existing signaling and gene-regulatory network knowledge — not just the receptor step, but the path from receptor to transcriptional response. Given a set of differentially expressed genes in the receiver, it ranks candidate ligands by how well their predicted targets match the observed changes, surfacing the ligands most likely to be driving the response.

**Why it matters.** This reframes communication as a regulatory question, which is the framing that connects to the network-biology thread (Geneformer, the TF work) and to differential expression — the receiver's DE signature, the same kind of signal DESeq2 produces, becomes the evidence. For the STU, predicting *which* niche signal is reshaping a cell's program is more actionable than a list of possible contacts.

**Verdict.** A distinctive, widely-used complement to the co-expression tools; its predictions inherit the coverage and biases of the prior networks it's built on, so ranked ligands are hypotheses to test. Read it as communication analysis that reaches into the receiver cell's regulatory program.
