# New academic homepage

The new homepage is independent of Jekyll. The Actions workflow publishes `dist/`. A generated root `index.html` and `.nojekyll` also support the default branch-based Pages publisher.

## Local preview

```sh
python3 scripts/build_homepage.py
python3 -m http.server 4173 --directory dist
```

Open http://localhost:4173.

## Editing

- `homepage.html`: biography, contact links, projects, education.
- `homepage.css`: responsive visual design.
- `homepage.js`: publication category filters.
- `homepage-publications.json`: publication content and categories.
- `scripts/build_homepage.py`: award metadata and build logic, no external dependencies.
- `index.html`: generated homepage; run the builder after editing source files and include the updated index in your commit. Do not edit this generated file directly.

## GitHub Pages

Create a public repository named wenkeyuan.github.io on the WenkeYuan account. Push this checkout to the new repository. In Settings → Pages, set Source to GitHub Actions. The Deploy academic homepage workflow builds and publishes the site.

Before publishing, confirm publication status, award descriptions, and the exact completion dates if they should be displayed. Academic status and the GitHub profile have been updated from the owner’s confirmation. No sample PDFs or fabricated CV links are published.

The builder only copies your portrait and five award images. Existing local changes are preserved; old theme files can be removed separately after reviewing them.

Target homepage: https://wenkeyuan.github.io/

This standalone checkout uses the new repository: https://github.com/WenkeYuan/wenkeyuan.github.io.git
