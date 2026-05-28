---
layout: page
title: Photos
description: A small set of photographs.
permalink: /gallery/
---

<p class="gallery-intro">A small set of photographs. Click any image to view it full size.</p>

<ul class="gallery-grid" id="gallery-grid" aria-label="Photo thumbnails">
{%- for photo in site.data.gallery %}
  <li class="gallery-cell">
    <button type="button" class="gallery-thumb"
            data-full="{{ '/assets/gallery/full/' | append: photo.file | relative_url }}"
            data-caption="{{ photo.caption | escape }}"
            aria-label="Open: {{ photo.caption | escape }}">
      <img src="{{ '/assets/gallery/thumbs/' | append: photo.file | relative_url }}"
           alt="{{ photo.caption | escape }}" loading="lazy" decoding="async">
    </button>
  </li>
{%- endfor %}
</ul>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button type="button" class="lightbox__btn lightbox__close" id="lb-close" aria-label="Close (Esc)">&times;</button>
  <button type="button" class="lightbox__btn lightbox__nav lightbox__nav--prev" id="lb-prev" aria-label="Previous (left arrow)">&lsaquo;</button>
  <button type="button" class="lightbox__btn lightbox__nav lightbox__nav--next" id="lb-next" aria-label="Next (right arrow)">&rsaquo;</button>
  <figure class="lightbox__figure">
    <img class="lightbox__img" id="lb-img" alt="">
    <figcaption class="lightbox__caption" id="lb-caption"></figcaption>
    <span class="lightbox__counter" id="lb-counter"></span>
  </figure>
</div>

<script>
(function () {
  'use strict';
  var lightbox  = document.getElementById('lightbox');
  var lbImg     = document.getElementById('lb-img');
  var lbCaption = document.getElementById('lb-caption');
  var lbCounter = document.getElementById('lb-counter');

  // Build the photo list from the server-rendered thumbnails (curated order).
  var thumbs = [].slice.call(document.querySelectorAll('#gallery-grid .gallery-thumb'));
  var photos = thumbs.map(function (btn) {
    return { full: btn.getAttribute('data-full'), caption: btn.getAttribute('data-caption') };
  });
  var current = -1;

  function show(i) {
    var p = photos[i];
    lbImg.src = p.full;
    lbImg.alt = p.caption;
    lbCaption.textContent = p.caption;
    lbCounter.textContent = (i + 1) + ' / ' + photos.length;
    current = i;
  }
  function open(i) {
    show(i);
    lightbox.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    lightbox.classList.remove('is-open');
    lbImg.src = '';
    document.body.style.overflow = '';
    current = -1;
  }
  function step(d) {
    if (current < 0) return;
    show((current + d + photos.length) % photos.length);
  }

  thumbs.forEach(function (btn, i) {
    btn.addEventListener('click', function () { open(i); });
  });
  document.getElementById('lb-close').addEventListener('click', close);
  document.getElementById('lb-prev').addEventListener('click', function () { step(-1); });
  document.getElementById('lb-next').addEventListener('click', function () { step(1); });
  lightbox.addEventListener('click', function (e) { if (e.target === lightbox) close(); });
  document.addEventListener('keydown', function (e) {
    if (current < 0) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });
})();
</script>
