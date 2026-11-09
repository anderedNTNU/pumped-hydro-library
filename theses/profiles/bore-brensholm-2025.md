# bore-brensholm-2025 — Martin Bore & Sigurd Skogan Brensholm, 2025
- File: theses/texts/bore-brensholm-2025.txt (TIØ4500 project report, "Multi-market optimization of flexible hydropower", 16 Dec 2025)
- Type: monograph
- Topic: deterministic hourly, one-year LP of a single price-taking reservoir hydropower plant in NO2 selling in DA, ID, aFRR and FCR markets; operational and economic effects of multi-market participation, and an NPV break-even analysis of capacity upgrades.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: high
- Citation style: author-year
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 18,950 by raw `wc -w` for ch. 1–11 (lines 312–2785, including captions, tables, equations and page headers); running prose ≈ 17,000 (?). Ch. 1–10 only ≈ 18,200.
- Research questions stated explicitly: yes (3 RQs, as bullets in §1.1 "Purpose of the project"; the abstract also gives a one-sentence "research problem" set off as an indented statement)

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| – | Preface | PRE | 22 | 120 | – | 2 | 0 | 0 |
| – | Abstract | ABS | 44 | 340 | – | 4 (+1 indented problem statement) | 0 | 0 |
| 1 | Introduction | INTRO | 312 | 1,390 | 7 % | 12 | 2 | 0 |
| 2 | Power markets | BACK (+DATA in §2.6) | 478 | 3,430 | 18 % | 32 | 6 | 2 |
| 3 | Hydropower | BACK (+light THEORY: HPF and NPV equations) | 919 | 2,800 | 15 % | 30 | 2 | 0 |
| 4 | Related literature review | LIT | 1256 | 3,890 (incl. ≈ 290 in Table 3) | 21 % | 31 | 0 | 1 |
| 5 | Problem description | PROB | 1711 | 570 | 3 % | 5 | 0 | 0 |
| 6 | Mathematical model | MODEL | 1772 | 1,650 | 9 % | 16 (+ assumption table rows) | 2 | 4 |
| 7 | Presenting the input data | DATA | 2086 | 190 | 1 % | 1 | 3 | 2 |
| 8 | Validation | VALID | 2133 | 1,210 | 6 % | 9 | 4 | 1 |
| 9 | Computational study | RES (+A-INSTANCES, R-TECH; discussion embedded) | 2305 | 2,560 | 13 % | 22 | 9 | 3 |
| 10 | Concluding remarks | CONCL | 2633 | 520 | 3 % | 5 | 0 | 0 |
| 11 | Future Research | FUT | 2692 | 760 | 4 % | 10 | 0 | 0 |

Notes: no separate DISC chapter (discussion sits inside ch. 9, which "presents and discusses"). Table numbering skips 4 and 13 (?). Appendices: A capacity-price distributions (5 figures), B/C turbine and generator efficiency curves, D GitHub link. Data sources and treatment are described in §2.6, not in ch. 7.

## 2. Chapters

### Abstract [ABS]
- **Moves:** P1 AB-CONTEXT+AB-WHY (drivers of balancing need, hydropower suited to several markets, ageing plants and upgrades); P2 AB-PROBLEM (market analysis → lit review → gap → indented one-sentence research problem); P3 AB-METHOD+AB-CASE (deterministic revenue-maximising model, NO2 producer, upgrade question); P4 AB-RES-OP+AB-RES-ECON+AB-IMPL (less aggressive operation, higher revenues, upgrade could be justified, model could become a decision-support tool).
- No numbers at all in the abstract; results are qualitative.

### 1 Introduction [INTRO]
- **Purpose in one line:** move from a dramatic price event to the need for flexible hydropower in several markets, then state RQs and preview findings.
- **Opening paragraph does:** I-HOOK — a dated price spike in Norway in December 2024, given in NOK/kWh and scaled against the yearly mean (about twenty times).
- **Closing paragraph does:** I-OUTLINE — two paragraphs, one sentence or clause per chapter (chapter 7 is left out of the outline).
- **Subsections (in order):** (unnumbered opening, 8 paragraphs) → context to problem; 1.1 Purpose of the project → aim, RQs, findings preview; 1.2 Outline → roadmap.
- **Paragraph moves (in order, per subsection):**
  - (opening): I-HOOK, I-CONCEPT (DA/ID/reserve markets in sequence), I-CONCEPT+I-CONTEXT (merit order, marginal gas plant, water value as opportunity cost, energy crisis), I-CONTEXT (net-zero, VRES cost fall, EVs; Fig. 1–2), I-NATIONAL (90 % hydro, interconnectors expose Norway to continental prices), I-CONTEXT+I-PROBLEM (three flexibility mechanisms; hydro favoured; accurate capacity modelling needed), I-PROBLEM (producers must schedule for several markets at once), I-NATIONAL+I-AIM (real producer doubling capacity of three plants; topic declared relevant)
  - 1.1 Purpose: I-AIM+I-LIT+I-RQ (three goals of the project, lit-review finding that multi-market models are scarce, three bullet RQs), I-AIM+I-FINDINGS+I-LIMIT (main purpose restated; results are an optimistic upper estimate by construction; previews fewer reservoir drawdowns, smaller but more frequent production changes, drivers of which reserve products pay)
  - 1.2 Outline: I-OUTLINE, I-OUTLINE
