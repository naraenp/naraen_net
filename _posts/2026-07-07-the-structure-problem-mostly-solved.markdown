---
layout: post
title: "The structure problem, mostly solved"
date: 2026-07-07 14:45:00 -0500
tags: [paper]
paper:
 title: "Highly accurate protein structure prediction with AlphaFold (AlphaFold2)"
 authors: "Jumper et al. (AlphaFold, DeepMind)"
 venue: "Nature, 2021"
 link: "https://doi.org/10.1038/s41586-021-03819-2"
 verdict: "A model triumph that's secretly a data-and-evaluation triumph, and now just infrastructure."
---

**The problem.** Predicting a protein's 3D structure from its sequence was a 50-year open problem. Physics-based folding didn't scale; earlier ML got close-ish. Then at CASP14, AlphaFold2 predicted structures at roughly experimental accuracy for most targets, and the field's central question changed overnight.

**The idea.** Two coupled representations: a **multiple-sequence-alignment** track (evolutionary covariation, which residues mutate together, hinting at contacts) and a **pairwise** track over residue pairs, refined together in the *Evoformer* by repeated attention. A final *structure module* places atoms directly in 3D, end-to-end, and the whole thing recycles its own output to iterate. It emits a per-residue confidence (**pLDDT**) that turns out to be trustworthy, you can tell where to believe it.

**Why it matters.** For someone whose day job is analysis, the underappreciated angle is that AlphaFold2 is as much a **data and evaluation** win as a modeling one: decades of curated PDB structures, a ruthless blind benchmark (CASP), and a well-posed loss. The architecture matters, but the *scaffolding around it* is what made the result real and reproducible, the same lesson that governs any serious pipeline. Downstream, predicted structures and the confidence score are now infrastructure: inputs to design (ProteinMPNN, RFdiffusion), annotation, and drug work.

**Verdict.** Genuinely field-defining, and the caveats are well-known and honestly relevant: it predicts *a* static structure, leans on deep MSAs (weak for orphan/designed sequences), and says little about dynamics, complexes, or the effect of point mutations. Read it for the architecture, but steal the meta-lesson about data and evaluation. Pairs naturally with ESMFold as "with MSA vs. without."
