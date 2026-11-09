# hope-kvamme-2025 — Johannes Skotte Hope and Othilie Rørlien Kvamme, 2025
- File: theses/texts/hope-kvamme-2025.txt
- Type: monograph
- Topic: Scheduling a shared BESS and smart EV charging in a 25-household energy community (EC) that takes part in a one-hour incentive-based demand-response (DR) event. "Temporal redistribution" (moving the curtailed load into predefined time slots) is used to control rebound effects. The method is a deterministic LP with SDDP cuts (daily stages) inside a rolling-receding horizon (RRH).
- Note on programme: the title page says MSc in Energy and Environmental Engineering, Department of Electric Energy (supervisor Thorvaldsen). It is not an IØT thesis, even though the brief called it one.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: medium. SDDP is used to carry long-term state information (monthly peak, battery SoC, EV SoC) into a short-term model. However, the SDDP **contains no stochasticity** (stated in 5.2.1). There is a separate discussion chapter, and the assumptions are revisited with the size of their error.
- Citation style: numeric (IEEE-like, [n])
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 32,800 (wc on lines 292–3881, minus ≈ 530 words of nomenclature). This includes captions, table text, equations and page numbers, so the prose is roughly 29,000–30,000 (?).
- Research questions stated explicitly: yes. In 1.2 there is one main RQ plus RQ1 and RQ2, which "supplement" it. Contributions follow as 5 bullets.

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction | INTRO | 292 | 990 | 3.0 % | 8 (lists counted as 1) | 1 (SDG logo) | 0 |
| 2 | Theory | BACK | 419 | 4,040 | 12.3 % | 44 | 6 | 0 |
| 3 | Literature Review | LIT | 846 | 2,690 | 8.2 % | 35 | 0 | 1 |
| 4 | Optimization Theory (incl. 4.4 Optimization Literature Review) | THEORY + LIT | 1173 | 3,140 (+ 530 nomenclature) | 9.6 % | 34 (22 theory + 12 lit) | 3 | 0 |
| – | Nomenclature (unnumbered, between ch. 4 and 5) | OTHER(symbol list) | 1526 | 530 | – | – | – | 1 list |
| 5 | Method | MODEL + SOLVE (5.1 works as PROB) | 1622 | 4,280 | 13.0 % | 40 | 5 | 1 |
| 6 | Case Study | DATA | 2119 | 2,260 | 6.9 % | 26 | 1 | 3 |
| 7 | Results | RES | 2382 | 10,360 | 31.5 % | 89 | 19 | 2 |
| 8 | Discussion | DISC | 3395 | 4,090 | 12.5 % | 35 | 0 | 0 (1 equation) |
| 9 | Conclusion (incl. 9.1 Further Work) | CONCL + FUT | 3784 | 990 | 3.0 % | 11 (4 + 7) | 0 | 0 |

Proportions: Results take almost a third of the text, and Results + Discussion together take 44 %. The front matter before the method (Intro + Background + Lit + Theory) is about 33 %. The introduction is very short (3 %).

## 2. Chapters

### 1 Introduction [INTRO]
- **Purpose in one line:** Moves from VRES growth to the need for demand-side flexibility, names the rebound effect as the unaddressed problem, then gives the RQs, contributions, limitations and outline.
- **Opening paragraph does:** I-CONTEXT + I-CONCEPT + I-LIT + I-PROBLEM. Section 1.1 is one paragraph (≈ 230 words). It runs from the renewables driver, through definitions of price- and incentive-based DR, a one-line group citation of prior studies and the rebound problem, to a gap that ends with the thesis as its "foundation".
- **Closing paragraph does:** OTHER(SDG 7 alignment, with targets 7.a and 7.3 named and an SDG logo figure).
- **Subsections (in order):** 1.1 Background and Motivation → context and gap in one paragraph; 1.2 Objective and Contributions → aim, RQ hierarchy, contribution bullets; 1.2.1 Limitations → scope cuts; 1.2.2 Structure → one line per chapter; 1.3 UN SDG → sustainability link.
- **Paragraph moves (in order, per subsection):**
  - 1.1: I-CONTEXT+I-CONCEPT+I-LIT+I-PROBLEM
  - 1.2: I-AIM+I-CONCEPT (temporal redistribution defined), I-AIM (bridge to the RQs, which are said to target the gap), I-RQ (main RQ + RQ1 + RQ2), I-CONTRIB (5 bullets: method combination, EC simulation, DR simulation, load shifting to predefined slots, cost analysis)
  - 1.2.1: I-SCOPE+I-LIMIT (aggregated data, operational costs only, no investment or remuneration, no grid model and so no recommendation to the DSO)
  - 1.2.2: I-OUTLINE (8 chapter lines)
  - 1.3: OTHER(SDG)
- **Paragraph length:** average ≈ 110 words; shortest ≈ 55 (SDG); longest ≈ 230 (1.1).
- **Figures and tables:** 1 (SDG logo); not interpreted.
- **Chapter-type specifics:** RQ form: one yes/no main RQ ("is X viable for Y") with two open supplementary RQs (implications for flexibility and cost; how to schedule for two actors). Contributions are bullets that start with a noun phrase (Application of…, Simulation of…, Modeling of…). Limitations are a separate subsection, and each cut is paired with a reason. No I-HOOK with a dated number. No findings preview.
- **What makes this chapter strong:**
  - The RQ hierarchy is explicit. The main RQ carries the gap, and two sub-RQs split it into an "implications/cost" question and a "how to schedule" question. The literature-review summary (3.5) later reuses this split, one paragraph per RQ.
  - Contributions are listed as concrete modelling artefacts (method combination, case, mechanism, analysis), so a reader can check each one against a later chapter.
  - Every limitation is stated together with its reason (for example, no recommendation to the DSO because that would need a grid model). This pre-empts the obvious examiner question.
- **Weaknesses:** The background is crammed into a single paragraph with no dated hook or number. The aim paragraph partly repeats 1.1. The SDG section is boilerplate.
- **Signal phrases:** "To the authors' knowledge", "This is the foundation of"

