---
layout: page
title: "AML scRNA-seq Analysis"
description: "Reproducible scRNA-seq pipeline characterizing pre-leukemic populations across 38 AML patient samples, deployed as an R Shiny dashboard."
thumbnail: "/assets/images/portfolio/aml_scrna.svg"
---

Built a reproducible scRNA-seq pipeline on **38 public AML patient samples** spanning the full pipeline from raw 10X data to clinical correlation. The R-side ([Seurat](https://satijalab.org/seurat/)) workflow handles per-sample QC, normalization, anchor-based integration, and **reference-guided cell-type annotation** against a hematopoietic atlas to surface pre-leukemic populations. The Python-side workflow ([Scanpy](https://scanpy.readthedocs.io/) + [CellRank](https://cellrank.readthedocs.io/)) extends the analysis with **diffusion pseudotime, GPCCA macrostates, and fate probabilities** out of HSC-rooted trajectories, then scores **PLPS/Stem11 gene signatures** with `decoupler` and runs Kaplan-Meier **survival analysis** against TCGA LAML clinical data using `lifelines`.

Findings are surfaced through an interactive R Shiny dashboard with two views: a filterable UMAP of integrated hematopoietic lineages, and a gallery of analysis figures (integrated UMAP, cell-type abundance, macrostates, fate probabilities, metabolic pathway activity, pseudotime gene dynamics, and the two survival plots).

**Platforms & Tools:** R, Python, R Shiny, Seurat, Scanpy, CellRank, decoupler, lifelines, Jupyter, Conda, shinyapps.io

Source data drawn from [Zeng et al., *Cell Genomics* (2023)](https://doi.org/10.1016/j.xgen.2023.100426) and AML clinical data from NCI. Pipeline source lives in [`bioinformatics-public/preleukemia_analysis`](https://github.com/naraenp/bioinformatics-public/tree/main/preleukemia_analysis).

<iframe src="https://naraenp2.shinyapps.io/preleuk_dashboard/" 
        style="width: 100%; height: 800px; border: 1px solid var(--pa-card-border);">
</iframe>
