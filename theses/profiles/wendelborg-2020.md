# wendelborg-2020 — Magnus A. Wendelborg, 2020
- File: theses/texts/sequencing-of-wholesale-electricity-markets-day-ahead-and-in.txt
- Type: monograph (with a draft journal paper attached as Appendix B; the paper is not coded here)
- Topic: three-stage stochastic capacity expansion model (EMPIRE extension: investment stage, day-ahead stage, intraday stage) to test how forecast errors between market stages change European investment and operation; simplified 3-node test case, then a 35-node European case and a deterministic counterpart.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: medium (multi-market sequencing with commitment links between stages, value-of-stochastic-solution attempt, hourly operation plots for a hydro node NO2; no SDDP, no plant-level view)
- Citation style: numeric ([n]), 63 references
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 19,000 by `wc -w` on lines 513–2705; this includes garbled equations, captions and table cells. Prose only ≈ 16,000 (?).
- Research questions stated explicitly: yes (3 RQs, bulleted at the end of ch. 1; RQ1 also repeated in the abstract; all three repeated verbatim as headings in ch. 7)

Front matter (not main text): preface (3 paragraphs: degree context, supervisor thanks, personal thanks), abstract (2 paragraphs, ≈ 390 words), Norwegian summary (1 long paragraph), nomenclature (abbreviations, then sets / parameters / variables grouped by role: supply-technology, temporal, spatial, stochastic, subsets; costs; technology limits; scenario input; investment and operational variables).

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| – | Abstract | ABS | 73 | 390 | – | 2 | 0 | 0 |
| 1 | Introduction | INTRO | 513 | 800 | 4 % | 5 (+ 3 RQ bullets) | 2 | 1 |
| 2 | Literature Review | LIT | 610 | 1,480 | 8 % | 7 | 0 | 1 |
| 3 | Problem Description | PROB | 765 | 1,310 | 7 % | 12 | 0 | 0 |
| 4 | Method | MODEL + SCEN (4.1–4.2 partly FRAME) | 909 | 4,520 (much of it equations) | 24 % | ≈ 35 prose + ≈ 12 one-line equation lead-ins | 3 | 0 |
| 5 | Simplified Test Case | VALID + DATA + RES | 1535 | 3,450 | 18 % | 19 | 4 | 3 |
| 6 | European Case Study | DATA (6.1) + RES + DISC (merged, "Results and Discussion") | 1919 | 6,240 | 33 % | 40 | 18 | 2 |
| 7 | Conclusion (incl. 7.1 Future Work) | CONCL + FUT | 2560 | 1,220 | 6 % | 6 + 4 bullets; 7.1: 1 + 5 headed items | 0 | 0 |
| A | Results from European case study | APP | 3013 | tables only | – | 0 | 0 | 8 |
| B | Paper: Designing day-ahead and intraday markets… | APP (draft journal paper with own intro, lit, model, results, conclusion and a scenario-generation appendix) | 3173 | – | – | – | – | – |

No separate background, theory, solution-method or discussion chapter. Market background is folded into ch. 1 (market stages explained) and ch. 3 (market types). Discussion is folded into every results paragraph (support from literature is cited inside the results).

## 2. Chapters

### Abstract [ABS]
- **Purpose in one line:** state driver, gap and RQ1, method and cases, then four numbered conclusions with numbers.
- **Paragraph moves:** P1: AB-CONTEXT (VRES growth makes intraday trading more important) + AB-PROBLEM (little literature on forecast errors in capacity expansion) + RQ1 written out as a question. P2: AB-METHOD (stochastic expansion model with DA and ID stages, EU emission path to 2050) + AB-CASE (three cases: standard, stochastic sequencing, deterministic sequencing) + numbered findings: OTHER(investment result: −10 % VRES, +40 % flexible) + AB-RES-OP (transmission volume +10–20 %) + OTHER(storage over-valued) + AB-RES-ECON (deterministic under-estimates cost, can be infeasible) + AB-IMPL + computational-cost note + future-work list.
- **Distinctive:** findings are given as a numbered list "1) … 4)" inside running prose, each with a percentage; the same four reappear as bullets in ch. 7.

