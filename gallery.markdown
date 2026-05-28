---
layout: page
title: Photos
description: A small set of photographs.
permalink: /gallery/
---

<p class="gallery-intro">A small set of photographs. Click any image to view it full size.</p>

<ul class="gallery-grid" id="gallery-grid" aria-label="Photo thumbnails"></ul>

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

  var BASE      = '{{ "/assets/gallery/" | relative_url }}';
  var CAPTIONS  = '{{ "/assets/gallery/captions.json" | relative_url }}';
  var FULL_DIR  = BASE + 'full/';
  var THUMB_DIR = BASE + 'thumbs/';

  var grid      = document.getElementById('gallery-grid');
  var lightbox  = document.getElementById('lightbox');
  var lbImg     = document.getElementById('lb-img');
  var lbCaption = document.getElementById('lb-caption');
  var lbCounter = document.getElementById('lb-counter');

  var photos = [];      // [{ file, caption }]
  var current = -1;     // index of the open photo, -1 when closed

  /* ---------- Build the grid ---------- */
  function render() {
    var frag = document.createDocumentFragment();

    photos.forEach(function (photo, i) {
      var li = document.createElement('li');
      li.className = 'gallery-cell';

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'gallery-thumb';
      btn.setAttribute('aria-label', 'Open: ' + photo.caption);
      btn.addEventListener('click', function () { open(i); });

      var img = document.createElement('img');
      img.src = THUMB_DIR + photo.file;
      img.alt = photo.caption;
      img.loading = 'lazy';
      img.decoding = 'async';

      btn.appendChild(img);
      li.appendChild(btn);
      frag.appendChild(li);
    });

    grid.innerHTML = '';
    grid.appendChild(frag);
  }

  /* ---------- Lightbox ---------- */
  function show(i) {
    var photo = photos[i];
    lbImg.src = FULL_DIR + photo.file;
    lbImg.alt = photo.caption;
    lbCaption.textContent = photo.caption;
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
  function step(delta) {
    if (current < 0) return;
    show((current + delta + photos.length) % photos.length);
  }

  document.getElementById('lb-close').addEventListener('click', close);
  document.getElementById('lb-prev').addEventListener('click', function () { step(-1); });
  document.getElementById('lb-next').addEventListener('click', function () { step(1); });
  lightbox.addEventListener('click', function (e) { if (e.target === lightbox) close(); });
  document.addEventListener('keydown', function (e) {
    if (current < 0) return;
    if (e.key === 'Escape')          close();
    else if (e.key === 'ArrowLeft')  step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });

  /* ---------- Load captions, then render (preserve their order) ---------- */
  fetch(CAPTIONS, { cache: 'no-cache' })
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (caps) {
      photos = Object.keys(caps).map(function (file) {
        return { file: file, caption: caps[file] };
      });
      render();
    })
    .catch(function (err) {
      grid.innerHTML = '<li class="gallery-cell" style="padding:16px;color:var(--pa-fg-muted)">' +
        'Could not load captions (' + err.message + ').</li>';
    });
})();
</script>