- **Paragraph length:** average ≈ 110 words; shortest ≈ 60; longest ≈ 200 (?)
- **Figures and tables:** 2 figures (Fig. 2 has two panels), 0 tables; introduced before shown? yes (referenced in text first); interpreted after? only "as illustrated" — 0 of 2 get observation → interpretation → implication.
- **Chapter-type specifics (INTRO):** RQs explicit (3, bullets) · contribution not stated separately (merged into purpose) · scope only implicit (deterministic, single plant) · findings previewed: yes, qualitatively, with the optimism caveat · no reused-material declaration · I-HOOK sourced (news + NVE + SSB).
- **What makes this chapter strong:**
  - The hook is a single dated event with a scaled number ("x times the annual mean"), which makes volatility concrete before any theory.
  - Zooms deliberately: European drivers → Norway's hydro share and interconnectors → flexibility mechanisms → producer scheduling → one named producer's investment plan, so the final paragraph lands on the exact decision the RQs study.
  - The key economic concept (water value) is explained in plain words in the intro, then reused by back-reference in §3.2.1, §8.1 and §9.1.1.
  - RQs are immediately followed by a findings preview that includes the honest framing of the results as an upper bound.
- **Weaknesses:** the outline skips chapter 7; the lit-review gap is claimed in §1.1 before the review is presented; the third and second RQs are not phrased as parallel questions to the first.
- **Signal phrases:** "illustrating the significant price fluctuations"; "is therefore a highly relevant"

### 2 Power markets [BACK (+DATA)]
- **Purpose in one line:** explain the Norwegian market chain from DA to reserves, flag coming market changes, and justify which historical reserve prices feed the case study.
- **Opening paragraph does:** B-SCOPE — lists markets covered, points to an overview figure, excludes long-term and financial markets.
- **Closing paragraph does:** OTHER(exclusion of one market with a reason) — mFRR capacity prices dropped because long, uncertain activation makes reservoir energy margins hard to estimate (forward ref to model parameters).
- **Subsections (in order):** 2.1 Norwegian market and system → liberalisation and grid roles; 2.2 Day-Ahead → clearing and timeline; 2.3 Intraday → continuous trading; 2.4 Reserve markets → frequency logic and four product families; 2.4.1–2.4.4 FFR, FCR, aFRR, mFRR → one product each; 2.4.5 Summary → timeline figure + requirements table; 2.5 Future considerations → coming platform changes, 15-min resolution, flow-based coupling; 2.6 Demand for balancing services → price trend analysis and choice of input data (run-in headings "Analysing the price development", "Input data used for case study").
- **Paragraph moves (in order, per subsection):**
  - (opening): B-SCOPE
  - 2.1: B-FACT (liberalisation date and its meaning), B-DEF+B-BRIDGE (grid levels, regulator, TSO role; forward ref to §2.4)
  - 2.2: B-MECH (bids, deadlines, coupling algorithm), B-FACT (move to 15-min resolution and why)
  - 2.3: B-MECH
  - 2.4: B-MECH (under/over-frequency and how balance is restored), B-DEF+B-FIG (four reserve categories; activation figure)
  - 2.4.1: B-DEF+B-FACT
  - 2.4.2: B-DEF (symmetric vs disturbance product), B-MECH (two sub-markets, eligibility), B-MECH (early sub-market timeline), B-MECH+B-RELEVANCE (late sub-market; why the split improves predictability)
  - 2.4.3: B-MECH+B-FACT
  - 2.4.4: B-MECH (capacity vs activation market), B-FACT (bid size, activation time, deadlines)
  - 2.4.5: B-SUMMARY (Fig. 5 bidding timeline, Table 1 product requirements)
  - 2.5: B-SCOPE (changes treated briefly), B-FACT (aFRR platform), B-FACT+OTHER(not modelled → future work), B-FACT+B-RELEVANCE (15-min shift vs hourly data used here), B-MECH (flow-based coupling), B-FIG (price increase after FBMC with a causal explanation)
  - 2.6: B-RELEVANCE (profitability is what drives supply of balancing), B-MODELLING (historical prices as uncertain proxies), OTHER(choice of comparison years with reasons), A-PROCESS (percentile filtering), B-FIG+B-SUMMARY (Fig. 8 + Table 2: prices rose; no zone clearly best), A-SOURCE+A-LIMIT (2024 prices used; may not persist; scenarios out of scope), A-CASE (confidential NO2 plant, data items listed), A-SOURCE+A-PROCESS (where each price series comes from; aFRR and ID built from one day per month replicated), OTHER(exclusion of mFRR with reason)
