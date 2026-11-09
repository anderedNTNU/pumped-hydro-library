---
bibkey: seranilla2023applications
bibkey_provisional: true
title: "On the Applications of Stochastic Dual Dynamic Programming"
authors: "Bonn Kleiford Seranilla"
year: 2023
venue: "PhD dissertation, University of Luxembourg (PhD-FDEF-2023-035), supervisor Nils Löhndorf; defended 13 October 2023"
peer_reviewed: false
methods: [sddp-markov-chain, sddp-time-series, benders-decomposition, multistage-scenario-trees, uncertainty-modelling]
review_sections: [modelling-phs-plants, research-gap]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "PhD thesis on SDDP: Ch. 1 is a tutorial (MSP, stagewise-independent vs Markovian processes, SAA, Markov-chain lattices via optimal quantization, Benders → L-shaped → nested Benders → SDDP algorithm), Ch. 2 is the SDDP application survey (same as seranilla2025), Ch. 3 is MSPLib/MSPFormat with a QUASAR vs SDDP.jl vs MSPPy benchmark; Chs. 4-5 (vaccine facility location, SDDiP) are not relevant to us."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDDP_i_vannkraft/Seranilla2023.pdf"
---

# On the applications of SDDP, PhD thesis (Seranilla, 2023)

_Page mapping: 189 PDF pages (pdftotext finds 185 page breaks). Front matter is unnumbered; **thesis page p = PDF page p + 14** (Chapter 1 starts on PDF page 15 = thesis p. 1). Page numbers below are printed thesis pages._

_Bibkey note: not in `references.bib`; key generated Better BibTeX style (stop words "On", "the" skipped → "applications"). Needs adding to Zotero if we cite it. For the survey content prefer `seranilla2025` (the co-authored preprint version of Ch. 2)._

_Reading scope (long document): read in full Ch. 1 (pp. 1-25), Ch. 2 (pp. 27-54, checked against seranilla2025), Ch. 3 (pp. 55-83 plus Appendix 3.A pp. 85-88) and Ch. 6 conclusion (pp. 149-150). Chs. 4-5 (COVID-19 vaccine facility location under flood risk, MSFLPD, SDDiP vs shadow price approximation) only skimmed via the abstract, TOC and conclusion; not relevant to our thesis._

_Tagging note: methods tags reflect Ch. 1 (Markov-chain lattice and AR discretisation, Benders lineage, scenario trees vs lattices). Review tags reflect Ch. 2 (same survey as seranilla2025)._

## Research question / purpose
- Showcase applications of SDDP for sequential decision making under uncertainty across domains (abstract, p. iii; p. 1).
- Ch. 1: introduce MSPs, solution techniques and the history of SDDP (pp. 1-25). Ch. 2: survey SDDP applications and adoption barriers (pp. 27-54). Ch. 3: MSPLib (problem library) and MSPFormat (JSON data format) for benchmarking SDDP implementations (pp. 55-95). Chs. 4-5: SDDiP and a new shadow price approximation (SPA) for multistage facility location under disruption (pp. 97-148).

## Setting
- **System:** generic MSPs; hydro-thermal scheduling used as the running SDDP example (simplified single-reservoir hydro-thermal problem in MSPLib, p. 61; Brazilian system p. 66; European EDF problem p. 68; 3-plant cascade p. 70).
- **Markets:** MSPLib includes Löhndorf and Wozabal's multi-market (day-ahead plus intraday) grid-storage bidding problem and a gas-storage valuation problem (p. 69).
- **Horizon and resolution:** varies by instance (e.g. simplified hydro-thermal T = 4 to 100 stages, p. 61).

## Method
- **Model type:** thesis combining tutorial, survey, software/benchmark and new algorithm.
- **How uncertainty is represented (Ch. 1, pp. 2, 6-8):**
  - Stagewise independent vs Markovian definitions (p. 2, p. 6).
  - Stagewise-independent processes discretised by SAA (Kleywegt et al. 2002); required N grows linearly with decision dimension; convergence rate depends on conditioning (pp. 6-7).
  - Markovian processes: (i) Markov-chain discretisation by optimal quantization, eq. 1.10, minimising expected p-norm distance to K_t quantizers per stage; Voronoi cells around the means become nodes of a lattice; discretisation error relates to stagewise Wasserstein distance; solvable by SAA, stochastic approximation (Bally and Pagès 2003) or robust SA (Nemirovski et al. 2009); refers to Ding (2020) (p. 7). (ii) First-order AR model of RHS uncertainty, eq. 1.11, which makes the errors stagewise independent so SAA applies (p. 7), with details in Löhndorf and Shapiro (2019).
  - Scenario tree vs lattice: a lattice is a recombining tree where nodes can have several predecessors (p. 8, Figs. 1.1-1.2); Gorski (2017) compares them.
