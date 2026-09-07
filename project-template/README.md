# UniSG Quarto Project Template

Quarto website holding the slides, manuscripts, analysis reports and code for one project.

## Render

```bash
quarto render
quarto preview
```

Output goes to `_site/`.

## Structure

- `index.qmd` — project overview page
- `slides/` — `index.qmd` lists the decks, `intro.qmd` is a starter deck, `showcase.qmd` shows every slide class
- `manuscript/` — `index.qmd` lists the manuscripts, `working-paper.qmd` renders to HTML, PDF and DOCX
- `reports/` — `index.qmd` lists the analysis reports, `analysis-report.qmd` is the example
- `data/raw/`, `data/processed/` — data, ignored by git apart from the README files
- `outputs/` — generated figures, tables and models
- `assets/logos/` — logos used by the navbar and social preview
- `_includes/` — reusable text fragments, included at the end of the working paper

The `ggplot2` and `matplotlib` theme helpers ship with the extension, in
`_extensions/unisg/plotting/`.

## First steps

1. Set the title, navbar and footer in `_quarto.yml`.
2. Replace the placeholder author names.
3. Delete the example decks, manuscripts and reports you do not need.

`_extensions/unisg/` is committed on purpose, so the project keeps rendering the same way if the central theme changes later.
