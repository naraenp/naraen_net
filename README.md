# naraen_net

Personal portfolio site at [naraen.net](https://naraen.net). Built with Jekyll 4
and published via GitHub Pages from `main`.

## Site structure

- **Home** (`/`): Hero, About, Selected projects, and Experience sections.
  Sticky glass nav with a light/dark theme toggle.
- **Portfolio** (`/portfolio/`): Auto-generated grid of project pages collected
  from `_portfolio/` (front matter: `title`, `description`, `thumbnail`).
- **Log** (`/log/`): The blog. Posts live in `_posts/` and use the
  `/log/:title/` permalink. The index (`log.markdown`) filters posts
  client-side by a fixed tag vocabulary (`log_tags` in `_config.yml`).
- **CV** (`/cv/`): Full CV with a downloadable résumé PDF
  (`assets/pdf/naraenp_resume.pdf`).
- **Gallery** (`/gallery/`): Lightbox photo grid driven by
  `assets/gallery/captions.json`.
- **Reading** (`/reading/`): Bookshelf driven by `_data/reading.yml`; the same
  data feeds a "Currently reading" strip on `/log/` and the home hero.
- **Search** (`/search/`): Client-side site search (Pagefind).
- **Contact** (`/contact/`): Formspree-backed contact form; the recipient
  email is not stored in the repo.

## Repo layout

```text
├── _config.yml          # Site config, formspree_form_id, plugin list
├── _data/               # reading.yml (bookshelf data)
├── _includes/           # header, head, footer, contact_form, theme_toggle
├── _layouts/            # default, home, page, post
├── _portfolio/          # One .md per portfolio project (collection)
├── _posts/              # Log entries (the blog)
├── _sass/               # Vendored minima + Aequorea design tokens
├── assets/              # main.scss, images/, icons/, fonts/, pdf/, gallery/, embeds/
├── bin/                 # Authoring/publish helpers (new-post.sh, publish.sh)
├── index.markdown       # layout: home
├── portfolio.markdown   # Portfolio grid index
├── log.markdown         # Log index (client-side tag filter)
├── cv.markdown          # CV page
├── gallery.markdown     # Photo gallery (lightbox)
├── reading.markdown     # Reading bookshelf
├── search.markdown      # Site search (Pagefind)
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

The site follows the **Aequorea** identity (personal, named for the GFP
jellyfish *Aequorea victoria*), scoped to naraen.net:

- A deep marine-ink "Abyssal" neutral ramp (tokens: `--aq-abyss` through
  `--aq-sail`) lit by a single bioluminescent aquamarine accent
  (`--aq-glow`) that lives outside the ramp.
- Three fonts (Zodiak serif, Switzer sans, JetBrains Mono monospace),
  self-hosted under `assets/fonts/` with their licenses alongside.
- 6px border radius; 1px borders; sentence-case headings; and a "glow,
  don't move" hover (an accent box-shadow bloom) instead of translate/scale.

Component CSS lives in `assets/main.scss`; tokens are declared at the top of
that file and surfaced as Sass defaults in `_sass/minima.scss`.

## Conventions worth preserving

A few deliberate decisions that are easy to undo by accident:

- **No theme gem.** minima's layouts, includes, and styles are vendored in-repo
  (`_layouts/`, `_includes/`, `_sass/minima.scss` + `_sass/minima/`), and
  `theme: minima` / `gem "minima"` are intentionally omitted. This keeps local
  builds matching production and stops Jekyll auto-loading minima's
  `jekyll-feed` dependency. Don't reintroduce the theme gem.
- **No RSS/Atom feed.** `jekyll-feed` is intentionally not in the plugin list
  (see `_config.yml`). The site is **content-only**: no comments, no
  third-party interaction widgets, no feed. The Formspree contact form is the
  single interaction channel.
- **Nav is hardcoded** in `_includes/header.html`, not generated from
  `header_pages`. Add new top-level pages to both.
- **Design system is fixed.** The Aequorea tokens, fonts, and identity rules
  above are intentional; treat them as the contract for any new UI.

## Config notes

- **Contact form:** Set `formspree_form_id` in `_config.yml` (form ID from
  [Formspree](https://formspree.io)). The recipient email lives only in the
  Formspree dashboard.
- **Résumé:** Place the PDF at `assets/pdf/naraenp_resume.pdf`. The CV page
  links to it via the download button in `cv.markdown`.
