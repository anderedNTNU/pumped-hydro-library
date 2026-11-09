# bjornstad-2024 — Mari Hellum Bjørnstad and Nora Kyte, 2024
- File: `theses/texts/towards-a-sustainable-bolivian-power-system.txt`
- Type: paper-based (three case-study papers, ch. 3, 4 and 6, framed by a monograph-style ch. 1, 2, 5 and 7)
- Topic: open-source expansion planning of the Bolivian power system (PyPSA-Earth-BO, deterministic, single-year) with gas-subsidy scenarios, a Monte Carlo composite adequacy tool, and a port to EMPIRE (multi-horizon stochastic LP) for model comparison
- Relevance to a pumped-hydro / SDDP / multi-market thesis: low for structure (paper-based, system planning, no single plant); medium for paragraph style in results and the deterministic-vs-stochastic comparison in ch. 6
- Citation style: author-year
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 31,800 (ch. 1–7, incl. the three per-paper abstracts, captions, tables and equations; running prose ≈ 28,500 (?))
- Research questions stated explicitly: yes (8 RQs, in ch. 2 Problem description: 3 for study 1, 2 for study 2, 3 for study 3; none in ch. 1)

Front matter (not main text): preface says the thesis builds on the TIØ4500 project and that the project was proposed for publication (works as the reuse declaration); thesis-level abstract in four paragraphs (AB-CONTEXT · AB-PROBLEM+AB-METHOD as a list of objectives · AB-METHOD per study · AB-RES-ECON+AB-RES-OP+AB-IMPL), plus a Norwegian sammendrag; abbreviation list; an AI-use declaration after ch. 7.

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction | INTRO | 438 | 1,890 | 6 % | 18 (+ 5-item list) | 0 | 0 |
| 2 | Problem description | PROB (really: per-study motivation + RQs) | 633 | 1,580 | 5 % | 24 (+ 8 RQ items) | 0 | 0 |
| 3 | Case study 1: gas subsidies (paper, "preprint submitted") | ABS · INTRO · LIT · FRAME+MODEL · DATA · SCEN · VALID · RES · CONCL | 811 | 10,390 | 33 % | ≈ 112 | 21 | 5 |
| 4 | Case study 2: composite system adequacy (paper) | ABS · INTRO · BACK+LIT · MODEL+SOLVE · DATA · RES (incl. SENS) · CONCL | 1965 | 6,290 | 20 % | ≈ 60 | 3 | 11 |
| 5 | Reflections on PyPSA-Earth | DISC (X-METHOD) + FRAME (bridge to paper 3) | 2739 | 840 | 3 % | 8 | 0 | 0 |
| 6 | Case study 3: EMPIRE vs PyPSA-Earth-BO (paper, "to be submitted") | ABS · INTRO · LIT · MODEL+THEORY · DATA+SCEN · VALID · RES · CONCL | 2829 | 9,860 | 31 % | ≈ 108 | 15 | 3 |
| 7 | Concluding Remarks | CONCL + FUT | 3826 | 950 | 3 % | 10 | 0 | 0 |

Mapping of the article sections to chapter types (words ≈):
- **Ch. 3:** abstract (300) ABS · 3.1 Introduction (490) INTRO · 3.2.1–3.2.2 Literature review (1,170) LIT, with 3.2.2 really BACK · 3.2.3 Gap and contributions (390) LIT (L-GAP/L-CONTRIB) · 3.2.4 Organisation INTRO (I-OUTLINE) · 3.3 Methodology (1,250) FRAME + MODEL (tool description, objective, own added constraints) · 3.4 Data (1,950) DATA · 3.5 Transition pathways and projections (510) SCEN · 3.6.1 Validation (170) VALID · 3.6.2 Evaluation metrics (340) OTHER(metric definitions, belongs to RES set-up) · 3.6.3–3.6.8 (3,380) RES · 3.7 Conclusion (420) CONCL (+ FUT pointers).
- **Ch. 4:** abstract (180) ABS · 4.1 Introduction (350) INTRO · 4.2 Background and contribution (760) BACK + LIT + L-CONTRIB · 4.3 Methodology (1,170) MODEL + SOLVE (Monte Carlo algorithm, metrics) · 4.4 Data (1,320) DATA (case system, limitations, failure/repair rates) · 4.5 Results (2,170) RES, 4.5.4 = R-SENS · 4.6 Conclusion (310) CONCL.
- **Ch. 6:** abstract (220) ABS · 6.1 Introduction (470) INTRO · 6.2 Literature review + contribution (1,000) LIT · 6.3 Methodology (1,350) MODEL (EMPIRE objective, cost calculation, own constraint) + THEORY (multi-horizon vs multistage) · 6.4 Data (2,090) DATA + SCEN (PyPSA→EMPIRE transfer, scenario data, study pathways) · 6.5.1 Validation (1,880) VALID · 6.5.2–6.5.3 (2,340) RES · 6.6 Conclusion (520) CONCL + FUT.
- No stand-alone LIT, MODEL, RES or DISC chapter at thesis level; ch. 5 is the only discussion outside the papers.

## 2. Chapters