- **Paragraph length:** average ≈ 100 words; shortest ≈ 45; longest ≈ 175
- **Figures and tables:** 6 figures, 2 tables; introduced before shown? mixed (Fig. 3–5 yes; Fig. 6–8 shown, then discussed); interpreted after? Fig. 3–5 descriptive only; Fig. 6 observation + cause; Fig. 7 and Fig. 8/Table 2 observation → interpretation → implication for data choice — 2 of 6 complete.
- **Numbers from other studies:** ≈ 22 sourced technical numbers in prose (frequencies, response times, minimum bids, deadlines, price-increment), plus Table 1; Table 2 is the authors' own analysis.
- **Own work mentioned:** ≈ 20 sentences, nearly all in §2.5 ("not modelled here") and §2.6 (data choices).
- **Chapter-type specifics (BACK):** B-MODELLING appears only in 2.6; B-BRIDGE used for forward refs to §2.4, §6, §8–9; summary device = timeline figure + requirements table; future market changes each tagged with whether the model includes them.
- **What makes this chapter strong:**
  - Every reserve product is described in the same order (purpose and trigger → technical requirements → bid timeline), so the reader can compare products, and the comparison is then collapsed into one timeline figure and one table.
  - Each coming market change ends with an explicit statement of whether it is in the model or deferred to future work.
  - The choice of historical price years is argued from system events (VRES growth, new interconnectors, energy crisis), and missing-data substitutions are disclosed in table footnotes.
  - One representative distribution plot is shown in the text and the rest go to an appendix, with one sentence saying they show the same trend.
  - The chapter ends by stating precisely which data enter the case study and which market is dropped, with the physical reason.
- **Weaknesses:** §2.6 mixes background with data sources and processing that belong in ch. 7; several one-paragraph subsections are pure lists of facts; the FBMC analysis is admitted to be non-exhaustive.
- **Signal phrases:** "is not considered in this project"; "Because of these factors"

### 3 Hydropower [BACK]
- **Purpose in one line:** give the physical chain from reservoir to generator and the economic notions (water value, planning horizons, market eligibility, reinvestment and NPV) that the model and the investment analysis need.
- **Opening paragraph does:** B-SCOPE — why optimisation is needed (temporal coupling, non-linearity, uncertainty) and that physics comes before economics.
- **Closing paragraph does:** B-MECH — explains the NPV symbols and the accept rule.
- **Subsections (in order):** 3.1 Physical/technical perspective → water courses and plant schematic; 3.1.1 reservoir; 3.1.2 inflow; 3.1.3 penstock; 3.1.4 generating unit; 3.1.5 production function (eq. 1); 3.2 Economic perspective → signpost; 3.2.1 Water value; 3.2.2 Planning horizons (run-in headings long/mid/short-term); 3.2.3 Market participation → hydro's eligibility for each reserve; 3.2.4 Investment analysis (run-in headings rearmament, expansions, cost drivers, NPV; eq. 2).
- **Paragraph moves (in order, per subsection):**
  - (opening): B-SCOPE
  - 3.1: B-FACT+B-FIG
  - 3.1.1: B-MECH+B-MODELLING · 3.1.2: B-MECH+B-MODELLING · 3.1.3: B-MECH+B-MODELLING · 3.1.4: B-MECH+B-MODELLING
  - 3.1.5: B-RELEVANCE+B-DEF (why the HPF matters for reserve capacity; eq. 1), B-MECH (each symbol; head depends on reservoir level), B-MODELLING (non-linearity → simplifications are common)
  - 3.2: B-SCOPE
  - 3.2.1: B-DEF+B-MECH (back-ref to ch. 1; seasonal filling pattern; water value as marginal value of stored water)
  - 3.2.2: B-DEF (three levels; price-taker assumption), B-FIG (Fig. 10), long-term: B-MECH, B-FACT+B-MODELLING, B-MODELLING+OTHER(critique: no revenues → no market upside), B-MODELLING (aggregation, time steps, disaggregation); mid-term: B-MODELLING, B-RELEVANCE (mid-term suits business cases and investment); short-term: B-MODELLING, B-MODELLING
  - 3.2.3: B-RELEVANCE+B-FACT (back-ref to ch. 2)
  - 3.2.4: B-FACT+B-DEF (plant age, reinvestment, two categories), B-DEF, B-DEF+B-CASE (named Norwegian expansion), B-FACT (cost range converted to EUR/MW), B-DEF ×2 (bullets: civil works, electro-mechanical), B-DEF+B-BRIDGE (NPV; forward ref to §9), B-MECH
