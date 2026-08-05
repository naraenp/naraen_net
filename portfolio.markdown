---
layout: page
title: Portfolio
description: "Bioinformatics and engineering projects by Naraen Palanikumar: Nextflow pipelines, single-cell and spatial analyses, and research tooling."
permalink: /portfolio/
---

{%- comment -%}
  The index is generated from content.yml's `projects` list (via
  _data/profile.yml), joined to the pages in _portfolio/ on `slug`.

  - `projects` supplies the order and the stack chips.
  - The matching _portfolio page supplies the thumbnail, title, description,
    and the URL, so page-level content stays with the page.
  - Where several projects share one page (the two AML projects), the extras
    carry `secondary_to`. Only the primary renders a card; the secondaries
    still contribute their stack chips.
  - Projects with no page (Bench) render as external cards.
  - Any _portfolio page that no project references still renders, at the end.
    Adding a page without a content.yml entry must never drop it from here.
{%- endcomment -%}

{%- assign rendered_slugs = "" | split: "" -%}

<div class="portfolio-grid">
{%- for project in site.data.profile.projects -%}
  {%- if project.secondary_to -%}{%- continue -%}{%- endif -%}
  {%- if project.slug -%}
    {%- unless rendered_slugs contains project.slug -%}
    {%- assign page_match = site.portfolio | where: "slug", project.slug | first -%}
    {%- if page_match -%}
      {%- assign rendered_slugs = rendered_slugs | push: project.slug -%}
      {%- comment -%}
        Some pages cover more than one project (the two AML projects share
        aml_proj). Merge the stacks so the chips describe the whole page.
      {%- endcomment -%}
      {%- assign stack = "" | split: "" -%}
      {%- for sibling in site.data.profile.projects -%}
        {%- if sibling.slug == project.slug -%}
          {%- for tech in sibling.stack -%}
            {%- unless stack contains tech -%}{%- assign stack = stack | push: tech -%}{%- endunless -%}
          {%- endfor -%}
        {%- endif -%}
      {%- endfor %}
  <a href="{{ page_match.url | relative_url }}" class="portfolio-item">
    <img src="{{ page_match.thumbnail | relative_url }}" alt="" width="640" height="360" loading="lazy" decoding="async">
    <h2 class="portfolio-item__title">{{ page_match.title }}</h2>
    {%- if stack.size > 0 %}
    <p class="portfolio-item__stack">{{ stack | join: " · " }}</p>
    {%- endif %}
    <p class="portfolio-item__desc">{{ page_match.description }}</p>
  </a>
    {%- endif -%}
    {%- endunless -%}
  {%- elsif project.url %}
  <a href="{{ project.url }}" class="portfolio-item portfolio-item--external" rel="noopener">
    {%- comment -%}
      Bench has no page in _portfolio/, so its card carries its own thumbnail
      from content.yml to sit flush with the rest of the grid. Without one it
      falls back to the text eyebrow rather than rendering a broken image.
    {%- endcomment -%}
    {%- if project.thumbnail %}
    <img src="{{ project.thumbnail | relative_url }}" alt="" width="640" height="360" loading="lazy" decoding="async">
    {%- else %}
    <p class="portfolio-item__eyebrow">External<span class="visually-hidden"> link</span></p>
    {%- endif %}
    <h2 class="portfolio-item__title">{{ project.short_name | default: project.name }}<span class="portfolio-item__external" aria-hidden="true">↗</span><span class="visually-hidden"> (external site)</span></h2>
    {%- if project.stack.size > 0 %}
    <p class="portfolio-item__stack">{{ project.stack | join: " · " }}</p>
    {%- endif %}
    {%- if project.bullets.size > 0 %}
    <p class="portfolio-item__desc">{{ project.bullets.first.text }}</p>
    {%- endif %}
  </a>
  {%- endif -%}
{%- endfor -%}

{%- comment -%} Safety net: pages with no matching project entry. {%- endcomment -%}
{%- for item in site.portfolio -%}
  {%- unless rendered_slugs contains item.slug %}
  <a href="{{ item.url | relative_url }}" class="portfolio-item">
    <img src="{{ item.thumbnail | relative_url }}" alt="" width="640" height="360" loading="lazy" decoding="async">
    <h2 class="portfolio-item__title">{{ item.title }}</h2>
    <p class="portfolio-item__desc">{{ item.description }}</p>
  </a>
  {%- endunless -%}
{%- endfor %}
</div>