### 1 Introduction [INTRO]
- **Purpose in one line:** Moves from the global decarbonisation challenge to Bolivia, then to the role of OR and open-source models, and states the objective as three linked studies.
- **Opening paragraph does:** I-HOOK+I-CONTEXT — climate urgency and the power/heat sector's share of CO2 (sourced number), ending on the reliability tension the transition creates.
- **Closing paragraph does:** I-OUTLINE — one long paragraph naming each chapter and quoting each paper title, including the bridge role of ch. 5.
- **Subsections (in order):** 1.1 A reliable and sustainable power system → global drivers (electrification, finite fossil fuels, variability, resilience, Paris) · 1.2 The Bolivian power system → national targets, barriers, gas subsidies · 1.3 Optimisation approaches and open-source modelling → why OR, resolution and uncertainty, five benefits of openness · 1.4 Objective of the thesis → main objective, then one paragraph per study · 1.5 Structure of the thesis → outline.
- **Paragraph moves (in order, per subsection):**
  - 1.1: I-HOOK+I-CONTEXT, I-CONTEXT, I-CONTEXT, I-CONTEXT, I-CONTEXT, I-CONTEXT
  - 1.2: I-NATIONAL, I-NATIONAL, I-NATIONAL+I-PROBLEM
  - 1.3: I-LIT, I-LIT+I-CONCEPT, I-CONCEPT, I-CONCEPT (lead-in to a numbered list of five bold-labelled benefits, each 35–65 words with citations)
  - 1.4: I-AIM, I-AIM+I-CONTRIB, I-AIM, I-AIM+I-CONTRIB
  - 1.5: I-OUTLINE
- **Paragraph length:** average ≈ 85 words; shortest ≈ 45; longest ≈ 190 (the outline)
- **Figures and tables:** 0
- **Chapter-type specifics:** I-HOOK yes (sourced share, not dated event) · I-NATIONAL yes (NDC target, subsidy cost in USD for 2022) · I-LIT brief (one review, told across two paragraphs) · I-AIM yes · I-RQ no (deferred to ch. 2) · I-CONTRIB inside the aim paragraphs ("first implementation", "first-ever integration of a non-European system") · I-SCOPE no · I-FINDINGS no · I-LIMIT no · I-REUSE no (in preface) · I-OUTLINE yes.
- **What makes this chapter strong (own words):**
  - Funnel in three headed steps: global driver → country → method family; each subsection is a self-contained layer, so the reader always knows which scale is being discussed.
  - The objective section gives one paragraph per study, and each paragraph says what the study builds on from the previous one; the dependency chain between the papers is stated before any paper starts.
  - Claims of novelty are attached to the objective ("first implementation in X", "first integration of Y"), not saved for a separate contribution list.
  - The outline paragraph names the function of the bridging chapter (ch. 5), not only its title.
- **Weaknesses:** 1.1 is six paragraphs of generic global context that do not yet mention the thesis; the five-item list of open-source benefits reads like a brochure and is not tied back to the problem; no scope or findings preview.
- **Signal phrases (≤ 3, ≤ 6 words each):** "The first study extends"; "builds on the validated system"

### 2 Problem description [PROB]
- **Purpose in one line:** Re-motivates the problem and gives each of the three studies its own subsection ending in a numbered RQ list.
- **Opening paragraph does:** P-PURPOSE — two sentences saying the chapter sets the scope and presents the RQs.
- **Closing paragraph does:** OTHER(RQ list) — three RQs for study 3, the last one asking what the comparison contributes to open-source modelling.
- **Subsections (in order):** unnumbered intro → transition, gas dependence, need for better representation · 2.1 Fuel subsidies → study 1 motivation, approach, scenarios, 3 RQs · 2.2 Composite system adequacy → study 2 motivation, Monte Carlo, critical components, 2 RQs · 2.3 Stochastic investment model → study 3 motivation, EMPIRE, comparison, transferability, 3 RQs.
- **Paragraph moves (in order, per subsection):**
  - intro: P-PURPOSE, P-SYSTEM, P-SYSTEM+P-UNCERT(?), OTHER(role of open-source models), P-PURPOSE, OTHER(roadmap: three studies)
  - 2.1: P-SYSTEM, OTHER(method preview: which model), P-PURPOSE, OTHER(scenario design preview: gradual vs sudden phase-out), P-PURPOSE → 3 RQs
  - 2.2: P-SYSTEM, OTHER(method preview + definition of composite adequacy), P-UNCERT (outages as stochastic, Monte Carlo), P-OUTPUT (critical components for planners), OTHER(contribution to open-source field) → 2 RQs
  - 2.3: OTHER(why compare models), OTHER(EMPIRE introduced), OTHER(data reuse across models), P-PURPOSE, P-OUTPUT, OTHER(transferability) → 3 RQs
- **Paragraph length:** average ≈ 55 words; shortest ≈ 28; longest ≈ 85
- **Figures and tables:** 0
- **Chapter-type specifics:** symbols: none · numbers: none · citations: 1 · length ≈ 4 pages. P-ACTOR, P-HORIZON, P-MARKETS, P-DECISIONS, P-CONSTRAINTS, P-OBJECTIVE are absent: this is a research-question chapter, not a problem description in the Bore & Brensholm sense. Uses future tense ("the study will") throughout.
- **What makes this chapter strong (own words):**
  - Every study subsection follows the same four-beat pattern: why it matters → which tool → what will be analysed → numbered RQs. Parallel structure makes the three studies easy to compare.
  - RQs are long and double-barrelled on purpose ("how can X be built, and what does it show"), so each RQ covers both a method deliverable and an insight deliverable.
  - The chapter has no numbers and no symbols; data and model detail are held back for the papers.
- **Weaknesses:** heavy repetition of ch. 1 (subsidies, open-source value); several paragraphs restate the same "valuable insights" claim; the RQs are never picked up by number later.
- **Signal phrases (≤ 3, ≤ 6 words each):** "through the following research questions"

