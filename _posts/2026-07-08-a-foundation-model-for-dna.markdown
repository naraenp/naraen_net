---
layout: post
title: "A foundation model for DNA"
date: 2026-07-08 09:15:00 -0500
tags: [paper]
paper:
  title: "Sequence modeling and design from molecular to genome scale with Evo"
  authors: "Nguyen, Poli, Durrant, et al. (Arc Institute / Stanford; Hsu & Hie)"
  venue: "Science, 2024"
  link: "https://doi.org/10.1101/2024.02.27.582234"
  verdict: "The genomics-foundation-model frontier where prediction and generative design finally meet at single-nucleotide resolution."
---

**The problem.** Protein language models learned to read amino acids. But DNA is the more general substrate — genes, regulatory elements, ncRNAs, whole operons — and modeling it at *single-nucleotide* resolution across long ranges had been out of reach. Could one model read and *write* DNA from molecule to genome scale?

**The idea.** Evo is a 7-billion-parameter model trained on millions of prokaryotic and phage genomes at byte-level (single-nucleotide) resolution, with a context window into the 100-kilobase range. The architectural trick is **StripedHyena** — a hybrid of data-controlled convolutions and attention — which buys long context at single-nt resolution without a pure transformer's quadratic cost. It does zero-shot prediction (the fitness effect of mutations across coding, non-coding, and regulatory sequence) *and* generation: it designs plausible CRISPR–Cas systems, transposons, and even megabase-scale genomic sequence.

**Why it matters.** This is where my own world (genomic pipelines producing sequence) meets the model world head-on. The same tokens-and-embeddings machinery I use over text and proteins, applied to the most fundamental sequence of all — and it's *generative*, so it points at design, not just annotation. It's the natural DNA-scale companion to AlphaFold and ESM, and the most concrete argument that a "read/write" interface to genomes is coming.

**Verdict.** Genuinely a frontier result, and refreshingly honest about the gap that matters: generated sequences are *plausible*, not *validated* — a model that produces genome-shaped text is not a model that produces a living organism. It's also prokaryote-centric for now. Read it for where the field is heading, and hold the "does it fold / does it live" skepticism the design papers earned. Ties directly to where my pipelines could feed or consume such a model.
