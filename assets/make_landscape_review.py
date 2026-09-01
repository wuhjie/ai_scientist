#!/usr/bin/env python3
"""Review-scale companion to make_landscape.py.

The repo figure is 1400x1474 and carries 35 entries at card size; at IEEE
double-column width (516pt) it is unreadable. This emits a condensed version
sized for a `figure*`: 516 x ~250pt, one line per system, organised on the
review's own axis (hypothesis representation) rather than by domain.

Data is read from README section 3 at build time, so the figure cannot drift
from the census. Regenerate: python3 assets/make_landscape_review.py
"""
import collections, re
from html import escape

W = 516
INK, MID, LIGHT, RULE = "#0b0b0b", "#52514e", "#898781", "#d8d7d0"
PAPER, ACCENT, WARN = "#ffffff", "#2a78d6", "#9e3129"

# ---- data, read from the census -------------------------------------------
sec = re.search(r'^## 3\. Systems at a glance(.*?)^## 4\.',
                open("README.md").read(), re.S | re.M).group(1)
lines = [l for l in sec.splitlines() if l.startswith('| ') and '---' not in l]
hdr = [c.strip() for c in lines[0].strip('|').split('|')]
D = []
for l in lines[1:]:
    c = [re.sub(r'\*\*|\[|\]\(.*?\)', '', x.strip()) for x in l.strip('|').split('|')]
    if len(c) != len(hdr): continue
    if c[0].startswith(('Checked by', 'An unconnected', 'Collaborating', 'The authors', 'Not stated')):
        continue
    D.append(dict(zip(hdr, c)))

def rep(v):
    v = v.lower()
    if 'logical' in v: return 'R4'
    if 'structured state' in v or 'state machine' in v or 'knowledge graph' in v: return 'R3'
    if 'program' in v: return 'R2'
    if 'retrieval' in v or v.startswith('n/a'): return 'R0'
    return 'R1'

def val(v):
    v = v.lower()
    if 'in vitro' in v or 'physical' in v: return 2      # physical / in vitro
    if 'benchmark' in v or 'held-out' in v or 'leaderboard' in v: return 1
    return 0                                              # none, partial or not reported

def who(v):
    v = v.lower()
    if 'third party' in v: return 'T'
    if 'external leaderboard' in v: return 'L'
    if 'collaborating' in v: return 'C'
    if v.strip() in ('—', '-', ''): return '?'
    return 'A'

ADAM = [d for d in D if 'Adam' in d['System']][0]
LLM = [d for d in D if 'Adam' not in d['System']]

RUNGS = [("R4", "logical, with entailment"),
         ("R3", "typed world model"),
         ("R2", "program-as-hypothesis"),
         ("R1", "natural language"),
         ("R0", "implicit")]
by = collections.defaultdict(list)
for d in LLM:
    by[rep(d['Hypothesis repr.'])].append(d)

out = []
def add(s): out.append(s)
def txt(x, y, s, size=6.4, fill=INK, weight=400, anchor="start", style=""):
    st = f' font-style="{style}"' if style else ""
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{st}>{escape(s)}</text>')

# ---- layout ---------------------------------------------------------------
LEFT, COLW, ROWH = 8, 109, 10.4
COLS_X = [LEFT + 62 + i * COLW for i in range(4)]
y = 16
body = []
for code, gloss in RUNGS:
    items = sorted(by.get(code, []), key=lambda d: d['System'])
    nrow = max(1, -(-len(items) // 4))
    body.append((code, gloss, items, y, nrow))
    y += max(ROWH * nrow, 12) + 7
H = y + 46

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" '
    f'viewBox="0 0 {W} {H:.0f}" role="img" aria-labelledby="t d" '
    f'font-family="Helvetica, Arial, sans-serif">')
add('<title id="t">AI Scientist systems by hypothesis representation, validation and checking party</title>')
add('<desc id="d">Twenty-six LLM-era systems grouped by hypothesis representation rung. Each '
    'carries a validation mark and a letter naming the party that performed the check.</desc>')
add(f'<rect width="{W}" height="{H:.0f}" fill="{PAPER}"/>')

for code, gloss, items, ry, nrow in body:
    add(f'<line x1="{LEFT}" y1="{ry-8:.1f}" x2="{W-8}" y2="{ry-8:.1f}" stroke="{RULE}" stroke-width="0.5"/>')
    txt(LEFT, ry + 1, code, 7.2, ACCENT, 700)
    txt(LEFT, ry + 9, gloss, 5.6, LIGHT)
    if not items:
        txt(COLS_X[0], ry + 1, "none in the LLM era", 6.4, WARN, 400, "start", "italic")
        if code == "R4":
            txt(COLS_X[0] + 78, ry + 1, "Robot Scientist Adam (2004) is the only instance in the corpus",
                5.8, LIGHT, 400, "start", "italic")
    for k, d in enumerate(items):
        cx, cy = COLS_X[k % 4], ry + 1 + ROWH * (k // 4)
        v, w = val(d['Validation']), who(d['Checked by'])
        g = {2: "●", 1: "◐", 0: "○"}[v]
        add(f'<text x="{cx:.1f}" y="{cy:.1f}" font-size="6.2" fill="{INK if v==2 else MID}">{g}</text>')
        txt(cx + 8, cy, d['System'][:20], 6.4, INK)
        txt(cx + COLW - 12, cy, w, 6.2, WARN if w in ('T', '?') else MID, 700, "end")

ly = H - 34
add(f'<line x1="{LEFT}" y1="{ly-8:.1f}" x2="{W-8}" y2="{ly-8:.1f}" stroke="{INK}" stroke-width="0.6"/>')
txt(LEFT, ly, "validation", 5.8, MID, 700)
txt(LEFT + 46, ly, "● physical / in vitro    ◐ benchmark or leaderboard    ○ none, partial or not reported", 5.8, MID)
txt(LEFT, ly + 9, "checked by", 5.8, MID, 700)
txt(LEFT + 46, ly + 9, "A authors    C collaborating labs    L external leaderboard    "
                        "T third party, after release    ? none stated", 5.8, MID)
txt(LEFT, ly + 18, f"n = {len(LLM)} LLM-era systems. Venues verified 29 July 2026. "
                   "Representation coded from the published description; borderline cases are noted in the text.",
    5.6, LIGHT, 400, "start", "italic")
add('</svg>')
open("assets/ai-scientist-landscape-review.svg", "w").write("\n".join(out))
print(f"wrote assets/ai-scientist-landscape-review.svg  ({W} x {H:.0f} pt)")
for code, _ in RUNGS:
    print(f"  {code}: {len(by.get(code, []))}")
