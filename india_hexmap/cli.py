"""
Command-line interface: india-hexmap data.csv --out map.png
CSV must have columns: code,value  (e.g. KL,96.2)
"""

import argparse
import csv
import matplotlib.pyplot as plt

from .plot import plot_hexmap


def main():
    parser = argparse.ArgumentParser(description="Render the India hex map from a CSV of values.")
    parser.add_argument("csv_path", help="CSV file with columns: code,value")
    parser.add_argument("--out", default="india_hexmap.png", help="Output image path")
    parser.add_argument("--cmap", default="YlGnBu", help="Matplotlib colormap name")
    parser.add_argument("--title", default=None, help="Map title")
    parser.add_argument("--categorical", action="store_true", help="Treat values as categories, not numbers")
    args = parser.parse_args()

    data = {}
    with open(args.csv_path, newline="") as f:
        for row in csv.DictReader(f):
            code = row["code"].strip().upper()
            raw = row["value"].strip()
            data[code] = raw if args.categorical else float(raw)

    fig, ax = plot_hexmap(data, cmap=args.cmap, title=args.title, categorical=args.categorical)
    fig.savefig(args.out, dpi=200, bbox_inches="tight")
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()
