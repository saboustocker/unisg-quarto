# UniSG Quarto

Quarto extension with University of St.Gallen formats for websites, slides, manuscripts and books, plus three starter projects.

## Install

```bash
quarto add YOUR_GITHUB_USER/unisg-quarto
```

Or from a local clone:

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

## What the extension ships

- Official UniSG logo variants in colour, black and white
- SCSS for pages, slides, manuscripts and books
- APA CSL and an APA-style Word reference document
- `ggplot2` and `matplotlib` theme helpers in `_extensions/unisg/plotting/`

## Slides

Backgrounds are set as classes on a heading:

```markdown
# Section {.section-header-bg .subtitle-section-header}

## Quote slide {.quote-slide-bg}

## Blue slide {.blue-slide-bg}
```

Available surfaces: `.section-header-bg`, `.quote-slide-bg`, `.image-slide-bg`, `.green-slide-bg`, `.darkgreen-slide-bg`, `.blue-slide-bg`, `.red-slide-bg`, `.yellow-slide-bg`.

Text, blockquote and table classes are listed in the showcase deck.

The UniSG logo is drawn in the footer band of every slide and switches between the colour and white variant with the background. Footer text is not rendered, since the logo occupies that band.

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
