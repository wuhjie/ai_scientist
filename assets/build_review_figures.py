#!/usr/bin/env python3
"""Build the Pass 3 review figures as matching SVG and TikZ assets.

The review owns this source so its figures cannot drift from the manuscript's
H/S/E/A/U/P taxonomy.  Run from any directory:

    python3 assets/build_review_figures.py
"""

from html import escape
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REVIEW = ROOT / "review"

INK = "#172033"
MID = "#526076"
MUTED = "#768399"
RULE = "#D7DEE9"
PANEL = "#F5F7FA"
ALT = "#FAFBFD"
ACCENT = "#245EA8"
PALE = "#EAF1FA"


CLASSICAL = [
    ("DENDRAL", "1965"),
    ("BACON", "1981"),
    ("KEKADA", "1988"),
    ("Robot Scientist Adam", "2004"),
]

CONTEXT = [
    ("Scientific Discovery", "1987"),
    ("The Automation of Science", "2009"),
    ("Empowering biomedical discovery", "2024"),
    ("MLE-bench", "2025"),
]

CONTEMPORARY = [
    (
        "GENERAL / CROSS-DOMAIN",
        [
            [("Agent Laboratory", "25"), ("KOSMOS", "25"), ("Agon", "26"), ("Co-Scientist", "26")],
            [("ERA", "26"), ("SCION", "26"), ("The AI Scientist", "26")],
        ],
    ),
    ("LITERATURE / EVIDENCE", [[("PaperQA2", "24")]]),
    (
        "CHEMISTRY / MATERIALS",
        [[("ChemCrow", "24"), ("HoneyComb", "24"), ("LLMatDesign", "24"),
          ("ChemAgents", "25"), ("SciAgents", "25")]],
    ),
    ("ML ENGINEERING", [[("AIDE", "25"), ("MLE-STAR", "25"), ("Zochi", "25")]]),
    (
        "BIOLOGY / LIFE SCIENCES",
        [[("Virtual Lab", "25"), ("Biomni", "26"), ("CRISPR-GPT", "25"), ("Robin", "26")]],
    ),
    (
        "SELF-DRIVING LABS",
        [[("A-Lab", "23"), ("Coscientist", "23"),
          ("Autonomous mobile robots", "24"), ("RoboChem", "24")]],
    ),
    (
        "PROGRAM / EQUATION",
        [[("FunSearch", "24"), ("AlphaEvolve", "25"), ("LLM-SR", "25")]],
    ),
]


def svg_text(x, y, value, size, fill=INK, weight=400, anchor="start", italic=False):
    style = ' font-style="italic"' if italic else ""
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{style}>{escape(value)}</text>'
    )


def svg_system_line(x, y, items):
    parts = [f'<text x="{x}" y="{y}" font-size="15" fill="{INK}" font-weight="600">']
    for index, (name, year) in enumerate(items):
        if index:
            parts.append(f'<tspan fill="{RULE}" font-weight="400">  •  </tspan>')
        parts.append(f'<tspan>{escape(name)}</tspan>')
        parts.append(f'<tspan fill="{MUTED}" font-size="13" font-weight="400"> ’{year}</tspan>')
    parts.append("</text>")
    return "".join(parts)


def build_landscape_svg():
    width, height = 906, 564
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="453pt" height="282pt" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="land-title land-desc" '
        'font-family="Helvetica, Arial, sans-serif">',
        '<title id="land-title">Scope of the reviewed AI Scientist landscape</title>',
        '<desc id="land-desc">Four classical comparators, four contextual publications, and '
        'twenty-seven contemporary systems grouped into seven application areas.</desc>',
        f'<rect width="{width}" height="{height}" fill="#FFFFFF"/>',
        svg_text(24, 27, "REVIEW CORPUS · PASS 3", 13, ACCENT, 700),
        svg_text(882, 27, "27 contemporary · 4 classical · 4 context", 13, MUTED, 400, "end"),
        f'<rect x="20" y="43" width="866" height="82" rx="10" fill="{PANEL}"/>',
        svg_text(36, 65, "CLASSICAL COMPARATORS", 14, MID, 700),
    ]

    card_y, card_w, gap = 76, 197, 12
    for index, (name, year) in enumerate(CLASSICAL):
        x = 36 + index * (card_w + gap)
        out.extend([
            f'<rect x="{x}" y="{card_y}" width="{card_w}" height="34" rx="5" '
            f'fill="#FFFFFF" stroke="{RULE}"/>',
            f'<rect x="{x}" y="{card_y}" width="5" height="34" rx="2.5" fill="{ACCENT}"/>',
            svg_text(x + 16, card_y + 22, name, 13 if index == 3 else 15, INK, 700),
            svg_text(x + card_w - 12, card_y + 22, year, 13, MUTED, 400, "end"),
        ])

    out.extend([
        svg_text(24, 148, "CONTEXT — publications and benchmarks, held outside system ratios", 13, MID, 700),
        f'<rect x="20" y="158" width="866" height="42" rx="7" fill="#FFFFFF" '
        f'stroke="{RULE}" stroke-dasharray="5 4"/>',
    ])
    cx = [36, 246, 456, 666]
    for index, (x, (name, year)) in enumerate(zip(cx, CONTEXT)):
        out.append(svg_text(x, 178, name, 11.5 if index == 2 else 13, MID, 600))
        out.append(svg_text(x, 194, year, 12, MUTED, 400))

    out.extend([
        f'<line x1="20" y1="221" x2="886" y2="221" stroke="{ACCENT}" stroke-width="2"/>',
        svg_text(24, 244, "CONTEMPORARY SYSTEMS", 14, ACCENT, 700),
        svg_text(882, 244, "grouped by application area; adjacency does not imply lineage", 13, MUTED, 400, "end", True),
    ])

    y = 258
    for index, (domain, lines) in enumerate(CONTEMPORARY):
        row_h = 56 if len(lines) == 2 else 35
        if index % 2 == 0:
            out.append(f'<rect x="20" y="{y}" width="866" height="{row_h}" rx="4" fill="{ALT}"/>')
        out.append(svg_text(34, y + 22, domain, 13, MID, 700))
        for line_index, items in enumerate(lines):
            out.append(svg_system_line(232, y + 22 + line_index * 21, items))
        out.append(f'<line x1="20" y1="{y + row_h}" x2="886" y2="{y + row_h}" stroke="{RULE}"/>')
        y += row_h

    out.extend([
        svg_text(24, 552, "Years follow the verified bibliography record for the version represented in the catalogue.", 12, MUTED, 400, "start", True),
        "</svg>",
    ])
    (HERE / "ai-scientist-landscape-review.svg").write_text("\n".join(out) + "\n", encoding="utf-8")


