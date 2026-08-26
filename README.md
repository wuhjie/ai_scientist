# AI Scientist Review

A critical review and verified catalogue of **LLM-based systems for autonomous and semi-autonomous scientific discovery** — AI Scientists, scientific agents, self-driving labs — organised around one question: **what has actually been verified, and who verified it?** Includes the reasoning, verification and evaluation literature these systems depend on.

**Venues last verified: 29 July 2026.** Venues are re-verified on each such update; see [Verification policy](#verification-policy). That refresh moved HoneyComb and AstaBench out of `[preprint]`, added a *Checked by* axis to [§3](#3-systems-at-a-glance), added the process-supervision and citation-verification work in [§4](#4-reasoning--verification-substrate)–[§5](#5-evidence-attribution--claim-verification), and added a [structural analysis](#structural-analysis-of-a-15-system-subset) of a 15-system subset coded from the papers themselves.

*Framing and denominators revised 13 August 2026. No venue re-check was performed on that date, so every `[preprint]` tag still dates from 29 July.*

> **Why another list?** Most repos in this space link to preprints that have since been peer-reviewed, and organise purely by application domain. This one tracks **canonical venues** (a large fraction of this field's headline systems are now in *Nature*, *Science* or *Nature Machine Intelligence*, not on arXiv), records **who performed each validation** rather than only whether one happened, and adds three sections that domain-organised lists usually omit: the **pre-LLM discovery systems**, the **reasoning/verification substrate**, and the **critical evaluations** of AI Scientists.

---

## The field at a glance

![Landscape of AI-enabled scientific-discovery systems — four classical discovery programmes and two foundational publications above an era break, then 27 contemporary systems in seven application-area panels, each card recording autonomy, experiment executor and evidence type; benchmarks and agenda papers held in a separate non-system panel](assets/ai-scientist-landscape.svg)

Sections [1](#1-classical-foundations-pre-llm)–[3](#3-systems-at-a-glance) as one picture. Regenerate with `python3 assets/make_landscape.py`.

**Panels are categories, not lineages.** Position, column and adjacency carry no claim of descent. Cards are ordered by year within a panel, ties alphabetical.

**Each card carries three fields** rather than a single validation mark: *autonomy* — degree of independent loop execution; *executor* — who or what performed the experiment or evaluation; *evidence* — the strongest reported validation type. Autonomy reads `not assessed` where this review has not classified it, which is the case for 11 of the 27 contemporary systems.

**Relations are drawn in three weights, each labelled.** Solid for a link the authors themselves state — Adam → *The Automation of Science*, and AlphaEvolve generalising FunSearch. Dashed for a documented citation — DENDRAL and *Scientific Discovery* → Adam. Dotted for a conceptual resemblance with no citation established — BACON and KEKADA → Adam. Nothing else is connected.

**Non-system entries are held separate.** The *Cell* agenda paper and MLE-bench sit in their own panel and are excluded from every system ratio, the same rule [§3](#3-systems-at-a-glance) applies. The figure holds 27 contemporary systems, 4 classical systems, 2 non-system entries and 2 foundational publications.

The figure’s panels differ from [§2](#2-systems-by-subfield)’s subfield tables in three places: PaperQA2 sits under literature and evidence synthesis rather than biology, LLM-SR under program and equation discovery rather than chemistry/materials, and the agenda paper and benchmark are held out as non-system entries.

---

## Contents

- [AI Scientist Review](#ai-scientist-review)
  - [The field at a glance](#the-field-at-a-glance)
  - [Contents](#contents)
  - [How to read this review](#how-to-read-this-review)
  - [1. Classical foundations (pre-LLM)](#1-classical-foundations-pre-llm)
  - [2. Systems by subfield](#2-systems-by-subfield)
    - [General / cross-domain frameworks](#general--cross-domain-frameworks)
    - [Biology / life sciences](#biology--life-sciences)
    - [Lab automation / self-driving labs (LLM-driven)](#lab-automation--self-driving-labs-llm-driven)
    - [ML / CS self-research](#ml--cs-self-research)
    - [Chemistry / materials](#chemistry--materials)
  - [3. Systems at a glance](#3-systems-at-a-glance)
    - [Structural analysis of a 15-system subset](#structural-analysis-of-a-15-system-subset)
  - [4. Reasoning \& verification substrate](#4-reasoning--verification-substrate)
  - [5. Evidence, attribution \& claim verification](#5-evidence-attribution--claim-verification)
  - [6. Critical evaluations \& audits](#6-critical-evaluations--audits)
    - [How much of this has been independently re-tested?](#how-much-of-this-has-been-independently-re-tested)
  - [7. Benchmarks](#7-benchmarks)
  - [8. Surveys \& agenda papers](#8-surveys--agenda-papers)
  - [Verification policy](#verification-policy)
    - [Contributing](#contributing)

---

## How to read this review

Section 2 organises systems by **application domain**, which is how most people search. Section 3 re-cuts the same systems along four **cross-cutting axes** that domain tables hide:

| Axis | Question | Values used here |
|---|---|---|
| **Hypothesis representation** | What kind of object is the hypothesis? | `free text` · `program` · `structured state` · `logical` |
| **Loop closure** | What decides whether a hypothesis survives? | `self-critique` · `debate/tournament` · `execution` · `statistical` · `wet lab` · `formal` |
| **Validation** | Was anything checked outside the model? | `none` · `benchmark` · `leaderboard` · `in vitro` · `physical synthesis` |
| **Checked by** | *Who* performed that check? | `authors` · `collaborating labs` · `external leaderboard` · `third party` |

Two systems in different domains that share a row in Section 3 are usually more alike than two systems in the same domain that don't.

**Status tags.** `[preprint]` = no peer-reviewed version found as of the last update. `[blog]` = company/lab post only. `‡` = acceptance recorded from the authors' own arXiv statement and not yet confirmed against a proceedings index; the KDD 2026 AI4Science track admits both archival full papers and **non-archival extended abstracts**, and which category applies has not been determined. Untagged, bolded entries carry a venue verified against a publisher page, PubMed or an official proceedings index.

---

## 1. Classical foundations (pre-LLM)

Included because these systems had **explicit hypothesis representations and explicit refutation semantics** — the capabilities the LLM-agent generation has not yet recovered. Frequently omitted from modern surveys; useful context for anyone working on hypothesis representation or belief revision.

| System | Year / venue | Contribution |
|---|---|---|
| **DENDRAL** | 1965– | Constrained molecular-structure hypotheses by mass-spectral fragmentation rules. Made genuine (not merely re-) discoveries |
| **BACON** | Langley et al., 1981 | Heuristic search for functional relations over observed variables; rediscovered Kepler's third law |
| **KEKADA** | Kulkarni & Simon, 1988 | **Anomaly-driven discovery** — detects surprise, forms explanations, runs experiments; modelled on Krebs' urea-cycle notebooks |
| **Robot Scientist "Adam"** | [*Nature* 427:247–252 (2004)](https://www.nature.com/articles/nature02236) | First machine to autonomously discover novel scientific knowledge. Logical hypotheses + **cost-optimal discriminating experiment selection** + physical lab automation, on yeast gene function |
| **"The Automation of Science"** | King et al., *Science* 324:85–89 (2009) | The Adam/Eve programme stated as a general position |
| **Scientific Discovery: Computational Explorations of the Creative Process** | Langley, Simon, Bradshaw & Żytkow (MIT Press) | The canonical text of this era |

---

## 2. Systems by subfield

### General / cross-domain frameworks

**Core problem:** end-to-end ideation → experiment → writing; how to evaluate it.
**Approaches:** tree-search agents · multi-agent debate · world model + long-horizon memory.

| System | Venue | Notes |
|---|---|---|
| [**The AI Scientist**](https://www.nature.com/articles/s41586-026-10265-5) (Sakana) | ***Nature* 651:914–919 (2026)** | "Towards end-to-end automation of AI research." Ideation → code → experiments → manuscript → automated review. A generated manuscript passed first-round review at an ICLR 2025 workshop (score 6.33; **the paper notes the workshop's acceptance rate was 70% vs 32% for the main conference**). System reports also at [arXiv 2408.06292](https://arxiv.org/abs/2408.06292) (v1) / [2504.08066](https://arxiv.org/abs/2504.08066) (v2, agentic tree search) |
| [**Co-Scientist**](https://www.nature.com/articles/s41586-026-10644-y) (Google) | ***Nature* 655:487–496 (2026)** | "Generate, debate, evolve." Supervisor + six specialist agents (Generation, Reflection, Ranking, Proximity, Evolution, Meta-review); Elo tournament over hypotheses. Three wet-lab validations, incl. independently recapitulating an unpublished AMR mechanism |
| [**ERA**](https://www.nature.com/articles/s41586-026-10658-6) (Google DeepMind) | ***Nature* 654:909–916 (2026)** | LLM + tree search over code against a scorable metric. Found **40 new single-cell analysis methods** beating the best human leaderboard entries; beat the official CovidHub COVID-19 hospitalisation ensemble |
| [**Kosmos**](https://arxiv.org/abs/2511.02824) (Edison Scientific) | `[preprint]` | Structured **world model** (entities, relations, results, open questions) as long-term memory; ~12-hour campaigns, ~200 rollouts, ~1,500 papers read. Commercial/closed |
| [**Agent Laboratory**](https://arxiv.org/abs/2501.04227) (AMD/JHU) | `[preprint]` | Multi-agent role-play across the research pipeline |
| [**SCION**](https://arxiv.org/abs/2607.03863) | `[preprint]` | *Scientific Collaborative Innovation with Agentic Organizational Nexus.* Compiles intent into a **Research Execution Plan** — staged objectives, dependencies, verification checkpoints, expected artifacts, fallback conditions — over a hierarchical runtime with layered epistemic memory; specialist subagents' noisy local traces are normalised before reintegration |
| [**Agon**](https://arxiv.org/abs/2606.24177) | `[preprint]` | Large-scale omnidisciplinary autonomous research system organised around a "prompt economy" |

**Open problems:** novelty assessment · reward hacking · disclosure & authorship ethics · denominator reporting (hit rates are usually given for selected hypotheses only).

---

### Biology / life sciences

**Core problem:** autonomous drug discovery, protein design, gene editing, literature synthesis.
**Approaches:** literature RAG agents · multi-agent virtual labs · protocol-planning agents · generalist tool-using bio agents.

| System | Venue | Notes |
|---|---|---|
| [**Biomni**](https://www.science.org/doi/10.1126/science.adz4351) (Stanford) | ***Science* (2026)**, doi 10.1126/science.adz4351 | "Autonomous biomedical research with an artificial intelligence agent." Generalist agent; an **action-discovery agent** mines tools/databases/protocols from literature across 25 domains. 400+ tasks; matches senior-scientist level on rare-disease diagnosis, disease-gene ID, drug repurposing. Preprint: [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1) |
| [**Robin**](https://www.nature.com/articles/s41586-026-10652-y) (FutureHouse) | ***Nature* 655:497–505 (2026)** | Literature agent ↔ data-analysis agent with an **explicit hypothesis-update step**. Proposed enhancing RPE phagocytosis for dry AMD; identified and confirmed *in vitro* efficacy of **ripasudil** and **KL001** |
| [**Virtual Lab**](https://www.nature.com/articles/s41586-025-09442-9) (Stanford) | ***Nature* (2025)** | LLM PI agent recruits specialist agents + a Scientific Critic; structured research meetings. Built an ESM → AlphaFold-Multimer → Rosetta pipeline; **92 nanobodies experimentally validated** against SARS-CoV-2 variants |
| [**CRISPR-GPT**](https://www.nature.com/articles/s41551-025-01463-z) (Stanford) | ***Nature Biomedical Engineering* 10(2):245–258 (2026)** | Task-decomposed multi-agent system for gene-editing design. Enabled novices to complete lung-cancer knockouts and melanoma epigenetic activation |
| [**PaperQA2**](https://arxiv.org/abs/2409.13740) (FutureHouse) | `[preprint]` | RAG agent over the literature with citation-graph traversal; reports superhuman literature retrieval and ~2.34 contradictions/paper detected in biology (70% validated) |
| [**Empowering biomedical discovery with AI agents**](https://pubmed.ncbi.nlm.nih.gov/39486399/) (Zitnik lab) | ***Cell* (2024)** | Agenda paper; autonomy-level taxonomy for biomedical agents; frames "AI scientists" as systems capable of *skeptical* reasoning |

**Open problems:** wet-lab loop cost · medical hallucination · causal vs correlational claims · calibration and abstention when the answer is unknown · fidelity of automatically-mined tools.

---

### Lab automation / self-driving labs (LLM-driven)

**Core problem:** LLM agents driving real hardware for autonomous synthesis and characterisation.
**Approaches:** LLM-programmed synthesis robots · mobile robotic chemists · LLM-orchestrated SDLs.

| System | Venue | Notes |
|---|---|---|
| [**Coscientist**](https://www.nature.com/articles/s41586-023-06792-0) (CMU) | ***Nature* 624:570–578 (2023)** | GPT-4 planner + web/docs search, code execution, liquid handler. Autonomous optimisation of Pd-catalysed cross-couplings |
| [**A-Lab**](https://www.nature.com/articles/s41586-023-06734-w) (LBNL/DeepMind) | ***Nature* (2023)** | Robotic synthesis + XRD + active recipe selection from DFT-predicted targets. ⚠️ Characterisation contested — see [§6](#6-critical-evaluations--audits) |
| [**RoboChem**](https://www.science.org/doi/10.1126/science.adj1817) (Noël, UvA) | ***Science* (2024)** | Closed-loop Bayesian optimisation of flow photocatalysis with in-line benchtop NMR |
| [**Autonomous mobile robots**](https://www.nature.com/articles/s41586-024-08173-7) (Cooper, Liverpool) | ***Nature* (2024)** | Mobile robot arms doing exploratory synthetic chemistry: combinatorial synthesis, supramolecular materials, photocatalyst screening |

**Open problems:** hardware portability · failure recovery · safety & cost · **automation of interpretation** (the A-Lab dispute is about inference from measurement, not about execution).

---

### ML / CS self-research

**Core problem:** AI doing ML research end-to-end (read → ideate → code → run → write).
**Approaches:** tree-search code agents · evolutionary code agents · multi-agent role-play.

| System | Venue | Notes |
|---|---|---|
| [**FunSearch**](https://www.nature.com/articles/s41586-023-06924-6) (DeepMind) | ***Nature* 625 (2024)** | LLM proposes *programs*; automated evaluator scores; evolutionary search. New cap-set constructions and improved bin-packing heuristics. The canonical "untrusted proposer + sound verifier" design |
| [**AlphaEvolve**](https://arxiv.org/abs/2506.13131) (DeepMind) | `[preprint]` | Extends FunSearch to whole codebases, any language, multi-objective |
| [**MLE-bench**](https://openreview.net/forum?id=6s5uXNWGIh) (OpenAI) | **ICLR 2025 (Oral)** | 75 Kaggle competitions; best setup reached bronze-medal level in 16.9% |
| [**AIDE**](https://arxiv.org/abs/2502.13138) (Weco) | `[preprint]` | ML engineering as tree search in the space of code |
| [**MLE-STAR**](https://arxiv.org/abs/2506.15692) (Google) | `[preprint]` | Search-and-refine ML engineering agent |
| [**Zochi**](https://www.intology.ai/blog/zochi-acl) (Intology) | `[blog]` | Claimed autonomously-produced ACL-accepted work |

**Open problems:** benchmark contamination · reward hacking · long-horizon gap vs humans · distinguishing genuine method discovery from leaderboard overfitting.

---

### Chemistry / materials

**Core problem:** autonomous synthesis planning, materials discovery, reaction optimisation.
**Approaches:** tool-augmented chemistry LLMs · multi-agent KG reasoning · self-reflective DFT-in-the-loop agents.

| System | Venue | Notes |
|---|---|---|
| [**ChemCrow**](https://www.nature.com/articles/s42256-024-00832-8) (EPFL) | ***Nature Machine Intelligence* 6 (2024)** | GPT-4 + 18 expert-designed chemistry tools; autonomously planned and executed syntheses of DEET and three organocatalysts |
| [**ChemAgents**](https://pubs.acs.org/doi/10.1021/jacs.4c17738) (USTC) | ***JACS* 147(15):12534–12545 (2025)** | Hierarchical multi-agent robotic AI chemist on an on-board Llama-3.1-70B: Task Manager + Literature Reader, Experiment Designer, Computation Performer, Robot Operator |
| [**SciAgents**](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adma.202413523) (MIT) | ***Advanced Materials* (2025)** | Ontological knowledge graphs + multi-agent generation and critique for bioinspired materials |
| [**LLM-SR**](https://proceedings.iclr.cc/paper_files/paper/2025/hash/28df8e730c054c5331855fd4d5403ba9-Abstract-Conference.html) | **ICLR 2025 (Oral)** | Equations as **program skeletons**; LLM priors + evolutionary search. Strong out-of-domain generalisation vs symbolic-regression baselines |
| [**HoneyComb**](https://aclanthology.org/2024.findings-emnlp.192/) | **Findings of EMNLP 2024** | MatSciKB curated knowledge base + ToolHub inductive tool construction + adaptive retriever selecting knowledge source or tool per task |
| [**LLMatDesign**](https://arxiv.org/abs/2406.13163) | `[preprint]` | Self-reflective LLM agent for materials design |

**Open problems:** novelty definition · predicted ≠ synthesizable · SDL integration · evaluator soundness outside optimisation-shaped tasks.

---

## 3. Systems at a glance

The same systems, re-cut along the axes from [How to read this review](#how-to-read-this-review).

**What this table's 27 rows are.** [§2](#2-systems-by-subfield) lists **29 entries**. Two are excluded here because neither is a discovery system — the agenda paper *Empowering biomedical discovery* and the MLE-bench benchmark — leaving **27 discovery systems**. **Agon** is dropped from those, its public record being too thin to code, and **Robot Scientist Adam** is carried down from [§1](#1-classical-foundations-pre-llm) as the pre-LLM reference point. So this table's 27 rows and §2's 27 discovery systems have the same size and are **not the same set**.

**"Checked by" is the axis most often collapsed.** *Validation* records what kind of check was performed; *Checked by* records who performed it. A wet-lab result produced by the authors' own laboratory and a score on a leaderboard maintained by a third party are both "validated" in most tables, and they are not the same evidence. Where a coding is not supported by the cited record, the cell reads `not reported` rather than being inferred.

| System | Venue | Hypothesis repr. | Loop closure | Validation | Checked by |
|---|---|---|---|---|---|
| Robot Scientist Adam | *Nature* '04 | logical | formal + wet lab | physical, autonomous | authors |
| FunSearch | *Nature* '24 | program | execution | benchmark (open problems) | authors; evaluator is public and sound |
| AlphaEvolve | `[preprint]` | program | execution | benchmark | authors |
| LLM-SR | ICLR '25 | program | execution | held-out / OOD data | authors |
| ERA | *Nature* '26 | program | execution | **public leaderboard** | **external leaderboard** |
| AI Scientist | *Nature* '26 | free text | execution + self-critique | benchmark; workshop review | workshop reviewers; **third party — v1 evaluated adversely** ([§6](#6-critical-evaluations--audits)) |
| Co-Scientist | *Nature* '26 | free text (ranked population) | debate/tournament | in vitro | collaborating labs |
| Kosmos | `[preprint]` | structured state | execution + citation | partial | **third party — 1 of 3 hypotheses upheld** ([§6](#6-critical-evaluations--audits)) |
| Virtual Lab | *Nature* '25 | free text (meetings) | debate → execution | **in vitro** (92 nanobodies) | authors |
| Robin | *Nature* '26 | free text (+ update step) | execution → wet lab | **in vitro** (ripasudil, KL001) | authors |
| Coscientist | *Nature* '23 | free text | execution → robot | **physical synthesis** | authors |
| A-Lab | *Nature* '23 | program-ish (recipes) | robot + XRD | physical synthesis | authors; **contested by third party** ([§6](#6-critical-evaluations--audits)) |
| CRISPR-GPT | *Nat. BME* '26 | task state machine | tool output → wet lab | **in vitro** (knockouts) | authors |
| Biomni | *Science* '26 | free text | execution | benchmark (400+ tasks) | authors |
| ChemCrow | *NMI* '24 | free text | execution → robot | physical synthesis (small) | authors |
| ChemAgents | *JACS* '25 | free text (role-decomposed) | execution → robot | physical synthesis | authors |
| RoboChem | *Science* '24 | structured state (reaction params) | Bayesian opt → robot + in-line NMR | **physical synthesis** | authors |
| Autonomous mobile robots | *Nature* '24 | free text → workflow | execution → robot | **physical synthesis** | authors |
| SciAgents | *Adv. Mater.* '25 | structured state (knowledge graph) | debate / critique | not reported | — |
| HoneyComb | *Findings EMNLP* '24 | free text | execution (tools) | benchmark | authors |
| AIDE | `[preprint]` | program | execution | benchmark | authors |
| MLE-STAR | `[preprint]` | program | execution | benchmark | authors |
| Agent Laboratory | `[preprint]` | free text (role-play) | self-critique | not reported | — |
| SCION | `[preprint]` | structured state (Research Execution Plan) | execution + verification checkpoints | not reported | — |
| LLMatDesign | `[preprint]` | structured state | execution (self-reflective loop) | not reported | — |
| PaperQA2 | `[preprint]` | n/a (retrieval) | citation check | benchmark | authors |
| Zochi | `[blog]` | free text | execution + self-critique | venue review (claimed) | — |

### Structural analysis of a 15-system subset

A separate pass coded 15 of these systems **field by field from the papers themselves** — 6 read in full text, 9 from abstracts only — along the axes above plus reasoning strategy, belief revision and human involvement.

> ⚠️ **This subset is neither the 27 systems catalogued in [§2](#2-systems-by-subfield) nor the 27 rows coded in [§3](#3-systems-at-a-glance).** It is 15 systems selected by what could be read, not by any inclusion rule. Its counts are not meant to reconcile with the counts elsewhere in this file.

**Independent verification is rare.** Who performed the check, across the 15:

| Checked by | Systems |
|---|---|
| An unconnected third party | **2** |
| Collaborating labs | 1 |
| The authors themselves | 4 |
| Not stated | **8** |

**Mechanism is reported less often than contribution.** All 15 state their contribution and their domain. Among the 6 read in full there are only **3 omissions across 66 coded fields**, so the fall-off on the mechanism fields is mostly what an abstract cannot tell you rather than what an author withheld. Hypothesis representation was recoverable in **6 of 6** full-text papers and **2 of 9** abstracts — the single sharpest difference between the two groups.

**Design choices form implication chains rather than correlations.** Every system whose hypothesis is a program verifies by execution (4/4) — but that is *definitional*, since a program-as-hypothesis is the artifact executed, and it should not be read as a finding. The empirical counterpart is wet lab → partial human involvement (4/4): in this subset every wet-lab experiment was human-executed. Programs, meanwhile, never co-occur with human review, LLM-as-judge, wet lab or partial human involvement. Association measures (lift, PMI) are deliberately not reported: at n=15 they are dominated by single coding decisions.

**Three caveats bound every number above.**

- The subset **under-samples wet-lab systems**: 27% of coded rows reach physical or *in vitro* validation, against 54% of the systems that could not be read. Execution-based verification is over-represented by construction.
- **Empty cells are not evidence of absence.** `logical` representation appears in 0 of the 8 rows where representation could be coded — but Adam, the one logical-representation system here, is among those that could not be read. That zero measures access, not design.
- **Single coder, no reliability estimate.** These codings have not been double-coded and no agreement statistic is reported. Treat them as a structured reading, not as a measurement.

---

## 4. Reasoning & verification substrate

What AI Scientists are built out of. Rarely included in domain-organised surveys, but it determines what these systems can and cannot establish.

| Paper | Venue | Why it matters here |
|---|---|---|
| [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html) | **ICLR 2024** | Process supervision > outcome supervision; PRM800K (800k step-level labels). No dataset of comparable scale exists for scientific reasoning; the 2026 entries below are the first attempts to define a scientific step label |
| [LLMs Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) | **ICLR 2024** | Intrinsic self-correction without external feedback fails. Relevant to every "reflection agent" in §2 |
| [Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html) | **NeurIPS 2023** | CoT systematically misrepresents the causes of model outputs; biasing features go unmentioned |
| [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) | `[preprint]` | Reasoning models verbalise decisive hints in <20% of cases; outcome-based RL improves faithfulness only to a plateau |
| [Faithful Chain-of-Thought Reasoning](https://aclanthology.org/2023.ijcnlp-main.20/) | **IJCNLP-AACL 2023** | Faithfulness *by construction*: emit a symbolic plan, execute it deterministically |
| [DeepSeek-R1](https://www.nature.com/articles/s41586-025-09422-z) | ***Nature* (2025)** | Reasoning incentivised by RL against **verifiable** rewards. Defines the field's dominant recipe — and its limit: open scientific claims have no verifier |
| [MOOSE-Chem](https://openreview.net/forum?id=IDDE01WDeN) | **ICLR 2025** | Rediscovery-under-cutoff evaluation: recover 2024 *Nature*-level chemistry hypotheses with a 2023-cutoff model |
| [SciMON](https://aclanthology.org/2024.acl-long.18/) | **ACL 2024** | Novelty-optimised hypothesis generation grounded in retrieved "inspirations" |
| [Sci-PRM](https://arxiv.org/abs/2606.04579) | KDD 2026 (AI4Science) ‡ | Process reward models are established for mathematical reasoning; this targets biology, chemistry and physics. Supervises **tool selection, execution accuracy and result interpretation** at each step of a Chain-of-Tool trajectory, for Best-of-N selection and as a dense RL reward |
| [Rewarding the Scientific Process](https://arxiv.org/abs/2604.24198) | KDD 2026 (AI4Science) ‡ | Process-level reward modelling for agentic data analysis — step-level credit where the outcome alone is uninformative |
| [AutoDiscovery](https://neurips.cc/virtual/2025/poster/116398) | **NeurIPS 2025** | Open-ended discovery driven by **Bayesian surprise** rather than a fixed objective. The closest modern relative of KEKADA's anomaly-triggered mechanism (Agarwal, Majumder, … Clark; AI2) |
| [Are LLM Belief Updates Consistent with Bayes' Theorem?](https://arxiv.org/abs/2507.17951) | ICML 2025 WS (Assessing World Models) | Introduces a Bayesian Coherence Coefficient for in-context credence updates; larger models score higher, but updating remains only approximately Bayesian |

---

## 5. Evidence, attribution & claim verification

| Paper / system | Venue | Contribution |
|---|---|---|
| [SciFact — Fact or Fiction](https://aclanthology.org/2020.emnlp-main.609/) | **EMNLP 2020** | Scientific claim verification with abstract-level evidence **and rationales**; 1.4k expert claims |
| [ALCE — LLMs generate text with citations](https://aclanthology.org/2023.emnlp-main.398/) | **EMNLP 2023** | Automatic **citation precision/recall** metrics — the field's operational definition of attribution |
| [Veritas](https://arxiv.org/abs/2604.12144) | `[preprint]` | Multi-agent clinical co-scientist emitting a fully auditable evidence trail; four-way epistemic labels — **supported / refuted / underpowered / invalid** |
| [StatefulDiscovery](https://arxiv.org/abs/2606.11851) | `[preprint]` | Externalised investigation state coupling frontier selection, evidence acquisition and **claim adjudication** |
| [VeriGraph](https://arxiv.org/abs/2606.16603) | `[preprint]` | Externalises an agent's reasoning into an executable evidence DAG traceable to raw data |
| [CiteAudit](https://arxiv.org/abs/2602.23452) | `[preprint]` | Benchmark for verifying scientific references; decomposes citation checking into claim extraction, evidence retrieval, passage matching, reasoning and calibrated judgment |
| [Cited but Not Verified](https://arxiv.org/abs/2605.06635) | `[preprint]` | Parses and evaluates source attribution in deep-research agents — whether a cited source was read, not merely cited |
| [Evaluating and Guarding Citation Faithfulness](https://arxiv.org/abs/2607.20527) | `[preprint]` | Reports that on **identical** agent outputs the unsupported-citation rate ranges ~3%→~18% depending only on verifier strictness, with negative-specific inter-verifier agreement of 0.27–0.30. Proposes gold-anchored calibration against human annotation plus a split-conformal guard bounding truly-unsupported citations. Evaluated on SciFact, QASA and PubMedQA |

---

## 6. Critical evaluations & audits

The fastest-moving part of this field as of mid-2026, and the least covered by other survey lists. Mostly preprints — that is a fact about the field, not a sourcing gap.

| Study | Venue | Finding |
|---|---|---|
| [AI scientists produce results without reasoning scientifically](https://arxiv.org/abs/2604.18805) | `[preprint]` | **25,000+ agent runs**, 8 domains. Base model explains **41.4%** of performance variance vs **1.5%** for the agent scaffold. Evidence ignored in **68%** of traces; refutation-driven belief revision in **26%**. Ceiling ~90%+ on workflow execution, never above 60% on hypothesis-driven tasks. Annotates traces with six epistemic operations (hypothesis, gather evidence, test prediction, justify, update belief, commit) |
| [The Agentic Garden of Forking Paths](https://arxiv.org/abs/2607.01507) | `[preprint]` | Agents with different personas reach **opposing conclusions from the same data**. 86% of mutually conflicting analyses passed independent AI review; 78% passed majority human-expert review. Introduces the **m-value** and Agentic Bootstrap |
| [Evaluating KOSMOS in radiation biology](https://arxiv.org/abs/2511.13825) | `[preprint]` | Independent test of three Kosmos hypotheses against **random-gene null controls**: one validated, one uncertain, one false (indistinguishable from noise) |
| [Evaluating Sakana's AI Scientist](https://dl.acm.org/doi/10.1145/3769733.3769747) | ***ACM SIGIR Forum* 59(1)**, 2025 — opinion paper | Third-party evaluation (Beel, Kan & Baumgart) of AI Scientist v1: reports a **42% experiment failure rate**, hallucinated results that the system's own automated review did not catch, and many generated ideas judged not genuinely novel. The [arXiv version](https://arxiv.org/abs/2502.14297) carries a different title |
| [Correct Answer, Wrong Mechanism](https://arxiv.org/abs/2606.23175) | **ICML 2026 AI4Science WS (spotlight)** | Agents reach right-looking results via reasoning that breaks under regime shift; one defended a claim with physics inconsistent with its own data. Proposes a two-step mechanism-fidelity check |
| [Can LLMs Generate Novel Research Ideas?](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html) | **ICLR 2025** | 100+ NLP researchers, blind review: LLM ideas judged **more novel** than expert human ideas, slightly less feasible |
| [Agents4Science reflections](https://www.nature.com/articles/s41587-025-02963-8) | ***Nature Biotechnology* (2025)** | First venue requiring AI first-authorship, with LLM reviewers and human spot-checks; public OpenReview record |
| [A-Lab characterisation dispute](https://www.chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article) | news + response | Reanalysis questioned space-group assignments; the lead author conceded a human could produce a higher-quality refinement while defending the demonstration's scope |

### How much of this has been independently re-tested?

Counting only cases where a group **unconnected to the original authors** re-tested or independently evaluated a released system, this review currently finds **three**: the Kosmos radiation-biology evaluation, the A-Lab characterisation reanalysis, and the *SIGIR Forum* evaluation of AI Scientist v1.

In all three the third party's verdict was partly or wholly negative — one of three Kosmos hypotheses upheld, A-Lab's space-group assignments questioned, a 42% experiment failure rate in AI Scientist v1. The *Checked by* column in [§3](#3-systems-at-a-glance) carries these outcomes rather than recording a bare "third party", since an external check is not the same as external corroboration.

Those three re-tests cover three distinct systems — Kosmos, A-Lab and AI Scientist — out of the **27 discovery systems** catalogued in [§2](#2-systems-by-subfield), 17 of which carry a peer-reviewed venue. (§2 lists 29 entries; the agenda paper and MLE-bench are excluded from the denominator because neither is a discovery system — the same rule stated in [§3](#3-systems-at-a-glance).)

This is worth separating from a larger figure often quoted alongside it: several systems report **wet-lab validation**, but in the published record those experiments were run by the authors or their collaborators — Co-Scientist's three validations in partner labs, Virtual Lab's 92 nanobodies, Robin's *ripasudil*/KL001 assays, CRISPR-GPT's knockouts. That is author-side validation, which is a different evidential category from third-party replication. ERA is the closest thing to an external check by construction, since a public leaderboard is scored by someone else against a pre-existing standard.

This is a count of what the sources record, not a claim that the remainder are wrong. Corrections are welcome — see [Contributing](#contributing).

---

## 7. Benchmarks

| Benchmark | Venue | Domain | Scope |
|---|---|---|---|
| [ScienceAgentBench](https://openreview.net/forum?id=6z4YKr0GK6) | **ICLR 2025** | Cross-domain | 102 tasks from 44 peer-reviewed papers, 9 expert validators; output unified to a self-contained Python file |
| DiscoveryBench | **ICLR 2025** | Data-driven discovery | 264 real tasks, 6 domains; best system ~25% |
| [MLE-bench](https://openreview.net/forum?id=6s5uXNWGIh) | **ICLR 2025 (Oral)** | ML engineering | 75 Kaggle competitions vs human leaderboards |
| [SciCode](https://openreview.net/forum?id=ADLaALtdoG) | **NeurIPS 2024 D&B** | Research coding | 80 main / 338 sub-problems across 16 subfields; o1-preview solved 7.7% |
| [PaperBench](https://proceedings.mlr.press/v267/starace25a.html) | **ICML 2025** | Replication | Replicate 20 ICML 2024 Spotlight/Oral papers; 8,316 gradable sub-tasks; best agent 21.0% |
| [ChemBench](https://www.nature.com/articles/s41557-025-01815-x) | ***Nature Chemistry* (2025)** | Chemistry | 2,788 Q–A pairs; best models beat the best human chemists on average but are overconfident |
| [AstaBench](https://openreview.net/forum?id=M7TNf5J26u) | **ICLR 2026 (Oral)** | Cross-domain | 2,400+ problems, 57 agents / 22 classes evaluated; production-grade search tools for controlled comparison and explicit cost accounting |
| [LAB-Bench](https://arxiv.org/abs/2407.10362) | `[preprint]` | Biology | 2,457 questions across 8 categories (LitQA2, SeqQA, ProtocolQA, …) |
| [BixBench](https://arxiv.org/abs/2503.00096) | `[preprint]` | Computational biology | 53 real scenarios, 296 open-answer questions; frontier models ~17% |
| RE-Bench (METR) | `[preprint]` | ML research | Human-vs-agent research engineering |
| [ReplicatorBench](https://arxiv.org/abs/2602.11354) | KDD 2026 (AI4Sciences) ‡ | Replicability | Agents attempting to replicate findings in the social and behavioural sciences — replication as the task, not as an afterthought |
| [Act As a Real Researcher](https://arxiv.org/abs/2606.07462) | `[preprint]` | Research lifecycle | Benchmark suite across the lifecycle; its stated motivation is that methodological rigour, uncertainty awareness and scientific judgement are largely unmeasured by existing suites |
| [AutoResearchBench](https://arxiv.org/abs/2604.25256) | `[preprint]` | Literature discovery | Agents on complex scientific literature discovery |
| MedAgentBench | `[preprint]` | Medical agents | — |
| MaScQA / MatBench | — | Materials | Weak proxies for discovery ability |

> **Caveat worth stating.** Almost every benchmark above scores **outcomes**. The audits in §6 find that outcome metrics do not detect epistemic failures — agents reaching right answers through reasoning that would not generalise. As of this update the first process-level alternatives have appeared (Sci-PRM and the process-reward work in §4; *Act As a Real Researcher* above), but none is yet widely adopted, and none has been used to re-score the systems in §2.

---

## 8. Surveys & agenda papers

| Survey | Venue | Angle |
|---|---|---|
| [From Automation to Autonomy: LLMs in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895/) | **EMNLP 2025** | Autonomy-level taxonomy (LLM as Tool / Analyst / Scientist). Peer-reviewed |
| [Empowering biomedical discovery with AI agents](https://pubmed.ncbi.nlm.nih.gov/39486399/) | ***Cell* (2024)** | Biomedical agenda; levels of autonomy for bio agents |
| [Towards Scientific Intelligence: LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047) | `[preprint]` | Mechanism-centric: planners, memory, action space, **verifiers** |
| [Agentic AI for Scientific Discovery](https://arxiv.org/abs/2503.08979) | `[preprint]` | Progress, challenges, future directions |
| [From AI for Science to Agentic Science](https://arxiv.org/abs/2508.14111) | `[preprint]` | Traces the transition from models-as-tools to agents-as-investigators |
| [Architecting Trust in Artificial Epistemic Agents](https://arxiv.org/abs/2603.02960) | `[preprint]` | Argues for demonstrable *epistemic competence* — including the ability to evaluate the reliability of evidence — as a deployment precondition |

---

## Verification policy

- Every untagged venue/volume/DOI claim in this file was checked against a publisher page, PubMed, or official proceedings index at the last-updated date.
- `[preprint]` means no peer-reviewed version was found **at that date** — this field moves fast and several 2025 preprints became *Nature*/*Science* papers in 2026. Re-check before citing.
- `‡` means acceptance is recorded from the authors' own arXiv statement and has **not** been confirmed against a proceedings index. It is used where the venue has both archival and non-archival categories and the record does not say which applies.
- Quantitative claims are taken from paper abstracts or full text where openly accessible. Figures sourced only from secondary coverage are not included.

**Known-stale risk.** Entries tagged `[preprint]` in §2 and §6 are the most likely to have been published since the last update. Note also that an arXiv `journal_ref` field is not a reliable negative: both upgrades found in the July 2026 refresh (HoneyComb, AstaBench) had empty or non-committal arXiv metadata and were caught only by checking ACL Anthology and OpenReview directly. Some `[preprint]` tags above are therefore likely to be false.

### Contributing

Corrections welcome — especially preprint→journal upgrades. Please include a link to the publisher record rather than a secondary source.
