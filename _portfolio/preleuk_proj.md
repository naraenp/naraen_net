---
layout: page
title: "AML scRNA-seq Analysis"
description: "Reproducible scRNA-seq pipeline characterizing pre-leukemic populations across 38 AML patient samples, deployed as an R Shiny dashboard."
thumbnail: "/assets/images/portfolio/umapdpt_pseudotime.png"
---

Built a reproducible scRNA-seq pipeline on 38 AML patient samples, performing QC, anchor-based integration, and reference-guided cell-type annotation to characterize pre-leukemic populations. Extended with pseudotime, fate mapping, and survival analysis of PLPS/Stem11 signatures against NCI clinical data. Deployed findings via an interactive R Shiny dashboard.

**Platforms & Tools:** R, Python, R Shiny, Seurat, Jupyter, Conda, shinyapps.io

Source data drawn from [Zeng et al., *Cell Genomics* (2023)](https://doi.org/10.1016/j.xgen.2023.100426) and AML clinical data from NCI.

<iframe src="https://naraenp2.shinyapps.io/preleuk_dashboard/" 
        style="width: 100%; height: 800px; border: 1px solid var(--pa-card-border);">
</iframe>