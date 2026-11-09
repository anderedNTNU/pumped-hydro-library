# rognes-2023 — Henrik Rognes, 2023
- File: theses/texts/a-novel-flexibility-market.txt
- Type: monograph
- Topic: a proposed day-ahead capacity market (PreFlex) in which wind producers pre-contract DER flexibility through aggregators to balance their own forecast errors; two-stage stochastic models, Norwegian case (NO1-NO4, July and December 2021).
- Relevance to a pumped-hydro / SDDP / multi-market thesis: medium (sequential DA/ID/imbalance markets, two-stage stochastic trading model, quantile-regression scenarios; no hydro, no multistage)
- Citation style: author-year
- Main-text words (intro to conclusion, excl. appendices and references): ≈ 15,800 raw by `wc -w` on lines 266-1819 (includes nomenclature, equations, table cells and captions; running prose ≈ 14,000 (?)). Short thesis: 43 pages of main text.
- Research questions stated explicitly: yes (3 RQs, numbered list in ch. 1 and repeated word for word in 3.2; one RQ per stakeholder: wind producer, DER owner, TSO)

## 1. Chapter map
| # | Title | Type code(s) | Start line | Words (≈) | Share of main text | Paragraphs | Figures | Tables |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction | INTRO | 266 | 940 | 6 % | 8 | 0 | 0 |
| 2 | Background (2.1 market overview; 2.2 literature review) | BACK + LIT | 357 | 2,220 (BACK 1,450; LIT 770) | 14 % | 18 (12 + 6) | 1 | 0 |
| 3 | Problem Description (3.1 market design, 3.2 RQs, 3.3 method overview) | PROB + FRAME | 553 | 2,480 | 16 % | 14 | 1 | 1 |
| 4 | Methodology (4.1 model formulations, 4.2 scenario generation) | MODEL + SCEN | 786 | 3,890 (MODEL 2,650; SCEN 1,250) | 25 % | ≈ 37 (incl. 6 assumption bullets) | 0 | 1 |
| 5 | Data and Case Study | DATA | 1235 | 2,350 | 15 % | 15 | 5 | 3 |
| 6 | Results and Discussion | RES + DISC | 1479 | 3,480 | 22 % | 18 | 4 | 3 |
| 7 | Conclusion | CONCL + FUT | 1788 | 400 | 2.5 % | 3 (?) (paragraph breaks unclear in the text file) | 0 | 0 |
| – | Appendix (descriptive statistics, regression summaries, cost table) | APP | ≈ 1950 | – | – | – | 1 | 8 |

No separate theory, solution-method, validation, discussion or future-research chapter. Literature review is a 3-page section inside Background.

## 2. Chapters

### Abstract [ABS]
- One paragraph, ≈ 220 words. Moves: AB-CONTEXT (DERs untapped) → AB-WHY/AB-PROBLEM (market entry barriers, especially balancing markets) → AB-METHOD (new market design; DERs contracted via aggregator) → AB-CASE (Norway) → AB-RES-OP (lower illiquidity exposure) → AB-RES-ECON (DER revenue ≈ 30 % of DA price) → AB-RES-OP (median system imbalance down, reserve cost not) → AB-IMPL (future work: sequential trading of DERs). A Norwegian summary (Sammendrag) mirrors it.