def build_loop_svg():
    width, height = 906, 354
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="453pt" height="177pt" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="loop-title loop-desc" '
        'font-family="Helvetica, Arial, sans-serif">',
        '<title id="loop-title">The Pass 3 epistemic loop</title>',
        '<desc id="loop-desc">Scientific claims and state receive evidence, evidence is adjudicated, '
        'and an update either changes an output or changes the represented epistemic state. Provenance '
        'records who produced and checked the evidence.</desc>',
        f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{ACCENT}"/></marker></defs>',
        f'<rect width="{width}" height="{height}" fill="#FFFFFF"/>',
        svg_text(24, 27, "EPISTEMIC CONTROL · PASS 3", 13, ACCENT, 700),
        svg_text(882, 27, "H/S → E → A → U", 13, MUTED, 600, "end"),
    ]

    cards = [
        (24, 50, 184, 154, "CLAIM + STATE", "H / S"),
        (228, 50, 166, 154, "EVIDENCE", "E"),
        (414, 50, 188, 154, "ADJUDICATION", "A"),
        (622, 50, 260, 154, "UPDATE", "U"),
    ]
    for x, y, w, h, title, code in cards:
        out.extend([
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFFFFF" stroke="{RULE}" stroke-width="2"/>',
            f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{PALE}"/>',
            f'<rect x="{x}" y="{y + 26}" width="{w}" height="8" fill="{PALE}"/>',
            svg_text(x + 14, y + 23, title, 14, INK, 700),
            svg_text(x + w - 14, y + 23, code, 14, ACCENT, 700, "end"),
        ])

    for x1, x2 in [(208, 228), (394, 414), (602, 622)]:
        out.append(f'<line x1="{x1 + 4}" y1="127" x2="{x2 - 5}" y2="127" stroke="{ACCENT}" stroke-width="2" marker-end="url(#arrow)"/>')

    out.extend([
        svg_text(40, 107, "H0–H3", 15, ACCENT, 700),
        svg_text(99, 107, "claim form", 15, INK, 600),
        svg_text(40, 137, "S0–S4", 15, ACCENT, 700),
        svg_text(99, 137, "scientific state", 15, INK, 600),
        svg_text(40, 171, "What claim exists, and what", 13, MID, 400),
        svg_text(40, 188, "persists between actions?", 13, MID, 400),

        svg_text(244, 105, "E0", 13, MUTED, 700), svg_text(280, 105, "none", 14, INK, 500),
        svg_text(244, 128, "E1", 13, MUTED, 700), svg_text(280, 128, "literature", 14, INK, 500),
        svg_text(244, 151, "E2–E3", 13, MUTED, 700), svg_text(300, 151, "execution · data", 14, INK, 500),
        svg_text(244, 174, "E4–E5", 13, MUTED, 700), svg_text(300, 174, "physical · formal", 14, INK, 500),

        svg_text(430, 105, "A0", 13, MUTED, 700), svg_text(468, 105, "none", 14, INK, 500),
        svg_text(430, 128, "A1", 13, MUTED, 700), svg_text(468, 128, "model / peer", 14, INK, 500),
        svg_text(430, 151, "A2–A3", 13, MUTED, 700), svg_text(490, 151, "metric · statistics", 14, INK, 500),
        svg_text(430, 174, "A4–A5", 13, MUTED, 700), svg_text(490, 174, "formal · expert", 14, INK, 500),

        f'<rect x="636" y="96" width="108" height="91" rx="5" fill="{PANEL}"/>',
        svg_text(648, 116, "U0–U3", 14, MID, 700),
        svg_text(648, 138, "operational", 13, MID, 600),
        svg_text(648, 153, "none · select", 12.5, MUTED, 400),
        svg_text(648, 169, "regenerate", 12.5, MUTED, 400),
        svg_text(648, 185, "append", 12.5, MUTED, 400),
        f'<rect x="756" y="96" width="112" height="91" rx="5" fill="{PALE}" stroke="{ACCENT}"/>',
        svg_text(768, 116, "U4–U6", 14, ACCENT, 700),
        svg_text(768, 138, "epistemic", 13, ACCENT, 600),
        svg_text(768, 153, "revise claim", 12.5, INK, 400),
        svg_text(768, 169, "revise strength", 12.5, INK, 400),
        svg_text(768, 185, "eliminate", 12.5, INK, 400),

        f'<path d="M 812 205 L 812 232 L 116 232 L 116 210" fill="none" stroke="{ACCENT}" '
        f'stroke-width="2.2" marker-end="url(#arrow)"/>',
        svg_text(464, 226, "an epistemic update changes the represented claim or state", 13, ACCENT, 600, "middle"),

        f'<rect x="228" y="254" width="374" height="54" rx="7" fill="{PANEL}" stroke="{RULE}" stroke-dasharray="5 4"/>',
        svg_text(244, 276, "PROVENANCE · P", 13, MID, 700),
        svg_text(244, 296, "internal · developer · collaborator · external scorer · independent verifier", 11.5, INK, 500),
        f'<line x1="312" y1="254" x2="312" y2="210" stroke="{RULE}" stroke-width="2" stroke-dasharray="4 4"/>',
        f'<line x1="508" y1="254" x2="508" y2="210" stroke="{RULE}" stroke-width="2" stroke-dasharray="4 4"/>',

        svg_text(453, 337, "Generation is not revision: only U4–U6 alter an explicit claim-level epistemic variable.", 14, MID, 600, "middle", True),
        "</svg>",
    ])
    (HERE / "ai-scientist-overview.svg").write_text("\n".join(out) + "\n", encoding="utf-8")


