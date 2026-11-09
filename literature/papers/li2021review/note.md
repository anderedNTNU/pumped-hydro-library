---
bibkey: li2021review
bibkey_provisional: true
title: "A Review of Stochastic Programming Methods for Optimization of Process Systems Under Uncertainty"
authors: "Can Li, Ignacio E. Grossmann"
year: 2021
venue: "Frontiers in Chemical Engineering 2, Article 622241 (doi:10.3389/fceng.2020.622241)"
peer_reviewed: true
methods: [two-stage-stochastic, multistage-scenario-trees, benders-decomposition, uncertainty-modelling]
review_sections: []
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Tutorial-style review of stochastic programming for process systems: two-stage and multistage (MI)LP/MINLP formulations, VSS/EEV worked example, Benders vs Lagrangean decomposition, nested Benders and SDDP (stagewise-independence caveat), endogenous uncertainty, and data-driven scenario-tree generation (SAA, moment/CDF matching)."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/117_Li_2021_A_Review_of_Stochastic_Programming_Methods_for_Optimization_of_Process_Systems_Under_Uncer.pdf"
---

# Review of stochastic programming for process systems (Li and Grossmann, 2021)

_Page mapping: the article is paginated 1-20 (article number 622241); PDF page n = article page n._

_Bibkey note: not in `references.bib`; key generated in Better BibTeX style (first significant title word "review"). Needs adding to Zotero (the KILDEINFO says it is already in the Zotero library as item N4DI87HM, so check whether Zotero has pinned a different key)._

_Tagging note: theory source only. No `sddp-*` tag because SDDP is only described in one paragraph (p. 12), with the stagewise-independence caveat and no Markov-chain treatment. No review_sections tag: no hydro, storage or electricity-market content._

## Research question / purpose
- Give beginners a tutorial and experts a high-level overview of stochastic programming (SP) and its use in process systems engineering (PSE) (abstract, p. 1).
- Cover: optimization under uncertainty and how SP differs from chance-constrained and robust optimisation (Sec. 2, pp. 3-4); two-stage SP for MILP and MINLP (Sec. 3, pp. 4-9); multistage SP (Sec. 4, pp. 9-13); multistage SP under endogenous uncertainty (Sec. 5, pp. 13-15); data-driven scenario-tree generation (Sec. 6, pp. 15-17); conclusions and challenges (Sec. 7, p. 17).

## Setting
- **System:** generic process-systems problems (supply chains, process networks, pooling, oil-field development). Table 1 (p. 2) lists representative PSE applications, one of which is "scheduling of power-intensive processes" under electricity-price uncertainty (Zhang et al. 2016). No hydro or storage.
- **Markets:** none.
- **Horizon and resolution:** illustrative 2- and 3-stage examples.

## Method
- **Model type:** review / tutorial. Formulations: generic MINLP/MILP/NLP/LP (eq. 1, p. 3); two-stage stochastic MILP deterministic equivalent (eq. 2, pp. 4-5); two-stage stochastic MINLP (eq. 5, p. 8); multistage SP nested form (eq. 6, p. 10), node-based deterministic equivalent and recursive cost-to-go form with transition probabilities q_nm (eqs. 8-9, pp. 10-11); endogenous-uncertainty formulation with conditional non-anticipativity constraints (eq. 10, p. 14); SAA (eqs. 11-12, p. 16); moment- and CDF-matching NLP (eq. 14, p. 17).
- **How uncertainty is represented:** discrete scenarios / scenario trees with known probabilities (p. 4); SAA of a "true" distribution (p. 16); property-matching scenario trees (p. 17).
- **Solution method (reviewed):** extensive form; Benders / L-shaped (finite convergence when recourse is continuous and linear, p. 7); Lagrangean decomposition via non-anticipativity constraints (heuristic upper bound, duality gap, p. 7); generalized Benders and other MINLP decompositions (p. 9); nested Benders (forward and backward pass, still exponential leaf nodes, p. 12); SDDP and SDDiP (p. 12); progressive hedging (p. 13).
- **Key modelling choices and assumptions:** SP framed as risk neutral with a known distribution (pp. 3-4, Table 2).

## Data / case
- Process network design with 3 processes, demand scenarios 8/10/12 with probabilities 0.25/0.5/0.25 (pp. 5-6). Stochastic pooling problem with 3 demand scenarios (p. 9). 3-stage capacity-expansion version (p. 11) and endogenous-yield version (pp. 14-15). No real data apart from the production-yield CDF example of Calfa et al. (2014) (Fig. 12, p. 16).