### 1 Introduction [INTRO]
- **Purpose in one line:** motivate a DER-dedicated market, define it, pose three stakeholder RQs and preview the answers.
- **Opening paragraph does:** OTHER(literary hook: a scene from Greek myth about controlling the winds) + I-CONTEXT — the myth is turned into the point that wind remains uncertain despite forecasting.
- **Closing paragraph does:** I-OUTLINE — one sentence per chapter.
- **Subsections (in order):** none (one unbroken chapter).
- **Paragraph moves (in order):** OTHER(myth hook)+I-CONTEXT, I-CONTEXT+I-CONCEPT (three system challenges of renewables → flexibility need → DERs defined by examples), I-PROBLEM+I-AIM (barriers to DERs in balancing markets → this work proposes a dedicated market; why a dedicated market can be more lenient), I-CONCEPT+I-CONTRIB (what PreFlex is and its value for each party; footnote narrows scope to wind), I-RQ (3 numbered RQs, one per stakeholder), OTHER(method preview: stochastic models + Norwegian case), I-FINDINGS (one result per RQ, with the 30 % number and the reason behind it), I-OUTLINE.
- **Paragraph length:** average ≈ 115 words; shortest ≈ 25 (RQ lead-in); longest ≈ 155.
- **Figures and tables:** 0.
- **Chapter-type specifics:** no dated I-HOOK fact; no I-LIT/gap paragraph (gap left implicit); no I-SCOPE paragraph (scope only in a footnote); I-FINDINGS is explicit and includes the mechanism behind the headline number. 5 citations in the chapter, all in the context paragraph.
- **What makes this chapter strong:**
  - RQs are built around three stakeholders (producer, DER owner, TSO); the same triad later names the sections of ch. 6 and the sentences of the conclusion, so the RQ list doubles as the thesis skeleton.
  - The findings preview gives each answer plus the reason for it (low value because contracted flexibility is often unused), so the reader gets a claim and its mechanism before any model is shown.
  - Scope narrowing (wind, not solar) is put in a footnote with a one-line reason, keeping the main text flowing.
  - Very compact: about 2 pages, eight paragraphs, each with one job.
- **Weaknesses:** the myth opener has no source and no number; there is no stated gap or contribution relative to literature; no explicit delimitation paragraph.
- **Signal phrases:** "Modern technology has not given us"; "The main results are as follows"

### 2 Background [BACK + LIT]
#### 2.1 Nordic power market overview [BACK]
- **Purpose in one line:** give the market and settlement knowledge needed to understand the forecast-error problem of a wind producer.
- **Opening paragraph does:** B-SCOPE — lists the markets covered and why imbalance settlement is included (it is central to the work).
- **Closing paragraph does:** B-FACT+B-SCOPE — recent Nordic settlement changes (single price, 15-minute ISP) followed immediately by the modelling simplification adopted (hourly).
- **Subsections (in order):** 2.1 overview → market timing and who operates what; 2.1.1 day-ahead → auction mechanics; 2.1.2 intraday → continuous trading and its role; 2.1.3 balancing market → capacity vs energy; 2.1.4 imbalance settlement → BRP/BSP roles and pricing rules.
- **Paragraph moves:**
  - 2.1: B-SCOPE, B-FIG+B-MECH (timeline figure; DA/ID vs TSO-run balancing), B-FACT+B-SCOPE (European harmonisation mentioned, declared out of scope)
  - 2.1.1: B-MECH+B-RELEVANCE (uniform-price auction; noon gate closure → wind must forecast 12-36 h ahead)
  - 2.1.2: B-DEF+B-RELEVANCE (imbalance cost defined; footnote on surplus pricing), B-MECH (continuous matching vs uniform price; pointer to an example in a cited source), B-FACT+B-RELEVANCE (ID complements balancing; German evidence)
  - 2.1.3: B-MECH (reserve capacity vs energy market; prequalification)
  - 2.1.4: B-DEF+B-MECH (BRP/BSP; settlement compares delivered vs contracted), B-MECH (who is paid in deficit vs surplus), B-MECH+B-BRIDGE (single vs dual pricing; assumptions deferred to ch. 4), B-FACT+B-SCOPE (Nov 2021 changes; hourly modelling chosen)
- **Paragraph length:** average ≈ 120 words; shortest ≈ 85; longest ≈ 150.
- **Figures and tables:** 1 (market timeline); introduced before shown: yes; interpreted: used as reference, no full OBS→INTERP→IMPL.
- **Numbers from other studies:** 0 numeric values with units from cited studies (only timing facts such as 12:00 gate closure).
- **Own work mentioned:** 4 sentences (key element of this work; out of scope; assumptions in ch. 4; hourly modelling in this work).
- **Chapter-type specifics:** B-MODELLING is absent; B-RELEVANCE is folded into the last sentence of mechanism paragraphs instead of separate paragraphs.
- **What makes this chapter strong:**
  - Each market subsection ends by stating what the mechanism means for a wind producer (e.g. gate-closure time → forecast horizon), so background is always tied to the actor of the thesis.
  - Out-of-scope items are named explicitly in one sentence where they come up, rather than silently omitted.
  - A recent rule change is reported and the modelling simplification adopted in response is stated right after it, so the reader knows how the real system and the model differ.
  - Footnotes carry secondary detail (surplus pricing, one-balance system) so the main paragraphs stay short.
