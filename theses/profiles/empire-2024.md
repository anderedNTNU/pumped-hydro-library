# empire-2024 — Ulsaker, Winberg & Drillestad, 2024
- File: `theses/texts/integrating-technical-hydropower-planning-into-empire-a-node.txt` (title page reads "Integrating Tactical Hydropower Planning into EMPIRE: A Node Formulation Approach")
- Type: monograph (group thesis, continuation of the group's autumn project report)
- Topic: replaces EMPIRE's independent-season scenario formulation with a node (scenario-tree) formulation, so that a combined regulated-hydro + pumped-hydro reservoir is linked across seasons within a year while keeping some operational uncertainty; tests three cases against a Standard case.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: high (inter-seasonal hydro storage, empirical season-to-season inflow transition probabilities, pumped-hydro charging, initial/final reservoir levels, spillage). No reserve markets, no SDDP.
- Citation style: author-year in square brackets, e.g. [Ulsaker et al., 2023] (not numeric, despite the brief)
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 31 400 raw (lines 592–3822, includes tables, equation fragments, 93 captions and page headers); ≈ 28 000 prose (?)
- Research questions stated explicitly: no. Only an aim in the introduction (develop the node formulation further, add hydro constraints for storing water across seasons) and an "objective" in ch. 5. The conclusion answers the aim in its last paragraph.

Front matter (not main text): preface (1 para, thanks supervisors; states it develops the project report); abstract (≈ 330 words, 2 paras) with moves AB-CONTEXT (EU 2050 goals), AB-WHY (hydro flexibility, models must capture it), AB-PROBLEM (EMPIRE seasons modelled independently), AB-METHOD (node formulation, new storage with level/production/pumping/inflow/spillage), AB-RES-ECON (objective ≈ 5 % lower), AB-RES-OP (less OCGT, storage shifts to high-demand periods). Norwegian summary mirrors it. List of abbreviations (14 entries).

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction | INTRO | 592 | 815 | 2.6 % | 7 | 0 | 0 |
| 2 | Background | BACK | 666 | 3 450 | 11.0 % | 30 | 9 | 0 |
| 3 | Related Literature | LIT | 978 | 2 560 | 8.1 % | 18 | 0 | 1 (large comparison table) |
| 4 | EMPIRE Model | THEORY + FRAME (existing model and its stochastic structure) | 1208 | 2 215 | 7.0 % | 24 | 7 | 0 |
| 5 | Problem Description | PROB | 1426 | 360 | 1.1 % | 4 | 0 | 0 |
| 6 | Mathematical Formulation | MODEL | 1460 | 3 670 | 11.7 % | 30 | 1 | 0 (notation as lists) |
| 7 | Data Collection | DATA + VALID (7.5) | 1925 | 2 890 | 9.2 % | 19 | 6 | 1 |
| 8 | Scenario Generation | SCEN | 2221 | 1 985 | 6.3 % | 21 | 6 | 1 |
| 9 | Computational Study | RES + VALID (9.6) + DISC (9.7) | 2403 | 12 265 | 39.0 % | ≈ 123 | 38 | 28 |
| 10 | Concluding Remarks | CONCL + FUT | 3711 | 1 225 (634 + 589) | 3.9 % | 13 (7 + 6) | 0 | 0 |

Appendices (not counted): A original EMPIRE formulation, B project-report formulation, C full thesis formulation (three complete formulations side by side), D season-transition probabilities for 2–5 start nodes.

## 2. Chapters

### 1 Introduction [INTRO]
- **Purpose in one line:** motivate storage in a renewable-heavy system, name the EMPIRE shortcoming (no inter-seasonal link) and state what this thesis adds to the project report.
- **Opening paragraph does:** I-CONTEXT+I-HOOK — fossil dominance and climate harm, then the EU 2030 target (−55 % vs 1990) and 2050 neutrality, one source at the end.
- **Closing paragraph does:** I-OUTLINE — one sentence per chapter, chapters 2–10.
- **Subsections (in order):** none.
- **Paragraph moves (in order):** I-CONTEXT+I-HOOK, I-CONCEPT (why intermittent supply needs storage), I-SCOPE (thesis focuses on hydro reservoirs incl. pumped hydro), I-CONTEXT (role of power-system optimisation models; temporal aggregation needed), I-PROBLEM (EMPIRE lacks inter-seasonal connections, so hydro cannot store water for later seasons), I-REUSE+I-AIM+I-CONTRIB (builds on project report's node formulation; develops hydro constraints for tactical planning), I-OUTLINE.
- **Paragraph length:** average ≈ 110 words; shortest ≈ 45; longest ≈ 150
- **Figures and tables:** 0
- **Chapter-type specifics:** no RQs, no explicit gap paragraph (the lit gap is only stated in 3.2), no findings preview, no limitations. Funnel is short: global → storage → hydro → models → EMPIRE flaw → this thesis. Only 2 citations in the whole chapter.
- **What makes this chapter strong:**
  - Very fast funnel (7 paragraphs, under 2 pages): each paragraph narrows the topic by exactly one level, ending at the single model flaw the thesis fixes.
  - The problem paragraph names the concrete mechanism of the flaw (no transfer of water between seasons → lost flexibility → more fossil back-up) rather than a vague "limitation".
  - Project-report continuity is declared in its own paragraph, so the reader knows what is inherited and what is new.
- **Weaknesses:** no research questions or explicit contributions list; the opening hook is generic climate framing; no preview of results.
- **Signal phrases:** "Building upon this foundation"; "a significant drawback in its formulation"

### 2 Background [BACK]
- **Purpose in one line:** explain the European power system, its future challenges and flexibility options, storage technologies, and what power-system optimisation models are.
- **Opening paragraph does:** B-SCOPE + OTHER(reuse declaration) — lists the parts of the chapter in order and states which sections are restructured from the project report and which is new.
- **Closing paragraph does:** B-MODELLING — why models use representative hours instead of 8 760 (tractability, and detailed dispatch would give false precision). No explicit bridge to ch. 3.
- **Subsections (in order):** 2.1 European Power System → bidding zones, markets; 2.1.1 Future Trends → demand growth, VRES growth and price effects; 2.1.2 Solutions → grid expansion, climate-friendly flexibility, Norwegian hydro (three bold unnumbered sub-headings); 2.2 Energy Storage Technologies → overview; 2.2.1 Hydropower Storage → how a plant and PHES work, planning horizons; 2.2.2 Batteries → role and limits; 2.3 Power System Optimization Models → what they are; 2.3.1 Objectives; 2.3.2 Temporal and Spatial Representation.
- **Paragraph moves (in order, per subsection):**
  - intro: B-SCOPE+OTHER(reuse declaration)
  - 2.1: B-MECH+B-FIG (bidding zones, transmission), B-MECH+B-FIG (day-ahead, intraday, reserves)
  - 2.1.1: B-SCOPE, B-FACT (demand +60 % 2023–2030), B-FACT+B-MECH+B-CASE (44 % renewables, negative prices in Norway 2023)
  - 2.1.2: B-SCOPE (two solutions); *grid*: B-MECH (three numbered advantages), B-FACT+B-CASE (€584 bn grid need; Norwegian cable debate); *flexibility*: B-DEF (flexibility), B-MECH+B-FIG (gas/coal cover peak load), B-MECH (drawbacks of fossil and nuclear), B-RELEVANCE+B-FACT (hydro is regulable; IEA), B-FACT (IEA and EU Parliament on pumped storage); *Norway*: B-MECH ("giant battery"), B-FACT+B-FIG (150 TWh, 96 % hydro, 75 % regulated), B-FACT+B-RELEVANCE (110 TWh of storage for Europe)
  - 2.2: OTHER(back-reference to the previous section's main finding)+B-SCOPE, B-MECH+B-FIG (storage overview)
  - 2.2.1: B-MECH+B-CASE+B-RELEVANCE (reservoir limits; 2023 flood and 2020–21 shortage as reasons for tactical management), B-MODELLING (water-value method; PHES), B-MECH+B-FIG (pump ≈ 85 % efficiency; pump when cheap), B-DEF (operational/tactical/strategic horizons)
  - 2.2.2: B-FACT, B-MECH+B-CASE (batteries short-term; Fortum hydro–battery pilot), B-MECH (peak shaving)
  - 2.3: B-DEF
  - 2.3.1: B-MODELLING, B-MODELLING, B-MODELLING (sector coupling raises complexity)
  - 2.3.2: B-MODELLING
- **Paragraph length:** average ≈ 105 words; shortest ≈ 30; longest ≈ 200
- **Figures and tables:** 9 figures (all borrowed, with source in caption); introduced before shown: yes; interpreted after: mostly one sentence describing what the figure shows; full observation → interpretation → implication: ≈ 2 of 9 (Fig. 2.5 supply–demand gaps → need for flexibility; Fig. 2.6 Norway self-sufficient → battery role)
- **Numbers from other studies:** ≈ 13 (60 %, 44 %, €584 bn, 150 TWh, 96 %, 75 %, 110 TWh, 85 %, horizon lengths 1–2 weeks / 1–2 years / 3–5 years, 5–10 years, 50 Hz) (?)
- **Own work mentioned:** ≈ 3 sentences (chapter intro and one "subsequent sections of this report")
- **Chapter-type specifics:** heavy use of grey literature and newspapers (IEA, McKinsey, Nettavisen, Europower). Norway is used as the running example. The PHES operating logic (pump when price is low and higher prices are expected) is given in plain words, no equations.
- **What makes this chapter strong:**
  - Each challenge is followed by a concrete, dated Norwegian event (2023 negative prices, 2023 flood, 2020–21 shortages, cable debate), which makes abstract system issues tangible.
  - Section 2.2 opens by restating the key finding of 2.1 (grid expansion is expensive, so flexibility matters) and uses it to justify the next topic: a one-sentence logical bridge between sections.
  - Planning horizons (short/medium/long, with lengths) are defined once in background, so the term "tactical" used throughout the thesis has a fixed meaning.
  - The flexibility argument is built by elimination: fossil is flexible but emits, nuclear is clean but inflexible, hence hydro.
- **Weaknesses:** sections end without bridges to the model; 2.3 on optimisation models overlaps with ch. 3 and ch. 4; several sources are newspapers.
- **Signal phrases:** "A more viable alternative is"; "effectively functioning as a giant battery"

### 3 Related Literature [LIT]
- **Purpose in one line:** compare 12 power-system models along structure, uncertainty and hydropower treatment to show EMPIRE (this version) is the only one that is both stochastic and connected across the year.
- **Opening paragraph does:** L-SCOPE — states the dimensions examined (horizon, spatial granularity, scope, scenario generation, operational detail).
- **Closing paragraph does:** L-GAP+L-CONTRIB — names the two-part challenge (managing stochasticity, capturing hydro flexibility without making the model too complex) as what this extension faces.
- **Subsections (in order):** intro → scope and order; 3.1 Comparison of models → introduces Table 3.1; 3.1.1 Model Structure → horizon/granularity trade-off, load-duration vs clustering; 3.1.2 Uncertainty → deterministic vs stochastic; 3.1.3 Hydropower Management → hydro as generator vs storage, pumped/regulated separated vs combined; 3.2 This Thesis Contribution → gap.
- **Paragraph moves (in order, per subsection):**
  - intro: L-SCOPE, L-SCOPE+L-RELEVANCE (why structure and uncertainty come before hydro)
  - 3.1: L-TABLE (incl. an ideal "optimal standard" row), L-TABLE+L-OWN (takeaway: own version is the only stochastic and year-connected one)
  - 3.1.1: L-TAXONOMY (how to read the table columns), L-PAIR (EMMA vs LIMES: short horizon/detail vs long horizon/trends), L-TAXONOMY+L-PAIR+L-CRITIQUE (load-duration curve vs clustering; Dyn-ELMOD vs EMPIRE/LIMES; clustering by season breaks links between seasons), L-RECAP
  - 3.1.2: L-RELEVANCE (why uncertainty matters; short quote from one study), L-TAXONOMY+L-GROUP+L-STUDY (original EMPIRE; group of 8 deterministic models; EMMA and LIMES ways to mimic uncertainty; E2M2/TIMES both modes), L-RECAP+L-SYNTH (most are deterministic, probably for tractability)
  - 3.1.3: L-TAXONOMY (generator vs storage), L-STUDY+L-CRITIQUE (Dyn-ELMOD: year-connected storage but perfect inflow foresight), L-STUDY+L-CRITIQUE (Kotzur et al.: inter/intra-period superposition; extra complexity), L-STUDY+L-CRITIQUE+L-SYNTH (LIMES treats hydro as generator → underestimates flexibility; detail vs hydro trade-off), L-TAXONOMY+L-PAIR+L-CRITIQUE (pumped and regulated hydro separate vs combined; combined allows pumping into reservoirs that have no pump)
  - 3.2: L-GAP+L-PAIR+L-RELEVANCE (closest model E2M2 differs in what is stochastic), L-GAP+L-CONTRIB
- **Paragraph length:** average ≈ 120 words; shortest ≈ 45; longest ≈ 280
- **Figures and tables:** 1 table (13 model rows + optimal standard, 8 columns, sources as footnotes); introduced before shown: yes; interpreted after: yes, with a one-sentence takeaway paragraph
- **Numbers from other studies:** ≈ 2 in prose (every 25th hour; six representative days); the table carries ≈ 50 numeric cells (horizons, step lengths, hours, node counts)
- **Own work mentioned:** ≈ 8 sentences (mostly in 3.1 and 3.2)
- **Chapter-type specifics (per subsection):**
  - 3.1.1: studies cited 3 · in depth 2 (Dyn-ELMOD; EMMA/LIMES pair) · paragraphs opening with author name 0 · critique phrased as a capability lost (season-based clustering makes links between seasons harder) · ends with L-RECAP.
  - 3.1.2: studies cited 11 · in depth 2 (EMMA, LIMES; plus original EMPIRE) · author-name openings 0 · critique phrased as trade-off (uncertainty given up for resolution) · ends with "To recap" synthesis.
  - 3.1.3: studies cited 3 · in depth 2–3 (Dyn-ELMOD, Kotzur et al., LIMES) · 1 paragraph opens with a model name, 0 with an author · critique phrased as flaw + real-world consequence (planners must consider overflow and shortage) · ends on a critique of the combined-storage approach that the thesis itself adopts (and later admits in 9.7).
  - 3.2: studies cited 2 · in depth 0 · ends with the challenge statement.
  - The review is organised by models, not by papers: each "study" is a named model with one source.
- **What makes this chapter strong:**
  - The comparison table has an "optimal standard" row (an ideal, computationally infeasible model), so every model's simplification is visible as a deviation from the ideal; the thesis's own version is a row in the same table.
  - Each subsection ends with a recap paragraph ("In summary", "To recap"), so the three dimensions build up step by step to the gap in 3.2.
  - Critique always names the real-world consequence (e.g. perfect inflow foresight means the model never faces overflow or shortage, unlike real planners).
  - Order is justified in the opening paragraph: structure and uncertainty first, because the hydro issue cannot be understood without them.
- **Weaknesses:** few studies in depth and no numbers compared across studies; the table cites model documentation rather than modelling papers; the gap is hedged (the authors say few or no models do this).
- **Signal phrases:** "However, a major flaw of"; "The main downside to this method"; "To recap"

### 4 EMPIRE Model [THEORY + FRAME]
- **Purpose in one line:** describe the existing EMPIRE model (scope, objective, temporal aggregation, scenario sampling, multi-horizon structure) and the node formulation inherited from the project report.
- **Opening paragraph does:** OTHER(reuse map) — which sections are inspired by which project-report chapters and which are new.
- **Closing paragraph does:** M-OVERVIEW — the new model structure (Fig. 4.7) and that branching position and number of start nodes (2–5) are user choices.
- **Subsections (in order):** 4.1 Introduction to EMPIRE → nodes, objective, technologies, assumptions; 4.2 Temporal Aggregation → 5-year steps, regular and peak seasons; 4.3 Scenario Sampling Methods → random, k-means, moment matching; 4.4 Model Structure → multi-horizon vs multi-stage; 4.4.1 Scenario Formulation → independent seasons; 4.4.2 Node Formulation → tree with branches, terminology.
- **Paragraph moves (in order, per subsection):**
  - intro: OTHER(reuse map), M-OVERVIEW (origin: Skar's PhD, Open EMPIRE)
  - 4.1: M-OVERVIEW+M-WORKFLOW (31 countries, Norway in 5 zones, Fig. 4.1), T-CONCEPT (multi-horizon stochastic programming: long-term decisions informed by short-term uncertainty), M-OVERVIEW (objective, costs, constraint families, outputs), M-OVERVIEW+OTHER(weakness of existing model: regulated hydro and pumped storage do not share a reservoir), D-ASSUMP (bullet list of 6 model assumptions, no consequences)
  - 4.2: M-STEP (5-year investment blocks), M-STEP (4 regular + 2 peak seasons, how peaks are picked), M-STEP (168 h / 24 h, 3–10 scenarios)
  - 4.3: M-STEP (random sampling), M-STEP (k-means with Wasserstein distance), M-STEP (moment matching)
  - 4.4: T-CONCEPT+T-COMPARE (multi-horizon vs multi-stage, Figs 4.2–4.3), T-COMPARE (size grows four times by step 3), T-CONCEPT (no strategic uncertainty, Fig. 4.4), T-RELEVANCE (why EMPIRE uses the smallest structure)
  - 4.4.1: T-CONCEPT+M-WORKFLOW (Fig. 4.5), T-CONCEPT (hours linked within a season only), T-COMPARE+T-RELEVANCE (strength: scenarios; weakness: no inter-seasonal link for hydro)
  - 4.4.2: T-CONCEPT+T-COMPARE (node vs scenario formulation: no non-anticipativity constraints), T-CONCEPT+M-WORKFLOW (stages, Fig. 4.6), OTHER(terminology change: "node" now means tree node, countries become "country nodes"; "start node" defined), M-OVERVIEW (Fig. 4.7)
- **Paragraph length:** average ≈ 85 words; shortest ≈ 35; longest ≈ 170
- **Figures and tables:** 7 figures (4 borrowed, 3 own diagrams); introduced before shown: yes; interpreted after: yes for the structure diagrams (what the size difference means for tractability)
- **Own work mentioned:** ≈ 6 sentences (which version is used; North Sea nodes used; what is new)
- **Chapter-type specifics:** no equations; the stochastic structure is taught with diagrams only. Ends with what the user can configure, which later becomes the run-time table in 9.2.1.
- **What makes this chapter strong:**
  - Explains the stochastic structure purely with paired diagrams plus one quantified comparison (multi-stage tree four times larger by step 3), which gives the reader the reason behind the chosen structure without algebra.
  - The weakness the thesis fixes is stated at the end of the subsection describing the current formulation (strength first, then the limitation for hydro), so the motivation is placed exactly where the reader understands it.
  - A dedicated terminology paragraph resolves a clash of terms ("node") before it can confuse the model chapter.
- **Weaknesses:** the assumption list has no consequences; overlaps with 2.3 and 3.1.
- **Signal phrases:** "falls short in addressing tactical considerations"

### 5 Problem Description [PROB]
- **Purpose in one line:** state the thesis objective and the new challenges the node formulation creates, each pointed to the chapter that handles it.
- **Opening paragraph does:** P-PURPOSE — enhance EMPIRE with inter-seasonal hydro while keeping operational uncertainty; links to the project report.
- **Closing paragraph does:** P-SCOPE — one-sentence summary of scope (improve tactical hydro decisions).
- **Subsections (in order):** none.
- **Paragraph moves (in order):** P-PURPOSE, P-SYSTEM+OTHER(two shortcomings of the existing hydro representation: PHES separate, production bound to history)+OTHER(forward pointers to ch. 6 and 7), P-HORIZON+P-DECISIONS (an operational scenario now spans a year; season linking and initial/final reservoir levels must be decided; pointers to ch. 8 and 6), P-SCOPE.
- **Paragraph length:** average ≈ 85 words; shortest ≈ 55; longest ≈ 120
- **Figures and tables:** 0
- **Chapter-type specifics:** symbols: no · numbers: no · length ≈ 1 page. No decision maker, no explicit uncertainty statement, no objective function in words, no markets, no description of what a solution contains. It reads as a statement of aims and challenges rather than a problem description.
- **What makes this chapter strong:**
  - Each challenge is tied to the chapter that resolves it, so the problem description works as a map of the method chapters.
  - Very short and free of data and notation, as the placement rule requires.
- **Weaknesses:** lacks actor, decisions, objective and uncertainty in plain words; partly repeats ch. 4.4.2.
- **Signal phrases:** "introduces new challenges"

### 6 Mathematical Formulation [MODEL]
- **Purpose in one line:** present the relevant parts of the original (scenario) formulation, then the new node formulation with a combined hydro reservoir, spillage and inflow.
- **Opening paragraph does:** D-INTRO+OTHER(map to appendices) — only modified or result-relevant parts of the original are shown; full versions in Appendices A–C.
- **Closing paragraph does:** OTHER(note that other constraints were only re-indexed and are not shown).
- **Subsections (in order):** intro → scope, naming (scenario vs node formulation), reuse; 6.1 Original Model → sets, parameters, variables, costs, objective, 11 constraint groups; 6.2 Node Formulation → what is new; 6.2.1 Explanation of New Modeling Approach → three modelling choices explained in words before any equation; 6.2.2 Mathematical Node Formulation → new sets, parameters, variables, costs, objective, 4 storage-balance constraints.
- **Paragraph moves (in order, per subsection):**
  - intro: D-INTRO+OTHER(appendix map), OTHER(naming of the two formulations), OTHER(reuse declaration)
  - 6.1: D-NOTATION (lists of sets, parameters, variables, costs), D-OBJ (term-by-term; discounting, period scaling, scenario probability, season scaling), D-INTRO (constraint order: hydro first, then indirect ones), D-CONSTR ×11 (seasonal regulated-hydro limit from history; annual hydro limit; PHES hourly balance; initial and final level 50 %; availability factor; storage cap; charge/discharge caps; one-line link to investment; capacity accumulation; investment bounds; flow balance)
  - 6.2: OTHER(what is inherited vs new)
  - 6.2.1: D-INTRO (why explain before formulas), D-ASSUMP (scenario-dependent initial/final levels; Fig. 6.1 shows 30–70 % range), D-EXT (new "Hydro Reservoir" storage type combining regulated and pumped discharge, kept as two variables because of investment logic), D-ASSUMP (weekly inflow spread evenly over hours; reason: avoid artificial spikes and overflow)
  - 6.2.2: D-NOTATION (new sets and their meaning), D-ASSUMP (why pumped discharge gets the same cost as regulated production; why spillage cost), D-OBJ (difference from original only), D-SUMMARY (overview of the four new constraints before they are shown), D-CONSTR ×4 (within-season balance; between-season balance via parent–child map; initial level; final level), OTHER(other constraints only re-indexed)
- **Paragraph length:** average ≈ 75 words; shortest ≈ 20; longest ≈ 190
- **Figures and tables:** 1 figure (NVE reservoir curves to justify varying initial levels); notation given as lists, not tables
- **Chapter-type specifics:** citations in the model chapter: ≈ 7 (Skar et al. once, project report five times, NVE in a caption). Assumptions: reasons are given ("otherwise the model would always prefer pumped production"), but direction of bias is not stated here; it is tested later (Cases 2 and 3). Typical constraint explanation: 2–5 sentences, ≈ 50–90 words, naming each variable and saying what goes wrong without the constraint. Constraint order (6.1): hydro production limits → storage balance → initial/final level → availability → storage capacity → charge/discharge capacity → capacity accumulation → investment bounds → flow balance. Order (6.2.2): within-season → between-season → initial → final. Equations are numbered 6.1–6.22.
- **What makes this chapter strong:**
  - A prose subsection (6.2.1) explains each new modelling choice and its reason before any notation appears; the formulas then only confirm what the reader already understands.
  - The constraint block opens with an overview paragraph that names each new constraint's role (within season, between seasons, start, end) before showing them.
  - The objective of the new model is described only by its difference from the original, which avoids repeating a long expression's explanation.
  - Constraint explanations often say what the model would do without the constraint (e.g. empty the store in one step and restart full).
- **Weaknesses:** original-model constraints take more space than the new ones; notation lists are hard to scan; some explanations restate the equation rather than its purpose.
- **Signal phrases:** "Before the mathematical formulation of"; "This forces the energy level"

### 7 Data Collection [DATA + VALID]
- **Purpose in one line:** derive inflow, reservoir limits, initial/final levels and spillage cost for all countries when the data exist only partly, then check the estimates.
- **Opening paragraph does:** A-PURPOSE — new constraints need new data; bullet list of the four parameters.
- **Closing paragraph does:** V-CHECK+V-VERDICT — estimated non-Norwegian capacity (51 %) vs Norway (49 %) matches the known ≈ 50 % share.
- **Subsections (in order):** intro → parameters and order; 7.1 Hydro Inflow → energy-balance back-calculation, reference countries; 7.2 Max and Min Storage → scaling from observed 93 % peak; 7.3 Initial and Final Levels → taken from the sampled week; 7.4 Cost of Spillage → set from lowest Norwegian price; 7.5 Data Validation → inflow vs NVE, capacities vs known share.
- **Paragraph moves (in order, per subsection):**
  - intro: A-PURPOSE (+ list), OTHER(roadmap)
  - 7.1: A-PROCESS (ideal data unavailable → energy-balance estimate), A-PROCESS (terms explained; loss ignored, pointer to 7.5), A-SOURCE (ENTSO-E datasets), A-FIG+A-SOURCE (map with three data-availability colours), A-PROCESS (reference-country ratio, two formulas), A-PROCESS+A-SOURCE (neighbour chosen by precipitation → Table 7.1), A-LIMIT (simplification admitted; affected countries are only 7 % of production, Fig. 7.2)
  - 7.2: A-PURPOSE (why limits change), A-SOURCE+A-FIG (NVE, HRV/LRV, observed max 93 %), A-PROCESS+A-LIMIT (divide by 0.93; ratios for unknown countries; Fig. 7.4), A-PROCESS (scale to a week), A-PROCESS (allow 0 % = LRV; three physical reasons for a minimum level)
  - 7.3: A-PROCESS
  - 7.4: A-PROCESS+A-SOURCE+A-LIMIT (6.1 EUR/MWh from the lowest observed price; called a pessimistic estimate)
  - 7.5: V-SETUP (energy loss ignored; NVE usable inflow as benchmark), V-BENCH+V-VERDICT (close match; why negative inflow can appear; NVE data used for Norway), V-CHECK+V-VERDICT (51 % vs 49 %)
- **Paragraph length:** average ≈ 130 words; shortest ≈ 45; longest ≈ 230
- **Figures and tables:** 6 figures, 1 table, 4 equations; introduced before shown: yes; data figures interpreted: yes for 7.2, 7.3, 7.5, 7.6 (with a conclusion on data quality); 7.1 and 7.4 are descriptive
- **Chapter-type specifics:** no instance table (instances come in ch. 9). Every simplification is followed by a size-of-impact argument. Validation is placed inside the data chapter, not in a separate chapter.
- **What makes this chapter strong:**
  - Error from a crude estimate is bounded by its weight: the countries estimated by proxy produce only 7 % of hydro output, so their error barely affects results.
  - Aggregate cross-check of estimated data against a known total (estimated rest-of-Europe capacity vs Norway's known share of about half) gives confidence without country-level data.
  - Data-availability map with three colour classes makes clear which estimation route applies to which country.
  - Forward pointer from the simplification (loss ignored) to the section that checks it (7.5), then the check explains residual deviations physically (evaporation, environmental release, flood spill).
- **Weaknesses:** the spillage cost is a single observed price with no sensitivity run; validation is only for Norway.
- **Signal phrases:** "It is needed to acknowledge"; "minimal impact on the model results"

### 8 Scenario Generation [SCEN]
- **Purpose in one line:** derive season-to-season inflow transition probabilities from 65 years of Norwegian data and use them to build and weight the scenario tree, choose the branching point and place peak seasons.
- **Opening paragraph does:** A-PURPOSE — roadmap of the chapter steps.
- **Closing paragraph does:** OTHER(summary + honest note that the new routine is not compared with the old one, out of scope).
- **Subsections (in order):** 8.1 Process from the Project Report → old tree, equal 11 % probabilities criticised; 8.2 Exploring Seasonal Correlations → wet/medium/dry classes, transition frequencies, de-trending; 8.3 Enhanced Process → clustered start nodes, weighted branches, conditional selection; 8.4 Branching → branch where transitions are most uneven; 8.5 Peak seasons → placed at year end; 8.6 Summary.
- **Paragraph moves (in order, per subsection):**
  - intro: A-PURPOSE
  - 8.1: A-SCEN+OTHER(critique of the inherited method)+A-PURPOSE
  - 8.2: A-SOURCE (weekly Norway 1959–2023; why Norway only), A-PROCESS (seasons of 13 weeks; equal-size classes; count transitions; others in App. D), A-PROCESS (linear de-trending for climate-driven inflow rise, Fig. 8.2), A-FIG (winter→spring nearly random after wet winter; snowmelt), A-FIG (spring→summer persistence 50 %/57 % vs 9 %/19 %; soil-moisture explanation), A-FIG (summer→fall weaker persistence), A-SCEN (conclusion: links strong enough to model)
  - 8.3: A-SCEN (3 clusters → 3 start nodes at 33 %), A-SCEN (with branching: one node per cluster per branch, weighted, e.g. 11.9 %), A-SCEN (without branching: next node drawn with conditional probabilities 50/41/9 %), A-SCEN (peaks random: only 5 samples), OTHER(one-sentence lead-in to Fig. 8.6)
  - 8.4: A-SCEN (cannot branch everywhere), A-SCEN+M-RATIONALE (branch at the most uncertain transition first)
  - 8.5: A-SCEN (peaks have no natural place), A-SCEN+A-PARAM-TABLE (peaks fall in Jan/Feb, Table 8.1), A-SCEN (end of year lets the reservoir be filled before them), A-SCEN (decision)
  - 8.6: OTHER(summary)+A-LIMIT
- **Paragraph length:** average ≈ 85 words; shortest ≈ 10; longest ≈ 230
- **Figures and tables:** 6 figures, 1 table; introduced before shown: yes; interpreted after: the three transition figures get observation → physical interpretation (snowmelt, soil moisture), and the chapter draws the implication (include links; branch at spring→summer); ≈ 3 of 6 complete
- **Chapter-type specifics:** this is effectively a hand-built Markov chain over seasons (three inflow states, empirical transition matrices) used inside a scenario tree.
- **What makes this chapter strong:**
  - Transition probabilities are estimated from data and then used for two separate design decisions: scenario weights and where to place the single branch (at the transition whose outcomes differ most).
  - Each probability pattern gets a physical explanation (snowmelt, dry soil absorbing rain), which makes the statistics credible to a non-hydrologist.
  - Data are de-trended before counting transitions, with the reason (climate-driven rise in inflow) and a before/after figure.
  - The inherited method is critiqued with one concrete number (all scenarios at 11 %) before the new method is introduced.
- **Weaknesses:** probabilities from Norway only are applied to all of Europe; the new routine is never tested against the old one.
- **Signal phrases:** "certain hydrological conditions tend to persist"; "grounded in both the likelihood"

### 9 Computational Study [RES + VALID + DISC]
- **Purpose in one line:** describe the Standard case, then isolate three modelling choices (no inter-seasonal link; fixed 50 % start/end; inflow pattern) as cases, compare with an external forecast and list shortcomings.
- **Opening paragraph does:** R-AIMS — cases change one alteration at a time; all use the same scenario data and tree; explains why the old formulation is not used as a comparison.
- **Closing paragraph does:** X-LIMIT — the model ignores political debate and local resistance, so it may recommend technically efficient but infeasible options.
- **Subsections (in order):** 9.1 Hardware and Software; 9.2 Standard case (9.2.1 tree choice, 9.2.2 generation mix, 9.2.3 investments, 9.2.4 transmission, 9.2.5 operational costs, 9.2.6 reservoir balance, 9.2.7 spillage, 9.2.8 pumped charging, 9.2.9 regulated production); 9.3 Case 1 No inter-seasonal connections (objective, generation investments, storage investments, transmission, operational costs, curtailment, reservoir balance, spillage, hydro utilisation, summary); 9.4 Case 2 Initial and final level (objective, investments, operational variables, summary); 9.5 Case 3 Variable inflow (objective, investments, curtailment, storage level, spillage, pumped charging, summary); 9.6 Comparison of the Results (vs ECN 2050 forecast); 9.7 Further Discussion and Model Shortcomings (six headed weaknesses).
- **Paragraph moves (in order, per subsection; figure-by-figure Europe/Norway pairs coded in groups):**
  - intro: R-AIMS, OTHER(roadmap)
  - 9.1: R-TECH+R-CAVEAT (shared cluster may distort run times)
  - 9.2 intro: R-AIMS (Standard case is the baseline; focus on Norway), R-CAVEAT (seasonal scaling distorts absolute numbers; relative differences hold)
  - 9.2.1: R-TECH (run-time table; 24 h rule → 3 start nodes, 1 branch, 9 scenarios), OTHER(back-reference: branch at spring→summer from ch. 8), OTHER(setup: 720 h per year, 2020–2060)
  - 9.2.2–9.2.5 (8 paras): R-OBS+R-INTERP for Europe then Norway in each; one R-LIT (block quote from an EEA/ACER report supporting the transmission trend)
  - 9.2.6–9.2.9 (8 paras): R-OBS+R-INTERP+R-CAVEAT (end-of-year rise caused by final-level constraint and peak placement); R-KEYREL (spillage as a flexibility indicator); R-OBS+R-IMPL (Norwegian discharge capacity too small for reservoirs); R-OBS+R-LIT+R-CAVEAT (Norway 25 % of hydro output vs 43 % in reality; pointer to 10.2)
  - 9.3 (45 paras): R-AIMS; then per metric the same pattern: R-KEYREL (why the metric shows flexibility + expected direction) → R-OBS (figure, then total table) → R-INTERP (mechanism) → R-IMPL (what it says about flexibility). Notable: R-OBS+R-INTERP (objective ≈ 200 bn EUR higher without links; expected since linking is a relaxation); R-KEYREL with two opposing hypotheses for transmission, resolved differently for Europe and Norway; R-OBS (spillage ≈ 8×, curtailment ≈ 50 % / ≈ 4× higher); R-INTERP that rules out a rival explanation (investment cap of 10 % too small to explain production gap); R-SUMMARY ×3
  - 9.4 (17 paras): R-AIMS+R-KEYREL (why test fixed 50 %; 30–70 % range; Norway omitted to avoid repetition), R-OBS ×3 (objective and investments nearly equal), R-KEYREL (cumulative storage as a gain/loss indicator), R-OBS+R-INTERP+R-CAVEAT (2.7 % net gain; single run only), R-OBS (individual scenarios differ), R-KEYREL+R-OBS (expected more spillage, confirmed), R-INTERP (spillage cost is 0.56 % of the objective gap, so it cannot explain it), R-KEYREL, R-OBS+R-INTERP ×2 (charging), R-SUMMARY+OTHER(verdict: keep varying levels)
  - 9.5 (20 paras): R-AIMS+R-SENS (three inflow shapes), R-SENS (Figs 9.29–9.31 explained; random-walk inflow formula, cited premise), R-CAVEAT (formula not validated), R-OBS (objective and investments nearly equal), R-KEYREL+R-OBS+R-INTERP (curtailment), OTHER(apparent contradiction examined period by period, judged coincidence), R-OBS+R-INTERP (storage), R-OBS (spillage patterns), R-INTERP (Standard optimistic, first-half pessimistic, random most realistic), R-SENS (spillage ×2 and ×3), R-OBS+R-INTERP (pumping more valuable with irregular inflow), R-SUMMARY+OTHER(verdict: even inflow sufficient for investment purpose)
  - 9.6 (4 paras): V-BENCH+R-LIT (why compare with an independent forecast), V-BENCH+R-CAVEAT (initial non-renewable share ≈ 20 % looks too low), V-BENCH+R-INTERP (wind ≈ 55 % vs ≈ 35 %, nuclear ≈ 10 % in forecast; hydro flexibility may displace nuclear, may be optimistic), V-VERDICT (same trends → sufficiently accurate)
  - 9.7 (13 paras): X-METHOD (intro), X-METHOD (less uncertainty than original; run-time tables), X-ASSUMP with bias direction (perfect information between seasons without branching → optimistic), X-ASSUMP (pumping allowed in every reservoir; mitigation by capacity limits), X-METHOD (alternative: separate balances; not done for lack of data), X-ASSUMP with bias direction (varying start/end → more spillage and charging than realistic), X-LIMIT (approximated data cannot be checked), X-LIMIT+X-GENERAL (Norway-based probabilities may not fit other countries), X-ASSUMP (no inflow gain from storage investment; small because of 10 % cap; climate trend also ignored), X-ASSUMP (central planner), X-IMPL (what is optimal for Europe may hurt one country; cable example back-referenced to ch. 2), X-ASSUMP (national profit motives), X-LIMIT (political resistance)
- **Paragraph length:** average ≈ 80 words; shortest ≈ 10 (one-sentence figure lead-ins); longest ≈ 250
- **Figures and tables:** 38 figures, 28 tables; introduced before shown: yes (almost always "Figure X illustrates …" before the figure); full OBS → INTERP → IMPL: ≈ 14 of 38 (?); ≈ 10 figures (mostly Norway counterparts and inflow illustrations) get only a one-sentence "same trend" treatment. Tables are small two-row totals (Standard vs Case n) that turn each figure into one headline number.
- **Chapter-type specifics:** order of result subsections: technical (hardware, run times, tree choice) → Standard case system results (generation mix, investments, transmission, costs) → hydro operations (reservoir, spillage, pumping, production) → per case: objective → investments → operational costs → hydro operational variables → summary with verdict → external benchmark → shortcomings. No in-sample/out-of-sample test, no value of the stochastic solution (R-STOCH absent); uncertainty effect is explicitly not tested. Discussion is inside the results chapter (9.7) with bold sub-headings.
- **What makes this chapter strong:**
  - One-change-at-a-time case design with identical scenario data, stated up front, so every difference can be attributed to the one modelling choice.
  - Each metric subsection starts by explaining why that metric indicates flexibility and what direction is expected, then reports whether the result confirms it; surprises are flagged and examined (e.g. Norway's transmission going the "wrong" way, the random-inflow curtailment anomaly).
  - Rival explanations are ruled out with a number: spillage cost is 0.56 % of the objective gap; the 10 % investment cap is too small to explain the production difference.
  - Each case ends with a summary and an explicit verdict on whether the modelling choice is kept, so the cases double as justification of the model design.
  - Shortcomings are listed under named headings, each with a direction of bias (optimistic/pessimistic), any mitigation, and why the obvious alternative was not done.
- **Weaknesses:** very long (39 % of main text) and repetitive Europe/Norway pairs; absolute numbers declared unreliable because of seasonal scaling; many claims rest on a single run; the effect of uncertainty, the core feature, is never tested.
- **Signal phrases:** "This outcome aligns with expectations"; "contradicts the argument presented in"; "introduces an overly optimistic bias"

### 10 Concluding Remarks [CONCL + FUT]
- **Purpose in one line:** restate aim and motivation, summarise what was implemented and what testing showed, admit what was not tested, and propose four extensions.
- **Opening paragraph does:** C-PROBLEM+C-DONE — what was modified, why hydro matters, the aim.
- **Closing paragraph does (10.1):** C-LIMIT+C-OVERALL — uncertainty representation weakened; effects on wind/solar not studied; the primary objective is nevertheless achieved.
- **Subsections (in order):** 10.1 Conclusion; 10.2 Future Work (Peak Seasons, Stability Testing, Scenario Generation, Parameter Validation).
- **Paragraph moves (in order, per subsection):**
  - 10.1: C-PROBLEM+C-DONE, C-DONE+C-GAP (branching added; all year-connected models in ch. 3 are deterministic), C-FIND-OP (links let hydro shift production to high-demand periods), C-DONE+C-LIMIT (storage balance and scenario generation implemented but not tested directly), C-FIND-OP (start/end levels and inflow shape tested and judged sufficient), C-FIND-INV (renewable shift and growing transmission), C-LIMIT+C-OVERALL
  - 10.2: OTHER(intro), F-EXT (peak seasons: problem paragraph + two solutions paragraph), F-EXT (stability testing), F-EXT (scenario generation on net load), F-EXT (parameter validation)
- **Paragraph length:** average ≈ 90 words; shortest ≈ 25; longest ≈ 160
- **Figures and tables:** 0
- **Chapter-type specifics:** C-ANSWER: no RQs; the aim is answered once, in the final paragraph. No numbers at all in the conclusion (the 5 % objective reduction appears only in the abstract). F-EXT parts: Peak seasons — what yes · why the current assumption limits yes · expected effect partly · complexity no. Stability testing — what yes · why yes · effect implicit · complexity yes (run time). Scenario generation — what yes · why yes (unintended correlations) · effect no · complexity no. Parameter validation — what yes · why yes (three result anomalies named) · effect "more realistic" · complexity no.
- **What makes this chapter strong:**
  - Separates what was implemented and tested from what was implemented but not tested, which is honest and easy to verify.
  - Ties the conclusion back to the literature finding (all year-connected models are deterministic) to restate the contribution.
  - Future-work items are motivated by concrete anomalies found in the results (Norwegian discharge too constrained, nuclear phased out, initial mix off), with back-references to the sections.
- **Weaknesses:** no quantitative findings in the conclusion; some untested changes are described as "strongly believed" improvements; future work rarely states expected effect or cost.
- **Signal phrases:** "Despite these limitations"; "is achieved"

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** reuse declarations at the start of ch. 2, 4 and 6 say what comes from the project report; frequent back-references by section number ("as explained in Section 4.4.2", "as argued in Section 6.2.1"); forward pointers from problem description to ch. 6–8 and from data simplifications to the validation section; fixed terms ("inter-seasonal connections", "Standard case", "start node", "country node") used throughout; the 3.1.3 critique of combined storage (pumping into reservoirs without pumps) reappears as a stated shortcoming in 9.7; the cable-debate example from ch. 2 returns in 9.7.
- **How the RQs or objectives are answered in the conclusion:** no RQs. The aim is restated in paragraph 1 and declared achieved in the last paragraph; findings are given qualitatively, in roughly the order of the cases (Case 1 → Cases 2/3 → benchmark), without numbers.
- **Anything a strong thesis does that the codes do not capture:**
  - The "optimal standard" row in the literature table, used as a fixed yardstick for every model including their own.
  - Results cases are designed as tests of modelling choices: each case ends with a decision to keep or change a design element, so the results chapter also validates the model chapter.
  - Rival explanations are quantified and ruled out (0.56 % share, 10 % cap) instead of just asserting the main cause.
  - Appendices hold three full formulations (original, project report, thesis), which documents the model's evolution and keeps the model chapter short.
  - Season-to-season inflow transition matrices (wet/medium/dry, from 65 years, de-trended) are a direct, simple precedent for Markov-chain state construction, and the "branch at the most uneven transition" rule is a reusable design heuristic.
  - Honest scope flags ("not tested", "outside the scope") are used repeatedly; they protect claims but also show the core uncertainty feature was never evaluated.