- **Paragraph length:** average ≈ 90 words; shortest ≈ 55; longest ≈ 190 (?)
- **Figures and tables:** 2 figures, 0 tables, 2 equations; introduced before shown? yes; interpreted after? no (schematics) — 0 of 2.
- **Numbers from other studies:** ≈ 7 (water-course counts, hydro share, build decades, horizon length in years, investment cost range, exchange rate, converted range)
- **Own work mentioned:** 1 sentence (NPV will be applied in §9).
- **Chapter-type specifics (BACK):** B-MODELLING is systematic in 3.1 and 3.2.2; B-BRIDGE to §9 for the NPV; cost benchmark planted here is reused in §9.4.1.
- **What makes this chapter strong:**
  - Each physical-component subsection is one short paragraph that ends with a one-sentence "In modelling, …" line saying how the component becomes a balance, bound or parameter — the bridge from physics to model is built paragraph by paragraph.
  - The production function is introduced as the meeting point of the earlier components, its symbols are explained in prose, and the paragraph after it argues why non-linearity forces simplification, which pre-justifies the PQ-curve approximation in ch. 6.
  - The planning-horizon part treats long, mid and short term with the same questions (length, purpose, uncertainty, resolution, method), and the mid-term part ends by saying why this horizon fits investment analysis — the authors' own choice is motivated without naming it.
  - A literature cost benchmark is converted into the unit the results will use (EUR/MW) so that it can be compared directly with the break-even costs in ch. 9.
- **Weaknesses:** key definitions (water value, mid-term criteria) rest on personal communication; §3.2.3 is a single thin paragraph; the planning-horizon text overlaps with literature-review content.
- **Signal phrases:** "In modelling, the"; "To maintain tractability"

### 4 Related literature review [LIT]
- **Purpose in one line:** review four dimensions (stochasticity, hydraulic modelling, multi-market participation, solution methods) with the 5 C's and position the work in a comparison table.
- **Opening paragraph does:** L-SCOPE — names the four dimensions, back-refs the planning-horizon discussion in ch. 3, announces the 5 C's approach.
- **Closing paragraph does:** L-OWN+L-RECAP — states what the model takes from the hydraulic, stochastic and solution-method sections, and that stochastic methods are noted for later.
- **Subsections (in order):** 4.1 Searching strategy → databases, keywords, an AI search tool, four quality-check questions, backward snowballing; 4.2 Stochasticity → which uncertainties matter; 4.3 Hydraulic modelling → HPF techniques and trade-off; 4.4 Multimarket dynamics → which markets studies co-optimise and with what result; 4.5 Relevant solution methods (run-in headings SDP/SDDP, two-stage Benders, stochastic SLP, multi-objective) → method families and their scaling; 4.6 Our contribution → Table 3, gap, contribution, links back.
- **Paragraph moves (in order, per subsection):**
  - (opening): L-SCOPE
  - 4.1: L-SEARCH (+bullet list of four questions), L-SEARCH (rule for the questions, snowballing)
  - 4.2: L-RELEVANCE+L-STUDY (stochastic beats deterministic in out-of-sample test), L-GROUP (inflow as main uncertainty; temperature as driver), L-PAIR+L-CRITIQUE (studies with/without environmental variable; dimensionality limit), L-SYNTH
  - 4.3: L-RELEVANCE (back-ref §3.1.5; accuracy vs complexity), L-TAXONOMY+L-STUDY+L-CRITIQUE (piecewise-linear tables vs binary-curve MILP; MILP scales badly), L-PAIR (two head-correction approaches told in detail), L-SYNTH
  - 4.4: L-RELEVANCE+L-OWN, L-PAIR+L-CRITIQUE (two co-optimisation studies agree; fixed activation share → optimistic; counter-point on risk), L-STUDY (activation ignored → costs underestimated; consequences for a producer), L-PAIR+L-CAVEAT (opposite finding on ID value; different markets and zones so not comparable), L-STUDY+L-NOTCOVERED (broad market set but no added-value analysis, no reserve direction), L-STUDY+L-CRITIQUE (out-of-scope study with a profit % and its limiting assumptions), L-SYNTH+L-GAP+L-OWN (joint formulation missing; own omission of activation will underestimate costs)
  - 4.5: L-RELEVANCE+L-OWN; SDP/SDDP: L-GROUP+L-STUDY (SDDP forward/backward pass; weekly SDP subproblems), L-STUDY+L-PAIR (daily SDP; SDDP vs SDP scaling); Benders: L-GROUP+L-STUDY+L-CRITIQUE (scenario-fan problems; aggregated description), L-STUDY (weekly decomposition with budget variables), L-STUDY+L-SYNTH (short-term AC-flow case; Benders works across horizons); SSLP: L-STUDY+L-CRITIQUE (scenario-tree uncertainty decay; no decomposition); MOO: L-STUDY+L-OWN (beyond scope → future work); L-SYNTH (methods compared by horizon, stages, tractability; nested Benders as fix)
  - 4.6: L-TABLE, L-GAP+L-CONTRIB, L-CONTRIB+L-OWN (mid-term, hourly case), L-OWN+L-RECAP
