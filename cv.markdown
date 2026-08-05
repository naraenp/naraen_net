---
layout: default
title: CV
description: "Curriculum vitae of Naraen Palanikumar: bioinformatics engineer and cloud architect. Experience, peer-reviewed publications, projects, and skills."
permalink: /cv/
---

{%- assign cv = site.data.profile -%}

<article class="post cv-page">

  <header class="title-container">
    <div class="name-and-links">
      <h1 class="cv-name">{{ cv.identity.name }}</h1>
      <p class="pa-eyebrow">Bioinformatics engineer · Cloud architect · {{ cv.identity.location }}</p>
      <p class="social-links">
        <a href="{{ '/contact/' | relative_url }}"><img src="{{ '/assets/icons/mail.svg' | relative_url }}" alt="" width="20" height="20" loading="lazy"> Contact</a>
        <a href="{{ cv.identity.linkedin }}" rel="me noopener"><img src="{{ '/assets/icons/linkedin.svg' | relative_url }}" alt="" width="20" height="20" loading="lazy"> LinkedIn</a>
        <a href="{{ cv.identity.github }}" rel="me noopener"><img src="{{ '/assets/icons/github.svg' | relative_url }}" alt="" width="20" height="20" loading="lazy"> GitHub</a>
        <a href="{{ cv.identity.orcid }}" rel="me noopener"><img src="{{ '/assets/icons/orcid.svg' | relative_url }}" alt="" width="20" height="20" loading="lazy"> ORCID</a>
      </p>
    </div>
    <a href="{{ site.resume_pdf | relative_url }}" class="download-button" download>Download resume (PDF)</a>
  </header>

  <div class="post-content">

    <section class="cv-section" aria-labelledby="cv-summary">
      <h2 class="cv-section__title" id="cv-summary">Professional summary</h2>
      <p>{{ cv.summary }}</p>
    </section>

    <section class="cv-section" aria-labelledby="cv-education">
      <h2 class="cv-section__title" id="cv-education">Education</h2>
      {%- for edu in cv.education %}
      <div class="cv-entry">
        <div class="cv-entry__head">
          <span class="cv-entry__org">{{ edu.institution }}</span>
          <span class="cv-entry__date">{{ edu.dates }}</span>
        </div>
        <div class="cv-entry__sub">
          <span class="cv-entry__role">{{ edu.degree_line }}</span>
          <span class="cv-entry__loc">{{ edu.location }}</span>
        </div>
      </div>
      {%- endfor %}
    </section>

    <section class="cv-section" aria-labelledby="cv-experience">
      <h2 class="cv-section__title" id="cv-experience">Professional experience</h2>
      {%- for job in cv.experience %}
      <div class="cv-entry">
        <div class="cv-entry__head">
          <span class="cv-entry__org">{{ job.org }}</span>
          <span class="cv-entry__date">{{ job.dates }}</span>
        </div>
        <div class="cv-entry__sub">
          <span class="cv-entry__role">{{ job.title }}</span>
          <span class="cv-entry__loc">{{ job.location }}</span>
        </div>
        {%- if job.bullets.size > 0 %}
        <ul>
          {%- for bullet in job.bullets %}
          <li>{{ bullet.text }}</li>
          {%- endfor %}
        </ul>
        {%- endif %}
      </div>
      {%- endfor %}
    </section>

    <section class="cv-section" aria-labelledby="cv-projects">
      <h2 class="cv-section__title" id="cv-projects">Projects</h2>
      {%- for project in cv.projects %}
      <div class="cv-entry">
        <div class="cv-entry__head">
          <span class="cv-entry__org">
            {%- if project.url %}<a href="{{ project.url }}">{{ project.name }}</a>{% else %}{{ project.name }}{% endif -%}
          </span>
          {%- if project.dates %}<span class="cv-entry__date">{{ project.dates }}</span>{% endif -%}
        </div>
        {%- if project.stack.size > 0 or project.team %}
        <div class="cv-entry__sub">
          <span class="cv-entry__stack">{{ project.stack | join: " · " }}</span>
          {%- if project.team %}<span class="cv-entry__loc">{{ project.team }}</span>{% endif -%}
        </div>
        {%- endif %}
        {%- if project.bullets.size > 0 %}
        <ul>
          {%- for bullet in project.bullets %}
          <li>{{ bullet.text }}</li>
          {%- endfor %}
          {%- if project.repo %}
          <li><a href="{{ project.repo }}" rel="noopener">Source on GitHub</a></li>
          {%- endif %}
        </ul>
        {%- endif %}
      </div>
      {%- endfor %}
    </section>

    <section class="cv-section" aria-labelledby="cv-publications">
      <h2 class="cv-section__title" id="cv-publications">Peer-reviewed publications</h2>
      <ol class="cv-pub-list">
        {%- for pub in cv.publications %}
        <li class="cv-pub">
          <p class="cv-pub__title">
            <a href="https://doi.org/{{ pub.doi }}" rel="noopener">{{ pub.title }}</a>
          </p>
          <p class="cv-pub__citation">{{ pub.citation }}</p>
          <p class="cv-pub__links">
            <a href="https://doi.org/{{ pub.doi }}" rel="noopener">doi:{{ pub.doi }}</a>
            {%- if pub.pmid %}<span class="cv-pub__sep" aria-hidden="true">·</span>
            <a href="https://pubmed.ncbi.nlm.nih.gov/{{ pub.pmid }}/" rel="noopener">PMID {{ pub.pmid }}</a>{% endif -%}
            {%- if pub.pmcid %}<span class="cv-pub__sep" aria-hidden="true">·</span>
            <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/{{ pub.pmcid }}/" rel="noopener">{{ pub.pmcid }}</a>{% endif -%}
          </p>
          {%- if pub.contribution %}
          <p class="cv-pub__contribution"><span class="cv-pub__label">Contribution</span> {{ pub.contribution }}</p>
          {%- endif %}
        </li>
        {%- endfor %}
      </ol>
    </section>

    <section class="cv-section" aria-labelledby="cv-skills">
      <h2 class="cv-section__title" id="cv-skills">Skills</h2>
      <dl class="cv-skills">
        {%- for group in cv.skills %}
        <dt>{{ group.label }}</dt>
        <dd>{{ group.items | join: ", " }}</dd>
        {%- endfor %}
      </dl>
    </section>

    <section class="cv-section" aria-labelledby="cv-certifications">
      <h2 class="cv-section__title" id="cv-certifications">Certifications</h2>
      <ul>
        {%- for cert in cv.certifications %}
        <li>
          {{ cert.name }}
          {%- if cert.issued_display %} <span class="cv-inline-date">({{ cert.issued_display }}{% if cert.expires_display %} - {{ cert.expires_display }}{% endif %})</span>{% endif -%}
        </li>
        {%- endfor %}
      </ul>
    </section>

    <section class="cv-section" aria-labelledby="cv-honors">
      <h2 class="cv-section__title" id="cv-honors">Honors &amp; awards</h2>
      <ul>
        {%- for honor in cv.honors %}
        <li>{{ honor.text }}</li>
        {%- endfor %}
      </ul>
    </section>

    {%- comment -%}
      Standardized exam scores are deliberately hardcoded. The numbers exist
      nowhere in content.yml (its `exam_scores` key holds only a suppression
      policy, and is private), so there is nothing to render them from.
    {%- endcomment -%}
    <section class="cv-section" aria-labelledby="cv-exams">
      <h2 class="cv-section__title" id="cv-exams">Standardized exam scores</h2>
      <div class="table-scroll">
        <table>
          <caption class="visually-hidden">Standardized exam scores with percentile and date taken</caption>
          <thead>
            <tr><th scope="col">Exam</th><th scope="col">Score</th><th scope="col">Percentile</th><th scope="col">Date</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">MCAT</th><td>521 / 528</td><td>98th</td><td>Jan 2024</td></tr>
            <tr><th scope="row">ACT</th><td>35 / 36</td><td>99th</td><td>Jul 2018</td></tr>
            <tr><th scope="row">SAT</th><td>1550 / 1600</td><td>99th</td><td>Apr 2018</td></tr>
          </tbody>
        </table>
      </div>
    </section>

  </div>
</article>
