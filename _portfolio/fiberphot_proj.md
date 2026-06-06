---
layout: page
title: "Fiber Photometry Web App"
description: "R Shiny web app streamlining fiber photometry data processing and figure generation, built for the Sweeney Lab."
thumbnail: "/assets/images/portfolio/fiber_photometry.svg"
---

<h3>Live Application Demo</h3>

Developed an R Shiny web app during my undergraduate work in **Dr. Patrick Sweeney's lab** to streamline fiber photometry data analysis. Lab members upload raw recordings and experiment-specific metadata directly through the browser and receive processed signals, summary statistics, and publication-ready figures, eliminating the per-experiment scripting overhead that previously bottlenecked downstream analysis.

The tool was used in [Sweeney et al., *Journal of Neuroscience* (2023) "Paraventricular Thalamic MC3R Circuits Link Energy Homeostasis with Anxiety-Related Behavior"](https://www.jneurosci.org/content/43/36/6280), where fiber photometry recordings were processed to characterize MC3R neuron activity dynamics.

**Platforms & Tools:** R, R Shiny, ggplot2, shinyapps.io

<figure class="media-figure">
  <iframe src="https://naraenp2.shinyapps.io/fp_final/"
          title="Fiber photometry R Shiny app"
          loading="lazy"
          style="height: 800px;">
  </iframe>
  <figcaption>Live R Shiny app: upload raw fiber photometry recordings and metadata to get processed signals, summary statistics, and publication-ready figures.</figcaption>
</figure>