### 1 Introduction [INTRO]
- **Purpose in one line:** motivate why forecast errors between day-ahead and intraday matter for long-term investment, and pose three RQs.
- **Opening paragraph does:** I-CONTEXT — shift from dispatchable to renewable generation, climate targets, projected continuation (three citations).
- **Closing paragraph does:** I-OUTLINE + I-REUSE — chapter-by-chapter roadmap, then a note that a journal paper was written in parallel and is attached as Appendix B.
- **Subsections (in order):** none.
- **Paragraph moves (in order):** I-CONTEXT, I-CONCEPT+I-PROBLEM (uncertainty from VRES; the day-ahead / intraday / balancing sequence explained plainly in one long paragraph), I-HOOK+I-CONTEXT (installed wind and solar growth 2015–2019 with percentages and GW, linked to Fig. 1.1, then intraday share growth from Fig. 1.2 / Table 1.1 and the inference that dependence on intraday trading will rise), I-RQ (one lead sentence + three bulleted RQs), I-OUTLINE+I-REUSE.
- **Paragraph length:** average ≈ 140 words; shortest ≈ 85 (opening); longest ≈ 210 (market-stage concept).
- **Figures and tables:** 2 figures + 1 table; introduced before shown: yes; interpreted after: the figure and table get observation → interpretation (more VRES coincides with more intraday volume) → implication (dependence on intraday will grow). 1 of 3 items explicitly carries all three; the table is not discussed separately.
- **Chapter-type specifics (INTRO):** no explicit I-AIM or I-CONTRIB paragraph (the contribution is placed at the end of ch. 2 instead); no I-SCOPE, I-FINDINGS or I-LIMIT. RQs: 3, ordered investment → operation → value of uncertainty, which is exactly the order of the answers in ch. 7. The hook is built from the author's own pull of ENTSO-E data rather than a quoted statistic.
- **What makes this chapter strong:**
  - The market-stage sequence (day-ahead → intraday → balancing) is explained in plain words in one paragraph before any RQ, so the reader knows what "market sequencing" means before it is asked about.
  - The data hook is the author's own figure built from a public platform, and each percentage is given with start and end values (GW 2015 → GW 2019), which makes the growth checkable.
  - The RQs follow directly from the data paragraph with a one-sentence bridge ("In line with … development"), so the questions feel caused by the evidence.
  - RQs are written so each maps to one result block later (investment, operation, uncertainty).
- **Weaknesses:** very short (≈ 4 % of text); no explicit gap or contribution statement in the introduction itself; Table 1.1 duplicates Fig. 1.2 without added discussion.
- **Signal phrases:** "three research questions are proposed"; "The thesis is structured as follows"

