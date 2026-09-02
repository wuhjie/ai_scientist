#!/usr/bin/env python3
"""Compatibility entry point for the Pass 3 epistemic-loop TikZ figure.

The canonical source is build_review_figures.py.
"""

from build_review_figures import build_loop_tex


if __name__ == "__main__":
    build_loop_tex()
    print("wrote review/fig-loop.tex")
