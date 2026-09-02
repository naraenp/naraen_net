---
layout: page
title: "TCR Clonality Analysis"
description: "Bulk TCR-β repertoire analysis testing whether clonality and TB-specific clonotype frequency differ between TB progressors and controllers, revised to respect the cohort's matched case-control design."
thumbnail: "/assets/images/portfolio/tcr_clonality.svg"
slug: tcrclonal_proj   # joins this page to its entry in content.yml projects
---

Analyzed publicly available bulk TCR-β sequencing data to test whether **repertoire clonality** and ***M. tuberculosis*-specific clonotype frequency** differ between people who progressed to active TB and those who controlled the infection. The workflow imports Adaptive-format repertoires with [`tcrdist3`](https://tcrdist3.readthedocs.io/) and standardizes V/J/CDR3 nomenclature to IMGT format. It then cross-references each repertoire against curated **IEDB** and **VDJdb** reference sets to flag TB-specific clonotypes. From those it computes total clonality and TB-specific clonality (both 1 minus normalized Shannon entropy) and TB-specific template frequency, and compares the two cohorts.

### The design

The cohort is a **matched case-control study**: each progressor was matched to controllers on time-to-diagnosis, age band, and sex, and most donors were sampled at more than one visit. The first version of this notebook pooled every sample into an unpaired Mann-Whitney test, which ignores both facts. This revision keeps the same three metrics and the same figure, and changes how they are computed and tested:

- **One baseline sample per donor**, so every observation is an independent person: 140 donors (52 progressors, 88 controllers).
- **Matched-set inference.** A stratified (van Elteren) rank test ranks donors within their matched set, and the p-value comes from permuting progressor status inside each of the 42 sets. Between-set variation never enters the contrast.
- **Depth standardization.** Normalized clonality divides by `ln(N)`, and library size spans a 181-fold range across these donors, so depth alone moves the metric. Every repertoire is rarefied to a common 43,414 templates before any statistic is computed.
- **Missing values are counted, never imputed.** Clonality is undefined below two clonotypes, and TB-specific clonality needs at least five database-matched clonotypes in most rarefaction draws, so the estimate cannot rest on a few lucky ones.
- **Effect sizes and multiplicity.** Each metric carries a Hodges-Lehmann shift with a bootstrap confidence interval, and the three tests are Benjamini-Hochberg adjusted together.

The revision also fixed a join bug. The two data sources spell sample IDs differently (`04-0333_D0` versus `04-0333-D0`), and the exact-string join had silently dropped most of the ACS cohort. A separator-insensitive join now matches 271 of 272 key records, and every unmatched ID on either side is printed.

### Result

**No difference in clonality or TB-specific frequency between progressors and controllers survives the matched-set analysis.** For total clonality the Hodges-Lehmann shift is +0.002 with a 95% interval of -0.023 to +0.021 (stratified *p* = 0.52). That interval is tight around zero: an informative null, not an underpowered one. The pooled p-values agree with the stratified ones, so the original conclusion was right, but it was right for the wrong reasons.

Exact database matching recovers a median of 16 TB-specific clonotypes per repertoire. That is enough to estimate a frequency but thin for an entropy, so TB-specific clonality is estimable in only 93 of the 140 samples. Distance-based neighborhood matching with `tcrdist3`, already a dependency here but used only as a file reader, is the first extension I would make.

**Platforms & Tools:** Python, Jupyter, tcrdist3, pandas, NumPy, SciPy, seaborn, Conda

Source data drawn from [Musvosvi et al., *Nature Medicine* (2022)](https://doi.org/10.1038/s41591-022-02110-9). Methodology mirrors prior work published in [*Frontiers in Immunology*](https://doi.org/10.3389/fimmu.2025.1576903). Notebook source lives in [`bioinformatics-public/tcr_analysis`](https://github.com/naraenp/bioinformatics-public/tree/main/tcr_analysis).

<figure class="media-figure">
  <iframe
  src="/assets/pdf/TCR_analysis.html"
  height="900px"
  frameborder="0"
  title="Jupyter Notebook Embedded Report"
  ></iframe>
  <figcaption>Embedded Jupyter notebook report: the revised TCR-β clonality analysis, with the revision note, figures, and conclusions.</figcaption>
</figure>
