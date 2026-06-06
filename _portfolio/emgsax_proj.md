---
layout: page
title: "EMG-Controlled Saxophone"
description: "Assistive prosthetic concept actuating saxophone keys via a surface-EMG analog front end and an Arduino servo system, exhibited at the 2023 Engineering Open House."
thumbnail: "/assets/images/portfolio/emg_saxophone.svg"
---

#### Group Members: Amaan Mirza, Lianna Mateski, Wyatt Wethington, Zyra Sheikh, and Myself

Designed and exhibited a prosthetic concept for the 2023 Engineering Open House that translates forearm muscle activation into saxophone keypresses, exploring how EMG-driven assistive devices could let musicians with limb-function loss continue playing. The system pairs a breadboarded surface-EMG front end (instrumentation amplifier, bandpass filtering, rectification) with an Arduino Uno that thresholds the signal and actuates servo motors over three saxophone keys. Designing and building the analog EMG acquisition circuit on the breadboard was my primary responsibility on the team. It is shown up close below, with the wired saxophone behind it, and again on the right side of our exhibit booth at the show.

**Platforms & Tools:** Arduino, C/C++, surface EMG circuitry, servo actuation

<figure class="media-figure media-figure--portrait">
  <img src="{{ '/assets/images/portfolio/emg_saxophone_circuit.jpg' | relative_url }}"
       alt="Close-up of the EMG saxophone build, with the breadboarded acquisition circuit and its jumper wires in the foreground and the wired saxophone in its case behind it"
       width="1200" height="1600" loading="lazy">
  <figcaption>The breadboarded EMG acquisition circuit (foreground) and the wired saxophone behind it. Building this circuit was my primary responsibility on the project.</figcaption>
</figure>

<figure class="media-figure">
  <img src="{{ '/assets/images/portfolio/emg_saxophone_booth.png' | relative_url }}"
       alt="Exhibit booth at the 2023 Engineering Open House showing the breadboarded EMG circuit on the right side of the table"
       width="682" height="666" loading="lazy">
  <figcaption>Our booth at the 2023 Engineering Open House, with the EMG circuit set up on the right.</figcaption>
</figure>