- **Weaknesses:** almost no quantitative facts about Norway (wind share, imbalance volumes) in background; some typos.
- **Signal phrases:** "To help set the stage"; "Being somewhat out of scope"

#### 2.2 Literature review on DER market integration [LIT]
- **Purpose in one line:** show where the literature thinks DERs should be traded and what barriers it names.
- **Opening paragraph does:** L-GROUP+L-PAIR — five sources agree on two points (TSO-DSO coordination, aggregators), then disagree on which market suits DERs best.
- **Closing paragraph does:** L-PAIR+L-OWN — two more sources favour intraday trade; one study is flagged as closest to this thesis's aim.
- **Paragraph moves:** L-GROUP+L-PAIR (consensus, then the split), L-STUDY (review: barriers to balancing markets), L-PAIR+L-STUDY (two sources add the BRP-imbalance issue and why frequency reserves came first), OTHER(concept explanation of the TSO-DSO conflict)+L-GROUP (pointers to an overview), L-PAIR (contrary view favouring intraday, with a two-sentence direct quotation), L-PAIR+L-OWN (supporting source; closest study and its finding)
- **Per subsection:** studies cited 8 · told in depth (≥ 2 sentences) 4 · paragraphs opening with an author name 2 (plus one opening "Contrary to" + names) · critique phrasing: none; differences are framed as disagreement between authors, not as weaknesses · ends with the closest study's finding, no gap statement.
- **Paragraph length:** average ≈ 130 words; shortest ≈ 85; longest ≈ 190.
- **Numbers from other studies:** 0.
- **Own work mentioned:** 1 sentence (closest study "similar to the aim").
- **Chapter-type specifics:** no L-SEARCH, L-TAXONOMY, L-CRITIQUE, L-GAP, L-TABLE or L-CONTRIB. The modelling literature (two-stage wind trading models) is not here but in 3.3 as method positioning. The gap is first argued in 3.1 ("barriers identified in the literature review").
- **What makes this chapter strong:**
  - Organised around consensus vs disagreement: one paragraph states what all sources agree on, the rest unpacks the disagreement, which gives the review an argument instead of a list.
  - The disagreement (balancing vs intraday markets) is exactly the design question the proposed market answers, so the review sets up ch. 3 without saying so explicitly.
  - Uses a pivot opener ("Contrary to X and Y, Z ...") to switch sides of the debate.
- **Weaknesses:** very short (≈ 770 words, 8 sources); no critique or gap paragraph; a long direct quotation stands in for the author's own synthesis.
- **Signal phrases:** "The authors disagree, however, on"; "Contrary to"; "Similar to the aim of"

### 3 Problem Description [PROB + FRAME]
- **Purpose in one line:** propose the market design, state its hypothesised benefits, motivate the RQs and give the two-model comparison approach.
- **Opening paragraph does:** P-PURPOSE+OTHER(section roadmap) — what each section does, and names the two cases (BAU, PreFlex).
- **Closing paragraph does:** M-STEP+M-BRIDGE — subcases that test the hypotheses; details deferred to ch. 4.
- **Subsections (in order):** 3.1 Designing a new market → design, three hypotheses, positioning figure, design-variable table; 3.2 Research questions → objectives, RQs, what is not measured; 3.3 Overview of methodology → method lineage, case comparison; 3.3.1 BAU, 3.3.2 PreFlex, 3.3.3 subcases → one paragraph each.
- **Paragraph moves:**
  - intro: P-PURPOSE+OTHER(roadmap)
  - 3.1: OTHER(design proposal: recap of lit-review barriers, grey-literature quote, market defined)+P-ACTOR, OTHER(hypothesis 1: fewer restrictions on wind producers, with three cited complications), OTHER(hypothesis 2: remuneration for DERs), OTHER(hypothesis 3: market efficiency, three numbered reasons), P-MARKETS+P-HORIZON (figure: position and timing relative to DA/ID/balancing; settlement with BRPs), P-SCOPE+OTHER(design-variable table introduced; design is provisional)
  - 3.2: P-ACTOR+P-PURPOSE+P-SCOPE (why evaluate before a costly institutional process; three actors; wind only; what each perspective measures) → RQ list, P-SCOPE (why social welfare is not quantified; three perspectives instead; conventional generators excluded)
  - 3.3: M-RATIONALE+OTHER(method lineage from literature and how this work differs), M-OVERVIEW (two cases compared; each RQ mapped to the comparison that answers it)
  - 3.3.1: M-STEP (BAU: two stages, DA then ID, scenarios from probabilistic forecasts)
  - 3.3.2: M-STEP (PreFlex as modification of BAU)
  - 3.3.3: M-STEP+M-BRIDGE