### 3 Case study 1: Gas subsidies and the power-system transition by 2040 [paper: ABS · INTRO · LIT · FRAME+MODEL · DATA · SCEN · VALID · RES · CONCL]
- **Purpose in one line:** Improves the Bolivian PyPSA-Earth model (101 nodes, corrected data, new constraints) and compares six subsidy/emission scenarios to 2040, plus the effect of spatial resolution.
- **Opening paragraph does:** (after the abstract) I-CONTEXT — developing countries must grow and decarbonise at once.
- **Closing paragraph does:** C-POINTER — sustainability is more than CO2; future work should add land use, resource depletion and life-cycle impacts.
- **Subsections (in order):** abstract → whole paper in one block with headline numbers · 3.1 Introduction → context, Bolivia, model requirements, aim + scope · 3.2.1 Energy system modelling → four challenges, resolution studies, Bolivian models rated in Table 3.1 · 3.2.2 Gas situation → reserves and subsidy cost · 3.2.3 Gap and contributions → gap from previous studies' own recommendations, 3 bullets · 3.2.4 Organisation · 3.3.1 Modelling tool → PyPSA-Earth workflow, objective, DC power-flow assumptions · 3.3.2 Technical add-ons → notation table + five own constraints · 3.3.3 Workflow → iterative yearly algorithm (one sentence + figure) · 3.4.1–3.4.2 Data → default data and six run-in-headed corrections · 3.5 Pathways → scenario tree and projections · 3.6.1 Validation · 3.6.2 Evaluation metrics · 3.6.3 Costs · 3.6.4 Emissions · 3.6.5 Installed capacities · 3.6.6 Generation mix · 3.6.7 Operation · 3.6.8 Spatial resolution · 3.7 Conclusion.
- **Paragraph moves (in order, per subsection):**
  - Abstract: AB-CONTEXT+AB-METHOD+AB-CASE+AB-RES-ECON+AB-RES-OP+AB-IMPL (one block)
  - 3.1: I-CONTEXT, I-NATIONAL+I-PROBLEM, I-CONCEPT (what a policy model must combine; why open source), I-AIM+I-SCOPE (horizon to 2040; main grid only, with its demand share)
  - 3.2.1: L-STUDY+L-TAXONOMY (four challenges), L-STUDY (second review confirms the same four), L-RELEVANCE (transparency), L-PAIR (two spatial-resolution studies with one number), L-TABLE+L-SYNTH (Table 3.1 rates Bolivian models on five dimensions; no model is high on all), L-GROUP+L-CRITIQUE (model A), L-GROUP+L-CRITIQUE (model B), L-GROUP+L-CRITIQUE (model C), L-GROUP+L-CRITIQUE+L-OWN (the model they extend: 4 nodes, spatial potential unused)
  - 3.2.2: B-FACT (gas reserves and export role), B-FACT (subsidies and their cost)
  - 3.2.3: L-GAP+L-OWN (gap built from what earlier studies listed as needed improvements), L-CONTRIB (3 bullets)
  - 3.2.4: I-OUTLINE
  - 3.3.1: D-INTRO, S-IMPL (version, where the full formulation is documented, why the description is brief), M-WORKFLOW (Figure 3.1 steps), D-INTRO (network as nodes and arcs, outputs) → D-OBJ (eq. 3.1), D-NOTATION (cost terms explained in prose), D-ASSUMP+D-LINEAR (four numbered linearisation assumptions), D-CONSTR (eq. 3.2, lossless), D-CONSTR (other constraints by reference)
  - 3.3.2: D-INTRO (what the add-ons are for) + Table 3.2, D-CONSTR (biomass yearly CF, eq. 3.3), D-CONSTR (yearly new-capacity cap, eq. 3.4), D-CONSTR (geothermal yearly cap, eq. 3.5), D-CONSTR (total potential caps, eq. 3.6), D-CONSTR (storage caps, eq. 3.7–3.9)
  - 3.3.3: M-WORKFLOW (Figure 3.2, one sentence)
  - 3.4.1: A-SOURCE+A-LIMIT (default global datasets; output only as good as input), A-PROCESS (custom files possible)
  - 3.4.2: A-PURPOSE, [network] A-FIG (isolated parts, Fig. 3.3), A-SOURCE+A-PROCESS, A-PROCESS (dead-end removal disabled: more buses), A-PROCESS+A-PARAM-TABLE (voltage levels, Table 3.3), A-PROCESS (line capacities from TSO report), A-FIG (Fig. 3.4 a→d walk-through), [plants] A-SOURCE+A-PROCESS (conservative capacity value chosen), A-PROCESS (expansion "shells" for geothermal and hydro), A-PROCESS (decommissioning), [load] A-PROCESS (manual load re-distribution), A-FIG (Fig. 3.5: how the error was spotted, what changed, why it matters), [costs] A-SOURCE + Table 3.4, A-PROCESS (biomass cost raised, with reason), [inflow] A-PROCESS, A-PROCESS+A-LIMIT (averaging at shared nodes), A-PROCESS (reservoir hours corrected), [biomass CF] A-PROCESS, [caps] A-PROCESS (yearly caps, with reasons), A-SOURCE (potential caps; lower bound chosen as conservative)
  - 3.5: A-SCEN (two scenario dimensions, six scenarios, Fig. 3.6), A-SCEN (three subsidy paths narrated), A-SCEN (emission-capped twins), A-SCEN+A-FIG (default vs TSO demand forecast, Fig. 3.7)
  - 3.6.1: V-BENCH+V-CHALLENGE+V-VERDICT (2022 generation mix vs TSO statistics; three named reasons for the gaps)
  - 3.6.2: OTHER(metric definitions with equations: NPV, subsidy NPV, total, emissions, capacity, capacity factor, lost load; ≈ 9 short paragraphs, each 1–2 sentences + equation + one line on what the metric reveals)
  - 3.6.3: R-OBS (Figs 3.9–3.10 introduced; headline pattern), R-OBS (NPV per scenario, numbers), R-INTERP+R-IMPL (subsidies included → ranking flips), R-CAVEAT (subsidies outside the optimisation)
  - 3.6.4: R-OBS+R-INTERP+R-IMPL (emission trends; subsidy cuts alone not enough), R-INTERP+R-CAVEAT (emission path acts as foresight the yearly model lacks), R-SUMMARY
  - 3.6.5: R-OBS (how to read Figs 3.12–3.13), R-OBS+R-INTERP, R-OBS+R-INTERP, OTHER(signpost), R-OBS+R-INTERP, R-OBS+R-INTERP, R-OBS+R-INTERP
  - 3.6.6: R-KEYREL (capacity → generation via marginal cost and cap), R-OBS+R-INTERP, R-OBS, R-OBS+R-INTERP, R-OBS, R-KEYREL (how to read a capacity factor), R-OBS+R-INTERP, R-INTERP (late emission rise explained by exhausted potentials), R-OBS (Fig. 3.16), R-OBS+R-INTERP, R-SUMMARY+R-IMPL
  - 3.6.7: R-OBS+R-INTERP (peak hours, no lost load)
  - 3.6.8: R-OBS, R-OBS+R-INTERP (solar CF range per resolution), R-OBS+R-IMPL (wind CF per resolution), OTHER(signpost: which scenario pair is compared), R-OBS (NPV nearly equal; Table 3.5), R-OBS+R-INTERP (4-node over-invests in solar, no wind), R-OBS+R-INTERP (transmission investment gap), R-INTERP (restrictive lines favour local generation), R-SUMMARY
  - 3.7: C-PROBLEM+C-DONE, C-FIND-ECON (€ saving vs BASE; flexibility for policymakers), C-DONE+C-FIND-INV (resolution: % differences in wind potential and line investment), C-LIMIT+C-POINTER (constant fuel prices → sensitivity), C-POINTER