def tex_item(name, year):
    escaped = name.replace("&", r"\&")
    return rf"\lsitem{{{escaped}}}{{'{year}}}"


def build_landscape_tex():
    rows = []
    y = -116.0
    for index, (domain, lines) in enumerate(CONTEMPORARY):
        height = 28.0 if len(lines) == 2 else 18.0
        fill = "lsalt" if index % 2 == 0 else "white"
        rows.append(rf"  \fill[{fill}] (0pt,{y + 4:.1f}pt) rectangle (453pt,{y - height + 4:.1f}pt);")
        rows.append(rf"  \node[domain] at (7pt,{y:.1f}pt) {{{domain}}};")
        line_tex = r" \,\textcolor{lsrulec}{\textbullet}\, ".join(tex_item(*item) for item in lines[0])
        if len(lines) == 2:
            line_tex += r"\\[-1pt]" + r" \,\textcolor{lsrulec}{\textbullet}\, ".join(tex_item(*item) for item in lines[1])
        rows.append(rf"  \node[systems] at (108pt,{y:.1f}pt) {{{line_tex}}};")
        rows.append(rf"  \draw[lsrule] (0pt,{y - height + 4:.1f}pt) -- (453pt,{y - height + 4:.1f}pt);")
        y -= height

    cards = []
    xs = [7.0, 117.0, 227.0, 337.0]
    for x, (name, year) in zip(xs, CLASSICAL):
        cards.extend([
            rf"  \filldraw[draw=lsrulec,fill=white,rounded corners=2pt] ({x:.1f}pt,-28pt) rectangle ({x + 103:.1f}pt,-48pt);",
            rf"  \fill[lsacc] ({x:.1f}pt,-28pt) rectangle ({x + 2.5:.1f}pt,-48pt);",
            rf"  \node[classic] at ({x + 7:.1f}pt,-38pt) {{{name}\hfill\textcolor{{lsmuted}}{{{year}}}}};",
        ])

    context_nodes = []
    context_x = [8.0, 118.0, 228.0, 338.0]
    for x, (name, year) in zip(context_x, CONTEXT):
        context_nodes.append(rf"  \node[context] at ({x:.1f}pt,-78pt) {{{name} \textcolor{{lsmuted}}{{{year}}}}};")

    tex = rf"""% Generated by review/assets/build_review_figures.py -- do not edit by hand.
\begin{{figure*}}[t]
\centering
\begingroup
\definecolor{{lsink}}{{HTML}}{{172033}}
\definecolor{{lsmid}}{{HTML}}{{526076}}
\definecolor{{lsmuted}}{{HTML}}{{768399}}
\definecolor{{lsrulec}}{{HTML}}{{D7DEE9}}
\definecolor{{lsalt}}{{HTML}}{{FAFBFD}}
\definecolor{{lspanel}}{{HTML}}{{F5F7FA}}
\definecolor{{lsacc}}{{HTML}}{{245EA8}}
\tikzset{{
  kicker/.style={{anchor=west,font=\fontsize{{6.6}}{{7.2}}\bfseries\selectfont,text=lsacc}},
  meta/.style={{anchor=east,font=\fontsize{{6.5}}{{7.1}}\selectfont,text=lsmuted}},
  classic/.style={{anchor=west,text width=91pt,font=\fontsize{{7.3}}{{8}}\bfseries\selectfont,text=lsink}},
  context/.style={{anchor=west,text width=105pt,font=\fontsize{{6.6}}{{7.2}}\selectfont,text=lsmid}},
  domain/.style={{anchor=north west,text width=92pt,font=\fontsize{{6.5}}{{7.2}}\bfseries\selectfont,text=lsmid}},
  systems/.style={{anchor=north west,text width=341pt,align=left,font=\fontsize{{7.3}}{{8.2}}\selectfont,text=lsink}},
  lsrule/.style={{draw=lsrulec,line width=0.35pt}}
}}
\newcommand{{\lsitem}}[2]{{\textbf{{#1}}\,\textcolor{{lsmuted}}{{\fontsize{{6.3}}{{7}}\selectfont #2}}}}
\begin{{tikzpicture}}[x=1pt,y=1pt]
  \node[kicker] at (0pt,0pt) {{REVIEW CORPUS \textperiodcentered\ PASS 3}};
  \node[meta] at (453pt,0pt) {{27 contemporary \textperiodcentered\ 4 classical \textperiodcentered\ 4 context}};
  \fill[lspanel,rounded corners=4pt] (0pt,-12pt) rectangle (453pt,-56pt);
  \node[domain,text width=150pt] at (7pt,-17pt) {{CLASSICAL COMPARATORS}};
{chr(10).join(cards)}
  \node[domain,text width=330pt] at (7pt,-63pt) {{CONTEXT --- publications and benchmarks, held outside system ratios}};
  \draw[lsrule,dashed] (0pt,-70pt) rectangle (453pt,-87pt);
{chr(10).join(context_nodes)}
  \draw[draw=lsacc,line width=0.8pt] (0pt,-99pt) -- (453pt,-99pt);
  \node[kicker] at (0pt,-107pt) {{CONTEMPORARY SYSTEMS}};
  \node[meta] at (453pt,-107pt) {{grouped by application area; adjacency is not lineage}};
{chr(10).join(rows)}
  \node[context,text width=440pt] at (7pt,{y - 3:.1f}pt) {{\itshape Years follow the verified bibliography record for the version represented in the catalogue.}};
\end{{tikzpicture}}
\endgroup
\caption{{Scope of the reviewed AI Scientist landscape. Classical comparators and contextual publications are separated from the 27 contemporary systems used in the landscape counts. Contemporary systems are grouped only by application area; position and adjacency do not imply influence, maturity, or epistemic capability.}}
\label{{fig:landscape}}
\end{{figure*}}
"""
    (REVIEW / "fig-landscape.tex").write_text(tex, encoding="utf-8")