- **Paragraph length:** average ≈ 165 words; shortest ≈ 90; longest ≈ 250.
- **Figures and tables:** 1 figure (market positioning) + 1 table (design variables: variable / trade-offs / choice here); both introduced before shown; figure explained in the paragraph after it.
- **Chapter-type specifics:** contains no symbols; numbers only in design choices (36-hour horizon, one-hour availability); ≈ 6 pages. P-DECISIONS, P-UNCERT, P-OBJECTIVE appear only inside the FRAME subsections (3.3.1-3.3.2), in words. 11 citations in the chapter (method lineage, hypotheses).
- **What makes this chapter strong:**
  - Benefits are stated as numbered, bold-titled hypotheses with a mechanism and citations; ch. 4 builds a subcase for each and ch. 6 returns to them one by one ("Another hypothesis was"). This makes testability visible.
  - The design-variable table (variable, trade-off, choice made) shows that the design is one point in a space and justifies each choice in one line.
  - The chapter states what it deliberately does not measure (social welfare) with two concrete reasons, and what replaces it (three stakeholder views), pre-empting an examiner's objection.
  - The method-overview paragraph maps every RQ to the comparison that answers it.
  - Method positioning names the research line the model belongs to and then two explicit differences (aggregate producers; aim is behaviour change, not optimal bidding).
- **Weaknesses:** RQs repeated verbatim from ch. 1; hypotheses and method-literature make the chapter partly a second lit review; the problem description is spread over design, RQs and method instead of a crisp decision-maker statement.
- **Signal phrases:** "Before undergoing the relatively cumbersome"; "Different from the literature mentioned above"

### 4 Methodology [MODEL + SCEN]
#### 4.1 Model formulations [MODEL]
- **Purpose in one line:** formulate the deterministic equivalents of the BAU and PreFlex two-stage models and the three subcases.
- **Opening paragraph does:** D-INTRO+OTHER(roadmap) — two models compared; 4.1 formulations, 4.2 scenarios.
- **Closing paragraph does:** D-EXT — the "DERs traded intraday" subcase is defined as PreFlex minus a named block of constraints.
- **Subsections (in order):** 4.1.1 Assumptions → six bold-titled bullets; 4.1.2 Nomenclature → indices, variables per model, parameters; 4.1.3 BAU → objective and 4 constraint groups; 4.1.4 PreFlex → only the changes; 4.1.5 Subcases → three variants.
- **Paragraph moves:**
  - intro + 4.1 intro: D-INTRO, OTHER(roadmap)
  - 4.1.1: D-ASSUMP ×6 (wind known late in ID; homogeneous producers per area; no market power; deterministic imbalance prices; single-price rule; DER availability independent of past use)
  - 4.1.2: D-NOTATION (lists, not tables)
  - 4.1.3: D-INTRO (purpose: baseline), D-OBJ, D-CONSTR (DA bid bound), D-CONSTR (imbalance balance), D-CONSTR (surplus/deficit split), D-CONSTR (non-negativity)
  - 4.1.4: D-EXT (what changes vs BAU), D-OBJ, D-CONSTR (contract bounds), D-CONSTR (imbalance with DER activation), D-CONSTR (activation ≤ contracted), D-CONSTR+D-LINEAR (big-M: no selling DER energy intraday), D-CONSTR+D-LINEAR (big-M: no intentional surplus), D-CONSTR (non-negativity)
  - 4.1.5: D-EXT (three subcases and their purpose), D-EXT+OTHER(empirical literature and theory behind wind-dependent ID prices), D-EXT+D-CONSTR (illiquidity: ID volume forced to zero in sampled scenarios), D-EXT (benchmark case)