- **Paragraph length:** average ≈ 85 words; shortest ≈ 15 (metric definitions); longest ≈ 230 (cost results)
- **Figures and tables:** 21 figures, 5 tables; introduced before shown? mostly yes ("Figure X displays …" opens the paragraph), a few floats land before their first mention; OBS→INTERP→IMPL complete for ≈ 5 of the 13 results figures (3.10, 3.11, 3.16, 3.18, 3.19); the rest stop at OBS→INTERP.
- **Numbers from other studies (LIT/BACK parts):** 3 (one % from a resolution study, one subsidy cost in USD, one demand share in the intro)
- **Own work mentioned (LIT part):** ≈ 4 sentences, all in 3.2.3, plus a "current study" row in Table 3.1
- **Chapter-type specifics:**
  - LIT 3.2.1: studies cited 15 · told in depth 4 · paragraphs opening with an author name 3 · critique phrased as a resolution rating ("only medium resolution in …") taken from the taxonomy table · ends on the model being extended, with its unused spatial potential (natural hand-off to the gap).
  - LIT 3.2.2: 5 sources, background facts only.
  - MODEL: citations ≈ 5 (tool documentation and earlier Bolivian studies) · constraint order: biomass CF → yearly capacity cap → geothermal cap → total potential → storage caps · each constraint has a bold run-in label, a 1–2 sentence reason, then the equation · D-ASSUMP for DC power flow listed without direction of bias, except "no losses" · one physical number (100 MW) appears in the model section.
  - DATA: six run-in headings (network, plants, load, costs, inflow, biomass CF, caps); each follows problem in default data → better source → fix → justification. A-LIMIT stated twice, with what is lost.
  - SCEN: instances defined by two dimensions with a figure; each scenario's story is narrated (what forces the country to act), not only tabulated.
  - VALID: one paragraph, one benchmark against official statistics, causes of mismatch named.
  - RES order: validation → metrics → economic (costs) → environmental (emissions) → investment (capacities) → operational (generation, peak hour) → method effect (spatial resolution).
  - CONCL: no RQ numbering; findings given with numbers; limitations converted directly into future work.
- **What makes this chapter strong (own words):**
  - The literature taxonomy is turned into a table (models × five resolution dimensions, with the current study as the last row), and the per-model paragraphs then only need one sentence of critique each because the table carries the comparison.
  - The gap is built from what earlier studies on the same case said should be improved, then extended with one improvement the authors found themselves; this makes the gap look discovered, not asserted.
  - Data corrections are written as short case files under run-in headings: what was wrong, how it was noticed, which source fixed it, and why the chosen value is conservative.
  - A figure series (network a→d) is walked through in one paragraph, one sentence per panel, so the reader sees the data-cleaning progression.
  - Results paragraphs explain mechanisms through the cost logic of the model (e.g. why a cheaper-capex but slightly dearer-opex unit fills capacity gaps) rather than only describing bars.