def build_loop_tex():
    tex = r"""% Generated by review/assets/build_review_figures.py -- do not edit by hand.
\begin{figure*}[t]
\centering
\begingroup
\definecolor{epink}{HTML}{172033}
\definecolor{epmid}{HTML}{526076}
\definecolor{epmuted}{HTML}{768399}
\definecolor{eprule}{HTML}{D7DEE9}
\definecolor{eppanel}{HTML}{F5F7FA}
\definecolor{epaccent}{HTML}{245EA8}
\definecolor{eppale}{HTML}{EAF1FA}
\tikzset{
  epframe/.style={draw=eprule,line width=0.7pt,rounded corners=3pt,fill=white},
  ephead/.style={anchor=west,font=\fontsize{6.8}{7.5}\bfseries\selectfont,text=epink},
  epcode/.style={anchor=east,font=\fontsize{6.8}{7.5}\bfseries\selectfont,text=epaccent},
  epbody/.style={anchor=west,font=\fontsize{7.1}{8}\selectfont,text=epink},
  epsmall/.style={anchor=west,font=\fontsize{6.3}{7.1}\selectfont,text=epmid},
  epflow/.style={draw=epaccent,line width=0.9pt,->},
  epdash/.style={draw=eprule,line width=0.7pt,dashed}
}
\begin{tikzpicture}[x=1pt,y=1pt]
  \node[anchor=west,font=\fontsize{6.6}{7.2}\bfseries\selectfont,text=epaccent] at (0pt,0pt) {EPISTEMIC CONTROL \textperiodcentered\ PASS 3};
  \node[anchor=east,font=\fontsize{6.5}{7.1}\bfseries\selectfont,text=epmuted] at (453pt,0pt) {H/S $\rightarrow$ E $\rightarrow$ A $\rightarrow$ U};

  \draw[epframe] (0pt,-12pt) rectangle (92pt,-89pt);
  \fill[eppale,rounded corners=3pt] (0pt,-12pt) rectangle (92pt,-29pt);
  \node[ephead] at (7pt,-20.5pt) {CLAIM + STATE};
  \node[epcode] at (85pt,-20.5pt) {H / S};
  \node[epbody] at (8pt,-43pt) {\textcolor{epaccent}{\textbf{H0--H3}}\quad claim form};
  \node[epbody] at (8pt,-57pt) {\textcolor{epaccent}{\textbf{S0--S4}}\quad scientific state};
  \node[epsmall,text width=76pt] at (8pt,-71pt) {What claim exists, and what persists between actions?};

  \draw[epframe] (102pt,-12pt) rectangle (185pt,-89pt);
  \fill[eppale,rounded corners=3pt] (102pt,-12pt) rectangle (185pt,-29pt);
  \node[ephead] at (109pt,-20.5pt) {EVIDENCE};
  \node[epcode] at (178pt,-20.5pt) {E};
  \node[epbody] at (110pt,-42pt) {\textcolor{epmuted}{\textbf{E0}}\quad none};
  \node[epbody] at (110pt,-54pt) {\textcolor{epmuted}{\textbf{E1}}\quad literature};
  \node[epsmall] at (110pt,-66pt) {E2--E3\quad execution / data};
  \node[epsmall] at (110pt,-78pt) {E4--E5\quad physical / formal};

  \draw[epframe] (195pt,-12pt) rectangle (289pt,-89pt);
  \fill[eppale,rounded corners=3pt] (195pt,-12pt) rectangle (289pt,-29pt);
  \node[ephead] at (202pt,-20.5pt) {ADJUDICATION};
  \node[epcode] at (282pt,-20.5pt) {A};
  \node[epbody] at (203pt,-42pt) {\textcolor{epmuted}{\textbf{A0}}\quad none};
  \node[epbody] at (203pt,-54pt) {\textcolor{epmuted}{\textbf{A1}}\quad model / peer};
  \node[epsmall] at (203pt,-66pt) {A2--A3\quad metric / statistics};
  \node[epsmall] at (203pt,-78pt) {A4--A5\quad formal / expert};

  \draw[epframe] (299pt,-12pt) rectangle (453pt,-89pt);
  \fill[eppale,rounded corners=3pt] (299pt,-12pt) rectangle (453pt,-29pt);
  \node[ephead] at (306pt,-20.5pt) {UPDATE};
  \node[epcode] at (446pt,-20.5pt) {U};
  \fill[eppanel,rounded corners=2pt] (306pt,-36pt) rectangle (371pt,-80pt);
  \node[epsmall] at (312pt,-43pt) {\textbf{U0--U3} operational};
  \node[epsmall] at (312pt,-54pt) {none / select};
  \node[epsmall] at (312pt,-64pt) {regenerate};
  \node[epsmall] at (312pt,-74pt) {append};
  \filldraw[draw=epaccent,fill=eppale,rounded corners=2pt] (377pt,-36pt) rectangle (446pt,-80pt);
  \node[epsmall,text=epaccent] at (383pt,-43pt) {\textbf{U4--U6} epistemic};
  \node[epsmall,text=epink] at (383pt,-54pt) {revise claim};
  \node[epsmall,text=epink] at (383pt,-64pt) {revise strength};
  \node[epsmall,text=epink] at (383pt,-74pt) {eliminate};

  \draw[epflow] (92pt,-50pt) -- (102pt,-50pt);
  \draw[epflow] (185pt,-50pt) -- (195pt,-50pt);
  \draw[epflow] (289pt,-50pt) -- (299pt,-50pt);
  \draw[epflow] (415pt,-89pt) -- (415pt,-103pt) -- (46pt,-103pt) -- (46pt,-91pt);
  \node[anchor=center,fill=white,inner xsep=4pt,font=\fontsize{6.4}{7}\bfseries\selectfont,text=epaccent] at (230pt,-103pt) {epistemic update changes the represented claim or state};

  \filldraw[draw=eprule,fill=eppanel,dashed,rounded corners=3pt] (102pt,-118pt) rectangle (289pt,-146pt);
  \node[anchor=west,font=\fontsize{6.4}{7}\bfseries\selectfont,text=epmid] at (110pt,-128pt) {PROVENANCE \textperiodcentered\ P};
  \node[anchor=west,text width=170pt,align=left,font=\fontsize{6.1}{6.8}\selectfont,text=epink] at (110pt,-138pt) {internal \textperiodcentered\ developer \textperiodcentered\ collaborator\\[-1pt]external scorer \textperiodcentered\ independent verifier};
  \draw[epdash] (144pt,-118pt) -- (144pt,-91pt);
  \draw[epdash] (242pt,-118pt) -- (242pt,-91pt);

  \node[anchor=center,font=\fontsize{6.8}{7.5}\bfseries\itshape\selectfont,text=epmid] at (226.5pt,-160pt) {Generation is not revision: only U4--U6 alter an explicit claim-level epistemic variable.};
\end{tikzpicture}
\endgroup
\caption{Epistemic control in an AI Scientist. Claim representation (H) and scientific state (S) determine what can be updated; evidence substrate (E) records what enters the loop; adjudication (A) records how it is interpreted; and update (U) records what changes. Provenance (P) records who produced or checked the evidence. Operational updates U0--U3 change a selection, output, or record, whereas U4--U6 alter an explicit claim-level epistemic variable.}
\label{fig:loop}
\end{figure*}
"""
    (REVIEW / "fig-loop.tex").write_text(tex, encoding="utf-8")


