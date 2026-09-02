---
layout: page
title: "Preleukemia and AML transcriptomics: single-cell + bulk RNA-seq"
description: "Two projects on the road into AML: a revised single-cell analysis of preleukemic mouse HSPCs (38 samples, eight mutation models) with a TCGA-LAML survival arm and an R Shiny dashboard, and a Nextflow bulk RNA-seq differential-expression pipeline with an interactive volcano."
thumbnail: "/assets/images/portfolio/aml_scrna.svg"
slug: aml_proj   # joins this page to its entry in content.yml projects
---

Two takes on the road into **acute myeloid leukemia**: a single-cell analysis of preleukemic mouse blood progenitors, and a bulk RNA-seq differential-expression pipeline built as a workflow-engineering exercise. The first asks *which cells* change before leukemia; the second asks *which genes* separate AML from healthy blood in bulk cohorts.

### Single-cell RNA-seq: preleukemic populations

A reanalysis of **38 mouse bone-marrow HSPC samples** across eight preleukemic mutation models (*Calr*, *Dnmt3a*, *Ezh2*, *Flt3*-ITD, *Idh1*, *Jak2*, *Npm1c*, *Utx*) from Isobe et al., with a trajectory arm, a **TCGA-LAML** survival arm, and an R Shiny dashboard. Each stage is a [Quarto](https://quarto.org/) document, and the rendered HTML files are the analysis record: they explain each method choice in place.

The first version of this analysis used one fixed QC cutoff for all 38 samples, anchor-based integration to an arbitrary reference sample, and cell-level tests for composition and differential expression. This version is a statistical revision. The question is the same; how it is answered changed:

- **Cell calling** with `emptyDrops` (FDR ≤ 0.001) instead of a fixed 200-gene floor, so each barcode is tested against the ambient profile.
- **Per-sample adaptive QC** (3 MADs on the log scale) plus doublet removal with `scDblFinder`. Libraries differ, and a fixed cutoff conflates quality with biology.
- **Harmony integration** over 50 PCs with sample as the batch, so no sample is picked as an arbitrary reference and condition is not treated as nuisance.
- **SingleR annotation** against the Dahlin 2018 mouse HSPC atlas, with pruned scores and marker verification, so each label carries a confidence.
- **Composition** tested with `propeller` and **differential expression** with pseudobulk `edgeR`, both on `~ model + condition`. The mouse, not the cell, is the replicate.
- **Trajectory** by diffusion pseudotime and [CellRank](https://cellrank.readthedocs.io/) fate probabilities from an *Hlf*-high HSC root. There are no spliced counts, so no velocity; that limitation is stated rather than worked around.
- **Survival** by age-adjusted Cox proportional hazards on the continuous signature score, with Kaplan-Meier curves for display. A median split discards information, and age is the dominant confounder.

**What it found.** 276,294 barcodes were called as cells and 230,684 remained after QC and doublet removal. Harmony mixed the 38 samples well (per-cluster sample-mixing entropy 0.95 to 0.97, where 1 is even mixing). Only 0.24% of cells were low-confidence under SingleR, and the label distribution matches an LK sort (4.6% HSCs). Then most of the results the original pipeline reported as significant went away. A chi-square on pooled cells gives *p* < 10⁻¹⁵ for composition, but `propeller` at the sample level finds no cell type at FDR 0.05. Pseudobulk differential expression finds no shared mutant-versus-WT genes in HSCs and at most 13 in any cell type. A program shared across eight different mutations is not detectable at *n* = 38, and per-model effects cannot be tested with 2 to 3 mice per arm. In TCGA-LAML (*n* = 151), neither the paper's **PLPS** nor **Stem11** signature is associated with overall survival after age adjustment (hazard ratio per SD 0.97 for both; *p* = 0.75 and 0.81), and the unadjusted result is null too.

Once the animal or the patient is the unit of inference and the covariates are included, most of the original findings do not hold. That is the correct result, not a disappointing one.

**Platforms & Tools:** R, Python, Quarto, R Shiny, Seurat, DropletUtils, scDblFinder, Harmony, SingleR, propeller / limma, edgeR, Scanpy, CellRank, lifelines, Conda, shinyapps.io

Source data drawn from [Isobe et al., *Cell Genomics* (2023)](https://doi.org/10.1016/j.xgen.2023.100426) (GEO GSE227026), and TCGA-LAML clinical data from NCI via cBioPortal. The Quarto stages, helper scripts, and the dashboard live in [`bioinformatics-public/preleukemia_analysis`](https://github.com/naraenp/bioinformatics-public/tree/main/preleukemia_analysis).

<figure class="media-figure">
  <iframe src="https://naraenp2.shinyapps.io/preleuk_dashboard/"
          title="Preleukemia scRNA-seq Shiny dashboard"
          loading="lazy"
          style="height: 800px;">
  </iframe>
  <figcaption>The deployed R Shiny dashboard: a filterable UMAP of integrated hematopoietic lineages and a gallery of analysis figures. It still shows the original analysis; the revised dashboard (QC, atlas, composition, differential expression, and survival tabs) is in the repository and has not been deployed yet.</figcaption>
</figure>

### Bulk RNA-seq differential expression (Nextflow)

A compact **[Nextflow DSL2](https://www.nextflow.io/)** pipeline for bulk RNA-seq differential expression, **AML vs. healthy**, run on real public RNA-seq cohorts. It complements the single-cell work: where that analysis follows preleukemic cells in mice, this one checks that the canonical AML markers separate AML from healthy blood in bulk human cohorts. AML samples come from **TCGA-LAML** and healthy controls from **GTEx whole blood**, both pulled from the **[recount3](https://rna.recount.bio/)** project, which re-aligns and re-quantifies TCGA and GTEx through one uniform Monorail / STAR / GENCODE v26 pipeline so the gene-level counts are directly comparable across the two sources.

It's a workflow-engineering exercise: a small, readable pipeline (channels, processes, `publishDir`, profile-driven config) on top of a transparent, dependency-light biology layer: library-size CPM normalization, a per-gene Welch t-test on log2-CPM, and a hand-rolled Benjamini-Hochberg FDR. The interactive volcano below labels the canonical AML markers (FLT3, KIT, MEIS1, HOXA9, MPO, CD34, …), which sit cleanly above the significance line.

**Four stages:**

1. [`LOAD_COUNTS`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/load_counts.py): join the TCGA-LAML + GTEx gene sums on Ensembl ID, map to HGNC symbols via GENCODE v26, subsample to balanced groups, and filter low-expression genes on pooled expression so the filter stays independent of the group contrast.
2. [`NORMALIZE_COUNTS`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/normalize_counts.py): library-size CPM, then `log2(CPM + 1)`.
3. [`RUN_DE`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/run_de.py): per-gene Welch t-test with BH-adjusted p-values.
4. [`MAKE_VOLCANO`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/bin/make_volcano.py): an interactive Plotly volcano.

The real-data inputs (~130 MB from recount3 + the GENCODE annotation) are fetched once with a small [`fetch_real_data.sh`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/fetch_real_data.sh) helper, and the whole thing runs in seconds on a laptop. Pinned conda env, project-relative paths, and fast data-free unit tests for the DE math.

> **Comparator caveat:** GTEx has no bone-marrow tissue, so whole peripheral blood is the closest large healthy comparator. Cohort is therefore confounded with disease, tissue, and collection protocol at once. The AML markers still recover cleanly, but progenitor genes can read as "up in AML" simply because mature blood has no progenitor populations, so the direction of a fold change should be read with that in mind. Swapping in a healthy bone-marrow cohort is the natural next step.

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
