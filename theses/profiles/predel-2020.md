# predel-2020 — Johannes Predel and Bobby Xiong, 2020
- File: theses/texts/the-potential-of-power-to-gas-for-congestion-management.txt
- Type: monograph (hybrid: ch. 6 and ch. 7 are each derived from one submitted journal article, Applied Energy and Energy Economics; leftovers such as "this paper" remain in several chapters)
- Topic: German day-ahead market followed by cost-based redispatch (sequential LP, DC power flow, 24 h rolling horizon, full year, 427 nodes); Power-to-Gas as a redispatch flexibility option; plus a qualitative legal analysis of whether system operators may own/operate PtG in Germany and the US. Co-authored master's thesis (SESAM, NTNU/TU Berlin), July 2020.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: low-medium (sequential market stages, storage modelling, data assumptions with direction of bias, calibration against historical statistics; no stochastic method)
- Citation style: author-year
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 24,400 prose words (≈ 27,700 raw incl. table and figure-axis text)
- Research questions stated explicitly: yes (2 RQs, bulleted; in the Summary and in ch. 3 Problem description, not in the Introduction, which instead names two numbered "research components" I and II)

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| – | Preface | PRE | 32 | 330 | – | 6 | 0 | 0 |
| – | Summary (+ Norwegian Sammendrag) | ABS | 72 | 390 | – | 4 | 0 | 0 |
| 1 | Introduction (1.1 Thesis structure, 1.2 Electricity markets, 1.3 The need for ancillary services) | INTRO+BACK | 434 | 3,000 | 12 % | 19 | 1 | 1 |
| 2 | Literature review | LIT | 758 | 2,600 (+≈600 in tables) | 11 % | 20 | 0 | 2 |
| 3 | Problem description | PROB | 1115 | 1,250 | 5 % | 10 | 1 | 0 |
| 4 | Technical background (power flow theory; PtG technology) | BACK+THEORY | 1263 | 3,100 | 13 % | 26 | 2 | 3 |
| 5 | Model framework | MODEL (+FRAME opening, SOLVE-style 5.3) | 1770 | 2,300 | 9 % | 32 | 1 | 0 |
| 6 | Spatial flexibility in redispatch (article 1) | DATA+RES (+VALID inside results, own chapter conclusion) | 2159 | 5,600 | 23 % | 42 | 16 | 4 |
| 7 | Exploring PtG implementations in regulated electricity markets (article 2) | BACK+RES (qualitative legal analysis; closest codes) | 3061 | 4,800 | 20 % | 37 | 1 | 3 |
| 8 | Concluding remarks (8.1 Critical reflection, 8.2 Further research, 8.3 Conclusion) | DISC+FUT+CONCL | 3637 | 1,700 | 7 % | 17 | 0 | 0 |
| A–D | Additional figures; Additional data; Modified IEEE-RTS24 test case (two small case studies); Model code | APP | 3805 | – | – | – | 16 | 4 |

Note on order: Problem description (ch. 3) comes before Technical background (ch. 4), and no separate data chapter exists: data sit inside the article-derived results chapter (6.1). A small validation-like test case (IEEE-RTS24) is pushed to Appendix C.

## 2. Chapters

### Summary [ABS]
- **Paragraph moves:** AB-CONTEXT+AB-PROBLEM (renewable growth, north–south transport, congestion, curtailment, lagging grid expansion) + AB-WHY (sector coupling shifts load to gas system); AB-PROBLEM + OTHER(two RQs listed as numbered items); AB-METHOD+AB-CASE (sequential market + CM model, 24 h foresight, Germany; second part compares Germany and US regulation); AB-RES-OP (12 % less curtailment, few locations benefit) + AB-IMPL (regulatory classification is the barrier).
- No economic result (cost savings are tiny and omitted); one headline number only.

### 1 Introduction [INTRO+BACK]
- **Purpose in one line:** Motivate redispatch costs and PtG, name the two research components, outline the thesis, and give market and ancillary-service background for Germany.
- **Opening paragraph does:** I-CONTEXT — Energiewende, renewables built where resources are, far from load; a sourced statement about planned grid expansion.
- **Closing paragraph does:** B-DEF+B-SUMMARY — balancing energy distinguished from redispatch, then a summary table of all TSO measures (service, procurement, measure type, legal basis).
- **Subsections (in order):** (unnumbered intro) → driver, problem, PtG idea, regulatory question, two components; 1.1 Thesis structure → chapter-by-chapter outline; 1.2 Electricity markets → market properties, merit order, uniform vs discriminatory auction, nodal vs zonal, DA/ID timing; 1.3 The need for ancillary services → grid-related, market-related (redispatch, countertrading, curtailment) and operational measures in German law.
- **Paragraph moves (in order, per subsection):**
  - intro: I-CONTEXT, I-HOOK+I-PROBLEM (own figure from regulator data: CM cost near one billion euro, curtailment share of cost 50 % → 75 %), I-CONCEPT+I-PROBLEM (PtG as sector coupling; whether regulated TSOs may use it), I-AIM+I-REUSE (two components I/II, term "spatial flexibility" coined, footnote with the two article submissions)
  - 1.1: I-OUTLINE
  - 1.2: B-FACT+B-MECH (liberalisation; bullet list of special properties of electricity), B-MECH (supply, demand, grid as natural monopoly), B-MECH (nodes, unbundling), B-DEF+B-MECH (merit order, uniform vs discriminatory, one study told), B-DEF+B-MECH (nodal pricing/LMP, country examples), B-MECH+B-BRIDGE (zonal pricing, copper plate, ex-post adjustment pointed to 1.3), B-SCOPE (German focus), B-FACT+B-MECH (DA and ID gate times and products)
  - 1.3: B-SCOPE+B-DEF (three categories of TSO measures), B-DEF (grid-related), B-DEF+B-MECH (redispatch, cost-based in Germany), B-MECH+B-MODELLING (opportunity cost compensation; one method from the literature for valuing it), B-MECH+B-FACT (countertrading, RE curtailment and compensation rules), B-DEF+B-SUMMARY (balancing energy; Table 1.1)
