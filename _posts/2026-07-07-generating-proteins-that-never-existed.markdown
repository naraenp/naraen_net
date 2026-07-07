---
layout: post
title: "Generating proteins that never existed"
date: 2026-07-07 16:30:00 -0500
tags: [paper]
paper:
  title: "De novo design of protein structure and function with RFdiffusion"
  authors: "Watson et al. (Baker lab)"
  venue: "Nature, 2023"
  link: "https://doi.org/10.1038/s41586-023-06415-8"
  verdict: "The same diffusion idea behind image models, pointed at protein backbones — and it makes real binders."
---

**The problem.** Prediction and inverse folding both start from something — a sequence, or a backbone you already drew. Design's most ambitious version starts from *intent*: "give me a protein that binds this target" or "that scaffolds this active site," with no template. Can you *generate* a plausible new backbone from noise?

**The idea.** RFdiffusion adapts **denoising diffusion** — the generative recipe behind modern image models — to protein structure. Fine-tuned from the RoseTTAFold network, it starts from random residue coordinates and iteratively denoises toward a coherent backbone, optionally *conditioned* on constraints: bind this epitope, obey this symmetry, hold this functional motif fixed. You then hand the backbone to ProteinMPNN for a sequence and to a predictor for a check. The Baker lab validated the outputs experimentally — de novo binders (some at picomolar affinity), symmetric assemblies, and motif scaffolds — not just in silico plausibility.

**Why it matters.** This is the "DALL·E for proteins" moment, and the mechanism is genuinely the same math you already know from image diffusion — which is the point worth internalizing: the generative-ML toolbox transfers across modalities once you have the right representation and enough validated data. It's the generative end of DBTL's **Design** step, the part most plausibly tooled by software rather than a foundry, and it composes cleanly with the models above into a design → sequence → predict loop.

**Verdict.** Genuinely exciting and, unusually for a generative-model paper, backed by wet-lab success rather than pretty renders alone. Honest limits: success rates vary by task, hard functional constraints (catalysis, complex dynamics) remain difficult, and every generated design still needs experimental confirmation. Read it last in this batch — it's where the whole design stack points.
