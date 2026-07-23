---
layout: post
title: "The fingerprints of mutation"
date: 2026-07-22 11:00:00 -0500
tags: [paper]
paper:
  title: "Signatures of mutational processes in human cancer"
  authors: "Alexandrov et al."
  venue: "Nature, 2013"
  link: "https://doi.org/10.1038/nature12477"
  verdict: "Decomposes the mutations in thousands of tumors into recurring patterns — each the fingerprint of a distinct mutational process — turning a catalogue of variants into readable cancer etiology."
---

**The problem.** A tumor genome carries thousands of somatic mutations, the accumulated residue of many processes: UV damage, tobacco carcinogens, defective repair, ageing, enzymatic editing. Listed as a pile of variants they're just noise. Buried in them, though, are systematic patterns — which base changes, in which sequence contexts — that each process leaves behind. Could you separate the overlapping fingerprints?

**The idea.** Represent each tumor's mutations as a spectrum over the 96 trinucleotide-context substitution types, stack thousands of tumors into a matrix, and factorize it (non-negative matrix factorization) into a small set of component signatures plus per-tumor exposures. Applied to ~5 million mutations across 7,042 cancers, this extracted 20-plus distinct signatures — some universal (an APOBEC-editing signature, an ageing clock), others confined to specific cancer types — each linkable to a biological process.

**Why it matters.** This is cancer genomics turning variant calls into mechanism, and it connects straight to my own interests: the somatic-variant pipelines I read about (MuTect today, the germline GATK stack earlier) produce exactly the mutation lists this method interprets, and AML has its own signature structure. It's the same decompose-into-latent-factors idea as MOFA+ or NMF-based deconvolution, applied to mutational spectra.

**Verdict.** A landmark that founded the mutational-signatures field (now the COSMIC catalogue); signatures are statistical constructs whose biological attribution needs care, and extraction depends on cohort and method. Read it as the fingerprints that tell you *how* a cancer's genome was damaged.
