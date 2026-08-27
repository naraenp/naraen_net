---
layout: page
title: "Germline variant calling: GATK short-variant pipeline (Nextflow)"
description: "A reproducible Nextflow DSL2 pipeline taking raw Illumina short reads through the GATK germline best-practice path (BWA-MEM alignment, duplicate marking, HaplotypeCaller joint genotyping, hard-filtering, and consequence annotation) to a filtered cohort VCF. Validated on a synthetic cohort with planted variants, and wired to benchmark against the GIAB HG002 truth set."
thumbnail: "/assets/images/portfolio/variant_calling.svg"
slug: variant_calling_proj   # joins this page to its entry in content.yml projects
---

A reproducible **[Nextflow DSL2](https://www.nextflow.io/)** pipeline that takes
**raw Illumina short reads** through the **[GATK](https://gatk.broadinstitute.org/)
germline short-variant best-practice path** to a filtered, annotated **cohort
VCF**. It is the **DNA-variant** member of my bioinformatics portfolio: where the
[bulk](/portfolio/plant_rnaseq_proj/) [RNA-seq](/portfolio/aml_proj/) and
[spatial](/portfolio/spatial_visium_proj/) pipelines quantify *expression*, this one
genotypes **SNVs and short indels** from the genome itself, the most common
task in clinical and population genomics.

### Data

The offline path runs on a **synthetic diploid cohort**: six samples in two
groups, with a planted set of **germline variants** (shared across the cohort
plus group-specific) written to a ground-truth VCF. The whole DAG, including a
recovery self-check, runs in under a minute with no download. The **real
target** is the **[Genome in a Bottle](https://www.nist.gov/programs-projects/genome-bottle)**
sample **HG002** (NIST / NA24385): a high-confidence slice of GRCh38 **chr20**,
with reads **range-sliced** straight out of GIAB's chr20 300× BAM over HTTPS
(only the bytes for the target window are fetched), benchmarked against the
**NIST v4.2.1** high-confidence truth VCF and confident-region BED. The reference
is GRCh38 chr20 (UCSC) and the annotation is **GENCODE v46**.

### Pipeline

A small, readable DSL2 workflow (channels, processes, `publishDir`,
profile-driven config) over the standard germline toolchain. **Twelve stages:**

1. [`SUBSAMPLE`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/bin/subsample_reads.sh): deterministic `seqtk` downsampling.
2. `QC_TRIM`: `fastp` adapter/quality trimming.
3. `PREP_REFERENCE`: `samtools faidx` + GATK sequence dictionary + `bwa index`.
4. [`ALIGN`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/main.nf): `bwa mem` with per-sample read groups, sorted with `samtools`.
5. `MARK_DUPLICATES`: `gatk MarkDuplicates`.
6. `CALL_VARIANTS`: `gatk HaplotypeCaller` in **GVCF mode** per sample (local haplotype reassembly).
7. `JOINT_GENOTYPE`: `CombineGVCFs` + `GenotypeGVCFs`, the GATK best-practice cohort call.
8. `FILTER_VARIANTS`: `gatk VariantFiltration` hard filters on **separate SNP and indel tracks** (the documented substitute for VQSR on small cohorts).
9. `NORMALIZE`: `bcftools norm` splits multiallelics and left-aligns indels.
10. [`ANNOTATE`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/bin/annotate_variants.py): a hand-rolled genic-consequence annotator (exonic / intronic / intergenic) that also tags SNVs as transitions or transversions.
11. [`MAKE_OVERVIEW`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/bin/make_overview.py) / [`MAKE_GENO_HEATMAP`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/bin/make_geno_heatmap.py): the two interactive charts below.

### Result

On the synthetic cohort the pipeline achieves **perfect recovery** of the
planted variants: **24/24 sites at recall = precision = 1.00**, with **genotype
concordance 1.00** across all 144 sample-genotypes and a cohort **Ts/Tv of
2.17**. The Nextflow and `run_local.sh` paths produce an *identical* normalized
callset. The self-check (`check_truth.py`) normalizes the called VCF and the
planted truth with `bcftools`, then asserts that recall, precision, and genotype
concordance pass threshold. That is the variant-calling analog of the
planted-DE-gene and planted-cell-type checks in the sibling pipelines. The
overview chart breaks each sample's calls down by genic region; the genotype
heatmap shows the planted group structure separating cleanly into group-A and
group-B variant blocks.

**Platforms & Tools:** Nextflow DSL2, BWA-MEM, samtools, GATK4 (MarkDuplicates / HaplotypeCaller / GenotypeGVCFs / VariantFiltration), bcftools, fastp, seqtk, Python (pandas / numpy / scipy / plotly), GIAB / NIST, GENCODE, conda, pytest

The pipeline source and the [`main.nf`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/main.nf) workflow live in [`bioinformatics-public/variant_calling_nf`](https://github.com/naraenp/bioinformatics-public/tree/main/variant_calling_nf); see [`docs/REPORT.md`](https://github.com/naraenp/bioinformatics-public/blob/main/variant_calling_nf/docs/REPORT.md) for a full run report. The whole thing is reproducible with one fetch script, a pinned conda env, and an offline synthetic mode that self-checks variant recovery and acts as the validation path.

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/variant_genotypes.html' | relative_url }}"
          title="Genotype heatmap of the most discriminating variants across the cohort"
          loading="lazy"
          style="height: 640px;">
  </iframe>
  <figcaption>Alt-allele dosage of the most discriminating variants across the synthetic cohort. The planted group-specific variants partition cleanly into group-A and group-B blocks; shared variants are present across all samples.</figcaption>
</figure>

<figure class="media-figure">
  <iframe src="{{ '/assets/embeds/variant_overview.html' | relative_url }}"
          title="Per-sample variant counts by genic region"
          loading="lazy"
          style="height: 560px;">
  </iframe>
  <figcaption>Per-sample PASS-variant counts split by genic region (exonic / intronic / intergenic), with the cohort transition/transversion ratio, a standard germline callset-QC read-out.</figcaption>
</figure>

> **Scope note:** the headline metrics are from the offline synthetic cohort,
> where ground truth is exact. The real GIAB HG002 run is fully wired and the
> data sources verified (`fetch_real_data.sh`), benchmarked with `bcftools isec`
> against the NIST truth, but the multi-GB-adjacent fetch is run on demand rather
> than in CI. Filtering is GATK hard-filters rather than VQSR/CNN (which need
> large cohorts or pretrained models), and somatic calling (Mutect2) is a natural
> drop-in sibling. Both are deliberate, documented trade-offs that keep the
> project laptop-reproducible.
