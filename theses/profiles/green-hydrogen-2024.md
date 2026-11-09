# green-hydrogen-2024 — Erlend Hordvei and Sebastian Hummelen, 2024
- File: `theses/texts/the-impact-of-green-hydrogen-and-seasonal-storage.txt`
- Type: paper-based (two articles, ch. 3 and ch. 5, framed by a thesis introduction (ch. 1), a problem description (ch. 2), a bridging "reflections" chapter (ch. 4) and concluding remarks (ch. 6))
- Topic: European multi-carrier capacity expansion (EMPIRE, multi-horizon stochastic LP) with (1) the EU green-hydrogen production rules and (2) seasonal hydrogen storage under tactical (inter-seasonal) uncertainty via multi-stage operational problems inside each investment period.
- Relevance to a pumped-hydro / SDDP / multi-market thesis: low-medium. Useful pieces: the three-level uncertainty vocabulary (operational / tactical / strategic, §5.2.1), the "seasonally linked storage gives perfect foresight unless you branch at season changes" argument (§5.2.2, §5.3.2), and a cited pumped-hydro paper with stochastic intrastage subproblems (Abgottspon and Andersson 2014). No SDDP, no reserve markets, no plant-level configuration.
- Citation style: author-year
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 18,400 (prose estimate; pdftotext word count is ≈ 20,300 including equation/figure residue; article appendices ≈ 3,700 words excluded)
- Research questions stated explicitly: thesis level objectives only (two numbered objectives in the abstract and §1.3, no RQs); inside the articles yes: 2 RQs in §3.1 (RQ2 split into lettered sub-items A/S/T) and 3 RQs in §5.1.

Note on text quality: both articles are typeset in two columns, so pdftotext interleaves left and right columns, and equations are garbled. Paragraph boundaries in ch. 3 and ch. 5 were reconstructed by following sentence continuity across columns; counts there are ±1–2 per subsection (?).

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction | INTRO | 322 | 1,280 | 7 % | 11 | 1 | 0 |
| 2 | Problem description | PROB + FRAME | 453 | 890 | 5 % | 11 | 0 | 0 |
| 3 | Article 1: from policy to practice, cost of green hydrogen | (paper) ABS · §3.1 INTRO · §3.2 BACK+LIT · §3.3 MODEL · §3.4 DATA (+ case-specific MODEL constraints) · §3.5 RES (+ §3.5.3 DISC limitations) · §3.6 CONCL | 557 | 7,200 | 39 % | ≈ 87 | 8 (+1 in app.) | 3 |
| 3-app | Appendix A (full formulation), B (renewable grid estimates) | APP | 1472 | (1,900, excl.) | – | – | 1 | 0 |
| 4 | Reflections on the first paper | DISC + FUT (+ bridge to ch. 5, with DATA-reduction decisions) | 1773 | 2,220 | 12 % | 26 | 0 | 0 |
| 5 | Article 2: hydrogen demand variations under tactical uncertainty with seasonal storage | (paper) ABS · §5.1 INTRO · §5.2 LIT · §5.3 MODEL + SOLVE · §5.4 DATA + SCEN · §5.5 RES (+ §5.5.5 DISC limitations) · §5.6 CONCL + FUT | 1995 | 5,900 | 32 % | ≈ 71 | 5 (+4 in app., plus 2 structure figs and 1 data fig in §5.3–5.4) | 2 (+3 in app.) |
| 5-app | Appendices A–F (why Spain, storage investments, price distribution, H2 for power, spatial aggregation, regional maps) | APP | 2838 | (1,800, excl.) | – | – | 5 | 3 |
| 6 | Concluding remarks (+ 6.1 Future research) | CONCL + FUT | 3134 | 945 | 5 % | 8 | 0 | 0 |

Figure count for ch. 5 main text: 5.1–5.9 = 9 (2 model-structure, 1 rolling-horizon, 1 demand-profile, 5 results).

## 2. Chapters

### 1 Introduction [INTRO]
- **Purpose in one line:** Sets up why hydrogen matters for European decarbonisation, how energy-system models handle it, and what gap the two papers fill.
- **Opening paragraph does:** I-HOOK: sourced share of European CO2 from energy, transport and industry (2021), then states that the last two sectors are the hard part.
- **Closing paragraph does:** I-OUTLINE: one paragraph walking through ch. 2–6, naming what each paper chapter does and that ch. 4 reflects between them.
- **Subsections (in order):**
  - 1.1 A European hydrogen future → policy and industry context, hydrogen colours, the EU definition.
  - 1.2 Energy system modelling → one paragraph on two-stage capacity expansion and multi-energy models.
  - 1.3 Objective of the thesis → gap plus aim (no RQs).
  - 1.4 Structure of the thesis → outline.
