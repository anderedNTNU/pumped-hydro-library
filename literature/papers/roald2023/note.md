---
bibkey: roald2023
title: "Power Systems Optimization under Uncertainty: A Review of Methods and Applications"
authors: "Line A. Roald, David Pozo, Anthony Papavasiliou, Daniel K. Molzahn, Jalal Kazempour, Antonio Conejo"
year: 2023
venue: "Electric Power Systems Research 214, 108725 (PSCC 2022 special issue); our PDF is the CORE Reprint 3257 in PSCC 2022 layout"
peer_reviewed: true
methods: [two-stage-stochastic, benders-decomposition, sddp-time-series, risk-averse-cvar, uncertainty-modelling, multistage-scenario-trees]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Power-systems-oriented overview of optimisation under uncertainty: uncertainty representations, risk-neutral/risk-averse/DRO/robust/chance-constrained formulations, Benders/SDDP/dual decomposition/PH/CCG, and a clear recipe for in-sample vs out-of-sample evaluation (EVPI, VSS); SDDP is called the go-to method for hydro-thermal planning, with water values from its duals."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/roald2023.pdf"
---

# Power systems optimisation under uncertainty (Roald et al., 2023)

_Page mapping: our PDF is the author/CORE reprint (34 PDF pages: 2 CORE cover pages, then the paper in PSCC 2022 two-column layout with printed page numbers 1-32). **Paper page n = PDF page n + 2.** All page numbers below are the printed PSCC-layout pages. The EPSR journal version (article 108725) has different pagination; if we cite page numbers, either obtain the publisher PDF or cite section numbers (which should be the same, unverified)._

_Tagging note: `sddp-time-series` because the SDDP described is the classical serially independent version, with a pointer to Löhndorf and Shapiro (2019) for more general uncertainty (p. 12); there is no Markov-chain detail. `multistage-scenario-trees` is mentioned only in passing (p. 2). `modelling-phs-plants` because Sec. XII (p. 24) states SDDP's role in hydro planning and water values and mentions pumped-hydro day-ahead bidding._

## Research question / purpose
- Overview of methods for modelling and optimisation under uncertainty for readers familiar with power systems and optimisation, especially graduate students; explicitly not a tutorial on any single method (p. 1).
- Part I: problem setup and uncertainty modelling (Sec. II), formulations (Sec. III), tractable reformulations and algorithms (Sec. IV), evaluation of solution quality (Sec. V). Part II: applications (SCOPF, chance-constrained OPF, reserve dimensioning, stochastic UC, transmission expansion, power-flow choice, hydro-thermal planning, large-consumer procurement). Part III: conclusions and outlook (pp. 1-2, 17).

## Setting
- **System:** mainly transmission-system-operator problems (p. 17). Hydro-thermal planning and consumer procurement are short sections.
- **Markets:** day-ahead unit commitment, reserves dimensioning (SOGL art. 157), spot/forward procurement.
- **Horizon and resolution:** generic two-stage; multistage mentioned for UC within a day and long-term planning (p. 2).

## Method
- **Model type:** review.
- **Generic problem (eq. 1, p. 2):** first-stage x (here-and-now), second-stage y (wait-and-see), risk operators R_cost and R_viol whose definition gives the different formulations.
- **Uncertainty representations (pp. 3-5, Fig. 1):** certainty equivalent (mean or mode) as a benchmark; perfect-information model as a benchmark; full probability distribution; distributionally robust ambiguity sets (moment- or Wasserstein-based); i.i.d. samples; discretised distributions (footnote: clustering is common for designing the scenario set, p. 5); robust uncertainty sets.
- **Formulations (pp. 6-8, Fig. 2):** risk-neutral expected cost (eq. 2); risk-averse with standard deviation, VaR, CVaR; DRO (eq. 3); robust min-max (eq. 4); single and joint chance constraints (eqs. 5-6); DR chance constraints (eqs. 7-8); robust constraints (eq. 9).
- **Algorithms (pp. 8-13):** sample-based finite formulation and scenario reduction (p. 9); affine and general recourse policies (p. 9, eq. 10); SAA (eq. 11, p. 9); subgradients and cutting planes (p. 10); Benders with master, subproblem, optimality and feasibility cuts, slack penalties for relatively complete recourse, UB/LB algorithm (pp. 10-11, eqs. 13-19); SDDP (pp. 11-12); dual decomposition (pp. 12-13, eqs. 20-24); progressive hedging (p. 13, eq. 25); column-and-constraint generation for robust problems (p. 13, eq. 26).
- **Evaluation (Sec. V, pp. 16-17):** split N samples into training (M) and testing (K > M) sets; in-sample solve; fix first-stage decisions and re-solve the second stage for each unseen sample (eq. 33); compare in-sample and out-of-sample objective values; benchmark against perfect information (EVPI) and certainty equivalent (VSS); out-of-sample runs can use more detailed constraints (e.g. AC instead of DC power flow) to test the effect of approximations.

