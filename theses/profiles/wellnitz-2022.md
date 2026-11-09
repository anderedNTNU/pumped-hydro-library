# wellnitz-2022 — Sonja Wellnitz and Simon Pearson, 2022
- File: `theses/texts/marketplaces-for-dso-side-flexibility-providers-insights-reg.txt`
- Type: paper-based (two journal-style papers framed by an introduction, a problem description, a bridge chapter and concluding remarks). SESAM dual degree (TU Berlin / NTNU).
- Topic: using load flexibility from distribution-grid resources (DERs) for German re-dispatch, first through TSO-DSO coordination frameworks (deterministic, 2015 and 2030), then through coordinated bidding in congestion management (CM) plus the intraday market (IDM) (two-stage stochastic, 2030).
- Relevance to a pumped-hydro / SDDP / multi-market thesis: low for structure; medium for paragraph style in results/discussion and for the multi-market bidding literature (coordinated vs separate bidding, Aasgård et al. 2019 on hydropower).
- Citation style: author-year (rendered "Author et al. (year)" even when parenthetical)
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 29,700 by `wc -w` (includes the two paper abstracts, equation and table residue; running prose ≈ 26,000–27,000 (?))
- Research questions stated explicitly: yes (4 RQs, two per paper; stated in Ch. 2 §2.2 and §2.3, and repeated as bullets in each paper's introduction, §3.1 and §5.1). Ch. 1 gives objectives only, no thesis-level RQ.

## 1. Chapter map
Mapping of article sections to chapter types: each paper (Ch. 3, Ch. 5) is one chapter that holds a full article. Its sections map as Abstract → ABS, Introduction → INTRO, Related literature → LIT, Methodology → FRAME+MODEL (with SCEN inside 5.3.2), Case study → DATA, Results (incl. "Discussion and sensitivity" / "Discussion and critical reflection") → RES+DISC, Conclusion → CONCL (+FUT bullets in 5.6), Appendices → APP. They are listed as sub-rows.

| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| – | Preface | PRE | 26 | 515 | – | 6 | 0 | 0 |
| – | Abstract (thesis) | ABS | 77 | 505 | – | 3 | 0 | 0 |
| 1 | Introduction | INTRO | 403 | 1,570 | 5.3 % | 14 | 3 | 0 |
| 2 | Problem description | PROB+FRAME | 591 | 1,690 | 5.7 % | 18 | 3 | 0 |
| 3 | Paper 1: value of TSO-DSO coordination in re-dispatch | (article) | 814 | 12,860 | 43.3 % | 101 | 8 | 6 |
| 3-abs | Abstract | ABS | 821 | 220 | | 1 | | |
| 3.1 | Introduction | INTRO | 842 | 670 | | 5 | 2 | |
| 3.2 | Related literature | LIT | 906 | 2,760 | | 16 | 1 | |
| 3.3 | Methodology (3.3.1–3.3.3 cases, 3.3.4 model) | FRAME+MODEL | 1178 | 3,360 | | 39 | 1 | |
| 3.4 | Case study | DATA | 1642 | 1,770 | | 11 | 1 | 2 |
| 3.5 | Results (incl. 3.5.3 discussion + sensitivity) | RES+DISC | 1883 | 3,630 | | 24 | 3 | 4 |
| 3.6 | Conclusion | CONCL | 2304 | 450 | | 5 | | |
| 3.7 | Appendices (nomenclature, gen. mix, sensitivity plots, code link) | APP | 2349 | 550 | excl. | – | 3 | – |
| 4 | Towards a more realistic value for DSO side flexibility | DISC+FRAME (bridge) | 2467 | 1,100 | 3.7 % | 9 | 0 | 0 |
| 5 | Paper 2: multi-market bidding (CM + IDM) | (article) | 2587 | 11,350 | 38.2 % | 82 | 16 | 3 |
| 5-abs | Abstract | ABS | 2594 | 235 | | 1 | | |
| 5.1 | Introduction | INTRO | 2617 | 520 | | 5 | 1 | |
| 5.2 | Related literature | LIT | 2684 | 2,070 | | 16 | 1 | |
| 5.3 | Methodology (5.3.2 = price scenarios; 5.3.4 = model) | FRAME+SCEN+MODEL | 2889 | 3,010 | | 26 | 7 | |
| 5.4 | Case study | DATA | 3316 | 1,050 | | 9 | | 1 |
| 5.5 | Results (incl. 5.5.3 discussion and critical reflection) | RES+DISC | 3436 | 3,820 | | 20 | 7 | 2 |
| 5.6 | Conclusion | CONCL+FUT | 3809 | 640 | | 5 | | |
| 5.7 | Appendices (nomenclature, regression tables, arbitrage table, code link) | APP | 3876 | 735 | excl. | – | 2 | 4 |
| 6 | Concluding remarks | CONCL+FUT | 4001 | 1,120 | 3.8 % | 7 | 0 | 0 |

Totals (main text): ≈ 231 paragraphs, 30 figures, 9 tables.

## 2. Chapters

### – Abstract (thesis-level) [ABS]
- **Purpose in one line:** summarise both papers in one text, one paragraph per paper after a shared context paragraph.
- **Moves:** P1 AB-CONTEXT+AB-WHY+AB-PROBLEM (+ a sentence declaring the paper-based format); P2 AB-METHOD+AB-CASE+AB-RES-OP+AB-RES-ECON+AB-IMPL (paper 1: deterministic model, two frameworks vs business as usual, 2015 and 2030, which framework wins, value too low today but promising later); P3 AB-METHOD+AB-RES-ECON+AB-IMPL (paper 2: two-stage stochastic, coordinated bidding, multi-market access raises value and lets more nodes take part).
- **Note:** no numbers in the abstract at all; results are directional only.

### 1 Introduction [INTRO]
- **Purpose in one line:** move from climate targets to the problem that distribution-side flexibility is large but unused, then state the two challenges the two papers address.
- **Opening paragraph does:** I-HOOK+I-CONTEXT — international climate target (sourced) → need for more renewables in power.
- **Closing paragraph does:** I-OUTLINE — chapter-by-chapter outline that names both paper titles and the short transition chapter.
- **Subsections (in order):**
  - 1.1 The future of European power systems → renewables make supply weather-dependent and decentralised; flexibility is short; DERs introduced with a services figure.
  - 1.2 The challenging integration of demand side resources → physical barrier (one-way grid design) and market barriers (minimum sizes, prequalification, low pay).
  - 1.3 Objectives of the thesis → narrow to re-dispatch; name two challenges; one paragraph per paper aim.
  - 1.4 Structure of the thesis → outline.
- **Paragraph moves (in order, per subsection):**
  - 1.1: I-HOOK+I-CONTEXT, I-CONTEXT, I-CONTEXT+I-PROBLEM, I-CONCEPT+I-PROBLEM
  - 1.2: I-PROBLEM (two kinds of challenge previewed), I-CONCEPT (top-down system, Fig. 1.2), I-PROBLEM (fit-and-forget blocks flexibility), I-CONCEPT (coordination makes the system bidirectional), I-PROBLEM+I-LIT (economic and regulatory barriers, Fig. 1.3)
  - 1.3: I-SCOPE (focus on re-dispatch because other services are already studied), I-AIM (two challenges named i/ii), I-AIM (paper 1), I-AIM (paper 2)
  - 1.4: I-OUTLINE
- **Paragraph length:** average ≈ 100 words; shortest ≈ 45; longest ≈ 175
- **Figures and tables:** 3 figures (flexibility services, traditional TSO/DSO set-up, German market timeline); each introduced in the text that surrounds it; interpreted only in one sentence, no implication step; 0 complete.
- **Chapter-type specifics (INTRO):** no explicit RQs here (they appear in Ch. 2); no contribution list, no findings preview, no reuse declaration (the preface mentions the specialization project; the thesis abstract says paper 1 extends it). Only 4 sourced claims in the whole chapter.
- **What makes this chapter strong:**
  - The barriers are sorted into two named kinds (physical/structural vs market/economic), and §1.3 reuses exactly those two as challenge (i) and (ii), giving one paper to each. The problem taxonomy becomes the thesis structure.
  - The scope is justified by what others already cover (other services are "already a matter of ongoing research"), so narrowing to re-dispatch looks like a positioning choice, not a limitation.
  - Each paper's aim gets its own short paragraph, and the second paragraph opens by contrasting itself with the first ("While the first paper…").
- **Weaknesses:** a stray working note was left under Fig. 1.3 (a file-location remark); the hook is generic (global warming target), not specific to Germany or flexibility; few sources.
- **Signal phrases:** "Nevertheless, there are several challenges"; "in order to maintain a reasonable focus"

### 2 Problem description [PROB+FRAME]
- **Purpose in one line:** set the scope and the two perspectives (system vs provider), describe the base model and the frameworks in words and diagrams, and state the RQs for each paper.
- **Opening paragraph does:** P-PURPOSE — tells what the chapter covers (scope + idea behind the model).
- **Closing paragraph does:** M-STEP+P-UNCERT — the IDM price is unknown when the CM decision is made, so regression-based price scenarios and a two-stage stochastic model are used.
- **Subsections (in order):**
  - (intro) → scope: market-based, not electrotechnical; two perspectives; preview.
  - 2.1 Power system model → the inherited base model (day-ahead dispatch then TSO congestion management), named BAU.
  - 2.2 Coordinated DER integration frameworks → RQs of paper 1; two-case approach. 2.2.1 TSO-managed (centralised; weakness). 2.2.2 DSO-managed (decentralised; trade-off).
  - 2.3 Providing incentive for DSO side flexibility → RQs of paper 2; extended framework with IDM price signals.
- **Paragraph moves:**
  - intro: P-PURPOSE, P-SCOPE, P-ACTOR (two stakeholder perspectives), M-OVERVIEW
  - 2.1: M-STEP (base model flow, Fig. 2.1), M-STEP (BAU ignores distribution side)
  - 2.2: M-OVERVIEW, I-RQ (2 bullets), M-STEP
  - 2.2.1: M-STEP, M-RATIONALE (why this case is unrealistic)
  - 2.2.2: M-STEP, M-RATIONALE (pros and cons)
  - 2.3: M-OVERVIEW+P-PURPOSE, P-MARKETS+I-RQ (2 bullets), M-STEP (Fig. 2.3), M-STEP, M-STEP+P-UNCERT
- **Paragraph length:** average ≈ 85 words; shortest ≈ 40; longest ≈ 185
- **Figures and tables:** 3 flow diagrams (BAU; TSO-M vs DSO-M side by side; provider-perspective framework). Each is announced in the paragraph ("As Figure 2.x shows") and then walked through box by box. 0 tables.
- **Chapter-type specifics (PROB):** P-PURPOSE yes · P-ACTOR yes (TSO, DSOs as aggregators, providers) · P-SYSTEM yes (German TS + DS nodes) · P-HORIZON no (daily sequences appear only in Ch. 3) · P-MARKETS yes (DAM, CM, IDM) · P-UNCERT yes (IDM price only) · P-DECISIONS partial (load shifting allocation) · P-CONSTRAINTS no · P-OBJECTIVE in words (cost min for DSO-M, benefit max under uncertainty for paper 2) · P-OUTPUT no · P-SCOPE yes (infrastructure excluded). **Symbols:** none. **Numbers:** none except "four scenarios". **Length:** ≈ 3.5 pages.
- **What makes this chapter strong:**
  - Each framework is described with the same pattern: who optimises, what information flows to whom, what is sent back. Then comes one paragraph on what is lost in realism. The pairs read as a set because the pattern is the same.
  - The DSO-M paragraph opens by naming the weakness of the TSO-M case that it fixes, so the second case is motivated by the first.
  - The RQs sit next to the framework they are answered with, not in the introduction. Each RQ pair is followed immediately by "to answer these questions, we…".
  - It is a symbol-free, number-free preview of both models, so a reader can follow the flow diagrams before the papers start.
- **Weaknesses:** the title promises a problem description, but most paragraphs are framework/method overview; no planning horizon or decision list; RQ wording differs slightly between Ch. 2 and the paper introductions.
- **Signal phrases:** "picks up the aforementioned weakness"; "bears some weaknesses when facing reality"

### 3 Paper 1 — The value of TSO-DSO coordination in re-dispatch [ABS, INTRO, LIT, FRAME+MODEL, DATA, RES+DISC, CONCL]

#### 3-abs Abstract [ABS]
- One paragraph: AB-CONTEXT (65 % renewables target → congestion), AB-PROBLEM (no regulatory route for DERs), AB-METHOD (two cases vs BAU), AB-CASE (2015, 2030), AB-RES-OP (both cases reduce re-dispatch), AB-RES-ECON (value too low in 2015), AB-IMPL (promising in 2030 for operators and asset owners). No numbers except the target.

#### 3.1 Introduction [INTRO]
- **Purpose in one line:** a journal-style introduction with a dated national target, the DER opportunity, the RQs, the case approach and an outline.
- **Opening paragraph does:** I-HOOK+I-CONTEXT — dated, sourced national target; two maps (overload index, re-dispatch cost) show the congestion consequence.
- **Closing paragraph does:** I-OUTLINE.
- **Paragraph moves:** I-HOOK+I-CONTEXT, I-CONCEPT+I-PROBLEM (DERs growing; one-way grid design keeps them out), I-AIM+I-LIT+I-RQ (2 bullets; one sentence says the literature gives this limited attention), OTHER(method preview: three cases, two data years), I-OUTLINE
- **Paragraph length:** average ≈ 130; shortest ≈ 60; longest ≈ 200
- **Figures:** 2 (maps), both introduced in P1 with one clause each on what they show; no interpretation beyond that.
- **What makes it strong:** the gap claim is one sentence placed directly before the RQs, so the RQs read as the answer to it; the case-approach paragraph explains why two data years are used (the current system vs the system the frameworks were designed for).
- **Weaknesses:** the outline points to the wrong section number (a section of paper 2), a copy-paste trace.
- **Signal phrases:** "has received very limited attention"

#### 3.2 Related literature [LIT]
- **Purpose in one line:** classify TSO-DSO coordination schemes and modelling approaches, then show that none applies DSO-side flexibility to re-dispatch.
- **Opening paragraph does:** L-TAXONOMY — DER categories and the default fit-and-forget treatment.
- **Closing paragraph does:** L-CONTRIB+L-OWN — groundwork claim, country-wide scale, a reusable model.
- **Subsections (in order):** (intro) DER types and integration paths → 3.2.1 Coordination mechanisms overview (centralised / hybrid / decentralised) → 3.2.2 Modelling approaches (centralised, hierarchical bi-level, iterative, aggregator-benefit) → 3.2.3 Contribution (summary figure + 4 bullets + paragraph).
- **Paragraph moves:**
  - intro: L-TAXONOMY, L-TAXONOMY+L-GROUP, L-SYNTH+L-RELEVANCE (active DSO as enabler → coordination needed)
  - 3.2.1: L-TAXONOMY (centralised vs decentralised; hierarchical vs distributed; three-way scheme), L-PAIR+L-CRITIQUE (TSO-managed: computational burden, harder with more DERs), L-STUDY+L-CRITIQUE (hybrid: efficient in theory but operator conflicts → judged unrealistic), L-PAIR+L-SYNTH (DSO-managed variants; challenges are start-up problems → judged most promising)
  - 3.2.2: L-TAXONOMY, L-GROUP, L-PAIR (two hierarchical models differ in timing), L-PAIR (iterative nodal-price variant), L-STUDY (aggregator-benefit model as a different perspective), L-NOTCOVERED+L-GAP
  - 3.2.3: L-GAP+L-TABLE (summary figure), L-CONTRIB (4 bullets), L-CONTRIB+L-OWN
- **Per subsection:**
  - intro: studies cited ≈ 11 · in depth 1 · author-name openers 0 · ends with the consensus that DSO coordination is needed.
  - 3.2.1: cited ≈ 10 · in depth ≈ 5 · author-name openers 1 · critique phrased as feasibility verdicts (not realistic / most promising) · ends with a verdict on which scheme is most promising.
  - 3.2.2: cited ≈ 9 · in depth ≈ 6 · author-name openers 1 · critique by contrast ("Unlike X and Y…") · ends with what nobody covers (re-dispatch with a DSO sub-problem).
  - 3.2.3: 0 new citations; points back to the figure.
- **Paragraph length:** average ≈ 150; shortest ≈ 50; longest ≈ 345
- **Figures and tables:** 1 literature-map figure (studies placed by market entrance point vs DSO model, with "This paper" placed in the map); introduced in 3.2.3 and used as evidence for the gap.
- **Numbers from other studies:** 0
- **Own work mentioned:** ≈ 9 sentences + 4 bullets, all in 3.2.3 (0 before it).
- **What makes this chapter strong:**
  - Each scheme in the taxonomy gets a verdict (complex / conflict-prone / most promising). The review argues towards the design choice (a decentralised DSO-managed case) instead of only listing.
  - The modelling subsection compares studies on one dimension at a time (order of the TSO and DSO sub-problems, market timing), so pairs of papers are contrasted on the same axis.
  - The gap is shown visually: the map figure puts all studies on two axes with the own paper in the empty corner, and the text points to it twice.
  - The final paragraph of 3.2.2 is a pure "not covered" paragraph that names the closest study and says exactly what it leaves out (DERs at TS level, no DSO model).
- **Weaknesses:** no quantitative results from any study (0 numbers); very long paragraphs where 4–6 names pile up in one sentence; the theme intro does not state the review's dimensions up front.
- **Signal phrases:** "Few solutions aim to integrate"; "Hence, neither … nor"

#### 3.3 Methodology [FRAME+MODEL]
- **Purpose in one line:** describe the three cases as steps in a daily flow chart, then give assumptions and the LP formulations (ED, CM, TSO-M extension, DSO-M load-shifting, final CM).
- **Opening paragraph does:** M-OVERVIEW — three cases, one flow chart.
- **Closing paragraph does:** D-EXT — the final CM is the base CM with demand replaced by the DSO's returned profiles.
- **Subsections (in order):** 3.3.1 BAU (benchmark; inherited model; sequential 24 h runs) → 3.3.2 TSO-M → 3.3.3 DSO-M → 3.3.4 Model formulation (tools; assumptions; ED step 1; CM step 2a; TSO-M step 2b; DSO-M step 3; final CM step 4).
- **Paragraph moves:**
  - 3.3: M-OVERVIEW
  - 3.3.1: M-STEP, M-STEP (sequence, information passed, remuneration rule)
  - 3.3.2: M-STEP+D-ASSUMP (no DS constraints), M-RATIONALE (welfare-maximising but unrealistic)
  - 3.3.3: M-STEP+D-ASSUMP (one DSO per node), M-STEP (steps 3–4), M-STEP
  - 3.3.4 tools: M-TOOLS (Julia, inherited code, nomenclature in appendix)
  - assumptions: D-ASSUMP ×6 (ramping, cross-border, inter-DSO competition, DER behaviour as load change, losses, sectoral shifting shares)
  - ED: D-INTRO, D-OBJ, D-CONSTR, D-CONSTR, D-CONSTR (PHS), D-CONSTR
  - CM: D-NOTATION (price as dual of ED balance), D-OBJ, D-CONSTR, D-CONSTR, D-CONSTR (line flow + margin), D-CONSTR, D-CONSTR
  - TSO-M: D-EXT, D-CONSTR ×5
  - DSO-M: D-EXT, D-NOTATION (daily average price; nodal re-dispatch cost/volume signal), D-OBJ
  - final CM: D-EXT, D-EXT
- **Paragraph length:** average ≈ 55; shortest ≈ 25; longest ≈ 210
- **Figures and tables:** 1 flow chart (left: BAU/TSO-M steps 1+2a/2b; right: DSO-M steps 1–4); introduced first and used throughout as the step numbering. 0 tables.
- **Chapter-type specifics (MODEL):** assumptions are given as bold run-in labels, 1–4 sentences each, each with a reason (non-binding, out of scope, no data, small magnitude). Direction of bias is stated for 1 of 6 (shifting shares chosen low to avoid overestimating); magnitude is given for losses (1.7–3.4 %). Constraint explanation: 1–3 sentences before the equation, introduced by a bold run-in label ("Objective function.", "Market clearing."). **Citations in the model section (3.3.4): ≈ 7; whole 3.3 ≈ 11.** Constraint order: objective → balance → capacity limits → storage → non-negativity; extensions are given as "what changes" relative to the base CM. Data numbers appear inside the model (VOLL 1,000, margin 0.25, 5 %/10 % shifting).
- **What makes this chapter strong:**
  - The step numbers in the flow chart (1, 2a, 2b, 3, 4) are reused as the subheadings of the formulation, so each equation block can be placed in the diagram.
  - Extensions are written as differences from the base model ("objective and most constraints remain unchanged; demand becomes a variable"), which keeps three models short.
  - Footnotes carry technical caveats (e.g. the price signal only matters through its shape within a day), so the main text keeps moving but the reader is warned.
  - Every case description ends with an honest one-paragraph realism check, which prepares the later discussion.
- **Weaknesses:** citations and data values inside the model; equation numbering mismatch in the text (refers to 3.9–3.11 for 3.8–3.11) (?); the sentence on power generation is cut off mid-clause.
- **Signal phrases:** "To keep computational effort reasonable"; "We acknowledge that assuming"

#### 3.4 Case study [DATA]
- **Purpose in one line:** describe the 2015 and 2030 data sets, the processing needed to make 2030 usable, and the uniform sector split for DSOs.
- **Opening paragraph does:** A-PURPOSE (one sentence: two data years).
- **Closing paragraph does:** A-PROCESS — sector shares chosen slightly below statistics to avoid overstating industry; justified as stable to 2030.
- **Paragraph moves:**
  - intro: A-PURPOSE
  - 3.4.1: A-SOURCE, A-CASE (grid size, plant counts, capacity shares, Table 3.1), A-PARAM-TABLE+A-PROCESS (marginal-cost formula)
  - 3.4.2: A-SOURCE, A-SOURCE+A-CASE (grid, generation, cost classes, the fictitious per-node backup capacity and why it exists), A-PROCESS (keeping that capacity because lost load would explode without it), A-PROCESS (format differences), A-PROCESS (3 bulleted line-parameter assumptions with a reactance formula)
  - 3.4.3: A-LIMIT (no DSO data; > 880 DSOs), A-PROCESS (Fig. 3.5 sector split)
- **Paragraph length:** average ≈ 90; shortest ≈ 25; longest ≈ 350 (bullet list)
- **Figures and tables:** 2 tables (capacity by technology / by cost class), 1 pie figure; tables introduced before shown; the pie is not interpreted.
- **What makes it strong:** each data set gets source → what it contains → why it is credible (who else used it) → what had to be adapted; a modelling oddity in the data (fictitious capacity) is explained from the source's own planning logic, not just stated; data gaps (DSO grids) are turned into an explicit uniform assumption with a reason.
- **Weaknesses:** the text references "Table 5.1" (paper 2's table) instead of Table 3.2; the 2030 table is a raw dump of cost classes.
- **Signal phrases:** "To avoid the lack of real data"

#### 3.5 Results (incl. 3.5.3 Discussion and sensitivity analysis) [RES+DISC]
- **Purpose in one line:** define four indicators, report annual results, zoom in on the two most expensive weeks, explain the mechanisms, discuss assumptions, price the flexibility and test smaller shifting shares.
- **Opening paragraph does:** R-AIMS — four key indicators, each with why it matters (cost, volume, use of DERs, curtailment as green-shift and cost proxy).
- **Closing paragraph does:** R-SENS+R-OBS — the expectations are confirmed; value per MWh rises as capacity falls.
- **Subsection order:** 3.5.1 indicators → 3.5.2 annual results (validity check first) → 3.5.3: microscopic two-week view → "Further discussion" (mechanisms; one block per case-specific assumption; pricing of DERs) → sensitivity. Order: validation → operational → economic → (investment signal via value of load shifting) → sensitivity.
- **Paragraph moves:**
  - 3.5.1: R-AIMS
  - 3.5.2: R-AIMS (Table 3.3), OTHER(validity check vs history + another study's result, gap explained by lost load × VOLL)=R-LIT+R-CAVEAT, R-OBS+R-INTERP+R-CAVEAT (cost savings %, DER pay not included), R-OBS (volume: expectation then check), R-SUMMARY, R-OBS+R-INTERP (load shifting volumes; forward reference), R-OBS
  - 3.5.3 intro: R-AIMS
  - microscopic view: R-AIMS (why and how the two weeks were chosen), R-OBS+R-INTERP (Fig. 3.6), R-OBS+R-INTERP (Fig. 3.7), R-OBS+R-INTERP (Fig. 3.8)
  - further discussion: OTHER(preview), R-INTERP (two mechanisms, numbered), R-INTERP (TSO-M uses both), R-INTERP (DSO-M only mechanism 1), X-ASSUMP (omniscient TSO), R-INTERP+X-ASSUMP (nodes without re-dispatch get no signal), X-ASSUMP (constant price → best-case effect), R-IMPL+R-INTERP (value of load shifting ≈ 8–9 €/MWh too low for investment; Fig. 3.6 explains why), R-OBS (2030 values higher)
  - sensitivity: R-SENS (motivation, setup, two expectations stated in advance), R-SENS+R-OBS
- **Paragraph length:** average ≈ 110; shortest ≈ 30; longest ≈ 275
- **Figures and tables:** 3 figures, 4 tables. Tables are introduced before they are shown; figures are introduced in the paragraph that reads them. OBS→INTERP for all 3 figures; IMPL only for Fig. 3.6 (reused later to explain the low value) → 1 of 3 complete.
- **Numbers from other studies:** 1 (another study's 2030 re-dispatch cost, used for validation).
- **Chapter-type specifics (RES):** R-TECH absent (no solver, runtime or size statistics). R-LIT used once, as validation. R-STOCH n/a (deterministic). Sensitivity on one parameter (shiftable share at ½ and ¼).
- **What makes this chapter strong:**
  - **Expectation first, then check**: before each indicator or sensitivity, the authors say what they expect and why, then report whether it held ("our expectation holds true"). This turns tables into tests.
  - A plausibility check comes before any comparison: modelled generation mix vs history (appendix), and modelled 2030 cost vs another study on the same data, with the gap explained quantitatively.
  - Results are explained by **two named mechanisms** (temporal shift to cheap hours; better fit with grid constraints), and each case's performance follows from which mechanism it can use. One explanation then serves all indicators.
  - The discussion blocks are labelled by case ("TSO-M: …", "DSO-M: …", "Both cases: …"), so the reader knows which result each caveat touches.
  - A simple derived indicator (cost saving ÷ shifted volume = break-even pay per MWh) connects an operational result to the investment question.
- **Weaknesses:** small number inconsistencies between text and tables (e.g. 12.17 vs 12.20 €/MWh); 2030 numbers are mislabelled in the tables (TWh/GWh rows shifted); no runtime or convergence information.
- **Signal phrases:** "our expectation holds true"; "A microscopic view"; "We emphasize that no pricing"

#### 3.6 Conclusion [CONCL]
- **Purpose in one line:** short wrap-up of paper 1.
- **Paragraph moves:** C-PROBLEM (field is new and relevant), OTHER(literature recap)=C-GAP, C-DONE, C-FIND-OP+C-OVERALL (centralised better, decentralised more realistic, trade-off), C-POINTER (three future directions in one paragraph)
- **Paragraph length:** average ≈ 90
- **Note:** no numbers; RQs not answered one by one; the investment finding (value too low) is missing here although it is in the abstract.
- **What makes it strong:** the main finding is phrased as a trade-off (performance vs acceptability), not a winner.
- **Weaknesses:** a whole paragraph recaps literature; no numbers; RQs not mirrored.

### 4 Towards a more realistic value for DSO side flexibility [DISC+FRAME (bridge)]
- **Purpose in one line:** reflect on paper 1's limits and turn each into a design change for paper 2.
- **Opening paragraph does:** OTHER(recap of paper 1 aim, cases, scenarios).
- **Closing paragraph does:** M-STEP — move from deterministic to two-stage stochastic because the IDM price is unknown when the CM allocation is decided.
- **Subsections (in order):** 4.1 Reflections (4.1.1 realisation potential, 4.1.2 static prices, 4.1.3 the two scenarios, 4.1.4 value of load shifting) → 4.2 Transition (focus shift, new market, stochastic extension).
- **Paragraph moves:**
  - 4.1: OTHER(recap), OTHER(preview: focus on limits that link to paper 2)
  - 4.1.1: X-ASSUMP+X-METHOD; 4.1.2: X-ASSUMP (constant price blocks gains from volatility); 4.1.3: X-METHOD (why both years were useful; future looks better); 4.1.4: X-IMPL (numbers: value still too low)
  - 4.2: M-RATIONALE (from system-optimal to provider revenue), M-STEP (add IDM because volatile), M-STEP (stochastic extension)
- **Paragraph length:** average ≈ 110; shortest ≈ 55; longest ≈ 200
- **What makes this chapter strong:**
  - Every reflection subsection ends on a limitation that paper 2 then removes (no signal for nodes without re-dispatch → second market; constant prices → volatile IDM; low value → more revenue streams). The red thread between the papers is explicit.
  - Each reflection is one paragraph with a one-line title, so it reads like a checklist.
- **Weaknesses:** some repetition of 3.5.3.
- **Signal phrases:** "aroused our interest in investigating"

### 5 Paper 2 — Multi-market bidding for DSO side flexibility providers [ABS, INTRO, LIT, FRAME+SCEN+MODEL, DATA, RES+DISC, CONCL+FUT]

#### 5-abs Abstract [ABS]
- One paragraph: AB-CONTEXT, AB-WHY (flexibility helps with balancing and congestion), AB-PROBLEM (unused; pay too low), AB-METHOD (two-stage stochastic, coordinated bidding, decentralised coordination), AB-RES-ECON (higher value than CM-only), AB-IMPL (more providers can take part). No numbers.

#### 5.1 Introduction [INTRO]
- **Paragraph moves:** I-CONTEXT, I-LIT+I-CONCEPT (Fig. 5.1 programmes), I-LIT+I-PROBLEM (limits of current research: CM little studied, incentives missing), I-AIM+I-RQ (2 bullets, after a "little research so far" sentence), I-OUTLINE
- **Paragraph length:** average ≈ 100
- **What makes it strong:** one figure (price-based vs incentive-based programmes) is used twice: first to show what exists, then to show what is missing.
- **Signal phrases:** "little research in this area"

#### 5.2 Related literature [LIT]
- **Purpose in one line:** which markets suit DSO-side flexibility and how multi-market bidding is modelled; position the paper as provider-perspective, stochastic, multi-market and country-scale.
- **Opening paragraph does:** L-TAXONOMY+L-SCOPE — flexibility categories; focus on demand response for load shifting.
- **Closing paragraph does:** L-CONTRIB — continue the CM framework, add the IDM, model its uncertainty stochastically, at country scale for 2030.
- **Subsections:** (intro) → 5.2.1 Attractive markets and perspectives → 5.2.2 Multi-market bidding strategies → 5.2.3 Contribution.
- **Paragraph moves:**
  - intro: L-TAXONOMY+L-SCOPE, L-SCOPE+L-OWN (previous own paper; what this review covers)
  - 5.2.1: L-TAXONOMY (three flexibility products), L-GROUP (agreement and disagreement among integration studies), L-GROUP (AS-market camp), L-PAIR (balancing-market camp), L-PAIR (IDM camp: real-time signals too short), L-PAIR+L-OWN (CM: own previous result plus a Danish study), L-NOTCOVERED+L-PAIR (most take the system view; few take the provider view, DAM vs IDM), L-PAIR+L-SYNTH (multi-market participation pays)
  - 5.2.2: L-RELEVANCE+L-CRITIQUE (strategies built for conventional producers need adapting), L-TAXONOMY+L-PAIR (coordinated vs separate bidding; small but positive gain), L-PAIR (coordinated + stochastic; hydropower example), L-PAIR+L-CRITIQUE (similar markets, small scope)
  - 5.2.3: L-SYNTH+L-GAP, L-CONTRIB
- **Per subsection:**
  - intro: cited ≈ 5 · in depth 0 · ends by saying what the following subsections review.
  - 5.2.1: cited ≈ 19 · in depth ≈ 5 · author-name openers ≈ 3 of 8 · critique phrased as disagreement between camps ("Unlike the previous authors") · ends with the multi-market benefit, which sets up the gap.
  - 5.2.2: cited ≈ 10 · in depth ≈ 3–4 · author-name openers 0 · critique: methods tailored to others; small scope · ends with the scope critique that the contribution answers (country-wide).
- **Paragraph length:** average ≈ 120; shortest ≈ 60; longest ≈ 185
- **Figures and tables:** 1 literature map (provider perspective × stochastic market model × multi-market, with "This paper" at the intersection).
- **Numbers from other studies:** 0
- **Own work mentioned:** ≈ 13 sentences (spread out, mostly references to the previous paper and to 5.2.3).
- **What makes this chapter strong:**
  - The market review is organised as **camps by recommended market** (AS, balancing, IDM, CM), each a paragraph, with the reason each camp gives. The reader sees why the IDM is chosen.
  - The method review introduces a binary distinction (coordinated vs separate bidding) and then sorts studies by it and by deterministic vs stochastic, so the model choices (coordinated, stochastic) are justified from the literature.
  - The final critique (small scope) is exactly the dimension the contribution claims (country-wide), so the gap and the contribution match one to one.
  - The own previous paper is treated as literature (cited with its result), which links the two papers without a special chapter.
- **Weaknesses:** no quantitative findings from studies; some sentences string 4–6 citations together.
- **Signal phrases:** "Unlike the previous authors"; "So far, the literature mainly focuses"

#### 5.3 Methodology [FRAME+SCEN+MODEL]
- **Purpose in one line:** reuse the DSO-M framework, generate IDM price scenarios by regression, and formulate the two-stage stochastic allocation LP.
- **Opening paragraph does:** M-OVERVIEW — order of what follows (CM signal → IDM prediction → decision).
- **Closing paragraph does:** S-IMPL — language, modelling package and solver versions.
- **Paragraph moves:**
  - 5.3: M-OVERVIEW
  - 5.3.1: M-STEP (previous framework, Fig. 5.3), M-STEP (steps 1–4 recap), M-STEP (which steps are kept, changed, removed)
  - 5.3.2: A-SCEN+D-ASSUMP (coordinated bidding; three price scenarios + one "bid not accepted" scenario; uniform IDM price assumed), A-SCEN (regression is the common approach; known drivers from 4 studies), A-SOURCE (candidate regressors, data sources, 2019–2021), A-SCEN (index price ≈ DA price, Eq. 5.1), A-SCEN (high price regression, Eq. 5.2), A-SCEN (low price: no fit → DA trend + random terms, Eq. 5.3), A-SCEN (checked against history, appendix), A-SCEN (probabilities set by correlation strength)
  - 5.3.3: M-STEP (Fig. 5.9: profit maximisation under uncertainty gives a strategy, not an overall optimum)
  - 5.3.4: D-NOTATION, D-ASSUMP ×3 (IDM volume not binding, with a forward reference to where it is checked; one DSO per node; sector shifting), D-OBJ (expected profit), D-OBJ (extensive form), D-CONSTR ×6 (bounds by sector and hour; CM/IDM totals; total shifting per scenario; zero IDM in scenario 4; daily balance; new load profiles), S-IMPL
- **Paragraph length:** average ≈ 90; shortest ≈ 30; longest ≈ 190
- **Figures and tables:** 7 figures (previous framework, market timeline with the decision point, two-stage tree, scenario probabilities, price correlation, price scenarios, flow chart). The two-stage tree and the market timeline make the information structure visible before the equations.
- **Chapter-type specifics:** citations in 5.3.4: 0 (previous paper referred to in words); whole 5.3 ≈ 8. Constraint order: objective → capacity bounds → aggregation → scenario-specific totals → scenario 4 restriction → daily balance → output profiles. SCEN: scenario generation is regression-based for 2 of 3 price scenarios, heuristic for the third; probabilities (45/25/20/10 %) are given in a figure with a qualitative justification only. A-LIMIT: none in the text.
- **What makes this chapter strong:**
  - A market timeline with the decision moment drawn in shows **why** the problem is two-stage (CM is decided before IDM prices are known), before any equation.
  - Market risk of not being filled (bid not accepted) is modelled as its own scenario, and the text later shows how this scenario shapes the results (it forces the CM and IDM positions to balance separately).
  - Assumptions that might bind (IDM volume) are flagged with a forward reference to the discussion, where they are tested against market data.
- **Weaknesses:** scenario probabilities are weakly justified; regression for the high price uses hour as a linear regressor (?) without comment; the low price scenario uses a random component that is described only loosely.
- **Signal phrases:** "a common approach to predict"; "was not a meaningful approach"

#### 5.4 Case study [DATA]
- **Paragraph moves:** A-PURPOSE+A-SOURCE (model previously validated on 2015 data; now only 2030), A-SOURCE, A-SOURCE (data set used by other studies → tested), A-CASE (grid, generation, cost classes, Table 5.1, fictitious backup capacity), A-PROCESS (adaptations documented in paper 1), A-LIMIT (no DS data), A-PROCESS (one unconstrained DSO per node), A-PROCESS (sector split), A-PROCESS (shifting shares; industry only during working hours)
- **Paragraph length:** average ≈ 95
- **What makes it strong:** reuse is declared and pointed to (adaptations "documented in our previous work") instead of repeated; the assumptions are numbered (firstly/secondly/thirdly).
- **Weaknesses:** largely duplicates 3.4 text content.

#### 5.5 Results (incl. 5.5.3 Discussion and critical reflection) [RES+DISC]
- **Purpose in one line:** report volume, revenue and value of load shifting per scenario and in expectation; explain node differences; test the probability of failed bids; run a discussion-only arbitrage case; critique the IDM model and the volume assumptions.
- **Opening paragraph does:** R-AIMS — three indicators with expectations stated (volume should rise vs paper 1) and the most important indicator named.
- **Closing paragraph does:** X-LIMIT+OTHER(future research: other uses of flexibility).
- **Subsection order:** 5.5.1 indicators + expected-value caveat → 5.5.2 volume → revenue → value → 5.5.3: node heterogeneity → sensitivity (failed-bid probability) → arbitrage experiment → IDM price model critique → market volume check → other uses. Order: operational → economic → spatial → sensitivity → model critique.
- **Paragraph moves:**
  - 5.5.1: R-AIMS, R-CAVEAT (expected value vs single-scenario columns)
  - 5.5.2: R-AIMS (Table 5.2; caveat repeated), R-OBS+R-INTERP (up/down shifts balance because of the scenario-4 constraint; IDM volumes; Figs. 5.10–5.11; industry hours), R-OBS+R-INTERP+R-IMPL (revenue; negative prices explain the low-price scenario; IDM > two-thirds of expected revenue; Figs. 5.12–5.13), R-OBS+R-LIT (value for CM compared with paper 1), R-OBS (total value range and expectation)
  - 5.5.3: R-AIMS (preview); nodes: R-INTERP (why nodal CM signals matter; goal from paper 1), R-OBS+R-INTERP+R-IMPL (best vs worst node; price distribution figure); sensitivity: R-SENS (assumption named), R-SENS (setup + expectations), R-SENS+R-OBS (both expectations met; %); arbitrage: R-SENS (setup + expectation), R-OBS+R-IMPL (revenue ×4, unregulated arbitrage risky for market stability); IDM prediction: X-ASSUMP+X-METHOD (uniform vs pay-as-bid; feedback of many new bidders → lower, less volatile prices → lower gains: direction of bias given); volumes: X-ASSUMP (market volume data), X-ASSUMP+R-OBS (Fig. 5.16 check; CM volume pay assumption imprecise, both directions discussed), C-POINTER (one-line summary: model volumes in future work); other uses: X-LIMIT
- **Paragraph length:** average ≈ 140; shortest ≈ 45; longest ≈ 330
- **Figures and tables:** 7 figures, 2 tables. OBS→INTERP→IMPL complete for ≈ 3 of 7 (expected revenue split; node comparison with price distribution; IDM volume check) (?).
- **Numbers from other studies:** 2 (exchange-reported minimum IDM volumes day/night).
- **Chapter-type specifics (RES):** R-TECH absent (no runtime, size or solver output). R-STOCH partial: expected value vs per-scenario outcomes, but no VSS/EVPI or out-of-sample test. R-LIT only against the own previous paper. Sensitivity: scenario probability (10 % → 25 %) and a structural variant (remove failed-bid scenario).
- **What makes this chapter strong:**
  - A **caveat sentence is repeated where it matters** (single-scenario columns are not realistic year-long outcomes; read the expected value), once at the indicators and once at the table.
  - Counter-intuitive patterns are traced to a specific constraint by equation number (balanced up/down shifts follow from the failed-bid scenario + daily balance). Results are explained by the model, not by guesses.
  - A **discussion-only experiment** (remove the failed-bid scenario) is clearly labelled as such and turned into a policy point (unregulated arbitrage).
  - Each limitation paragraph has a bold run-in title and states what the assumption does to the result (e.g. many new bidders would flatten prices and reduce gains).
  - An assumption from the model chapter (IDM volume not binding) is checked against data with a figure, closing the loop opened by the forward reference.
- **Weaknesses:** a unit slip (value given in MWh instead of €/MWh); the conclusion's "scenario 4" range is at odds with the table (?); no runtime or convergence information.
- **Signal phrases:** "which we perform only for discussion purposes"; "This does not come as a surprise"; "is by no means exhaustive"

#### 5.6 Conclusion [CONCL+FUT]
- **Paragraph moves:** C-DONE (long: why the IDM, how scenarios were built, two-stage model), C-FIND-ECON (volume, expected revenue split, value vs paper 1 with numbers), C-OVERALL, C-LIMIT+X-IMPL (no regulatory framework yet; information exchange needed), C-POINTER (3 bullets)
- **FUT bullets:** 3 extensions; each has what to add + why the current assumption limits (2 of 3); none gives expected effect or complexity cost.
- **What makes it strong:** headline numbers are given with a direct comparison to the previous paper (more than double), which makes the contribution measurable.
- **Weaknesses:** a celebratory sentence on exceeding expectations; RQs not answered explicitly.

### 6 Concluding remarks [CONCL+FUT]
- **Purpose in one line:** a thesis-level conclusion that tells the story paper by paper with numbers, then gives limits and a future-research list.
- **Opening paragraph does:** C-PROBLEM+C-DONE — what was researched and which base model was extended.
- **Closing paragraph does:** C-OVERALL+C-POINTER — the contribution in system and provider terms, then 6 future-research bullets.
- **Paragraph moves:** C-PROBLEM+C-DONE, C-DONE+C-FIND-OP+C-FIND-ECON (relative vs absolute savings 2015 → 2030), C-FIND-ECON+C-FIND-INV (centralised better, decentralised realistic; value too low to invest but almost triples), C-DONE (why the IDM was picked among alternatives), C-FIND-ECON (value 25.78 → 52.77 €/MWh; volume +≈60 %; root cause: nodes without re-dispatch now have a use), C-LIMIT (list of assumptions; the main one is dependence on IDM price assumptions), C-OVERALL+C-POINTER (6 bullets)
- **Paragraph length:** average ≈ 135; shortest ≈ 40; longest ≈ 190
- **Chapter-type specifics (CONCL):** RQs not answered one by one or by label; findings are given in paper order with numbers. FUT bullets: 6, each names what to add; ≈ 3 say why the current assumption limits; none gives expected effect or complexity cost.
- **What makes this chapter strong:**
  - Relative and absolute effects are paired (percent savings fall while absolute savings rise), which prevents a misleading reading of the trend.
  - The improvement in paper 2 is tied causally to a weakness found in paper 1 (nodes with no signal), so the conclusion shows a learning arc, not two separate results.
  - The limitations paragraph ends by naming the single most influential assumption rather than leaving a flat list.
- **Weaknesses:** one percentage differs from the paper 1 results (5.68 vs 5.86 %); "We could continue this list" is informal; the RQs from Ch. 2 are not mirrored.
- **Signal phrases:** "The main challenge, however, is"

## 3. Whole-thesis notes
- **Red thread:** (1) the two challenge types from §1.2 become the two paper aims in §1.3 and the two halves of Ch. 2; (2) Ch. 4 is a dedicated bridge in which each limitation of paper 1 maps to a design change in paper 2; (3) paper 2 cites paper 1 as literature and compares its key number to paper 1's (value of load shifting); (4) the same case names (BAU, TSO-M, DSO-M) and the same step numbers (1–4) recur in every diagram; (5) the same indicator (value of load shifting, €/MWh) is the measuring stick in paper 1 results, Ch. 4, paper 2 results and Ch. 6.
- **How RQs are answered:** not explicitly. The four RQs are answered implicitly in the paper conclusions and Ch. 6, in paper order and with numbers, but never quoted or labelled.
- **Beyond the codes:**
  - Literature-map figures with the own paper drawn as a point in the field (Figs. 3.3, 5.2) carry the gap argument visually.
  - "Expectation → result → verdict" is used systematically for indicators and every sensitivity run. It is the most reusable paragraph pattern for our results chapter.
  - Bold run-in labels inside sections (assumptions, constraints, discussion items) replace deeper subsection numbering and keep each paragraph to one point.
  - Footnotes hold technical caveats and edge cases (excluded node, signal scale invariance, the degenerate 100 % case that reproduces paper 1). This keeps the argument clean but shows rigour.
  - Paper-based cost: data and assumptions are repeated almost verbatim across papers (3.4 vs 5.4), and small numerical inconsistencies creep in between the chapters (several noted above).
