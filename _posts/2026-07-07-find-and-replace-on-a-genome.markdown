---
layout: post
title: "Find-and-replace on a genome"
date: 2026-07-07 14:00:00 -0500
tags: [paper]
paper:
 title: "Total synthesis of Escherichia coli with a recoded genome (Syn61)"
 authors: "Fredens et al. (Chin lab)"
 venue: "Nature, 2019"
 link: "https://doi.org/10.1038/s41586-019-1192-5"
 verdict: "The clearest answer yet to 'what does Build mean at genome scale', and it lived."
---

**The problem.** The genetic code is redundant, 64 codons for 20 amino acids plus stop, so in principle you don't need all 64. But "in principle" is cheap. Could you actually *rewrite* an entire genome to use fewer codons, across every gene at once, and have the organism survive?

**The idea.** Chin's group designed and chemically synthesized a 4-megabase *E. coli* genome, **Syn61**, in which every occurrence of three codons was swapped for a synonym: two serine codons (TCG→AGC, TCA→AGT) and the TAG stop codon (TAG→TAA). That's ~18,000 edits genome-wide, designed *in silico*, synthesized in segments, and stitched into the chromosome by stepwise replacement (REXER/GENESIS), continuously checking viability. The recoded strain grows, a little slower, but it lives.

**Why it matters.** This is the vivid, tangible answer to what genome-scale **Build** looks like, and it's really a computation story wearing a lab coat: the genome is designed as *text*, validated by software, and only then fabricated. The payoff is downstream, freeing codons means you can reassign them, e.g. to encode non-canonical amino acids or to engineer genetic isolation and phage resistance (the follow-up Syn61Δ3 work). It's the strongest single illustration that genomes are editable at the whole-organism level, and that the hard part is increasingly design and verification, not chemistry.

**Verdict.** A landmark, and an honest one, the reduced growth rate and the sheer cost/effort are stated plainly, and "removed three codons" is a long way from "designed a genome from function." But as a demonstration of scale it's unmatched, and it's the cleanest on-ramp to the DBTL framing. My favorite "genome as editable file" post.