- **Per LIT subsection:**
  | Subsection | Studies cited | Told in depth (≥ 2 sentences) | Paragraphs opening with author name | Critique phrased as | Ends with |
  |---|---|---|---|---|---|
  | 4.1 | 1 (method source) | 0 | 0 | – | method name + source |
  | 4.2 | ≈ 10 | 1–2 | 0 | "However, treating all prices…" → dimensionality | L-SYNTH (prices and inflow; limit number of variables) |
  | 4.3 | 4 (+1 personal comm.) | 4 | 0 | "The drawback of a MILP" | L-SYNTH (trade-off tailored to purpose) |
  | 4.4 | 8 | 6 | 0 | "A potential limitation with the latter"; "the study lacks" | L-GAP + own-work caveat |
  | 4.5 | ≈ 11 | 8 | 2–3 | "However, the SSLP does not…" | L-SYNTH (method comparison) |
  | 4.6 | (Table 3: 14 studies + own row; 5 columns: horizon, hydraulics, stochastic variables, markets, method) | – | 0 | "none incorporate the" | L-OWN+L-RECAP |
  Unique studies in the chapter ≈ 23.
- **Paragraph length:** average ≈ 110 words; shortest ≈ 40; longest ≈ 195
- **Figures and tables:** 0 figures, 1 table (Table 3, introduced first in §4.6).
- **Numbers from other studies:** ≈ 5 (one profit %, case lengths in days/weeks/years); the review is almost number-free.
- **Own work mentioned:** ≈ 20 sentences (≈ 5 in the search-strategy method, ≈ 5 spread across 4.4–4.5, ≈ 10 in 4.6).
- **Chapter-type specifics (LIT):** themed by modelling dimension, not by paper; the 5 C's are named as the method; contribution section = comparison table + gap paragraph + "what we take from each subsection" paragraph.
- **What makes this chapter strong:**
  - Almost no paragraph opens with an author name; paragraphs open with a connector or a claim ("Building on…", "In contrast to…", "Similar to…"), so the text reads as an argument with studies as evidence.
  - Critiques are always paired with their consequence for results (e.g. a fixed activation share → too optimistic; ignoring activation → costs underestimated), and sometimes balanced with a strength of the same model.
  - When two studies disagree, the paragraph explains the disagreement by differences in markets and bidding zones before drawing any conclusion (explicit comparability caveat).
  - Every subsection ends with a short synthesis paragraph, and the solution-method subsection ends with a cross-method comparison (scaling with scenarios, stage limits, a named remedy).
  - The contribution section links each earlier subsection to a concrete modelling choice, and admits which strands (stochasticity, solution methods) are noted but not used yet.
- **Weaknesses:** heading typo and some personal-communication sources; 4.2 and 4.3 do not connect to own work until 4.6; the comparison table does not mark which dimension carries the gap.
- **Signal phrases:** "Building on this,"; "A potential limitation with the latter"; "To the author's best knowledge"

### 5 Problem description [PROB]
- **Purpose in one line:** state the hourly, one-year multi-market allocation problem in plain words.
- **Opening paragraph does:** P-PURPOSE — what is described, with a pointer to the assumption table.
- **Closing paragraph does:** P-OBJECTIVE+P-OUTPUT — maximise revenue; a solution gives hourly schedule, reservoir path and market commitments.
- **Subsections (in order):** none.
- **Paragraph moves (in order):** P-PURPOSE; P-ACTOR+P-HORIZON+P-MARKETS (operator, mid-term hourly year, inputs: inflow and prices in five markets); P-UNCERT+P-DECISIONS+P-SCOPE (uncertainty acknowledged then assumed away; decision variables listed; market sequence ignored); P-CONSTRAINTS (enumerated First/Second/Third/Lastly: production bounds and efficiency, reservoir limits and water balance, reserve headroom up/down, activation margins, plant share of reserve market, ID volume share); P-OBJECTIVE+P-OUTPUT.
- **Paragraph length:** average ≈ 110 words; shortest ≈ 50; longest ≈ 230
- **Chapter-type specifics (PROB):** symbols: no · numbers: no · length ≈ 1.3 pages.
- **What makes this chapter strong:**
  - The uncertainty move is made in two short sentences: admit prices and inflows are uncertain, then state the simplifying assumption, so the deterministic choice is visible and owned.
  - Constraints are enumerated with ordinal words, and each one explains the physical or market reason (e.g. headroom between current output and limits bounds up/down reserves), so every later constraint has a plain-language twin.
  - It ends on what a solution looks like, which tells the reader how to read the results chapters.
- **Weaknesses:** points to a table located in the next chapter; one very long constraint paragraph.
- **Signal phrases:** "In reality,"; "Within this framework,"