- **Paragraph length:** constraint paragraphs ≈ 20-80 words; assumption bullets ≈ 40-80; subcase paragraphs up to ≈ 225.
- **Figures and tables:** 0 in 4.1.
- **Chapter-type specifics:** assumptions are justified (reason or literature) for 3 of 6, one is admitted unrealistic, one states its modelling consequence (hourly decomposition); no direction of bias given for any. Constraint explanation is typically one bold run-in heading plus 1-3 sentences before the equation. Constraint order: objective → market bid bounds → balance → imbalance split → logic (big-M) → non-negativity. Citations in 4.1: ≈ 9 (assumption support and subcase motivation); 4.2 adds ≈ 3.
- **What makes this chapter strong:**
  - Every constraint group has a bold run-in title written as a plain-language rule (e.g. that DER energy cannot be resold intraday), so the reader can skim the model by its headings.
  - The extended model is presented as a delta to the base model: only added variables, the modified objective and new constraints, with an explicit statement that the rest holds.
  - The benchmark subcase is defined by removing a named equation range, which makes the comparison exact.
  - Logical big-M constraints are each motivated by an undesired behaviour from the system's point of view, not just stated.
- **Weaknesses:** notation has errors (a probability given a price unit, mixed MWh/kWh, garbled symbols); no explicit objective-term walk-through table; assumptions lack direction of bias.
- **Signal phrases:** "Somewhat unrealistically,"; "All changes and modifications"

