"""
Core plotting logic for india_hexmap.
"""

import math
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize, ListedColormap

from .positions import POSITIONS, NAMES


def plot_hexmap(
    data=None,
    cmap="YlGnBu",
    no_data_color="#dddddd",
    label_color="white",
    label_size=8,
    edge_color="white",
    edge_width=2,
    show_colorbar=True,
    colorbar_label="Value",
    title=None,
    categorical=False,
    ax=None,
    figsize=(10, 8),
):
    """
    Draw the India hex map.

    Parameters
    ----------
    data : dict, optional
        Mapping of state/UT code -> value (e.g. {"KL": 96.2, "MH": 84.8}).
        States left out are drawn with `no_data_color`. If None, every
        hexagon is drawn with `no_data_color` (useful as a blank base map).
    cmap : str or Colormap
        Any matplotlib colormap name, used for continuous numeric data.
        Ignored if `categorical=True` and `data` values are strings.
    categorical : bool
        Set True if `data` values are category labels (strings) rather
        than numbers. Colors are then assigned per unique category and a
        legend is drawn instead of a colorbar.
    ax : matplotlib.axes.Axes, optional
        Draw onto an existing axes instead of creating a new figure.
    figsize : tuple
        Figure size, only used when `ax` is None.

    Returns
    -------
    fig, ax : the matplotlib Figure and Axes used.
    """
    data = data or {}

    # Pointy-top hexagon geometry: with column spacing DX = 1, hexagons
    # share full edges (no gaps, no overlap) when radius R = DX / sqrt(3)
    # and row spacing = 1.5 * R.
    DX = 1.0
    radius = DX / math.sqrt(3)
    dy = 1.5 * radius

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    if categorical:
        categories = sorted({v for v in data.values() if v is not None})
        palette = plt.get_cmap(cmap if isinstance(cmap, str) else "tab10")
        color_map = {
            cat: palette(i / max(len(categories) - 1, 1))
            for i, cat in enumerate(categories)
        }
        color_of = lambda val: color_map[val] if val is not None else no_data_color
    else:
        numeric_vals = [v for v in data.values() if v is not None]
        if numeric_vals:
            norm = Normalize(vmin=min(numeric_vals), vmax=max(numeric_vals))
        else:
            norm = Normalize(vmin=0, vmax=1)
        palette = plt.get_cmap(cmap)
        color_of = lambda val: palette(norm(val)) if val is not None else no_data_color

    max_row = 0
    for code, (col, row) in POSITIONS.items():
        x = col * DX
        y = -row * dy
        max_row = max(max_row, row)
        val = data.get(code)
        color = color_of(val)

        hexagon = RegularPolygon(
            (x, y),
            numVertices=6,
            radius=radius,
            orientation=0,  # pointy-top
            facecolor=color,
            edgecolor=edge_color,
            linewidth=edge_width,
        )
        ax.add_patch(hexagon)
        ax.text(x, y, code, ha="center", va="center",
                 color=label_color, fontsize=label_size, fontweight="bold")

    xs = [c for c, r in POSITIONS.values()]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(-max_row * dy - 1, dy + 0.5)
    ax.set_aspect("equal")
    ax.axis("off")

    if title:
        ax.set_title(title, fontsize=14, fontweight="bold", pad=20)

    if show_colorbar and not categorical and numeric_vals:
        sm = ScalarMappable(cmap=palette, norm=norm)
        sm.set_array([])
        cbar = fig.colorbar(sm, ax=ax, shrink=0.5, pad=0.02)
        cbar.set_label(colorbar_label)
    elif show_colorbar and categorical and categories:
        handles = [
            plt.Line2D([0], [0], marker="h", color="w", markerfacecolor=color_map[cat],
                        markersize=15, label=str(cat))
            for cat in categories
        ]
        ax.legend(handles=handles, loc="center left", bbox_to_anchor=(1.02, 0.5),
                  frameon=False, title=colorbar_label)

    fig.tight_layout()
    return fig, ax