### 6 Mathematical model [MODEL]
- **Purpose in one line:** formulate the deterministic LP with linearised PQ-curve, reserve headroom and ID volume limits.
- **Opening paragraph does:** D-INTRO — model class, perspective, objective, perfect foresight so results are an upper bound, PQ-curves used.
- **Closing paragraph does:** D-CONSTR (non-negativity); no summary.
- **Subsections (in order):** 6.1 Assumptions and simplifications (Table 5); unnumbered "PQ-curve modelling"; Sets / Parameters / Decision variables (Tables 6–8); Objective; Constraints.
- **Paragraph moves (in order, per subsection):**
  - (opening): D-INTRO
  - 6.1: D-ASSUMP (pointer to Table 5; table has assumption | consequence columns, 5 rows)
  - PQ-curve: D-PHYS (curve built from appendix efficiency data by interpolation), D-PHYS (Fig. 11: weakly convex low part, concave high part), D-LINEAR (avoid binaries for run time and future extensions; linear low part, piecewise inequalities for concave part, conservative; Fig. 12)
  - Notation: D-NOTATION ×3 (tables)
  - Objective: D-OBJ (one short paragraph; equation with labelled under-braces for capacity and energy revenue)
  - Constraints: D-CONSTR ×10 (production bounds; reservoir bounds with reserve energy margins; initial level; end level = initial; PQ-curve; reservoir balance; down-reserve headroom; up-reserve headroom; max reserve bid; ID volume limit; non-negativity)
- **Paragraph length:** average ≈ 70 words (constraint texts ≈ 25–45 words, 1–2 sentences); longest ≈ 120 (PQ paragraphs)
- **Figures and tables:** 2 figures, 4 tables; Fig. 11 interpreted (shape → modelling consequence).
- **Chapter-type specifics (MODEL):** citations in model chapter: 1 (personal communication inside the assumption table) · assumptions give consequences for all 5, direction of bias for 3 (perfect foresight → optimistic upper bound; no activation → lost income but small; head simplification → small deviation) · constraint order: production → reservoir bounds → initial → terminal → PQ → balance → reserve down → reserve up → reserve caps → ID caps → domains · typical explanation: bold run-in name + 1–2 sentences before the equation, unit in brackets after.
- **What makes this chapter strong:**
  - The opening paragraph tells the reader how to interpret every result (upper bound due to perfect foresight) before any equation.
  - The assumption table pairs each assumption with its consequence, including the direction of bias, so limitations are stated where they arise.
  - The linearisation is justified from the data: a figure shows where the curve is convex and concave, and the text says why binaries are avoided and that the chosen approximation is conservative.
  - Uniform constraint layout (bold name, one or two plain sentences, equation, unit) makes the model scannable.
- **Weaknesses:** parameter-table slips (minimum capacity described as maximum, odd inflow unit); no model summary; the reserve-margin parameters are introduced without saying how they are set (?).
- **Signal phrases:** "represent a demonstrative upper bound"; "To avoid the use of binary"

### 7 Presenting the input data [DATA]
- **Purpose in one line:** show the parameter values, inflow and price series used.
- **Opening paragraph does:** A-PURPOSE — back-ref to §2.6, lists data groups, says why the reader needs them (to read ch. 8–9).
- **Closing paragraph does:** none (chapter ends with figures).
- **Paragraph moves:** A-PURPOSE; then A-PARAM-TABLE (Table 9 plant bounds), A-FIG (inflow), A-PARAM-TABLE (Table 10 reserve prices and volume caps), A-FIG (price duration curves), A-FIG (ID volume caps) — none interpreted.
- **Figures and tables:** 3 figures, 2 tables; interpreted: 0 of 3.
- **Chapter-type specifics (DATA):** sources and processing are in §2.6, not here; no instance table here (it is in §9.1); no data limitations here (they are in §2.6 and §9.4.1).
- **What makes this chapter strong:** the one paragraph states the reader-oriented purpose of the data section; parameter values are kept out of the model chapter.
- **Weaknesses:** figures and tables are not discussed at all; data provenance is split from the data presentation.
- **Signal phrases:** —

### 8 Validation [VALID]
- **Purpose in one line:** show on a two-week case that the model's decisions follow its objective and constraints.
- **Opening paragraph does:** V-PURPOSE — validation checks behaviour and builds credibility for ch. 9.
- **Closing paragraph does:** V-VERDICT+OTHER(lesson carried forward) — model ready; net energy production treated as base case in ch. 9.
- **Subsections (in order):** (intro: purpose, setup, three-step plan); 8.1 Water value → dual vs perturbation; 8.2 Net production → production at minimum; 8.3 Prices vs volumes → when it produces and arbitrages; 8.4 Capacity market participation → how reserves are allocated; closing paragraph.
- **Paragraph moves (in order, per subsection):**
  - (intro): V-PURPOSE, V-SETUP+V-CHALLENGE (two January weeks for visual clarity; terminal constraint infeasible, relaxed to a fraction of start level, with stated effect), V-SETUP (three checks announced in order)
  - 8.1: V-CHECK (back-ref to ch. 1 definition; constant water value), V-CHECK+V-BENCH+V-VERDICT (re-solve with one extra MWh; difference split by market in Table 11 equals the dual)
  - 8.2: V-CHECK+V-VERDICT
  - 8.3: V-CHECK+V-VERDICT (production in highest DA hours; DA–ID arbitrage; ID cap binding)
  - 8.4: V-CHECK+V-VERDICT (full up-headroom to aFRR Up when price > 0; FCR-N first, then aFRR Down; caps respected), V-VERDICT
