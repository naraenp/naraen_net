---
layout: page
title: Search
description: "Search the Log, portfolio, and pages on naraen.net."
permalink: /search/
---

<div id="search" class="pf-search"></div>

<noscript><p class="log-empty">Search needs JavaScript. Browse the <a href="{{ '/log/' | relative_url }}">Log</a> or <a href="{{ '/portfolio/' | relative_url }}">portfolio</a> directly.</p></noscript>

<link rel="stylesheet" href="{{ '/pagefind/pagefind-ui.css' | relative_url }}">
<script src="{{ '/pagefind/pagefind-ui.js' | relative_url }}"></script>
<script>
  window.addEventListener('DOMContentLoaded', function () {
    if (typeof PagefindUI === 'undefined') return;
    new PagefindUI({
      element: '#search',
      showImages: false,
      showSubResults: true,
      resetStyles: false
    });
  });
</script>
