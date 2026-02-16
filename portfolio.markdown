---
layout: page
title: Portfolio
permalink: /portfolio/
---

<div class="portfolio-grid">
  {% for item in site.portfolio %}
    <a href="{{ item.url | relative_url }}" class="portfolio-item">
      <img src="{{ item.thumbnail | relative_url }}" alt="{{ item.title }}" loading="lazy">
      <h3>{{ item.title }}</h3>
      <p>{{ item.description }}</p>
    </a>
  {% endfor %}
</div>