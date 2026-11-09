# hansen-pinderud-2024 — Andreas Fosse Hansen and Jonas Henrik Pinderud, 2024
- File: theses/texts/hansen-pinderud-2024.txt
- Type: monograph (a conference paper, "Paper I", came out of it and is referred to for the SDDP algorithm and two figures)
- Topic: operating an office building with an aggregated EV parking lot (EVPL) under hourly spot prices and a monthly peak demand charge, while answering throttling signals from an incentive-based demand response programme (IBDRP) with 0, 2 or 12 h notice; SDDP builds future-cost cuts on the monthly peak, and a receding-horizon (RH) loop runs hourly operation using those cuts. Supervisor Kasper Thorvaldsen; written at the Department of Electric Energy (not IØT, despite the brief).
- Relevance to a pumped-hydro / SDDP / multi-market thesis: medium (SDDP cuts on a single state variable feeding a short-term operating loop; marginal-future-cost reading of cuts; no reserves market, no investment)
- Citation style: numeric ([n]), 96+ references
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 27,900 raw by wc (includes captions, table cells, notation lists and equation fragments); ≈ 25,000 prose (?)
- Research questions stated explicitly: no. Objectives only: one aim paragraph (1.2) plus a 5-bullet contribution list; the gap is one sentence in that aim paragraph.

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction | INTRO | 361 | 1,000 | 3.6 % | 8 (+5 contribution bullets, 7 outline items) | 0 | 0 |
| 2 | Theory | BACK | 470 | 3,250 | 11.6 % | 29 | 2 | 0 |
| 3 | Literature Review | LIT | 780 | 2,550 | 9.2 % | 23 | 0 | 0 |
| 4 | Optimization Theory and Literature Review | THEORY + LIT | 1012 | 3,050 (theory ≈1,440; lit ≈1,610) | 10.9 % | 32 (15 theory + 17 lit) | 3 | 0 |
| 5 | Method | FRAME + MODEL + SOLVE | 1321 | 3,300 | 11.9 % | 32 | 6 (+1 algorithm) | 0 (notation as lists) |
| 6 | Case Study | DATA + SCEN | 1716 | 2,400 | 8.6 % | 20 | 5 | 4 |
| 7.1–7.4 | Results and Discussion (Cases 0–3) | RES | 1994 | 10,600 | 37.9 % | 80 | 24 | 7 |
| 7.5 | General Discussion | DISC | 2979 | 1,120 | 4.0 % | 9 | 0 | 0 |
| 8 | Conclusion | CONCL | 3071 | 420 | 1.5 % | 4 | 0 | 0 |
| 8.1 | Further Work | FUT | 3111 | 210 | 0.8 % | 3 | 0 | 0 |

Front matter: abstract (4 paragraphs, ≈ 330 words), Norwegian summary, preface, abbreviation list (~45 entries). No appendix. Discussion is a final section of the results chapter, not its own chapter.

## 2. Chapters

### Abstract [ABS]
- Moves: AB-CONTEXT+AB-WHY+AB-PROBLEM+AB-CASE (EV growth strains grid; flexible EVPL studied with real office data) → AB-METHOD (RH framework + SDDP future-cost curves; tested on notice times, throttling depth, V2G) → AB-RES-OP+AB-RES-ECON (five numbers: 0.57 %, 35 %, 49 %, 3.2 %, 1.8 %) → AB-IMPL (value to building owner and DSO given enough notice).
- Strong: the results paragraph is a ladder of one number per tested setting, ordered as the cases are later.

### 1 Introduction [INTRO]
- **Purpose in one line:** motivates why an office EVPL facing a monthly demand charge should be studied as a demand-response resource, and lists what the thesis delivers.
- **Opening paragraph does:** I-HOOK+I-CONTEXT — EV adoption, a cited Norwegian study's share of electricity use and a TSO forecast for transport demand in 2030.
- **Closing paragraph does:** OTHER(list of publications) — names the conference paper that came out of the work.
- **Subsections (in order):** 1.1 Motivation → driver, problem, national example; 1.2 Objective/Contributions → aim, one-sentence gap, contribution bullets; 1.2.1 Limitations → three delimitations; 1.2.2 Structure → chapter-by-chapter outline; 1.2.3 List of Publications.
- **Paragraph moves (in order, per subsection):**
  - 1.1 Motivation: I-HOOK+I-CONTEXT, I-PROBLEM+I-CONCEPT (peak loads; monthly demand charge explained plainly), I-NATIONAL+I-CONCEPT (IBDRP with a notice-dependent tariff discount from a named Norwegian DSO)
  - 1.2 Objective/Contributions: I-AIM+I-LIT (aim, then the one-sentence gap on notice times), I-CONTRIB (5 bullets: RH framework; SDDP for demand charge; IBDR with notice times; V2G; economic incentive)
  - 1.2.1 Limitations: I-SCOPE+I-LIMIT (no power-flow limits, no investment cost, aggregated EV data)
  - 1.2.2 Structure: I-OUTLINE
  - 1.2.3 List of Publications: OTHER(publication declaration)
