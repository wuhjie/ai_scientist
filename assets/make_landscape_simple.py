#!/usr/bin/env python3
"""Simple companion to make_landscape.py: the same systems and the same
groupings, without the interpretive layer.

Dropped: the autonomy / executor / evidence line on every card, all relation
arrows and their labels, the reference markers and footnotes, and the
"reading a card" legend. What remains is a plain map of the field -- who is
in it, and how it divides.

Data is read out of make_landscape.py by AST, so the two figures cannot drift
apart. Regenerate: python3 assets/make_landscape_simple.py
"""
import ast
from html import escape

src = ast.parse(open("assets/make_landscape.py").read())
DATA = {}
for node in src.body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
        name = node.targets[0].id
        if name.isupper():
            try: DATA[name] = ast.literal_eval(node.value)
            except Exception: pass

W, PANEL_W, CARD_H, CARD_GAP, PAD = 1400, 315, 36, 7, 12
COL_X = [40, 375, 710, 1045]
INK, MID, LIGHT, RULE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
PAPER, FILL = "#fcfcfb", "#f4f3ef"

out = []
def add(s): out.append(s)
def txt(x, y, s, size=11, fill=INK, weight=400, anchor="start", style=""):
    st = f' font-style="{style}"' if style else ""
    add(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
        f'text-anchor="{anchor}"{st}>{escape(s)}</text>')

def card(x, y, e, dashed=False):
    dash = ' stroke-dasharray="4 3"' if dashed else ""
    add(f'<rect x="{x}" y="{y}" width="{PANEL_W}" height="{CARD_H}" rx="6" '
        f'fill="{PAPER if not dashed else "none"}" stroke="{RULE}" stroke-width="1"{dash}/>')
    txt(x + 11, y + 16, e[0], 11.5, INK, 600)
    txt(x + 11, y + 29, e[1], 9.5, LIGHT)

def panel(x, y, title, entries, dashed=False):
    h = PAD + 30 + len(entries) * CARD_H + (len(entries) - 1) * CARD_GAP + PAD
    add(f'<rect x="{x}" y="{y}" width="{PANEL_W}" height="{h}" rx="8" fill="{FILL}"/>')
    txt(x + 12, y + 22, title, 10.5, MID, 700)
    txt(x + PANEL_W - 12, y + 22, str(len(entries)), 10.5, LIGHT, 600, "end")
    add(f'<line x1="{x+12}" y1="{y+29}" x2="{x+PANEL_W-12}" y2="{y+29}" stroke="{RULE}" stroke-width="1"/>')
    cy = y + PAD + 30
    for e in entries:
        card(x, cy, e, dashed=dashed); cy += CARD_H + CARD_GAP
    return h

SYSTEMS = (DATA["GENERAL"] + DATA["BIOLOGY"] + DATA["LABS"] + DATA["PROGRAM"]
           + DATA["MLENG"] + DATA["CHEM"] + DATA["LIT"])

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{{H}}" viewBox="0 0 {W} {{H}}" '
    f'role="img" aria-labelledby="t d" '
    f'font-family=\'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif\'>')
add('<title id="t">Landscape of AI-enabled scientific-discovery systems</title>')
add('<desc id="d">Systems grouped by application area, with venues. Panels are categories, '
    'not lineages.</desc>')
add(f'<rect width="{W}" height="{{H}}" fill="{PAPER}"/>')

txt(40, 46, "Landscape of AI-enabled scientific-discovery systems", 22, INK, 700)
txt(40, 68, "Grouped by application area. Panels are categories, not lineages \u2014 position and "
            "adjacency carry no claim of descent. Venues as verified 29 July 2026.", 11.5, MID)

# classical band
yA = 92
BAND = PAD + 30 + 2 * CARD_H + CARD_GAP + PAD
add(f'<rect x="24" y="{yA}" width="{W-48}" height="{BAND+8}" rx="10" fill="{FILL}"/>')
txt(40, yA + 24, "CLASSICAL DISCOVERY PROGRAMMES (PRE-LLM)", 10.5, MID, 700)
txt(W - 40, yA + 24, "4 systems \u00b7 2 publications", 10.5, LIGHT, 600, "end")
add(f'<line x1="40" y1="{yA+32}" x2="{W-40}" y2="{yA+32}" stroke="{RULE}" stroke-width="1"/>')
y1 = yA + 46
for i, c in enumerate(DATA["CLASSICAL"]): card(COL_X[i], y1, c)
card(COL_X[3], y1, DATA["ADAM"])
y2 = y1 + CARD_H + CARD_GAP
card(COL_X[0], y2, DATA["BOOK"], dashed=True)
card(COL_X[1], y2, DATA["AUTOM"], dashed=True)
txt(COL_X[2], y2 + 23, "Publications, held separate from systems.", 9, LIGHT, 400, "start", "italic")

yBreak = yA + BAND + 34
add(f'<line x1="40" y1="{yBreak}" x2="{W-40}" y2="{yBreak}" stroke="#c3c2b7" stroke-width="1" stroke-dasharray="4 5"/>')
add(f'<rect x="{W//2-230}" y="{yBreak-8}" width="460" height="16" fill="{PAPER}"/>')
txt(W // 2, yBreak + 4, "\u2500  contemporary systems \u00b7 LLM agents, program search & autonomous labs  \u2500",
    10, LIGHT, 600, "middle")

yB = yBreak + 26
COLUMNS = [
    [("GENERAL / CROSS-DOMAIN RESEARCH AGENTS", DATA["GENERAL"], False),
     ("LITERATURE & EVIDENCE SYNTHESIS", DATA["LIT"], False)],
    [("CHEMISTRY / MATERIALS AGENTS", DATA["CHEM"], False),
     ("ML ENGINEERING SELF-RESEARCH", DATA["MLENG"], False)],
    [("BIOLOGY / LIFE SCIENCES", DATA["BIOLOGY"], False),
     ("SELF-DRIVING LABS", DATA["LABS"], False)],
    [("PROGRAM & EQUATION DISCOVERY", DATA["PROGRAM"], False),
     ("NON-SYSTEM ENTRIES", DATA["NONSYS"], True)],
]
bottoms = []
for ci, stack in enumerate(COLUMNS):
    cy = yB
    for (t, e, dashed) in stack:
        cy += panel(COL_X[ci], cy, t, e, dashed=dashed) + 22
    bottoms.append(cy - 22)

yF = max(bottoms) + 30
txt(40, yF, f"{len(SYSTEMS)} contemporary systems \u00b7 4 classical systems \u00b7 "
            f"{len(DATA['NONSYS'])} non-system entries \u00b7 2 foundational publications.", 9.6, MID)
add('</svg>')

H = yF + 24
open("assets/ai-scientist-landscape-simple.svg", "w").write("\n".join(out).replace("{H}", str(H)))
print(f"wrote assets/ai-scientist-landscape-simple.svg  ({W} x {H})  systems={len(SYSTEMS)}")
