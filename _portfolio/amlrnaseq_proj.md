---
layout: page
title: "AML Bulk RNA-seq Pipeline (Nextflow)"
description: "Mini Nextflow DSL2 pipeline for AML vs. healthy bulk RNA-seq DE, exercised end-to-end on TCGA-LAML + GTEx whole blood via recount3."
thumbnail: "/assets/images/portfolio/aml_rnaseq.svg"
---

Built a small **[Nextflow DSL2](https://www.nextflow.io/)** pipeline for bulk RNA-seq differential expression (AML vs. healthy) with a deliberately dual-mode design: a fast **simulated-counts mode** with planted log-fold-changes on canonical AML genes for CI and self-checking, and a **`--real_data` mode** that pulls **TCGA-LAML** and **GTEx whole-blood** gene-level counts from the **[recount3](https://rna.recount.bio/)** project (uniform Monorail / STAR / GENCODE v26 alignment) so the same pipeline operates on real public RNA-seq cohorts.

End-to-end on **50 AML vs. 50 healthy whole-blood samples × ~20 k expressed genes**: pipeline runs in ~11 s, recovers **all 20** canonical AML signature genes (FLT3, KIT, MEIS1, HOXA9, MPO, CD34, RUNX1, GATA2, …) as significant at FDR<0.05, with **14/20** in the published-literature direction. The 6 "direction mismatches" are progenitor-associated TFs (RUNX1, GATA2, DNMT3A, ASXL1, TET2) — a known confound when comparing AML bone-marrow blasts against mature peripheral blood. The signature-recovery stage surfaces it explicitly rather than hiding it.

Five Nextflow processes — `LOAD_REAL_COUNTS` (or `SIMULATE_COUNTS`) → `NORMALIZE_COUNTS` → `RUN_DE` (Welch t-test on log2-CPM + hand-rolled BH FDR) → `MAKE_VOLCANO` (interactive Plotly) → `SIGNATURE_RECOVERY` (recall / precision / median rank vs. a curated 20-gene AML signature). Pinned conda env, project-relative paths, pytest smoke test on the simulated mode.

**Platforms & Tools:** Nextflow DSL2, Python (numpy / pandas / scipy / plotly / kaleido), recount3, GENCODE v26, conda, pytest

Pipeline source and the full real-data run report live in [`bioinformatics-public/aml_rnaseq_nf`](https://github.com/naraenp/bioinformatics-public/tree/main/aml_rnaseq_nf) — see [`docs/REPORT.md`](https://github.com/naraenp/bioinformatics-public/blob/main/aml_rnaseq_nf/docs/REPORT.md) for the narrative walkthrough (methods, dataset provenance, embedded volcano, signature recovery table, runtime profile).

![Volcano plot from the real-data run: TCGA-LAML AML vs. GTEx whole-blood healthy, with the curated AML signature genes labeled. All 20 markers sit above the FDR line.](https://raw.githubusercontent.com/naraenp/bioinformatics-public/main/aml_rnaseq_nf/docs/volcano.png)