- **Paragraph length:** average ≈ 85 words; shortest ≈ 25; longest ≈ 140 (aim paragraph)
- **Figures and tables:** 0
- **Chapter-type specifics (INTRO):** RQs no; contributions as bullets; findings not previewed; scope in its own short subsection; reuse of project-thesis material is declared at the start of ch. 2 and ch. 3, not in the intro.
- **What makes this chapter strong:**
  - The contribution bullets map one-to-one onto the later Cases 0–3 (framework, IBDR, V2G, economic incentive), so the list doubles as a preview of the results chapter's structure.
  - The national example (a real DSO product whose discount grows as notice time shrinks) gives the reader the exact trade-off the thesis studies before any model appears.
  - Very short (≈ 1,000 words): three motivation paragraphs, aim, bullets, done.
- **Weaknesses:** no explicit RQs; the gap is a single unsupported sentence ("To the author's knowledge, limited work"); the hook repeats the same two numbers that open 3.1.1.
- **Signal phrases:** "To the author's knowledge, limited work"; "The main contributions of this work"

### 2 Theory [BACK]
- **Purpose in one line:** gives a non-specialist the grid, market, tariff, demand-response and EV-charger background needed to follow the problem.
- **Opening paragraph does:** B-SCOPE — lists the three blocks the chapter covers in order; a second paragraph declares which sections reuse project-thesis text (OTHER(reuse declaration)).
- **Closing paragraph does:** B-MECH+B-SCOPE — explains V2G/V2B and fixes that "V2G" will cover both from here on (a terminology decision).
- **Subsections (in order):** 2.1 Electricity grid (2.1.1 TSO, 2.1.2 DSO, 2.1.3 challenges in Norway) → actors and why flexibility is needed; 2.2 Norwegian pricing model (power market, day-ahead, grid tariff) → where prices and the demand charge come from; 2.3 Demand side management (DR, price-based, incentive-based) → the two DR families; 2.4 Electric vehicle (charging, charger modes, bi-directional) → what flexibility each charger type can give.
- **Paragraph moves (in order, per subsection):**
  - intro: B-SCOPE, OTHER(reuse declaration)
  - 2.1: B-DEF+B-SCOPE
  - 2.1.1: B-DEF+B-FACT
  - 2.1.2: B-DEF+B-MECH+B-FACT
  - 2.1.3: B-MECH+B-FACT, B-FACT+B-RELEVANCE (TSO lacks reserves; consumption must contribute flexibility)
  - 2.2.1: B-FACT+B-FIG
  - 2.2.2: B-MECH (auction timeline with clock times)
  - 2.2.3: B-DEF+B-MECH (tariff components; term "demand charge" fixed), B-FACT (small-customer tariff), B-FACT+B-MECH (large-customer tariff: single highest hour)
  - 2.3: B-DEF (quoted definition), B-MECH+B-FIG (peak clipping, valley filling, load shifting)
  - 2.3.1: B-DEF+B-FACT, B-RELEVANCE+B-SCOPE
  - 2.3.1.1: B-DEF+B-MECH+B-FACT, B-MECH+B-RELEVANCE (demand charge couples short-term decisions to the month)
  - 2.3.1.2: B-DEF+B-MECH, B-CASE (three real programmes, the last being the DSO product used later)
  - 2.4: B-FACT+B-RELEVANCE+B-BRIDGE (forward pointer to 3.1.2)
  - 2.4.1: B-SCOPE+B-DEF (passive vs smart chargers)
  - 2.4.1.1: B-SCOPE, B-DEF+B-FACT+B-RELEVANCE ×4 (one paragraph per charger mode)
  - 2.4.1.2: B-DEF, B-MECH+B-FACT+B-SCOPE
- **Paragraph length:** average ≈ 100 words; shortest ≈ 30; longest ≈ 180
- **Figures and tables:** 2 figures (both borrowed, both introduced in the text before shown; neither interpreted beyond naming its contents); 0 tables
- **Numbers from other studies:** ≈ 25 (voltage levels, tariff thresholds, VAT, EV shares, charger power levels, auction clock times)
- **Own work mentioned:** ≈ 6 sentences (definition adopted for the thesis, scope of physical market only, term choice, V2G naming)
- **Chapter-type specifics (BACK):** defines terms the model later uses (demand charge, IBDR, V2G); one real-case paragraph (2.3.1.2) seeds the case study; only one forward bridge; no "how it is usually modelled" paragraphs.
- **What makes this chapter strong:**
  - Every charger-mode paragraph ends with the same closing move: what flexibility that mode can offer the DSO. A fixed last sentence per item turns a technical catalogue into an argument.
  - The tariff section separates small and large customers and then states which variant the thesis uses, so the later demand-charge constraint has a clear real-world source.
  - Terminology decisions are made explicitly in the background (the capacity tariff component is given one fixed name; V2G covers V2B too), which keeps terms fixed in later chapters.
- **Weaknesses:** grid basics (TSO/DSO voltage levels) are generic and not used later; figures are not interpreted; one Wikipedia-style source is cited as a TSO source.
- **Signal phrases:** "Based on the scope of this thesis"; "from here on encompasses"