### 2 Theory [BACK]
- **Purpose in one line:** Gives the domain background: the Norwegian power system, the market sequence, end-user pricing, a chain of flexibility concepts (DSM → DR → flexibility potential → rebound), energy communities and emerging flexibility markets.
- **Opening paragraph does:** B-SCOPE (says what the reader will be able to follow afterwards). It is followed by a section roadmap and a reuse declaration (parts revised from the project thesis).
- **Closing paragraph does:** B-MECH + B-BRIDGE. It notes that emerging markets lack a framework and fair remuneration, then points to Sec. 3.4.
- **Subsections (in order):** 2.1 Norwegian Power System (2.1.1 production, 2.1.2 transmission, 2.1.3 distribution, 2.1.4 end-user flexibility as a solution) → system and grid pressure; 2.2 Energy Markets (forwards, capacity/reserves, day-ahead, intraday, re-dispatch) → market sequence; 2.3 End User Pricing (electricity price, grid tariff with demand charge) → the cost terms used later in the model; 2.4 Flexibility (DSM, DR with price-/incentive-based sub-subsections, flexibility potential, rebound effect) → the core concept chain; 2.5 Energy Communities → definition, EU directives, barriers; 2.6 Emerging Products and Markets → link to the lit-review market section.
- **Paragraph moves (in order, per subsection):**
  - intro: B-SCOPE, B-SCOPE (roadmap), OTHER(reuse declaration)
  - 2.1: B-DEF+B-FIG+B-FACT; 2.1.1: B-FACT, B-FACT+B-RELEVANCE (demand growth vs new production); 2.1.2: B-DEF+B-MECH, B-FACT+B-RELEVANCE; 2.1.3: B-DEF+B-MECH, B-RELEVANCE (security margins mean poor utilisation); 2.1.4: B-MECH+B-BRIDGE
  - 2.2: B-SCOPE+B-RELEVANCE; 2.2.1: B-DEF+B-SCOPE (out of scope, not discussed further); 2.2.2: B-MECH, B-FIG+B-MECH, B-MECH; 2.2.3: B-MECH+B-FIG; 2.2.4: B-MECH, B-MECH; 2.2.5: B-MECH+B-RELEVANCE
  - 2.3: B-SCOPE; 2.3.1: B-DEF+B-FACT; 2.3.2: B-DEF, B-MECH (demand charge mechanism: three highest peaks, brackets)
  - 2.4: B-DEF+B-SCOPE, B-DEF+B-SCOPE (supply side excluded); 2.4.1: B-DEF+B-FIG, B-MECH+B-BRIDGE; 2.4.2: B-DEF; 2.4.2.1: B-MECH, B-MECH, B-RELEVANCE; 2.4.2.2: B-MECH, B-MECH+B-BRIDGE; 2.4.3: B-DEF+B-FIG+B-MECH (baseline vs metered load, gaming risk), B-MECH+B-BRIDGE; 2.4.4: B-DEF, B-RELEVANCE, B-FIG
  - 2.5: B-DEF (no uniform definition; EU package and two directives), B-MECH+B-FACT, B-RELEVANCE (benefits and barriers)
  - 2.6: B-MECH, B-MECH+B-BRIDGE
- **Paragraph length:** average ≈ 85 words; shortest ≈ 40 (capacity-market definition); longest ≈ 190 (flexibility potential).
- **Figures and tables:** 6 figures (system sketch, reserve timeline, price zones, DSM measures, flexibility potential, rebound characteristics), all taken or adapted from sources. Introduced before shown: mixed (several are placed before the text refers to them). Interpreted: each gets 1–3 sentences of explanation. None gets observation → interpretation → implication, which is natural for background figures.
- **Numbers from other studies:** ≈ 11 (supply reliability %, hydro and wind capacity shares, current and 2050 demand in TWh, regional consumption growth vs production growth in %, voltage ranges, 80 % spot-contract share).
- **Own work mentioned:** ≈ 5 sentences (scope statements such as "this thesis focuses mostly on…", out-of-scope notes, and the chapter aim).
- **Chapter-type specifics:** The chapter is called "Theory" but is pure domain background. The market subsections end with a relevance or scope line instead of a summary. Concepts that the model needs (the demand charge, incentive-based DR, flexibility potential, rebound) get the most space (2.4 ≈ 1,480 words, 37 % of the chapter).
- **What makes this chapter strong:**
  - The concepts are built as a chain, each defined from the previous one (DSM → DR → price- vs incentive-based → flexibility potential → rebound), so the key term (rebound) arrives last with all its prerequisites in place.
  - Out-of-scope items are pruned in one sentence where they come up (forwards market, supply-side flexibility) instead of being described at length.
  - Subsections often end with a forward pointer to where the concept is used ("further explored in Sec. 2.5/2.6/3.4"), which keeps the background tied to later chapters.
  - The demand charge (the term that later drives every result) is explained concretely: how the peak is averaged, how the price brackets work, and why the DSO cares about it (losses).
- **Weaknesses:** The Norwegian-system facts (TWh numbers, Trøndelag growth) are not tied back to the problem. Several figures come only from sources and get thin explanation. The chapter has no closing summary.
- **Signal phrases:** "falls outside this thesis' scope", "Building on DSM"

### 3 Literature Review [LIT]
- **Purpose in one line:** Reviews application studies on EV charging, BESS, DR (price- and incentive-based) and real flexibility programmes, then condenses them into a table, RQ-mapped takeaways and a gap.
- **Opening paragraph does:** L-SCOPE (why the review is done), followed by a roadmap that says why ECs get no separate section, then a reuse declaration.
- **Closing paragraph does:** L-GAP. The literature shows the benefits of load shifting but neglects rebound, and controlled shifting to predefined slots, with its costs, is unstudied.
- **Subsections (in order):** 3.1 EV Charging (3.1.1 grid impact, 3.1.2 EVs and flexibility); 3.2 BESS (3.2.1 BESS and flexibility, 3.2.2 operation and sizing); 3.3 Demand Response (3.3.1 price-based, 3.3.2 incentive-based); 3.4 Flexibility Programs and Markets (real Norwegian schemes); 3.5 Summary (table + 3 RQ-mapped paragraphs + gap).
- **Paragraph moves (in order, per subsection):**
  - intro: L-SCOPE, L-SCOPE, OTHER(reuse declaration)
  - 3.1: L-RELEVANCE; 3.1.1: L-STUDY, L-STUDY, L-STUDY; 3.1.2: L-STUDY, L-STUDY, L-STUDY
  - 3.2: L-RELEVANCE; 3.2.1: L-STUDY, L-STUDY+L-CRITIQUE (no investment analysis, so the savings are uncertain), L-STUDY+L-CRITIQUE (method unclear, one day only); 3.2.2: L-STUDY, L-STUDY
  - 3.3: L-RELEVANCE; 3.3.1: L-SCOPE, L-STUDY, L-STUDY+L-OWN (setting "comparable to this thesis' model"), L-STUDY; 3.3.2: L-RELEVANCE+L-OWN, L-STUDY+L-CRITIQUE (notice time not stated), L-STUDY, L-STUDY, L-STUDY
  - 3.4: L-SCOPE (back-reference to 2.6), L-STUDY+L-CRITIQUE, L-STUDY, L-PAIR+L-CRITIQUE (two DSO schemes compared; no standard approach)
  - 3.5: L-TABLE, OTHER(signpost that the next three paragraphs target RQ1, RQ2 and the main RQ), L-SYNTH (RQ1), L-SYNTH (RQ2), L-GAP (main RQ)
