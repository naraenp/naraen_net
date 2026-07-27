---
layout: post
title: "Changing one letter without a break"
date: 2026-07-27 10:00:00 -0500
tags: [paper]
paper:
 title: "Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage"
 authors: "Komor et al."
 venue: "Nature, 2016"
 link: "https://doi.org/10.1038/nature17946"
 verdict: "Most disease variants are single-letter changes, yet cutting DNA is a blunt way to fix one. Base editing rewrites a single base directly, no double-strand break needed."
---

**The problem.** Standard CRISPR fixes a point mutation by cutting the DNA and hoping the cell uses a supplied template to repair it. That repair path is inefficient in many cells, and the double-strand break invites messy insertions and deletions. For a one-letter change, cutting is the wrong-sized tool.

**The idea.** The authors fused a cytidine deaminase enzyme to a Cas9 that no longer cuts both strands. The dead or nicking Cas9 parks the complex on the target using its guide RNA, and the deaminase chemically converts a C into a U within a small window, which the cell then reads and copies as a T. So a C-to-T (and on the other strand G-to-A) change is written directly, with no break and no donor template. Adding a repair inhibitor and using a nickase pushed the edit to stick.

**Why it matters.** This is a genuine shift in what "editing" means: chemistry on a base rather than breaking and repairing the backbone. Since so many pathogenic variants are single substitutions, precise base changes without a double-strand break is exactly the capability the clinic wants. It also shows the dCas9 chassis from CRISPRi as a general delivery platform for a payload.

**Verdict.** A foundational precision-editing method, later joined by adenine base editors and prime editing. Read it as the first move from cutting to writing single bases.
