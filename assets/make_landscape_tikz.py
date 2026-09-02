#!/usr/bin/env python3
"""Compatibility entry point for the review landscape TikZ figure.

The canonical source is build_review_figures.py.
"""

from build_review_figures import build_landscape_tex


if __name__ == "__main__":
    build_landscape_tex()
    print("wrote review/fig-landscape.tex")
