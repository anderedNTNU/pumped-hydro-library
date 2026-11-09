# norland-2025 — Amund Norland, Lasse Skare, Ole Jakob Viken, 2025
- File: theses/texts/capacity-expansion-in-integrated-energy-systems.txt
- Type: monograph
- Topic: multi-stage stochastic LP for capacity expansion at an industrial site (pulp and paper, aluminum), with load shifting, storage, fuel switching and coordinated day-ahead, intraday and reserve (mFRR) participation; tests how scenario-tree size, structure and scenario generation routine (SGR) affect investment quality (in-/out-of-sample stability, VSS, rule-of-thumb benchmark), plus a carbon/technology price sensitivity.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: high (multi-market reserve + spot modelling, storage, scenario-tree stability testing, investment under uncertainty; no SDDP)
- Citation style: author-year
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 30,150 raw (wc -w lines 525–4169, incl. tables, equations, captions, page headers); prose alone ≈ 25,000 (?). Appendices A–G ≈ 5,300 words; 84 references.
- Research questions stated explicitly: yes (1 overarching "problem statement" + 2 numbered RQs, in ch. 1; a central hypothesis is also stated in ch. 1 and repeated in ch. 7)

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| – | Preface (incl. reuse table) | PRE | 37 | 250 | – | 3 | 0 | 1 |
| – | Abstract (+ Norwegian Sammendrag) | ABS | 82 | 400 | – | 6 | 0 | 0 |
| 1 | Introduction | INTRO | 525 | 920 | 3.0 % | 10 | 2 | 0 |
| 2 | Background | BACK | 636 | 2,080 | 6.9 % | 30 | 3 | 1 |
| 3 | Power system flexibility from an industrial perspective | BACK + OTHER(interview-based "methodological study") | 882 | 2,160 | 7.2 % | 30 | 3 | 0 |
| 4 | Techno-economic description and key modeling characteristics | BACK (B-MODELLING-dominated; reads as a modelling-choices chapter) | 1143 | 2,190 | 7.3 % | 28 | 4 | 0 |
| 5 | Mathematical programming | THEORY | 1383 | 1,060 | 3.5 % | 14 | 1 | 0 |
| 6 | Related literature review | LIT | 1541 | 2,430 | 8.1 % | 22 | 0 | 1 |
| 7 | Problem description | PROB | 1822 | 350 | 1.2 % | 6 | 0 | 0 |
| 8 | Mathematical model | MODEL | 1867 | 4,680 | 15.5 % | 30 | 2 | 4 |
| 9 | Case study and input data | DATA + SCEN + VALID-like benchmarks (dummy, EV, deterministic setups) | 2514 | 4,440 | 14.7 % | 51 | 8 | 6 |
| 10 | Computational results and discussion | RES | 3079 | 6,160 | 20.4 % | 72 | 9 | 7 |
| 11 | Discussion of methodology and assumptions | DISC | 3789 | 1,950 | 6.5 % | 16 | 0 | 0 |
| 12 | Conclusion | CONCL | 3983 | 940 | 3.1 % | 10 | 0 | 0 |
| 13 | Future research | FUT | 4082 | 810 | 2.7 % | 10 | 0 | 0 |
| A–G | Reserve products, market actors, historical data analysis, simulation pseudo-code, case data, stability-test statistics, conference paper | APP | 4645 | 5,290 | – | – | 11 | 20 |

Note: background-type material (ch. 2–4) takes ≈ 21 % of the main text, more than the literature review (8 %). Results + data + model ≈ 51 %.

## 2. Chapters

### Preface [PRE]
- **Purpose in one line:** frame the course, thank supervisors and industry contacts, and declare reused project-report material.
- **Opening paragraph does:** names the course and that the thesis builds on the group's project report.
- **Closing paragraph does:** thanks industry representatives for operational insight.
- **Chapter-type specifics:** the reuse declaration is a section-by-section table (section number → what was reused, which figures/tables reused). This replaces an I-REUSE paragraph in the introduction.
- **What makes this strong:** the reuse table is precise (names figures and tables reused) and costs only a few lines.

### Abstract [ABS]
- **Paragraph moves:** AB-CONTEXT+AB-WHY+AB-METHOD, AB-PROBLEM (the overarching RQ plus two secondary aims), AB-CASE+AB-METHOD (two sectors, several SGRs), AB-RES-ECON+AB-RES-OP (up to 35 % lower expected cost; small trees underinvest, 500–1000 scenarios stable), AB-RES-OP (sensitivity: dispatch order, fuel switching, gas with CCS), OTHER(future research directions).
- **What makes it strong:** one headline number (35 %) and concrete tree sizes (100 vs 500–1000 scenarios) make the methodological result tangible.
- **Weakness:** ends on future research rather than an implication; ≈ 400 words is long.

