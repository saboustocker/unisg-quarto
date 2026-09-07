"""UniSG plotting helpers for matplotlib."""

UNISG_COLORS = {
    "green": "#00802f",
    "dark_green": "#0a5f2d",
    "beige": "#e1d7c3",
    "blue": "#73a5af",
    "coral": "#eb6969",
    "yellow": "#fff04b",
    "ink": "#1f2933",
}

UNISG_PALETTE = [
    UNISG_COLORS["green"],
    UNISG_COLORS["blue"],
    UNISG_COLORS["coral"],
    UNISG_COLORS["dark_green"],
    UNISG_COLORS["yellow"],
]


def apply_unisg_matplotlib():
    """Apply a lightweight UniSG style to matplotlib."""
    import matplotlib.pyplot as plt
    from cycler import cycler

    plt.rcParams["axes.prop_cycle"] = cycler(color=UNISG_PALETTE)
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.labelcolor"] = UNISG_COLORS["dark_green"]
    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["savefig.facecolor"] = "white"