- **Paragraph length:** average ≈ 110 words; shortest ≈ 30; longest ≈ 180
- **Figures and tables:** 4 figures, 1 table; each figure is shown first, then read in the next paragraph; all 4 get observation → interpretation (model logic) → verdict.
- **What makes this chapter strong:**
  - The reduced case is justified (readability of hourly plots) and the one model change it forces is disclosed with its effect on the production plan.
  - The water-value check is a concrete numerical test: add one unit of water, re-solve, and decompose the objective change by market to show it matches the dual — a reusable template for validating marginal values.
  - Each check paragraph ends with a one-sentence verdict starting with "Overall", so the chapter reads as a checklist.
  - The final paragraph carries a specific lesson into the results chapter instead of only declaring the model valid.
- **Weaknesses:** checks are qualitative except the dual test; no comparison with real plant operation or external benchmark.
- **Signal phrases:** "Overall, the analysis demonstrates"; "To conclude the validation exercises"

### 9 Computational study [RES]
- **Purpose in one line:** compare market-inclusion instances operationally and economically, then test whether the added revenue justifies capacity upgrades.
- **Opening paragraph does:** R-AIMS — what the chapter contains and the investor perspective.
- **Closing paragraph does:** R-OBS+R-IMPL+R-CAVEAT — break-even costs vs benchmark range; feasible at the low end, sensitive to discount rate at the high end; single-year data caveat.
- **Subsections (in order):** 9.1 Instances (Table 12) → one market group added per instance; 9.1.1 Water values vs reservoir level → key relationship; 9.2 Technical execution; 9.3 Operational and economic performance (signpost); 9.3.1 Operational (duration and ramping curves); 9.3.2 Economic (water values, energy, capacity, revenues, per-MW table); 9.4 Capacity expansions (revenue vs added MW); 9.4.1 Investment analysis (NPV break-even table across discount rates).
- **Paragraph moves (in order, per subsection):**
  - (opening): R-AIMS
  - 9.1: A-INSTANCES (instances isolate each market group; goal implicit, not per instance)
  - 9.1.1: R-AIMS, R-KEYREL (stepwise water value explained by depletion events under perfect foresight; reader told to recall this later)
  - 9.2: R-TECH (language, modelling layer, solver, hardware; run time omitted with a reason)
  - 9.3: OTHER(signpost)
  - 9.3.1: R-OBS+R-INTERP (fewer full-output hours with reserves), R-OBS+R-INTERP (smaller but more frequent ramps; down-reserve case most stable), R-OBS+R-IMPL+R-LIT+R-CAVEAT (ramping wear; reserves may help; activation would change this)
  - 9.3.2: R-OBS+R-INTERP (down-reserve instance has highest water value: one unit earns energy and down-capacity at once), R-OBS+R-INTERP+R-IMPL (small reserve share → more depletions; downward reserves keep flexibility), R-OBS+R-INTERP (annual energy nearly identical), R-OBS+R-INTERP (aFRR Up dominates: price synergy and volume bias), R-OBS+R-INTERP+R-SUMMARY (priority order of products; market capacity decisive), R-OBS+R-SUMMARY (revenue stack), OTHER(sets up per-MW normalisation), R-OBS+R-INTERP (revenue per MW vs mean price)
  - 9.4: R-AIMS (strategic question; how upgrade is implemented in the model), R-OBS+R-INTERP+R-LIT (weakly concave revenue in added MW; fixed ID caps; diminishing returns)
  - 9.4.1: OTHER(NPV assumptions: lifetime, O&M share, timing, sourced), OTHER(method: solve for break-even cost per MW across discount rates) + R-SENS, R-OBS+R-IMPL+R-CAVEAT
- **Paragraph length:** average ≈ 100 words; shortest ≈ 25; longest ≈ 185
- **Figures and tables:** 9 figures, 3 tables; mostly shown first, then read; OBS → INTERP → IMPL complete for ≈ 3 (ramping Fig. 22, water values Fig. 23, break-even Table 15); OBS → INTERP only for ≈ 5; incremental-revenue Fig. 28 shown without interpretation.
- **Chapter-type specifics (RES):** order = instances → key relationship → technical → operational → economic → investment · R-SENS only on discount rate and upgrade size · R-STOCH: none (deterministic) · R-LIT: 2 light references (wear; diminishing marginal utility) · numbers in text are rare; most quantitative content sits in figures and two tables.
- **What makes this chapter strong:**
  - A short "key relationship" subsection before the results explains a pattern that recurs in later figures (stepwise water values from reservoir depletions), so later paragraphs can refer back instead of re-explaining.
  - Each figure paragraph explains the observation through the model's own mechanism (e.g. down-reserve water is paid twice; headroom creates a volume bias towards up-reserves) rather than just describing the curve.
  - Revenues are normalised per MW and set against mean input prices, which exposes the role of market share and energy decisions.
  - The investment question is reversed: instead of assuming a cost, they compute the maximum cost per MW at NPV = 0 for three discount rates and compare it with the benchmark range planted in ch. 3.
  - Caveats are attached to the specific result they affect (activation → ramping; one year of data → NPV).