### 2 Literature Review [LIT]
- **Purpose in one line:** survey flexibility needs, multi-market operational models and capacity expansion models, then show that combining the two is rare and done only for a small system.
- **Opening paragraph does:** L-SCOPE — why the field has grown (climate, computing power) and the focus (investment and operational decisions under VRES uncertainty), with a back-reference to the RQs in ch. 1.
- **Closing paragraph does:** L-GAP + L-CONTRIB — combined models are rare and only on small systems with little transmission and storage; this work sets out to quantify the effect on generation, transmission and storage capacity.
- **Subsections (in order):** none; themes are signalled by paragraph-opening transition sentences.
- **Paragraph moves (in order):** L-SCOPE, L-RELEVANCE+L-GROUP+L-PAIR (flexibility providers; one study favours transmission, another storage — contrasted with "However"), L-TAXONOMY (capacity expansion vs operational models), L-GROUP+L-STUDY+L-PAIR (multi-market operational models: six studies in a chain, one contrasted against two others), L-STUDY+L-PAIR (capacity expansion under uncertainty: stochastic vs deterministic; risk in the discount rate; transmission; emission caps; operational detail — a long chain across a page break), L-STUDY+L-CRITIQUE+L-TABLE+L-SYNTH (the single combined study, its limits, then the comparison table and an expectation for the results), L-GAP+L-CONTRIB.
- **Paragraph length:** average ≈ 210 words; shortest ≈ 55 (taxonomy); longest ≈ 345 (capacity expansion chain).
- **Figures and tables:** 1 table (Table 2.1: author, whether investments are modelled, which markets; 13 rows); introduced before shown: yes; interpreted after: no (the table is not discussed beyond one sentence pointing to it).
- **Numbers from other studies:** 1 (storage of about one day of load).
- **Own work mentioned:** ≈ 6 sentences (back-reference to RQs, "issues addressed in this thesis", table of literature used to build the model, expected effect on our results, gap/aim sentences).
- **Chapter-type specifics (LIT):** studies cited ≈ 25 (refs 10–34); told in depth (≥ 2 sentences) ≈ 12; paragraphs opening with an author name: 0 (every paragraph opens with a thematic sentence, author names start sentences inside); critique phrased once, explicitly, against the closest study ("However, [authors] used" a small one-country model without transmission or storage results); other studies are reported, not critiqued. The section ends with an expectation (systems will rely more on flexibility and costs will rise), which is later tested in the results — a hypothesis move not covered by the codes.
- **What makes this chapter strong:**
  - Ordered as two separate strands (operational multi-market models, then investment models) followed by the one study that joins them; the gap falls out of the structure rather than being asserted.
  - Contradicting findings are set side by side in the same paragraph (transmission vs storage as best flexibility source; higher vs lower total cost with more VRES), which later lets the results "take sides".
  - The single closest competitor gets the only explicit critique, and the critique names exactly the dimensions the thesis adds (system size, transmission, storage).
  - A literature-derived expectation is written down at the end and re-checked in ch. 5 ("hypothesis" not met, explained) and ch. 6.
  - The comparison table uses two binary/category columns (investment yes/no, markets covered) that make the gap visible at a glance.
- **Weaknesses:** long chained paragraphs with one sentence per study read as a list; only one critique; the table has no row for "this thesis" and is not discussed.
- **Signal phrases:** "In addition to multi-market modeling"; "This thesis aims to fill"

### 3 Problem Description [PROB]
- **Purpose in one line:** describe in words only the planner's capacity expansion problem with a day-ahead and an intraday stage.
- **Opening paragraph does:** P-PURPOSE — one short paragraph naming the problem and the focus on forecast errors.
- **Closing paragraph does:** OTHER(summary) — restates problem and objective in two sentences.
- **Subsections (in order):** 3.1 Problem Definition → system, markets, stage structure; 3.2 Objective → minimise expected discounted system cost, what costs include; 3.3 Decisions → strategic vs two operational groups, information at each stage; 3.4 Assumptions → known costs and sites, no outages, perfect competition, information timing, cross-border intraday trading, full re-balancing market design; 3.5 Restrictions → investment limits, then operational limits; 3.6 Summary.
- **Paragraph moves (in order, per subsection):**
  - intro: P-PURPOSE
  - 3.1: P-SYSTEM+P-ACTOR (perspective of a capacity expansion planner; generation, transmission, storage), P-MARKETS+P-UNCERT (forward ignored; day-ahead vs intraday; forecasts deviate from reality), P-HORIZON+P-UNCERT (strategic stages + two operational stage types; why forecast errors matter for investment)
  - 3.2: P-OBJECTIVE
  - 3.3: P-DECISIONS (three ordered groups of decisions, tied to information available)
  - 3.4: P-SCOPE, P-SCOPE (market-design assumption flagged as "crucial", with its consequence: day-ahead not binding)
  - 3.5: OTHER(signpost sentence), P-CONSTRAINTS (investment), P-CONSTRAINTS (operations: balance, load shedding only intraday, ramping between markets, capacity, storage, hydro reservoir, losses, emission cap)
  - 3.6: OTHER(summary)
