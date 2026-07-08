---
layout: post
title: "Where the software lives in the DBTL loop"
date: 2026-07-08 15:25:00 -0500
tags: [paper]
paper:
  title: "Technologies for design-build-test-learn automation and computational modelling across the synthetic biology workflow: a review"
  authors: "Network Modeling Analysis in Health Informatics and Bioinformatics"
  venue: "NetMAHIB, 2024"
  link: "https://doi.org/10.1007/s13721-024-00455-4"
  verdict: "The best single 'where does a data shop fit' map of the DBTL toolchain — read for the hand-off points."
---

**The problem.** Synthetic biology is organized around the Design–Build–Test–Learn cycle, but "where exactly does software add value?" is usually hand-waved. This review answers it computation-first, walking the whole loop and naming the tools at each stage.

**The idea.** It surveys the DBTL toolchain node by node. **Design**: biological CAD, pathway and genome design, sequence/part selection. **Build**: DNA-assembly automation and biofoundry robotics. **Test**: analytics and omics readouts that quantify what was built. **Learn**: ML models, active learning, and design-of-experiments that turn test data into the next design. Crucially, it foregrounds the *hand-offs* — the data formats and interfaces where one stage feeds the next — which is precisely where a software/data layer either exists or doesn't.

**Why it matters.** This is the most useful positioning document I've read for the "bioinformatics shop eyeing synbio" question. The wet-lab **Build** needs a foundry; the **Design** and **Learn** ends, and every **hand-off** between stages, are software and data problems — exactly what a pipelines-and-ML team can own without owning a lab. It reframes DBTL from a biology diagram into a systems-integration diagram, which is a language I already speak.

**Verdict.** As a 2024 survey it's current and refreshingly computation-centric, though (being a review) it's a map, not evidence — the real test is whether the hand-off seams it identifies are as ownable as they look. My plan: extract its DBTL diagram and annotate each node with "foundry-required" vs. "a data shop can own this," as a positioning artifact.
