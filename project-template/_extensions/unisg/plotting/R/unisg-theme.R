# UniSG plotting helpers for ggplot2

unisg_palette <- c(
  green = "#00802f",
  dark_green = "#0a5f2d",
  beige = "#e1d7c3",
  blue = "#73a5af",
  coral = "#eb6969",
  yellow = "#fff04b",
  ink = "#1f2933"
)

scale_color_unisg <- function(...) {
  ggplot2::scale_color_manual(values = unname(unisg_palette[c("green", "blue", "coral", "dark_green", "yellow")]), ...)
}

scale_fill_unisg <- function(...) {
  ggplot2::scale_fill_manual(values = unname(unisg_palette[c("green", "blue", "coral", "dark_green", "yellow")]), ...)
}

theme_unisg <- function(base_size = 12, base_family = "Arial") {
  ggplot2::theme_minimal(base_size = base_size, base_family = base_family) +
    ggplot2::theme(
      plot.title = ggplot2::element_text(face = "bold", color = unisg_palette[["dark_green"]]),
      plot.subtitle = ggplot2::element_text(color = unisg_palette[["ink"]]),
      axis.title = ggplot2::element_text(color = unisg_palette[["dark_green"]]),
      panel.grid.minor = ggplot2::element_blank(),
      legend.title = ggplot2::element_text(face = "bold"),
      plot.caption = ggplot2::element_text(color = unisg_palette[["dark_green"]])
    )
}
