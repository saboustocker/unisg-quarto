# UniSG Slides Template

Slides only, no website around them.

## Render

```bash
quarto render
quarto preview talk.qmd
```

Output goes to `_output/`.

## Structure

- `talk.qmd` — starter deck, copy it for each new talk
- `showcase.qmd` — every slide class the theme provides, with the text colour that works on each surface

## Slide classes

Set a background by adding a class to the heading:

```markdown
# Section {.section-header-bg .subtitle-section-header}

## Quote slide {.quote-slide-bg}

## Blue slide {.blue-slide-bg}
```

Surfaces: `.section-header-bg`, `.quote-slide-bg`, `.image-slide-bg`, `.green-slide-bg`, `.darkgreen-slide-bg`, `.blue-slide-bg`, `.red-slide-bg`, `.yellow-slide-bg`.

Paragraph colours: `.ink-p`, `.darkgreen-p`, `.green-p`, `.blue-p`, `.red-p`, `.yellow-p`, `.beige-p`, `.white-text-p`.

Blockquote colours: `.bq-green`, `.bq-darkgreen`, `.bq-blue`, `.bq-red`, `.bq-yellow`.

Tables take `.striped` or `.plain`.

The logo sits in the footer band of every slide and switches between the colour and white variant with the background, so `footer:` text is not rendered.

To export PDF handouts, add `?print-pdf` to the URL and print from the browser.
