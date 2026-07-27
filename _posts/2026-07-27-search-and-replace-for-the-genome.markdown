---
layout: post
title: "Search and replace for the genome"
date: 2026-07-27 11:00:00 -0500
tags: [paper]
paper:
 title: "Search-and-replace genome editing without double-strand breaks or donor DNA"
 authors: "Anzalone et al."
 venue: "Nature, 2019"
 link: "https://doi.org/10.1038/s41586-019-1711-4"
 verdict: "Prime editing carries the new sequence in its own guide and writes it in with a reverse transcriptase. One system for all point mutations and small insertions or deletions, no break, no donor."
---

**The problem.** Base editing writes single substitutions cleanly, but only certain ones, and it cannot handle small insertions or deletions. Cutting with a template can do more but relies on inefficient break repair. What was missing was a single precise method that covers the full range of small edits without a double-strand break.

**The idea.** Prime editing fuses a nicking Cas9 to a reverse transcriptase and drives it with a longer guide, a pegRNA, that both targets the site and carries a template for the edit. The Cas9 nicks one strand, the reverse transcriptase copies the edit off the pegRNA directly into the genome, and the cell resolves the flap so the new sequence stays. Because the change is written from an RNA template the tool brings with it, all twelve point substitutions and short insertions and deletions become reachable, with no separate donor DNA.

**Why it matters.** This is the most general of the precision editors, and it closes the arc that runs through this whole batch: from cutting DNA, to blocking transcription, to changing one base, to writing an arbitrary short edit. It narrows the gap between reading a pathogenic variant and correcting it, which is the promise that started with Cas9 in a test tube.

**Verdict.** A landmark method that widened the precision-editing range in one system. Read it as the current far end of the "write, do not break" line of work.