### 3 Literature Review [LIT]
- **Purpose in one line:** reviews studies on EV impact on the grid, EV flexibility, V2G, demand charges and IBDRPs to show what is already known.
- **Opening paragraph does:** L-SCOPE — names the topics and says the chapter is used to define the thesis's scope; then OTHER(reuse declaration).
- **Closing paragraph does:** L-STUDY — a single study on notice times in a DR programme (the closest to the thesis); no link to own work and no gap statement follow.
- **Subsections (in order):** 3.1 EV charging and flexibility (3.1.1 EV diffusion effects; 3.1.2 grid problems; 3.1.3 flexibility from EV charging; 3.1.4 V2G); 3.2 Demand response (3.2.1 demand charge; 3.2.2 flexibility in IBDRPs).
- **Paragraph moves (in order, per subsection):**
  - intro: L-SCOPE, OTHER(reuse declaration)
  - 3.1: L-SCOPE
  - 3.1.1: L-RELEVANCE+L-STUDY, L-STUDY, L-STUDY+OTHER(mechanism: socket-to-charger shift raises congestion)
  - 3.1.2: L-GROUP, L-PAIR+L-SYNTH (two penetration case studies, then a one-line synthesis)
  - 3.1.3: L-STUDY, L-STUDY+OTHER(analogy: why battery-storage literature applies to EVs), L-STUDY+L-STUDY, L-STUDY
  - 3.1.4: L-SCOPE (three V2G domains; only the consumer domain reviewed), L-STUDY+L-CRITIQUE (two-stage office V2G; struggles with the monthly peak), L-STUDY
  - 3.2: L-SCOPE (back-reference to 2.3.1)
  - 3.2.1: L-SCOPE+OTHER(definition), L-STUDY+L-STUDY (one with SDP for the demand charge, 36.1 % cost increase if ignored), L-RELEVANCE+L-STUDY
  - 3.2.2: L-SCOPE, L-STUDY+L-STUDY, L-STUDY+L-STUDY+L-SYNTH, L-STUDY
- **Per subsection:**

| Sub | Studies cited | Told in depth (≥2 sent.) | Paras opening with author name | Critique phrasing | Ends with |
|---|---|---|---|---|---|
| 3.1.1 | 5 | 3 | 0 (opens with "A study done by …") | none | mixed observation (new chargers also help) |
| 3.1.2 | 4 | 2 | 0 | none | synthesis sentence |
| 3.1.3 | 5 | 5 | 2 | none | summary of end-user motives |
| 3.1.4 | 3 | 2 | 1 | difficulty reported from the study itself | one-sentence extra study |
| 3.2.1 | 4 | 3 | 0 | none | a study's % result |
| 3.2.2 | 5 | 5 | 2 (+1 opening with a bare reference number) | none | a study's finding, no link drawn |

- **Paragraph length:** average ≈ 110 words; shortest ≈ 30; longest ≈ 270
- **Figures and tables:** 0; no comparison table
- **Numbers from other studies:** 16 (shares of electricity use, penetration thresholds, peak increases, cost reductions)
- **Own work mentioned:** ≈ 2 sentences (chapter purpose; focus on consumer domain)
- **Chapter-type specifics (LIT):** search strategy not described; no taxonomy opener; no comparison table; no gap or contribution section; critique is almost always the reviewed study's own limitation, not the authors' assessment.
- **What makes this chapter strong:**
  - Several subsections open with a one-paragraph scope that also says *why* the theme matters for the thesis (e.g. EV battery = flexible load, so storage literature is admissible). Short justification paragraphs like this make an otherwise adjacent literature legitimate.
  - The demand-charge subsection picks studies that show the size of the stake (cost increase when the monthly charge is ignored), which motivates the SDDP future-cost approach without saying so outright.
  - The last study (notice times vs forecast quality) states both sides of the trade-off the thesis tests, so the reader arrives at the model knowing what to expect.
- **Weaknesses:** study-by-study listing with little comparison; no explicit gap, no L-OWN links; repeats the intro's hook numbers verbatim in content.
- **Signal phrases:** "From the literature, it is evident"; "The studies presented show that"