def build_history_svg():
    width, height = 906, 386
    phases = [
        {
            "x": 24,
            "number": "1",
            "title": "EXPLICIT SCIENTIFIC OBJECTS",
            "examples": ["DENDRAL · BACON · KEKADA", "Adam · Eve"],
            "lines": ["structured claims or models", "targeted evidence relations", "revision or elimination possible"],
            "scope": "narrow, domain-specific control",
        },
        {
            "x": 323,
            "number": "2",
            "title": "GENERAL REASONING + TOOL USE",
            "examples": ["Chain-of-Thought · ReAct"],
            "lines": ["flexible task decomposition", "action–observation interaction", "state often remains context"],
            "scope": "broader task handling",
        },
        {
            "x": 622,
            "number": "3",
            "title": "FRAMEWORK-LEVEL CONTROL",
            "examples": ["AI Scientist · Co-Scientist", "KOSMOS · Robin"],
            "lines": ["longer research workflows", "distributed roles and tools", "operational updates common"],
            "scope": "broader, more open-ended control",
        },
    ]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="453pt" height="193pt" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="history-title history-desc" '
        'font-family="Helvetica, Arial, sans-serif">',
        '<title id="history-title">Historical design transition in AI systems for scientific discovery</title>',
        '<desc id="history-desc">Three analytic phases show expansion from explicit but narrow scientific '
        'objects, through general reasoning and tool use, to framework-level research control. Agentic '
        'control expands across the phases while explicit epistemic revision remains uneven.</desc>',
        f'<defs><marker id="history-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{ACCENT}"/></marker></defs>',
        '<rect width="906" height="386" fill="#FFFFFF"/>',
        svg_text(24, 27, "HISTORICAL DESIGN TRANSITION", 13, ACCENT, 700),
        svg_text(882, 27, "analytic phases, not a genealogy", 13, MUTED, 400, "end", True),
    ]
    for phase in phases:
        x = phase["x"]
        out.extend([
            f'<rect x="{x}" y="50" width="260" height="186" rx="9" fill="#FFFFFF" stroke="{RULE}" stroke-width="2"/>',
            f'<rect x="{x}" y="50" width="260" height="42" rx="9" fill="{PALE}"/>',
            f'<rect x="{x}" y="84" width="260" height="8" fill="{PALE}"/>',
            f'<circle cx="{x + 22}" cy="71" r="12" fill="{ACCENT}"/>',
            svg_text(x + 22, 76, phase["number"], 14, "#FFFFFF", 700, "middle"),
            svg_text(x + 44, 76, phase["title"], 13, INK, 700),
        ])
        for example_index, example in enumerate(phase["examples"]):
            out.append(svg_text(x + 18, 113 + example_index * 17, example, 12.5, MID, 600))
        for line_index, line in enumerate(phase["lines"]):
            y = 145 + line_index * 25
            out.append(f'<circle cx="{x + 22}" cy="{y - 4}" r="3.5" fill="{ACCENT}"/>')
            out.append(svg_text(x + 34, y, line, 14, INK, 500))
        out.extend([
            f'<line x1="{x + 18}" y1="214" x2="{x + 242}" y2="214" stroke="{RULE}"/>',
            svg_text(x + 18, 229, phase["scope"], 12, MUTED, 400, "start", True),
        ])

    for start, end in [(284, 323), (583, 622)]:
        out.append(f'<line x1="{start + 7}" y1="143" x2="{end - 8}" y2="143" stroke="{ACCENT}" stroke-width="2" marker-end="url(#history-arrow)"/>')

    out.extend([
        svg_text(24, 274, "AGENTIC CONTROL", 13, ACCENT, 700),
        f'<line x1="174" y1="269" x2="866" y2="269" stroke="{ACCENT}" stroke-width="4" marker-end="url(#history-arrow)"/>',
        svg_text(174, 260, "action space", 12, MID, 500),
        svg_text(456, 260, "research horizon", 12, MID, 500, "middle"),
        svg_text(834, 260, "orchestration", 12, MID, 500, "end"),

        svg_text(24, 325, "EPISTEMIC CONTROL", 13, MID, 700),
        f'<line x1="174" y1="320" x2="866" y2="320" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 6" marker-end="url(#history-arrow)"/>',
        f'<rect x="558" y="300" width="308" height="38" rx="5" fill="{PANEL}"/>',
        svg_text(712, 324, "explicit evidence → claim revision remains uneven", 13, MID, 600, "middle"),
        svg_text(453, 370, "Framework scale increases what can be done; it does not by itself determine what evidence changes.", 13, MID, 600, "middle", True),
        "</svg>",
    ])
    (HERE / "ai-scientist-historical-transition.svg").write_text("\n".join(out) + "\n", encoding="utf-8")


