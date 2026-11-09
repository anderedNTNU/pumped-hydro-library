---
bibkey: jacobson2023computationally
bibkey_provisional: true
title: "A Computationally Efficient Benders Decomposition for Energy Systems Planning Problems with Detailed Operations and Time-Coupling Constraints"
authors: "Anna Jacobson, Filippo Pecci, Nestor Sepulveda, Qingyu Xu, Jesse Jenkins"
year: 2023
venue: "INFORMS Journal on Optimization 6(1), 32-45 (Winter 2024; online 2 Aug 2023)"
peer_reviewed: true
methods: [benders-decomposition, deterministic-lp-milp]
review_sections: [reservoir-sizing-capacity]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Benders for deterministic capacity expansion: investments plus 'budgeting variables' for time-coupling policy constraints (CO2 cap, RPS) in the master, 52 independent weekly operational subproblems solved in parallel with one cut each (multicut); runtime linear in number of weeks; storage is circular within each 168-h week, so no inter-week storage."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/28_Jacobson_2023_Computationally_efficient_Benders_decomposition_for_energy_systems_planning.pdf
---

# Benders decomposition for energy systems planning (Jacobson et al., 2023/2024)

_Page mapping: PDF page n = journal page 31 + n (journal pp. 32-45; the last PDF page is an EBSCO copyright notice). Year: online 2023, issue 2024; the bibkey uses 2023 (provisional, check Zotero's date)._

## Research question / purpose
- Make large macro-energy capacity-expansion LP/MILPs with hourly operations and time-coupling constraints tractable via a Benders scheme that decouples operational timesteps (abstract, p. 32).

## Setting
- **System:** zonal US Eastern Interconnection, 2-19 zones; generation, storage and transmission investment and retirement plus hourly dispatch, aggregated UC (relaxed), ramping (pp. 34-35).
- **Markets:** central planner, least cost; no market participation.
- **Horizon and resolution:** single planning year, hourly, 2 to 52 representative weeks (8,736 h for 52 weeks) (p. 34).

## Method
- **Model type:** deterministic LP or MILP (integer investments) (p. 33).
- **Uncertainty:** none (perfect foresight).
- **Solution method:** Benders with investments and budgeting variables q_w (each week's share of an annual CO2/RPS budget) in the master; weekly operational subproblems fully decoupled, solved in parallel, one cut per subproblem per iteration (pp. 34, 36-37). Compared with monolithic solves and a standard Benders with one full-year subproblem.
- **Key modelling choice:** storage and UC are "circular" within each 168-hour week, i.e. weeks are decoupled (p. 35). The authors note the budgeting idea "should be extensible to ... long-duration storage state-of-charge or hydro reservoir levels", but this is not implemented (p. 37).

## Data / case
- Eastern US data, three policy scenarios (reference, RPS 70%, CO2 cap) (p. 35).

## Key findings
- (pp. 40-41) Runtime grows linearly with the number of weeks and quadratically with zones; more weeks -> more cuts per iteration -> fewer iterations.
- (p. 41) Decomposed scheme beats monolithic for all MILPs with more than 2 weeks; for LPs only for larger instances; standard (non-decoupled) Benders is intractable beyond 22 weeks.
- (pp. 42-43) Too few representative weeks gives large errors in capacity recommendations, especially for storage (up to ~600 MW average deviation per site).
- (p. 43) The reformulation with budgeting variables is the main contribution.

## Strengths
- Clear demonstration that multicut, time-decoupled Benders scales; useful computational evidence that temporal aggregation biases storage investment.

## Weaknesses / limitations
- Deterministic; storage decoupled between weeks, so seasonal / long-duration storage value is not captured (acknowledged only as future extension, p. 37).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: Benders, application in energy planning | Investment master + parallel operational subproblems, multicut | pp. 36-37, Sec. 3 |
| Lit. review: sizing/investment models ignore inter-week storage | Circular indexing per 168 h week | p. 35 |
| Lit. review / motivation: temporal aggregation biases storage investment | MSE of capacity vs number of weeks | pp. 42-43, Fig. 6 |
| Discussion: extending budgeting variables to reservoir levels | Authors' remark | p. 37 |

## Useful quotes (with page numbers)
> "For the work in this manuscript, subperiods are one week long; circular indexing occurs over a 168-hour time period." (p. 35)

## Follow-up references to check (backward snowballing)
- Lohmann and Rebennack (2017), tailored Benders for generation expansion planning.
- Sepulveda (2020), nested decomposition for planning (MIT PhD thesis).
- Mallapragada et al. (2020), representative periods and storage.

