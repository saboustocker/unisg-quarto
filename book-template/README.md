# UniSG Quarto Book Template

Quarto book using the UniSG book formats.

## Render

```bash
quarto render                       # all formats
quarto render --to unisg-book-html
quarto render --to unisg-book-pdf
quarto preview
```

Output goes to `_book/`.

## Structure

- `index.qmd` — preface, the first page of the book
- `chapters/` — one file per chapter, plus `appendix-data.qmd` as an appendix
- `references.bib`, `references.qmd` — bibliography, cited in APA style
- `slides/talk.qmd` — companion deck in the UniSG slide theme

## First steps

1. Set the title, author, chapter list and appendices in `_quarto.yml`.
2. Replace the placeholder author name in the page footer.
3. Add references to `references.bib`.

The PDF format needs a TeX installation; `quarto install tinytex` provides one.

`_extensions/` is committed on purpose, so the book keeps rendering the same way if the central theme changes later.
