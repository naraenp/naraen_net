# naraen_net

Personal portfolio website built with Jekyll.

## Motivation

This site is the public-facing layer for project communication:

- show research and engineering projects clearly,
- provide CV and contact links,
- make technical work legible to recruiters and collaborators.

## Structure

```text
naraen_net/
├── _layouts/
├── _includes/
├── _portfolio/
├── _posts/
├── assets/
├── portfolio.markdown
├── blog.markdown
├── cv.markdown
└── _config.yml
```

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Then open:

- `http://127.0.0.1:4000`

## Notes for maintainability

- Keep portfolio entries in `_portfolio/`.
- Keep reusable metadata in `_config.yml` or `_data/`.
- Add narrative structure to project pages:
  - problem,
  - approach,
  - result,
  - impact.