- **Solution method (Ch. 1):** deterministic equivalent (eqs. 1.5-1.9, p. 5); Lagrangian decomposition and progressive hedging (pp. 9-10); Benders decomposition with steps (pp. 12-13); L-shaped with optimality and feasibility cuts (pp. 14-16); nested Benders with ascend/descend sequencing heuristics and abridged nested decomposition (pp. 17-19); SDDP forward simulation and backward pass with cut sharing, Algorithm 1 taken from Ding (2020) (pp. 20-22); enhancements: periodic/infinite-horizon SDDP (Shapiro and Ding 2020), non-block-diagonal structure via state expansion, risk aversion, infinite support (Guigues 2016), stagewise dependence (Löhndorf and Shapiro 2019) (pp. 21-23); SDDiP (p. 23).
- **Ch. 3 benchmark design (pp. 59, 76-77):** instances classed easy (15-25 iterations to converge), medium (50-70), difficult (>80); discretisations of 100, 200, 300 realisations per stage; criteria: iteration limit, time limit, parallel processing (1 vs 32 cores).

## Data / case
- MSPLib synthetic problems (simplified hydro-thermal, air-conditioner production, electricity planning, newsvendor, semiconductor, farmer, asset management, generation expansion, flower seller, inventory with lead time; pp. 60-66) and real-world problems (Brazilian hydro-thermal SWI and AR/MC variants, production-inventory with renewables, European hydro-thermal, dairy farm, grid-storage multi-market bidding, gas storage, multi-echelon lot sizing, hydro cascade, American put; pp. 66-70). Repository: github.com/bonnkleiford/MSPLib-Library (p. 57).
- Appendix 3.A (pp. 85-88): full MSPFormat JSON of the 3-stage simplified hydro-thermal problem: reservoir volume (state, ub 200), thermal generation (stage costs 50, 100, 150), hydro generation, spill, demand 150; lattice with inflow 0/50/100 and transition probabilities 1/3 to each successor.

## Key findings
- (p. 2) Markovian process: conditional distribution of ξ_t given the full history equals that given ξ_{t-1}; state variables carry the system from stage to stage, control variables are stage-local.
- (p. 3) DP reformulation with expected cost-to-go V_{t+1}(x_t, ξ_t) := E[V_{t+1}(x_t, ξ_{t+1}) | ξ_t] (eqs. 1.2-1.3): for Markovian data the cost-to-go depends on the current random state.
- (pp. 5-6) Deterministic equivalent grows exponentially with scenarios and stages (curse of dimensionality).
- (p. 7) Markov-chain discretisation via optimal quantization produces a lattice whose error depends on the stagewise Wasserstein distance.
- (p. 8) Lattices (recombining trees) vs classical scenario trees.
- (pp. 10-11) Lagrangian decomposition splits by scenarios, NBD by nodes; NBD needs less memory upfront but more later; PH is not paired with sampling.
- (p. 21) Cuts can be shared across scenarios because of convexity; SDDP iterates until lower bound and policy value (upper bound) converge or a stopping criterion is met; SDDP avoids the DP curse of dimensionality because state discretisation is not necessary.
- (p. 22) Stagewise independence creates a single cost-to-go function per stage; convergence proof by Philpott and Guan (2008).
- (pp. 27-54) Survey: identical in substance to seranilla2025 (186 papers to Dec 2022, p. 33; end-of-horizon effect and horizon doubling, p. 38; medium-term with prices, p. 39; markets and trading, p. 41; storage, p. 43; 4 state variables in the Brazilian case, p. 49; MC approach "has no convergence guarantees", p. 50; 76% energy and 60% hydro-thermal, p. 52).
- (pp. 67-68) Löhndorf and Shapiro's Markov-chain approach allows any parameter to be Markovian, permitting a "much broader range of stochastic models which may better represent the true process" than the AR approach, which adds state variables.
- (p. 69) Grid-storage multi-market bidding (Löhndorf and Wozabal 2023): a coordinated policy that reserves capacity for intraday is optimal; deviation from a sequential policy grows with intraday price volatility and liquidity.
- (pp. 78-83) QUASAR (commercial, Quantego) beat SDDP.jl and MSPPy on all criteria: e.g. for 105 easy instances QUASAR solved all within about 350 s, versus about 65 for the others in that time; SDDP.jl needed about 6,000 s and MSPPy about 12,000 s for all (p. 78). SDDP.jl did not support parallel processing for MSPFormat at the time (p. 80). Only QUASAR could run the storage-bidding and gas-storage instances (pp. 80-81). Note: author's supervisor developed QUASAR (p. 57), so this is not an independent comparison.
- (p. 149) Conclusion restates that at least 75% of SDDP works exploit hydro-thermal scheduling (inconsistent with the ~60% hydro-thermal / 76% energy split given on p. 52).

