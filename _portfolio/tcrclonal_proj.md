---
layout: page
title: "TCR Clonality Analysis"
description: "Bulk TCR-β repertoire analysis comparing clonality and antigen-specific frequencies in TB progressors vs. controllers."
thumbnail: "/assets/images/portfolio/tcr_clonal.png"
---

Analyzed publicly available bulk TCR-β sequencing data to test whether repertoire clonality and *M. tuberculosis*-specific clonotype frequency differ between TB progressors and controllers. Standardized V/J/CDR3 nomenclature to IMGT format, cross-referenced experimental repertoires against curated IEDB and VDJdb reference sets, and computed total and antigen-specific clonality metrics with statistical comparison across patient groups.

**Platforms & Tools:** Python, Jupyter, tcrdist3, pandas, NumPy, SciPy, seaborn, Conda

Source data drawn from [Musvosvi et al., *Nature Medicine* (2022)](https://doi.org/10.1038/s41591-022-02110-9). Methodology mirrors prior work published in *Frontiers in Immunology*.

<iframe
src="/assets/pdf/TCR_analysis.html"
width="100%"
height="900px"
frameborder="0"
style="border: 1px solid var(--pa-card-border); border-radius: 0;"
title="Jupyter Notebook Embedded Report"
></iframe>