- **Paragraph length:** average ≈ 105 words; shortest ≈ 30 (intro); longest ≈ 245 (operational restrictions).
- **Figures and tables:** 0.
- **Chapter-type specifics (PROB):** symbols: none. Numbers: one (information revealed one hour before delivery). Length ≈ 3.3 pages. P-OUTPUT (what a solution contains) is not stated separately. Headings follow a fixed template (definition, objective, decisions, assumptions, restrictions, summary).
- **What makes this chapter strong:**
  - Fixed heading skeleton (objective / decisions / assumptions / restrictions) makes the verbal problem map one-to-one onto the later formulation: restrictions are listed in roughly the order the constraints appear.
  - Decisions are grouped by when information is revealed (before forecast, with forecast, with actual values), which is exactly the stage structure of the stochastic model.
  - The single most consequential assumption (intraday re-balances the full load) is singled out in its own paragraph and its consequence is stated.
  - Strictly no symbols and no data, so the chapter reads for a non-modeller.
- **Weaknesses:** the actor is a generic "system" planner and is never named; 3.1 partly re-explains market background already given in ch. 1; restrictions paragraph is a dense list.
- **Signal phrases:** "Let us take the perspective"; "A crucial assumption is the"

### 4 Method [MODEL + SCEN, 4.1–4.2 partly FRAME]
- **Purpose in one line:** present the base model (EMPIRE), the added day-ahead/intraday structure, the full formulation, scenario generation, model shortcomings and a derived intraday-volume metric.
- **Opening paragraph does:** M-OVERVIEW — roadmap of the five sections.
- **Closing paragraph does:** OTHER(metric caveat) — the computed intraday volume is not comparable with the historical volumes in ch. 1 because of the market design, but still shows the difference between stages.
- **Subsections (in order):** 4.1 EMPIRE → base model, geography, temporal structure, uncertainty; 4.2 Explanation of the model → three stages, flexible vs inflexible generators, links between markets (Fig. 4.2), availability definition; 4.3 Model Formulation (4.3.1 objective, 4.3.2 constraints split into operational and investment) → full LP; 4.4 Scenario Generation → sampling + moment matching; 4.5 Shortcoming of the model → simplifications and their consequences; 4.6 Intraday Volume → post-processing metric.
- **Paragraph moves (in order, per subsection):**
  - intro: M-OVERVIEW
  - 4.1: D-INTRO (base model type, nodes, periods, seasons, where uncertainty sits)
  - 4.2: D-INTRO+D-ASSUMP (three stages, perfect competition, best-guess clearing, inflexible units committed), D-ASSUMP+M-WORKFLOW (storage fully flexible between markets; Fig. 4.2 explains the links), D-PHYS (normalised availability, eq. 4.1)
  - 4.3: D-NOTATION (pointer to nomenclature), D-OBJ, D-OBJ; then 15 constraint blocks, each D-CONSTR: DA balance, ID balance, DA–ID deviation limits, capacity limits, ramping, storage initial/final level, storage balance, storage energy limit, charge/discharge limit, hydro seasonal and annual limits, transmission NTC, emission cap, capacity accumulation, investment and installed caps, power–energy ratio
  - 4.4: A-SOURCE+A-SCEN, A-SCEN (moment-matching procedure step by step), A-SCEN (symbols of the distance measure), A-SCEN+A-PROCESS (which series are matched, how nodes are weighted, why the same hours are reused)
  - 4.5: D-ASSUMP+X-LIMIT (linearised physics, perfect market, no start-up or minimum-run, no reserves or outages → investments may sit at a bare minimum), D-ASSUMP+A-LIMIT (no cost recovery for units that reduce output; availability data reflect bids, not weather)
  - 4.6: OTHER(metric definition), OTHER(metric equations), OTHER(metric equations), OTHER(why only increases are counted: zero-sum, no double counting), OTHER(metric as share of load), OTHER(metric caveat)
