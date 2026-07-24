---
layout: post
title: "The single-cell best-practices bible"
date: 2026-07-10 15:00:00 -0500
tags: [paper]
paper:
 title: "Best practices for single-cell analysis across modalities"
 authors: "Heumos, Schaar, Lance et al."
 venue: "Nature Reviews Genetics, 2023"
 link: "https://doi.org/10.1038/s41576-023-00586-w"
 verdict: "The current, community-maintained map of how to do single-cell analysis properly, and its companion book is the one I'd actually keep open."
---

**The problem.** Single-cell tooling moves so fast that "best practice" is a moving target, and the 2019 tutorials, good as they were, no longer cover multimodal data, the deep-generative methods, or the pitfalls the field has since learned. Newcomers need one current, opinionated, end-to-end reference.

**The idea.** This is a comprehensive review spanning the whole workflow, QC, normalization, integration, clustering, annotation, trajectory, differential and compositional analysis, and reaching across modalities (RNA, ATAC, protein, spatial). It's also tied to the living [sc-best-practices.org](https://www.sc-best-practices.org/) book, so the recommendations come with runnable code and get updated as methods change, rather than freezing at publication.

**Why it matters.** This is the natural capstone to the spatial and single-cell fortnight: everything I read this week, scVI, scANVI, the deconvolution and segmentation methods, has a place in this map, and the review is where the judgment about *when* to use each lives. For a facility, a shared, current best-practice reference is worth more than any single tool; it's the standard you point collaborators to.

**Verdict.** The most useful "one thing to bookmark" of the batch, and the maintained book is the real deliverable. Its only ceiling is the field's own churn, even a living document lags the newest methods. Read it as the framework, and treat the website as the working manual. This closes out §6; tomorrow the reading turns to foundations.