def build_history_tex():
    tex = r"""% Generated by assets/build_review_figures.py -- do not edit by hand.
\begin{figure*}[t]
\centering
\begingroup
\definecolor{hdink}{HTML}{172033}
\definecolor{hdmid}{HTML}{526076}
\definecolor{hdmuted}{HTML}{768399}
\definecolor{hdrule}{HTML}{D7DEE9}
\definecolor{hdpanel}{HTML}{F5F7FA}
\definecolor{hdpale}{HTML}{EAF1FA}
\definecolor{hdaccent}{HTML}{245EA8}
\tikzset{
  hdframe/.style={draw=hdrule,line width=0.7pt,rounded corners=3pt,fill=white},
  hdtitle/.style={anchor=west,font=\fontsize{6.4}{7}\bfseries\selectfont,text=hdink},
  hdexamples/.style={anchor=west,text width=116pt,font=\fontsize{6.0}{6.7}\bfseries\selectfont,text=hdmid},
  hdbody/.style={anchor=west,font=\fontsize{6.6}{7.3}\selectfont,text=hdink},
  hdscope/.style={anchor=west,font=\fontsize{5.9}{6.5}\itshape\selectfont,text=hdmuted},
  hdflow/.style={draw=hdaccent,line width=0.9pt,->}
}
\begin{tikzpicture}[x=1pt,y=1pt]
  \node[anchor=west,font=\fontsize{6.6}{7.2}\bfseries\selectfont,text=hdaccent] at (0pt,0pt) {HISTORICAL DESIGN TRANSITION};
  \node[anchor=east,font=\fontsize{6.4}{7}\itshape\selectfont,text=hdmuted] at (453pt,0pt) {analytic phases, not a genealogy};

  \draw[hdframe] (0pt,-12pt) rectangle (132pt,-105pt);
  \fill[hdpale,rounded corners=3pt] (0pt,-12pt) rectangle (132pt,-33pt);
  \fill[hdaccent] (7pt,-22.5pt) circle (6pt);
  \node[font=\fontsize{6.7}{7.2}\bfseries\selectfont,text=white] at (7pt,-22.5pt) {1};
  \node[hdtitle] at (17pt,-22.5pt) {EXPLICIT SCIENTIFIC OBJECTS};
  \node[hdexamples,align=left] at (8pt,-43pt) {DENDRAL · BACON · KEKADA\\[-1pt]Adam · Eve};
  \fill[hdaccent] (10pt,-59pt) circle (1.6pt); \node[hdbody] at (15pt,-59pt) {structured claims or models};
  \fill[hdaccent] (10pt,-72pt) circle (1.6pt); \node[hdbody] at (15pt,-72pt) {targeted evidence relations};
  \fill[hdaccent] (10pt,-85pt) circle (1.6pt); \node[hdbody] at (15pt,-85pt) {revision or elimination possible};
  \draw[draw=hdrule] (8pt,-94pt) -- (124pt,-94pt);
  \node[hdscope] at (8pt,-100pt) {narrow, domain-specific control};

  \draw[hdframe] (160pt,-12pt) rectangle (292pt,-105pt);
  \fill[hdpale,rounded corners=3pt] (160pt,-12pt) rectangle (292pt,-33pt);
  \fill[hdaccent] (167pt,-22.5pt) circle (6pt);
  \node[font=\fontsize{6.7}{7.2}\bfseries\selectfont,text=white] at (167pt,-22.5pt) {2};
  \node[hdtitle] at (177pt,-22.5pt) {GENERAL REASONING + TOOL USE};
  \node[hdexamples] at (168pt,-43pt) {Chain-of-Thought · ReAct};
  \fill[hdaccent] (170pt,-59pt) circle (1.6pt); \node[hdbody] at (175pt,-59pt) {flexible task decomposition};
  \fill[hdaccent] (170pt,-72pt) circle (1.6pt); \node[hdbody] at (175pt,-72pt) {action--observation interaction};
  \fill[hdaccent] (170pt,-85pt) circle (1.6pt); \node[hdbody] at (175pt,-85pt) {state often remains context};
  \draw[draw=hdrule] (168pt,-94pt) -- (284pt,-94pt);
  \node[hdscope] at (168pt,-100pt) {broader task handling};

  \draw[hdframe] (320pt,-12pt) rectangle (453pt,-105pt);
  \fill[hdpale,rounded corners=3pt] (320pt,-12pt) rectangle (453pt,-33pt);
  \fill[hdaccent] (327pt,-22.5pt) circle (6pt);
  \node[font=\fontsize{6.7}{7.2}\bfseries\selectfont,text=white] at (327pt,-22.5pt) {3};
  \node[hdtitle] at (337pt,-22.5pt) {FRAMEWORK-LEVEL CONTROL};
  \node[hdexamples,align=left] at (328pt,-43pt) {AI Scientist · Co-Scientist\\[-1pt]KOSMOS · Robin};
  \fill[hdaccent] (330pt,-59pt) circle (1.6pt); \node[hdbody] at (335pt,-59pt) {longer research workflows};
  \fill[hdaccent] (330pt,-72pt) circle (1.6pt); \node[hdbody] at (335pt,-72pt) {distributed roles and tools};
  \fill[hdaccent] (330pt,-85pt) circle (1.6pt); \node[hdbody] at (335pt,-85pt) {operational updates common};
  \draw[draw=hdrule] (328pt,-94pt) -- (445pt,-94pt);
  \node[hdscope] at (328pt,-100pt) {broader, more open-ended control};

  \draw[hdflow] (132pt,-58pt) -- (160pt,-58pt);
  \draw[hdflow] (292pt,-58pt) -- (320pt,-58pt);

  \node[anchor=west,font=\fontsize{6.3}{7}\bfseries\selectfont,text=hdaccent] at (0pt,-124pt) {AGENTIC CONTROL};
  \draw[hdflow,line width=1.5pt] (86pt,-124pt) -- (445pt,-124pt);
  \node[anchor=west,font=\fontsize{5.9}{6.5}\selectfont,text=hdmid] at (88pt,-116pt) {action space};
  \node[anchor=center,font=\fontsize{5.9}{6.5}\selectfont,text=hdmid] at (265pt,-116pt) {research horizon};
  \node[anchor=east,font=\fontsize{5.9}{6.5}\selectfont,text=hdmid] at (443pt,-116pt) {orchestration};

  \node[anchor=west,font=\fontsize{6.3}{7}\bfseries\selectfont,text=hdmid] at (0pt,-150pt) {EPISTEMIC CONTROL};
  \draw[draw=hdmuted,line width=0.8pt,dashed,->] (86pt,-150pt) -- (445pt,-150pt);
  \fill[hdpanel,rounded corners=2pt] (278pt,-160pt) rectangle (445pt,-140pt);
  \node[anchor=center,font=\fontsize{6.1}{6.8}\bfseries\selectfont,text=hdmid] at (361.5pt,-150pt) {explicit evidence $\rightarrow$ claim revision remains uneven};
  \node[anchor=center,font=\fontsize{6.4}{7}\bfseries\itshape\selectfont,text=hdmid] at (226.5pt,-174pt) {Framework scale increases what can be done; it does not determine what evidence changes.};
\end{tikzpicture}
\endgroup
\caption{Historical design transition in what is placed under machine control. The phases are analytic rather than genealogical: early discovery systems manipulated explicit scientific objects in narrow domains; language-model reasoning and tool use broadened task handling; and contemporary frameworks broaden research horizon and orchestration. Increased agentic control does not by itself supply explicit evidence-linked revision of represented claims.}
\label{fig:history-transition}
\end{figure*}
"""
    (REVIEW / "fig-history.tex").write_text(tex, encoding="utf-8")