- **Per-subsection record:**
  - 3.1: cited 6 · in depth 6 · open with author name 0 (they open "A study examines…", "A case study from Trondheim…", "The impact of … is examined [n]") · critique only as study-internal drawbacks ("However, …") · ends on the last study, no synthesis.
  - 3.2: cited 5 · in depth 5 · author-name openings 0 · critique phrased as the authors' doubt ("credibility … questioned", "unclear about whether") · ends on the last study.
  - 3.3: cited 6 distinct ([3] and [4] reused from earlier subsections) · in depth 6 · author-name openings 0 · critique: what a study leaves out and how much that matters (notice time) · ends on the last study.
  - 3.4: cited 4 (programmes and DSOs) · in depth 4 · openings name the programme · critique: missing specification (duration, service, notice) · ends with the critique of non-standardisation.
  - 3.5: table of 20 references with columns "flexibility resource/role" and "contribution and inspiration" · ends with the gap.
- **Paragraph length:** average ≈ 70 words; shortest ≈ 35 (3.4 intro); longest ≈ 110.
- **Figures and tables:** 1 table (literature taxonomy); introduced before shown: yes.
- **Numbers from other studies:** ≈ 14 (cost reductions in %, remuneration in €/year and €/kWh, % cost increase, programme volume range kWh–MWh, demand thresholds in MWh, notice times in h, demand-charge discounts in %, durations in months, neighbourhood size).
- **Own work mentioned:** ≈ 5 sentences.
- **Chapter-type specifics:** Organised by flexible resource and by DR type, not by method (method studies are in 4.4). Almost every study paragraph has the same order: setting/country → aim → method (briefly) → one result, often with a number → limitation or relevance. There are no author-year openings because citations are numeric. L-PAIR appears only once.
- **What makes this chapter strong:**
  - Each study paragraph follows a fixed micro-template (setting, aim, result with one number, limitation), which makes 20 studies quick to scan and easy to compare.
  - The summary table has a "contribution and inspiration" column that says what each reference gives this thesis. That is a cheap way to make L-OWN explicit for every study.
  - The summary paragraphs are explicitly mapped to RQ1, RQ2 and the main RQ, and the gap paragraph is the last thing in the chapter. The review is visibly built to justify the RQs.
  - Real industry programmes (DSO schemes, pilots) are reviewed alongside academic studies and critiqued for missing specifications. This grounds the case parameters chosen later (12-hour notice time) in observed practice.
- **Weaknesses:** Studies are told one after another, with almost no comparison within subsections (only one L-PAIR), and no subsection ends with a synthesis. Critique is sparse and mostly repeats what a study itself says. There is no search strategy and no caveat about comparing numbers across very different settings.
- **Signal phrases:** "The study is unclear about", "it often overlooks the rebound effect"

### 4 Optimization Theory [THEORY + LIT]
- **Purpose in one line:** Explains LP and duality, rolling vs receding horizon, multistage stochastic programming and SDDP, then reviews applications of these methods to justify combining RRH with SDDP.
- **Opening paragraph does:** T-SCOPE + T-RELEVANCE (a method that can see rebound consequences is needed), followed by a roadmap and a reuse declaration.
- **Closing paragraph does:** L-SYNTH + L-OWN. Rolling and receding horizons give short-term adaptivity but miss long-term uncertainty, SDDP complements them, and the combination is therefore chosen.
- **Subsections (in order):** 4.1 Foundations (4.1.1 LP, 4.1.2 duality) → building blocks; 4.2 Time-adaptive Optimization (4.2.1 rolling and receding horizon) → three horizons defined; 4.3 Multi-stage Stochastic Programming (4.3.1 SDDP) → state variables, cuts, passes; 4.4 Optimization Literature Review (4.4.1 rolling/receding, 4.4.2 SDDP, 4.4.3 combined, 4.4.4 summary) → method choice justified.
- **Paragraph moves (in order, per subsection):**
  - intro: T-SCOPE+T-RELEVANCE, T-SCOPE (roadmap), OTHER(reuse declaration)
  - 4.1: T-CONCEPT+T-RELEVANCE; 4.1.1: T-CONCEPT, T-FORMAL (standard form), T-PROPERTY (constraint types, non-negativity); 4.1.2: T-CONCEPT+T-PROPERTY, T-FORMAL+T-PROPERTY (dual of the dual)
  - 4.2: T-CONCEPT; 4.2.1: T-CONCEPT, T-CONCEPT (scheduling, prediction and control horizon defined), T-CONCEPT+T-COMPARE (rolling: pros and cons), T-CONCEPT+T-COMPARE (receding: pros and cons)
  - 4.3: T-CONCEPT+T-EXAMPLE (battery SoC as state variable); 4.3.1: T-CONCEPT+T-PROPERTY (no discretisation; convexity required), T-CONCEPT+T-EXAMPLE (battery: empty today vs keep for tomorrow), T-CONCEPT+T-EXAMPLE (high/normal/low price scenarios), T-ALGO (forward pass, figure), T-ALGO+T-FORMAL (cut equation), T-ALGO (backward pass), T-ALGO+T-PROPERTY (cut accumulation figure; convergence)
  - 4.4: L-SCOPE+L-OWN; 4.4.1: L-STUDY+L-CRITIQUE, L-STUDY, L-STUDY+L-CRITIQUE (rolling horizon cannot see the end-of-month peak, which motivates SDDP), L-STUDY+L-CRITIQUE, L-STUDY; 4.4.2: L-STUDY+L-CRITIQUE (no information update), L-STUDY, L-STUDY+L-CRITIQUE (non-convexity); 4.4.3: L-STUDY, L-STUDY+L-CRITIQUE (one state variable only); 4.4.4: L-SYNTH+L-OWN
