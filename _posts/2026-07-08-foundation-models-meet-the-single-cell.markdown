---
layout: post
title: "Foundation models meet the single cell"
date: 2026-07-08 10:20:00 -0500
tags: [paper]
paper:
 title: "Transfer learning enables predictions in network biology (Geneformer)"
 authors: "Theodoris et al."
 venue: "Nature, 2023"
 link: "https://doi.org/10.1038/s41586-023-06139-9"
 verdict: "The first big single-cell foundation model, pretrain once on millions of cells, fine-tune with almost no data."
---

**The problem.** Single-cell RNA-seq gives you a matrix of ~20,000 genes × thousands of cells, but most biological questions come with *tiny* labeled datasets. Could you pretrain on the mountain of unlabeled transcriptomes that already exist, then transfer to specific tasks with little task-specific data, the recipe that worked for language?

**The idea.** Geneformer is a transformer pretrained on **Genecorpus-30M**, around 30 million single-cell transcriptomes. Its representation is clever: each cell becomes a *rank-value encoding*, an ordered list of its genes sorted by expression (normalized for each gene's typical level), so the model attends over "which genes dominate this cell." After self-supervised pretraining, fine-tuning on small labeled sets predicts network-biology properties, dosage-sensitive genes, chromatin state, network rewiring, and *in silico* deletion nominates therapeutic targets (demonstrated for cardiomyopathy).

**Why it matters.** This is directly adjacent to my AML scRNA-seq work: instead of engineering features from scratch on one dataset, you inherit an embedding trained on everything. The interesting shift is conceptual, the unit of reuse becomes a *pretrained representation of a cell*, the way text embeddings are reused across NLP tasks.

**Verdict.** A landmark for staking the "foundation models for cells" claim, but I read it with the field's live skepticism in hand: several follow-up benchmarks question whether single-cell FMs actually beat well-tuned classical methods (scVI, even logistic regression) on routine tasks like annotation and integration. The honest position is that pretraining clearly helps *some* low-data, network-level tasks and is unproven on others. Pair it with scGPT and ask, task by task, where the pretraining earns its keep.