- **Weaknesses:** implications for the producer are thin; few numbers quoted in text; no out-of-sample or stochastic test; instance goals not stated individually.
- **Signal phrases:** "Interpreted within the model context"; "it is reasonable that"

### 10 Concluding remarks [CONCL]
- **Purpose in one line:** restate problem and gap, then give findings by perspective in RQ order.
- **Opening paragraph does:** C-PROBLEM+C-GAP+C-DONE — what was examined, the gap, the deterministic mid-term model, and a purpose list that mirrors the three RQs.
- **Closing paragraph does:** C-OVERALL+C-POINTER — overall contribution, list of five future directions.
- **Paragraph moves (in order):** C-PROBLEM+C-GAP+C-DONE; C-FIND-OP (RQ 1, implicit); C-FIND-ECON (RQ 2, implicit); C-FIND-INV+C-LIMIT (RQ 3; conservative assumptions needed); C-OVERALL+C-POINTER.
- **Paragraph length:** average ≈ 100 words; shortest ≈ 70; longest ≈ 125
- **Chapter-type specifics (CONCL):** C-ANSWER: RQs answered in order, one paragraph each, opened with a perspective adverb, but not labelled as RQ answers · no numbers at all · one limitation sentence.
- **What makes this chapter strong:**
  - Finding paragraphs open with "Operationally,", "Economically,", "From the investment perspective", which maps one-to-one onto the three RQs and the results subsections.
  - Each finding is followed by its mechanism and a trade-off, not only the outcome.
- **Weaknesses:** no numbers (break-even costs, revenue gains) even though they exist; RQs not explicitly referenced; the added value of reserve markets (RQ 2) is not quantified.
- **Signal phrases:** "Operationally, the results indicate"; "From the investment perspective"

### 11 Future Research [FUT]
- **Purpose in one line:** propose model extensions and solution methods in order of priority.
- **Opening paragraph does:** OTHER(signpost: extensions and solution methods).
- **Closing paragraph does:** F-EXT+OTHER(industry relevance) — a named SDP framework as inspiration; relevance at a time of upgrades.
- **Subsections (in order):** "Possible model expansions" (run-in: Stochasticity; Cost and degradation; Reserve activation; Transition to 15-minute resolution) → "Possible solution methods".
- **Extensions (what to add · why current assumption limits · expected effect · complexity cost):**
  | Extension | Paragraphs | What | Why | Effect | Complexity |
  |---|---|---|---|---|---|
  | Stochastic prices, inflow, ID volumes; multi-stage bid sequence | 3 | yes | yes (perfect foresight optimistic, over-confident water use) | yes, detailed (arbitrage would shrink, water-value path changes, reservoir smoother) | no (?) |
  | Start-up/shut-down, O&M, taxes, degradation | 2 | yes | yes (revenues only) | vague ("more realistic") | yes (binaries for start-ups; others cheap but data-hungry) |
  | Reserve activation | 1 | yes (named simpler approach) | no (stated earlier in thesis) | no | partial ("computationally efficient") |
  | 15-minute resolution | 1 | yes | no | no | yes (horizon ×4; data availability) |
  | SDP decomposition | 2 | yes | yes (growing complexity) | partial ("new insights") | implicit |
- **What makes this chapter strong:** the first extension spells out how each current result would change under uncertainty, which doubles as an honest limitation of the results; complexity cost is weighed explicitly for cost terms (which need binaries, which do not).
- **Weaknesses:** later items are one paragraph without expected effect; no priority ordering argued.
- **Signal phrases:** "A natural first step would be"

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** recurring concepts are planted early and paid off by explicit back-references: water value (ch. 1 → §3.2.1 → §8.1 → §9.1.1 → §9.3.2); production function (§3.1.5 → §4.3 → PQ-curve in ch. 6); cost benchmark and NPV formula (§3.2.4 → §9.4.1); the exclusion of activation is flagged consistently (§2.5, §4.4, §4.6, ch. 5, Table 5, §9.3.1, ch. 11). Chapters often open by naming the section they build on ("Section X introduced/showed …").
- **How the RQs or objectives are answered in the conclusion:** in order, one paragraph per RQ, signalled by perspective (operational, economic, investment), qualitatively and without numbers; RQs are not quoted or numbered in the conclusion.
- **Anything a strong thesis does that the codes do not capture:**
  - The abstract isolates the research problem as a single indented sentence between the gap and the method.
  - Data provenance and processing are placed in the background chapter (§2.6) next to the price analysis that motivates them; the data chapter only displays values.
  - Run-in bold headings inside subsections (planning horizons, investment types, solution-method families, future-research items) give structure without deeper numbering.
  - Validation is a full chapter between model and results with a reduced instance and a numerical marginal-value test.
  - There is no discussion chapter; discussion of mechanisms is embedded in each results paragraph, and caveats are attached locally.
