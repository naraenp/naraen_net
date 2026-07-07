---
layout: post
title: "The edit button"
date: 2026-07-07 13:00:00 -0500
tags: [paper]
published: false
paper:
  title: "A programmable dual-RNA–guided DNA endonuclease in adaptive bacterial immunity"
  authors: "Jinek, Chylinski, Fonfara, Hauer, Doudna & Charpentier"
  venue: "Science, 2012"
  link: "https://doi.org/10.1126/science.1225829"
  verdict: "The biochemistry that made genome editing programmable — and cheap enough to change who gets to compete."
---
<!-- DRAFT — AI-generated sample review for the paper-a-day comparison exercise. Held at published:false; verify against your own reading before shipping. -->

**The problem.** Targeted DNA cutting existed before CRISPR — zinc fingers, TALENs — but each new target meant engineering a new *protein*. That's slow and expensive. The question was whether you could retarget a nuclease by changing something cheap instead.

**The idea.** Jinek et al. dissected the *Streptococcus pyogenes* Cas9 system biochemically and showed three things. Cas9 is an RNA-guided endonuclease whose two domains (RuvC and HNH) each nick one DNA strand, giving a blunt double-strand break. Targeting requires a two-RNA duplex — crRNA (which base-pairs the target) plus tracrRNA — and cleavage needs a short **PAM** motif next to the target. Then the punchline: the two RNAs can be fused into a **single guide RNA**. Now retargeting is just typing a new 20-nucleotide sequence.

**Why it matters.** This is the enabling technology under most of modern synthetic biology and functional genomics. It collapsed the cost of "edit here" from protein engineering to oligo synthesis, which is the kind of cost change that reshapes a whole field — CRISPR screens, base/prime editing, engineered organisms, diagnostics all follow. In DBTL terms it made **Build** programmable, the same way AlphaFold later made **Design** computational.

**Verdict.** Foundational, with one honesty note that's easy to lose: this paper is *in vitro* biochemistry. It proves the mechanism and the programmability, but editing in living eukaryotic cells was demonstrated by others (Cong, Mali, and colleagues) months later, and the credit story is genuinely multi-lab. Read this one for the mechanism; read the 2013 cell-editing papers for what it unleashed.
