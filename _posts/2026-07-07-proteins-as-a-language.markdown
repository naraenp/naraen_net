---
layout: post
title: "Proteins as a language"
date: 2026-07-07 15:20:00 -0500
tags: [paper]
published: false
paper:
  title: "Evolutionary-scale prediction of atomic-level protein structure with a language model (ESM-2 / ESMFold)"
  authors: "Lin et al. (Meta AI / ESM)"
  venue: "Science, 2023"
  link: "https://doi.org/10.1126/science.ade2574"
  verdict: "Structure straight from a sequence model, no alignment — the 'LLM for proteins' idea made concrete."
---
<!-- DRAFT — AI-generated sample review for the paper-a-day comparison exercise. Held at published:false; verify against your own reading before shipping. -->

**The problem.** AlphaFold2 is accurate but leans on a multiple-sequence alignment per target, which is slow to build and thin for orphan or designed sequences. Could a model learn enough biology from *raw sequences alone* to skip the MSA entirely?

**The idea.** Train a large protein **language model** — ESM-2, scaled up to ~15B parameters — on hundreds of millions of sequences with a masked-token objective: predict the hidden amino acid from context. No structural labels. Structure emerges *implicitly* in the internal representations, and a folding head (**ESMFold**) reads those representations to predict atomic coordinates directly from a single sequence. It's less accurate than AlphaFold2 on hard targets but roughly an order of magnitude faster, and — because there's no MSA step — it scales to sequences evolution barely samples. They used it to fold ~600 million metagenomic proteins into the ESM Metagenomic Atlas.

**Why it matters.** This is the paper that makes the "proteins are a language" analogy literal, and it maps directly onto the LLM machinery I already work with in Bench: tokens (residues), self-supervised pretraining, emergent structure in embeddings, and the scale-versus-accuracy trade you make when you want to run over *everything* rather than one target well. The representations themselves — not just the folds — are the reusable asset, exactly like text embeddings.

**Verdict.** Important as an idea and as infrastructure for scale, with an honest ceiling: on individual well-aligned targets AlphaFold2 still wins on accuracy, and single-sequence folding degrades on the hardest cases. The right read is "different tool for a different regime," not "replacement." A clean conceptual pairing with AlphaFold2 and with the inverse-design models.
