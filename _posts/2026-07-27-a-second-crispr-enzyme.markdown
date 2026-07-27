---
layout: post
title: "A second CRISPR enzyme"
date: 2026-07-27 09:00:00 -0500
tags: [paper]
paper:
 title: "Cpf1 is a single RNA-guided endonuclease of a class 2 CRISPR-Cas system"
 authors: "Zetsche et al."
 venue: "Cell, 2015"
 link: "https://doi.org/10.1016/j.cell.2015.09.038"
 verdict: "Cas9 is not the only option. Cpf1 (now Cas12a) needs only one short RNA, reads a different PAM, and leaves staggered cut ends, widening where and how you can edit."
---

**The problem.** Cas9 is powerful but not universal. It needs two RNAs combined into a guide, reads a G-rich PAM that is missing from some target regions, and leaves blunt cut ends. If those constraints block your site, you are stuck. Are there other natural enzymes with a different set of rules?

**The idea.** The authors characterized Cpf1, a class 2 CRISPR enzyme distinct from Cas9. It is guided by a single short crRNA with no separate tracrRNA, which simplifies the design and the delivery. It recognizes a T-rich PAM, opening up AT-rich regions that Cas9 struggles with, and it cuts to leave staggered ends with short overhangs rather than blunt breaks, which can help direct how an insert goes in. It also processes its own guide array, useful for multiplexing.

**Why it matters.** This is the reminder that CRISPR is a family, not a single tool. A different PAM and a single-RNA guide are practical advantages: they change which sites are reachable and make library and multiplex design cleaner. For synthetic biology, having orthogonal enzymes means you can run more than one targeting program in the same cell.

**Verdict.** The paper that established Cpf1/Cas12a as a real alternative to Cas9. Read it for the mechanistic differences and what they buy you.
