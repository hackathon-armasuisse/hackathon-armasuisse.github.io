# hackathon-armasuisse.github.io

Site for the Armasuisse Hackathon, built with [Jekyll](https://jekyllrb.com/) and the [Just the Docs](https://just-the-docs.com/) theme. Deployed automatically to GitHub Pages from the `main` branch via the workflow in `.github/workflows/pages.yml`.

## Local development

Requires Ruby 3.1+ and Bundler.

```bash
bundle install
bundle exec jekyll serve --livereload
```

The site will be available at <http://127.0.0.1:4000>.

## Content layout

```
index.md                              Welcome page
general-information.md                Infrastructure, scoring, attacks, out of scope
submitting-exploits.md                Exploit categories and submission form

tracks/
  track-1/
    index.md                          Track 1 parent (Documentation Assistant)
    introduction.md
    data.md
    application-criteria.md
    submitting-application.md
```

To add a new track, copy `tracks/track-1/` to `tracks/track-N/`, bump the `nav_order` in the new track's `index.md`, and update the `parent:` field in each child page to match the new title.

## Deployment

Pushing to `main` triggers the GitHub Actions workflow, which builds the site with Jekyll and publishes the result to GitHub Pages. Make sure **Settings &rarr; Pages &rarr; Build and deployment &rarr; Source** is set to `GitHub Actions` for the repository.
