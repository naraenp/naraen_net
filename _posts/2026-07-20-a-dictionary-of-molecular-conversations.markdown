---
layout: post
title: "A dictionary of molecular conversations"
date: 2026-07-20 06:30:00 -0500
tags: [paper]
paper:
  title: "CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes"
  authors: "Efremova et al."
  venue: "Nature Protocols, 2020"
  link: "https://doi.org/10.1038/s41596-020-0292-x"
  verdict: "The curated ligand–receptor repository plus a permutation test that turned 'which cell types talk to each other' into a routine analysis — the entry point to cell–cell communication."
---

**The problem.** Once you have cell types from a single-cell atlas, the next question is which ones signal to which — but a receptor is often a multi-subunit complex, and naïvely pairing single genes misrepresents the biology. You need a reference that knows a functional receptor requires all its subunits expressed, and a way to say an interaction is *enriched* rather than incidental.

**The idea.** CellPhoneDB is two things: a hand-curated database of ligands, receptors, and their interactions that respects heteromeric complex structure, and a statistical framework that permutes cell-type labels to test whether a ligand–receptor pair is specifically enriched between two cell types. Only when every subunit is expressed does the complex count, so the calls reflect assembled receptors, not lone transcripts.

**Why it matters.** This is the on-ramp for the whole cell–cell communication field, and it reframes an atlas from a catalogue of cells into a network of interactions — exactly the shift the STU cares about when a tissue's function is the conversation between its cell types. It pairs naturally with the clustering and annotation methods from earlier days: cluster, label, then ask who signals.

**Verdict.** Foundational and heavily used; its weakness is that expression co-occurrence isn't spatial proximity, which is what pushes the field toward the spatially-aware methods that follow. Read it as the vocabulary of cell–cell signaling, the dictionary the later methods speak from.
