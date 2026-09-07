# UniSG Quarto

Quarto extension with University of St.Gallen formats for websites, slides, manuscripts and books, plus three starter projects.

## Install

```bash
quarto add saboustocker/unisg-quarto
```

Or from a local clone, if you want to make your own edits:

```bash
quarto add /path/to/unisg-quarto
```

## Formats

| Format | Use |
|--------|-----|
| `unisg-html` | website pages and reports |
| `unisg-revealjs` | slides |
| `unisg-pdf` | PDF manuscripts |
| `unisg-docx` | Word manuscripts, APA reference doc |
| `unisg-book-html` | books, HTML |
| `unisg-book-pdf` | books, PDF |

```yaml
format:
  unisg-revealjs: default
```

Book formats need `project: type: book`.

## Starter projects

Copy the folder you need into a new repository and edit `_quarto.yml`. Each one already contains `_extensions/`, so it renders without installing anything.

| Folder | Project type |
|--------|--------------|
| `project-template/` | Quarto website with slides, manuscripts, analysis reports and code |
| `book-template/` | Quarto book |
| `slides-template/` | slides only |

`project-template/slides/showcase.qmd` and `slides-template/showcase.qmd` render every slide class the theme provides. Start there when writing a deck.

## Included in extension

- Official UniSG logo variants in colour, black and white
- SCSS for pages, slides, manuscripts and books
- APA CSL and an APA-style Word reference document
- `ggplot2` and `matplotlib` theme helpers in `_extensions/unisg/plotting/`

## Repository layout

```
_extensions/          the extension, this is what `quarto add` installs
project-template/     website starter
book-template/        book starter
slides-template/      slides starter
```

Each starter carries its own copy of `_extensions/`, because Quarto only looks for extensions inside the project directory. After changing the extension, run:

```bash
python scripts/sync-extensions.py
```
