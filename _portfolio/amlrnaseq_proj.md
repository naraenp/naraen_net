---
layout: page
title: "AML Bulk RNA-seq Pipeline (Nextflow)"
description: "A small Nextflow DSL2 pipeline for AML vs. healthy bulk RNA-seq differential expression, run end-to-end on real TCGA-LAML and GTEx data via recount3."
thumbnail: "/assets/images/portfolio/aml_rnaseq.svg"
---

A compact **[Nextflow DSL2](https://www.nextflow.io/)** pipeline for bulk RNA-seq differential expression — **AML vs. healthy** — run end-to-end on real public RNA-seq cohorts. AML samples come from **TCGA-LAML** and healthy controls from **GTEx whole blood**, both pulled from the **[recount3](https://rna.recount.bio/)** project, which re-aligns and re-quantifies TCGA and GTEx through one uniform Monorail / STAR / GENCODE v26 pipeline so the gene-level counts are directly comparable across the two sources.

It's a workflow-engineering exercise: a small, readable pipeline (channels, processes, `publishDir`, profile-driven config) on top of a transparent, dependency-light biology layer — library-size CPM normalization, a per-gene Welch t-test on log2-CPM, and a hand-rolled Benjamini–Hochberg FDR. The interactive volcano labels the canonical AML markers (FLT3, KIT, MEIS1, HOXA9, MPO, CD34, …), which sit cleanly above the significance line.

**Four stages:**

1. [`LOAD_COUNTS`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/load_counts.py) — join the TCGA-LAML + GTEx gene sums on Ensembl ID, map to HGNC symbols via GENCODE v26, subsample to balanced groups, and filter low-expression genes.
2. [`NORMALIZE_COUNTS`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/normalize_counts.py) — library-size CPM, then `log2(CPM + 1)`.
3. [`RUN_DE`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/run_de.py) — per-gene Welch t-test with BH-adjusted p-values.
4. [`MAKE_VOLCANO`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/make_volcano.py) — an interactive Plotly volcano.

The real-data inputs (~130 MB from recount3 + the GENCODE annotation) are fetched once with a small [`fetch_real_data.sh`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/fetch_real_data.sh) helper, and the whole thing runs in seconds on a laptop. Pinned conda env, project-relative paths, and fast data-free unit tests for the DE math.

> **Comparator caveat:** GTEx has no bone-marrow tissue, so whole peripheral blood is the closest large healthy comparator. The AML markers recover cleanly, but progenitor-associated genes can read as "up in AML" simply because mature blood lacks progenitor populations — swapping in a healthy bone-marrow cohort is the natural next step.

**Platforms & Tools:** Nextflow DSL2, Python (numpy / pandas / scipy / plotly), recount3, GENCODE v26, conda, pytest

The pipeline source and the [`main.nf`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/main.nf) workflow live in [`bioinformatics-public/aml_rnaseq_nf`](https://github.com/naraenp/bioinformatics-public/tree/main/aml_rnaseq_nf); see [`docs/REPORT.md`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/docs/REPORT.md) for a full run report — dataset provenance, the embedded volcano, and a runtime profile.

![Volcano plot from a run on TCGA-LAML AML vs. GTEx whole-blood healthy samples, with the canonical AML marker genes labeled above the FDR line.](https://raw.githubusercontent.com/naraenp/bioinformatics-public/main/aml_rnaseq_nf/docs/volcano.png)
