---
bibkey: elgersma2026
title: "Tight MIP Formulations for Optimal Operation and Investment of Storage Including Reserves"
authors: "Maaike B. Elgersma, Germán Morales-España, Karen I. Aardal, Niina Helistö, Juha Kiviluoma, Mathijs M. de Weerdt"
year: 2026
venue: "IEEE Transactions on Power Systems 41(4), 2428-2440"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [modelling-phs-plants, market-participation, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Derives the single-period convex hull (tightest MIP / best LP relaxation) for storage operation, operation with up/down reserves, and investment plus operation with reserves; embedded multi-period, the LP relaxations reduce (not eliminate) simultaneous charging/discharging and the tight MIP solves faster; also flags that the common reserve formulation under-uses storage flexibility."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/elgersma2026.pdf
---

# Tight MIP formulations for storage incl. reserves (Elgersma et al., 2026)

_Page mapping: PDF page n = journal page 2427 + n (journal pp. 2428-2440). Open access (CC BY 4.0). Proofs of most tight models are in an online companion (ref. [23])._

## Research question / purpose
- Large energy-system models relax storage integrality to LP, which allows simultaneous charging and discharging; find tighter MIP formulations whose LP relaxation is the convex hull for one period, including reserves and investments (pp. 2428-2430).

## Setting
- **System:** generic storage unit (pumped hydro named as an example, p. 2428) embedded in UC and transmission expansion planning (TEP) case studies taken from Arroyo et al. 2020 (p. 2434).
- **Markets:** up/down reserve capacity as in power-system scheduling, no market prices.
- **Horizon and resolution:** single period for the theory; 2 h and 4 h x 365 = 1460 periods in the case studies (pp. 2434-2436).

## Method
- **Model type:** MILP storage models: BO-MIP (basic operation, eqs. 1a-1f), BOR-MIP (with reserves, eqs. 2a-2i), BIR-MIP (investment and operation with reserves, eqs. 3a-3j) (pp. 2430-2432). Reserve energy bounds (2a)-(2b): state of charge must leave room for reserve delivery over the period, scaled by efficiencies (p. 2431).
- **Solution approach:** convex hull of the two disjunctions (charging/discharging) via Balas' disjunctive programming, projected with Fourier-Motzkin elimination, redundant constraints removed (p. 2432). Parameter conditions: charge/discharge and reserve capacities cannot exceed what fits in storage in one period; efficiencies in (0, 1] (p. 2432).
- **Implementation:** Julia/JuMP, Gurobi 10.0.2 (p. 2434).

## Data / case
- UC and TEP instances from Arroyo et al. (2020), adapted with reserve requirements (>= 1 MW; or >= 10% of demand) and storage investment (pp. 2434-2435). Multi-period UC: 1460 periods (p. 2435).

## Key findings
- (p. 2429) Binary variables are required to model reserves correctly and to forbid simultaneous charging/discharging; LP relaxations used in decomposition schemes can cause significant errors because the LP is solved many times.
- (p. 2429) Simultaneous charging/discharging is sometimes beneficial in an LP (e.g. negative prices) and in some systems (composite batteries, multiple/fast units) it may actually be executable.
- (p. 2431) The common BOR reserve formulation "does not fully exploit the flexibility of a storage unit" (details in Appendix B1).
- (pp. 2434-2435) Tight LPs (TO-LP, TOR-LP, TIR-LP) prevent simultaneous charge/discharge in the 2-period cases where the basic LPs do not; with reserves some error remains (down reserve from charging while discharging, p. 2435).
- (pp. 2435-2436) In 1460-period UC the tight MIP explores fewer nodes and solves faster; the tight LP has a slightly better bound and less than half the simultaneous charge/discharge of the basic LP.
- (p. 2436) Multi-period convex hull remains open; suspected exponential growth with periods.

## Strengths
- Rigorous (proved convex hulls); covers reserves and investment, which most storage-tightening work ignores.

## Weaknesses / limitations
- Single-period tightness only; deterministic; small illustrative cases; generic battery-like storage without head effects, inflow or separate pump/turbine units.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model assumptions: simultaneous pump/generation (`06_mathematical_model.tex:59`) | Exception: multiple/fast units can execute it; otherwise LP artefact | p. 2429, Sec. I-B |
| Model: reserve energy margins in storage | Reserve-adjusted state-of-charge bounds (2a)-(2b) | p. 2431, Sec. II-B |
| Method: why SDDP/LP subproblems may show simultaneous operation | Decomposition solves LP relaxations repeatedly -> errors | p. 2429 |
| Lit. review: market participation, reserves from storage | Up/down reserves when charging or discharging | p. 2431 |
| Lit. review: sizing, investment in charge/discharge/energy capacity | BIR-MIP with separate c, d, e investments | pp. 2431-2432, eqs. (3a)-(3j) |

## Useful quotes (with page numbers)
> "Binary variables are required to correctly model reserves and to ensure that the storage cannot charge and discharge simultaneously" (p. 2429)

## Follow-up references to check (backward snowballing)
- Pozo (2022/2023), convex hull formulations for storage (ref. [18]; check exact year).
- Baldick et al., tighter formulation for pumped-storage hydro (ref. [17]).
- Liu et al. (2021), secured reserve scheduling of pumped-storage hydropower in ISO day-ahead market, IEEE TPWRS 36(6) (ref. [21]).

