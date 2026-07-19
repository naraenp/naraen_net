---
layout: post
title: "Velocity for messier dynamics"
date: 2026-07-18 08:45:00 -0500
tags: [paper]
paper:
  title: "Generalizing RNA velocity to transient cell states through dynamical modeling (scVelo)"
  authors: "Bergen et al."
  venue: "Nature Biotechnology, 2020"
  link: "https://doi.org/10.1038/s41587-020-0591-3"
  verdict: "RNA velocity without the steady-state assumption — the version most people actually run, and a lesson in relaxing a founding model's shortcuts."
---

**The problem.** The original RNA velocity model assumed genes reach a transcriptional steady state and that splicing rates are shared — convenient, but often false. In transient, fast-changing populations (exactly where dynamics are most interesting), those assumptions break, and the velocity arrows can point wrong.

**The idea.** scVelo drops the steady-state shortcut and instead fits the full transcriptional dynamics — transcription, splicing, and degradation rates per gene — via a likelihood-based dynamical model. This recovers velocities in transient states the original method mishandled, and yields per-gene kinetic parameters and a data-driven estimate of latent time. Same biological principle (unspliced vs. spliced), more honest math.

**Why it matters.** scVelo is the RNA-velocity implementation most analyses now use, and it slots into the Scanpy/AnnData ecosystem (day 10) as a standard step. Reading it after La Manno is a clean study in method maturation: a compelling idea's simplifying assumptions get identified and relaxed, and the field's default shifts — the same edgeR-to-Leiden pattern of "founding paper, then the fix" I keep seeing.

**Verdict.** Foundational as the practical standard for RNA velocity; still requires care (velocity remains model-dependent and can mislead on some systems). Read it as the generalisation that made velocity broadly usable, and as the AnnData-native tool I'd actually reach for.
