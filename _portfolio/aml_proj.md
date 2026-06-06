---
layout: page
title: "AML transcriptomics: single-cell + bulk RNA-seq"
description: "Two complementary acute myeloid leukemia projects: a single-cell pipeline characterizing pre-leukemic populations (R Shiny dashboard) and a Nextflow bulk RNA-seq differential-expression pipeline (interactive volcano)."
thumbnail: "/assets/images/portfolio/aml_scrna.svg"
---

Two complementary takes on **acute myeloid leukemia** transcriptomics: a single-cell pipeline that characterizes pre-leukemic populations across patient cohorts, and a bulk RNA-seq differential-expression pipeline built as a workflow-engineering exercise. The first asks *which cells* drive the disease; the second asks *which genes* separate AML from healthy blood at the cohort level.

### Single-cell RNA-seq: pre-leukemic populations

Built a reproducible scRNA-seq pipeline on **38 public AML patient samples** spanning the full pipeline from raw 10X data to clinical correlation. The R-side ([Seurat](https://satijalab.org/seurat/)) workflow handles per-sample QC, normalization, anchor-based integration, and **reference-guided cell-type annotation** against a hematopoietic atlas to surface pre-leukemic populations. The Python-side workflow ([Scanpy](https://scanpy.readthedocs.io/) + [CellRank](https://cellrank.readthedocs.io/)) extends the analysis with **diffusion pseudotime, GPCCA macrostates, and fate probabilities** out of HSC-rooted trajectories, then scores **PLPS/Stem11 gene signatures** with `decoupler` and runs Kaplan-Meier **survival analysis** against TCGA LAML clinical data using `lifelines`.

Findings are surfaced through an interactive R Shiny dashboard with two views: a filterable UMAP of integrated hematopoietic lineages, and a gallery of analysis figures (integrated UMAP, cell-type abundance, macrostates, fate probabilities, metabolic pathway activity, pseudotime gene dynamics, and the two survival plots).

**Platforms & Tools:** R, Python, R Shiny, Seurat, Scanpy, CellRank, decoupler, lifelines, Jupyter, Conda, shinyapps.io

Source data drawn from [Zeng et al., *Cell Genomics* (2023)](https://doi.org/10.1016/j.xgen.2023.100426) and AML clinical data from NCI. Pipeline source lives in [`bioinformatics-public/preleukemia_analysis`](https://github.com/naraenp/bioinformatics-public/tree/main/preleukemia_analysis).

<figure class="media-figure">
  <iframe src="https://naraenp2.shinyapps.io/preleuk_dashboard/"
          title="AML scRNA-seq Shiny dashboard"
          loading="lazy"
          style="height: 800px;">
  </iframe>
  <figcaption>Interactive R Shiny dashboard: a filterable UMAP of integrated hematopoietic lineages and a gallery of analysis figures.</figcaption>
</figure>

### Bulk RNA-seq differential expression (Nextflow)

A compact **[Nextflow DSL2](https://www.nextflow.io/)** pipeline for bulk RNA-seq differential expression, **AML vs. healthy**, run end-to-end on real public RNA-seq cohorts. AML samples come from **TCGA-LAML** and healthy controls from **GTEx whole blood**, both pulled from the **[recount3](https://rna.recount.bio/)** project, which re-aligns and re-quantifies TCGA and GTEx through one uniform Monorail / STAR / GENCODE v26 pipeline so the gene-level counts are directly comparable across the two sources.

It's a workflow-engineering exercise: a small, readable pipeline (channels, processes, `publishDir`, profile-driven config) on top of a transparent, dependency-light biology layer: library-size CPM normalization, a per-gene Welch t-test on log2-CPM, and a hand-rolled Benjamini-Hochberg FDR. The interactive volcano below labels the canonical AML markers (FLT3, KIT, MEIS1, HOXA9, MPO, CD34, …), which sit cleanly above the significance line.

**Four stages:**

1. [`LOAD_COUNTS`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/load_counts.py): join the TCGA-LAML + GTEx gene sums on Ensembl ID, map to HGNC symbols via GENCODE v26, subsample to balanced groups, and filter low-expression genes.
2. [`NORMALIZE_COUNTS`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/normalize_counts.py): library-size CPM, then `log2(CPM + 1)`.
3. [`RUN_DE`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/run_de.py): per-gene Welch t-test with BH-adjusted p-values.
4. [`MAKE_VOLCANO`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/make_volcano.py): an interactive Plotly volcano.

The real-data inputs (~130 MB from recount3 + the GENCODE annotation) are fetched once with a small [`fetch_real_data.sh`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/fetch_real_data.sh) helper, and the whole thing runs in seconds on a laptop. Pinned conda env, project-relative paths, and fast data-free unit tests for the DE math.

> **Comparator caveat:** GTEx has no bone-marrow tissue, so whole peripheral blood is the closest large healthy comparator. The AML markers recover cleanly, but progenitor-associated genes can read as "up in AML" simply because mature blood lacks progenitor populations. Swapping in a healthy bone-marrow cohort is the natural next step.

**Platforms & Tools:** Nextflow DSL2, Python (numpy / pandas / scipy / plotly), recount3, GENCODE v26, conda, pytest

The pipeline source and the [`main.nf`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/main.nf) workflow live in [`bioinformatics-public/aml_rnaseq_nf`](https://github.com/naraenp/bioinformatics-public/tree/main/aml_rnaseq_nf); see [`docs/REPORT.md`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/docs/REPORT.md) for a full run report: dataset provenance, the embedded volcano, and a runtime profile.

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/aml_volcano.html' | relative_url }}"
          title="Interactive volcano plot, AML vs. healthy bulk RNA-seq"
          loading="lazy"
          style="height: 760px;">
  </iframe>
  <figcaption>Interactive volcano of the differential-expression results, with the canonical AML markers labeled above the significance line.</figcaption>
</figure>
