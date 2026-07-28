# AI Scientist Survey

A curated survey of **LLM-based systems for autonomous and semi-autonomous scientific discovery** — AI Scientists, scientific agents, self-driving labs — together with the reasoning, verification and evaluation literature they depend on.

**Last updated: July 2026.** Venues are re-verified on each update; see [Verification policy](#verification-policy).

> **Why another list?** Most survey repos in this space link to preprints that have since been peer-reviewed, and organise purely by application domain. This one tracks **canonical venues** (a large fraction of this field's headline systems are now in *Nature*, *Science* or *Nature Machine Intelligence*, not on arXiv) and adds three sections that domain-organised lists usually omit: the **pre-LLM discovery systems**, the **reasoning/verification substrate**, and the **critical evaluations** of AI Scientists.

---

## The field at a glance

![The AI Scientist family — pre-LLM discovery systems above an era break, then LLM-era systems grouped into five subfield branches, each node marked with how strongly it was validated; below, the hypothesis-representation → loop-closure → validation cycle from §3](assets/ai-scientist-family-tree.svg)

Sections [1](#1-classical-foundations-pre-llm)–[3](#3-systems-at-a-glance) as one picture. Arrows mark **only** the lineages this survey states — Adam → the Adam/Eve programme, and AlphaEvolve extending FunSearch. Columns are subfield groupings, not shared descent, and §1 is context rather than ancestry. Node marks are the Validation column of [§3](#3-systems-at-a-glance): ● checked outside the model (*in vitro* or physical synthesis) · ◐ benchmark, leaderboard or held-out data · ○ partial, as reported.

---

## Contents

- [The field at a glance](#the-field-at-a-glance)
- [How to read this survey](#how-to-read-this-survey)
- [1. Classical foundations (pre-LLM)](#1-classical-foundations-pre-llm)
- [2. Systems by subfield](#2-systems-by-subfield)
- [3. Systems at a glance](#3-systems-at-a-glance)
- [4. Reasoning & verification substrate](#4-reasoning--verification-substrate)
- [5. Evidence, attribution & claim verification](#5-evidence-attribution--claim-verification)
- [6. Critical evaluations & audits](#6-critical-evaluations--audits)
- [7. Benchmarks](#7-benchmarks)
- [8. Surveys & agenda papers](#8-surveys--agenda-papers)
- [Verification policy](#verification-policy)

---

## How to read this survey

Section 2 organises systems by **application domain**, which is how most people search. Section 3 re-cuts the same systems along three **cross-cutting axes** that domain tables hide:

| Axis | Question | Values used here |
|---|---|---|
| **Hypothesis representation** | What kind of object is the hypothesis? | `free text` · `program` · `structured state` · `logical` |
| **Loop closure** | What decides whether a hypothesis survives? | `self-critique` · `debate/tournament` · `execution` · `statistical` · `wet lab` · `formal` |
| **Validation** | Was anything checked outside the model? | `none` · `benchmark` · `leaderboard` · `in vitro` · `physical synthesis` |

Two systems in different domains that share a row in Section 3 are usually more alike than two systems in the same domain that don't.

**Status tags.** `[preprint]` = no peer-reviewed version found as of the last update. `[blog]` = company/lab post only. Untagged entries carry a verified peer-reviewed venue.

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
| [**HoneyComb**](https://arxiv.org/abs/2409.00135) | `[preprint]` | LLM agent system for materials science |
| [**LLMatDesign**](https://arxiv.org/abs/2406.13163) | `[preprint]` | Self-reflective LLM agent for materials design |

**Open problems:** novelty definition · predicted ≠ synthesizable · SDL integration · evaluator soundness outside optimisation-shaped tasks.

---

## 3. Systems at a glance

The same systems, re-cut along the axes from [How to read this survey](#how-to-read-this-survey).

| System | Venue | Hypothesis repr. | Loop closure | Validation |
|---|---|---|---|---|
| Robot Scientist Adam | *Nature* '04 | logical | formal + wet lab | physical, autonomous |
| FunSearch | *Nature* '24 | program | execution | benchmark (open problems) |
| AlphaEvolve | `[preprint]` | program | execution | benchmark |
| LLM-SR | ICLR '25 | program | execution | held-out / OOD data |
| ERA | *Nature* '26 | program | execution | **public leaderboard** |
| AI Scientist | *Nature* '26 | free text | execution + self-critique | benchmark; workshop review |
| Co-Scientist | *Nature* '26 | free text (ranked population) | debate/tournament | in vitro (human labs) |
| Kosmos | `[preprint]` | structured state | execution + citation | partial, external |
| Virtual Lab | *Nature* '25 | free text (meetings) | debate → execution | **in vitro** (92 nanobodies) |
| Robin | *Nature* '26 | free text (+ update step) | execution → wet lab | **in vitro** (ripasudil, KL001) |
| Coscientist | *Nature* '23 | free text | execution → robot | **physical synthesis** |
| A-Lab | *Nature* '23 | program-ish (recipes) | robot + XRD | physical synthesis (contested) |
| CRISPR-GPT | *Nat. BME* '26 | task state machine | tool output → wet lab | **in vitro** (knockouts) |
| Biomni | *Science* '26 | free text | execution | benchmark (400+ tasks) |
| ChemCrow | *NMI* '24 | free text | execution → robot | physical synthesis (small) |
| ChemAgents | *JACS* '25 | free text (role-decomposed) | execution → robot | physical synthesis |
| PaperQA2 | `[preprint]` | n/a (retrieval) | citation check | benchmark |

---

## 4. Reasoning & verification substrate

What AI Scientists are built out of. Rarely included in domain-organised surveys, but it determines what these systems can and cannot establish.

| Paper | Venue | Why it matters here |
|---|---|---|
| [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html) | **ICLR 2024** | Process supervision > outcome supervision; PRM800K (800k step-level labels). **No equivalent step-level dataset exists for scientific reasoning** |
| [LLMs Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) | **ICLR 2024** | Intrinsic self-correction without external feedback fails. Relevant to every "reflection agent" in §2 |
| [Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html) | **NeurIPS 2023** | CoT systematically misrepresents the causes of model outputs; biasing features go unmentioned |
| [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) | `[preprint]` | Reasoning models verbalise decisive hints in <20% of cases; outcome-based RL improves faithfulness only to a plateau |
| [Faithful Chain-of-Thought Reasoning](https://aclanthology.org/2023.ijcnlp-main.20/) | **IJCNLP-AACL 2023** | Faithfulness *by construction*: emit a symbolic plan, execute it deterministically |
| [DeepSeek-R1](https://www.nature.com/articles/s41586-025-09422-z) | ***Nature* (2025)** | Reasoning incentivised by RL against **verifiable** rewards. Defines the field's dominant recipe — and its limit: open scientific claims have no verifier |
| [MOOSE-Chem](https://openreview.net/forum?id=IDDE01WDeN) | **ICLR 2025** | Rediscovery-under-cutoff evaluation: recover 2024 *Nature*-level chemistry hypotheses with a 2023-cutoff model |
| [SciMON](https://aclanthology.org/2024.acl-long.18/) | **ACL 2024** | Novelty-optimised hypothesis generation grounded in retrieved "inspirations" |

---

## 5. Evidence, attribution & claim verification

| Paper / system | Venue | Contribution |
|---|---|---|
| [SciFact — Fact or Fiction](https://aclanthology.org/2020.emnlp-main.609/) | **EMNLP 2020** | Scientific claim verification with abstract-level evidence **and rationales**; 1.4k expert claims |
| [ALCE — LLMs generate text with citations](https://aclanthology.org/2023.emnlp-main.398/) | **EMNLP 2023** | Automatic **citation precision/recall** metrics — the field's operational definition of attribution |
| [Veritas](https://arxiv.org/abs/2604.12144) | `[preprint]` | Multi-agent clinical co-scientist emitting a fully auditable evidence trail; four-way epistemic labels — **supported / refuted / underpowered / invalid** |
| [StatefulDiscovery](https://arxiv.org/abs/2606.11851) | `[preprint]` | Externalised investigation state coupling frontier selection, evidence acquisition and **claim adjudication** |
| [VeriGraph](https://arxiv.org/abs/2606.16603) | `[preprint]` | Externalises an agent's reasoning into an executable evidence DAG traceable to raw data |

---

## 6. Critical evaluations & audits

The fastest-moving part of this field as of mid-2026, and the least covered by other survey lists. Mostly preprints — that is a fact about the field, not a sourcing gap.

| Study | Venue | Finding |
|---|---|---|
| [AI scientists produce results without reasoning scientifically](https://arxiv.org/abs/2604.18805) | `[preprint]` | **25,000+ agent runs**, 8 domains. Base model explains **41.4%** of performance variance vs **1.5%** for the agent scaffold. Evidence ignored in **68%** of traces; refutation-driven belief revision in **26%**. Ceiling ~90%+ on workflow execution, never above 60% on hypothesis-driven tasks. Annotates traces with six epistemic operations (hypothesis, gather evidence, test prediction, justify, update belief, commit) |
| [The Agentic Garden of Forking Paths](https://arxiv.org/abs/2607.01507) | `[preprint]` | Agents with different personas reach **opposing conclusions from the same data**. 86% of mutually conflicting analyses passed independent AI review; 78% passed majority human-expert review. Introduces the **m-value** and Agentic Bootstrap |
| [Evaluating KOSMOS in radiation biology](https://arxiv.org/abs/2511.13825) | `[preprint]` | Independent test of three Kosmos hypotheses against **random-gene null controls**: one validated, one uncertain, one false (indistinguishable from noise) |
| [Correct Answer, Wrong Mechanism](https://arxiv.org/abs/2606.23175) | **ICML 2026 AI4Science WS (spotlight)** | Agents reach right-looking results via reasoning that breaks under regime shift; one defended a claim with physics inconsistent with its own data. Proposes a two-step mechanism-fidelity check |
| [Can LLMs Generate Novel Research Ideas?](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html) | **ICLR 2025** | 100+ NLP researchers, blind review: LLM ideas judged **more novel** than expert human ideas, slightly less feasible |
| [Agents4Science reflections](https://www.nature.com/articles/s41587-025-02963-8) | ***Nature Biotechnology* (2025)** | First venue requiring AI first-authorship, with LLM reviewers and human spot-checks; public OpenReview record |
| [A-Lab characterisation dispute](https://www.chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article) | news + response | Reanalysis questioned space-group assignments; the lead author conceded a human could produce a higher-quality refinement while defending the demonstration's scope |

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
| [AstaBench](https://arxiv.org/abs/2510.21652) | `[preprint]` | Cross-domain | 2,400+ problems, 57 agents / 22 classes evaluated, cost-controlled comparison |
| [LAB-Bench](https://arxiv.org/abs/2407.10362) | `[preprint]` | Biology | 2,457 questions across 8 categories (LitQA2, SeqQA, ProtocolQA, …) |
| [BixBench](https://arxiv.org/abs/2503.00096) | `[preprint]` | Computational biology | 53 real scenarios, 296 open-answer questions; frontier models ~17% |
| RE-Bench (METR) | `[preprint]` | ML research | Human-vs-agent research engineering |
| MedAgentBench | `[preprint]` | Medical agents | — |
| MaScQA / MatBench | — | Materials | Weak proxies for discovery ability |

> **Caveat worth stating.** Every benchmark above scores **outcomes**. The audits in §6 find that outcome metrics do not detect epistemic failures — agents reaching right answers through reasoning that would not generalise. There is currently no widely-used benchmark for *reasoning quality* in scientific agents.

---

## 8. Surveys & agenda papers

| Survey | Venue | Angle |
|---|---|---|
| [From Automation to Autonomy: LLMs in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895/) | **EMNLP 2025** | Autonomy-level taxonomy (LLM as Tool / Analyst / Scientist). Peer-reviewed |
| [Empowering biomedical discovery with AI agents](https://pubmed.ncbi.nlm.nih.gov/39486399/) | ***Cell* (2024)** | Biomedical agenda; levels of autonomy for bio agents |
| [Towards Scientific Intelligence: LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047) | `[preprint]` | Mechanism-centric: planners, memory, action space, **verifiers** |
| [Agentic AI for Scientific Discovery](https://arxiv.org/abs/2503.08979) | `[preprint]` | Progress, challenges, future directions |

---

## Verification policy

- Every untagged venue/volume/DOI claim in this file was checked against a publisher page, PubMed, or official proceedings index at the last-updated date.
- `[preprint]` means no peer-reviewed version was found **at that date** — this field moves fast and several 2025 preprints became *Nature*/*Science* papers in 2026. Re-check before citing.
- Quantitative claims are taken from paper abstracts or full text where openly accessible. Figures sourced only from secondary coverage are not included.

**Known-stale risk:** entries tagged `[preprint]` in §2 and §6 are the most likely to have been published since the last update.

### Contributing

Corrections welcome — especially preprint→journal upgrades. Please include a link to the publisher record rather than a secondary source.
