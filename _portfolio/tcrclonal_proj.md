---
layout: page
title: "TCR Clonality Analysis"
description: "Bulk TCR-β repertoire analysis comparing clonality and antigen-specific frequencies in TB progressors vs. controllers."
thumbnail: "/assets/images/portfolio/tcr_clonality.svg"
---

Analyzed publicly available bulk TCR-β sequencing data to test whether **repertoire clonality** and ***M. tuberculosis*-specific clonotype frequency** differ between TB progressors and controllers. The workflow imports Adaptive-format repertoires with [`tcrdist3`](https://tcrdist3.readthedocs.io/), standardizes V/J/CDR3 nomenclature to IMGT format, and cross-references experimental repertoires against curated **IEDB** and **VDJdb** reference sets to flag TB-specific clonotypes. From there it computes total and antigen-specific clonality (1 - normalized Shannon entropy) and TB-specific template frequency, then statistically compares the two cohorts.

Across these metrics, the analysis found **no strong correlation** between TCR-β clonality or TB-specific frequency and progressor/controller status, suggesting that clonality alone is insufficient to stratify *M. tuberculosis* infection trajectory in this cohort.

**Platforms & Tools:** Python, Jupyter, tcrdist3, pandas, NumPy, SciPy, seaborn, Conda

Source data drawn from [Musvosvi et al., *Nature Medicine* (2022)](https://doi.org/10.1038/s41591-022-02110-9). Methodology mirrors prior work published in [*Frontiers in Immunology*](https://doi.org/10.3389/fimmu.2025.1576903). Notebook source lives in [`bioinformatics-public/tcr_analysis`](https://github.com/naraenp/bioinformatics-public/tree/main/tcr_analysis).

<figure class="media-figure">
  <iframe
  src="/assets/pdf/TCR_analysis.html"
  height="900px"
  frameborder="0"
  title="Jupyter Notebook Embedded Report"
  ></iframe>
  <figcaption>Embedded Jupyter notebook report: the full TCR-β clonality analysis, figures and all.</figcaption>
</figure>
