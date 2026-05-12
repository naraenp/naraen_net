# naraen_net

Personal portfolio site (Jekyll, GitHub Pages): single-page landing plus CV and portfolio.

## Site structure

- **Home** (`/`) — Hero, About, Projects, Experience. Sticky glass nav; light/dark theme toggle.
- **CV** (`/cv/`) — Full CV and PDF download. Resume file: `assets/pdf/naraenp_resume.pdf`.
- **Portfolio** (`/portfolio/`) — Collection of project pages from `_portfolio/` (front matter: `title`, `description`, `thumbnail`, etc.).

## Repo structure

```text
├── _config.yml       # Site title, url, formspree_form_id, plugins, exclude (_posts)
├── _includes/       # header, head, contact_form, theme_toggle
├── _layouts/        # default, home, page, post
├── _portfolio/      # One .md per project (collection)
├── assets/          # main.scss, images/, icons/, pdf/
├── index.markdown   # layout: home
├── portfolio.markdown
├── cv.markdown
└── CNAME            # Custom domain (e.g. naraen.net)
```

Blog is off: `_posts` is excluded; no blog page.

## Config notes

- **Contact:** Set `formspree_form_id` in `_config.yml` (form ID from [Formspree](https://formspree.io)); your email is only in their dashboard.
- **Resume:** Put the PDF at `assets/pdf/naraenp_resume.pdf`.