### 4 Optimization Theory and Literature Review [THEORY + LIT]
- **Purpose in one line:** first teaches LP, duality, multistage SP, SDP/SDDP and MPC (rolling vs receding horizon); then reviews how those methods were used for EVs, storage and demand charges, ending at the RH+SDDP combination the thesis uses.
- **Opening paragraph does:** T-SCOPE — theory first, then how earlier studies applied it.
- **Closing paragraph does:** L-SYNTH — the RH+SDDP combination is presented as a promising way to combine long-term planning with real-time operation.
- **Subsections (in order):** unnumbered divider "Optimization Theory": 4.1 Deterministic programming (4.1.1 LP, 4.1.2 dual); 4.2 Stochastic programming (4.2.1 MSSP, 4.2.2 decomposition: SDP vs SDDP); 4.3 MPC (ROH vs RH horizons). Divider "Optimization Literature Review": 4.4 Model approaches (4.4.1 aggregated vs individual EV models; 4.4.2 MPC and control techniques; 4.4.3 SDDP; 4.4.4 combining RH and SDDP).
- **Paragraph moves (in order, per subsection):**
  - intro: T-SCOPE
  - 4.1: T-CONCEPT
  - 4.1.1: T-CONCEPT, T-FORMAL (generic LP with symbols explained)
  - 4.1.2: T-CONCEPT+T-PROPERTY (duals for sensitivity)
  - 4.2: T-CONCEPT
  - 4.2.1: T-CONCEPT+T-EXAMPLE (scenario tree figure)
  - 4.2.2: T-CONCEPT (state variables, Markov property), T-ALGO+T-PROPERTY (SDP recursion, curse of dimensionality), T-COMPARE (SDDP samples states; tree does not fan out, with figure), T-ALGO+T-PROPERTY (cuts from duals, forward/backward pass, non-convexity drawback)
  - 4.3: T-CONCEPT+T-RELEVANCE, T-CONCEPT (three horizons in ROH, figure), T-COMPARE (RH: prediction horizon length trade-off), T-ALGO
  - 4.4: L-SCOPE
  - 4.4.1: L-TAXONOMY (aggregated vs individual), L-STUDY (+ block quote), L-PAIR, L-SYNTH
  - 4.4.2: L-TAXONOMY+L-CRITIQUE (other feedback-control methods and their weaknesses), L-STUDY+L-STUDY, L-STUDY+L-NOTCOVERED (rolling horizon study without demand charge), L-STUDY+L-CRITIQUE (stochastic RH too heavy; suggests decomposition), L-SYNTH
  - 4.4.3: L-RELEVANCE+L-STUDY (SDDP in hydropower; Markov-chain price state to avoid non-convexity), L-PAIR (two non-hydro SDDP uses and why SDDP was chosen), L-STUDY+L-CRITIQUE (cuts captured the peak cost only approximately)
  - 4.4.4: L-RELEVANCE+L-OWN (picks up the decomposition suggestion from 4.4.2), L-STUDY+L-CRITIQUE, L-STUDY, L-SYNTH
- **Per LIT subsection:** 4.4.1 cited 3 / depth 2 / author openers 0 / ends L-SYNTH; 4.4.2 cited 7 / depth 5 / 0 / ends L-SYNTH; 4.4.3 cited 5 / depth 3 / 0 / ends study + accuracy caveat; 4.4.4 cited 3 / depth 2 / 0 / ends L-SYNTH.
- **Paragraph length:** average ≈ 95 words; shortest ≈ 30; longest ≈ 290 (4.2.2 SDP/SDDP block)
- **Figures and tables:** 3 figures (scenario tree; SDDP "non-fanning" tree; ROH vs RH horizon panels), all introduced before shown; the SDDP tree gets a one-sentence observation; 1 equation block.
- **Numbers from other studies:** 5
- **Own work mentioned:** ≈ 2 sentences
- **Chapter-type specifics (THEORY):** theory is generic and short (LP in one equation, duality in two sentences, SDDP in prose without equations); the T-RELEVANCE moves are mostly left to the lit-review half.
- **What makes this chapter strong:**
  - Theory and method literature sit in one chapter under two dividers, and the literature half narrows step by step (EV models → control techniques → SDDP → RH+SDDP), so the last subsection lands exactly on the thesis's own method.
  - A suggestion from one reviewed study's future work (add decomposition to stochastic RH) is carried forward and used as the motivation for the combined method two subsections later. Reusable: harvest "future work" sentences from the literature as the bridge to your method.
  - Most lit subsections close with a short paragraph that turns the studies into a design choice (aggregate EVs; avoid rolling horizon because it cannot see the monthly charge).
- **Weaknesses:** SDDP is explained without formulas or cut equation (the cut appears only in ch. 5); duality, which the cuts depend on, gets two sentences; one figure reference points to the wrong panel.
- **Signal phrases:** "An important observation from the figure"; "As suggested by"

### 5 Method [FRAME + MODEL + SOLVE]
- **Purpose in one line:** presents the system, the daily-stage LP with the monthly peak as the only state variable, the SDDP algorithm that builds peak cuts, and the RH loop that uses them and reveals throttling signals.
- **Opening paragraph does:** D-INTRO — what the model minimises and that motivations and assumptions are given.
- **Closing paragraph does:** S-ALGO — how a throttling signal is switched on at notice time and removed after the activation hour.
- **Subsections (in order):** 5.1 Model description (5.1.1 overview, 5.1.2 setup, 5.1.3 notation, 5.1.4 decomposed problem: objective, constraints) → the stage problem; 5.2 SDDP framework (5.2.1 algorithm, 5.2.2 future cost curves) → strategy phase; 5.3 RH algorithm and framework → simulation phase.
- **Paragraph moves (in order, per subsection):**
  - 5.1: D-INTRO
  - 5.1.1: M-OVERVIEW+M-RATIONALE (hourly decisions, monthly tariff, daily stages, single state), M-RATIONALE (why SDDP on top of RH), M-WORKFLOW (block figure: input → model setup → SDDP → RH)
  - 5.1.2: D-INTRO+D-ASSUMP (system figure; unlimited grid exchange), D-ASSUMP (EVs aggregated into one virtual vehicle, figure)
  - 5.1.3: D-NOTATION (one line + lists of sets, parameters, variables with units)
  - 5.1.4.1: D-OBJ (each term tied to an equation line)
  - 5.1.4.2: D-INTRO (constraints grouped by system part); Loads: D-CONSTR, D-ASSUMP (no efficiency: losses already in measured data), D-CONSTR; EVPL: D-CONSTR; V2G: D-ASSUMP, D-ASSUMP+D-CONSTR, D-CONSTR+D-ASSUMP (no binary for simultaneous charge/discharge, justified by losses), D-CONSTR; Grid tariff: D-CONSTR, D-CONSTR, D-CONSTR (cut constraint); Throttling: D-CONSTR, D-CONSTR
  - 5.2: OTHER(bridge: places the section in the workflow figure)
  - 5.2.1: S-WHY+D-ASSUMP (SDDP ignores throttling signals), [Algorithm 1 = S-PSEUDO], S-STOP (cuts repeat within ε three times), S-ALGO (line-by-line forward and backward pass, single-cut averaging)
  - 5.2.2: S-FIG (cuts → piecewise envelope → its slope as marginal future cost)
  - 5.3: M-OVERVIEW, S-WHY (why neither pure rolling nor fixed receding horizon works; hybrid), S-ALGO (three horizons), S-FIG+S-ALGO (cuts represent the time beyond the prediction horizon; horizon expands when prices clear), S-ALGO (states stored and passed hour to hour; flow chart), S-ALGO (signal revealed at notice time)
