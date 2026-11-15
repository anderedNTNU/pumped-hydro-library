---
bibkey: helseth2018optimal
bibkey_provisional: true    # not in references.bib yet (Zotero was not running 2026-11-15); key follows the Better BibTeX pattern
title: "Optimal Hydropower Maintenance Scheduling in Liberalized Markets"
authors: "Arild Helseth, Marte Fodstad, Birger Mo"
year: 2018
venue: "IEEE Transactions on Power Systems, 33(6), 6989–6998 (doi:10.1109/TPWRS.2018.2840043)"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, benders-decomposition, uncertainty-modelling]
review_sections: [market-participation, modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-15
takeaway: "Benders decomposition that coordinates binary maintenance timing (MILP master) with the hybrid SDP/SDDP medium-term model of helseth2016 for a price-taking Norwegian watercourse selling energy and symmetric spinning reserve capacity; the weekly LP, the reserve constraints and the 10 % reserve limit are the same as in helseth2016, and the case uses upper-bound stabilisation as the stopping rule."
---

# Hydropower maintenance scheduling with hybrid SDP/SDDP (Helseth et al., 2018)

_Our copy is the **accepted manuscript** from the Norwegian research archive (NVA, CC BY-NC-ND), paginated 1–10; the published version is IEEE TPWRS 33(6), pp. 6989–6998. Page numbers below are **manuscript pages**. Downloaded 2026-11-15 from hdl.handle.net/11250/2598137._

## Research question / purpose
When should a profit-maximising, price-taking, risk-neutral hydropower producer take plants out for preventive maintenance, when the lost income depends on uncertain inflow and on uncertain prices for energy and reserve capacity (abstract, p. 1; p. 2)? The paper coordinates the maintenance decision with the medium-term scheduling model instead of treating the two separately.

## Setting
- **System:** Norwegian watercourse with 7 reservoirs and plants, 986 MW (p. 7, Fig. 3). Conventional hydropower, **no pumping**.
- **Markets:** energy and reserve capacity, price-taker in both; allocated capacity "should be spinning and symmetric" (p. 7). No activation of reserves.
- **Horizon and resolution:** 2 years, weekly decision stages, 21 time steps per week (p. 7). Maintenance of 3 consecutive weeks within weeks 15–45 (p. 8).

## Method
- **Model type:** multistage stochastic MILP. A master problem (MS) holds the binary maintenance schedule; the hydropower scheduling problem (HPS) is a multistage LP (eqs. 1–3, pp. 3–5).
- **How uncertainty is represented:** weekly average energy and reserve capacity prices in a discrete Markov chain of price clusters; weekly inflow from a lag-1 autoregressive model. Price is assumed independent of inflow, which the hybrid method requires; the authors say a significant correlation between local inflow and average price is hard to find for a single watercourse (p. 6).
- **Solution method:** Benders decomposition between MS and HPS; the HPS is solved by the hybrid SDP/SDDP method (refs. to Gjelsvik 1999 and Pereira 1999). Cuts are built and stored **per price cluster** and shared among system states within a week and price cluster (p. 6, p. 7). The maintenance decisions enter the HPS cuts as extra state variables (eqs. 4–5, p. 5).
- **Bounds and stopping:** upper bound from the master problem, lower bound from the forward simulation; convergence can formally be declared when the upper bound lies within a confidence interval of the lower bound (p. 6). In the case study that test was sensitive to the case and the number of scenarios, error terms and price clusters, so **stabilisation of the upper bound** was used instead, with reference to Shapiro 2011 (p. 8).
- **Key modelling choices and assumptions:** concave generation function by discharge segments; spillage without upper bound acts as slack so that every state is feasible (p. 7); end-of-horizon value from cuts taken from initial runs with a four-year horizon, the same cuts for all cases (p. 7).

## Model elements (weekly HPS subproblem, eq. 10, p. 6)
- **Sets:** reservoirs/stations H; discharge segments S_h; time steps K within the week; stages T; maintenance window T^R; scenario-tree nodes N; price clusters p; cut sets per price cluster; upstream reservoirs of h (nomenclature, p. 1).
- **Parameters:** max generation capacity per station (MW); max and min reservoir volume per time step; max capacity sales per station (MW); duration of each time step; **scaling factors that turn the weekly average energy and capacity price into a price per time step** (expected profiles); energy equivalent per discharge segment (MWh/Mm3); max discharge per segment; max bypass; maintenance duration (pp. 1–2).
- **Variables:** generation, allocated reserve capacity, volume, discharge per segment, spillage, bypass, future expected profit, binary maintenance (pp. 1–2).
- **Constraints:** water balance with upstream discharge, spillage and bypass (10b); generation as the sum of segment discharges times energy equivalents (10c); **spinning requirement**: capacity sold cannot exceed what is already generating (10d); generation plus capacity within installed capacity (10e); **enough water in the reservoir to deliver the up-regulation at the lowest efficiency for the whole time step** (10f); cuts (10g); no discharge during maintenance (10i); reservoir, bypass and capacity-sales bounds (10j–10l).

## Data / case
- Prices from the EMPS model on a Nordic system description with 80 historical inflow years and reserve constraints per price zone; 80 energy and reserve price scenarios; **6 price nodes per stage (3 energy × 2 capacity price clusters)**, built as in helseth2016 (p. 7).
- Inflow: lag-1 autoregressive model fitted to one series of 80 historical years, normal errors (p. 7).
- 200 scenarios re-sampled in each forward iteration; 12 inflow error terms per stage in the backward iteration (p. 7).
- **Max 10 % of each plant's installed capacity to the reserve market** (p. 7).
- C++ with Gurobi 7.5 (p. 7).

## Key findings
- (p. 8, Table I) Four cases. With energy and capacity sales the two plants in series are maintained together in weeks 42–44; with energy only in weeks 29–31. Higher reserve capacity prices in summer make it profitable to postpone maintenance to autumn.
- (p. 8, Table I) Iterations and time: 340 iterations / 168 h (A), 323 / 81 h (B), 40 / 20 h (C, no maintenance), 520 / 263 h (D). The column order was read from the layout text and matches the per-iteration times (our reading).
- (p. 8) Maintenance slows convergence; a stable schedule over several iterations is needed before the cuts are built around it.

## Strengths
- Same weekly model as helseth2016 with a full nomenclature, so sets, parameters and constraints are easy to compare with ours.
- States openly why the confidence-interval stopping test was abandoned in practice.

## Weaknesses / limitations
- Very long run times (20–263 hours).
- No sensitivity on the number of forward scenarios (p. 9).
- No pumping; reserve activation and its energy are not modelled.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model: reserve constraints (spinning, capacity, water for up-regulation) | eqs. (10d)–(10f) with explanation | pp. 6–7 |
| Model: 10 % reserve limit per plant | case setting | p. 7 |
| Method: cuts stored per price cluster | hybrid SDP/SDDP description | pp. 6–7 |
| Method: stopping on a stable upper bound instead of the confidence-interval test | reason given | p. 8 |
| Method: end-of-horizon value from cuts of a longer run | case description | p. 7 |
| Data: price clusters from EMPS scenarios (3 energy × 2 capacity) | case description | p. 7 |
| Literature review 5.6: SDDP applied to a producer's investment-like decision | maintenance timing by Benders + SDDP | pp. 2–5 |

## Useful quotes (with page numbers)
> "Allocated capacity should be spinning and symmetric." (p. 7)

## Follow-up references to check (backward snowballing)
- Infanger & Morton (1996), cut sharing with interstage dependency (their [32]).
- Street, Brigatto & Valladão (2017), co-optimisation of energy and ancillary services in hydrothermal planning (their [11]).