### 1 Introduction [INTRO]
- **Purpose in one line:** move from the energy transition to the industrial investment problem, state hypothesis, problem statement and two RQs.
- **Opening paragraph does:** I-CONTEXT — energy transition and volatility create a need for decision support for industrial prosumers.
- **Closing paragraph does:** I-OUTLINE — one long paragraph walking through all 13 chapters with a purpose clause for each.
- **Subsections (in order):** none.
- **Paragraph moves (in order):** I-CONTEXT, I-CONTEXT+I-HOOK (OR tradition; emission quota share), I-NATIONAL+I-HOOK (Nordic projections, Fig. 1), I-NATIONAL (TSO measures; industry's share of consumption and emissions), I-CONTEXT (Fig. 2: expected demand-side flexibility, heat processes), I-PROBLEM+I-LIT (industry must evaluate flexible assets and multi-market participation; gap stated in one sentence), I-AIM (central hypothesis + problem statement, set off), I-RQ (two numbered RQs), I-CONTRIB, I-OUTLINE.
- **Paragraph length:** average ≈ 80 words; shortest ≈ 35; longest ≈ 170 (outline).
- **Figures and tables:** 2 figures (both third-party projections), each introduced in the text before shown; interpreted with one clause each (no full obs→interp→impl).
- **Chapter-type specifics:** RQs explicit (problem statement + RQ1 on uncertainty representation and value of advanced models, RQ2 on emission and technology prices). Hypothesis given before the RQs. No I-SCOPE, no I-FINDINGS, no I-LIMIT; reuse is in the preface. The literature gap is one sentence inside I-PROBLEM; full gap comes in ch. 6.4.
- **What makes this chapter strong:**
  - A hypothesis → problem statement → numbered sub-RQs ladder; the hypothesis is later tested explicitly in the conclusion.
  - Each number in the hook paragraphs is tied to a source and to a figure, so the reader sees the trend rather than reading a list of percentages.
  - The national context (Nordic/Norwegian) is used to explain why industrial flexibility, not just generation, matters.
  - Contribution is one compact paragraph, separated from the gap.
- **Weaknesses:** no scope/delimitation paragraph; outline is one dense block; gap sentence relies on "to the authors' knowledge" without a citation trail.
- **Signal phrases:** "to the authors' knowledge"; "The central hypothesis is that"; "Specifically, the analysis investigates".

### 2 Background [BACK]
- **Purpose in one line:** explain the Norwegian power system, its actors and the three market types an industrial actor can trade in.
- **Opening paragraph does:** B-SCOPE — announces structure, says Norway is the example but the principles generalise, and fixes two term equivalences (electricity/power market).
- **Closing paragraph does:** B-FACT+OTHER(scope exclusion) — upcoming European platform integration removes price bounds; effect declared out of scope and deferred to future research (it reappears in ch. 13).
- **Subsections (in order):** 2.1 traditional electricity system → structure and actors; 2.1.1 Norwegian system → grid levels, hydro dominance, why balancing becomes harder; 2.1.2 actors and roles → who does what (details to appendix B); 2.2 electricity markets → pricing principles and ongoing reforms; 2.2.1 day-ahead; 2.2.2 intraday; 2.2.3 reserve markets.
- **Paragraph moves (in order, per subsection):**
  - 2.1: B-SCOPE
  - 2.1.1: B-FACT+B-FIG, B-FACT, B-MECH+B-RELEVANCE, B-DEF (ancillary services; only frequency control kept), B-RELEVANCE (opportunity for demand side)
  - 2.1.2: B-SCOPE (pointer to appendix), B-DEF, B-DEF, B-DEF, B-DEF, B-DEF (Fig. 4)
  - 2.2: B-SCOPE, B-MECH (pay-as-cleared vs pay-as-bid; price-taker vs price-setter), B-FACT (dated reforms: 15-min resolution, platforms, delays), B-FIG (pointer to timeline figure)
  - 2.2.1: B-MECH, B-MECH+B-BRIDGE (deviations motivate intraday)
  - 2.2.2: B-MECH+B-FACT, B-RELEVANCE, B-DEF, B-MECH, B-MECH+B-FACT, B-RELEVANCE
  - 2.2.3: B-DEF, B-MECH+B-FIG (reserve products by response time), B-MECH+B-SUMMARY (up/down regulation for a prosumer, Table 3), B-MECH (capacity → activation obligation), B-MECH (activation price bounds and payment direction), B-FACT+OTHER(scope exclusion → future research)
- **Paragraph length:** average ≈ 60 words; shortest ≈ 25; longest ≈ 115.
- **Figures and tables:** 3 figures + 1 table; introduced before shown: mixed (the market-timeline figure is referenced here but printed in ch. 3); interpreted fully: 0 (figures are explanatory diagrams).
- **Numbers from other studies:** ≈ 15 sourced facts with units/% (voltage levels, number of DSOs, renewable and hydro shares, traded TWh, response times, frequency band).
- **Own work mentioned:** ≈ 4 sentences (term choices, scope exclusions).
- **Chapter-type specifics:** each market subsection follows a fixed order: who operates it → how bids/clearing work → timing → why the next market is needed (bridge). Each sub-subsection ends by handing over to the next market.
- **What makes this chapter strong:**
  - Market subsections are chained: the limitation of one market (e.g. no real-time adjustment) is the opening reason for the next.
  - A table translates TSO terminology (up/down regulation) into what an industrial prosumer physically does — reader-centred translation from system view to actor view.
  - Recent, dated regulatory events are included with months, which signals currency; items not modelled are explicitly parked as future research.
  - Definitions of synonyms used interchangeably are fixed once at the start.
- **Weaknesses:** actor descriptions are a list of one-paragraph definitions with little link to the model; timeline figure displaced.
- **Signal phrases:** "used interchangeably throughout this thesis"; "outside the scope of this thesis".

### 3 Power system flexibility from an industrial perspective [BACK + OTHER(interview study)]
- **Purpose in one line:** use interviews with four industrial actors plus literature to derive how industry really trades and what that implies for the model.
- **Opening paragraph does:** B-RELEVANCE — actors have conflicting objectives and the industrial perspective is thin in literature, so a qualitative study is motivated.
- **Closing paragraph does:** B-SUMMARY — last of three "key findings" paragraphs (automatic activation concerns; up-regulation more common).
- **Subsections (in order):** intro (interview design, bullet list of six core questions; interview findings not cited); 3.1 power market trading for industrial actors → contracts, imbalances, internal deadlines, modelling implications; 3.2 DSM → definitions, sector differences, outage cost; 3.3 regulatory barriers (3.3.1 grid tariff, 3.3.2 connection charges); 3.4 key findings.
- **Paragraph moves (in order, per subsection):**
  - intro: B-RELEVANCE, OTHER(interview method + question list), OTHER(note that interview findings are uncited)
  - 3.1: B-MECH, B-MECH+B-MODELLING (fixed-price PPAs → model spot prices only), B-MECH (imbalance settlement), B-MECH (intraday rarely used), B-FIG, B-FIG+B-MODELLING (internal BRP deadlines matter little for modelling), B-CASE (worked MW example of how a BRP caps spot purchase), B-MODELLING (unrestricted real-time adjustment would let the model dodge obligations), B-MODELLING (include adjustments but penalise heavily)
  - 3.2: B-DEF, B-DEF (own definition: load shifting), B-FACT (sector differences, aligned with interviews), B-MECH (process interdependence), B-FACT+B-FIG (outage-cost curve; shedding vs shifting), B-RELEVANCE (manual vs automated flexibility; recovery time example)
  - 3.3: B-SCOPE (barrier taxonomy from a review; two picked)
  - 3.3.1: B-DEF+B-MODELLING (only energy and power parts matter for the optimum), B-FACT (static tariffs weaken incentives; conflicting signals), B-FACT+OTHER(proposed reform → future research)
  - 3.3.2: B-DEF (cost-base formula), B-DEF (terms explained), B-FACT (lead times and cost ranges), B-MECH (connection on terms), B-RELEVANCE+B-MODELLING (framework could analyse it via capacity constraints)
  - 3.4: B-SUMMARY, B-SUMMARY, B-SUMMARY
- **Paragraph length:** average ≈ 55 words; shortest ≈ 25; longest ≈ 130.
- **Figures and tables:** 3 figures; introduced before shown: yes; interpreted (obs→interp→impl): 1 (outage-cost curve → distinguish shedding from shifting).
- **Numbers from other studies:** ≈ 6 (share of support-service load, recovery hours, consumer threshold, connection lead times and costs) plus a 3-number worked example from an interview.
- **Own work mentioned:** ≈ 7 sentences, all of the form "therefore the model should…".
- **What makes this chapter strong:**
  - Qualitative interviews are turned directly into modelling rules (spot price instead of PPA, penalised real-time adjustment), and these rules are later cited back by section number in ch. 8, 9 and 11.
  - The interview guide is shown as a bullet list, so the reader can judge what the evidence covers.
  - A small numerical example (forecast load, reserve commitment, resulting purchase cap) explains a market rule faster than prose would.
  - The chapter ends with a short "key findings" section, which makes the chapter usable as a source for later justifications.
- **Weaknesses:** uncited interview claims are mixed with literature claims in the same paragraphs; four interviews is a thin base and this is not discussed.
- **Signal phrases:** "highlight important modeling implications"; "These findings are not explicitly cited".

### 4 Techno-economic description and key modeling characteristics [BACK, modelling-choices]
- **Purpose in one line:** for each asset class, lay out how literature models it and state which variant this thesis adopts and why (mostly: to stay linear).
- **Opening paragraph does:** B-RELEVANCE — sector coupling and fuel switching as the route to flexibility.
- **Closing paragraph does:** B-MODELLING — discounting of operating costs neglected, with a one-line reason.
- **Subsections (in order):** intro (fuels, power-to-heat, link to project report's technology mapping); 4.1 energy storage; 4.2 load shift; 4.3 generation, conversion and grid technologies (operating modes); 4.4 cost normalisation and discounting (EAC formula).
- **Paragraph moves (in order, per subsection):**
  - intro: B-RELEVANCE, B-FACT, B-FACT, B-SCOPE+B-BRIDGE
  - 4.1: B-MODELLING, B-MODELLING+B-FIG (three ways to stop simultaneous charge/discharge; linear sum-limit chosen), B-MODELLING+B-FIG (generic storage representation), B-MODELLING (simplifications: constant efficiency, full SoC range; degradation needed), B-MECH+B-MODELLING (degradation mechanisms; options from literature), B-MODELLING (cycle-cost approaches rejected as non-linear with endogenous capacity), B-MODELLING (adopted: cost per discharge, post-processable)
  - 4.2: B-MODELLING (separate up/down shift, from interviews), B-MODELLING (ways to price inconvenience; linear cost chosen), B-MODELLING (flexibility characteristics; flexible node balance), B-MODELLING (assumption: production met → no shedding), B-FIG, B-MODELLING (rest time: binary vs implicit approach in two studies), B-MODELLING (rest time not modelled; handled via instance design), B-MODELLING (bottom-up vs top-down), B-MODELLING (framework supports both; ramping left out to avoid binaries)
  - 4.3: B-MODELLING (heat pump input from excess heat; timing caveat), B-MODELLING (operating modes per technology), B-FIG
  - 4.4: B-MODELLING, B-MODELLING (EAC formula), B-MODELLING (discount-rate choice), B-MODELLING (other depreciation methods → future work), B-MODELLING
- **Paragraph length:** average ≈ 70 words; shortest ≈ 25; longest ≈ 155.
- **Figures and tables:** 4 figures (all small schematic diagrams of a modelling idea); introduced before shown: yes; interpreted fully: 0 (explanatory).
- **Numbers from other studies:** 0.
- **Own work mentioned:** ≈ 25 sentences ("this thesis adopts/limits/proposes") — the chapter is essentially a justified-choices chapter.
- **What makes this chapter strong:**
  - Fixed micro-pattern per modelling element: requirement → 2–3 alternatives from literature with their cost (non-linear, binary, complexity) → adopted choice → what is lost. This lets the model chapter later be citation-free.
  - Rejected options are named with the precise reason they fail here (e.g. non-linearity because capacity is endogenous), not just "too complex".
  - Each simplification points to how its effect can be repaired afterwards (post-processing the discharge cost, building rest time into scenario design).
  - Tiny schematic figures with the future symbols already shown, so the reader meets notation before the formulation.
- **Weaknesses:** sits awkwardly between background and model; some choices (load shift without rest time) are argued only by assertion.
- **Signal phrases:** "To retain linearity, this thesis"; "are therefore not selected".

### 5 Mathematical programming [THEORY]
- **Purpose in one line:** give just enough LP/MILP and stochastic programming theory to justify LP, node formulation and stability tests used later.
- **Opening paragraph does:** T-CONCEPT — what mathematical programming is.
- **Closing paragraph does:** T-CONCEPT — out-of-sample stability defined (sets up the main experimental design).
- **Subsections (in order):** intro (LP vs MILP vs NLP); 5.1 stochastic programming (scenario trees, two-stage vs multistage, recourse, decomposition); 5.1.1 multi-stage vs multi-horizon; 5.1.2 node vs scenario formulation; 5.1.3 stability test.
- **Paragraph moves (in order, per subsection):**
  - intro: T-CONCEPT, T-COMPARE
  - 5.1: T-CONCEPT, T-CONCEPT, T-CONCEPT (complete vs relatively complete recourse), T-CONCEPT (decomposition named, not used)
  - 5.1.1: T-CONCEPT, T-RELEVANCE (trade-off; strategic parameters explored by sensitivity instead)
  - 5.1.2: T-COMPARE, T-CONCEPT+T-EXAMPLE (scenario formulation, figure), T-COMPARE+T-RELEVANCE (node formulation smaller; reported size reduction)
  - 5.1.3: T-CONCEPT, T-CONCEPT, T-CONCEPT
- **Paragraph length:** average ≈ 70 words; shortest ≈ 35; longest ≈ 150.
- **Figures and tables:** 1 figure (same small tree drawn in both formulations, side by side); introduced before: yes.
- **Own work mentioned:** ≈ 1 sentence; the chapter stays generic, the link is made later in ch. 8.1 by back-reference.
- **Chapter-type specifics:** no equations at all; theory is verbal. Each subsection is chosen because a later modelling or experiment decision cites it (LP choice, node formulation, no multi-horizon, stability tests).
- **What makes this chapter strong:**
  - Only theory that is later invoked is included; ch. 8.1 and 9 refer back to 5.1.1, 5.1.2 and 5.1.3 by number.
  - A side-by-side figure of the same tree in two formulations explains the difference without equations.
  - Stability testing is introduced as theory before the case study, so results can be read against defined criteria.
- **Weaknesses:** no formal notation for a scenario tree or the deterministic equivalent; the decomposition paragraph is unused.
- **Signal phrases:** "A critical aspect in stochastic programming".

### 6 Related literature review [LIT]
- **Purpose in one line:** review three themes and position the thesis with a feature table.
- **Opening paragraph does:** L-SCOPE — aim, link to the RQ, focus areas.
- **Closing paragraph does:** L-TABLE — introduces the feature-comparison table (20 studies + project report + "our contribution").
- **Subsections (in order):** intro (2 paragraphs); 6.1 multi-market participation under uncertainty; 6.2 industrial flexibility, storage and DSM; 6.3 capacity expansion and decarbonisation pathways; 6.4 our contribution.
- **Paragraph moves (in order, per subsection):**
  - intro: L-SCOPE, L-SCOPE (announces ending with gap and contribution)
  - 6.1: L-TAXONOMY+L-STUDY+L-STUDY+L-NOTCOVERED (coordinated vs separate bidding; two studies with gains), L-GROUP+L-GROUP+L-NOTCOVERED (DA+reserve group; DA+ID+reserve group; none link to capacity expansion), L-STUDY+L-NOTCOVERED, L-GROUP (scenario reduction techniques), L-CRITIQUE+L-PAIR (collapsing real-time stages; one study's justification)
  - 6.2: L-GROUP+L-NOTCOVERED, L-RELEVANCE+L-STUDY, L-STUDY+L-PAIR+L-NOTCOVERED, L-SYNTH+L-GAP, L-CRITIQUE+L-STUDY (overlooked reserve revenue; technology suitability → modelling trade-off), L-STUDY+L-NOTCOVERED, L-GROUP, L-STUDY+L-STUDY+L-NOTCOVERED, L-PAIR+L-NOTCOVERED
  - 6.3: L-RELEVANCE+L-STUDY+L-NOTCOVERED, L-STUDY+L-STUDY+L-CRITIQUE (position papers that propose no method), L-GROUP+L-CRITIQUE (named energy system models lack single-site granularity), L-OWN (open framework judged suitable; its missing reserve markets)
  - 6.4: L-GAP+L-CONTRIB, L-TABLE
- **Per LIT subsection:**
  - 6.1: studies cited 12 · in depth 4 · author-name paragraph openers 1 · critique phrased as "However, they do not consider" / "yet none assess" · ends with a study's simplification of stages and its own justification (prepares the single-stage market choice in ch. 8).
  - 6.2: studies cited 16 · in depth 9 · author-name openers 3 · critique "do not consider uncertainty" / "both studies overlook" · ends L-NOTCOVERED (no uncertainty, no long-term investment).
  - 6.3: studies cited 3 papers + project report + 4 named models (uncited) · in depth 3 · author-name openers 0 · critique "do not propose a methodological framework" · ends L-OWN (tool choice + its limitation).
  - 6.4: 0 new studies · ends with the table.
- **Paragraph length:** average ≈ 90 words; shortest ≈ 28; longest ≈ 170.
- **Figures and tables:** 0 figures, 1 table (feature matrix: markets, stochastic, DSM, capacity expansion of conversion/storage, storage and conversion technologies).
- **Numbers from other studies:** ≈ 7 (gain ranges from coordinated bidding for different storage types, a relative gain, a stage aggregation from hourly to daily, a flexibility cost range in EUR/MWh).
- **Own work mentioned:** ≈ 4 sentences outside 6.4; ≈ 7 including 6.4.
- **What makes this chapter strong:**
  - Almost every paragraph ends with a "does not consider X" sentence where X is one of the thesis's own features (reserve markets, uncertainty, investment, intraday); the table columns are exactly those features, so the critique sentences and the table reinforce each other.
  - Groups of 4–5 studies are cited in one sentence for breadth, then one or two are told in depth — breadth and depth in the same paragraph.
  - Methodological simplifications found in literature (scenario reduction, collapsing stages) are reviewed as a theme, which pre-justifies the thesis's own simplification.
  - The project report gets its own row in the comparison table, making the master-thesis increment visible.
- **Weaknesses:** critique is mostly "not covered" rather than weakness + consequence; few numbers in 6.2–6.3; 6.3 drifts into tool selection.
- **Signal phrases:** "However, they do not consider"; "yet none assess how"; "Building on this".

### 7 Problem description [PROB]
- **Purpose in one line:** restate in plain words why industrial investment under uncertainty with multiple markets is hard, and what the thesis aims to support.
- **Opening paragraph does:** P-ACTOR+OTHER(context recap) — volatility and new expectations on industrial actors.
- **Closing paragraph does:** P-PURPOSE+P-OBJECTIVE — aim, cost minimisation, site-specific constraints.
- **Paragraph moves (in order):** P-ACTOR+OTHER(context recap), P-UNCERT (long lifetimes, unknown future prices and rules), P-UNCERT+P-MARKETS (scenario-based evaluation needed; new market revenue), P-MARKETS+P-DECISIONS (several markets, fuel/technology interdependence), OTHER(hypothesis restated), P-PURPOSE+P-OBJECTIVE.
- **Paragraph length:** average ≈ 60 words; shortest ≈ 35; longest ≈ 70.
- **Chapter-type specifics:** no symbols, no numbers, ≈ 1 page (≈ 350 words). Missing: P-HORIZON, P-SYSTEM detail, P-CONSTRAINTS list, P-OUTPUT. System description is deferred to ch. 8.1.
- **What makes this chapter strong:**
  - Strict placement rule kept: no data or symbols.
  - Restating the hypothesis here links the problem to the test in the results.
- **Weaknesses:** largely repeats the introduction; does not say what a solution contains, the horizon, or the decision sequence — the reader learns those only in ch. 8.1.
- **Signal phrases:** "We hypothesize that explicitly modeling".

### 8 Mathematical model [MODEL]
- **Purpose in one line:** describe the model in words, list assumptions with consequences, define notation, objective and constraints.
- **Opening paragraph does:** D-INTRO — LP and node formulation chosen (back-referencing ch. 5), markets in one stage, activation bidding omitted.
- **Closing paragraph does:** D-CONSTR — optional emission cap.
- **Subsections (in order):** 8.1 model description (verbal, two figures: tree with stage-to-period mapping, on-site energy-flow diagram); 8.2 assumptions (table only); 8.3 notation (sets, parameters, variables tables with units); 8.4 objective (total cost + seven cost-balance equations); 8.5 constraints (grouped under bold run-in headings).
- **Paragraph moves (in order, per subsection):**
  - 8.1: D-INTRO, D-ASSUMP (single-stage markets: limitation stated, then defended with ch. 3 evidence), D-INTRO+D-EXT (stage structure; why no multi-horizon), D-INTRO (figure of information flow per stage), D-ASSUMP (price-taker, participation cap, risk-neutral; consequence given), D-INTRO (flexibility types), D-INTRO (energy-flow figure), D-INTRO (availability), D-INTRO (costs, modes, carbon intensity, CCS), D-INTRO (energy balance)
  - 8.2: D-ASSUMP (table: 8 assumptions, each with consequence/comment)
  - 8.3: D-NOTATION (3 tables)
  - 8.4: D-OBJ, D-OBJ (each component explained; double counting warning)
  - 8.5: D-CONSTR ×18 (energy balances; market balances; intraday volume limit; conversion; ramping; heat-pump input; load shifting ×2; reserve bid limits ×2 incl. note that two constraints are redundant if activation is simulated right; charge/discharge; storage dynamics ×2; energy limits; availability; peak load ×2; CO2 cap)
- **Paragraph length:** average ≈ 75 words for prose paragraphs (helper average 101 includes table text); shortest ≈ 30; longest ≈ 170 (8.1).
- **Figures and tables:** 2 figures, 4 tables; 39 numbered equations (8 objective, 31 constraints).
- **Chapter-type specifics:** citations in model chapter: 0. Assumptions: in a two-column table (assumption | consequence); direction of bias given for 4–5 of 8 (overestimates flexibility, overestimates technology capability, overestimates asset value; two judged "reasonable for large industries"). Constraint order: energy balance → market balances → intraday volume → conversion → ramping → heat-pump input → load shift → reserve bid limits → charge/discharge → storage dynamics → storage energy limit → availability → peak load for tariff → emission cap. Typical explanation: one paragraph of ≈ 50–90 words per group, naming each constraint number and what each term represents, often with a back-reference to ch. 3–5 for the reason.
- **What makes this chapter strong:**
  - Verbal model description before any symbol, with an information-flow figure that maps stages to market decisions.
  - Assumptions table with a "consequence" column states the likely bias of each simplification in one line.
  - Bold run-in group labels ("Storage dynamics:") make 31 constraints scannable; each group's prose says which constraint does what and refers to the section where the choice was argued.
  - Model chapter is citation-free because every choice was argued in ch. 3–5; it cites sections instead of papers.
  - Honest notes such as "these constraints are redundant if…" and boundary-condition explanations (end-of-horizon storage level prevents free energy).
- **Weaknesses:** no D-SUMMARY; parameter and variable tables are long (≈ 4 pages); some assumptions in 8.1 prose are not in the table.
- **Signal phrases:** "Note that if the risk"; "To properly assess the research questions".

### 9 Case study and input data [DATA + SCEN]
- **Purpose in one line:** define the two industrial cases, the four SGRs, the instance grid and test design, the input data, and the benchmark setups (dummy rule-of-thumb, EV/EEV, deterministic with foresight).
- **Opening paragraph does:** A-PURPOSE+A-CASE — two sectors chosen because they differ in flexibility and heat/electricity mix.
- **Closing paragraph does:** A-LIMIT — deterministic-foresight benchmark is only indicative.
- **Subsections (in order):** intro (links RQ1/RQ2 to the setup); 9.1 scenario generation; 9.2 computational instances (instance table, in-/out-of-sample design, reference tree, load-shedding penalty, sensitivity setup); 9.3 input data (9.3.1 site, 9.3.2 technologies, 9.3.3 prices and emissions); 9.4 dummy case (hand-made rule-of-thumb investment); 9.5 deterministic setups (9.5.1 EV/EEV/VSS, 9.5.2 deterministic alternative).
- **Paragraph moves (in order, per subsection):**
  - intro: A-PURPOSE+A-CASE, A-PURPOSE (RQ1 → uncertainty representations; RQ2 → best configuration), A-PROCESS (outline; exchange rate; one stage = one day hourly)
  - 9.1: A-SCEN, A-SCEN, A-PROCESS (historical analysis → two seasons; random version as control), A-SCEN (four SGRs as bullets), A-SCEN+A-FIG, A-SCEN (concentrated routine details), A-SCEN+OTHER(hypothesis behind the routine), A-FIG, OTHER(open question: effect on investment unclear), A-SCEN (diversified as counter-benchmark), A-FIG, A-SCEN+A-PROCESS (whole-day sampling keeps auto- and cross-correlation; equal node probabilities), A-SCEN (rule-based simulation of activation; pseudo-code to appendix)
  - 9.2: A-INSTANCES, A-INSTANCES (20 independent in-sample runs; fixed first stage tested out-of-sample), A-SCEN (reference tree; checked against dataset moments in a table), A-PROCESS (load shedding penalty only out-of-sample, for complete recourse), A-INSTANCES (sensitivity on best configuration)
  - 9.3: A-SOURCE
  - 9.3.1: A-CASE+A-FIG, A-FIG+A-SOURCE, A-SOURCE+A-PROCESS, A-SOURCE, A-PROCESS, A-PROCESS, A-PARAM (load-shift limits per sector)
  - 9.3.2: A-SOURCE+A-FIG, A-PROCESS (ramping dropped as redundant at hourly resolution), A-SOURCE+A-FIG, A-PROCESS
  - 9.3.3: A-SOURCE+A-PROCESS, A-SOURCE+A-PROCESS (synthetic intraday prices), A-PROCESS (penalty level set from a percentile of reserve compensation), A-SOURCE+A-PROCESS, A-SOURCE, A-PARAM-TABLE
  - 9.4: A-INSTANCES, OTHER(levelised-cost screening table), OTHER(reading of screening), OTHER(reserve revenue benchmark), OTHER(storage viability threshold), OTHER(conclusion of screening)
  - 9.5: A-INSTANCES; 9.5.1: A-INSTANCES (VSS defined), A-PROCESS+A-LIMIT (how to take the expectation of binary parameters; alternatives considered), A-INSTANCES+A-LIMIT; 9.5.2: A-INSTANCES, A-LIMIT
- **Paragraph length:** average ≈ 70 words; shortest ≈ 25; longest ≈ 190.
- **Figures and tables:** 8 figures, 6 tables. Data figures interpreted: SGR and site figures explained; cost and PV figures shown with little or no interpretation (≈ 3 of 8 interpreted).
- **Chapter-type specifics:** instance table (36 combinations of size × structure × SGR + benchmarks); each instance class gets a stated goal in prose (dummy → is optimisation needed; deterministic → value of uncertainty; grid → RQ1). Reference tree validated by comparing mean and std. dev. with the dataset. A-LIMIT present for intraday data, EV construction, deterministic benchmark.
- **What makes this chapter strong:**
  - The RQs are mapped to experiment parts in the first lines of the chapter ("RQ1 → …, RQ2 → …").
  - Each SGR comes with the hypothesis it tests and a deliberately opposite routine as a benchmark, so results can confirm or reject the hypothesis.
  - The out-of-sample reference tree is checked against the data's moments in a table before it is used as "truth".
  - A hand-built rule-of-thumb investment (levelised cost per utilisation level, reserve revenue threshold) gives a practitioner benchmark that the optimiser must beat.
  - Every penalty or cap value is justified by a data rule (e.g. a percentile of observed compensation), not picked freely.
- **Weaknesses:** mixes method (SGRs, test design) and data in one long chapter; some data figures lack interpretation; dummy-case section reads like results.
- **Signal phrases:** "To address research question No. 1".

### 10 Computational results and discussion [RES]
- **Purpose in one line:** report runtimes, benchmark comparisons, the RQ1 stability analysis, a second-industry comparison, and the RQ2 carbon/technology price sensitivity.
- **Opening paragraph does:** R-TECH — software, solver, algorithm, hardware.
- **Closing paragraph does:** R-SENS+R-OBS+R-INTERP — as gas use grows with carbon price, grid-tariff costs fall.
- **Subsections (in order):** 10.1 technical performance; 10.2 baseline (10.2.1 VSS, 10.2.2 deterministic and dummy, 10.2.3 removing each flexibility option); 10.3 impact of uncertainty representation (10.3.1 case sizes, 10.3.2 tree structures, 10.3.3 investment and cost components, 10.3.4 aluminum comparison); 10.4 sensitivity (10.4.1 technology mix, 10.4.2 objective components).
- **Paragraph moves (in order, per subsection):**
  - 10.1: R-TECH, R-TECH+R-OBS+R-INTERP (stages costlier than scenarios), R-TECH (reference-tree size and memory), R-TECH+R-CAVEAT
  - 10.2: R-AIMS
  - 10.2.1: R-AIMS, R-STOCH+R-OBS+R-INTERP (why EV underinvests), R-STOCH+R-CAVEAT (large VSS partly from penalty)
  - 10.2.2: R-OBS, R-OBS+R-CAVEAT, R-INTERP (bid cap explains storage size), R-OBS+R-INTERP+R-CAVEAT (35 % better than rule of thumb; which interdependencies the rule misses)
  - 10.2.3: R-AIMS, R-OBS+R-INTERP+R-IMPL, R-OBS+R-INTERP+R-IMPL, R-OBS+R-IMPL
  - 10.3 intro: R-AIMS (RQ1; reading order), R-AIMS (focus sector; "broad then narrow"), OTHER(annual scaling makes instances comparable), OTHER(cost-year note)
  - 10.3.1: R-AIMS (how to read the boxplots; outliers flagged), R-OBS+R-INTERP, R-OBS+R-INTERP (mechanism: underrepresented variability → underinvest → shedding), R-OBS+R-INTERP+R-IMPL, R-OBS+R-INTERP, R-OBS, R-OBS+R-INTERP, R-OBS+R-INTERP, R-SUMMARY
  - 10.3.2: R-AIMS (axis-scaling warning), R-OBS+R-INTERP, R-INTERP+R-IMPL, R-OBS+R-INTERP, R-OBS+R-INTERP (node counts explain coverage), R-OBS+R-INTERP, R-OBS+R-INTERP+R-CAVEAT (possible bias from reference-tree design), R-OBS, R-OBS+R-INTERP (early-stage nodes dominate), R-SUMMARY
  - 10.3.3: R-AIMS (configurations excluded and why), R-OBS+R-INTERP, R-OBS+R-INTERP, R-OBS+R-INTERP+R-CAVEAT, R-OBS+R-INTERP (flat objective, alternative optima), R-INTERP+R-CAVEAT (assumptions favour gas boilers), R-OBS+R-INTERP, R-OBS (minor outliers ignored), R-OBS+R-INTERP+R-IMPL (operating cost dominates; extra investment tuning adds little), R-OBS+R-INTERP, R-OBS+R-INTERP, R-INTERP ("hedging" behaviour), R-OBS+R-IMPL+R-CAVEAT (reserve revenue stable ≈ 5 %)
  - 10.3.4: R-OBS, R-INTERP, R-INTERP, R-OBS+R-INTERP, R-INTERP
  - 10.4: R-AIMS (RQ2), R-AIMS (best configuration chosen from 10.3), R-AIMS (what is held fixed)
  - 10.4.1: R-AIMS (utilisation defined), R-SENS+R-OBS+R-INTERP, R-SENS+R-OBS+R-IMPL, R-SENS+R-OBS+R-INTERP, R-SENS+R-INTERP (dispatch order), R-SENS+R-INTERP, R-INTERP, R-SENS+R-OBS+R-INTERP
  - 10.4.2: OTHER(table reading note), R-SENS+R-OBS+R-INTERP, R-SENS+R-OBS+R-INTERP, R-SENS+R-OBS+R-INTERP
- **Paragraph length:** average ≈ 75 words; shortest ≈ 25; longest ≈ 150.
- **Figures and tables:** 9 figures (boxplots and bar charts), 7 tables; introduced before shown: yes (each figure is named in the first sentence of the paragraph that discusses it). Full obs→interp→impl: 3 of 9 figures; 5 of 7 tables.
- **Chapter-type specifics:** order technical → baseline benchmarks → RQ1 (size → structure → investment/cost mechanism → second case) → RQ2 sensitivity. R-STOCH via VSS plus 20-run in- and out-of-sample stability tests. R-LIT: none in this chapter despite the title (literature comparison moved to ch. 11). R-SUMMARY closes 10.3.1 and 10.3.2 with a "key takeaways" paragraph and a forward pointer.
- **What makes this chapter strong:**
  - "Broad then narrow": weak configurations are explicitly excluded with reasons before the deeper analysis, so later figures show fewer, more relevant instances.
  - Before each figure group, a reading-guide paragraph says what the plot contains, how outliers are marked and what drives them (penalised load shedding).
  - Leave-one-out tests (remove load shift / storage / reserve market) give a clean percentage value for each flexibility option.
  - Results are explained by mechanism (e.g. too little variability in-sample → underinvestment → expensive load shedding out-of-sample), not only described.
  - The second industry is used as a contrast case that explains why the first case's results look the way they do (investment share of objective 12 % vs 0.5 %).
- **Weaknesses:** no comparison with literature in the results; some paragraphs pile up relative standard deviations without a takeaway; RQ2 is answered only with tables.
- **Signal phrases:** "Key takeaways from this section are"; "A key insight is that".

### 11 Discussion of methodology and assumptions [DISC]
- **Purpose in one line:** revisit modelling assumptions, market-participation simplifications and scenario-generation choices, stating how each may bias results.
- **Opening paragraph does:** OTHER(one-line chapter scope).
- **Closing paragraph does:** X-LIMIT — long-term uncertainty (prices, weather, policy) not represented; one study quantifies a solar change.
- **Subsections (in order):** 11.1 modelling assumptions and limitations; 11.2 flexibility, technologies and market participation; 11.3 scenario generation and uncertainty representation.
- **Paragraph moves (in order, per subsection):**
  - intro: OTHER(scope)
  - 11.1: X-ASSUMP+X-METHOD (linearity → no economies of scale; fix with binaries), X-ASSUMP (full-range operation, shift cost, degradation, no multi-horizon; direction given), X-ASSUMP+X-METHOD (ramping; hypothesised small effect and why), X-GENERAL+X-CONTEXT (site-specific data; one finding in line with a cited study)
  - 11.2: X-ASSUMP+X-METHOD (real-time penalty level and side effects; suggested comparison), X-METHOD (refinement with binaries; observed conservative commitments explained), X-ASSUMP+X-LIMIT (intraday value probably underestimated), X-ASSUMP+X-CONTEXT (shedding penalty higher than in literature; defended), X-ASSUMP (risk neutrality and price-taking → upper estimate of reserve revenue; interview evidence pointing the other way), X-ASSUMP (activation as parameter → may overestimate activation benefit)
  - 11.3: X-LIMIT+X-CONTEXT (one data year; volatility may rise), X-METHOD (clustering variable choice; alternatives), X-METHOD (random vs stratified sampling), X-METHOD+X-CONTEXT (reference-tree bias; consistent with a cited study), X-LIMIT
- **Paragraph length:** average ≈ 110 words; shortest ≈ 45; longest ≈ 220.
- **Numbers from other studies:** 1 (range of projected solar change).
- **What makes this chapter strong:**
  - Each assumption is discussed with the direction of the likely bias (overstate, understate, upper estimate) and a concrete fix (binaries, piecewise costs, shorter time steps).
  - Interview evidence is used against the model's own assumption (industry bids larger than the model would), which shows critical distance.
  - Possible bias from the experimental design itself (reference tree built with one of the tested routines) is raised and checked against the results and a prior study.
- **Weaknesses:** X-IMPL (implications for industry/policy) almost absent; few comparisons with literature numbers; future-work ideas leak into the discussion.
- **Signal phrases:** "may overstate the economic potential"; "we hypothesize that constructing".

### 12 Conclusion [CONCL]
- **Purpose in one line:** summarise what was done and answer RQ1 then RQ2 with key numbers, then give an overall verdict.
- **Opening paragraph does:** C-PROBLEM+C-DONE — model, markets, two cases.
- **Closing paragraph does:** C-OVERALL — accounting for uncertainty improves decisions, especially for flexible, variable systems.
- **Paragraph moves (in order):** C-PROBLEM+C-DONE, C-ANSWER+C-FIND-INV (VSS; hypothesis supported), C-ANSWER+C-FIND-ECON (rule-of-thumb 35 % worse), C-DONE (what was varied), C-ANSWER+C-FIND-INV (small trees insufficient; diversified routine helps), C-ANSWER+C-FIND-INV (systematic routines better for larger trees; medium size enough; hypothesis supported), C-FIND-INV+C-POINTER (investment share small when capacity suffices; 12 % vs 0.5 %), C-FIND-ECON (reserve participation consistently profitable but site-specific), C-ANSWER+C-FIND-INV (RQ2: dispatch order 2025 vs 2050, fuel switching, CCS), C-OVERALL.
- **Paragraph length:** average ≈ 90 words; shortest ≈ 55; longest ≈ 145.
- **Chapter-type specifics:** RQs answered in order (RQ1 parts first, RQ2 last) but not labelled "RQ1/RQ2"; ordering words ("Firstly", "Further", "Lastly") carry the structure. Numbers given (35 %, 100 / 500 / 1000 scenarios, 12 % vs 0.5 %). Hypothesis revisited twice. No C-LIMIT paragraph.
- **What makes this chapter strong:**
  - One paragraph per finding, each opening with the finding and closing with what it means for a decision maker.
  - The hypothesis from ch. 1 and 7 is explicitly marked as supported, closing the loop.
  - Scenario counts are translated into practical advice (what size is enough; which routine to use if forced to go small).
- **Weaknesses:** RQs not named, so the reader must map paragraphs to RQs; limitations absent.
- **Signal phrases:** "Firstly, the value of"; "A particularly interesting observation is"; "In conclusion, this thesis demonstrates".

### 13 Future research [FUT]
- **Purpose in one line:** list methodological refinements and market/regulatory developments worth studying.
- **Opening paragraph does:** OTHER(intro: method refinements and system-level directions).
- **Closing paragraph does:** F-EXT — broad outlook (geopolitics, policy, technology) with only "what".
- **Paragraph moves (in order):** OTHER(intro), F-EXT ×9.
- **Four-part check per extension (what / why current assumption limits / expected effect / complexity cost):**
  1. Unit-commitment detail (rest periods, process inflexibility): what ✓ · why ✓ (scalability prioritised) · effect ✓ · cost (implicit) (?)
  2. Non-linear degradation, minimum investment, more reserve markets, eligibility mapping: ✓ · partial · ✓ · ✗
  3. Embed in an open modelling platform with reserve markets: ✓ · ✗ · ✓ (validation, reuse) · ✗
  4. Sequential instead of single-stage market bidding: ✓ · ✓ · partial · ✗
  5. Market trajectories and 15-minute resolution: ✓ · ✗ · partial · ✗
  6. Shift of volume to activation market; multi-horizon investment periods: ✓ · partial · partial · ✗
  7. Emission quota allocation: ✓ · ✗ · ✓ · ✗
  8. Tariff reform and connection on terms: ✓ · ✓ (static tariff) · ✓ · ✗
  9. Broad outlook: ✓ · ✗ · ✗ · ✗
- **What makes this chapter strong:** several items are the very items parked as "left for future research" in ch. 2–4 and 11, with section back-references, so nothing raised earlier is dropped.
- **Weaknesses:** complexity cost almost never stated; no prioritisation.
- **Signal phrases:** "Building on the findings, limitations"; "An interesting extension could be".

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** dense back-references by section number (e.g. the interview-derived rule to penalise real-time adjustment appears in 3.1 → 8.1 → 9.3.3 → 11.2). Theory in ch. 5 is cited by section in ch. 8.1 to justify LP, node formulation and no multi-horizon. RQs are referred to by number in ch. 9 and 10 ("research question No. 1"). The hypothesis appears in ch. 1, ch. 7, ch. 9.1 (routine-specific hypotheses) and the conclusion. Items declared out of scope in background chapters reappear in Future research.
- **How the RQs or objectives are answered in the conclusion:** in order (RQ1 sub-findings first, RQ2 last), one paragraph per finding, with numbers; RQs not labelled; hypothesis explicitly confirmed.
- **Anything a strong thesis does that the codes do not capture:**
  - A small qualitative interview study (question list shown) used as evidence for modelling rules.
  - A practitioner "rule-of-thumb" benchmark built by hand (levelised cost by utilisation, reserve revenue threshold), compared out-of-sample with the stochastic solution.
  - A modelling-choices chapter (ch. 4) that frees the model chapter from citations.
  - A feature-comparison table with a row for the earlier project report and a row for the thesis.
  - Results narrowed step by step, with excluded configurations named and justified.
  - Reading-guide sentences before figure groups (axis scaling differs, red labels mark outliers, what the outliers mean).
  - Preface reuse table at section level.