- **Weaknesses:** the transmission-investment number is inconsistent between results (6 %), conclusion (< 6 %) and abstract (15 times); several results paragraphs use vague evaluative words ("fascinating dynamics", "innovative approach"); evaluation metrics are defined inside Results instead of in the method section.
- **Signal phrases (≤ 3, ≤ 6 words each):** "it is evident that no model"; "Building on these insights"; "A closer look reveals"

### 4 Case study 2: Composite system adequacy in PyPSA-Earth-BO [paper: ABS · INTRO · BACK+LIT · MODEL+SOLVE · DATA · RES · CONCL]
- **Purpose in one line:** Adds Monte Carlo component failures to the 2040 network from paper 1, computes EENS/LOLP/VOLL, and identifies critical lines and generators, with and without the emission cap.
- **Opening paragraph does:** (after abstract) I-HOOK — a projected electricity share of final energy use, then the dependence it creates.
- **Closing paragraph does:** C-POINTER+X-IMPL — future refinements (multiple-unit failures, more scenarios) and a policy message on dispatchable renewables and grid investment.
- **Subsections (in order):** abstract (3 paras: context, method/case, result + implication) · 4.1 Introduction → reliability under transition · 4.2 Background and contribution → definitions, outage types, inertia, review gap · 4.2.1 Contribution · 4.2.2 Organisation · 4.3 Methodology → system under study · 4.3.1 failure model · 4.3.2 Monte Carlo + pseudocode · 4.3.3 implementation as constraints · 4.3.4 metrics · 4.4 Data → load centres, components and their modelling limits, failure/repair rates · 4.5 Results → system level, buses, components, relaxed emission cap · 4.6 Conclusion.
- **Paragraph moves (in order, per subsection):**
  - 4.1: I-HOOK, I-CONTEXT, I-CONCEPT (what composite adequacy analysis does), I-CONTEXT (reliability–cost trade-off), OTHER(rhetorical closing that restates the previous paragraph)
  - 4.2: B-DEF (adequacy vs security vs resilience; three hierarchical levels), B-MECH (load shedding vs blackout; trade-off), B-FACT (loss of inertia, converters; TSO source), L-STUDY+L-GAP (review: most studies use test systems, with count)
  - 4.2.1: L-OWN (builds on the paper-1 scenario), I-AIM+L-CONTRIB (2 bullets)
  - 4.2.2: I-OUTLINE
  - 4.3: D-INTRO (which network and year), D-ASSUMP (independent failures, no correlation; no bias direction), T-FORMAL (exponential density, eq. 4.1), S-IMPL (pseudo-random generator), S-WHY (Monte Carlo for large systems), S-ALGO (state-transition sampling → 0/1 matrix) + S-PSEUDO (Algorithm 1), D-CONSTR (dispatch forced to zero when failed, eq. 4.2–4.3, Table 4.1), S-IMPL (no investment, cap on, 1000 runs), D-ASSUMP+S-IMPL (second run without cap, 100 runs for computational reasons), T-FORMAL ×5 (EENS, its MC estimate, LOLP, its estimate, VOLL; each 1–2 sentences before the equation)
  - 4.4: A-PURPOSE, A-CASE+A-FIG (Fig. 4.1 + Table 4.2), A-FIG (why these load centres matter for the results), A-CASE (2040 network origin and CO2 limit), A-LIMIT (aggregated solar/wind units; expansion added to existing units), A-CASE (parallel lines kept), A-LIMIT (line expansion on existing lines only), A-LIMIT (network optimised without reliability → likely performs worse than a reliability-aware design), A-FIG (Fig. 4.2 key components), A-SOURCE+A-LIMIT (rates from literature, not Bolivian) + Tables 4.3–4.4, A-PROCESS (one rate for all sizes), A-PROCESS (wind approximated by solar; plant-level rates)
  - 4.5.1: R-OBS+R-INTERP (indices, share of demand, VOLL set against operating cost)
  - 4.5.2: R-OBS (how Table 4.6 was built), R-OBS+R-INTERP (region shares explained by isolation, technology mix, line capacity)
  - 4.5.3: OTHER(table-reading guide: what each column means) + R-CAVEAT, R-OBS+R-INTERP (critical lines located on the map), R-OBS, R-OBS+R-INTERP (critical generators), R-INTERP (why solar is absent), R-CAVEAT (combined failures out of scope), R-SUMMARY+R-CAVEAT (two numbered conclusions: modelling exaggerates lost load; lines and large dispatchable units are critical)
  - 4.5.4: R-SENS (why relax the cap), R-SENS+R-INTERP (EENS falls to 28 %, LOLP to 5.6 %), R-OBS+R-INTERP (new bus appears; isolation explains it), R-OBS (two buses carry about half), R-OBS+R-INTERP (generators negligible), R-SUMMARY+R-IMPL
  - 4.6: C-DONE+OTHER(tool is easy to adapt), C-FIND-OP (72 % reduction; lines dominate), C-POINTER+X-IMPL
- **Paragraph length:** average ≈ 75 words; shortest ≈ 25; longest ≈ 170
- **Figures and tables:** 3 figures, 11 tables; introduced before shown? yes; tables are always interpreted in the next paragraph (location → reason → consequence), but Fig. 4.3 (lost-load distribution) is only mentioned, never interpreted; OBS→INTERP→IMPL complete for ≈ 3 of 7 results tables.
- **Numbers from other studies (BACK/LIT parts):** 3 (one projected share, review count out of a total)
- **Own work mentioned (BACK/LIT parts):** ≈ 3 sentences (all in 4.2.1)
- **Chapter-type specifics:**
  - LIT: studies cited ≈ 6 · told in depth 2 · paragraphs opening with an author name 1 · critique by counting (share of reviewed studies on test systems) · ends with the gap (no realistic systems).
  - MODEL/SOLVE: citations ≈ 8 · order: assumptions → failure distribution → sampling algorithm → constraints → metrics · Algorithm 1 as pseudocode · metric equations each with a one-sentence definition first.
  - DATA: A-LIMIT given as consequences for the results, with direction (lost load exaggerated; network weaker than a reliability-aware one).
  - RES order: system level → most affected buses → critical components → sensitivity (cap relaxed).