- **Paragraph moves (in order, per subsection):**
  - 1.1: I-HOOK, I-CONTEXT (hydrogen hype cycles over decades), I-HOOK+I-CONTEXT (dated pilot auction with budget and volume), I-CONTEXT (today's hydrogen use, mostly on-site), I-CONTEXT (supply chain must change; pipeline backbone initiative), I-CONCEPT (why hard-to-abate sectors need hydrogen, concrete examples with a temperature figure), I-CONCEPT+I-PROBLEM (grey/blue/green with Figure 1.1, EU delegated act; the definition is flagged as the thing studied later)
  - 1.2: I-LIT (two-stage models explained in plain words, then multi-energy models, two example studies)
  - 1.3: I-LIT+I-PROBLEM (literature mostly keeps blue hydrogen, little aligned with EU strategy), I-AIM (quantify cost of the new definition; seasonal storage as second theme)
  - 1.4: I-OUTLINE
- **Paragraph length:** average ≈ 115 words; shortest ≈ 55; longest ≈ 200 (§1.2).
- **Figures and tables:** 1 (schematic of hydrogen production routes); introduced in text before it appears; no interpretation needed.
- **Numbers from other studies:** (intro, counted for reference) ≈ 9 sourced numbers (emission share, auction budget and tonnes, EU target, current consumption, on-site share, process temperature, 2050 demand share).
- **Own work mentioned:** 3 sentences (in 1.3 and the forward pointer in 1.1).
- **Chapter-type specifics (INTRO):** no explicit RQs at thesis level; aim stated in 1.3 in the first person plural; no contribution list, scope, findings preview or limitation; no reused-material declaration here (it is in the preface: both papers submitted to journals, contribution statements on each article cover page).
- **What makes this chapter strong:**
  - The context moves from global to European to concrete policy event (a dated auction with a euro figure), so the reader gets a "why now" before any modelling.
  - The key concept (hydrogen colours) gets one figure and one paragraph, and the paragraph ends by saying that this definition is what the thesis later models: concept and problem are introduced in the same move.
  - Short, labelled subsections let an examiner find the aim (1.3) in seconds.
- **Weaknesses:**
  - §1.2 (modelling) is a single paragraph; the method context that the papers depend on is thin at thesis level.
  - No thesis-level RQs; the reader must wait for each article to see them.
  - The gap in §1.3 rests on "our literature review" without citations in that paragraph.
- **Signal phrases (≤ 3, ≤ 6 words each):** "Our literature review discovered that"; "explored later in this thesis"

### 2 Problem description [PROB + FRAME]
- **Purpose in one line:** States the overall problem (support European energy investment decisions with a cost-minimising model) and splits it into one policy problem and one technical modelling problem, each mapped to a paper chapter.
- **Opening paragraph does:** OTHER(chapter scope in two sentences: overview of scope and methods, situates the model).
- **Closing paragraph does:** OTHER(one-sentence implementation statement: the seasonal-storage method is built into EMPIRE).
- **Subsections (in order):**
  - (intro, 4 paragraphs) → general problem, why energy-system models, their limitations, roadmap.
  - 2.1 Energy system model → why EMPIRE is the base model.
  - 2.2 Implementing European green hydrogen requirements → policy problem, approach bullets, intended users.
  - 2.3 Enhancing multi-horizon modeling with seasonal energy storage → technical problem, approach bullets.
- **Paragraph moves (in order, per subsection):**
  - intro: OTHER(chapter scope), P-PURPOSE+P-ACTOR (investment decisions shaped by costs, policies, technology; cost-minimising system models as decision support), P-UNCERT+P-PURPOSE (models limited by computation and unknown futures; hydrogen makes it worse; two areas of improvement), OTHER(roadmap)
  - 2.1: P-SYSTEM+M-RATIONALE (base model and four reasons: multi-horizon stochastic, multi-carrier, open source, widely cited)
  - 2.2: P-PURPOSE (EU rule exists; current models lack it; ch. 3 answers it), M-OVERVIEW (bulleted approach: policy constraints, comparative cases), P-OUTPUT+P-ACTOR (insights for policymakers and industry)
  - 2.3: P-PURPOSE+P-UNCERT (why seasonal storage matters; two modelling requirements: link periods and represent tactical uncertainty instead of full foresight; ch. 5 answers it), M-OVERVIEW (bulleted approach: multi-stage linking, cases with/without storage, demand-profile variations), OTHER(implementation sentence)
- **Paragraph length:** average ≈ 75 words; shortest ≈ 25; longest ≈ 125.
- **Figures and tables:** 0.
- **Chapter-type specifics (PROB):** no symbols; essentially no numbers (only the 2048 horizon year); ≈ 3 pages. It is not a classical problem description (no decision maker, decisions, constraints or objective spelled out); it is a problem framing plus approach overview, because the formal problem sits in each article.
- **What makes this chapter strong:**
  - Parallel structure: both problem sections have the same three beats (why it matters and why current models fall short → "we approach this problem by" + bullets → who gains / where it is implemented). Easy to reuse when a thesis has two contributions.
  - Each problem section names the chapter that solves it, so the chapter doubles as a reading guide to the papers.
  - The uncertainty argument is phrased as the specific modelling assumption it removes (operating storage with full foresight of demand and renewable availability), not as a general "uncertainty is important".
- **Weaknesses:**
  - No explicit actor, decision list or objective; a reader who skips the articles does not get the model's problem in words.
  - §2.1 justifies the base model with credibility arguments (open source, widely cited) rather than problem fit.
- **Signal phrases:** "We approach this problem by"; "one policy-driven aspect"

### 3 Article 1: From policy to practice — the cost of Europe's green hydrogen ambitions [paper: ABS / INTRO / BACK+LIT / MODEL / DATA / RES / CONCL]
- **Purpose in one line:** Quantifies the extra system cost and investment shifts from forcing all electrolysis to meet the EU green-hydrogen rules (additionality, spatial and temporal correlation, 90 % renewable-grid exemption), and the effect of each rule.
- **Opening paragraph does:** (abstract) AB-CONTEXT+AB-PROBLEM+AB-METHOD+AB-RES-ECON+AB-RES-OP; (§3.1 first paragraph) I-CONTEXT+I-CONCEPT+I-HOOK+I-PROBLEM: explains the three rules in one sentence each, gives the auction budget and bid count, then states the cost risk.
- **Closing paragraph does:** C-LIMIT+C-POINTER: representative weeks per season mean storage cannot move energy between seasons, flagged as future research (this sets up ch. 4 and ch. 5).
- **Subsections (in order):**
  - Abstract (1 paragraph).
  - 3.1 Introduction → definition, gap, objective, base model and why, 2 RQs, outline.
  - 3.2 Literature review → 3.2.1 European definition of green hydrogen (policy history and rules: background content), 3.2.2 Green hydrogen definition in European energy system modeling (studies, Table 3.1, gap).
  - 3.3 Methodology → 3.3.1 model structure in words + energy-flow figure; 3.3.2 new sets, constraints (eq. 3.1–3.4) and pipeline repurposing (eq. 3.5–3.8); full model in Appendix A.
  - 3.4 Case studies and data → 3.4.1 six cases and the constraint changes that define them (eq. 3.9–3.12, Tables 3.2–3.3); 3.4.2 data sources and assumptions.
  - 3.5 Results and discussion → 3.5.1 cost of green hydrogen (Base vs AST90, then generators / electrolyzers / transmission); 3.5.2 breakdown by requirement (four "one rule removed" cases); 3.5.3 limitations.
  - 3.6 Conclusion and policy implications → what was done, RQ1 answer with numbers, RQ2 answer as a labelled list per rule, limitation pointer.
- **Paragraph moves (in order, per subsection):**
  - Abstract: AB-CONTEXT+AB-PROBLEM+AB-METHOD+AB-RES-ECON+AB-RES-OP
  - 3.1: I-CONTEXT+I-CONCEPT+I-HOOK+I-PROBLEM, I-LIT (models exist; inconsistencies; no quantitative study), I-AIM+I-PROBLEM, I-CONTRIB (extend EMPIRE; model history in one sentence), OTHER(base-model suitability: linear so high spatial resolution, stochastic so robust for weather-driven supply), I-RQ (2 RQs; RQ2 lists the three rules as A/S/T), I-OUTLINE
  - 3.2 intro: L-SCOPE
  - 3.2.1: B-FACT+B-DEF (directive history, RFNBO), B-FACT+B-RELEVANCE (delegated acts, legal certainty), B-RELEVANCE (more demand must be truly renewable), B-DEF+OTHER(scope: grid-connected only) (numbered list of the three rules), B-DEF (90 % exemption and its cap), L-GROUP+B-RELEVANCE (industry reaction; one study and one association say costs rise)
  - 3.2.2: L-GROUP+L-TABLE+L-STUDY+L-NOTCOVERED (one long paragraph walking through four models, each one or two sentences on how electrolysis is labelled and what is missing), L-STUDY+L-CRITIQUE (the one study that does model the EU rule; strength, then narrow scope: two years, one country), L-GAP+L-SYNTH (shortcomings listed; need for a European, uncertainty-aware study)
  - 3.3 intro: D-INTRO (roadmap)
  - 3.3.1: D-INTRO (graph of nodes and arcs, carriers), D-INTRO+A-SCEN (two time scales, two-stage stochastic, sampled operational scenarios, which parameters are stochastic), D-INTRO (objective and constraint families in words), D-INTRO+OTHER(figure explained as a numbered list: sources, carriers, sinks)
  - 3.3.2: D-INTRO (two-part contribution; pointer to Appendix A), D-NOTATION (two new sets), D-CONSTR (additionality, eq. 3.1), D-CONSTR (spatial/temporal, eq. 3.2), D-CONSTR (eq. 3.3), D-CONSTR (90 % exemption, eq. 3.4), D-NOTATION+D-ASSUMP (pipeline arcs; no NG investment, no depreciation), D-OBJ (objective extension for repurposing, eq. 3.5), D-CONSTR (eq. 3.6), D-CONSTR (eq. 3.7), D-CONSTR (eq. 3.8)
  - 3.4 intro: A-PURPOSE
  - 3.4.1: A-INSTANCES+D-ASSUMP (six cases; electrolysis is the only route), D-CONSTR (fixed hydrogen output, eq. 3.9), D-CONSTR+A-SOURCE (quantities from prior model run, Table 3.2), A-INSTANCES (RQ1 → Base vs AST90; the name spells the active rules), A-INSTANCES (RQ2 → four cases, each removing one rule; Table 3.3), D-CONSTR (ST90), D-CONSTR (AT90), D-CONSTR (AS90: hourly → annual matching), D-CONSTR (AST: empty exemption set)
  - 3.4.2: A-SOURCE (discount rate, costs), A-CASE (node structure), A-SOURCE (initial capacities), A-CASE+D-ASSUMP (3-year periods chosen to fit the 36-month additionality window), A-SOURCE (which sources count as renewable), A-PROCESS (exemption set precomputed to keep the model linear; Appendix B), A-SOURCE+D-ASSUMP (repurposing cost and flow factors), A-SOURCE (demands, load-shed penalty), A-SOURCE (industry demand), A-SOURCE (electrolysis and reformer rates), A-SOURCE (CO2 cap), A-SOURCE (CCS network), OTHER(open code and data statement)
  - 3.5 intro: R-AIMS
  - 3.5.1: R-OBS+R-INTERP (total difference in € and %, front-loaded), R-OBS+R-INTERP (where the change comes from), R-OBS+R-INTERP+R-LIT (net generation cost = extra capex minus fuel savings; consistent with a cost-structure source), R-OBS+R-INTERP (electrolyzer capex), R-INTERP (why pipelines and transmission rise), OTHER(signpost to the three component sub-headings), R-OBS+R-INTERP+R-IMPL ("Changes in generators", Fig 3.3a), R-OBS+R-INTERP (Fig 3.3b by country), R-OBS+R-INTERP ("Changes in electrolyzers", capacity factors), R-INTERP (spatial inflexibility), R-OBS+R-INTERP (production concentration, Fig 3.4), R-OBS+R-INTERP ("Energy transmission upgrades", Fig 3.5a), R-OBS+R-INTERP+R-CAVEAT (Fig 3.5b; what the 2045 map hides about 2027–2030)
  - 3.5.2: R-OBS (Fig 3.6, ST90), R-OBS+R-INTERP (AT90, AS90, AST costs), R-OBS+R-INTERP (Fig 3.7–3.8, Norway and Spain), R-OBS+R-INTERP+R-IMPL (additionality is costliest; fossil fills in), R-OBS+R-INTERP (AT90), R-OBS+R-INTERP (AS90: solar gains from annual matching), R-OBS+R-INTERP+R-IMPL (AST: Norway's role rests on the exemption)
  - 3.5.3: R-CAVEAT (four limitations; direction of bias given for one: no electrolyzer bounds → too cheap)
  - 3.6: C-PROBLEM+C-DONE, C-ANSWER+C-FIND-ECON+C-FIND-OP (RQ1: total cost, where it falls, fossil reduction per year), OTHER(list lead-in), C-ANSWER (additionality), C-ANSWER (spatial), C-ANSWER (temporal), C-ANSWER (exemption), C-LIMIT+C-POINTER
- **Paragraph length:** average ≈ 85 words; shortest ≈ 15 (list lead-in); longest ≈ 260 (the walk-through paragraph in §3.2.2).
- **Figures and tables:** 8 figures in main text (1 model, 7 results) + 3 tables (literature comparison, fixed quantities, case–criteria matrix). Introduced before shown: each figure is named in the first sentence of the paragraph that discusses it; physical order mixed because of two-column floats. OBS→INTERP→IMPL complete for ≈ 2 of 7 results figures (3.3 and the 3.7/3.8 pair); the rest stop at interpretation.
- **Numbers from other studies:** lit review text ≈ 0 numbers from studies (rule thresholds like 36 months and 90 % are regulation, not study results); Table 3.1 carries ≈ 12 resolution numbers.
- **Own work mentioned (lit review):** ≈ 2 sentences (scope note on grid-connected electrolysis; closing need statement).
- **Chapter-type specifics:**
  - LIT §3.2.1: studies cited 2 (one study, one industry body) plus legal documents; told in depth 0; paragraphs opening with an author name 0; critique phrased as stakeholder controversy; ends with relevance to support schemes. This subsection is really BACK (policy) placed inside the literature review.
  - LIT §3.2.2: studies cited 6 (5 in text, 1 only in Table 3.1); told in depth 3; paragraphs opening with an author name 0; critique phrased "In contrast with the studies described" then a narrow-scope critique (years, countries); ends with L-GAP.
  - MODEL: citations ≈ 3 (all in §3.3.1, crediting the base model and its scenario method); constraint order: new sets → additionality → spatial/temporal → exemption → pipeline objective term → pipeline capacity balance → repurposing cap → hydrogen pipeline capacity; each constraint explained in 1–3 sentences (≈ 40–60 words) right after it, naming every symbol. Assumptions given with reason, rarely with direction of bias.
  - DATA: instances each tied to an RQ (yes); A-PARAM-TABLE as quantities table and case–criteria matrix; no data figures in the main text; no data limitations paragraph.
  - RES: order is total cost → cost components (generators, electrolyzers, transmission) → per-rule breakdown → limitations. R-TECH absent (no solver, runtime or gap reported; the 300 GB memory issue appears only in ch. 4). R-SENS only as the designed case comparison; no R-STOCH.
  - CONCL: RQ1 then RQ2, in order; RQ2 answered rule by rule with bold labels.
- **What makes this chapter strong:**
  - Case names encode the active constraints (letters for each rule plus "90" for the exemption), and a check-mark matrix table shows which rule is on in which case. The "remove one rule at a time from the full case" design isolates each rule's cost, and the conclusion mirrors it with one labelled item per rule.
  - RQ2 is written with the rules as lettered sub-items, so the reader sees from the start that results and conclusion will go rule by rule.
  - Cost results are given as an absolute figure plus a share of total system cost, and one net effect is broken into its parts (extra capex minus fuel and operating savings), which makes the number traceable.
  - The cost-breakdown figure is used as a table of contents: after it, a one-sentence signpost announces three bold sub-headings in the same order as the figure's main components.
  - Every case-defining constraint change is written as an explicit modification of a numbered base equation, so the case definitions are reproducible.
- **Weaknesses:**
  - §3.2.1 is policy background inside the literature review; the review of modelling studies (§3.2.2) has only three paragraphs.
  - Results interpretation seldom reaches an implication for policy or industry, though "policy implications" is in the conclusion heading.
  - Limitations are one paragraph; only one has a stated direction of bias.
- **Signal phrases:** "To the authors' knowledge, no"; "In contrast with the studies described"; "This indicates that"

### 4 Reflections on the first paper [DISC + FUT]
- **Purpose in one line:** Critically reviews paper 1 (gap identification, modelling decisions, computational experience), lists future-research directions, and turns one of them (seasonal storage) into the design decisions for paper 2.
- **Opening paragraph does:** OTHER(scope of the reflection: recaps paper 1 in two sentences, then lists what will be evaluated: framework, assumptions, data, depth).
- **Closing paragraph does:** D-ASSUMP+A-SOURCE: replaces endogenous industrial hydrogen demand with exogenous hourly profiles for comparability across cases (last of the model-reduction decisions for paper 2).
- **Subsections (in order):**
  - 4.1 Identifying research gaps → how the gap was found (literature + industry co-supervisors) and what it was.
  - 4.2 Modeling decisions → three decisions revisited (fixed hydrogen output, electrolysis-only, pipeline repurposing).
  - 4.3 Practical experience when solving → memory, not time, is the bottleneck.
  - 4.4 Identified potentials for future research → 4.4.1 off-grid electrolysis, 4.4.2 feasibility of Spain as dominant producer, 4.4.3 seasonal energy storage.
  - 4.5 Introducing the next paper → motivation and the reductions made to fit seasonal storage in memory.
- **Paragraph moves (in order, per subsection):**
  - intro: OTHER(reflection scope)
  - 4.1: OTHER(research process: literature plus industry needs), L-GAP
  - 4.2: X-ASSUMP+X-METHOD (fixed output enables fair comparison but forces the system; endogenous demand would be more realistic), X-ASSUMP+X-CONTEXT (excluding blue hydrogen; earlier study finds blue cheaper → costs likely overstated; direction given), X-ASSUMP+X-METHOD (repurposing included; without it costs would look too high; but adds memory and its feasibility is uncertain; direction given)
  - 4.3: OTHER(context: model has grown), X-METHOD (memory requirement over 300 GB, driven by stochastic scenarios), X-METHOD (lesson: choose features deliberately)
  - 4.4: OTHER(lead-in: three most critical), F-EXT (off-grid: what + why), F-EXT (expected effect), F-EXT (Spain: what), F-EXT (land competition and spatial resolution: why the assumption limits), F-EXT (freshwater: what + why + a fix), F-EXT (transmission reliability and distance: why + direction "overstates Spain's advantage"), F-EXT (regional model: complexity cost handled), F-EXT (seasonal storage: why missing, history), F-EXT (why it hurts hydrogen specifically: consequence), F-EXT (complexity cost: memory)
  - 4.5: OTHER(bridge: solar reliance implies seasonal imbalance; one supporting citation), M-RATIONALE (memory forces reductions; decided using paper 1's results), A-PROCESS+D-ASSUMP (16 of 30 generators below 1 % of energy removed), A-PROCESS (51 → 20 nodes; how merged), D-ASSUMP (CCS and gas network replaced by cost/price data), D-ASSUMP+A-SOURCE (exogenous hourly hydrogen demand)
- **Paragraph length:** average ≈ 85 words; shortest ≈ 25; longest ≈ 200 (blue-hydrogen paragraph in §4.2).
- **Figures and tables:** 0.
- **Numbers from other studies:** 0 (all numbers are own: memory size, generator and node counts).
- **Chapter-type specifics (DISC/FUT):** X-ASSUMP with direction of bias in 2 of 3 decisions; X-METHOD on computational limits with one hard number; F-EXT parts present: off-grid (what, why, effect), Spain (what, why, effect for the transmission item, complexity for the regional-model item), seasonal storage (what, why, consequence, complexity) — seasonal storage is the only one with all four parts, and it is the one taken forward.
- **What makes this chapter strong:**
  - Each revisited modelling decision follows the same arc: what we did → why it served the RQ → what it excludes → which way the result is likely biased. Two of three state the direction explicitly (excluding blue hydrogen raises costs; omitting repurposing would exaggerate costs).
  - The computational lesson is concrete (memory, not runtime, with a GB figure and its cause), and it is reused later as the reason for every reduction in §4.5.
  - Future-research items are ranked ("most critical"), and the last one becomes the next paper, so the chapter is a hinge rather than an add-on.
  - Model reductions for the next paper are each justified with a measurable criterion (share of energy produced, demand size, geographic closeness), which is a reusable way to defend simplifications.
- **Weaknesses:**
  - §4.1 is process narrative (how the group worked with supervisors) that adds little to the argument.
  - Off-grid electrolysis and Spain items are not followed up anywhere later.
- **Signal phrases:** "A more realistic approach would"; "comes at the expense of"; "Upon seeing the heavy reliance"

### 5 Article 2: Exploring European hydrogen demand variations under tactical uncertainty with seasonal hydrogen storage [paper: ABS / INTRO / LIT / MODEL+SOLVE / DATA+SCEN / RES / CONCL+FUT]
- **Purpose in one line:** Introduces multi-stage operational problems (tree branching at season changes, cyclic storage linking) inside a multi-horizon stochastic capacity expansion model, and measures the value of seasonal hydrogen storage under three hydrogen-demand profiles.
- **Opening paragraph does:** (abstract) AB-CONTEXT+AB-WHY+AB-METHOD+AB-RES-OP+AB-RES-ECON (three numbered results); (§5.1 first paragraph) I-CONTEXT+I-CONCEPT: hydrogen's role and the balancing value of seasonal storage.
- **Closing paragraph does:** F-EXT: added complexity forced lower resolution; test whether multi-stage matters enough, and test other sampling methods / hours per season.
- **Subsections (in order):**
  - Abstract.
  - 5.1 Introduction → context, own prior paper and its gap, other studies' gap, 3 RQs, aim and novelty, outline.
  - 5.2 Literature review → 5.2.1 uncertainty modelling in energy system planning (with three uncertainty levels defined); 5.2.2 seasonal energy storage modelling; 5.2.3 seasonal hydrogen storage in energy system models; 5.2.4 research gaps and contribution; Table 5.1.
  - 5.3 Methodology → 5.3.1 model structure; 5.3.2 model extensions (multi-stage operations, scale factor, rolling horizon, Figures 5.1–5.3); 5.3.3 mathematical formulation (storage linking, eq. 5.1–5.3).
  - 5.4 Case studies and data → 5.4.1 six cases (3 demand profiles × with/without seasonal storage, Fig 5.4); 5.4.2 data (Table 5.2); 5.4.3 rolling horizon and multi-stage parameters.
  - 5.5 Results and discussion → 5.5.1 total system costs; 5.5.2 hydrogen investments; 5.5.3 hydrogen system operations; 5.5.4 power generation differences; 5.5.5 limitations.
  - 5.6 Conclusion → three bold-labelled takeaways; 5.6.1 future research.
- **Paragraph moves (in order, per subsection):**
  - Abstract: AB-CONTEXT+AB-WHY+AB-METHOD+AB-RES-OP+AB-RES-ECON
  - 5.1: I-CONTEXT+I-CONCEPT, I-LIT (own paper 1: findings and what it lacks), I-LIT (other studies: perfect foresight or no inter-season transfer; demand-profile assumptions untested), I-RQ (3 RQs: how to model, effect on investments, effect of demand profile), I-AIM+I-CONTRIB (two-part novelty), I-OUTLINE
  - 5.2 intro: L-SCOPE+L-TABLE
  - 5.2.1: L-RELEVANCE+L-GROUP+L-STUDY (multi-horizon SP as state of the art; two works by one group told in one sentence each), L-PAIR (two review articles, two sentences each), L-TAXONOMY (operational / tactical / strategic uncertainty defined as a labelled list), L-RELEVANCE+L-OWN
  - 5.2.2: L-STUDY+L-CRITIQUE (one study links seasons but without tactical uncertainty), L-SYNTH+L-CRITIQUE (uncertainty vs seasonal linking conflict; seasonally independent models such as the base model undervalue storage), L-STUDY+L-PAIR+L-NOTCOVERED (pumped-hydro stochastic-tree study; contrasted by perspective with the previous study; neither looks at system investments)
  - 5.2.3: L-STUDY+L-CRITIQUE (single-business MILP, one week per quarter), L-PAIR (three full-year models; storage outcomes differ, one cites a cavern-storage volume), L-PAIR+L-NOTCOVERED (how they set hydrogen demand: no seasonal profile), L-CRITIQUE+L-OWN (no uncertainty, flat demand → this study complements)
  - 5.2.4: L-GAP+L-CONTRIB
  - 5.3 intro: D-INTRO
  - 5.3.1: D-INTRO, D-INTRO+A-SCEN (Fig 5.1, two horizons, sampled scenarios), D-INTRO (objective and constraint families in words), D-ASSUMP (electrolysis only, green rules applied, exemption dropped because eligibility is uncertain)
  - 5.3.2: D-EXT (two extensions announced), OTHER(base structure recap with Fig 5.1: seasons independent), D-EXT (Fig 5.2: link seasons; perfect-information problem; branch at season changes), D-EXT+D-ASSUMP (scale factor for storage change because samples cover part of a season), D-EXT (more and longer representative periods to reduce sampling irregularity), S-WHY+S-ALGO (rolling horizon), S-ALGO+S-FIG (Fig 5.3: fixed vs forecast decisions), S-WHY (trade-off stated), D-ASSUMP (lower spatial and technology detail; Appendix E)
  - 5.3.3: D-NOTATION+D-INTRO (sets, operational nodes, cyclic linking; full model referred to paper 1), D-CONSTR (eq. 5.1–5.2 storage balance), D-CONSTR (eq. 5.3 inter-node storage passing with scale factor)
  - 5.4 intro: A-PURPOSE
  - 5.4.1: A-INSTANCES (six cases tied to RQ2–RQ3; profiles stated as illustrative, not forecasts), A-INSTANCES+A-FIG (non-seasonal cases fix start/end storage at half capacity; Fig 5.4 profiles; power peaks in winter)
  - 5.4.2: A-SOURCE, A-SOURCE, A-SOURCE+A-PROCESS+A-SCEN (demand totals, profile source, how profiles are assigned to aggregated countries, same sample dates for cross-correlation), A-SOURCE (storage cost), OTHER(open code statement)
  - 5.4.3: S-IMPL+A-PROCESS (horizon lengths, number of subproblems, hours per year, branching months)
  - 5.5 intro: R-AIMS
  - 5.5.1: R-OBS (Fig 5.5: storage lowers cost for every profile), R-INTERP (cause: fewer generators; storing beats building), R-OBS (constant profile saving), R-OBS+R-INTERP (winter peak saving and why), R-OBS+R-INTERP (summer peak; flagged counter-intuitive comparison explained by early, undiscounted investments)
  - 5.5.2: R-OBS (Fig 5.6 introduced), R-OBS+R-INTERP (winter peak: where storage goes; pipeline reduction in %), R-OBS+R-INTERP (constant), R-OBS+R-INTERP (summer peak: storage spread out, half the need), R-INTERP+R-CAVEAT (why storage cost and capacity rank differently: timing and discounting; Appendix B)
  - 5.5.3: R-OBS (Fig 5.7, expected values defined), R-OBS+R-INTERP (without storage production tracks demand; with storage profiles converge), R-OBS+R-INTERP+R-IMPL (burning hydrogen for power is inefficient; Appendix D)
  - 5.5.4: R-OBS+R-INTERP (why production differences do not sum to zero: losses), R-OBS+R-INTERP (Fig 5.8), R-OBS+R-INTERP (Fig 5.9 winter peak), R-INTERP (summer peak), R-SUMMARY+R-IMPL (storage favours VRES, especially solar; price stabilisation in Appendix C)
  - 5.5.5: R-CAVEAT+C-POINTER (rolling horizon may cause myopic decisions; decomposition could fix it)
  - 5.6: C-DONE, C-ANSWER (RQ1, labelled "Modelling tactical uncertainty"), C-ANSWER+C-FIND-INV+C-FIND-OP (RQ2, storage investment multiplied 5–14 times; less pipeline and dispatchable capacity), C-ANSWER+C-FIND-INV (RQ3)
  - 5.6.1: F-EXT
- **Paragraph length:** average ≈ 83 words; shortest ≈ 20; longest ≈ 200.
- **Figures and tables:** 9 figures in main text (2 model-structure diagrams shown as a before/after pair, 1 rolling-horizon diagram, 1 demand-profile figure, 5 results) + 2 tables (literature comparison, data sources). Each results figure is named at the start of its subsection; OBS→INTERP→IMPL complete for ≈ 2 of 5 (Fig 5.7 and the Fig 5.8–5.9 pair via the summary paragraph).
- **Numbers from other studies (lit review):** 2 in text (a representative-week choice, a cavern-storage volume); Table 5.1 adds seasonal scale factors.
- **Own work mentioned (lit review):** ≈ 6 sentences (end of 5.2.1, inside 5.2.2 about the base model, end of 5.2.3, and 5.2.4).
- **Chapter-type specifics:**
  - LIT §5.2.1: studies cited 8; told in depth 2; author-name openings 0; critique none (sets vocabulary); ends with L-OWN.
  - LIT §5.2.2: studies cited 2; told in depth 2; author-name openings 2 of 3; critique phrased with "However," and "Neither focuses on"; ends with L-NOTCOVERED.
  - LIT §5.2.3: studies cited 4; told in depth ≈ 3; author-name openings 2 of 4; critique phrased as "do not consider"; ends with L-OWN.
  - LIT §5.2.4: one-paragraph gap and contribution with two numbered gaps.
  - MODEL: citations ≈ 9 (base model papers, scenario sampling, scale-factor source, rolling-horizon source, EU policy); constraint order: intra-node storage balance → first-hour balance → inter-node storage passing; only the changed constraints are given, the rest referred to paper 1.
  - SOLVE: rolling horizon with S-WHY, S-ALGO and S-FIG; no bounds or stopping criteria (not a decomposition algorithm).
  - DATA/SCEN: cases tied to RQs (yes); profiles explicitly declared illustrative; data-source table; scenario sampling keeps cross-correlation by sharing dates across demand and VRES; no data limitations paragraph.
  - RES: order is economic (total cost) → investment → operational (hydrogen) → operational (power) → limitations. R-TECH absent; no R-STOCH (no value of the multi-stage structure vs perfect-information linking is measured, which 5.6.1 admits).
  - CONCL: three labelled takeaways in RQ order.
- **What makes this chapter strong:**
  - The method extension is shown as a before/after pair of model-structure figures, and every design step is paired with the specific problem it fixes (linking seasons → perfect foresight → branch at season changes; partial sampling → undervalued storage → scale factor; unrepresentative samples → more and longer periods). Each fix cites where the problem was identified.
  - The literature review defines three uncertainty levels as a labelled list before reviewing storage papers, then uses "tactical" consistently through method, results and conclusion. This is the clearest vocabulary move in the thesis.
  - Two studies are contrasted by perspective (investment planning vs plant revenue) and the paragraph closes with what neither does, which leads straight into the gap.
  - Results compare matched case pairs ('X' vs 'X - S') with one percentage each, and one counter-intuitive comparison is flagged and then explained (early investments miss later cost declines and discounting).
  - Conclusion takeaways carry bold labels that paraphrase each RQ, so the RQ-to-answer mapping is visible at a glance.
- **Weaknesses:**
  - The method claims to add tactical uncertainty, but no result isolates its value (no comparison with deterministic seasonal linking); this is left to future research.
  - Results stay at observation/interpretation; few implications for planners.
  - Limitations section is one short paragraph about the rolling horizon only.
- **Signal phrases:** "However, these studies either assume"; "Neither focuses on"; "From the literature review, we find"

### 6 Concluding remarks [CONCL + FUT]
- **Purpose in one line:** Summarises both papers' findings as numbered lists with headline numbers, synthesises them into one message, and lists three future-research directions.
- **Opening paragraph does:** C-PROBLEM: two sentences restating the purpose and why hydrogen demand matters.
- **Closing paragraph does:** F-EXT: model a natural gas network alongside the reduced model to study green vs blue hydrogen.
- **Subsections (in order):** (main body: paper 1 findings, paper 2 findings, synthesis) → 6.1 Future research.
- **Paragraph moves (in order, per subsection):**
  - main: C-PROBLEM, C-ANSWER+C-FIND-ECON+C-FIND-INV+X-IMPL+C-LIMIT (paper 1: three numbered findings with the headline cost; a policy suggestion on the exemption; caveat that modelled volumes exceed EU ambitions), C-ANSWER+C-FIND-ECON+C-FIND-INV+C-FIND-OP (paper 2: four numbered findings, one with a cost range in %, the last one methodological), C-OVERALL (the two papers together: green hydrogen requires much new VRES, seasonal storage balances it; both should be central)
  - 6.1: OTHER(lead-in), F-EXT (restore full multi-horizon investment instead of rolling horizon: what + why it limits), F-EXT (higher spatial resolution, bidding zones: what + why + "could impact results"), F-EXT (green vs blue with gas network: what + why)
- **Paragraph length:** average ≈ 118 words; shortest ≈ 35; longest ≈ 300 (paper 1 findings paragraph).
- **Figures and tables:** 0.
- **Chapter-type specifics (CONCL/FUT):** findings presented per paper, numbered, in the same order as each paper's RQs; numbers repeated from results (headline cost, cost-variation %); no new results. F-EXT parts: what to add present in all 3; why the assumption limits in all 3; expected effect only vaguely in 1; complexity cost in 1 (the rolling-horizon item, implicitly).
- **What makes this chapter strong:**
  - Each paper gets one paragraph that starts with a one-line restatement of its method and then a numbered list of findings, each finding followed by one sentence on what it means (for models, for subsidy adequacy, or for policy design).
  - The last body paragraph does the synthesis a paper-based thesis needs: it states the one message that only appears when both papers are read together (complementary strategies), tying back to the title.
  - One finding is turned into a concrete policy suggestion (tightening the renewable-grid exemption), with a hedge that the realism of the modelled strategy is outside their remit.
- **Weaknesses:**
  - Future research overlaps with ch. 4 and §5.6.1 without cross-referencing; expected effects are mostly missing.
  - The thesis-level objectives from §1.3 are not named explicitly; answers are organised by paper instead.
- **Signal phrases:** "Our studies reveal the following"; "These papers highlight the interplay"

## 3. Whole-thesis notes
- **How the red thread is kept between chapters:** Ch. 2 splits the problem into two sections that map one-to-one to ch. 3 and ch. 5, each naming its chapter. Paper 1's conclusion ends on the seasonal-storage limitation; ch. 4 lists it as a future-research item with all four parts, and §4.5 turns it into the design of paper 2 (including the memory-driven reductions). Paper 2's introduction cites paper 1 (by its journal reference) and states exactly what it lacked. Ch. 6 has one paragraph per paper and then one synthesis paragraph. Recurring terms held constant: green hydrogen, VRES, additionality/spatial/temporal correlation, tactical uncertainty, seasonal storage, EMPIRE.
- **How the RQs or objectives are answered in the conclusion:** Within each article, RQs are answered in order (paper 1: RQ1 in prose with numbers, RQ2 as a bold-labelled list per rule; paper 2: one bold-labelled takeaway per RQ). In ch. 6, findings are numbered per paper with headline numbers; the two thesis-level objectives of §1.3 are not addressed by name.
- **Anything a strong thesis does that the codes do not capture:**
  - A bridging "reflections" chapter between papers is a reusable device for paper-based theses: it critiques paper 1 (assumptions with bias direction, computational lessons) and justifies paper 2's design, which turns two separate articles into a sequence.
  - Case naming as a code for active constraints, plus a case × criterion check-mark table, makes a factorial-style design readable without prose.
  - Appendices answer "why" questions that the results raise (why one country dominates, why storage cost and capacity disagree, why hydrogen is burned for power), each referenced from the exact results sentence that raises it; the main results stay short.
  - Article cover pages state contributions by students vs supervisors and the journal submission status (reuse declaration handled at the article level and in the preface).
  - For our thesis: the argument that linking storage across representative periods inside a two-stage scenario model gives the storage operator perfect foresight, and the remedy of branching at season changes, is the same issue that motivates stagewise uncertainty (Markov-chain SDDP) in our work; their three-level uncertainty vocabulary could be cited or contrasted in our method or literature chapters. Abgottspon and Andersson (2014), a pumped-storage paper with stochastic intrastage subproblems, is cited in §5.2.2 and is worth checking for our literature list (not yet verified against our references).