- **Paragraph length:** average ≈ 85 words (prose); shortest ≈ 35 (constraint explanations); longest ≈ 305 (shortcomings, joined across page break).
- **Figures and tables:** 3 figures (EMPIRE overview, DA–ID link, merit-order clearing); introduced before shown: yes; interpreted after: Fig. 4.2 explained in text; Figs. 4.1 and 4.3 only referenced.
- **Chapter-type specifics (MODEL):** citations in the formulation section 4.3: 1 (emission policy source); citations in the whole chapter: ≈ 15 (base model, its applications, scenario approach, shortcomings literature). Constraint order: operational first (balance DA → balance ID → inter-market link → capacity → ramping → storage → hydro → transmission → emissions), then investment (accumulation → caps → storage ratio). Typical explanation length after each constraint block: ≈ 40–90 words (median ≈ 55); pattern is a one-line plain-language lead-in sentence ending in a colon, the equation(s), then a paragraph starting "Constraints (x)–(y) …". Notation lives entirely in the front-matter nomenclature. Assumptions in 4.5: consequences given for several (minimal investment, unmet demand in extremes, uncompensated generators), but direction of bias on results is mostly not stated. No separate SOLVE chapter: solver, hardware and runtime are never reported; only model size (constraints, variables) appears later.
- **What makes this chapter strong:**
  - Every constraint block is preceded by a one-line plain-English lead-in ("storage balance between time steps:") and followed by an explanation, so the reader always knows what an equation is for before reading it.
  - Day-ahead and intraday versions of each constraint are shown as twin equations, making the stage duplication visible and easy to check.
  - Constraints are explained by role, in a fixed order (balance → links between stages → capacity → dynamics → resource limits → policy → investment), which follows the problem chapter's restriction list.
  - A dedicated "shortcomings" section states each simplification together with what it may cause in the results (e.g. bare-minimum investment).
  - A post-processing indicator (intraday volume) is defined with equations and a justification for counting only upward changes, then explicitly marked as not comparable to observed data.
- **Weaknesses:** chapter title "Method" mixes model, data and limitations; no solution-method or runtime information; a constraint reference typo (4.22 twice) suggests limited proofreading.
- **Signal phrases:** "There is also the issue"; "Note that we only consider"

### 5 Simplified Test Case [VALID + DATA + RES]
- **Purpose in one line:** proof of concept on a three-node system (Germany, Denmark, France) with four cases, before the full European run.
- **Opening paragraph does:** V-PURPOSE+V-SETUP — why a reduced case is run, what is reduced, pointer to data and to ch. 6.
- **Closing paragraph does:** R-LIT+V-VERDICT+R-CAVEAT — findings agree with the literature; flexible sources gain value; the approach is better but much heavier computationally.
- **Subsections (in order):** 5.1 Description of cases (5.1.1 Case 0 standard, 5.1.2 Case 1 base case, 5.1.3 Case 2 no intraday transmission, 5.1.4 Case 3 less flexibility) → one goal per case; 5.2 Input Data (5.2.1 Data Gathering) → system, emission cap, periods, scenarios, data cleaning; 5.3 Results (5.3.1 objective, 5.3.2 investments, 5.3.3 output, 5.3.4 transmission and storage in case 0, 5.3.5 storage, 5.3.6 transmission); 5.4 Conclusion.
- **Paragraph moves (in order, per subsection):**
  - intro: V-PURPOSE+V-SETUP
  - 5.1: A-INSTANCES (case 0 as reference), A-INSTANCES+D-ASSUMP (case 1; why intraday cross-border trading is allowed, with current market project as justification), A-INSTANCES (case 2 + modified constraint 5.1), A-INSTANCES (case 3 + modified constraints with a cited ramping assumption)
  - 5.2: A-CASE+A-PARAM-TABLE+A-SCEN+R-TECH (nodes, emission cap table, cost years, periods, scenario sampling, model size), A-SOURCE+A-PROCESS+A-LIMIT (ENTSO-E data, gaps filled by neighbours, median smoothing, onshore profiles reused for offshore and the consequence)
  - 5.3: R-AIMS; 5.3.1: R-OBS+R-INTERP+R-LIT; 5.3.2: R-OBS+R-INTERP (drop in capacity explained by lifetimes and end-of-horizon effect), R-OBS+R-INTERP+R-LIT (expected rise in flexible capacity not seen; explained by capacity and emission caps); 5.3.3: R-OBS+R-INTERP, R-OBS+R-INTERP (case differences explained by what each case restricts); 5.3.4: R-OBS+R-INTERP, R-OBS+R-INTERP; 5.3.5: R-OBS+R-INTERP; 5.3.6: R-OBS+R-INTERP+R-LIT
  - 5.4: R-SUMMARY+V-VERDICT, R-LIT+V-VERDICT+R-CAVEAT