## Strengths
- Ch. 1 is a compact, self-contained tutorial with explicit algorithm statements (Benders, L-shaped, NBD, SDDP) and a clear Markov-chain lattice definition; good for explaining our Theory chapter in our own words.
- Appendix 3.A gives a concrete, minimal hydro-thermal SDDP instance with a Markov lattice and transition probabilities, useful as a teaching example or unit test for our implementation.
- MSPLib is an open benchmark that includes Markovian hydro instances and a storage multi-market bidding instance.

## Weaknesses / limitations
- Not peer reviewed; Ch. 2 duplicates the preprint.
- Benchmark is not independent (QUASAR is developed by the supervisor's company; p. 57, p. 75) and reports aggregate figures only.
- Editing inconsistencies: chapter order differs between abstract (Ch. 4 vaccine, Ch. 5 MSFLPD; p. iii-iv), Sec. 1.3.6 (pp. 24-25, Ch. 4 described twice) and the conclusion (pp. 149-150); Benders Step 6 says "If UB = LB, add Benders cut" (p. 13), which should be "≠"; 75% vs 60% hydro-thermal share (p. 149 vs p. 52).
- Same unreferenced claims as the survey (MC approach without convergence guarantees; horizon doubling).
- "Through a few iterations, the upper and lower bounds converge" (p. 21) overstates practice.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3 (Multistage): MSP formulation, state vs control variables, stagewise independent vs Markovian | eq. 1.1 and definitions | pp. 2-3, Sec. 1.1 |
| Theory 3 (Markov Representation): Markov-chain discretisation by optimal quantization, Voronoi cells, lattice | eq. 1.10 | p. 7, Sec. 1.2.2 |
| Theory 3 (Time-series Representation): AR(1) RHS and SAA | eq. 1.11 | p. 7 |
| Theory 3: scenario tree vs lattice (recombining tree) | Figs. 1.1-1.2 | p. 8 |
| Theory 3 (Benders, L-shaped, nested Benders): algorithm steps | Secs. 1.3.1-1.3.3 | pp. 12-19 |
| Theory 3 (SDDP): forward/backward pass, cut sharing, Algorithm 1 | Sec. 1.3.4 | pp. 20-22 |
| Theory 3 (SDDP extensions): periodic SDDP, risk aversion, infinite support, dependence | Sec. 1.3.5 | pp. 21-23 |
| Method (implementation choice): QUASAR vs SDDP.jl vs MSPPy | Ch. 3 benchmark | pp. 75-83 |
| Model validation: toy hydro-thermal Markov lattice instance | Appendix 3.A JSON | pp. 85-88 |
| Literature review: SDDP application survey | Ch. 2 (prefer citing seranilla2025) | pp. 27-54 |

## Useful quotes (with page numbers)
> "A lattice is a recombined scenario tree where each node can have multiple predecessor nodes." (p. 8)

## Follow-up references to check (backward snowballing)
- Ding, L. (2020). Multistage stochastic programming (PhD thesis, Georgia Tech) and Ding, Ahmed, Shapiro (2019) MSPPy.
- Gorski (2017). Comparison of classic scenario trees and lattices (unverified details).
- Bally and Pagès (2003). A quantization algorithm for solving multidimensional discrete-time optimal stopping problems. Bernoulli.
- Löhndorf and Wozabal (2023). The value of coordination in multimarket bidding of grid energy storage. Operations Research (unverified title).
- Shapiro and Ding (2020). Periodical multistage stochastic programs (in repo inbox: `shapiro2020`).
- Donohue and Birge (2006). Abridged nested decomposition.
- Murphy (2013). Benders, nested Benders and stochastic programming: an intuitive introduction (in inbox).
- Dowson and Garcia (2020). StochOptFormat.

