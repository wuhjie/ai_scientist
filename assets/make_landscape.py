#!/usr/bin/env python3
"""
Landscape of AI-enabled scientific-discovery systems.

Replaces the earlier "family tree" figure, whose tree grammar implied ancestry
and comparable autonomy where neither is established. Panels are categories.
Documented relationships and explicitly identified conceptual similarities are
drawn, each labelled, in three line weights: solid for a stated same-programme
link, dashed for a documented citation, dotted for a conceptual resemblance with
no citation established.

Regenerate:  python3 assets/make_landscape.py
"""
from html import escape

W, PANEL_W, CARD_H, CARD_GAP, PAD = 1400, 315, 74, 8, 12
COL_X = [40, 375, 710, 1045]

INK, MID, LIGHT, RULE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
PAPER, FILL, ACCENT, WARN = "#fcfcfb", "#f4f3ef", "#2a78d6", "#9e3129"
DOTTED = "#b9b8b1"

out = []
def add(s): out.append(s)
def txt(x, y, s, size=11, fill=INK, weight=400, anchor="start", style=""):
    st = f' font-style="{style}"' if style else ""
    add(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{st}>{escape(s)}</text>')

def card(x, y, e, dashed=False):
    """System card: name, venue, autonomy line, executor+evidence line.
       Publication / non-system card: name, venue, kind line."""
    name, venue = e[0], e[1]
    dash = ' stroke-dasharray="4 3"' if dashed else ""
    add(f'<rect x="{x}" y="{y}" width="{PANEL_W}" height="{CARD_H}" rx="6" '
        f'fill="{PAPER if not dashed else "none"}" stroke="{RULE}" stroke-width="1"{dash}/>')
    txt(x + 11, y + 19, name, 11.5, INK, 600)
    if len(e) > 4 and e[4]:
        txt(x + PANEL_W - 11, y + 19, e[4], 9, WARN, 600, "end")
    txt(x + 11, y + 34, venue, 9.5, LIGHT)
    if dashed:
        txt(x + 11, y + 55, e[2], 8.8, MID, 400, "start", "italic")
    else:
        txt(x + 11, y + 51, f"autonomy: {e[2]}", 8.8, MID)
        txt(x + 11, y + 64, f"executor: {e[3][0]} · evidence: {e[3][1]}", 8.8, MID)

def panel(x, y, title, entries, dashed=False, note=None):
    h = PAD + 30 + len(entries) * CARD_H + (len(entries) - 1) * CARD_GAP + PAD + (16 if note else 0)
    add(f'<rect x="{x}" y="{y}" width="{PANEL_W}" height="{h}" rx="8" fill="{FILL}"/>')
    txt(x + 12, y + 22, title, 10.5, MID, 700)
    txt(x + PANEL_W - 12, y + 22, str(len(entries)), 10.5, LIGHT, 600, "end")
    add(f'<line x1="{x+12}" y1="{y+29}" x2="{x+PANEL_W-12}" y2="{y+29}" stroke="{RULE}" stroke-width="1"/>')
    cy, ys = y + PAD + 30, []
    for e in entries:
        ys.append(cy)
        card(x, cy, e, dashed=dashed)
        cy += CARD_H + CARD_GAP
    if note:
        txt(x + 12, cy - CARD_GAP + 14, note, 8.6, LIGHT, 400, "start", "italic")
    return h, ys

# ── data · ordered by year within each panel, ties alphabetical ────────────
CLASSICAL = [
    ("DENDRAL", "1965– · Stanford", "not assessed", ("code", "rule-consistency check")),
    ("BACON", "Langley et al., 1981", "not assessed", ("code", "rediscovery of known laws")),
    ("KEKADA", "Kulkarni & Simon, 1988", "not assessed", ("simulation", "historical-case replication")),
]
BOOK = ("Scientific Discovery", "Langley, Simon, Bradshaw & Żytkow, MIT Press 1987", "monograph — not a system")
ADAM = ("Robot Scientist “Adam”", "Nature 427:247–252 (2004)", "closed-loop autonomous", ("robot", "physical, autonomous"))
AUTOM = ("The Automation of Science", "King et al., Science 324:85–89 (2009)", "research article describing Adam — not a separate system")

GENERAL = [
    ("Agent Laboratory", "Findings of EMNLP 2025", "semi-autonomous; optional human feedback", ("code", "none reported")),
    ("Kosmos", "preprint, arXiv 2511.02824 (2025)", "human-steered", ("code", "expert rating (partial)")),
    ("Agon", "preprint, arXiv 2606.24177 (2026)", "human-steered", ("code", "none reported")),
    ("Co-Scientist", "Nature 655:487–496 (2026)", "human-steered", ("human lab", "in vitro")),
    ("ERA", "Nature 654:909–916 (2026)", "not assessed", ("code", "public leaderboard")),
    ("SCION", "preprint, arXiv 2607.03863 (2026)", "not stated", ("code", "none reported")),
    ("The AI Scientist", "Nature 651:914–919 (2026)", "minimal supervision", ("code", "benchmark; workshop review")),
]
BIOLOGY = [
    ("Virtual Lab", "Nature 646:716–723 (2025)", "not assessed", ("human lab", "in vitro")),
    ("Biomni", "Science (2026)", "not assessed", ("code", "benchmark, 400+ tasks")),
    ("CRISPR-GPT", "Nat. Biomed. Eng. 10(2) (2026)", "human-steered", ("human lab", "in vitro")),
    ("Robin", "Nature 655:497–505 (2026)", "human-steered", ("human lab", "in vitro")),
]
LABS = [
    ("A-Lab", "Nature (2023)", "closed-loop", ("robot", "physical synthesis"), "some reported phase identifications disputed [R1]"),
    ("Coscientist", "Nature 624:570–578 (2023)", "not assessed", ("robot", "physical synthesis")),
    ("Autonomous mobile robots", "Cooper et al., Nature (2024)", "not assessed", ("robot", "physical synthesis")),
    ("RoboChem", "Science (2024)", "not assessed", ("robot", "physical synthesis")),
]
PROGRAM = [
    ("FunSearch", "Nature 625 (2024)", "not assessed", ("code", "benchmark, open problems")),
    ("AlphaEvolve", "preprint, arXiv 2506.13131 (2025)", "not stated", ("code", "benchmark")),
    ("LLM-SR", "ICLR 2025 (Oral)", "not stated", ("code", "held-out / OOD data")),
]
MLENG = [
    ("AIDE", "preprint, arXiv 2502.13138 (2025)", "minimal supervision", ("code", "benchmark")),
    ("MLE-STAR", "preprint, arXiv 2506.15692 (2025)", "minimal supervision", ("code", "benchmark")),
    ("Zochi", "company blog (2025)", "not assessed", ("code", "venue review (claimed)")),
]
CHEM = [
    ("ChemCrow", "Nature Mach. Intell. 6 (2024)", "human-steered", ("robot, supervised", "physical synthesis")),
    ("HoneyComb", "Findings of EMNLP 2024", "not stated", ("code", "benchmark")),
    ("LLMatDesign", "preprint, arXiv 2406.13163 (2024)", "not assessed", ("code", "none reported")),
    ("ChemAgents", "JACS 147(15):12534–12545 (2025)", "not assessed", ("robot", "physical synthesis")),
    ("SciAgents", "Advanced Materials (2025)", "not assessed", ("code", "none reported")),
]
LIT = [("PaperQA2", "preprint, arXiv 2409.13740 (2024)", "minimal supervision", ("code", "benchmark, LitQA2"))]
NONSYS = [
    ("Empowering biomedical discovery", "Zitnik lab, Cell (2024)", "agenda / perspective — autonomy-level taxonomy"),
    ("MLE-bench", "ICLR 2025 (Oral) · OpenAI", "benchmark — 75 Kaggle competitions"),
]

SYSTEMS = GENERAL + BIOLOGY + LABS + PROGRAM + MLENG + CHEM + LIT
N_SYS = len(SYSTEMS)
N_UNASSESSED = sum(1 for s in SYSTEMS if s[2] == "not assessed")

# ── canvas ─────────────────────────────────────────────────────────────────
add('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="{H}" viewBox="0 0 %d {H}" '
    'role="img" aria-labelledby="ttl dsc" '
    'font-family=\'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif\'>' % (W, W))
add('<title id="ttl">Landscape of AI-enabled scientific-discovery systems</title>')
add('<desc id="dsc">Systems grouped by application area, each card recording autonomy, '
    'experiment executor and evidence type. Panels are categories, not lineages. Documented '
    'relationships and explicitly identified conceptual similarities are drawn, each labelled.</desc>')
add('<defs>'
    f'<marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{ACCENT}"/></marker>'
    f'<marker id="arwg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{LIGHT}"/></marker>'
    f'<marker id="arwd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{DOTTED}"/></marker>'
    '</defs>')
add(f'<rect width="{W}" height="{{H}}" fill="{PAPER}"/>')

txt(40, 50, "Landscape of AI-enabled scientific-discovery systems", 23, INK, 700)
txt(40, 73, "Grouped by application area. Panels are categories, not lineages — cards are ordered by year within a panel, ties alphabetical.", 11.5, MID)
txt(40, 90, "Documented relationships and explicitly identified conceptual similarities are drawn; each is labelled. Categories and proximity do not imply "
            "influence or descent.  Venues as verified 29 July 2026.", 11.5, MID)

# ── Band A · classical ─────────────────────────────────────────────────────
yA, BAND_A_H = 116, 306
add(f'<rect x="24" y="{yA}" width="{W-48}" height="{BAND_A_H}" rx="10" fill="{FILL}"/>')
txt(40, yA + 24, "CLASSICAL DISCOVERY PROGRAMMES (PRE-LLM)", 10.5, MID, 700)
txt(W - 40, yA + 24, "4 systems · 2 publications", 10.5, LIGHT, 600, "end")
add(f'<line x1="40" y1="{yA+32}" x2="{W-40}" y2="{yA+32}" stroke="{RULE}" stroke-width="1"/>')

yA1 = yA + 46
for i, c in enumerate(CLASSICAL):
    card(COL_X[i], yA1, c)
yA2 = yA1 + CARD_H + 78
card(COL_X[0], yA2, BOOK, dashed=True)
card(COL_X[1], yA2, ADAM)
card(COL_X[2], yA2, AUTOM, dashed=True)

# DENDRAL — cited in the reference list of the 2004 Adam paper [R2]: dashed, documented
add(f'<path d="M {COL_X[0]+PANEL_W//2} {yA1+CARD_H} L 445 {yA2-5}" fill="none" stroke="{LIGHT}" '
    f'stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#arwg)"/>')
txt(48, yA2 - 12, "documented influence — direct citation, not descent  [R2]", 9, LIGHT, 400, "start", "italic")

# BACON, KEKADA — resemblance only; separate pairwise dotted links, no shared bus
for i, tx in ((1, 528), (2, 600)):
    cx = COL_X[i] + PANEL_W // 2
    add(f'<path d="M {cx} {yA1+CARD_H} L {tx} {yA2-5}" fill="none" stroke="{DOTTED}" '
        f'stroke-width="1" stroke-dasharray="1.5 3.5" marker-end="url(#arwd)"/>')
txt(W - 40, yA1 + CARD_H + 42, "conceptual similarity — no direct citation established", 9, LIGHT, 400, "end", "italic")

# documented citation — the 2004 Adam paper cites the 1987 monograph
by = yA2 + CARD_H + 18
add(f'<path d="M {COL_X[0]+PANEL_W//2} {yA2+CARD_H} L {COL_X[0]+PANEL_W//2} {by} '
    f'L {COL_X[1]+PANEL_W//2} {by} L {COL_X[1]+PANEL_W//2} {yA2+CARD_H+5}" fill="none" '
    f'stroke="{LIGHT}" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#arwg)"/>')
txt(COL_X[1] + PANEL_W // 2 + 14, by + 4, "documented influence — direct citation, not descent  [R2]", 9, LIGHT, 400, "start", "italic")

# same research programme
add(f'<path d="M {COL_X[1]+PANEL_W+4} {yA2+CARD_H//2} L {COL_X[2]-4} {yA2+CARD_H//2}" fill="none" '
    f'stroke="{ACCENT}" stroke-width="1.5" marker-end="url(#arw)"/>')
txt(COL_X[2] + 2, yA2 - 10, "same research programme", 9, ACCENT, 600, "start")
txt(W - 40, by + 4, "Publications and monographs — held separate from systems.", 9, LIGHT, 400, "end", "italic")

# ── divider ────────────────────────────────────────────────────────────────
yBreak = yA + BAND_A_H + 26
add(f'<line x1="40" y1="{yBreak}" x2="{W-40}" y2="{yBreak}" stroke="#c3c2b7" stroke-width="1" stroke-dasharray="4 5"/>')
add(f'<rect x="{W//2-230}" y="{yBreak-8}" width="460" height="16" fill="{PAPER}"/>')
txt(W // 2, yBreak + 4, "─  contemporary systems · LLM agents, program search & autonomous labs  ─", 10, LIGHT, 600, "middle")

# ── Band B · category panels, stacked to balance column heights ────────────
yB = yBreak + 26
COLUMNS = [
    [("GENERAL / CROSS-DOMAIN RESEARCH AGENTS", GENERAL, False),
     ("LITERATURE & EVIDENCE SYNTHESIS", LIT, False)],
    [("CHEMISTRY / MATERIALS AGENTS", CHEM, False),
     ("ML ENGINEERING SELF-RESEARCH", MLENG, False)],
    [("BIOLOGY / LIFE SCIENCES", BIOLOGY, False),
     ("SELF-DRIVING LABS", LABS, False)],
    [("PROGRAM & EQUATION DISCOVERY", PROGRAM, False),
     ("NON-SYSTEM ENTRIES", NONSYS, True)],
]
prog_ys, col_bottom = None, []
for ci, stack in enumerate(COLUMNS):
    cy = yB
    for (t, e, dashed) in stack:
        note = "Benchmarks and agenda papers. Excluded from every system ratio." if dashed else None
        h, ys = panel(COL_X[ci], cy, t, e, dashed=dashed, note=note)
        if t.startswith("PROGRAM"):
            prog_ys = ys
        cy += h + 24
    col_bottom.append(cy - 24)

fx = COL_X[3] + PANEL_W - 30
add(f'<path d="M {fx} {prog_ys[0]+CARD_H} L {fx+18} {prog_ys[0]+CARD_H} '
    f'L {fx+18} {prog_ys[1]+CARD_H//2} L {fx+2} {prog_ys[1]+CARD_H//2}" fill="none" '
    f'stroke="{ACCENT}" stroke-width="1.5" marker-end="url(#arw)"/>')
txt(fx - 8, prog_ys[0] + CARD_H + 20, "methodological generalisation", 8.8, ACCENT, 600, "end")

# ── legend ─────────────────────────────────────────────────────────────────
yL = max(col_bottom) + 30
add(f'<rect x="24" y="{yL}" width="{W-48}" height="150" rx="10" fill="{FILL}"/>')
txt(40, yL + 22, "READING A CARD", 10.5, MID, 700)
add(f'<line x1="40" y1="{yL+30}" x2="{W-40}" y2="{yL+30}" stroke="{RULE}" stroke-width="1"/>')
txt(40, yL + 48, "autonomy — degree of independent loop execution:  closed-loop autonomous · semi-autonomous · minimal supervision · human-steered · "
                 "not stated (source silent) · not assessed — autonomy not classified in this figure", 9.6, MID)
txt(40, yL + 66, "executor — who or what performs the experiment or evaluation:  code · simulation · robot · robot, supervised · human lab", 9.6, MID)
txt(40, yL + 84, "evidence — the strongest reported validation type:  benchmark · leaderboard · held-out data · in vitro · physical synthesis · expert rating · none reported", 9.6, MID)
add(f'<line x1="40" y1="{yL+96}" x2="{W-40}" y2="{yL+96}" stroke="{RULE}" stroke-width="1"/>')
txt(40, yL + 112, "[R1]  A-Lab — an independent reanalysis disputed a subset of reported phase identifications. The autonomous-lab architecture is not invalidated.", 9.4, WARN)
txt(40, yL + 126, "         Source: “New analysis raises doubts over autonomous lab’s materials discoveries”, Chemistry World (RSC, 2024), with response from the A-Lab authors — secondary reporting; no primary DOI recorded in this review.", 9, LIGHT)
txt(40, yL + 142, "[R2]  Documented-influence links (DENDRAL → Adam, Scientific Discovery → Adam) are drawn from the reference list of King et al., Nature 427:247–252 (2004), doi:10.1038/nature02236.", 9, LIGHT)

yF = yL + 150 + 22
txt(40, yF, f"{N_SYS} contemporary systems · 4 classical systems · 2 non-system entries · 2 foundational publications.  "
            f"Ratios elsewhere are reported over the {N_SYS} contemporary systems unless stated.", 9.6, MID)
add('</svg>')

H = yF + 26
open("assets/ai-scientist-landscape.svg", "w").write("\n".join(out).replace("{H}", str(H)))
print(f"wrote assets/ai-scientist-landscape.svg  ({W} x {H})  "
      f"systems={N_SYS}  not-assessed={N_UNASSESSED}")