## Data / case
- None (review; no numerical experiments).

## Key findings
- (p. 3) Listed uncertainty sources include the price of electricity and precipitation, "where ξ may represent the water inflow to a hydropower reservoir". The best representation depends on time scale and on the decision maker (a generation company sees others' bids as uncertain).
- (pp. 3-4) The certainty-equivalent model is often easier and can perform well, so it "can therefore provide an important benchmark" to judge whether a more complex representation is worthwhile. The perfect-information model is an unrealistic but useful bound/benchmark (p. 4).
- (p. 5) Historical time series are typically not i.i.d. because one step depends on the previous one. Discretised distributions are designed to reflect the underlying distribution and can reduce the number of samples; clustering is a common way to design the scenario set (footnote 1). Complicated dependence may need copulas or multivariate time-series models.
- (p. 6) The risk-neutral expected-value formulation is generally not the same as the certainty-equivalent problem, because E[f(x,y,ξ)] ≠ f(x,y,E[ξ]).
- (pp. 6-7) VaR is non-convex and not coherent; CVaR is convex and coherent and an upper bound on VaR; risk-averse formulations limit tail costs at the expense of higher expected cost.
- (p. 7) Robust formulations often assume relatively complete recourse; for DC power flow this can be ensured by allowing load shedding and curtailment.
- (p. 10) Convexity of the second-stage value function is critical for Benders convergence.
- (p. 11) If relatively complete recourse fails, use feasibility cuts from extreme rays, or slack variables penalised in the objective. The Benders UB comes from the subproblem at fixed x, the LB from the relaxed master; stop when UB - LB ≤ ε.
- (pp. 11-12) SDDP: blends cutting planes with Monte Carlo simulation; structure: stagewise decisions, linear coupling to the previous stage, linear constraints with uncertain inputs (a discretisation of uncertainty is needed); typical assumptions: right-hand-side uncertainty and serial independence, "although more general uncertainty structures can be handled as well" (citing Löhndorf and Shapiro 2019); backward passes refine convex cost-to-go approximations, forward passes sample uncertainty; choosing convergence criteria is non-trivial (citing Shapiro 2011); finite convergence in the linear case (citing Philpott and Guan 2008), but specific instances can have serious difficulty narrowing gaps (citing Shapiro et al. 2013); acceleration by regularisation and cut selection; highly parallelisable; open-source implementations in Matlab and Julia; "remains computationally complex and a topic of active research".
- (pp. 16-17) Out-of-sample simulation is "the most common approach" to evaluate solution quality irrespective of the method; a large in-sample/out-of-sample gap indicates the training set does not represent the uncertainty well.
- (p. 17) Part II focuses on the TSO perspective; generation-company (hydropower bidding/scheduling) and consumer views are covered less comprehensively, and much of the electricity-market, trading and load-management literature is not covered.
- (p. 20) Reserve dimensioning: European SOGL article 157 and industry practice motivate probabilistic sizing; without network constraints it reduces to estimating capacity-shortfall quantiles; with network constraints a chance-constrained problem.
- (pp. 20-21) Stochastic UC is typically a two-stage MILP solved with Lagrangian relaxation plus feasibility heuristics, PH, Benders or bundle methods; SDDP for a multistage version has been proposed (Zou et al.).
- (p. 24, Sec. XII) Inflow, with strong seasonal patterns, is the key hydropower uncertainty; this motivates yearly-horizon multistage SP, "with the most common algorithm being" SDDP, which has become the go-to methodology for medium- and long-term hydro-thermal planning in many countries. The key question is whether to spend water now or save it. The dual SDDP solutions give the "value of water" and are "as useful (if not more)" as the primal reservoir targets. SDDP has also been applied to day-ahead bidding of pumped-hydro plants (citing Löhndorf, Wozabal and Minner 2013), gas storage valuation, dairy farming, short-term operations and distribution grid restoration.
- (p. 24, Sec. XIII) Large-consumer procurement as two-stage SP with a mean-risk objective (eq. 37); spot price uncertainty is typically much larger than demand or fuel-cost uncertainty.
- (pp. 24-25) Modelling and algorithms go hand in hand; trade-offs between solution quality, probabilistic guarantees and tractability; "Solution evaluation is vitally important".
- (p. 25) Outlook: seasonal and yearly wind/solar variation (e.g. European wind drought of October 2021) and its correlation with load; high-impact low-probability events; interdependent systems; whether ancillary-service products remunerate assets that improve system stability; scalability (pp. 25-26); distributed optimisation; pricing of risk (p. 26).

## Strengths
- Authoritative, recent, power-systems-specific overview by leading authors; good for a single citation covering the landscape of methods.
- Very clear, method-agnostic out-of-sample evaluation recipe with EVPI and VSS (Sec. V).
- Explicit statement that SDDP is the go-to method for hydro planning and that its duals give water values (Sec. XII).

## Weaknesses / limitations
- Our copy is the PSCC/CORE author version; page numbers differ from the EPSR journal version.
- Hydro and storage are covered in one short paragraph; no Markov-chain SDDP, no PHS-specific modelling, no reserve-market participation from a producer's perspective.
- The evaluation recipe (Sec. V) is written for two-stage problems (fix x, re-solve the second stage); for a multistage policy one simulates the whole policy, which the paper does not spell out.
- Citation of Löhndorf et al. (2013) as "day-ahead bidding of pumped-hydro plants" (p. 24) not verified against that paper.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3 (Stochastic Optimisation): overview of SP, DRO, RO, chance constraints | Fig. 2 overview and Sec. III formulations | pp. 6-8, Sec. III |
| Theory 3: uncertainty sources in power systems incl. price and inflow | List of sources | p. 3, Sec. II-C |
| Theory / Model 6.x (Representation of Prices and Inflow): discretised distributions, clustering, non-i.i.d. time series | Sec. II-E and footnote 1 | pp. 3-5 |
| Theory 3 (Benders): master, cuts, UB/LB, feasibility cuts vs penalised slacks | Algorithm steps (0)-(3) | pp. 10-11, Sec. IV-B |
| Theory 3 (SDDP): structure, assumptions, convergence caveats, acceleration, parallelism | One-paragraph overview with refs [38]-[54] | pp. 11-12 |
| Theory: risk measures (VaR vs CVaR, coherence) if we discuss risk aversion | Definitions and pros/cons | pp. 6-7, Sec. III-B |
| Model 6.x (Evaluation on Unseen Weekly Data): in-sample vs out-of-sample | Training/testing split, eq. 33, interpretation of the gap | pp. 16-17, Sec. V |
| Model 6.x (Benchmark Comparisons): perfect information and certainty equivalent, EVPI and VSS | Benchmarks and definitions | pp. 3-4; p. 17 |
| Theory 3 (Water Value): SDDP duals give the value of water | Sec. XII | p. 24 |
| Literature review (modelling of PHS plants): SDDP as go-to for hydro planning | Sec. XII statement with refs | p. 24 |
| Background (markets/reserves): probabilistic reserve sizing in EU (SOGL art. 157) | Sec. VIII | p. 20 |
| Introduction/Background (LDES): need to model seasonal wind/solar variation, wind droughts | Outlook item 1 | p. 25, Sec. XV |

## Useful quotes (with page numbers)
> "Solution evaluation is vitally important in these applications" (p. 25)

Paraphrased: SDDP has become the go-to methodology for medium- and long-term hydro-thermal planning, and its dual solutions describing the value of water are as useful as, if not more than, the primal reservoir targets (p. 24). Out-of-sample simulation is the most common way to evaluate solution quality irrespective of the decision approach (p. 16).

## Follow-up references to check (backward snowballing)
- [38] Pereira (1989). Optimal stochastic operations scheduling of large hydroelectric systems. IJEPES 11(3).
- [41] Rebennack (2016). Combining sampling-based and scenario-based nested Benders decomposition methods: application to SDDP. Math. Programming 156.
- [42] Löhndorf and Shapiro (2019), EJOR 273 (in repo: `lohndorf2019`).
- [44] Shapiro, Tekaya, da Costa, Soares (2013). Risk neutral and risk averse SDDP. EJOR 224.
- [48] de Matos, Philpott, Finardi (2015). Improving the performance of SDDP. J. Comput. Appl. Math. 290.
- [49] Guigues (2017). Dual dynamic programming with cut selection. EJOR 258.
- [50] Löhndorf, Wozabal, Minner (2013). Optimizing trading decisions for hydro storage systems using approximate dual dynamic programming. Operations Research 61(4).
- [52] Pinto, Borges, Maceira (2013). Efficient parallel algorithm for large-scale hydrothermal operation planning. IEEE TPWRS 28(4).
- [241] Flach, Barroso, Pereira (2010). Long-term optimal allocation of hydro generation for a price-maker company. IET GTD.
- [88] Conejo, Carrión, Morales (2010). Decision Making Under Uncertainty in Electricity Markets. Springer.
- [246] Carrión, Philpott, Conejo, Arroyo (2007). Stochastic programming approach to electric energy procurement for large consumers. IEEE TPWRS 22(2).

