#!/usr/bin/env python3
"""Compatibility entry point for the review-scale landscape SVG.

The canonical source is build_review_figures.py. Keeping this filename as a
thin delegate prevents older regeneration commands from restoring the retired
R0--R4 figure.
"""

from build_review_figures import build_landscape_svg


if __name__ == "__main__":
    build_landscape_svg()
    print("wrote assets/ai-scientist-landscape-review.svg")