- **Paragraph length:** average ≈ 70 words; shortest ≈ 25; longest ≈ 250 (algorithm walk-through)
- **Figures and tables:** 6 figures + 1 algorithm; all introduced before shown; workflow, system and horizon figures are explained in the text, not only captioned.
- **Chapter-type specifics (MODEL):** citations in the model text 0 (one figure caption cites a source; the algorithm is said to be adapted from Paper I). Constraint order: load balance → daily EV energy → EVPL capacity → V2G capacity, balance, daily recharge → peak ≥ hourly import, peak ≥ initial peak, cut constraint → throttling limits. Typical constraint explanation: 1–3 sentences (what it ensures + where the parameter comes from). Assumptions: 6 stated inline; a consequence is given for 2 (losses in data; no binary because losses make simultaneous charge/discharge unprofitable); direction of bias never given. Numbers: one (ε). Notation is given as lists with units, not tables.
- **What makes this chapter strong:**
  - One workflow figure is set up early and every later section places itself in it (which side of the figure), so the reader always knows which phase is being described.
  - Constraints are grouped under plain run-in headings by system part (Loads, EVPL, V2G, Grid tariff, Throttling) and each gets a one- or two-sentence purpose, which keeps a long constraint list readable.
  - The pseudocode is followed by a line-number walk-through (stop rule, then forward lines, then backward lines), so the algorithm is explained in prose the reader can match line by line.
  - The cut envelope is turned into its slope, a "marginal future cost curve", before any result is shown; this defines the main lens of the results chapter in the method chapter.
  - The RH section argues the design by elimination: rolling horizon cannot see the monthly charge, a fixed month-long horizon cannot see tomorrow's prices, so a hybrid with SDDP cuts is used.
- **Weaknesses:** all SDDP equations live in the algorithm box with garbled indices; transition probabilities and cut averaging are stated loosely; the convergence test (cuts repeat) is non-standard and no bound gap is reported; "Paper I" stands in for a citation.
- **Signal phrases:** "Therefore, this methodology presents a combination"; "of no concern because"

### 6 Case Study [DATA + SCEN]
- **Purpose in one line:** states the case goal, software, data sources and treatment, tariff and IBDRP parameters, load scenarios for SDDP, RH horizon settings and the four model cases.
- **Opening paragraph does:** A-PURPOSE — restates the study goal and what the chapter will provide.
- **Closing paragraph does:** A-INSTANCES — Case 3 and its goal.
- **Subsections (in order):** 6.1 Python → tools; 6.2 Input data (office load, EVPL, price, tariff, IBDRP); 6.3 Algorithm input (stochastic office load; RH inputs; prediction horizons); 6.4 Model cases (Case 0–3).
- **Paragraph moves (in order, per subsection):**
  - intro: A-PURPOSE
  - 6.1: M-TOOLS
  - 6.2: A-SOURCE+A-PROCESS (data owner, price zone, year, interpolation)
  - 6.2.1: A-FIG (not interpreted)
  - 6.2.2: A-PROCESS+A-PARAM-TABLE, A-CASE+A-PARAM-TABLE (fuse, chargers, arrival ramp), A-PROCESS (V2G efficiency, availability assumptions)
  - 6.2.3: A-SOURCE+A-FIG+A-LIMIT (2022 was abnormal)
  - 6.2.4: A-SOURCE, A-PROCESS+A-PARAM-TABLE (tariff variant, neglected reactive charge, derived constants)
  - 6.2.5: A-CASE+A-SOURCE (real DSO programme, discount table), A-PROCESS (signal range, one-hour activation)
  - 6.3.1: A-SCEN+A-LIMIT (three load levels ±30 %, stagewise-independent probabilities; admits values are arbitrary)
  - 6.3.2: A-PROCESS (two different ENS penalties: one to steer the optimiser, one for reporting)
  - 6.3.2.1: A-PROCESS (horizon lengths; expansion at price publication; figure)
  - 6.4: A-INSTANCES (overview of cases with common goal), A-INSTANCES ×4 (one paragraph per case, each with its own goal)
