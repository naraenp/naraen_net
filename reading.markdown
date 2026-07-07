---
layout: page
title: Reading
description: "Books I'm reading, have read, and want to read next."
permalink: /reading/
---

<p class="reading-intro">A running shelf of what I'm reading now, recently finished, and queued up next.</p>

{% assign groups = "reading,finished,queue" | split: "," %}
{% assign labels = "Currently reading,Finished,Queue" | split: "," %}

{% for status in groups %}
  {% assign books = site.data.reading | where: "status", status %}
  {% if books.size > 0 %}
  <section class="reading-group">
    <h2 class="reading-group__title">{{ labels[forloop.index0] }}</h2>
    <ul class="reading-list">
      {% for book in books %}
      <li class="reading-item">
        <div class="reading-item__head">
          <span class="reading-item__title">
            {% if book.link != "" and book.link %}<a href="{{ book.link }}" rel="noopener">{{ book.title }}</a>{% else %}{{ book.title }}{% endif %}
          </span>
          <span class="reading-item__author">{{ book.author }}</span>
        </div>
        {% if book.note != "" and book.note %}<p class="reading-item__note">{{ book.note }}</p>{% endif %}
        {% if book.post != "" and book.post %}<a class="reading-item__post" href="{{ book.post | relative_url }}">Read my notes →</a>{% endif %}
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
{% endfor %}