def build_instruments_svg():
    width, height = 906, 390
    columns = ["CLAIM", "METHOD /\nEXECUTION", "EVIDENCE", "EVIDENCE →\nCLAIM", "OUTCOME"]
    rows = [
        ("Outcome benchmark", "scores the endpoint", [0, 0, 0, 0, 2]),
        ("Manuscript / AI review", "reads the reported record", [1, 1, 1, 1, 2]),
        ("Claim-level audit", "checks traceability", [2, 2, 2, 2, 1]),
        ("Interventional test", "perturbs evidence", [1, 0, 2, 2, 1]),
        ("Independent re-test", "re-runs outside the team", [2, 2, 2, 2, 2]),
    ]
    col_x = [286, 424, 562, 700, 838]
    row_y = [132, 181, 230, 279, 328]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="453pt" height="195pt" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="inst-title inst-desc" '
        'font-family="Helvetica, Arial, sans-serif">',
        '<title id="inst-title">Observational coverage of AI Scientist evaluation instruments</title>',
        '<desc id="inst-desc">A matrix shows which parts of the scientific chain are directly targeted, '
        'observed only through a reported artifact, or generally outside scope for five evaluation instruments.</desc>',
        '<rect width="906" height="390" fill="#FFFFFF"/>',
        svg_text(24, 27, "WHY OUTCOME EVALUATION MISSES PROCESS FAILURES", 13, ACCENT, 700),
        svg_text(882, 27, "primary observational target, not a guarantee of correctness", 13, MUTED, 400, "end", True),
        f'<rect x="632" y="48" width="136" height="302" fill="{PALE}"/>',
        f'<line x1="216" y1="99" x2="882" y2="99" stroke="{RULE}" stroke-width="2"/>',
    ]
    for x, label in zip(col_x, columns):
        lines = label.split("\n")
        if len(lines) == 1:
            out.append(svg_text(x, 79, lines[0], 12.5, MID, 700, "middle"))
        else:
            out.append(svg_text(x, 69, lines[0], 12, MID, 700, "middle"))
            out.append(svg_text(x, 84, lines[1], 12, MID, 700, "middle"))
    for index, ((label, gloss, cells), y) in enumerate(zip(rows, row_y)):
        if index % 2 == 0:
            out.append(f'<rect x="20" y="{y - 24}" width="862" height="48" rx="4" fill="{ALT}"/>')
        out.append(svg_text(30, y - 2, label, 14, INK, 700))
        out.append(svg_text(30, y + 16, gloss, 12, MUTED, 400))
        for x, cell in zip(col_x, cells):
            if cell == 2:
                out.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{ACCENT}"/>')
            elif cell == 1:
                out.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#FFFFFF" stroke="{MUTED}" stroke-width="2"/>')
            else:
                out.append(f'<line x1="{x - 8}" y1="{y}" x2="{x + 8}" y2="{y}" stroke="{RULE}" stroke-width="2"/>')
        out.append(f'<line x1="20" y1="{y + 24}" x2="882" y2="{y + 24}" stroke="{RULE}"/>')
    out.extend([
        f'<circle cx="32" cy="372" r="6" fill="{ACCENT}"/>', svg_text(45, 376, "direct target", 12, MID, 500),
        f'<circle cx="168" cy="372" r="6" fill="#FFFFFF" stroke="{MUTED}" stroke-width="2"/>', svg_text(181, 376, "reported or indirect", 12, MID, 500),
        f'<line x1="354" y1="372" x2="366" y2="372" stroke="{RULE}" stroke-width="2"/>', svg_text(378, 376, "generally outside scope", 12, MID, 500),
        svg_text(882, 376, "coverage varies by implementation", 12, MUTED, 400, "end", True),
        "</svg>",
    ])
    (HERE / "ai-scientist-evaluation-instruments.svg").write_text("\n".join(out) + "\n", encoding="utf-8")