- **Paragraph length:** average ≈ 90 words; shortest ≈ 30; longest ≈ 190
- **Figures and tables:** 5 figures (each two panels, March and September), 4 tables; all introduced before shown; data figures interpreted: 0 of 4 fully (the price figures get one caveat sentence; the load figures none).
- **Chapter-type specifics (DATA/SCEN):** sources named for every input; data treatment (averaging weekdays, interpolation) stated; scenario generation is three fixed levels, not fitted; instance list has a goal per case (yes); limitations of the data mentioned for 2022 prices and for arbitrary scenario values, without stated implications.
- **What makes this chapter strong:**
  - Each case gets its own short subsection opening with its goal and what it changes relative to an earlier case ("an extension of C1"), so the cases form a visible ladder.
  - The thesis separates a steering penalty (large, to force delivery) from a reporting penalty (moderate, to keep costs comparable) and explains why, which is a clean way to handle slack costs in reported results.
  - The real tariff and the real DSO programme are tabulated with sources, so every economic number later can be traced.
- **Weaknesses:** data figures are shown without any observation; scenario values are openly arbitrary and their effect is not tested; a table is mis-aligned in the source text (?).
- **Signal phrases:** "chosen quite arbitrarily"; "This case is an extension of"

### 7.1–7.4 Results and Discussion [RES]
- **Purpose in one line:** for each case, reads the SDDP marginal-cost curves, then hourly and monthly operation, then costs, then a marginal-cost sensitivity to throttling depth.
- **Opening paragraph does:** R-AIMS — what is covered; only operating costs counted.
- **Closing paragraph does:** R-OBS+R-INTERP — the 0 h notice curve in Case 3 rises to the ENS penalty; the system is willing to raise the peak until demand cannot be met.
- **Subsections (in order):** 7.1 Case 0 (future cost curves; operational impact; four peak-cost approaches compared); 7.2 Case 1 IBDRP (operation under signals; peak increase; daily operation; economics; sensitivity, every-weekday signal; marginal cost, single signal); 7.3 Case 2 V2G (future cost curves; 12 h operation; operation under signals; costs; marginal cost; challenges with V2G); 7.4 Case 3 DCCR (future cost curves; change in planning; operation; potential of 0 and 2 h; economics; marginal cost).
- **Order of result subsections:** within every case: strategy (cut curves) → operational (average profiles, then single days) → economic (cost table) → sensitivity (marginal cost vs throttling). No technical subsection (no solver, runtime, iterations or convergence reported).
- **Paragraph moves (in order, per subsection):**
  - intro: R-AIMS
  - 7.1: R-AIMS
  - 7.1.1: R-KEYREL (how marginal curves are computed from the cuts), R-OBS+R-INTERP, R-OBS+R-INTERP (later days lie closer to the demand charge, as expected), R-OBS+R-INTERP+R-STOCH (stochastic vs deterministic cuts), R-OBS+R-INTERP+R-CAVEAT (cuts accurate only near visited peaks; SDP as alternative), R-OBS+R-INTERP (curve jump traced back to a load spike in the data figure)
  - 7.1.2: R-OBS (figure set-up), R-OBS+R-INTERP (charging pushed late; explained by price and load profiles from ch. 6)
  - 7.1.3: R-AIMS (four benchmarks defined: no peak cost, myopic daily minimum, deterministic cuts, stochastic cuts), R-OBS (figure legend), R-OBS+R-INTERP ×5 (one paragraph per benchmark and month, each opening with what was expected), R-SUMMARY+R-STOCH
  - 7.2: R-AIMS (worst case = signal every weekday; single-signal case for marginal analysis; Base Case named)
  - 7.2.1: R-OBS (set-up), R-OBS+R-INTERP, R-OBS (table set-up), R-OBS+R-INTERP+R-CAVEAT+R-IMPL (model weakness; forcing spare capacity would cost; worst case is rare)
  - 7.2.2: R-OBS, R-INTERP+R-CAVEAT (SDDP blind to signals → system one day behind in raising the peak)
  - 7.2.3: R-AIMS, R-OBS+R-INTERP, R-OBS+R-INTERP, R-OBS+R-IMPL (ENS of one day; one hour more notice would avoid it)
  - 7.2.4: R-AIMS (cost categories defined), R-OBS+R-INTERP+R-IMPL+R-CAVEAT (cost of flexibility = minimum incentive; ENS penalty arbitrary)
  - 7.2.5: R-AIMS+R-SENS, R-OBS (figure set-up), R-OBS+R-INTERP
  - 7.2.6: R-SENS (set-up), R-OBS+R-INTERP+R-IMPL (12 h flexibility is cheap for the DSO), R-OBS+R-INTERP (breaking point; hand calculation of the expected marginal cost, gap attributed to price flexibility), R-OBS+R-INTERP, R-SUMMARY+R-IMPL+R-CAVEAT (one month only)
  - 7.3: R-AIMS
  - 7.3.1: R-OBS+R-INTERP (compared with 7.1.1)
  - 7.3.2: R-OBS+R-INTERP+R-IMPL, R-OBS+R-INTERP, R-OBS+R-INTERP (share of daily EV demand that must be moved)
  - 7.3.3: R-OBS (table symbols), R-OBS+R-INTERP, R-OBS+R-INTERP (energy balance written as an equation in the text)
  - 7.3.4: R-OBS (set-up), R-OBS+R-INTERP (V2G saves almost nothing; round-trip loss explains it), R-OBS
  - 7.3.5: R-SENS (set-up), R-OBS+R-INTERP+R-IMPL, R-OBS+R-INTERP (an unexpected dip flagged for later), R-OBS+R-INTERP, R-OBS+R-INTERP (dip explained with a zoomed figure and a day-by-day plot)
  - 7.3.6: R-AIMS, R-OBS, R-OBS+R-INTERP+R-IMPL (ENS +271.9 % with V2G), R-OBS+R-INTERP, R-CAVEAT (battery degradation omitted; back-reference to 2.4.1.2), R-CAVEAT (8-hour presence assumption needs owner commitment)
  - 7.4: R-AIMS (why V2G is left out of Case 3)
  - 7.4.1: R-OBS, R-OBS+R-INTERP
  - 7.4.2: R-AIMS+R-OBS, R-OBS+R-INTERP, R-OBS+R-INTERP
  - 7.4.3: R-OBS (table set-up), R-OBS+R-INTERP, R-OBS+R-INTERP (expected peak rise explained by the discount)
  - 7.4.4: R-AIMS, R-OBS+R-INTERP, R-OBS+R-INTERP+R-IMPL, R-IMPL+R-SUMMARY (benefit depends on three named conditions)
  - 7.4.5: R-OBS (set-up), R-OBS+R-INTERP+R-IMPL (1.8 % saving even in worst case), R-OBS+R-INTERP (an expectation stated in 7.4.3 is checked and turns out reversed)
  - 7.4.6: R-SENS (set-up), R-OBS+R-INTERP, R-OBS+R-INTERP (dip linked to 7.3.5; stochastic cuts treat the peak rise as too risky)