- **Per-subsection record (4.4):** cited 10 distinct · in depth 10 · author-name openings 3 ("Knudsen et al.", "Hafiz et al.", "Helseth et al.") · critique placed as the paragraph's last 1–2 sentences, tied to a design need ("Only a 24-hour SH…", "applied without the update of new information") · ends with the method-choice synthesis.
- **Paragraph length:** theory ≈ 80 words (incl. equations); lit ≈ 100; shortest ≈ 40; longest ≈ 125.
- **Figures and tables:** 3 figures (rolling/receding panels, SDDP passes, 1–2–3 cut evolution), all drawn by the authors or "inspired by" a source. 5 equations. Introduced before shown: yes. Each is explained step by step afterwards.
- **Numbers from other studies:** ≈ 16 in 4.4 (horizon lengths in minutes, hours, days and weeks; cost reductions of 7.93 %, 17.8 % and 17 %; experiment length in days; number of households and state variables).
- **Own work mentioned:** ≈ 4 sentences (chapter aim, "selection of methodology for this thesis", "For this thesis, a shorter…").
- **Chapter-type specifics:** Theory runs from general to specific (LP → duality → time-adaptive → multistage → SDDP). The duality section exists to explain where cut coefficients come from. The method literature review is put **inside** the theory chapter, after the methods are defined, so studies can be reported in the same vocabulary (SH/PH/CH, state variables, cuts).
- **What makes this chapter strong:**
  - Every method concept gets a domain example from their own system (a battery's end-of-day SoC as the state variable; draining vs keeping energy for tomorrow as the reason for a cost-to-go function), so the abstract idea lands immediately.
  - Rolling and receding horizon are presented symmetrically: a figure panel each, a mechanism, a computational pro and a realism con. The reader gets a ready-made comparison that the chosen hybrid (RRH) resolves.
  - SDDP is shown with two complementary figures: one for the flow of passes and one for how successive cuts approximate the true cost-to-go (1, 2, 3 cuts).
  - In the method review, each study's critique is phrased as a missing capability that the thesis needs (no end-of-month peak, no information updates, only one state variable). The summary therefore reads as a derived requirement, not a list.
- **Weaknesses:** The SDDP explanation is informal (no stage subproblem, no bounds, no stopping rule), and the stochastic part is explained but then not used in the model. Some LP basics (standard form, duality) are generic textbook content.
- **Signal phrases:** "A drawback of the method", "For this thesis,"

### Nomenclature (unnumbered, between ch. 4 and ch. 5)
- Sets, parameters (uppercase, with units) and variables (lowercase, with units) are listed in one place. The model section points to it instead of repeating tables. Cut coefficients (Φ_c, λ_c, state values in cut c) are listed as parameters.

### 5 Method [MODEL + SOLVE; 5.1 works as PROB]
- **Purpose in one line:** Describes the EC system and the DR mechanism (marginal cost curves, temporal redistribution blocks), then the SDDP + RRH algorithm with a flow chart, the LP formulation, an assumptions table and the implementation.
- **Opening paragraph does:** D-INTRO + M-OVERVIEW (what is modelled, how costs are reduced, which methods are combined). It is followed by a roadmap and by a paragraph that says what the model extends from the project thesis.
- **Closing paragraph does:** S-IMPL (Python, Pyomo, Gurobi, one paragraph of ≈ 30 words).
- **Subsections (in order):** 5.1 Model Description (5.1.1 model, 5.1.2 incentive-based DR signal, 5.1.3 temporal redistribution) → system, signal and blocks; 5.2 Algorithm (5.2.1 generating cuts with SDDP, 5.2.2 RRH, 5.2.3 flow chart) → solution procedure; 5.3 Mathematical Framework (5.3.1 objective, 5.3.2 constraints) → LP; 5.4 Assumptions → table; 5.5 Code Implementation.
- **Paragraph moves (in order, per subsection):**
  - intro: D-INTRO+M-OVERVIEW, OTHER(roadmap), OTHER(extension of and reuse from the project thesis)
  - 5.1: P-OBJECTIVE+P-HORIZON+P-DECISIONS; 5.1.1: P-SYSTEM (figure; EC "representative" of the literature), P-SYSTEM+P-SCOPE (common meter not legal but used; household demand inflexible; BESS does not serve EVs, with reasons)
  - 5.1.2: P-MARKETS (DR signal, notice times taken from a real DSO scheme), M-STEP (marginal cost curve built by decrements of 1 kWh/h until ENS), M-STEP (generic curve explained segment by segment)
  - 5.1.3: M-RATIONALE (why free shifting is a problem for the DSO), M-STEP (block example via figure), P-OUTPUT+P-ACTOR (curves per block go to the DSO, which chooses)
  - 5.2: S-WHY; 5.2.1: S-WHY+S-ALGO (three state variables, curse of dimensionality, one drawback), S-ALGO+D-ASSUMP (stages = days; no stochasticity; inaccuracy after a signal); 5.2.2: S-ALGO+S-FIG, S-ALGO (SH = month, CH = hour, PH dynamic), S-ALGO (13:00 price publication extends PH; last day uses the actual demand charge); 5.2.3: S-FIG+S-ALGO (flow chart walked through in prose, ≈ 250 words)
  - 5.3: D-NOTATION (pointer to the nomenclature; lowercase/uppercase convention); 5.3.1: D-OBJ, D-OBJ+D-LINEAR (last-day objective; linearised demand charge); 5.3.2: D-CONSTR (general note, non-negativity); cut constraint: D-CONSTR, D-CONSTR (three parts of a cut explained); energy balance: D-CONSTR, D-CONSTR; peak import: D-CONSTR, D-CONSTR; grid limit/temporal redistribution: D-CONSTR, D-CONSTR; BESS: D-CONSTR, D-CONSTR; BESS extension: D-CONSTR, D-CONSTR+D-EXT; EV: D-CONSTR+D-ASSUMP (EV flexibility modelled as a virtual battery), D-CONSTR (with an unrealistic counterexample), D-CONSTR
  - 5.4: D-ASSUMP (one sentence + table)
  - 5.5: S-IMPL
- **Paragraph length:** average ≈ 85 words; shortest ≈ 20; longest ≈ 250 (flow-chart walk-through).
- **Figures and tables:** 5 figures (EC power-flow sketch, generic marginal cost curve, block example, RRH with cost-to-go, flow chart) and 1 table (assumptions + justification). 9 numbered equation groups (5.1–5.9, with sub-labels a–h). Introduced before shown: yes.
- **Chapter-type specifics:**
  - PROB: no separate problem-description chapter. 5.1 does that job: objective, actor (EC; the DSO as decision maker on blocks), system, horizon (month), signal. Contains symbols: yes (variable names in the power-flow description). Numbers: yes (example notice times, 3-hour blocks). ≈ 3 pages.
  - SOLVE: S-WHY (twice), S-ALGO, two S-FIG, S-IMPL. No pseudocode, no S-BOUNDS, no S-STOP (convergence is not defined or reported anywhere).
  - MODEL: constraint order is cost-to-go cut → energy balance → peak import → grid-limit (temporal redistribution) → BESS → BESS extension → EV. Each group has a bold-ish heading, a one-sentence intro, the equation block and an equation-by-equation explanation that refers to the sub-labels. Typical explanation length is 2–6 sentences (≈ 40–120 words). Citations in 5.3: 1. Citations in the whole chapter: ≈ 11 (most in 5.1). Assumptions are in a table with 10 rows and a "justification" column. Consequences and direction of bias are **not** given here but are taken up in ch. 8 for several items.
- **What makes this chapter strong:**
  - The generic marginal cost curve figure is introduced and explained segment by segment (negative, zero, low and high volumetric steps, demand-charge jump, ENS wall) **before** any results. Every later result curve can then be read against this template.
  - Constraints are grouped by physical function with short headings. After each block comes a paragraph that walks through the sub-equations by label. This is easy to follow without a separate notation table in the section.
  - Constraints are justified by naming the unrealistic solution they prevent (without the midnight SoC bounds, all EVs would charge in the first days of the month).
  - Modelling simplifications that break reality are stated openly where they arise (a shared meter is not legal; stochasticity is left out), each with the reason it is acceptable for the research question.
  - The flow chart is narrated as a loop with decision points (signal received? activated? end of horizon? hour = 13:00?), which makes the RRH + SDDP interplay concrete.
- **Weaknesses:** Calling it SDDP while stating that no stochasticity is included is confusing (deterministic DDP in practice). There is no convergence criterion or number of iterations. The assumptions table gives justifications but not the consequences or direction of bias, which only appear in the discussion.
- **Signal phrases:** "henceforth referred to as the", "This is done for modeling purposes"

### 6 Case Study [DATA]
- **Purpose in one line:** Sets the case (25 households in Trondheim, NO3, January 2022), gives a source and justification for every input, and defines four cases from least to most restrictive, each with an aim.
- **Opening paragraph does:** A-PURPOSE + A-CASE (goal, location, price zone, DSO, components), followed by a reader-oriented purpose paragraph, a roadmap and a reuse declaration.
- **Closing paragraph does:** A-INSTANCES. Case 3 is described as the most restrictive and therefore the one that gives the most control over rebound.
- **Subsections (in order):** 6.1 Input Data (6.1.1 household demand, 6.1.2 electricity cost, 6.1.3 grid tariff, 6.1.4 EV charging, 6.1.5 BESS, 6.1.6 cost of ENS, 6.1.7 the restricted hour); 6.2 The Modeled Cases (6.2.1–6.2.4, Cases 0–3).
- **Paragraph moves (in order, per subsection):**
  - intro: A-PURPOSE+A-CASE, A-PURPOSE, OTHER(roadmap), OTHER(reuse declaration)
  - 6.1: A-SOURCE+A-CASE (why January; units convention); 6.1.1: A-SOURCE+A-PROCESS (mean per metering point scaled to 25); 6.1.2: A-SOURCE+A-PROCESS (VAT added); 6.1.3: A-SOURCE+A-LIMIT+A-PARAM-TABLE (tariff period mismatch judged not to discredit the analysis), A-PROCESS (bracket tariff linearised to a slope + intercept); 6.1.4: A-SOURCE+A-PROCESS (weekday/weekend profiles repeated and aligned), A-CASE (charger count, private share, kW), A-PROCESS (±20 % day-to-day shift limit, with reason); 6.1.5: A-PARAM-TABLE+A-SOURCE (Powerwall-based; SoC limits from cited studies); 6.1.6: OTHER(penalty value justified by what it prevents); 6.1.7: A-CASE (09:00 chosen as a historically high-load hour), A-CASE+A-SOURCE (12 h notice from real schemes and a study), A-CASE (restriction level; SoC range relaxed to 0–100 %)
  - 6.2: A-INSTANCES (overview: Case 0 + three increasingly restrictive cases), A-INSTANCES (Case 0), A-INSTANCES (common goal of Cases 1–3, date and hour), A-INSTANCES (Cases 1–3 in one paragraph each + with/without demand charge); 6.2.1: A-INSTANCES (goal: reference case); 6.2.2: A-INSTANCES (goal: "stepping stone"); 6.2.3: A-INSTANCES, A-INSTANCES (goal: partial control of rebound timing); 6.2.4: A-INSTANCES (goal: most control)
- **Paragraph length:** average ≈ 75 words; shortest ≈ 30; longest ≈ 130.
- **Figures and tables:** 1 figure (Before/After illustration) and 3 tables (energy charge, demand-charge brackets, BESS parameters). No data figures (no price or demand profile is plotted).
- **Chapter-type specifics:** A-INSTANCES: 4 cases, each with an explicit goal (yes) and a role in the sequence. The demand charge on/off is a cross-cutting switch applied to every case. A-LIMIT appears once (tariff period mismatch). The penalty and SoC limits are justified with sources.
- **What makes this chapter strong:**
  - Every parameter has a source sentence and a "why this value" sentence (coldest month, so grid strain; 09:00 as a high-load hour; 12 h notice as used by two DSOs).
  - Cases are ordered from least to most restrictive and each is given a role (reference case, stepping stone, partial control, most control). The results chapter can then follow the same order and the reader knows what each case is meant to show.
  - A known data inconsistency is named and judged openly instead of being hidden.
  - The tariff linearisation is shown as one equation with the fitted numbers, which links the data table directly to the model term.
- **Weaknesses:** Input series (prices, demand, EV profile) are never plotted, so the reader cannot see the price pattern that later explains every result. There is no table summarising the cases.
- **Signal phrases:** "henceforth referred to as the"

### 7 Results [RES]
- **Purpose in one line:** Shows model mechanics (Case 0, SDDP cuts), then for each case the operation, the marginal cost curves and monthly heat maps (each with and without the demand charge), then how the curves evolve over the month, then the cost tables for a single activation.
- **Opening paragraph does:** R-AIMS (what the cases show and how performance is judged: rebound and cost), followed by a roadmap, R-CAVEAT (only one day is shown in detail, with 17:00 added for contrast) and a term definition ("total volumetric electricity price").
- **Closing paragraph does:** R-OBS + R-IMPL + R-SUMMARY. Optimising for the demand charge lowers the base-case total cost by ≈ 6 %, and every activation costs less than 1 %, which suggests flexibility is cheap for the EC.
- **Subsections (in order):** 7.1 Case 0 (7.1.1 SDDP cut results, 7.1.2 operation); 7.2 Case 1 (operation, marginal cost [excl / incl / comparison], heat maps); 7.3 Case 2 (same three layers, plus 17:00 heat map); 7.4 Case 3 (same three layers); 7.5 Evolution of the marginal cost curves (days of the month); 7.6 Economic results for one activation (two tables + comparison).
- **Paragraph moves (in order, per subsection).** Cases 1–3 have the same internal structure and are coded per layer.
  - intro: R-AIMS, OTHER(roadmap), R-CAVEAT, OTHER(term definition)
  - 7.1: R-AIMS, OTHER(figure roadmap); 7.1.1: R-KEYREL+R-CAVEAT (only one state variable plotted, for visualisation), R-KEYREL (how the cost-to-go is the upper envelope of cuts), R-KEYREL (marginal curve as derivative), R-OBS+R-INTERP (zero then rising marginal cost; compared with the analytical demand-charge slope), R-OBS+R-INTERP+R-CAVEAT (artefact of SDDP exploring only "interesting" states); 7.1.2: OTHER(figure reading guide: colours and series), R-OBS+R-INTERP, R-OBS+R-INTERP, R-OBS, R-OBS+R-INTERP (the demand charge evens out import; the value of the cuts), R-OBS+R-INTERP (DSM measures named; peak −50 %), R-OBS+R-INTERP (less battery cycling)
  - 7.2: R-AIMS, OTHER(roadmap); 7.2.1: OTHER(reading guide: highlights for signal and restricted hours), OTHER(reading guide: lines), R-OBS+R-INTERP, R-OBS+R-INTERP, R-OBS+R-INTERP (two strategies contrasted); 7.2.2 excl: R-KEYREL (how the curve is built; area = cost), R-OBS, R-INTERP, R-OBS+R-INTERP; incl: OTHER(reading guide), R-OBS+R-INTERP; comparison: R-CAVEAT (curves not fully comparable), R-OBS+R-INTERP (+ pointer to 7.6); 7.2.3: R-KEYREL (heat-map construction), OTHER(worked example of one day's point), R-OBS+R-INTERP, R-OBS+R-IMPL (days with zero flexibility), R-OBS+R-INTERP
  - 7.3: R-AIMS (Before/After defined), R-AIMS+OTHER(roadmap); 7.3.1: OTHER(reading guide) ×3, R-OBS+R-INTERP, R-OBS+R-INTERP (peak +1.3 % vs +0.9 %); 7.3.2 excl: OTHER(guide), R-OBS+R-INTERP, R-OBS+R-INTERP; incl: OTHER(guide), R-OBS+R-INTERP; comparison: R-IMPL (DSO perspective vs cost), R-IMPL; 7.3.3: R-OBS+R-INTERP (excl), R-OBS+R-INTERP (incl), R-OBS+R-INTERP+R-IMPL (17:00 reverses the ranking; value of guaranteed flexibility for the DSO), R-SUMMARY (time of day decides the strategy), R-INTERP (why)
  - 7.4: R-AIMS, OTHER(roadmap); 7.4.1: OTHER(guide), OTHER(guide: block colours), R-OBS+R-INTERP, R-OBS+R-INTERP, R-OBS+R-INTERP (a new peak is exploited for the rest of the month), R-INTERP+R-IMPL (rebound evident but timing controllable for the operator); 7.4.2 excl: R-OBS+R-INTERP, R-OBS+R-INTERP; incl: R-OBS, R-OBS+R-INTERP, R-OBS+R-INTERP (observed plateau vs the analytical value of slope ÷ 3 hours, explained); comparison: R-SUMMARY; 7.4.3: R-OBS, R-INTERP+R-IMPL (Block D best at 09:00), R-OBS, R-OBS+R-INTERP
  - 7.5: R-KEYREL (why Block B; axis choice), R-OBS+R-INTERP+R-IMPL (cost depends on time of month as well as time of day), R-INTERP+R-CAVEAT (plateau reflects SDDP inaccuracy away from explored states)
  - 7.6: R-AIMS+R-CAVEAT (single activation only); excl: OTHER(table reading guide: Case 0 absolute, others as deltas), R-OBS+R-INTERP (max +4.20 NOK, ≈ 0.01 %), R-OBS+R-CAVEAT (peak unchanged only for this day), R-OBS+R-INTERP (negative costs explained by the penalty), R-INTERP, R-OBS+R-INTERP+R-IMPL; incl: OTHER(guide), R-OBS+R-INTERP, R-OBS+R-INTERP+R-IMPL (cost of activation 0.01–0.79 %; cheapest = least rebound); comparison: R-OBS+R-IMPL+R-SUMMARY
- **Paragraph length:** average ≈ 110 words; shortest ≈ 35; longest ≈ 230 (Case 2 heat map, excl.).
- **Figures and tables:** 19 figures (3 + 4 + 6 + 5 + 1) and 2 tables. Introduced before shown: yes, for almost all, usually by a reading-guide paragraph. Observation → interpretation is present for essentially every figure. Observation → interpretation → implication (for the EC/DSO) is complete for ≈ 7 of 19 (7.2.4, 7.3.2/7.3.3 via the comparison, 7.3.6, 7.4.1, 7.4.4, 7.5.1).
- **Chapter-type specifics:** Order: mechanism check (cuts and base operation) → case by case (operation → marginal cost → heat map) → time-of-month evolution → economics. R-TECH: **absent** (no runtimes, iterations, SDDP convergence or solver statistics). R-LIT: absent (no citations in the chapter). R-STOCH: absent (deterministic). R-SENS: implicit, through demand charge on/off, 09:00 vs 17:00 and all days of the month (heat maps).
- **What makes this chapter strong:**
  - Each case has an identical three-layer structure (operation plot → marginal cost curve → monthly heat map). Each layer is split into "Excluding / Including the demand charge / Comparison" sub-headings, so the reader always knows where a result is and what it is compared with.
  - A reading-guide paragraph comes before each complex figure (what each colour, line and highlight means). Only then come observation paragraphs. This separates "how to read" from "what it shows".
  - Observed numbers are checked against an analytical expectation (marginal cost vs the demand-charge slope, or the slope ÷ 3 for 3-hour blocks), and the gap is explained. This doubles as a sanity check.
  - Method artefacts are flagged where they appear (SDDP cuts are inaccurate away from explored states). The reader is not left to find them, and this sets up the discussion.
  - A worked example shows how one day's result becomes one cell of the heat map, before the heat map is interpreted.
  - The cost tables give the base case in absolute numbers and all other cases as deltas, and each result is turned into a percentage of total cost, so magnitude is clear.
- **Weaknesses:** Repetitive. Many paragraphs describe lines in plots at length, and the chapter is 31 % of the text. Discussion-like material is mixed into the results ("together with a brief discussion"). No computational results are given, although SDDP and RRH are central. Some numbers are reported to more precision than they deserve.
- **Signal phrases:** "may be interpreted as follows", "It is worth noting that"

### 8 Discussion [DISC]
- **Purpose in one line:** Synthesises results across cases (three numbered arguments for optimising the demand charge, cost by case, the DSO perspective), then discusses method and assumptions one by one, quantifying their effect, and ends with a worked valuation of flexibility.
- **Opening paragraph does:** OTHER(chapter purpose: compare across cases and assess credibility), followed by a roadmap (case-specific part, then general part) and a reuse declaration.
- **Closing paragraph does:** X-IMPL. The DSO should read the EC's marginal cost as a flexibility indicator and weigh three sensitivities (timing, quantity, cost).
- **Subsections (in order):** 8.1 Case Discussion (8.1.1 optimising for the demand charge, 8.1.2 cost of temporal redistribution, 8.1.3 the DSO's perspective); 8.2 General Discussion (8.2.1 SDDP for long-term consequences, 8.2.2 demand-charge modelling, 8.2.3 battery degradation, 8.2.4 household data, 8.2.5 feasibility of smart EV charging, 8.2.6 price-based DR undermining incentive-based DR, 8.2.7 value of flexibility).
- **Paragraph moves (in order, per subsection):**
  - intro: OTHER(purpose), OTHER(roadmap), OTHER(reuse declaration); 8.1: OTHER(section scope)
  - 8.1.1: OTHER(cross-case claim "First": lower total cost, with numbers), OTHER(claim "Second": more deliverable flexibility, battery-friendly), OTHER(claim "Third": less rebound; Case 3 the exception, with % range), X-METHOD (needs good forecasts; needs a cost-to-go)
  - 8.1.2: OTHER(case synthesis: Case 1), OTHER(case synthesis: Case 2, ≈ 370 words), OTHER(case synthesis: Case 3)+X-METHOD (heat maps cannot capture the demand-charge change)
  - 8.1.3: X-IMPL, X-IMPL (trade-off: predictability vs intensity of rebound), X-GENERAL (a portfolio of ECs with different blocks activated)
  - 8.2: OTHER(scope)
  - 8.2.1: X-METHOD (efficiency vs accuracy away from explored states), X-METHOD+X-ASSUMP (linearity; integer extensions exist but are out of scope), X-METHOD (alternative SDP described and rejected: size, discretisation, accuracy), X-ASSUMP (verdict: computation prioritised over accuracy)
  - 8.2.2: X-ASSUMP (linear vs stepwise: error quantified at ≈ 4.6 %), X-ASSUMP (direction: the linear model cannot exploit headroom up to a bracket bound), X-ASSUMP (stepwise brackets would change the block ranking), X-ASSUMP (single peak vs average of three: ≈ 2.4 % overstatement, only for non-optimised cases), X-ASSUMP (aggregated tariff unrealistic, so linearisation is defensible)
  - 8.2.3: X-ASSUMP+X-LIMIT (degradation only via a penalty outside 20–80 %; a full model conflicts with SDDP linearity)
  - 8.2.4: X-ASSUMP+X-GENERAL (exact demand data matters little for behaviour), X-GENERAL (adding heating/water heaters needs the demand charge)
  - 8.2.5: X-ASSUMP (EV availability assumed; direction stated: performance overestimated, cost underestimated)
  - 8.2.6: X-CONTEXT (similar finding in [4]) + X-IMPL, X-IMPL (remuneration needed)
  - 8.2.7: X-IMPL (valuation question, with the Case 2 cost), OTHER(worked market-clearing example with profit equation), X-IMPL (per-household remuneration small, but ≈ 2× cost; benchmarked to [3]), X-CONTEXT+X-IMPL (single bid = lower bound; real programme average NOK/kWh), X-IMPL (DSO's three sensitivities)
- **Paragraph length:** average ≈ 115 words; shortest ≈ 30; longest ≈ 370.
- **Figures and tables:** 0 figures, 0 tables, 1 equation. Results figures and tables are referred to by number throughout.
- **Numbers from other studies:** ≈ 2 (one programme's average remuneration; the date of a tariff rule change).
- **Chapter-type specifics:** X-CONTEXT is rare (2 paragraphs; literature comparison is thin). X-ASSUMP is strong: 8 paragraphs, several with the size of the error and/or the direction of bias. X-METHOD includes a rejected alternative (SDP) with reasons. X-IMPL is stakeholder-specific (EC vs DSO). X-LIMIT appears only inside the assumption paragraphs. There is no separate limitations subsection.
- **What makes this chapter strong:**
  - The case discussion opens with a claim backed by three numbered reasons (First/Second/Third), each pointing to a specific table or figure and number. The chapter's main finding is stated in the first paragraph.
  - Simplifications are quantified, not just named. The cost under the true stepwise tariff is recomputed for the actual peak (≈ 4.6 % error), and the three-peak rule is checked (≈ 2.4 %). For each, the text says which results are affected and in which direction.
  - A rejected alternative method (SDP) is described fairly (what it would allow, why it was not chosen for this state space), which shows the method choice was deliberate.
  - A worked example turns the marginal cost curve into a market bid, clearing price and profit. The result is then scaled per household and benchmarked against a real programme. This makes an abstract curve economically meaningful.
  - The stakeholder perspective is a subsection of its own, ending on a clear trade-off statement (more predictable rebound means a more intense rebound).
- **Weaknesses:** Little comparison with literature results (X-CONTEXT is almost absent). 8.1.2 largely retells results case by case. There is no explicit generalisability statement beyond one EC and one month.
- **Signal phrases:** "for several reasons", "comes at the expense of", "In this thesis, computational feasibility"

### 9 Conclusion [CONCL] and 9.1 Further Work [FUT]
- **Purpose in one line:** Restates what was done, gives findings case by case with numbers, states the demand-charge finding and ends with the policy implication on remuneration. Then 6 further-work items.
- **Opening paragraph does:** C-PROBLEM + C-DONE (research aim, model, RRH/SDDP roles, temporal redistribution, the cases).
- **Closing paragraph does:** C-OVERALL + C-LIMIT. Temporal redistribution lets the DSO trade intensity, timing and cost of rebound, grid-side analysis is still needed, and remuneration should reflect grid value. The further-work section ends on DSO valuation and fair remuneration.
- **Subsections (in order):** (unnamed main body: 4 paragraphs); 9.1 Further Work (intro + 6 items).
- **Paragraph moves (in order, per subsection):**
  - main: C-PROBLEM+C-DONE, C-FIND-OP+C-FIND-ECON (Cases 1→3 in order, each with marginal cost and total cost numbers; upper bound in %), C-FIND-OP+C-FIND-ECON (demand-charge effect, deliverable flexibility in kWh/h; time-of-month effect), C-OVERALL+C-LIMIT (implicit answer to the main RQ; remuneration implication)
  - 9.1: OTHER(intro: links to the assumptions table in 5.4), F-EXT ×6
- **Paragraph length:** main ≈ 150 words; 9.1 items ≈ 55.
- **Chapter-type specifics:** C-ANSWER: the RQs are **not** named or answered one by one. The main RQ is answered implicitly in the last paragraph, RQ1 (flexibility/cost) through the case-by-case numbers, and RQ2 (scheduling) through the demand-charge paragraph. Findings follow the case order.
  - F-EXT parts (what / why current assumption limits / expected effect / complexity cost):
    1. Uncertainty in SDDP + individual-unit data: what yes · why yes (realism) · effect no · cost yes (claimed simple to add)
    2. Multiple activations and times: what yes · why yes (recurring service, value) · effect no · cost no
    3. Summer month or full year, over-voltage DR: what yes · why yes (different load curves, PV) · effect no · cost no
    4. Equal Before/After lengths, other block lengths: what yes · why yes (comparability) · effect no · cost no
    5. Degradation model and investment costs: what yes (with source to adapt) · why partial · effect partial · cost no
    6. DSO valuation and remuneration: what yes · why yes · effect no · cost no
- **What makes this chapter strong:**
  - Findings are given case by case, in the same order as the results, with one or two numbers each and the overall cost upper bound. The reader gets the whole quantitative story in one paragraph.
  - The final paragraph lifts the result to a practical implication (who should pay and why) instead of restating numbers.
  - Further work is explicitly derived from the assumptions table (5.4), which closes the loop between method and outlook.
- **Weaknesses:** The RQs from 1.2 are never named, so the reader must map the answers. Some numbers do not quite match the results chapter (?) (e.g., the Case 1 marginal cost, and the Case 3 "before" flexibility range vs the 24.2 kWh/h for Block A). Further-work items rarely state the expected effect or cost.
- **Signal phrases:** "comes at the expense of"

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:**
  - Coined terms are introduced once with "henceforth referred to as" and then used without synonyms: restricted hour, signaled hour, Before/After, Block A–D, temporal redistribution, total volumetric electricity price.
  - The same day and hour (6 January, 09:00) is used in every case.
  - Every result is shown in a pair (excluding/including the demand charge).
  - Section numbers are cited for back-references (3.4 refers back to 2.6; 7.x figures are referred back to 7.1.3; 8.2.7 refers back to 3.4).
  - The method literature review (4.4) produces the requirements that 5.2 meets: SDDP is needed because a rolling horizon cannot see the end-of-month peak.
  - The assumptions table (5.4) is revisited in 8.2 and named as the basis of 9.1.
  - Each chapter opens with a purpose, a roadmap and a reuse declaration, so all chapters start the same way.
- **How the RQs or objectives are answered in the conclusion:** implicitly. They are not numbered or quoted. Findings go case by case in results order with numbers, then the demand-charge finding, then the overall verdict on viability and the remuneration implication. The lit-review summary (3.5) is the only place outside ch. 1 that names RQ1, RQ2 and the main RQ.
- **Anything a strong thesis does that the codes do not capture:**
  - Reuse declarations at the start of chapters 2, 3, 4, 5, 6 and 8 name exactly which sections are revised from the project thesis.
  - Reading-guide paragraphs come before every complex figure, and there is a worked example of how one data point enters an aggregate plot (heat map).
  - A "template" figure in the method chapter (a generic marginal cost curve with labelled segments) teaches the reader to read every later result curve.
  - The cross-cutting experimental switch (demand charge on/off) is applied to every case and gives a free sensitivity analysis.
  - The method literature review is placed inside the theory chapter, after the concepts, so studies are reported in the vocabulary just defined (horizon lengths per study).
  - A worked economic example in the discussion (market-clearing bid → price → profit → per household → benchmark) turns a model output into a policy-relevant number.
  - A separate nomenclature sits between the theory and the method chapters, so the model section only points to it.
