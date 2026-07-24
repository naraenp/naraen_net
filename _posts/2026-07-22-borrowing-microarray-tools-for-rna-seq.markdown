---
layout: post
title: "Borrowing microarray tools for RNA-seq"
date: 2026-07-22 08:45:00 -0500
tags: [paper]
paper:
 title: "voom: precision weights unlock linear model analysis tools for RNA-seq read counts"
 authors: "Law et al."
 venue: "Genome Biology, 2014"
 link: "https://doi.org/10.1186/gb-2014-15-2-r29"
 verdict: "A clever bridge: estimate each count's mean–variance relationship, turn it into a precision weight, and hand RNA-seq to limma's mature linear-model machinery, a third route to differential expression."
---

**The problem.** RNA-seq counts are heteroscedastic: a gene's variance depends on its mean and on sequencing depth, which violates the equal-variance assumption of ordinary linear models. Count-based methods (edgeR, DESeq2) model this with negative-binomial GLMs. But the microarray world had years of refined linear-model tools in limma, could RNA-seq reuse them instead of reinventing?

**The idea.** voom estimates the mean–variance trend of the log-counts empirically, then assigns each observation a precision weight reflecting its reliability. Feed the log-counts and weights into limma's empirical-Bayes linear-model pipeline, and the heteroscedasticity is accounted for. Suddenly the whole limma toolkit, flexible designs, contrasts, empirical-Bayes moderation, applies to RNA-seq, and simulations show it matches or beats count-based methods.

**Why it matters.** This is the third major differential-expression philosophy alongside edgeR and DESeq2, all of which I've now read, worth knowing because the choice affects results and limma-voom shines with complex experimental designs. It's also a lesson in method reuse: rather than build anew, weight the data so an existing, battle-tested framework applies. That instinct shows up again in transfer learning on the ML side.

**Verdict.** A widely-used, flexible DE approach, especially strong for complex designs; the mean–variance estimate needs enough genes and samples to behave. Read it as RNA-seq differential expression routed through the microarray era's best linear-model tools.