## Key findings
- (pp. 3-4, Table 2) SP is risk neutral and uses a probability distribution; chance-constrained programming is risk averse (distribution plus risk level); robust optimisation guards the worst case over an uncertainty set.
- (p. 4) Two-stage logic: first-stage "here and now" decisions, then uncertainty resolves, then "wait and see" recourse decisions.
- (pp. 5-6) Worked VSS example: RP = 117.22, EEV = 114.20, VSS = RP - EEV = 3.02 for a maximisation problem (eq. 4). The deterministic (mean-value) model under-sizes process 3 because it is "unaware" of the high-demand scenario.
- (p. 6) Solving the deterministic equivalent directly can be prohibitive because computation time can grow exponentially with the number of scenarios.
- (p. 7) Benders views first-stage variables as "complicating variables"; the master gives the lower bound, the best feasible solution the upper bound; finite convergence when second-stage variables are continuous and constraints linear. Lagrangean decomposition dualises non-anticipativity constraints, decomposes by scenario, upper bound is heuristic, may have a duality gap.
- (p. 9) Stochastic MINLP is hard because of (i) nonconvex second-stage functions and (ii) integer recourse.
- (p. 12) Number of scenarios grows exponentially with stages (3^(H-1) with 3 outcomes per stage). Nested Benders decomposes by nodes but must still solve an exponential number of leaf nodes. SDDP avoids this; "one caveat" is that the process must be stagewise independent, because cuts are then shared among nodes. SDDiP (Zou et al. 2019) extends to integer problems with Lagrangean, integer and strengthened Benders cuts.
- (p. 12) Nested Benders decomposes by nodes, Lagrangean decomposition by scenarios.
- (p. 13) Software: SDDP.jl (Julia/JuMP), MSPPy (Python, SDDP/SDDiP), PySP (progressive hedging in Pyomo).
- (p. 15) Scenario data sources: historical data (reliable but may generalise poorly), statistical/time-series models such as ARIMA and hidden Markov models, and expert knowledge; usually a combination. A poor scenario-generation method "can spoil" the whole model. A good tree captures marginal distributions (moments) and inter-temporal dependence; quality is measured by stability and error (Kaut and Wallace 2003).
- (p. 16) SAA: optimal value and solutions converge as N grows under mild assumptions; sample-size estimates are usually too conservative; SAA can be unstable with few samples and requires knowing the "true" distribution.
- (pp. 16-17) Property matching: Høyland and Wallace (2001) moment matching (NLP over values and probabilities) is under-specified; Calfa et al. (2014) add matching of the empirical CDF (fitted with a generalized logistic function).
- (p. 17) Open challenges: convincing practitioners, nonconvexity (multistage stochastic MINLP with stagewise dependence is a "utopia problem"), better integration of risk measures (CVaR, stochastic dominance), links to other communities (Powell), and high-fidelity data for low-error scenario trees.

## Strengths
- Clear, compact definitions with small numerical examples (VSS/EEV; how the two-stage solution hedges between idle capacity and lost sales, p. 9).
- Good side-by-side description of Benders vs Lagrangean decomposition with a schematic (Fig. 5, p. 7) and of node vs scenario decomposition in the multistage case (p. 12).
- Short, citable overview of scenario-generation approaches (Sec. 6).

## Weaknesses / limitations
- Process-engineering focus; no energy-storage, hydro or market examples.
- SDDP coverage is one paragraph and presents stagewise independence as a hard requirement; Markov-chain SDDP and autoregressive state augmentation are not mentioned. Do not cite it for SDDP with dependent uncertainty.
- Risk aversion only mentioned as future work (p. 17).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3 (Stochastic Optimisation): SP vs chance-constrained vs robust | Table 2 contrast of risk attitude and uncertainty description | pp. 3-4, Sec. 2, Table 2 |
| Theory 3 (Two-Stage): here-and-now / recourse, extensive form | Definitions and eq. 2 | pp. 4-5, Sec. 3.1.1 |
| Theory 3: VSS / EEV for a maximisation problem | VSS = RP - EEV, numerical example | p. 6, eq. 4 |
| Theory 3 (Benders Decomposition): complicating variables, bounds | Master/subproblem, LB/UB, finite convergence for continuous linear recourse | p. 7, Sec. 3.1.3, Fig. 5 |
| Theory 3 (Multistage): scenario tree, nodes, transition probabilities, cost-to-go recursion | eqs. 6-9, Fig. 7 | pp. 10-11, Sec. 4.1 |
| Theory 3 (SDDP): why not nested Benders on full tree; SDDP shares cuts | Exponential leaf nodes; cut sharing under stagewise independence | p. 12, Sec. 4.3 |
| Method: software options | SDDP.jl, MSPPy, PySP | p. 13 |
| Method 6.x (Representation of Prices and Inflow): sources of scenario data and quality criteria | Historical / time series / HMM / expert; stability and error | p. 15, Sec. 6 |
| Theory: SAA | eqs. 11-12, convergence and caveats | p. 16, Sec. 6.1 |

## Useful quotes (with page numbers)
> "A poor scenario-generation method can spoil the result of the whole optimization model." (p. 15)

Paraphrased: one caveat of SDDP is that the stochastic process must be stagewise independent, which allows cuts to be shared among nodes (p. 12).

## Follow-up references to check (backward snowballing)
- Kaut, M. and Wallace, S.W. (2003). Evaluation of scenario-generation methods for stochastic programming.
- Kaut, M. (2011). Scenario generation for stochastic programming: introduction and selected methods (inbox has `kaut2024`, a different item).
- Høyland, K. and Wallace, S.W. (2001). Generating scenario trees for multistage decision problems. Management Science.
- Zou, J., Ahmed, S. and Sun, X.A. (2019). Stochastic dual dynamic integer programming. Math. Programming.
- Kleywegt, Shapiro and Homem-de-Mello (2002). The sample average approximation method for stochastic discrete optimization.
- Torres et al. (2019) and Küçükyavuz and Sen (2017) reviews of decomposition for stochastic integer programs.
- Escudero et al. (2017) review of decomposition algorithms for two- and multistage stochastic MILP.

