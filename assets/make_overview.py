#!/usr/bin/env python3
"""Overview figure: the discovery loop, and what may close it.

Four stages in a cycle -- a represented hypothesis is put to an experiment or
evaluation, which yields evidence, which is acted on by retaining, revising or
rejecting the hypothesis, which returns to the first stage. Alongside the
second stage, the six things that can play the role of "experiment or
evaluation", ordered by the strength of the evidence they produce.

No capability shading: this states the structure of the loop, not a verdict on
who implements which part.

516 x 202 pt -- IEEE `figure*`. Regenerate: python3 assets/make_overview.py
"""
from html import escape

W, H = 516, 202
INK, MID, LIGHT, RULE = "#0b0b0b", "#52514e", "#8a8880", "#d5d4cd"
PAPER, ACCENT = "#ffffff", "#2a78d6"

STAGES = ["Represented hypothesis", "Experiment / evaluation", "Evidence",
          "Retention · revision · rejection"]
MODES = [("C0", "no demonstrated closure"), ("C1", "self-critique"),
         ("C2", "multi-agent critique or selection"), ("C3", "executable evaluation"),
         ("C4", "statistical adjudication"), ("C5", "empirical feedback"),
         ("C6", "formal verification")]

out = []
def add(s): out.append(s)
def txt(x, y, s, size=7.2, fill=INK, weight=400, anchor="middle", style=""):
    st = f' font-style="{style}"' if style else ""
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
        f'text-anchor="{anchor}"{st}>{escape(s)}</text>')

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'role="img" aria-labelledby="t d" font-family="Helvetica, Arial, sans-serif">')
add('<title id="t">The discovery loop and what may close it</title>')
add('<desc id="d">A cycle of four stages: represented hypothesis, experiment or evaluation, '
    'evidence, and retention, revision or rejection, returning to the hypothesis. Six kinds of '
    'experiment or evaluation are listed beside the second stage, coded as non-ordinal.</desc>')
add(f'<defs>'
    f'<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" '
    f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{MID}"/></marker>'
    f'<marker id="ab" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" '
    f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{ACCENT}"/></marker>'
    f'<marker id="af" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" '
    f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{LIGHT}"/></marker>'
    f'</defs>')
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

BX, BW, BH, GAP = 74, 186, 28, 16
ys = [12 + i * (BH + GAP) for i in range(4)]
for i, (s, y) in enumerate(zip(STAGES, ys)):
    add(f'<rect x="{BX}" y="{y}" width="{BW}" height="{BH}" rx="3" fill="{PAPER}" '
        f'stroke="{INK}" stroke-width="0.8"/>')
    txt(BX + BW / 2, y + BH / 2 + 2.6, s, 7.8, INK, 600)
    if i < 3:
        add(f'<path d="M{BX+BW/2} {y+BH} L{BX+BW/2} {y+BH+GAP-3}" stroke="{MID}" '
            f'stroke-width="1" marker-end="url(#a)"/>')

# the return edge: what makes it a loop
rx = BX - 30
add(f'<path d="M{BX} {ys[3]+BH/2} L{rx} {ys[3]+BH/2} L{rx} {ys[0]+BH/2} L{BX-3} {ys[0]+BH/2}" '
    f'fill="none" stroke="{ACCENT}" stroke-width="1.1" marker-end="url(#ab)"/>')
txt(rx, ys[0] + BH / 2 - 10, "↺", 11, ACCENT, 400, "middle")
add(f'<text x="{rx-7:.1f}" y="{(ys[0]+ys[3])/2+BH/2:.1f}" font-size="6.2" fill="{ACCENT}" '
    f'text-anchor="middle" transform="rotate(-90 {rx-7:.1f} {(ys[0]+ys[3])/2+BH/2:.1f})">'
    f'the loop closes here</text>')

# what can play the role of "experiment / evaluation"
PX, PY = 306, 8
PW, PH = 196, 150
add(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="4" fill="{PAPER}" '
    f'stroke="{RULE}" stroke-width="0.8"/>')
txt(PX + 10, PY + 15, "what may close the loop", 6.8, MID, 700, "start")
add(f'<line x1="{PX+10}" y1="{PY+20}" x2="{PX+PW-10}" y2="{PY+20}" stroke="{RULE}" stroke-width="0.5"/>')
for i, (rung, name) in enumerate(MODES):
    y = PY + 32 + i * 16.5
    txt(PX + 16, y, rung, 6.6, LIGHT, 700, "start")
    txt(PX + 36, y, name, 7.6, INK, 400, "start")

# connector from the second stage into the panel
add(f'<path d="M{BX+BW} {ys[1]+BH/2} L{PX-3} {ys[1]+BH/2}" stroke="{RULE}" stroke-width="0.8" '
    f'stroke-dasharray="2.5 2" marker-end="url(#af)"/>')


txt(BX + BW / 2, H - 8, "A hypothesis that is not represented cannot be revised on evidence.",
    7.0, MID, 400, "middle", "italic")
add('</svg>')

open("assets/ai-scientist-overview.svg", "w").write("\n".join(out))
print(f"wrote assets/ai-scientist-overview.svg  ({W} x {H} pt)")
