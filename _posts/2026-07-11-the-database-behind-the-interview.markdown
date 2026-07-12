---
layout: post
title: "The database behind the interview"
date: 2026-07-11 07:00:00 -0500
tags: [paper]
paper:
  title: "DIANA-TarBase v8: a decade-long collection of experimentally supported miRNA–gene interactions"
  authors: "Karagkouni et al."
  venue: "Nucleic Acids Research, 2018"
  link: "https://doi.org/10.1093/nar/gkx1141"
  verdict: "The reference database of experimentally validated miRNA targets — and, not incidentally, a signature resource of the group I'm interviewing with."
---

**The problem.** Predicting microRNA targets computationally is easy and mostly wrong — sequence complementarity throws off huge false-positive lists. What the field actually needs is a curated record of interactions that were *experimentally* observed, not just predicted, so downstream analysis rests on evidence.

**The idea.** TarBase v8 is exactly that: a manually and computationally curated collection of hundreds of thousands of experimentally supported miRNA–gene interactions, spanning many cell types and conditions, with the *type* of supporting experiment recorded for each entry. It turns "here are sequences that might bind" into "here is what has actually been shown to bind, and how we know."

**Why it matters.** Two reasons. First, it's the model for a well-run resource — evidence-tagged, versioned, queryable — which is the standard I'd want any facility database held to. Second, it's a Vlachos-lab / DIANA-tools flagship, so reading it is doing my homework: understanding the intellectual lineage of the group whose spatial unit I want to join. Knowing the reference resources a lab is *known for* is the difference between generic interest and specific fit.

**Verdict.** A model curation effort, and worth reading for both the miRNA biology and the resource-design lessons. The honest caveat is that any target database reflects the coverage and biases of the experiments feeding it — comprehensive is not the same as complete. Read it as infrastructure, and as context for who I want to work with.