#### 4.2 Scenario generation [SCEN]
- **Purpose in one line:** build 14 probability-weighted wind scenarios from quantile regression and set the intraday price model.
- **Paragraph moves:** A-SCEN+OTHER(method choice justified by non-normal errors, forward reference to ch. 5), A-SCEN (regressors explained), A-SCEN (quantile list), A-SCEN (forecast error → production quantile), A-SCEN (symbols explained), A-SCEN+A-PARAM-TABLE (adjacent quantiles averaged; probabilities in table), A-SCEN+A-PROCESS (ID price: volume-weighted, anchored on DA price, regression set up), A-SCEN (symbols explained), OTHER(regression result → modelling choice: no systematic relation, so ID = DA in base case), A-SCEN (wind-dependent case calibrated at 5 %, justified as low end of a cited range plus Norway's lower wind share)
- **Figures and tables:** 1 table (scenario probabilities).
- **What makes this chapter strong:**
  - Each calibration number is justified twice: by a cited range and by a country-specific reason for picking its low end.
  - A tested-but-rejected modelling relation is reported, and the base case is set from that finding, so a simplification is backed by evidence.
- **Weaknesses:** regression findings (a result) are reported in the method chapter; equations display badly in text form.

### 5 Data and Case Study [DATA]
- **Purpose in one line:** describe the 2021 Norwegian wind, DER and price inputs and the treatments applied.
- **Opening paragraph does:** A-PURPOSE+A-CASE — Norwegian 2021 context, hourly decomposition, and two contrasting months chosen on purpose.
- **Closing paragraph does:** OTHER(expectation for results) — since DERs respond to direct activation, not price, price volatility affects results only through the producers' demand for flexibility.
- **Subsections (in order):** 5.1 Wind power data → sources, statistics, forecast-error distributions, generated forecasts; 5.2 DER data → volumes from a TSO report and adjustments; 5.3 Electricity price data → DA and ID series and two-month comparison.
- **Paragraph moves:**
  - intro: A-PURPOSE+A-CASE, OTHER(roadmap: three data categories)
  - 5.1: A-SOURCE+A-PROCESS (net errors only; NO5 dropped), A-FIG (violin plot read with numbers), A-FIG+A-LIMIT (NO3 bias noted; raw data kept to avoid complexity), A-FIG+OTHER(statistics → method choice: leptokurtic, skewed → quantile regression; consistent with an international study), A-FIG+A-LIMIT (forecasts judged realistic by visual check; proper backtests named but not done)
  - 5.2: A-SOURCE (three DER types following a cited study; volumes from a national report, cross-checked with a second source), A-PROCESS (peak-hour estimates ÷ 12, allocated by population), A-FIG+A-PROCESS (availability rules by season and hour; symmetric up/down), A-FIG+A-PROCESS+A-PARAM-TABLE (uneven distribution → inter-area exchange assumption, sanity-checked with observed flows on 10 days), A-PARAM-TABLE
  - 5.3: A-SOURCE+A-FIG (price series; regime shift late 2021 explained by gas supply and interconnection), A-PARAM-TABLE+OTHER(why compare July and December), OTHER(expectation for results)
- **Paragraph length:** average ≈ 155 words; shortest ≈ 50; longest ≈ 250.
- **Figures and tables:** 5 figures + 3 tables; introduced before shown: yes; data figures interpreted: 5 of 5 (4 with a consequence for the model or case).
- **What makes this chapter strong:**
  - Each descriptive statistic is followed by its consequence for the method (non-normal errors → quantile regression; uneven DER location → exchange assumption).
  - Transformations of external estimates are spelled out step by step (divide, allocate by population, restrict by season and hour), and a second source is used as a robustness check.
  - Limitations are declared at the point where they arise, each with the reason for accepting them (e.g. visual check deemed sufficient for a simulation use).
  - The two months are chosen to span low and high price volatility, which gives the results a built-in contrast.
  - The chapter ends by telling the reader what the price data should and should not change in the results.
- **Weaknesses:** the DER volume assumption (central to the results) gets no sensitivity in ch. 6; some details (e.g. 10 arbitrary days) are thin as evidence.
- **Signal phrases:** "should be noticed"; "a visual check is deemed"

### 6 Results and Discussion [RES + DISC]
- **Purpose in one line:** answer the three RQs from the simulations, one stakeholder per section.
- **Opening paragraph does:** R-SUMMARY — all main results with ranges up front (cost reductions per month, 30 % DER price, median vs peak imbalances).
- **Closing paragraph does:** R-OBS+R-IMPL — peak empirical imbalances far exceed the simulated reductions, so reserve costs would not fall.
- **Subsections (in order):** 6.1 Wind producer perspective (RQ1) → revenues, imbalance-management costs, two hypothesis tests; 6.2 DER perspective (RQ2) → price sweep, value, activation share, intraday benchmark; 6.3 Effects on system balancing (RQ3) → simulated vs empirical imbalances.
- **Paragraph moves:**
  - intro: R-SUMMARY, OTHER(roadmap by perspective)
  - 6.1: R-OBS+R-INTERP+R-CAVEAT (revenues: modest gains; benchmark gain flagged as optimistic; pointer to 6.2), R-OBS+R-INTERP+R-IMPL (cost reductions with and without DER cost; displaced ID volumes), OTHER(hypothesis test: disadvantageous ID prices)+R-OBS+R-INTERP, OTHER(hypothesis test: illiquidity)+R-OBS+R-IMPL
  - 6.2: R-AIMS+OTHER(method: DER price swept as share of DA price, with reasons), R-OBS (revenue peak at 30 %), R-INTERP+R-IMPL (difference between months traced to NO3 forecast-error skew; 30 % taken as realistic), R-OBS+R-INTERP (value table; low compared with producers' alternatives), R-OBS+R-INTERP+R-CAVEAT (≈ 40-56 % activation explained by error symmetry; aggregation assumption discussed), R-INTERP+R-IMPL (unused capacity limits willingness to pay → utilisation is the lever), R-OBS (benchmark: higher value), R-CAVEAT+X-ASSUMP+R-IMPL (who would buy that energy? empirical ID volume quartiles → benchmark overstated; DERs need several markets)
  - 6.3: R-AIMS+A-SOURCE+R-CAVEAT (RQ3; only December has data; order-of-magnitude comparison only), R-OBS (empirical imbalance figure), R-OBS+R-INTERP (median reductions as % of system imbalance; NO3 explained by back-reference to ch. 5), R-OBS+R-IMPL (peaks vs reductions → reserve volume unchanged)
- **Paragraph length:** average ≈ 175 words; shortest ≈ 45; longest ≈ 310.
- **Figures and tables:** 4 figures + 3 tables (+ 1 appendix table referenced); introduced before shown: yes; OBS→INTERP→IMPL complete for ≈ 6 of 7 (revenue figure lacks a clear implication, deferred).
- **Chapter-type specifics:** order of result subsections follows the RQs/stakeholders (producer → DER owner → TSO), not technical → operational → economic. R-TECH absent (no solver, runtime, model size). R-LIT absent (no cited study in the chapter). R-SENS only through the price sweep and subcases; R-STOCH absent. DISC moves (X-ASSUMP, X-IMPL) are embedded in result paragraphs; no separate discussion or limitation section.
- **What makes this chapter strong:**
  - Opens with the complete set of headline numbers, so the rest of the chapter reads as evidence for already-stated claims.
  - Hypotheses from ch. 3 are tested one per paragraph, each opened by restating the hypothesis and closed with a verdict.
  - An unknown input (the DER price) is handled by sweeping it and taking the revenue-maximising level as the estimate of value, and the reason for expressing it relative to the DA price is given.
  - A surprising number (low value) is explained by a simple reasoning chain (deficits occur about half the time → about half the capacity is used → willingness to pay is capped), which becomes the main policy lesson and the future-work item.
  - The optimistic benchmark is challenged with a direct question about who the buyer would be, then answered with empirical trading-volume quartiles; the median-vs-peak distinction in 6.3 likewise turns a positive finding into a nuanced conclusion.
- **Weaknesses:** no computational details or convergence checks; results never compared with other studies; no sensitivity on DER volumes or scenario count.
- **Signal phrases:** "At first glance, this appears"; "The following question arises"; "From this, it is concluded"

### 7 Conclusion [CONCL + FUT]
- **Purpose in one line:** restate what was done, answer the three RQs in order with one number each, and give one future-research direction.
- **Opening paragraph does:** C-PROBLEM+C-DONE — market proposed, simulated in a Norwegian case, judged from three perspectives.
- **Closing paragraph does:** F-EXT — sequential trading of DER flexibility, with a concrete mechanism (a release deadline after which unused flexibility can be sold elsewhere).
- **Paragraph moves:** C-PROBLEM+C-DONE, C-ANSWER (RQ1)+C-FIND-ECON+C-ANSWER (RQ2, with 30 % and the activation range and its cause)+C-ANSWER (RQ3), F-EXT+C-POINTER
- **Paragraph length:** ≈ 60, ≈ 200, ≈ 140 words.
- **Chapter-type specifics:** RQs answered in order but not labelled as RQs; numbers carried into the conclusion (30 %, 38.7-56.3 %). No C-LIMIT, no C-GAP. F-EXT has: what to add (yes), why the current design limits (yes: low utilisation), expected effect (yes: higher revenue, more DER supply), complexity cost (no).
- **What makes this chapter strong:**
  - The single future-research item is derived from the key driver found in the results (utilisation), so it reads as a consequence, not a wish list.
  - The future-work item includes a concrete design mechanism, not only a topic.
  - Short (≈ 400 words) and follows the RQ order exactly.
- **Weaknesses:** no limitations; only one extension; complexity cost of the extension not discussed.
- **Signal phrases:** "Further research should consider"

## 3. Whole-thesis notes
- **Red thread:** the three-stakeholder triad (wind producer, DER owner, TSO) appears in the intro RQs, the 3.2 objectives, the 3.3 RQ-to-comparison mapping, the 6.x section titles and the conclusion. The three hypotheses of 3.1 are turned into subcases in 4.1.5 and tested by name in 6.1. The headline number (≈ 30 % of the DA price) recurs in abstract, intro, results and conclusion. Back-references are explicit ("as discussed previously", with figure and chapter numbers).
- **How the RQs are answered in the conclusion:** in order, one per stakeholder, each with a number or a clear yes/no-type verdict, but without the words "RQ1/2/3".
- **Beyond the codes:**
  - The thesis proposes a new institution (a market design) rather than optimising a plant; it handles this by a design-variable table plus testable hypotheses, which is a reusable way to make a qualitative design choice examinable.
  - Literature on modelling methods is placed in the framework section (3.3) as positioning of the model, separate from the domain literature review in 2.2.
  - Results and discussion are merged, with caveats and assumption checks embedded in the paragraph where each result appears.
  - Empirical data (system imbalances, ID trade volumes, cross-border flows) are used repeatedly as reality checks on simulated or assumed quantities.
  - Relatively thin by A-level standards on literature (≈ 40 references, short review) and on technical reporting; its strength is the tight RQ → hypothesis → subcase → result chain.
