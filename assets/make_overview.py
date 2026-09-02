#!/usr/bin/env python3
"""Compatibility entry point for the Pass 3 epistemic-loop SVG.

The canonical source is build_review_figures.py. Keeping this filename as a
thin delegate prevents older regeneration commands from restoring the retired
C0--C6 overview.
"""

from build_review_figures import build_loop_svg


if __name__ == "__main__":
    build_loop_svg()
    print("wrote assets/ai-scientist-overview.svg")
