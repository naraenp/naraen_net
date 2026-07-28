---
layout: post
title: "Rebuilding PLINK for biobank scale"
date: 2026-07-28 03:00:00 -0500
tags: [paper]
paper:
 title: "Second-generation PLINK: rising to the challenge of larger and richer datasets"
 authors: "Chang et al."
 venue: "GigaScience, 2015"
 link: "https://doi.org/10.1186/s13742-015-0047-8"
 verdict: "The same PLINK, rewritten so it does not fall over on biobank-scale data: bit-level tricks and better algorithms to keep the standard workflow fast on hundreds of thousands of samples."
---

**The problem.** The original PLINK was built for cohorts of thousands. By the mid-2010s, biobanks held hundreds of thousands of people and millions of imputed variants, and the old code was too slow and memory-hungry for that. Rewriting from scratch risked breaking the workflows everyone already trusted.

**The idea.** The authors reimplemented the PLINK core with data structures and algorithms tuned for the new scale. Genotypes pack two bits each and are processed with bitwise operations, so common operations run on many samples at once. Hot paths like association tests, relatedness, and linkage-disequilibrium calculations were reworked to be faster and to stream rather than hold everything in memory. The command interface stayed close to the original, so existing pipelines mostly kept working.

**Why it matters.** This is a clean example of a lesson that shows up across my reading: the science does not change, but the data grows by orders of magnitude, and the tool has to be rebuilt to keep up. It is the same story as second-generation aligners and count-based RNA-seq methods. Keeping the interface stable while replacing the engine is why the community could move to biobank data without relearning everything.

**Verdict.** An engineering paper more than a methods one, but an important one. Read it for how a workhorse tool is modernized without stranding its users.