- Paragraphs in the repetitive figure/table set-up role (name the figure, then define each line colour) are coded R-OBS individually above; ≈ 20 of the 80 paragraphs are pure set-up.
- **Paragraph length:** average ≈ 100 words; shortest ≈ 30; longest ≈ 250
- **Figures and tables:** 24 figures, 7 tables; all introduced before shown (often by a full set-up paragraph that defines colours and symbols); OBS→INTERP→IMPL complete for ≈ 11 of 24 figures (?); nearly all get OBS+INTERP; IMPL is most often a statement for the DSO or the building owner about notice time.
- **Chapter-type specifics (RES):** R-TECH absent; R-KEYREL present (marginal curve explained before reading it); R-LIT 0; R-SENS in all three IBDR cases; R-STOCH only as deterministic-vs-stochastic cuts in-sample (no out-of-sample test); R-CAVEAT frequent and specific.
- **What makes this chapter strong:**
  - Every case repeats the same internal order (cut curves → operation → costs → marginal sensitivity), and later cases explicitly compare to the earlier one by section number. Readers learn the pattern once and then only look for differences.
  - The SDDP cuts are read through their slope: a zero region (raising the peak is free because a later day will set it anyway), a steep rise, and a plateau at the demand charge. Each zone is given a physical meaning for the operator. Directly reusable for reading water values or peak cuts.
  - Expected-vs-observed framing: many paragraphs begin with what should happen (e.g. the no-peak-cost benchmark should give the highest peak) and then confirm it from the table, so a result reads as a test.
  - Hand calculation inside the text: the expected marginal cost is computed from the tariff and the observed peak-rise rate, and the gap to the plotted value is attributed to spot-price flexibility. A one-line decomposition of a dual-like quantity into its parts.
  - Anomalies are not hidden: an unexpected dip is flagged, then explained in a later paragraph with a higher-resolution plot and the operation of the affected days, and tied back to the stochastic cuts.
  - A benchmark ladder (ignore the charge / myopic daily minimum / deterministic cuts / stochastic cuts) shows the value of the cuts with one small table before the main cases.
- **Weaknesses:** no runtime, iterations or convergence evidence; no out-of-sample evaluation of the SDDP policy; results never compared with literature; some numbers missing or inconsistent in the text (one approximate value with the number missing; one table referenced by a wrong number).
- **Signal phrases:** "This is as expected, as"; "To summarize, it can be seen"; "Similar to C1 in Section"

