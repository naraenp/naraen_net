---
layout: post
title: "Searching spectra at speed"
date: 2026-07-15 00:20:00 -0500
tags: [paper]
paper:
  title: "MSFragger: ultrafast and comprehensive peptide identification in mass spectrometry–based proteomics"
  authors: "Kong et al."
  venue: "Nature Methods, 2017"
  link: "https://doi.org/10.1038/nmeth.4256"
  verdict: "The search engine that made open, modification-tolerant proteomics practical — the identification step, an order of magnitude faster."
---

**The problem.** Identifying peptides means matching each observed spectrum against theoretical spectra from a protein database. If you also want to catch post-translational modifications, you must widen the mass tolerance enormously — an "open search" — which explodes the candidate space and made comprehensive searches painfully slow.

**The idea.** MSFragger uses a fragment-ion indexing scheme that makes spectrum-to-peptide matching dramatically faster, so open searches over huge modification spaces become tractable. Suddenly you can survey *all* mass shifts in a dataset — discovering unexpected modifications — instead of only looking for the ones you pre-specified.

**Why it matters.** This is the identification engine in the proteomics stack whose other pieces I've already read: MaxQuant/Andromeda and Percolator do related jobs, and MSFragger is the speed-and-openness leap. Conceptually it rhymes with the FM-index/BWA thread from day 6 — the right index turns an intractable search into a fast one. Same algorithmic lesson, proteomics instead of genomics.

**Verdict.** Foundational for modern proteomics, especially open and modification-focused searches; it anchors the FragPipe ecosystem. Read it for the fragment-indexing trick and for how much biology (unanticipated modifications) becomes visible once the search is cheap enough to run wide.