- **Paragraph length:** average ≈ 155 words; shortest ≈ 55; longest ≈ 300 (data gathering).
- **Figures and tables:** 4 figures (scenario tree, installed capacity case 1, case 0, output case 1) + 3 tables (emission cap, generator sets, key results of four cases); introduced before shown: mixed; observation → interpretation → implication complete: ≈ 1 of 4 figures (Fig. 5.3, set against the stated hypothesis); others get observation + interpretation.
- **Chapter-type specifics (VALID):** no V-CHECK of correctness against a known solution and no V-BENCH; the "validation" is that the results behave as the case design predicts (case 2 deviates most because transmission is fixed; case 3 deviates least because ramping is restricted) and agree with cited studies. Model size reported (constraints and variables for case 0 vs sequencing cases). Each case has a stated goal: yes (4 of 4).
- **What makes this chapter strong:**
  - Each test case isolates one mechanism (no intraday transmission, shorter gate closure) and states its goal and the exact constraint change, so results can be read as controlled experiments.
  - Results are explained by the case design itself ("this case restricts X, so Y deviates most"), which doubles as a sanity check of the model.
  - An unmet hypothesis is reported openly and explained by binding capacity and emission limits.
  - A model artefact (end-of-horizon effect in the last period) is named and explained rather than left in the figures.
  - A one-table summary of key results across all cases precedes the subsection-by-subsection discussion.
- **Weaknesses:** the test case doubles as a full results chapter, so later European results repeat the same structure; no formal verification; storage/transmission split over three small subsections with overlap.
- **Signal phrases:** "The hypothesis of the thesis"; "These results are also supported by"

### 6 European Case Study [DATA (6.1) + RES + DISC]
- **Purpose in one line:** run the 35-node European model for three cases and answer the RQs, ending with the value of considering uncertainty.
- **Opening paragraph does:** R-AIMS+A-CASE — answer the RQs; nodes, periods, seasons, scenarios, data source, pointer to Appendix A.
- **Closing paragraph does:** R-STOCH+R-INTERP+R-IMPL — although the VSS could not be computed, the cost gap and the under-sized deterministic capacity show that the stochastic plan is more robust; capacity saved costs less than shortage.
- **Subsections (in order):** 6.1 Description of Cases (case 0 standard, case 1 stochastic sequencing, case 2 deterministic sequencing) → cases and model size; 6.2 Results and Discussion (6.2.1 objective, 6.2.2 investments, 6.2.3 output); 6.3 Storage (6.3.1 operation); 6.4 Transmission; 6.5 Curtailment; 6.6 Intraday Volume; 6.7 Hourly operations in Germany and Norway (choice of nodes and week, one subsection per case, then comparison split into DA Norway, DA Germany, ID Norway, ID Germany); 6.8 The Importance of Considering Uncertainty.
- **Paragraph moves (in order, per subsection):**
  - intro: R-AIMS+A-CASE
  - 6.1: A-INSTANCES+R-TECH, A-INSTANCES+R-TECH, A-INSTANCES+R-TECH (deterministic case built from scenario averages; why its size is not directly comparable)
  - 6.2: R-AIMS (structure of the section); 6.2.1: R-OBS+R-INTERP+R-LIT+R-IMPL, R-INTERP+R-TECH; 6.2.2: R-OBS, R-OBS, R-OBS+R-INTERP, R-OBS+R-INTERP+R-LIT, R-INTERP (why capacity grows over time: demand, storage and transmission use, lower capacity factor); 6.2.3: R-OBS+R-INTERP+R-LIT, R-OBS+R-INTERP+R-LIT, R-OBS+R-INTERP+R-LIT (two competing explanations for higher intraday VRES output weighed against Fig. 6.5)
  - 6.3: R-OBS+R-INTERP+R-LIT, R-INTERP+R-IMPL+R-LIT+R-CAVEAT (storage over-valued without forecast errors; caveat that no curtailment penalty exists); 6.3.1: R-OBS+R-INTERP
  - 6.4: R-OBS+R-INTERP+R-LIT, R-OBS+R-INTERP+R-LIT
  - 6.5: R-OBS+R-INTERP
  - 6.6: OTHER(back-reference to the motivating data in ch. 1)+R-AIMS, R-OBS+R-INTERP+R-LIT
  - 6.7: R-AIMS; 6.7.1: OTHER(justification of the chosen nodes and week); 6.7.2: R-OBS+R-INTERP, R-OBS+R-INTERP+R-LIT; 6.7.3: R-OBS+R-INTERP, R-OBS+R-INTERP; 6.7.4: R-OBS+R-INTERP, R-OBS+R-INTERP; 6.7.5: R-OBS, R-OBS+R-INTERP, R-OBS+R-INTERP (includes an admitted unclear pattern with two tentative explanations), R-OBS+R-INTERP
  - 6.8: R-AIMS, R-STOCH (VSS defined and procedure), R-STOCH (infeasible: explained via the day-ahead balance equality and absence of day-ahead load shedding), V-CHALLENGE (four remedies tried or considered and why each was rejected), R-STOCH+R-INTERP+R-IMPL