### 7.5 General Discussion [DISC]
- **Purpose in one line:** revisits the main assumptions (worst-case signals, V2G costs, ENS penalty, EV aggregation, SDDP vs SDP, activation hour) and what they mean for the results.
- **Opening paragraph does:** X-ASSUMP — says the section discusses how assumptions affect results.
- **Closing paragraph does:** X-ASSUMP+X-LIMIT — a more realistic activation hour and several activations per day would tighten the system further.
- **Subsections (in order):** none (9 paragraphs).
- **Paragraph moves (in order):** X-ASSUMP, X-ASSUMP (worst case chosen to test maximum strain), X-IMPL (no signal = pure saving for the building, insurance for the DSO), X-ASSUMP+X-IMPL (V2G: charger cost, degradation, month choice, all-EVs-bidirectional), X-ASSUMP+X-IMPL (ENS cost depends on contracts; alternatives), X-METHOD+X-ASSUMP (aggregation vs individual EVs; computational cost), X-METHOD+X-CONTEXT (SDDP vs SDP with one cited study; SDP better for out-of-range peaks), X-ASSUMP (hour 12 choice; an earlier hour would reduce ENS), X-ASSUMP+X-LIMIT
- **Paragraph length:** average ≈ 105 words; shortest ≈ 30; longest ≈ 185
- **Numbers from other studies:** 0
- **What makes this chapter strong:**
  - Each assumption paragraph states the direction of the effect if the assumption changed (earlier activation hour → less ENS; more activations → tighter system; another month with more price spread → more V2G value).
  - Method self-critique ties back to a result: SDDP's sparse cuts outside the visited range matter precisely because throttling pushes the peak there, so SDP is named as the better fit for this specific use.
- **Weaknesses:** almost no comparison with other studies (one citation); no generalisability paragraph; limitations not separated from assumptions.
- **Signal phrases:** "It can therefore be discussed if"

### 8 Conclusion [CONCL]
- **Purpose in one line:** restates what was built and gives one paragraph of findings per case group with the headline number.
- **Opening paragraph does:** C-PROBLEM+C-DONE+C-FIND-OP — what was examined, the SDDP+RH model, and that the cuts are accurate in the normal range but not at outlying peaks.
- **Closing paragraph does:** C-FIND-ECON — the existing discount programme with 12 h notice lowers operating cost by 1.8 %.
- **Paragraph moves (in order):** C-PROBLEM+C-DONE+C-FIND-OP, C-FIND-OP+C-FIND-ECON (12 h handles signals at 0.57 %; marginal flexibility cost is tiny for the DSO; short notice fails), C-FIND-OP+C-FIND-ECON+C-OVERALL (V2G constrains further; 3.2 %; notice time is essential), C-FIND-ECON
- **Paragraph length:** average ≈ 105 words
- **Chapter-type specifics (CONCL):** C-ANSWER n/a (no RQs); findings follow the contribution bullets and Cases 1–3 in order, with numbers; no C-GAP, no C-LIMIT beyond the cut-accuracy remark; future work in a subsection.
- **What makes this chapter strong:**
  - One paragraph per case, each with one number and one implication for the DSO or building owner; very easy to map back to the contribution list.
- **Weaknesses:** one paragraph names the wrong pair of notice times as insufficient (contradicts the results) (?); no overall answer to the aim beyond the last paragraph.

### 8.1 Further Work [FUT]
- **Extensions (F-EXT) and parts present (what / why limit / effect / cost):**
  1. Stochastic scenarios in the RH loop — what yes; why (RH uses deterministic data) yes; effect no; cost no.
  2. Forecast of likely throttling hours — what only.
  3. Another decomposition method — what; why = comparison only.
  4. Sensitivity on notice times beyond the three in the programme — what; why (only three tested) yes.
  5. Other activation hours — what only.
  6. Non-aggregated EVPL — what; why (aggregated) yes; effect (more realistic) yes; cost (much data) yes. The only complete item.
  7. Marginal flexibility-cost curves as price information for DSOs — what; why (reflect true flexibility cost) yes.
- **What makes it useful:** item 6 shows the full four-part pattern in two sentences; item 7 turns a result artefact (marginal-cost curves) into a policy use.

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** dense numbered back-references (model → tariff section 2.2.3; algorithm → theory 4.2.2; results → data figures 6.2.1/6.2.3; later cases → earlier case sections). One workflow figure (5.1.1) anchors the method and is referenced by later sections. Fixed terms and abbreviations (BC, C0–C3, DCC, DCCR, ENS, PH/CH/SH) defined once and used throughout. The SDDP outer-range inaccuracy recurs as a thread: theory (SDDP explores "interesting" states) → result 7.1.1 → 7.3.1 → discussion (SDP alternative) → conclusion opening. A reviewed study's future-work suggestion (4.4.2) becomes the motivation for the combined method (4.4.4, 5.1.1).
- **How the RQs or objectives are answered in the conclusion:** no RQs; the conclusion follows the contribution bullets and Cases 1–3 in order, one paragraph each, each with a headline percentage.
- **Anything a strong thesis does that the codes do not capture:**
  - Results chapter uses a two-scenario design per case: a worst-case stress test (signal every weekday) for operation and cost, and a single-signal test for marginal cost. Stating why each design is used at the top of the case.
  - Two penalties for the same slack (one to steer, one to report) keep the reported costs comparable.
  - Cases are built as a cumulative ladder (C0 baseline → C1 adds signals → C2 adds V2G → C3 adds the incentive instead of V2G), with the reason for excluding V2G from C3 stated.
  - Theory and method literature are merged in one chapter, the literature half funnelling to the exact method used; the domain literature review is separate and earlier.
  - Weaknesses to avoid: no explicit gap section; no computational evidence for SDDP; no out-of-sample policy test; data figures without interpretation; scenario values called arbitrary without a sensitivity check.
