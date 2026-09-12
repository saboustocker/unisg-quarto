# UniSG reveal.js slide styles

Reference for every class the `unisg-slides-revealjs` format provides, and how to apply it.

Classes go in braces after a heading for slide-level styles, or on a fenced div
for block-level styles:

```markdown
## Slide title {.green-slide-bg}

::: {.quote-p}
Text in the quote style.
:::
```

## Format defaults

Set in `_extension.yml`, override in your document's front matter.

| Key | Value | Effect |
| --- | --- | --- |
| `width` / `height` | 1600 × 900 | 16:9 deck, letterboxed with black bars when the window is a different shape |
| `margin` | 0 | slide surface reaches the edges of the 16:9 box; padding comes from CSS |
| `center` | false | slides start at the top, `#` heading slides are centred |
| `auto-stretch` | false | image sizing is handled by the extension, not Quarto |
| `slide-number` | true | centred in the footer band |
| `progress` | true | dark green bar |
| `transition` | fade | |
| `chalkboard` | true | |

## Slide backgrounds

Apply to a `##` heading. Each one also exists in a `-no-underline-bg` variant
that removes the rule under the title.

| Class | Surface | Text |
| --- | --- | --- |
| *(none)* | beige `#f2ecdf` | ink, green `h2` |
| `.image-slide-bg` | white with a beige band along the bottom | ink |
| `.green-slide-bg` | green `#00802f` | white |
| `.darkgreen-slide-bg` | dark green `#0a5f2d` | white |
| `.blue-slide-bg` | blue `#73a5af` | white |
| `.red-slide-bg` | coral `#eb6969` | white |
| `.yellow-slide-bg` | yellow `#fff04b` | ink |
| `.quote-slide-bg` | dark green with a beige band down the left | white |
| `.section-header-bg` + `.subtitle-section-header` | green-to-dark-green gradient | white |

No-underline variants: `.green-slide-no-underline-bg`,
`.darkgreen-slide-no-underline-bg`, `.blue-slide-no-underline-bg`,
`.red-slide-no-underline-bg`, `.yellow-slide-no-underline-bg`,
`.image-slide-no-underline-bg`.

```markdown
## Findings {.darkgreen-slide-bg}

## Findings {.darkgreen-slide-no-underline-bg}
```

A `#` heading always renders as a section-header slide on the gradient with a
white logo, whether or not you add the classes:

```markdown
# Part two {.section-header-bg .subtitle-section-header}

# Q&A
```

## Paragraph styles

Fenced divs. Colours are chosen for contrast on their intended surface.

| Class | Use |
| --- | --- |
| `.quote-p` | pull quote with a yellow rule, for `.quote-slide-bg` |
| `.source-p` | source line under a quote, oblique |
| `.source-p-blue` | right-aligned source line, oblique |
| `.subtitle-p` | right-aligned subtitle on dark surfaces |
| `.authors-p` | author line, small |
| `.callout-slide-p` | inset callout block for `.image-slide-bg` |
| `.question-slide-p` | large white text for a discussion prompt |
| `.smalltext-p` | 0.6em note |
| `.rightalign-p` | 0.8em, right aligned |
| `.smaller-p` | 0.8em |
| `.bib-p` | bibliography block, left aligned, 0.42em |
| `.bib-end-p` | bibliography block, right aligned |
| `.bib-quote-p` | right-aligned reference under a quote |

Colour-only paragraph classes, all 1em: `.white-text-p`, `.darkgreen-p`,
`.green-p`, `.blue-p`, `.red-p`, `.yellow-p`, `.beige-p`, `.ink-p`.

```markdown
## A quotation {.quote-slide-bg}

::: {.quote-p}
The quotation itself.
:::

::: {.source-p}
Author, 2026
:::
```

## Blockquotes

A blockquote picks up a green left rule by default. Wrap it to recolour:

| Class | Rule and tint |
| --- | --- |
| `.bq-green` | green |
| `.bq-darkgreen` | dark green |
| `.bq-blue` | blue |
| `.bq-red` | coral |
| `.bq-yellow` | yellow |

```markdown
::: {.bq-red}
> Not a revolution, but an evolution.
:::
```

## Tables

Plain markdown tables are styled with a dark green header row. Two variants:

| Class | Effect |
| --- | --- |
| `.striped` | white rows, alternate rows tinted green |
| `.plain` | transparent rows, dark green rules |

Wrap the table in a fenced div to apply one:

```markdown
::: {.striped}
| Cluster | Mentions |
| --- | ---: |
| Generative AI | 225 |
:::
```

Sizing is automatic — see *Automatic fitting* below. Tables are centred in
their column when they are narrower than it.

## Layout helpers

| Class | Effect |
| --- | --- |
| `.center-align` | centres text and images in the block |
| `.center-middle` | flex column, centred both axes, at least 60% of the slide height |
| `.image-center-stack` | grid cell 62vh tall with its contents centred |
| `.plotly-frame` | 420px tall frame for an embedded plotly iframe |

## Columns

Standard Quarto columns. Quote the widths.

```markdown
:::: {.columns}

::: {.column width="60%"}
Text on the left.
:::

::: {.column width="40%"}
![A figure](images/plot.png)
:::

::::
```

## Layered slides

Use reveal's `.r-stack` to overlay steps on one slide. Do not position fragments
with inline `position: absolute` — that takes them out of the slide's padding
box and out of the fitting logic.

```markdown
## Results {.image-slide-bg}

::: {.r-stack}

:::: {.fragment .fade-out}
![First view](images/one.png)
::::

:::: {.fragment .fade-in-then-out}
![Second view](images/two.png)
::::

:::

```

Each layer is measured and fitted independently.

## Automatic fitting

`assets/js/fit-images.html` runs on every slide change and window resize. For
each column, each `.r-stack` layer, and the slide as a whole, it finds the
largest scale at which that group's images and tables still fit inside the
slide's content box and their own column, and applies it.

- Images grow into empty space as well as shrink, keeping their aspect ratio.
- Tables scale with `zoom`, so the caption shrinks with the table and stays
  inside the slide. They are never enlarged beyond their natural size.
- Captions are never pushed past the bottom of the slide.
- Content that already fits is left untouched.

Nothing needs to be added to a slide for this to happen.

## Citations

Citations render in the muted colour at 0.6em, including the brackets and the
semicolons between multiple references. On green, dark green, blue and red
surfaces they switch to beige.

```markdown
Generative AI has a profound impact [@grewal2025; @cillo2025]
```

## Colour reference

| Name | Hex | Text that passes on it |
| --- | --- | --- |
| Beige surface | `#f2ecdf` | ink, dark green |
| Brand beige (bands) | `#e1d7c3` | ink, dark green |
| Green | `#00802f` | white |
| Dark green | `#0a5f2d` | white, beige |
| Blue | `#73a5af` | white |
| Coral | `#eb6969` | white |
| Yellow | `#fff04b` | ink |
| Ink | `#1f2933` | — |