- **What makes this chapter strong (own words):**
  - Limitations of how components are represented are stated in the data section with their expected effect on the results, and the results section then refers back to them when interpreting; the caveat is planted before it is needed.
  - Every critical-component table is interpreted geographically: the paragraph places each bus or line in a named region and explains its role through isolation, technology mix or line capacity.
  - The sensitivity run is motivated by realism (a country would not keep a CO2 cap during an outage), so the second simulation answers a question the reader already has.
  - A section summary uses two numbered conclusions, one a modelling caveat and one a substantive finding, and explicitly says the second must be read in light of the first.
- **Weaknesses:** the introduction's last two paragraphs repeat each other; Fig. 4.3 is shown but never discussed; failure rates are admitted to be not Bolivian, which weakens the critical-component ranking more than the text acknowledges.
- **Signal phrases (≤ 3, ≤ 6 words each):** "points to two important conclusions"; "must be considered in light of"

### 5 Reflections on PyPSA-Earth [DISC + FRAME (bridge)]
- **Purpose in one line:** Takes stock of what the first two papers did, weighs the tool's strengths and weaknesses, and motivates the switch to a stochastic multi-horizon model for paper 3.
- **Opening paragraph does:** OTHER(recap) — what has been done so far in the thesis.
- **Closing paragraph does:** M-BRIDGE — the same inputs in both models allow attributing output differences to model features.
- **Subsections (in order):** 5.1 Potential and challenges → recap, strengths, weaknesses, ongoing development · 5.2 Introduction to case study 3 → why EMPIRE, why fewer nodes, what comes next.
- **Paragraph moves (in order, per subsection):**
  - 5.1: OTHER(recap), X-METHOD (strengths), X-METHOD+X-LIMIT (usability, data gaps, deterministic, single-year), OTHER(ongoing development by the tool community)
  - 5.2: M-RATIONALE (EMPIRE addresses the two named limits), M-RATIONALE (node reduction as a detail–computation trade-off), M-BRIDGE, M-BRIDGE
- **Paragraph length:** average ≈ 100 words; shortest ≈ 60; longest ≈ 170
- **Figures and tables:** 0 (refers to an appendix map)
- **What makes this chapter strong (own words):**
  - A short interlude chapter turns the limitations of the first tool into the motivation of the next paper: the two weaknesses named last in 5.1 (deterministic, single year) are exactly the two features introduced first in 5.2.
  - The resolution reduction for the next study is justified up front as a trade-off, so paper 3 does not have to defend it.
- **Weaknesses:** the weaknesses paragraph mixes user-interface complaints with modelling limits; little evidence beyond the authors' experience.
- **Signal phrases (≤ 3, ≤ 6 words each):** "Being a tool under active development"

