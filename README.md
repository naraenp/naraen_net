# naraen_net

Personal portfolio site at [naraen.net](https://naraen.net). Built with Jekyll 4
and published via GitHub Pages from `main`.

## Site structure

- **Home** (`/`): Hero, About, Selected projects, and Experience sections.
  Sticky glass nav with a light/dark theme toggle.
- **CV** (`/cv/`): Full CV with a downloadable résumé PDF
  (`assets/pdf/naraenp_resume.pdf`).
- **Portfolio** (`/portfolio/`): Auto-generated grid of project pages collected
  from `_portfolio/` (front matter: `title`, `description`, `thumbnail`).
- **Contact** (`/contact/`): Formspree-backed contact form; the recipient
  email is not stored in the repo.

The blog is intentionally disabled (`_posts` is in `exclude:` in
`_config.yml`).

## Repo layout

```text
├── _config.yml          # Site config, formspree_form_id, plugin list
├── _includes/           # header, head, footer, contact_form, theme_toggle
├── _layouts/            # default, home, page, post
├── _portfolio/          # One .md per portfolio project (collection)
├── _sass/               # Minima overrides + PA design tokens
├── assets/              # main.scss, images/, icons/, fonts/, pdf/
├── index.markdown       # layout: home
├── portfolio.markdown   # Portfolio grid index
├── cv.markdown          # CV page
├── contact.markdown     # Contact page
├── 404.html             # Custom 404
├── CNAME                # Custom domain (naraen.net)
└── robots.txt
```

## Develop locally

```bash
bundle install
bundle exec jekyll serve   # http://127.0.0.1:4000
bundle exec jekyll build   # outputs to _site/
```

## Adding a portfolio project

Drop a new file in `_portfolio/<slug>.md` with the front matter below. No
config change is needed.

```yaml
---
layout: page
title: "Project title"
description: "One-sentence summary used on the portfolio card."
thumbnail: "/assets/images/portfolio/<slug>.svg"
---
```

Body content can include arbitrary HTML or embeds (the portfolio uses iframes
for some live demos). Thumbnails are scaled to a 180px-tall card via
`object-fit: cover`; SVGs in the existing PA visual grammar live in
`assets/images/portfolio/`.

## Design system

The site follows the Phalaena Automata identity, scoped to naraen.net:

- One mauve color ramp (tokens: `--pa-onyx` through `--pa-snow`).
- Three fonts (Sentient serif, Plein sans, Fragment Mono monospace),
  self-hosted under `assets/fonts/`.
- Zero border radius except the avatar and spinner; no box shadows; 1px
  borders; sentence-case headings.

Component CSS lives in `assets/main.scss`; tokens are declared at the top of
that file and surfaced as Sass defaults in `_sass/minima.scss`.

## Config notes

- **Contact form:** Set `formspree_form_id` in `_config.yml` (form ID from
  [Formspree](https://formspree.io)). The recipient email lives only in the
  Formspree dashboard.
- **Résumé:** Place the PDF at `assets/pdf/naraenp_resume.pdf`. The CV page
  links to it via the download button in `cv.markdown`.