def build_instruments_tex():
    columns = [(143, "CLAIM"), (212, "METHOD /\\\\[-1pt]EXECUTION"), (281, "EVIDENCE"),
               (350, "EVIDENCE $\\rightarrow$\\\\[-1pt]CLAIM"), (419, "OUTCOME")]
    rows = [
        ("Outcome benchmark", "scores the endpoint", [0, 0, 0, 0, 2]),
        ("Manuscript / AI review", "reads the reported record", [1, 1, 1, 1, 2]),
        ("Claim-level audit", "checks traceability", [2, 2, 2, 2, 1]),
        ("Interventional test", "perturbs evidence", [1, 0, 2, 2, 1]),
        ("Independent re-test", "re-runs outside the team", [2, 2, 2, 2, 2]),
    ]
    row_y = [-54, -78, -102, -126, -150]
    marks = []
    for row_index, ((label, gloss, cells), y) in enumerate(zip(rows, row_y)):
        if row_index % 2 == 0:
            marks.append(rf"  \fill[evalt] (0pt,{y + 12:.1f}pt) rectangle (453pt,{y - 12:.1f}pt);")
        marks.append(rf"  \node[evrow] at (5pt,{y - 1:.1f}pt) {{{label}}};")
        marks.append(rf"  \node[evgloss] at (5pt,{y - 9:.1f}pt) {{{gloss}}};")
        for (x, _), cell in zip(columns, cells):
            if cell == 2:
                marks.append(rf"  \fill[evacc] ({x}pt,{y:.1f}pt) circle (3.8pt);")
            elif cell == 1:
                marks.append(rf"  \draw[draw=evmuted,line width=0.8pt] ({x}pt,{y:.1f}pt) circle (3.8pt);")
            else:
                marks.append(rf"  \draw[draw=evrule,line width=0.8pt] ({x - 4}pt,{y:.1f}pt) -- ({x + 4}pt,{y:.1f}pt);")
        marks.append(rf"  \draw[draw=evrule,line width=0.35pt] (0pt,{y - 12:.1f}pt) -- (453pt,{y - 12:.1f}pt);")
    headers = [rf"  \node[evhead] at ({x}pt,-29pt) {{{label}}};" for x, label in columns]
    tex = rf"""% Generated by assets/build_review_figures.py -- do not edit by hand.
\begin{{figure*}}[t]
\centering
\begingroup
\definecolor{{evink}}{{HTML}}{{172033}}
\definecolor{{evmid}}{{HTML}}{{526076}}
\definecolor{{evmuted}}{{HTML}}{{768399}}
\definecolor{{evrule}}{{HTML}}{{D7DEE9}}
\definecolor{{evalt}}{{HTML}}{{FAFBFD}}
\definecolor{{evpale}}{{HTML}}{{EAF1FA}}
\definecolor{{evacc}}{{HTML}}{{245EA8}}
\tikzset{{
  evhead/.style={{anchor=center,align=center,font=\fontsize{{6.2}}{{6.8}}\bfseries\selectfont,text=evmid}},
  evrow/.style={{anchor=west,font=\fontsize{{6.8}}{{7.4}}\bfseries\selectfont,text=evink}},
  evgloss/.style={{anchor=west,font=\fontsize{{5.9}}{{6.5}}\selectfont,text=evmuted}}
}}
\begin{{tikzpicture}}[x=1pt,y=1pt]
  \node[anchor=west,font=\fontsize{{6.6}}{{7.2}}\bfseries\selectfont,text=evacc] at (0pt,0pt) {{WHY OUTCOME EVALUATION MISSES PROCESS FAILURES}};
  \node[anchor=east,font=\fontsize{{6.2}}{{6.8}}\itshape\selectfont,text=evmuted] at (453pt,0pt) {{primary target, not a guarantee of correctness}};
  \fill[evpale] (316pt,-18pt) rectangle (384pt,-162pt);
{chr(10).join(headers)}
  \draw[draw=evrule,line width=0.7pt] (108pt,-42pt) -- (453pt,-42pt);
{chr(10).join(marks)}
  \fill[evacc] (7pt,-179pt) circle (3pt);
  \node[anchor=west,font=\fontsize{{6}}{{6.6}}\selectfont,text=evmid] at (14pt,-179pt) {{direct target}};
  \draw[draw=evmuted,line width=0.7pt] (80pt,-179pt) circle (3pt);
  \node[anchor=west,font=\fontsize{{6}}{{6.6}}\selectfont,text=evmid] at (87pt,-179pt) {{reported or indirect}};
  \draw[draw=evrule,line width=0.8pt] (181pt,-179pt) -- (189pt,-179pt);
  \node[anchor=west,font=\fontsize{{6}}{{6.6}}\selectfont,text=evmid] at (195pt,-179pt) {{generally outside scope}};
  \node[anchor=east,font=\fontsize{{5.9}}{{6.5}}\itshape\selectfont,text=evmuted] at (453pt,-179pt) {{coverage varies by implementation}};
\end{{tikzpicture}}
\endgroup
\caption{{Schematic observational coverage of common AI Scientist evaluation instruments. Filled markers indicate the part of the research chain directly targeted, open markers indicate access through a reported artefact or another indirect signal, and dashes indicate that the element is generally outside the instrument's scope. Coverage does not guarantee correctness, and the scope of an independent re-test still depends on what is repeated.}}
\label{{fig:evaluation-instruments}}
\end{{figure*}}
"""
    (REVIEW / "fig-instruments.tex").write_text(tex, encoding="utf-8")


def main():
    build_landscape_svg()
    build_loop_svg()
    build_landscape_tex()
    build_loop_tex()
    build_history_svg()
    build_history_tex()
    build_instruments_svg()
    build_instruments_tex()
    print("wrote assets/ai-scientist-landscape-review.svg")
    print("wrote assets/ai-scientist-overview.svg")
    print("wrote assets/ai-scientist-historical-transition.svg")
    print("wrote assets/ai-scientist-evaluation-instruments.svg")
    print("wrote fig-landscape.tex")
    print("wrote fig-loop.tex")
    print("wrote fig-history.tex")
    print("wrote fig-instruments.tex")


if __name__ == "__main__":
    main()