- **Paragraph length:** average ≈ 155 words; shortest ≈ 40; longest ≈ 280 (remedies for infeasibility).
- **Figures and tables:** 18 figures + 2 tables (objective and model size; intraday volume by period); introduced before shown: mixed (text references often come after the float because of placement); observation → interpretation → implication complete: ≈ 3 of 18 (storage capacity, storage load coverage, intraday contributions) (?); the ten operational-week figures get observation + interpretation, often hour-by-hour.
- **Numbers from other studies:** 0 (≈ 14 qualitative "supported by [n]" statements; no cited numbers are compared with own numbers).
- **Chapter-type specifics (RES):** order: technical/size (6.1, 6.2.1) → economic (objective) → investment (generation) → operational (output) → storage → transmission → curtailment → intraday metric → hourly operations → value of uncertainty. Discussion is merged: literature support is attached to most results paragraphs. Runtime and solver are not reported; size in millions of constraints/variables is. R-SENS: none. R-STOCH: VSS attempted, failed by infeasibility, then replaced by a qualitative cost-gap argument.
- **What makes this chapter strong:**
  - Every case comparison is quantified relative to the reference case (±% of standard model), so all differences share one baseline.
  - When two explanations are possible, both are stated and one is tested against a figure (forecast vs actual availability plot used to weigh "better weather" against "over-dispatch").
  - The hourly-operations section first justifies the choice of nodes (a flexible hydro exporter and a VRES-heavy importer) and the week, then walks the same week through each case, then compares by market and node — a reusable template for showing stage-wise operation.
  - Hour ranges on the figures are named explicitly (e.g. specific hour windows where exports flip to imports), which ties prose to the plot precisely.
  - The failed VSS is turned into a result: the cause is traced to a specific constraint, each attempted fix is reported with why it was rejected, and a fallback argument is given.
- **Weaknesses:** literature support is mostly "supported by [n]" without saying what the cited study found or with what numbers; few implications for actors; 18 figures, many with very similar content; inconsistent cost-gap figures between sections (7.3 % vs ≈ 10 %, against different reference cases) are not reconciled.
- **Signal phrases:** "Two rationales can explain"; "It is difficult to state"