- **Paragraph length:** average ≈ 150 words; shortest ≈ 35; longest ≈ 280
- **Figures and tables:** 1 figure, 1 table; both introduced in the text before/at the point shown; Fig. 1.1 gets observation → interpretation (cost share rising) → implication (counterproductive for decarbonisation): 1 of 1 complete.
- **Numbers from other studies (background part only):** ≈ 3 (compensation percentages from the renewable energy act; most numbers are in the intro hook from the regulator's statistics)
- **Own work mentioned (background part only):** 3 sentences (German focus, own naming of the uniform price, pointer to 1.3)
- **Chapter-type specifics (INTRO):** hook = own two-panel figure (volume vs cost) built from five years of regulator reports; RQs not in the intro (only "components I and II"); no explicit contribution list, no findings preview, no scope paragraph; reuse declared in a footnote naming journals and article titles.
- **What makes this chapter strong:**
  - The hook figure is read twice: volume shows curtailment is the smaller measure, cost shows it is the growing problem — the contrast does the motivating.
  - The two research components are numbered I and II and map one-to-one onto the two analysis chapters (6 and 7) and the two article submissions, which keeps the thesis split clean.
  - Background concepts each get a bold run-in heading (auction type, nodal/zonal, DA/ID), are defined in general, then pinned to the German case in the last sentences.
  - The ancillary-services section ends with a classification table (service, procurement, legal basis) that the problem description and ch. 7 can lean on.
- **Weaknesses:**
  - RQs are absent from the introduction; a reader meets them only in the Summary and ch. 3.
  - Background is folded into the introduction chapter, making it long (12 %) and mixing motivation with textbook content; nodal pricing is explained again in 7.1 almost identically.
  - Article leftovers ("this paper", "our paper") in a thesis.
- **Signal phrases:** "Meanwhile, flexibility potentials" · "the question arises whether" · "we refer to this type"

### 2 Literature review [LIT]
- **Purpose in one line:** Classify flexibility options, place PtG in that classification, review PtG energy-system models, and derive three gaps.
- **Opening paragraph does:** L-SCOPE+L-SEARCH — names the two themes and the databases searched (Web of Science, Scopus, Google Scholar).
- **Closing paragraph does:** L-GAP+L-CONTRIB — third gap (regulation ignored by models assuming one benevolent optimiser) filled by ch. 7.
- **Subsections (in order):** 2.1 Flexibility → definitions and a six-way taxonomy of flexibility with run-in headings, ending with PtG positioned as demand-side; 2.2 PtG in energy system models → one study per paragraph plus a two-part comparison table; 2.3 Research gaps and contribution → three gap paragraphs.
- **Paragraph moves (in order, per subsection):**
  - opening: L-SCOPE+L-SEARCH
  - 2.1: L-GROUP+L-RELEVANCE (definition of flexibility; need grows with RE), L-TAXONOMY (demand vs supply side), L-TAXONOMY+L-GROUP (transmission as flexibility, public opposition), L-TAXONOMY+L-PAIR+L-SYNTH (storage: two studies with opposite conclusions → system boundaries matter), L-TAXONOMY+L-STUDY+L-PAIR (system flexibility: one study in depth, a second confirming), L-TAXONOMY+L-PAIR (curtailment as indicator of flexibility need), L-TAXONOMY+L-PAIR+L-SYNTH+L-OWN (sector coupling; four studies; PtG adopted as demand-side flexibility)
  - 2.2: L-SCOPE+L-TABLE (models in Tables 2.1–2.2; pointer to an existing review), L-STUDY (MILP storage comparison, Netherlands), L-STUDY (optimal PtG siting, Germany), L-STUDY (regional PtG, Denmark), L-STUDY (non-linear gas–electricity model, GB), L-STUDY+L-CRITIQUE (a study that itself criticises others for ignoring uncertainty; one more study in a sentence), L-STUDY (PtG + CHP smoothing), L-STUDY (PtG–GfG real-time scheduling with a compensation mechanism), L-STUDY (pumped hydro / Western Balkan model)
  - 2.3: L-GAP+L-CONTRIB (sequential markets + limited foresight), L-GAP+L-CONTRIB+L-OWN (spatial side of flexibility in redispatch; pointer to ch. 6), L-GAP+L-CONTRIB (regulation; pointer to ch. 7)
- **Per LIT subsection:**
  - 2.1: studies cited ≈ 23 · told in depth ≈ 8 · paragraphs opening with author name 0 (all open with a run-in theme heading) · critique: almost none; contrast phrased as differing outcomes · ends with L-OWN (positioning PtG).
  - 2.2: studies cited ≈ 13 (incl. table-only) · told in depth 8 · paragraphs opening with author name 4 · critique: only one, reported second-hand from a reviewed study · ends with a single study (no synthesis).
  - 2.3: studies cited 2 · told in depth 0 · author-name openings 0 · critique phrased as "existing models either … or …" and "often neglected" · ends with contribution + chapter pointer.
- **Paragraph length:** average ≈ 120 words; shortest ≈ 50; longest ≈ 270
- **Figures and tables:** 0 figures, 2 tables (one table split in two); introduced before shown: yes; tables are not interpreted afterwards, and the gap section does not refer back to table columns.
- **Numbers from other studies:** ≈ 16 (≈ 3 in 2.1, ≈ 13 in 2.2: shares of RE, GW ranges, % cost and curtailment reductions)
- **Own work mentioned:** ≈ 12 sentences (2 in opening, 1 at end of 2.1, 1 in 2.2, ≈ 8 in 2.3)
- **Chapter-type specifics (LIT):** themes = (1) flexibility taxonomy, (2) PtG models; taxonomy opener used in 2.1; comparison table columns (sequential markets, CM, PtG, grid representations, region) encode the gap; three gaps, each bound to a chapter.
- **What makes this chapter strong:**
  - Taxonomy first, own technology last: 2.1 walks through six flexibility types under run-in headings and ends by assigning PtG to one class, which becomes the term used throughout.
  - A two-study contrast with opposite findings is turned into a lesson for the field (results depend on system boundaries) rather than left as a list.
  - Each 2.2 paragraph has the same skeleton: method type → case/region → mechanism → quantitative result, which makes the studies comparable at a glance.
  - Comparison table with check-mark columns for exactly the features the thesis adds (sequential markets, CM, PtG) lets the gap be seen before it is stated.
  - Gap section: three paragraphs, each = one gap + how we fill it + which chapter; the third gap justifies the whole non-model half of the thesis.
- **Weaknesses:**
  - 2.2 is study-by-study with almost no own critique and ends on a loosely related study instead of a synthesis.
  - The key predecessor for the sequential approach appears only in the table and the gap paragraph, never told in depth.
- **Signal phrases:** "show the importance of system boundaries" · "existing models either capture" · "we contribute by taking into account"

### 3 Problem description [PROB]
- **Purpose in one line:** Stand-alone, symbol-free description of the two-stage problem (market clearing, then congestion management with/without PtG) and the regulatory question.
- **Opening paragraph does:** P-PURPOSE — says what the chapter covers (objective, scope, decisions, information, restrictions) and that it should be readable alone.
- **Closing paragraph does:** P-DECISIONS+P-CONSTRAINTS + OTHER(regulatory task stated) — PtG decisions in the CM variant, then what the legal analysis must determine.
- **Subsections (in order):** (unnumbered) purpose, RQs, PtG concept, two-stage structure figure, benchmark vs PtG variant; 3.1 Replicating the day-ahead spot market; 3.2 Managing congestion with redispatch; 3.3 Integrating PtG as flexibility option.
- **Paragraph moves (in order, per subsection):**
  - intro: P-PURPOSE, P-PURPOSE+P-ACTOR+OTHER(two RQs bulleted), P-SYSTEM (PtG two steps, SNG via gas grid to GfG units), P-MARKETS+P-DECISIONS+P-SCOPE (uniform price copper plate vs physical limits → two-stage approach; capacities fixed, no outages), OTHER(benchmark variant vs PtG variant, tied to the figure)
  - 3.1: P-MARKETS+P-OBJECTIVE (cost-minimal merit-order dispatch, inelastic demand), P-CONSTRAINTS+P-DECISIONS (capacity bound; must-run excluded; outputs and price per step)
  - 3.2: P-OBJECTIVE+P-DECISIONS+P-CONSTRAINTS (redispatch cost and compensation rule in words; ramping, capacity), P-CONSTRAINTS+P-SCOPE (DC approximation of AC flows)
  - 3.3: P-DECISIONS+P-CONSTRAINTS+OTHER(regulatory task)
- **Paragraph length:** average ≈ 110 words; shortest ≈ 55; longest ≈ 250
- **Figures and tables:** 1 figure (problem stages with A = benchmark, B = PtG variant); introduced and interpreted (each half explained) — yes.
- **Chapter-type specifics (PROB):** symbols: no; numbers: no; length ≈ 3.5 pages. No P-HORIZON stated as such (daily foresight only appears in ch. 5); no P-UNCERT (deterministic, limited foresight); P-OUTPUT implicit.
- **What makes this chapter strong:**
  - It declares itself stand-alone and keeps that promise: no symbols, no numbers, jargon pushed into footnotes with pointers back to background.
  - One block figure fixes the comparison design (same first stage, two second-stage variants), which the results chapter then follows.
  - Subsections mirror the model stages one-to-one (ED → CM → PtG extension = 5.2.2 → 5.2.3 → 5.2.4), so the reader meets each stage first in words, then in equations.
  - Compensation rules (reimburse marginal cost for up, lost profit for down) are stated in plain words here, so the objective in ch. 5 needs no new explanation.
- **Weaknesses:**
  - Pumped storage is in the model but never mentioned here; must-run is excluded here but bounds the model in eq. 5.3 (resolved only in the data chapter).
  - RQs are introduced here rather than in the introduction.
- **Signal phrases:** "a standalone description of the problem" · "we apply a two-stage approach"

### 4 Technical background [BACK+THEORY]
- **Purpose in one line:** Derive DC power flow from AC power system analysis, review electrolysis and methanation technologies, and turn the review into modelling assumptions.
- **Opening paragraph does:** B-SCOPE — announces the two parts and that the chapter ends with conclusions for modelling.
- **Closing paragraph does:** B-MODELLING+B-BRIDGE+B-FIG — hydrogen buffer allows ignoring methanation minimum load; key take-aways shown in a Sankey diagram of assumed efficiencies.
- **Subsections (in order):** 4.1 Transmission system (4.1.1 Power system analysis → AC quantities and nodal injection equations; 4.1.2 Linearisation using DC power flow → three numbered assumptions → linear flow); 4.2 Power-to-Gas (4.2.1 Electrolysis → three technologies compared; 4.2.2 Methanation → biological vs catalytic; 4.2.3 From theory to modelling → modelling choices).
- **Paragraph moves (in order, per subsection):**
  - opening: B-SCOPE
  - 4.1: B-SCOPE+B-RELEVANCE
  - 4.1.1: T-CONCEPT+T-FORMAL (apparent power), T-CONCEPT+T-FORMAL (impedance, admittance), T-FORMAL (admittance matrix), T-CONCEPT (nodal injection, figure), T-FORMAL (derivation chain in short linking sentences), T-FORMAL+T-PROPERTY (active/reactive split), T-CONCEPT+B-MODELLING (per-unit system, base power used)
  - 4.1.2: T-SCOPE, T-FORMAL (three numbered approximations), T-FORMAL+T-PROPERTY (only active power and angles remain unknown)
  - 4.2: B-SCOPE (two steps; CO2 supply excluded)
  - 4.2.1: B-MECH (electrolysis reaction), B-MECH (three types listed), B-MECH+B-FACT (AEL), B-MECH+B-FACT (PEM), B-MECH+B-FACT (SOEC), B-FACT+B-RELEVANCE+B-SUMMARY ("electrolysis and flexibility"; Table 4.1), B-SUMMARY+B-RELEVANCE (Table 4.2; PEM chosen)
  - 4.2.2: B-MECH+B-FACT (reactions, efficiency), B-MECH+B-RELEVANCE (biological excluded), B-MECH+B-FACT+B-SUMMARY (catalytic reactors; Table 4.3), B-FACT+B-RELEVANCE ("methanation and flexibility")
  - 4.2.3: B-MODELLING+B-RELEVANCE (electrolysis drives PtG flexibility; storage decouples steps), B-MODELLING+B-BRIDGE+B-FIG
- **Paragraph length:** average ≈ 90 words; shortest ≈ 30; longest ≈ 380
- **Figures and tables:** 2 figures, 3 tables; all introduced before shown; Fig. 4.2 is a synthesis figure (not interpreted afterwards, it is the conclusion); tables 4.1–4.3 are each followed by a judgement sentence for PtG.
- **Numbers from other studies:** ≈ 25 (efficiencies, load ranges, start-up times, temperatures, cell counts)
- **Own work mentioned:** ≈ 16 sentences (concentrated in openings and 4.2.3)
- **Chapter-type specifics (BACK/THEORY):** theory part is a textbook derivation (one book cited for the assumptions); technology part reviews alternatives against one criterion (flexibility for redispatch).
- **What makes this chapter strong:**
  - Each technology alternative gets a run-in-headed paragraph covering the same attributes (maturity, efficiency, load range, start-up, cost), followed by a separate "… and flexibility" paragraph that judges them against the thesis' purpose.
  - A benefits / drawbacks / suitability-for-PtG table turns the review into a decision, and a literature parameter table collects values per source that later define the sensitivity range in 6.2.3.
  - The section "From theory to modelling" converts the technology review into explicit modelling simplifications (ignore minimum load, assume hydrogen buffer) with a reason for why accuracy is barely affected.
  - The DC derivation lists its approximations as numbered assumptions so the model chapter can cite equation numbers instead of re-deriving.
- **Weaknesses:**
  - The full AC derivation is longer than the model needs; mostly textbook material.
  - Placing technical background after the problem description means ch. 3 refers forward for basic concepts.
- **Signal phrases:** "From theory to modelling" · "We summarise our key take-aways"

### 5 Model framework [MODEL]
- **Purpose in one line:** Present assumptions, notation, and the LP formulations of the day-ahead dispatch, the congestion-management model and its PtG extension, plus software.
- **Opening paragraph does:** D-INTRO+M-WORKFLOW — two-stage LP, sequential clearing then hourly redispatch with 24 h foresight, rolled over 365 days (timeline figure).
- **Closing paragraph does:** S-IMPL — Julia/JuMP, R toolchain for plots, run on a university computing cluster.
- **Subsections (in order):** 5.1 Model assumptions → three run-in assumptions; 5.2 Mathematical formulation (5.2.1 Model terminology → sets/variables/parameters lists; 5.2.2 Day-ahead economic dispatch; 5.2.3 Congestion management; 5.2.4 Power-to-Gas extension); 5.3 Implementation and software toolbox.
- **Paragraph moves (in order, per subsection):**
  - opening: D-INTRO+M-WORKFLOW
  - 5.1: D-ASSUMP (intro), D-ASSUMP (ramping: numbers show it is non-binding hourly; consequence and constraint savings stated), D-ASSUMP (no cross-border trade: why historic flows distort price; what is lost stated), D-ASSUMP (single virtual SNG storage; future-research pointer, no consequence)
  - 5.2: D-NOTATION (typographic convention)
  - 5.2.1: D-NOTATION (sets), D-NOTATION (variables), D-NOTATION (parameters; overline marks first-stage results fixed in second stage)
  - 5.2.2: D-INTRO (ED, copper plate, no binaries so price = dual), D-OBJ, D-CONSTR (market clearing), D-CONSTR (generation bounds), D-CONSTR (pumped storage: pump, turbine, level, balance), D-CONSTR (non-negativity)
  - 5.2.3: D-INTRO (CM follows an earlier formulation), D-OBJ (profit-neutral redispatch cost, storage and lost load), D-CONSTR (dispatch composition), D-CONSTR (nodal balance and angles), D-CONSTR (line flow with reliability margin), D-CONSTR+D-LINEAR (bounds that avoid simultaneous up/down without binaries), D-CONSTR (non-negativity)
  - 5.2.4: D-EXT (where PtG is added; new variable), D-OBJ, D-CONSTR (PtG uses only curtailable output), D-CONSTR (SNG storage balance and initial level), D-CONSTR (SNG use limited by storage), D-CONSTR (nodal balance with PtG), D-CONSTR (lists unchanged constraints), D-CONSTR (GfG capacity shared fossil/SNG), D-CONSTR (non-negativity)
  - 5.3: S-IMPL
- **Paragraph length:** average ≈ 50 words; shortest ≈ 15; longest ≈ 180
- **Figures and tables:** 1 figure (rolling-horizon timeline), introduced and explained; notation given as lists, not tables.
- **Chapter-type specifics (MODEL):** citations in the model chapter: 5 distinct (one for ramp rates, two for the CM formulation, two for remuneration practice). Constraint order: ED = objective → balance → generation bounds → storage → non-negativity; CM = objective → composition → nodal balance/angles → line flows → generation bounds → non-negativity; extension = objective → new technology bounds → storage → use limit → modified balance → unchanged list → modified bounds → non-negativity. Typical constraint explanation: 1–3 sentences (≈ 25–40 words) under a bold run-in label, placed before the equation. Assumptions: 2 of 3 state consequences; direction of bias given for cross-border only qualitatively. Notation convention is the reverse of ours (variables uppercase, parameters lowercase).
- **What makes this chapter strong:**
  - Opening timeline figure (daily ED → CM pairs over the year) gives the whole sequential structure before any symbol.
  - Each assumption is argued with a small quantitative check (e.g., per-minute ramp rates imply full range within an hour, so the constraint cannot bind) and a statement of what the simplification costs.
  - Base model + extension: the PtG subsection writes only new or changed constraints and explicitly lists which earlier ones stay, which keeps the formulation short.
  - The LP choice is justified by what it enables (market price read as the dual of the balance constraint), not by speed alone.
  - First-stage results passed to the second stage are visually marked (overline), so the stage coupling is readable in every equation.
- **Weaknesses:**
  - Minimum generation appears in eq. 5.3 while ch. 3 says must-run is excluded (resolved only in 6.1.2 by setting it to zero).
  - Implementation is one paragraph: no solve times, model size, or convergence information here or in results.
  - Citations inside the model chapter (contrary to our rule).
- **Signal phrases:** "We deliberately exclude binary variables" · "remain unchanged"

### 6 Spatial flexibility in redispatch: supporting low carbon energy systems with PtG [DATA+RES]
- **Purpose in one line:** Apply the model to Germany 2015: data and data assumptions, market results, calibration against statistics, redispatch and PtG results, efficiency sensitivity, chapter conclusion, and two extra sensitivity analyses.
- **Opening paragraph does:** A-PURPOSE+OTHER(chapter outline; footnote that results are part of a submitted article).
- **Closing paragraph does:** R-CAVEAT+R-IMPL — the counter-intuitive CO2 result does not make PtG uneconomic; it shows dependence on the remuneration assumption and price.
- **Subsections (in order):** 6.1 Data (6.1.1 Overview → grid, generation, load, merit order; 6.1.2 Data assumptions → must-run, availability, pumped storage, reliability margin, PtG costs); 6.2 Results (6.2.1 Economic dispatch; 6.2.2 Congestion management and PtG utilisation; 6.2.3 Sensitivity to PtG efficiencies); 6.3 Conclusion; 6.4 Additional in-depth analyses (6.4.1 More renewables; 6.4.2 Higher CO2 price).
- **Paragraph moves (in order, per subsection):**
  - opening: A-PURPOSE+OTHER(outline)
  - 6.1: A-SOURCE (open reference data set, version, documentation pointer)
  - 6.1.1: A-PARAM-TABLE (lines), A-CASE+A-PARAM-TABLE+A-FIG (generation fleet, capacities, spatial figure), A-CASE+A-FIG (load, nodes, load centres named), A-PROCESS (marginal-cost formula, CO2 price, merit-order figure)
  - 6.1.2: A-PURPOSE, A-PROCESS+A-LIMIT (must-run set to zero; two reasons; direction of bias: gas share underestimated, PtG not overestimated), A-PROCESS (monthly availability, calibration of nuclear), A-PROCESS+A-LIMIT (pumped storage split of capacity between stages; admitted as improvable), A-PROCESS (reliability margin value), A-PROCESS+A-LIMIT (PtG efficiencies from ch. 4; PtG pays market price → conservative; SNG carbon-neutral)
  - 6.2: R-AIMS (order of results)
  - 6.2.1: R-OBS+R-INTERP (four exemplary weeks: base load, seasonal wind/solar, storage peak shaving, prices), R-OBS+R-INTERP (price spread winter vs summer, storage arbitrage), V-BENCH+R-INTERP (generation mix vs statistics; gap explained by omitted exports), V-BENCH+R-INTERP+V-VERDICT (gas, oil, pumped storage deviations explained; model judged adequate)
  - 6.2.2: R-OBS+R-INTERP (annual redispatch volume by technology; winter share), R-OBS+R-INTERP+V-BENCH (spatial pattern follows planned HVDC corridors; volume and cost as % of documented values, each gap tied to a named simplification with direction), R-OBS+R-INTERP (PtG hours, 12.1 % less curtailment), R-OBS+R-LIT+R-IMPL (top PtG nodes coincide with two planned real projects and another study's optimal sites), R-OBS (cost saving minimal), R-OBS+R-INTERP (0.05 % saving; regression gives saving per MWh of SNG)
  - 6.2.3: R-SENS+OTHER(range motivated by the literature tables), R-SENS (runs defined in a table), R-SENS+R-INTERP (utilisation doubles at small efficiency gains; threshold below which PtG is never used)
  - 6.3: C-PROBLEM+C-DONE, C-FIND-OP (few bottlenecks, winter, north → south shift via gas grid), C-FIND-OP+X-IMPL+C-POINTER (attractive locations; not location-bound unlike storage; investment and other sectors as future work), C-LIMIT+C-POINTER+C-OVERALL (must-run, cross-border; sensitivity equivalent to price changes), C-POINTER+OTHER(bridge to ch. 7)
  - 6.4: R-AIMS+R-SENS (purpose and plan of extra runs; expectations announced)
  - 6.4.1: R-SENS (setup: +10 … +40 % RE), OTHER(expectations stated before results), R-SENS+R-OBS+R-INTERP (curtailment and PtG grow; price falls 2–2.5 % per step), R-OBS+R-INTERP (counteracting downward adjustments explained by merit-order position)
  - 6.4.2: R-SENS (setup and motivation), OTHER(expectation stated), R-OBS+OTHER(expectation refuted), R-INTERP (mechanism I: gas less hit by CO2 than coal), R-INTERP (mechanism II: PtG pays the higher market price, round-trip efficiency low), R-CAVEAT+R-IMPL
- **Paragraph length:** average ≈ 120 words; shortest ≈ 20; longest ≈ 330
- **Figures and tables:** 16 figures, 4 tables; mostly referenced in the paragraph that interprets them (float placement sometimes precedes the reference); figures with full observation → interpretation → implication: ≈ 3 of 16 (generation-mix comparison, PtG locations with Table 6.3, CO2 sensitivity pair); 2 exemplary-week figures only pointed to; merit-order figure not interpreted.
- **Chapter-type specifics (DATA):** source and version named; data treatment in run-in paragraphs; every data assumption states its effect direction except availability; no instance table. **(RES):** order = market stage → redispatch → PtG → cost → sensitivity → (conclusion) → extra sensitivities; no technical/solver subsection; calibration (V-BENCH) placed inside results.
- **What makes this chapter strong:**
  - Data assumptions come with a direction of bias in the same paragraph (e.g., ignoring must-run lowers the gas share; making PtG pay the market price is conservative), so later results can be read as lower or upper bounds.
  - Calibration against official statistics is quantified (shares of documented redispatch volume and cost) and each gap is attributed to one named simplification, with whether it pushes the number up or down.
  - Results are anchored in the real world: the model's best PtG nodes are matched against two planned industrial projects and against another study's optimal locations, which turns a model output into an implication for investors.
  - Sensitivity runs state an expectation first, then report results; when the CO2 run contradicts the expectation, the explanation is given as two numbered mechanisms, and the last paragraph says what the result does and does not mean.
  - A small cost effect is reported honestly (0.05 %) and reframed with a regression as saving per MWh, which gives the reader a usable unit result.
- **Weaknesses:**
  - Chapter mixes data, validation, results, conclusion and post-submission add-ons; its own conclusion overlaps with 8.3.
  - Some figures are shown but only pointed to; one cross-reference is wrong (refers to "Section 1" for the technology overview).
  - No runtime, model size or solver details anywhere.
- **Signal phrases:** "We point out that" · "To our surprise, our intuitions" · "Interestingly, our research results"

### 7 Exploring PtG implementations in regulated electricity markets [BACK+RES]
- **Purpose in one line:** Answer RQ2 by testing four possible legal classifications of PtG against German/EU and US rules on what system operators may own or operate.
- **Opening paragraph does:** OTHER(RQ2 restated as chapter aim, motivated by natural monopoly regulation).
- **Closing paragraph does:** C-ANSWER+C-LIMIT — US: storage status unclear, pending transmission-asset proposal leaves the answer open.
- **Subsections (in order):** (opening) aim, outline, four candidate classifications; 7.1 CM in Europe and the US → nodal vs zonal CM, comparison figure; 7.2 PtG under German and US regulation (7.2.1 Definitions → operators and four classifications; 7.2.2 PtG in Germany → test of each classification; 7.2.3 PtG in the US → storage resource order, unbundling, transmission-asset proposals); 7.3 Conclusion → one run-in paragraph per country.
- **Paragraph moves (in order, per subsection):** (legal tests coded OTHER(legal test) = provision cited → interpretation for PtG → verdict)
  - opening: OTHER(RQ2 as aim), OTHER(outline + four classifications listed)
  - 7.1: B-MECH (nodal pricing in the US), B-MECH+B-DEF (transmission rights, flowgates, equivalence to countertrading), B-MECH+OTHER(critique of redispatch as slow, cost hidden in network charges), B-FACT (EU rule on market-based redispatch; Germany still cost-based)
  - 7.2: B-SCOPE
  - 7.2.1: B-SCOPE, B-DEF (TSO, ownership unbundling), B-DEF (ISO/RTO), B-DEF+OTHER(terminology convention; perspective chosen), B-DEF (as storage), B-DEF (as gas producer), B-DEF (as consumer), B-DEF (as grid component / transmission asset)
  - 7.2.2: B-SCOPE+OTHER(method: map definitions to law, then check unbundling; pending EU directive included), OTHER(translation note)+L-GROUP (two prior legal studies), OTHER(legal test: end-consumer), OTHER(question split into two sub-questions), OTHER(legal test: storage, national law), OTHER(legal test: storage, EU directive; operators barred), OTHER(legal test: grid component), OTHER(legal test: gas producer), OTHER(legal test: vertical/horizontal unbundling), B-SUMMARY (Tables 7.1–7.3)
  - 7.2.3: B-SCOPE (US legal basis), OTHER(legal test: storage resource definition), OTHER(verdict: may qualify), OTHER(legal test: unbundling; bridge to transmission asset), B-CASE (two ISOs' storage-as-transmission initiatives), OTHER(proposed definition quoted at length), B-CASE (earlier regulator ruling with listed conditions), B-CASE+OTHER(stakeholder critique of the proposal)
  - 7.3: C-DONE+C-OVERALL, C-ANSWER (Germany), C-ANSWER (US, part 1), C-ANSWER+C-LIMIT (US, part 2)
- **Paragraph length:** average ≈ 120 words; shortest ≈ 25; longest ≈ 400
- **Figures and tables:** 1 figure (ancillary services Europe vs US), 3 tables (classification × source × wording × assessment for electricity SO and gas SO); introduced before shown: yes; tables summarise rather than being interpreted.
- **Numbers from other studies:** ≈ 1
- **Chapter-type specifics:** no thesis template code fits a legal analysis; it behaves like a qualitative results chapter with its own conclusion. No link back to the model's numbers.
- **What makes this chapter strong:**
  - The analysis frame is fixed up front: four candidate classifications defined in one subsection, then each is tested against the law of each jurisdiction, and every test ends with an explicit verdict sentence.
  - A complex legal question is split into two numbered sub-questions (is it a storage? may an operator run a storage?), and the same split is reused for the second country.
  - Summary tables separate the assessment for the electricity operator from the gas operator, so a reader can find the verdict per actor.
  - The chapter conclusion uses one run-in paragraph per jurisdiction, mirroring the comparison.
- **Weaknesses:**
  - Long verbatim quotations of legal text; nodal-pricing background repeats ch. 1.2.
  - The regulatory verdicts are never connected to the quantitative results of ch. 6 (e.g., which of the top nodes could be served under which classification).
- **Signal phrases:** "we break down the question" · "neither explicitly excluded or included"

### 8 Concluding remarks [DISC+FUT+CONCL]
- **Purpose in one line:** Reflect critically on assumptions, list further research, and conclude on both research components.
- **Opening paragraph does:** OTHER(chapter outline)+C-OVERALL — announces reflection, future work, conclusion; self-assessment of the work.
- **Closing paragraph does:** C-OVERALL+X-IMPL — policy message: regulation needs clear but flexible classification of sector-coupling technologies.
- **Subsections (in order):** 8.1 Critical reflection → five run-in assumption paragraphs; 8.2 Further research → six run-in extensions; 8.3 Conclusion → three paragraphs.
- **Paragraph moves (in order, per subsection):**
  - opening: OTHER(outline)+C-OVERALL
  - 8.1: X-METHOD (simplicity vs detail trade-off), X-ASSUMP (PtG representation: fixed efficiencies, PtG everywhere, no throughput cap → theoretical maximum; no minimum run time; gas-grid security ignored), X-ASSUMP (PtG pays market price = worst case for operator), X-ASSUMP+X-METHOD (24 h foresight: tractable and realistic, but misses multi-day synergies; longer foresight → more PtG value), X-GENERAL (objective tailored to Germany; rest of model reusable with other data), X-LIMIT+X-ASSUMP (2015 data; more renewables today → potential likely higher)
  - 8.2: OTHER(intro), F-EXT (investment), F-EXT (CO2 sources), F-EXT (hydrogen-only path), F-EXT (heat and transport coupling), F-EXT (nodal markets / arbitrage), F-EXT (regulatory design)
  - 8.3: C-DONE+C-FIND-OP+C-FIND-ECON (qualitative: less curtailment, lower congestion cost in SNG hours, higher RE share; few locations matter) + C-ANSWER (RQ1, implicit), C-ANSWER (RQ2: no clear classification; unbundling limits), C-OVERALL+X-IMPL
- **Paragraph length:** average ≈ 95 words; shortest ≈ 30; longest ≈ 240
- **Figures and tables:** 0
- **Numbers from other studies (discussion):** 0
- **Chapter-type specifics (DISC):** every assumption paragraph names its effect; direction of bias given in 4 of 5 (maximum potential, worst case, longer foresight raises value, newer data raises potential). **(FUT):** six extensions — what to add: 6/6; why the current assumption limits: 2/6; expected effect: 6/6; complexity cost: 0/6. **(CONCL):** RQs answered in order (model, then regulation) but not restated or labelled; no numbers in the conclusion (the 12 % headline appears only in the Summary).
- **What makes this chapter strong:**
  - Critical reflection is organised by assumption, each with a run-in heading and a sentence on which way it pushes the result (upper bound, worst case, underestimate) — reusable as a template for an assumption-revisited discussion.
  - The foresight paragraph gives both the reason for the choice (linear growth of computation, mirrors the day-ahead market) and a concrete example of what it misses, ending with a one-line take-away.
  - Conclusion is three paragraphs: one per research component plus one policy paragraph — short and in RQ order.
- **Weaknesses:**
  - The conclusion gives no numbers, so the main quantitative findings must be looked up in ch. 6.
  - Future-research items never estimate the modelling cost or complexity of the extension.
- **Signal phrases:** "The longer the modelling horizon" · "this is the "worst case""

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** The two numbered research components (I model, II regulation) from the introduction become the two gaps in 2.3 that end with "Chapter 6" and "Chapter 7" pointers, the two RQs in ch. 3, the two article-derived chapters, and the two answer paragraphs in 8.3. Problem-description subsections mirror the model subsections (ED → CM → PtG extension). Ch. 4 parameter tables are reused as the sensitivity range in ch. 6, and ch. 6's conclusion ends with a bridge paragraph into ch. 7. Recurring coined term: "spatial flexibility". Ch. 7 opens by naming the "second key research question".
- **How the RQs or objectives are answered in the conclusion:** in order (model paragraph, then regulatory paragraph), but without restating or labelling the RQs and without numbers; quantitative answers live in the chapter-6 conclusion and the Summary.
- **Anything a strong thesis does that the codes do not capture:**
  - Mixed-method design: a quantitative optimisation model and a qualitative legal analysis answer two complementary RQs (can it help? is it allowed?), which makes the contribution feel complete.
  - Chapters built from submitted articles keep their own conclusions; the thesis frame (intro, problem, model, concluding remarks) wraps them.
  - Model validation against real statistics is done inside results, and a small standard test case (IEEE-RTS24) with two illustrative case studies is moved to an appendix to show mechanisms without cluttering the main text.
  - Run-in bold headings are used everywhere (background concepts, lit themes, assumptions, constraints, results paragraphs, future-research items), which makes long subsections skimmable without deeper numbering.
  - Expectation-before-result structure in the extra sensitivity analyses, including openly reporting a refuted expectation.