### 6 Case study 3: EMPIRE for Bolivia, compared with PyPSA-Earth-BO [paper: ABS · INTRO · LIT · MODEL+THEORY · DATA+SCEN · VALID · RES · CONCL]
- **Purpose in one line:** Ports the Bolivian data to EMPIRE, validates it against PyPSA-Earth-BO by removing differences one at a time, then compares deterministic single-year and stochastic multi-horizon investment paths, and extends the horizon to 2060.
- **Opening paragraph does:** I-HOOK — sourced growth of VRES share from 2020 to 2050.
- **Closing paragraph does:** C-LIMIT+C-POINTER — the 2060 run is limited by investment caps on dispatchable sources, which future work should revisit.
- **Subsections (in order):** abstract (4 paras) · 6.1 Introduction → VRES challenge, stochastic modelling, trade-off, aim · 6.2 Literature review → uncertainty in energy models, approaches, Bolivian tools, EMPIRE · 6.2.1 Contribution · 6.2.2 Organisation · 6.3.1 EMPIRE → formulation, cost calculation, own changes · 6.3.2 PyPSA-Earth-BO → what load flow adds · 6.4 Data → EMPIRE inputs, transfer workbook by workbook, scenario data, study pathways · 6.5.1 Validation · 6.5.2 Deterministic vs stochastic · 6.5.3 Towards 2060 · 6.6 Conclusion.
- **Paragraph moves (in order, per subsection):**
  - Abstract: AB-CONTEXT+AB-METHOD+AB-CASE, AB-RES-OP, AB-RES-OP (convergence of portfolios), AB-IMPL
  - 6.1: I-HOOK, I-CONTEXT, I-CONCEPT (what stochastic models add), I-CONCEPT (stochastic vs deterministic trade-off), I-AIM+I-LIT+I-CONTRIB
  - 6.2: L-STUDY+L-PAIR (review on VRES models; two more reviews agree), L-TAXONOMY+L-STUDY (four approaches to uncertainty; aleatory uncertainty), L-STUDY (deterministic models underestimate cost and emissions), L-NOTCOVERED+L-STUDY+L-CRITIQUE (no open-source uncertainty model for Bolivia; the government's proprietary SDDP-based tool lacks openness), L-GROUP+L-GAP (all open-source Bolivian models deterministic), L-STUDY+L-GAP (EMPIRE, so far only European)
  - 6.2.1: L-OWN+L-CONTRIB (2 bullets), OTHER(framing: comparison judged by modelling assumptions)
  - 6.2.2: I-OUTLINE
  - 6.3.1: D-INTRO, T-CONCEPT+T-COMPARE (strategic foresight vs operational uncertainty; multi-horizon vs multistage, Fig. 6.1), D-OBJ (eq. 6.1, term by term), D-CONSTR (constraint list in prose; transport-model flow), S-IMPL (version), [cost calculations] D-OBJ (annualisation, eq. 6.2–6.3), D-OBJ (opex, eq. 6.4), D-OBJ (NPV), [changes] D-EXT (start-year parameter, scenario generation, new annual CF constraint eq. 6.5)
  - 6.3.2: D-INTRO, T-COMPARE (what power-flow constraints add; without them transmission capacity is overestimated), D-OBJ (same objective, by reference)
  - 6.4: A-PURPOSE, A-SOURCE, A-SOURCE (network vs scenario input files), A-SOURCE, A-PROCESS (reuse of refined data), A-PROCESS (101 → 30 nodes; automated transfer), A-PROCESS (yearly → five-year periods), [network] A-PROCESS ×9 (one paragraph per input workbook: sets, generators, decommissioning/ramping, caps, nodes with VoLL, general/CO2 cap, storage, transmission), [scenario data] A-SCEN+A-LIMIT (one sample year for load and inflow, three for weather), A-PROCESS (aggregation), A-PROCESS, A-LIMIT (uniform inflow per node), A-PROCESS, A-PROCESS+A-LIMIT ("both rather oversimplified")
  - 6.4.3: A-INSTANCES (validation scenarios and the comparison scenario, each with its goal), A-INSTANCES (extended horizon and its motivation)
  - 6.5.1: V-PURPOSE, V-SETUP (hydro expansion off), V-SETUP (PyPSA run per 5-year period; yearly caps removed), V-SETUP (one weather year, max hours, one scenario), V-SETUP (remaining known sources of difference listed), V-BENCH (BASE generation mix), V-BENCH (BASE costs, Table 6.1: capex vs opex gap traced to hydro), V-BENCH (total % gap), V-SETUP (BASE NZE with investment cap), V-BENCH (capex gap split into solar and lines, € each), V-BENCH (opex gap), V-BENCH (solar dispatch gap; weather ruled out via capacity factors), V-BENCH (hydro), V-BENCH (load flow), V-BENCH (wind), V-BENCH (transmission), V-BENCH (geothermal gap explained by location, Fig. 6.7), V-BENCH (biomass, OCGT), V-VERDICT
  - 6.5.2: R-AIMS (from alignment to distinctive features), R-CAVEAT (different cost accounting), R-OBS (BASE unchanged), R-AIMS (why focus on BASE NZE and GC; what each shows), R-OBS (investment paths diverge, end portfolios similar), R-OBS+R-INTERP (deterministic model reacts year by year), R-INTERP (stochastic model invests early), R-INTERP+R-STOCH (10 weather scenarios → cautious), R-OBS (geothermal biggest gap), R-INTERP, R-OBS+R-INTERP (lines vs generation location, Fig. 6.10), R-CAVEAT (one fuel price per period), R-INTERP (price thresholds), R-OBS (period 1), R-INTERP (perceived capex burden; solar "certain" in the deterministic model), R-OBS+R-INTERP (period 2), R-OBS+R-INTERP (period 3), R-OBS+R-INTERP (spatial distribution, Fig. 6.13), R-SUMMARY, R-SUMMARY, R-IMPL (which model suits which question)
  - 6.5.3: R-SENS (why a longer horizon), OTHER(run set-up), R-OBS (solar + batteries dominate), R-INTERP+R-CAVEAT (expected, since other potentials are capped in the model), OTHER(focus shift to early-period strategy), R-OBS+R-INTERP (less geothermal, more solar early)
  - 6.6: C-PROBLEM+C-DONE, OTHER(value of open source), C-FIND-OP (deterministic model's strength), C-FIND-INV (stochastic model's strength; longer horizon changes first-period decisions), C-FIND-OP (largest gaps in high-VRES systems; deterministic overestimates VRES), C-FIND-INV (portfolios converge), C-POINTER (power flow in EMPIRE; hybrid models), C-LIMIT+C-POINTER
- **Paragraph length:** average ≈ 85 words; shortest ≈ 25; longest ≈ 200
- **Figures and tables:** 15 figures, 3 tables; introduced before shown? yes, except Fig. 6.2 (pathway overview), which is never referenced in the text; OBS→INTERP→IMPL complete for ≈ 4 of 13 results/validation figures (6.8, 6.9, 6.10, 6.12); most validation figures stop at OBS→INTERP by design (the implication is the verdict).
- **Numbers from other studies (INTRO/LIT):** 2 (both VRES shares in the opening; the literature review itself reports no numbers)
- **Own work mentioned (LIT part):** ≈ 3 sentences (the gap sentences and 6.2.1)
- **Chapter-type specifics:**
  - LIT: studies cited 9 · told in depth 6 · paragraphs opening with an author name 0 (each opens with the theme, then the author) · critique phrased as a missing property (no uncertainty, not open, not used outside Europe) · ends with the tool they adopt and its unused geographic scope (gap = their contribution).
  - MODEL: citations ≈ 8 (all to the tool papers and their own paper 1) · objective explained term by term in prose before the equation · most constraints described in one prose list rather than written out · own constraint written in full.
  - DATA: organised by the input files of the tool, one paragraph per file; data limits stated with their consequence for each model.
  - VALID: deliberate alignment of the two models (switching off features), then residual differences explained one by one with € and TWh, until each gap is attributed to hydro modelling or load flow.
  - RES order: validation → like-for-like comparison per scenario (BASE → BASE NZE → GC) → horizon extension.
  - R-STOCH: present qualitatively (number of weather scenarios drives caution); no out-of-sample or VSS figure.
- **What makes this chapter strong (own words):**
  - Validation by controlled alignment: features that differ between the models are switched off one at a time and listed, so every remaining gap has a short list of candidate causes; each gap is then split into named parts with a figure for each (e.g. capex gap = solar part + lines part).
  - Ruling out a cause with a second figure: a dispatch gap is first suspected to come from weather, then a capacity-factor plot shows the weather is the same, so the cause must be elsewhere. This "suspect → check → exclude" sentence pattern is reusable for any model comparison.
  - The results section opens with an explicit change of goal ("so far we aligned the models; now we let them differ") and a cost-accounting caveat, which tells the reader how to read every later difference.
  - Period-by-period narration of investment decisions (period 1, 2, 3) links each step to a price threshold or to uncertainty, giving a causal story instead of a bar-by-bar description.
  - The comparison ends with a "which model for which question" judgement rather than declaring a winner.
- **Weaknesses:** Fig. 6.2 is never referenced; the data section is a long walk through input files that reads like documentation; the "stochastic" benefit is asserted from behaviour, without an out-of-sample test.
- **Signal phrases (≤ 3, ≤ 6 words each):** "Moving forward, the distinctive features"; "Nonetheless, the model lacks"

### 7 Concluding Remarks [CONCL + FUT]
- **Purpose in one line:** Restates the objectives, summarises each study in order, draws thesis-level implications and lists future work.
- **Opening paragraph does:** C-PROBLEM — the objectives repeated as four goals.
- **Closing paragraph does:** F-EXT — extending EMPIRE to other non-European countries.
- **Subsections (in order):** none.
- **Paragraph moves (in order):** C-PROBLEM, C-DONE+C-FIND-ECON (study 1, with the € saving; cost and emission goals do not conflict), C-DONE+C-FIND-OP+C-POINTER (study 2), C-DONE+C-FIND-INV (study 3), C-OVERALL, C-OVERALL+X-IMPL, F-EXT, F-EXT, F-EXT, F-EXT
- **Paragraph length:** average ≈ 95 words; shortest ≈ 50; longest ≈ 170
- **Figures and tables:** 0; citations 0
- **Chapter-type specifics:**
  - CONCL: RQs are not answered one by one or by number; the answer is one paragraph per study, in study order, with one number in total (the € saving). Limitations appear only inside future work.
  - FUT (4 paragraphs, ≈ 7 extensions): fuel-price sensitivity (what + why: yes; effect: "more nuanced"; cost: no) · less restrictive caps on dispatchable sources (what + why: yes; effect/cost: no) · reliability tool: better component data, correlated failures, local rates, reliability inside the optimisation (what: yes; why: implicit; effect: stronger predictions; cost: no) · hybrid deterministic–stochastic models (what: yes; others: no) · longer-term studies (what only) · other countries (what + why). No extension states its complexity cost.
- **What makes this chapter strong (own words):**
  - One paragraph per paper, each opening with how it builds on the previous one, keeps the three studies reading as one project.
  - A separate implications paragraph lifts the findings from the case (Bolivia) to the wider modelling community.
- **Weaknesses:** the eight RQs from ch. 2 are never answered explicitly; almost no numbers; future work lists items without expected effect or cost.
- **Signal phrases (≤ 3, ≤ 6 words each):** "made significant strides in improving"

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** each paper cites the earlier paper as a publication (the first paper is cited ≈ 18 times in ch. 4 and 6) instead of by chapter number, so each paper stands alone; ch. 1.4 and ch. 7 both describe the studies as a chain (study 2 uses the 2040 network from study 1, study 3 reuses its data); ch. 5 is an explicit bridge that converts the limits of tool 1 into the motivation for tool 2; scenario names (BASE, BASE NZE, GC, SC) are reused unchanged across all three papers.
- **How the RQs or objectives are answered in the conclusion:** not one by one. Ch. 7 goes study by study in order, with prose summaries and one number; the RQs in ch. 2 are not referred to again. Each paper's own conclusion gives more numbers than ch. 7.
- **Anything a strong thesis does that the codes do not capture:**
  - Paper-based framing chapters (1, 2, 5, 7) are only ≈ 17 % of the text; the per-paper abstracts include headline numbers, so the reader gets the result before the method in each paper.
  - The thesis repeats context heavily between ch. 1, ch. 2 and each paper's introduction (subsidy cost, open-source benefits); that is a cost of the paper-based format and a warning for a monograph.
  - Useful for our ch. on method comparison: the deterministic-vs-stochastic comparison (ch. 6) uses identical inputs and switches off differing features to validate, then switches them on to compare. The same design fits a comparison of a deterministic benchmark and our Markov-chain SDDP policy.
  - The ch. 6 literature review mentions that a commercial SDDP-based planning tool is used by the Bolivian authorities and criticises it only for not being open source (relevant if we cite SDDP use in industry; check the source before using it).
