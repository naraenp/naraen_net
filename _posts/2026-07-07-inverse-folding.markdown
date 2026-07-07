---
layout: post
title: "Inverse folding"
date: 2026-07-07 15:55:00 -0500
tags: [paper]
published: false
paper:
  title: "Robust deep learning–based protein sequence design using ProteinMPNN"
  authors: "Dauparas et al. (Baker lab)"
  venue: "Science, 2022"
  link: "https://doi.org/10.1126/science.add2187"
  verdict: "The workhorse that answers the design question: given a shape, what sequence folds to it?"
---
<!-- DRAFT — AI-generated sample review for the paper-a-day comparison exercise. Held at published:false; verify against your own reading before shipping. -->

**The problem.** Structure prediction runs sequence → structure. Protein *design* needs the inverse: you have a backbone you want (a fold, a binder, a scaffold), and you need an amino-acid sequence that will actually fold to it. Physics-based design (Rosetta) worked but was slow and often failed.

**The idea.** ProteinMPNN is a **message-passing graph neural network** over the backbone: each residue is a node, geometric relationships are edges, and the model autoregressively predicts amino acids conditioned on the structure and the residues already chosen. It's fast, order-agnostic in its decoding, and can tie or fix positions for symmetry and constraints. The headline numbers: native sequence recovery around 52% versus ~33% for Rosetta, and — more tellingly — it experimentally *rescues* designs that Rosetta and even AlphaFold-guided pipelines couldn't get to fold, often just by redesigning the sequence for an existing backbone.

**Why it matters.** This is the "Learn"-adjacent design tool that pairs with generative backbone models: RFdiffusion (or another method) proposes a shape, ProteinMPNN dresses it in a sequence, and a predictor checks it. It's the concrete counterpart to AlphaFold — same coordinate-and-graph world, opposite direction — and it's cheap enough to run at scale, which is exactly the regime a computational shop can own without a wet lab.

**Verdict.** Quietly one of the most *useful* papers in the modern design stack — not because the architecture is exotic (it isn't) but because it's fast, robust, and validated in the lab, not just on held-out recovery. The caveat is scope: it designs sequences for a *given* backbone; it doesn't decide what backbone you should want. Read it as one half of a pair with RFdiffusion.
