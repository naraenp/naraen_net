---
layout: page
title: Log
description: "Occasional notes on what's on my mind, what I'm reading, and what I'm building."
permalink: /log/
---

<p class="log-intro">Occasional notes on what I'm building and thinking about, including a running habit of reading and reviewing one paper a day.</p>

{% assign now_reading = site.data.reading | where: "status", "reading" %}
{% if now_reading.size > 0 %}
<aside class="log-reading">
  <span class="log-reading__label">Currently reading</span>
  <span class="log-reading__books">
    {% for book in now_reading %}<span class="log-reading__book"><em>{{ book.title }}</em> by {{ book.author }}</span>{% unless forloop.last %}<span class="log-reading__sep"> · </span>{% endunless %}{% endfor %}
  </span>
  <a class="log-reading__more" href="{{ '/reading/' | relative_url }}">Full shelf →</a>
</aside>
{% endif %}

{% comment %} Chips come from the fixed vocabulary (site.log_tags), limited to tags that have at least one post. {% endcomment %}
{% assign present_tags = "" | split: "" %}
{% for tag in site.log_tags %}{% assign n = site.posts | where_exp: "p", "p.tags contains tag" | size %}{% if n > 0 %}{% assign present_tags = present_tags | push: tag %}{% endif %}{% endfor %}

{% if present_tags.size > 0 %}
<div class="log-filter" role="group" aria-label="Filter posts by tag">
  <button type="button" class="filter-chip is-active" data-tag="all" aria-pressed="true">All</button>
  {% for tag in present_tags %}
  <button type="button" class="filter-chip" data-tag="{{ tag | slugify }}" aria-pressed="false">{{ tag }}</button>
  {% endfor %}
</div>
{% endif %}

{% if site.posts.size == 0 %}
<p class="log-empty">No posts yet. The first one is on its way.</p>
{% endif %}

<ul class="post-list" id="post-list">
  {% for post in site.posts %}
  {% assign tag_slugs = "" %}{% for tag in post.tags %}{% assign tag_slugs = tag_slugs | append: tag | slugify | append: " " %}{% endfor %}
  <li class="post-card" data-tags="{{ tag_slugs | strip }}">
    <a href="{{ post.url | relative_url }}">
      <span class="post-card__date">{{ post.date | date: "%b %-d, %Y" }} · {{ post.content | number_of_words | divided_by: 200 | plus: 1 }} min read</span>
      <h3 class="post-card__title">{{ post.title | escape }}</h3>
      <p class="post-card__excerpt">{{ post.excerpt | strip_html | truncate: 180 }}</p>
      {% if post.tags.size > 0 %}
      <span class="post-card__tags">{% for tag in post.tags %}<span class="post-tag">{{ tag }}</span>{% endfor %}</span>
      {% endif %}
    </a>
  </li>
  {% endfor %}
</ul>

<p class="log-empty" id="log-empty" hidden>No posts with that tag yet.</p>

<script>
(function () {
  'use strict';
  var chips = Array.prototype.slice.call(document.querySelectorAll('.filter-chip'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.post-card'));
  var empty = document.getElementById('log-empty');
  if (!chips.length) return;

  function filter(tag) {
    var shown = 0;
    cards.forEach(function (card) {
      var tags = (card.getAttribute('data-tags') || '').split(/\s+/);
      var match = tag === 'all' || tags.indexOf(tag) !== -1;
      card.hidden = !match;
      if (match) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      chips.forEach(function (c) { c.classList.remove('is-active'); c.setAttribute('aria-pressed', 'false'); });
      chip.classList.add('is-active');
      chip.setAttribute('aria-pressed', 'true');
      filter(chip.getAttribute('data-tag'));
    });
  });
})();
</script>
