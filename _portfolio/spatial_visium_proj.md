---
layout: page
title: "Spatial transcriptomics: Visium breast-cancer cell-type deconvolution (Nextflow)"
description: "A reproducible Nextflow DSL2 pipeline that takes a 10x Visium breast-cancer section plus an annotated scRNA-seq atlas and maps cell types back into tissue space: per-spot NNLS deconvolution and spatially variable genes, rendered as interactive figures."
thumbnail: "/assets/images/portfolio/spatial_visium.svg"
slug: spatial_visium_proj   # joins this page to its entry in content.yml projects
---

A reproducible **[Nextflow DSL2](https://www.nextflow.io/)** pipeline that takes a
**10x Visium** spatial transcriptomics section plus an **annotated scRNA-seq
reference** and maps cell types back into tissue space. Two readouts: per-spot
**cell-type deconvolution** (which cell types sit where, and in what proportion)
and **spatially variable genes** (which genes vary across the tissue rather than
at random). It is the spatial companion to my
[AML differential-expression pipeline](/portfolio/aml_proj/): where that one maps
*phenotype to genes*, this one maps *tissue to cell types in space*.

### Data

The real target is breast cancer. The spatial side is the **10x Visium Human
Breast Cancer (Block A, Section 1)** demo section (Space Ranger 1.1.0, CC BY 4.0):
3,798 in-tissue spots across 36,601 genes. The reference is the **Wu et al. 2021**
single-cell atlas of human breast cancers (GEO **[GSE176078](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176078)**), 100,064 cells
annotated into 9 major cell types (cancer and normal epithelial, CAFs, PVL,
endothelial, myeloid, T, B, plasmablast). The reference is not patient-matched to
the section; it is a cross-platform cell-type reference, which is the realistic
deconvolution setting. One fetch script pulls both and arranges them, and a pinned
conda env makes the run reproducible.

### Pipeline

A small, readable DSL2 workflow (channels, processes, `publishDir`,
profile-driven config). **Nine stages:**

1. [`LOAD_SPATIAL`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/load_spatial.py) / [`LOAD_REFERENCE`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/load_reference.py): read the Visium filtered matrix plus tissue positions, and the annotated reference, into AnnData on one code path for toy and real data.
2. [`QC_SPATIAL`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/qc_spatial.py): per-spot counts, genes, and mitochondrial fraction, with threshold filtering.
3. [`NORMALIZE`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/normalize.py): library-size normalization and log1p, then highly variable genes chosen on the reference and intersected with the spatial genes, putting both into one shared 2,000-gene space (20,309 genes are shared before HVG selection).
4. [`BUILD_SIGNATURE`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/build_signature.py): a per-cell-type signature matrix, just the mean expression of each type's cells.
5. [`DECONVOLVE`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/deconvolve_nnls.py): **non-negative least squares** ([`scipy.optimize.nnls`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html)) of each spot onto the signatures, normalized to proportions. Each gene is first divided by its mean signature level (inverse-mean weighting), so the fit is not dominated by a few very high-expression genes; without it, plain NNLS on real cross-platform data collapses onto one or two loud immune signatures.
6. [`SVG`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/svg_moran.py): spatially variable genes by **Moran's I** on a symmetric kNN spot graph, computed from first principles and vectorized across genes, with a seeded permutation test.
7. [`MAKE_CELLTYPE_PLOT`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/make_celltype_plot.py) / [`MAKE_SVG_PLOT`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/bin/make_svg_plot.py): the two interactive figures below.

I deliberately kept the methods transparent (a mean-expression signature, plain
NNLS, a hand-rolled Moran's I) rather than reaching for a heavier black box. The
same preference runs through the AML pipeline, and it makes every number on this
page traceable to a few lines of code.

### Result

Run on the breast-cancer section, the deconvolution recovers the expected tumor
composition: **cancer epithelium dominates** (mean proportion 0.38, the leading
type in 2,201 of 3,798 spots), with stromal (CAF, PVL, endothelial) and immune
(myeloid, T, B, plasmablast) compartments mapping to coherent regions rather than
scattering across the section. The cell-type map below switches between the
dominant-type view and any single type's proportion gradient.

The spatially variable genes tell the same story gene-by-gene: of 1,632 expressed,
variable genes, **949 are significant** (Moran's I permutation *p* < 0.05), and the
strongest ones read as a tour of the tissue's compartments: **MUC1** (epithelial
and breast-cancer mucin), **MGP** and **IGFBP5** (stromal matrix), **CD74**
(antigen presentation), and **IGHG3** with **IGKC** (immunoglobulins marking
plasma-cell and lymphoid aggregates). The second figure shows the top genes in
space.

Because the reference is not patient-matched to this section, the absolute
proportions carry the cross-platform shift between the two assays; the
inverse-mean weighting is what keeps the transparent NNLS baseline honest under
that shift. NNLS also gives a point estimate with no uncertainty. Comparing it
against a probabilistic method that models the counts and returns a posterior
(cell2location or RCTD), alongside an R Shiny viewer over the exported maps, is a
planned follow-up.

**Platforms & Tools:** Nextflow DSL2, Python (scanpy, anndata, squidpy, numpy, scipy, scikit-learn, pandas, plotly), 10x Visium, conda, pytest

The pipeline source and the [`main.nf`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/main.nf) workflow live in [`bioinformatics-public/spatial_visium_nf`](https://github.com/naraenp/bioinformatics-public/tree/main/spatial_visium_nf); see [`docs/REPORT.md`](https://github.com/naraenp/bioinformatics-public/blob/main/spatial_visium_nf/docs/REPORT.md) for a full run report. The whole thing is reproducible with one fetch script, a pinned conda env, and an offline `--demo` mode. The demo synthesizes a toy section with planted, spatially structured cell-type proportions and self-checks that the deconvolution recovers them (mean absolute error 0.0074 against the known truth). That check is the CI gate: if a change to the method stops it recovering the planted values, the build fails. The Nextflow and no-Nextflow paths are verified to produce identical proportions.

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/spatial_celltypes.html' | relative_url }}"
          title="Spatial map of deconvolved cell types across the Visium breast-cancer section"
          loading="lazy"
          style="height: 760px;">
  </iframe>
  <figcaption>Each Visium spot coloured by its dominant deconvolved cell type (use the dropdown to switch to any single cell type's proportion map). Cancer epithelium, stroma, and immune compartments occupy coherent regions of the section.</figcaption>
</figure>

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/spatial_svg.html' | relative_url }}"
          title="Spatial expression of the top spatially variable genes"
          loading="lazy"
          style="height: 700px;">
  </iframe>
  <figcaption>The top spatially variable genes (Moran's I) in tissue space, naming the compartments that vary: epithelial (MUC1), stromal (MGP, IGFBP5), and immune (CD74, immunoglobulins).</figcaption>
</figure>
