---
layout: page
title: "Plant RNA-seq: drought tolerance differential expression (Nextflow)"
description: "A reproducible Nextflow DSL2 pipeline taking raw Illumina reads from drought-tolerant and drought-susceptible rice cultivars through alignment, quantification, and differential expression to a GO-enrichment view of the genes — and processes — that separate the two phenotypes."
thumbnail: "/assets/images/portfolio/plant_rnaseq.svg"
---

A reproducible **[Nextflow DSL2](https://www.nextflow.io/)** pipeline that takes
**raw Illumina short reads** from two rice cultivars with opposite drought
phenotypes — the tolerant landrace **Apo** and the susceptible variety
**IR64** — all the way to a functional read-out of *which genes, and which
biological processes, distinguish the two*. It's the read-processing companion
to my [bulk AML pipeline](aml_proj): where that one starts from pre-quantified
counts, this one demonstrates the full short-read path — QC and trimming,
spliced **genome alignment**, gene-level quantification, differential
expression, and **GO over-representation** — on real public plant data.

### Data

Paired-end RNA-seq from **[BioProject PRJNA338445](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA338445)** (Wilkins et al.): the
drought-tolerant cultivar **Apo** and the drought-susceptible cultivar
**IR64**, each sampled under control and drought-stress conditions. Reads are
pulled straight from the **[ENA](https://www.ebi.ac.uk/ena/browser/home)** and stream-subsampled (only the leading read
pairs of each run are downloaded) so the whole study runs on a laptop. The
reference is the **Ensembl Plants IRGSP-1.0** rice genome and annotation, and
the GO gene sets are built from **Ensembl Plants BioMart** so their gene IDs
match the annotation exactly.

### Pipeline

A small, readable DSL2 workflow (channels, processes, `publishDir`,
profile-driven config) over a standard short-read toolchain. **Ten stages:**

1. [`SUBSAMPLE`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/bin/subsample_reads.sh): deterministic `seqtk` downsampling.
2. `QC_TRIM`: `fastp` adapter/quality trimming + FastQC.
3. `HISAT2_BUILD` / [`ALIGN`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/main.nf): spliced `HISAT2` alignment to the rice genome, sorted with `samtools`.
4. `QUANTIFY`: `featureCounts` gene-level counts.
5. [`BUILD_MATRIX`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/bin/build_count_matrix.py): tidy counts + sample metadata.
6. [`RUN_DE`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/bin/run_de.py): **[pydeseq2](https://pydeseq2.readthedocs.io/)** — DESeq2 median-of-ratios normalization and a negative-binomial Wald test on the design `~condition + genotype`, so the genotype contrast (tolerant vs. susceptible) is estimated *controlling for the drought treatment*.
7. [`ENRICH`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/bin/run_enrichment.py): hypergeometric GO over-representation on the significant DE genes, with a hand-rolled Benjamini-Hochberg adjustment.
8. [`MAKE_HEATMAP`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/bin/make_heatmap.py) / [`MAKE_ENRICH_PLT`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/bin/make_enrichment_plot.py): the two interactive charts below.

The enriched processes are the phenotype link: they name the biology — stress
response, signalling, transport — that the most differentially expressed genes
belong to, connecting the transcriptome back to drought tolerance.

### Result

Across ~2 M read pairs/sample (HISAT2 to IRGSP-1.0, 83–94% aligned, 38,993 genes
quantified), **56 genes** separate the tolerant and susceptible cultivars at
padj < 0.05. Those genes are over-represented for **defense response** (padj
1.4 × 10⁻⁴), **response to other organism**, and **defense response to other
organism**, with **diterpenoid metabolic process** — rice phytoalexin
(momilactone) biosynthesis — and photosynthesis close behind. That is the
phenotype link in one line: the transcriptional gap between a drought-tolerant
and a drought-susceptible rice line concentrates in stress- and defense-related
biology. The heatmap below shows the two genotype blocks separating cleanly; the
bar chart ranks the enriched processes.

**Platforms & Tools:** Nextflow DSL2, HISAT2, samtools, subread/featureCounts, fastp, seqtk, Python (pydeseq2 / pandas / numpy / scipy / plotly), Ensembl Plants, ENA, conda, pytest

The pipeline source and the [`main.nf`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/main.nf) workflow live in [`bioinformatics-public/plant_rnaseq_nf`](https://github.com/naraenp/bioinformatics-public/tree/main/plant_rnaseq_nf); see [`docs/REPORT.md`](https://github.com/naraenp/bioinformatics-public/blob/main/plant_rnaseq_nf/docs/REPORT.md) for a full run report. The whole thing is reproducible with one fetch script, a pinned conda env, and an offline toy-genome mode used as the CI smoke test.

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/plant_heatmap.html' | relative_url }}"
          title="Heatmap of top differentially expressed genes, tolerant vs. susceptible rice"
          loading="lazy"
          style="height: 780px;">
  </iframe>
  <figcaption>Top differentially expressed genes between the tolerant (Apo) and susceptible (IR64) cultivars, row z-scored and clustered. Genotype blocks separate cleanly.</figcaption>
</figure>

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/plant_enrichment.html' | relative_url }}"
          title="GO process enrichment among differentially expressed genes"
          loading="lazy"
          style="height: 620px;">
  </iframe>
  <figcaption>Biological processes over-represented among the DE genes — the phenotype-facing summary, linking the differentially expressed genes to drought-relevant biology.</figcaption>
</figure>

> **Scope note:** reads are stream-subsampled and the two within-genotype
> libraries (control + stress) act as replicates for the genotype contrast — a
> deliberate, documented trade-off that keeps the project laptop-reproducible
> rather than a maximally powered study. Swapping in more biological replicates
> and the full read depth is a drop-in change.
