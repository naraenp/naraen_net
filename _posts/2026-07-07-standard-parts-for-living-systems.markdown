---
layout: post
title: "Standard parts for living systems"
date: 2026-07-07 11:00:00 -0500
tags: [paper]
paper:
  title: "Foundations for engineering biology"
  authors: "Drew Endy"
  venue: "Nature, 2005"
  link: "https://doi.org/10.1038/nature04342"
  verdict: "The manifesto that argued biology's bottleneck is engineering discipline, not biology — still the right diagnosis."
---

**The problem.** After the toggle switch and repressilator, building anything *bigger* was miserable: every part behaved differently in every new context, and each project started from scratch. Endy's claim is that this is not a biology problem but an *engineering* one — biology lacked the abstractions that let other fields compose complexity.

**The idea.** Three borrowed principles. **Standardization** — define parts (promoters, RBSs, coding sequences) with measured, documented behavior so they can be shared and reused (the BioBrick/registry vision). **Decoupling** — separate *design* from *fabrication*, so you can reason about what to build without also solving how to synthesize it. **Abstraction** — a hierarchy (DNA → parts → devices → systems) where each layer hides the mess below it, so a systems designer needn't think in base pairs.

**Why it matters.** This is the conceptual scaffold the whole field's tooling hangs on, and the analogy to software is exact: datasheets, interfaces, layered abstraction, separation of concerns. It's also the clearest articulation of *why reproducibility is an engineering value, not a virtue* — standard, characterized, composable units are what make work cumulative. The same instinct drives containerized, versioned analysis pipelines: decouple the definition of an analysis from the machine that runs it, and hide the plumbing behind a clean interface.

**Verdict.** Twenty years on, the diagnosis is right and the cure is partial. Standardization keeps foundering on biological context-dependence — a part's behavior still leaks across its boundaries in a way a resistor's doesn't. But as a statement of what "engineering biology" should *mean*, it hasn't been improved on. Read it as the philosophy under everything else in this list.