### 7 Conclusion [CONCL] and 7.1 Future Work [FUT]
- **Purpose in one line:** recap what was built and tested, answer the three RQs under their own headings, list four main conclusions, and propose five extensions.
- **Opening paragraph does:** C-PROBLEM+C-DONE — what the method does, that the test case proved it works, and what each of the three European cases represents.
- **Closing paragraph does:** C-OVERALL+C-LIMIT — forecast errors matter; the third stage greatly raises computational burden.
- **Subsections (in order):** (unnumbered) RQ1 heading, RQ2 heading, RQ3 heading, bullet summary; 7.1 Future Work with five bold mini-headings.
- **Paragraph moves (in order):** C-PROBLEM+C-DONE, C-ANSWER+C-FIND-INV+C-FIND-ECON (+ literature support), C-ANSWER+C-FIND-OP, C-ANSWER+C-FIND-ECON, C-OVERALL (four bullets), C-OVERALL+C-LIMIT.
- **Paragraph length:** average ≈ 120 words; shortest ≈ 60; longest ≈ 200.
- **Chapter-type specifics (CONCL):** RQs answered one by one, in order, each RQ repeated verbatim as a bold heading; answers carry numbers (cost +2.1 %, VRES −10 %, flexible +40 %, VRES share 80 %, storage −16 %, transmission capacity < 1 % change, transmission use +10–20 %, deterministic cost −7.3 %). No C-GAP, no C-POINTER beyond the section that follows.
- **FUT (F-EXT parts present: what to add / why the current assumption limits / expected effect / complexity cost):**
  - Cost recovery: what yes; why yes (units that cut output are uncompensated); effect partly (would reflect higher intraday prices); complexity no.
  - Market design (incremental intraday balancing): what yes; why yes (full re-balance is unrealistic); effect vague ("could prove beneficial"); complexity no.
  - Demand response (combine with existing module): what yes; why partly (more flexibility need); effect yes (may mirror the storage reduction); complexity no.
  - Curtailment cap or cost: what yes; why yes (no mechanism, high curtailment); effect yes (better conditions for storage and transmission); complexity no.
  - Branching in the intraday stage: what yes (two extra ± scenarios); why yes (not done for lack of method and compute); effect no; complexity yes.
- **What makes this chapter strong:**
  - Each RQ is reprinted as a heading and answered directly underneath with the key percentages, so a grader can tick them off.
  - A final four-bullet list compresses the answers into claims that match the abstract's numbered findings.
  - Future-work items are each tied to a named model simplification from 4.5 (cost recovery, market design, curtailment), closing the loop with the shortcomings section.
- **Weaknesses:** answer to RQ3 uses a different cost comparison than 6.8 without comment; future-work items rarely state expected effect or cost; no explicit limitation paragraph in the conclusion.
- **Signal phrases:** "Below, the three research question"

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** the RQs are stated once (ch. 1), referenced at the start of ch. 2 and ch. 6, and reprinted as headings in ch. 7. The ch. 1 data on intraday volume is explicitly picked up again in 6.6 (with a back-reference) and the metric that makes this possible is defined in 4.6 with a caveat pointing back to ch. 1. The expectation written at the end of ch. 2 is checked in ch. 5 ("hypothesis") and ch. 6. Constraint numbers from ch. 4 are cited in the case definitions (ch. 5) and in the VSS failure explanation (6.8). Simplifications listed in 4.5 return as future-work items. Fixed terms throughout: market sequencing, forecasting errors, flexible / inflexible / intermittent generators, case 0/1/2.
- **How the RQs are answered in the conclusion:** one by one, in the original order, under verbatim RQ headings, each with numbers; then a four-bullet overall summary.
- **Anything a strong thesis does that the codes do not capture:**
  - A two-step results design: a small test case first (proof of concept, case-by-case mechanism isolation), then the full-scale case with the same result headings, so the reader learns how to read the results before the big run.
  - Model size (constraints and variables per case) is used as a result in itself to argue the computational cost of adding a stage.
  - A failed analysis (infeasible VSS) is reported in full: cause, tried remedies, rejected options, and a fallback argument — this turns a negative outcome into a finding about the importance of uncertainty.
  - A literature-derived hypothesis is stated at the end of the review and explicitly confronted in the results.
  - A draft journal paper is attached as an appendix and declared in the introduction.
