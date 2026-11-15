---
bibkey: hole2025capacity
bibkey_provisional: false   # in references.bib since 2026-11-15 (added through Zotero, key pinned)
title: "Capacity planning of renewable energy systems using stochastic dual dynamic programming"
authors: "Jarand Hole, Andy B. Philpott, Oscar Dowson"
year: 2025
venue: "European Journal of Operational Research 322(2), 573–588 (doi:10.1016/j.ejor.2024.12.031); filed copy is the arXiv preprint 2312.08556v1"
peer_reviewed: true
methods: [sddp-time-series, uncertainty-modelling]
review_sections: [reservoir-sizing-capacity, ldes-seasonal-storage, modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-15
takeaway: "Capacity (wind, peaker, HVDC) is optimised inside an infinite-horizon SDDP model of the New Zealand hydro system (JADE, SDDP.jl) by adding an investment node and a capacity state variable to a cyclic policy graph, so no finite horizon or end value is needed; one case includes the 1.5 GW / 5 TWh Lake Onslow pumped storage, where pumping is a release with a negative conversion factor."
---

# Capacity planning inside SDDP (Hole et al., 2025)

_Our copy is the **arXiv preprint v1** (13 Dec 2023, 32 pages); the article was published open access (CC BY) in EJOR 322(2), pp. 573–588. Page numbers below are **arXiv pages**; check the published version before quoting. Downloaded 2026-11-15 from arxiv.org/pdf/2312.08556._

## Research question / purpose
How can capacity investment be optimised together with the operating policy of a hydro-dominated system under inflow uncertainty, in one model that existing SDDP software solves without a custom decomposition (abstract, p. 1; contribution, pp. 3–4)?

## Setting
- **System:** New Zealand electricity system in a target year 2035, 11-node network, existing hydro reservoirs; three cases: **Onslow** (a pumped hydro storage of 1.5 GW and 5 TWh), **Peakers** (zero-emission peaker plant) and **Wind only** (pp. 12–13).
- **Markets:** none. System cost minimisation: fuel cost plus cost of shed load (Appendix A, p. 23).
- **Horizon and resolution:** infinite horizon, weekly stages in a yearly cycle; each week is split into load blocks of a load duration curve (168 hours in total) (p. 6, pp. 9–10).

## Method
- **Model type:** multistage stochastic linear program on a **cyclic policy graph** with one investment node in front (Figs. 2–3, pp. 6–7).
- **How uncertainty is represented:** weekly inflows, stagewise independent (Appendix A, p. 23); wind as a factor per load block that is linear in installed capacity (pp. 8–11). Demand and all other data are deterministic.
- **Solution method:** SDDP with SDDP.jl; training stopped at a fixed limit of 1000 iterations; the lower bound and the rolling mean of the forward-pass values are shown (pp. 15–16, Fig. 8). The policies are simulated over the 31 historical inflow years 1990–2020 (p. 17).
- **Key modelling choices and assumptions:**
  - A finite-horizon model needs very long horizons to limit end-of-horizon effects when it is used to estimate steady-state operating cost; the discounted infinite-horizon model avoids choosing a terminal cost function (p. 3, p. 6).
  - Weekly discount factor equal to the annual factor to the power 1/52; in the policy graph this is a probability of leaving to a zero-cost node (Appendix A, pp. 23–24). Annual factor 0.9 in the case (p. 14).
  - Investment is a state variable set once, before operation starts; with a finite lifetime the capacity is assumed reinvested, which scales the overnight cost (p. 7).
  - Wind capacity enters each weekly problem through a linear bound on wind generation per load block, fitted at five capacity levels (pp. 9–11).

## Model elements (Appendix A, pp. 23–26)
- **Sets:** weeks, network nodes, load blocks, plants, reservoirs, peaker plants and hydro plants per node, load types per node.
- **Parameters:** marginal cost of peakers; cost of shedding each load type; **conversion factor from water flow to power** per station; demand per node and block; hours per load block; plant capacity in m3/s; **spillway capacity**; reservoir capacity; incidence matrix of the river chain; feasible set of transmission flows.
- **Variables:** peaker generation, shed load, storage, hydro releases and spills per block, transmission flows.
- **Constraints:** demand balance per node and block; water balance over the river chain with inflow constant over the week; capacity bounds; in some cases minimum flows from environmental consents (p. 26).
- **Pumping:** "The same variables and constraints can be used to model pumping" with a negative conversion factor, since energy is consumed (p. 26). The pump is therefore a release arc with its own flow capacity; no separate pump efficiency parameter is shown.
- **Soft minimum level:** storage may fall below the consented operating minimum at a cost penalty (caption of Fig. 10, p. 19).

## Data / case
- JADE, open-source SDDP model distributed by the New Zealand Electricity Authority, written in Julia with JuMP and SDDP.jl (p. 12).
- Wind: LCOE 65 NZD/MWh, capacity factor 0.355, lifetime 20 years, giving 1.78 million NZD/MW overnight cost at an annual discount factor of 0.9 (p. 14).
- Benchmark: Philpott and Downward (2023) found the wind capacity by enumeration (`philpott2023using`).

## Key findings
- (p. 15, Fig. 7) The wind investment found inside SDDP approaches the values found by enumeration as the number of iterations grows.
- (p. 17, Table 2) With HVDC and peaker capacity also optimised: Onslow case 1315 MW wind and 643 MW HVDC, total 6761 MNZD; Peakers 1458 MW wind and 837 MW peaker, 5890 MNZD; Wind only 1997 MW wind, 8822 MNZD. The cost of building Onslow (15,700 MNZD) is not in these figures; with it the Onslow case costs 22,461 MNZD, almost four times the Peakers case.
- (p. 17) Extra HVDC capacity is most valuable with Onslow, because power must flow south for pumping and north when Onslow generates.
- (p. 21) In a few simulated weeks load shedding is very high with Onslow: the storage is needed but was emptied by a dry period the year before.
- (p. 21) Conclusion: under their assumptions a peaker plant supplements wind more cheaply than the pumped storage.

## Strengths
- Shows a way to choose capacity inside the SDDP model instead of re-solving it for each capacity (our plan for the pump capacity is re-solving).
- Infinite-horizon formulation with discounting as an alternative to an extended horizon or an end-volume requirement.
- Simulation on historical inflow years, separate from the sampling used in training.

## Weaknesses / limitations
- System cost minimisation with fixed demand, not a price-taking owner; no reserve markets.
- Inflows stagewise independent; hourly wind independent between hours (p. 8).
- Fixed iteration limit, no convergence test (p. 16).
- Load blocks instead of chronological hours, so short-term storage dynamics are not represented (p. 8).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Literature review 5.5: capacity of storage and generation chosen with SDDP | investment node and capacity state variable | pp. 6–7 |
| Literature review 5.5 / gap: pumped storage in an SDDP model | Onslow case; pumping as negative conversion factor | pp. 13, 26 |
| Model: end of horizon, alternatives to a terminal value | infinite-horizon cyclic graph; remark on long horizons | pp. 3, 6 |
| Model: weekly discount factor from an annual factor | Appendix A | pp. 23–24 |
| Method: evaluation on historical inflow years after training | 31 years 1990–2020 | p. 17 |
| Method: fixed iteration limit as stopping rule | 1000 iterations | p. 16 |

## Useful quotes (with page numbers)
> "forces models to use excessively long horizons to mitigate end-of-horizon effects" (p. 3, on finite-horizon models used for steady-state cost)

## Follow-up references to check (backward snowballing)
- Philpott & Downward (2023), JADE study of the Onslow pumped storage: filed as `philpott2023using`.
- Dowson & Kapelevich (2021), SDDP.jl, INFORMS Journal on Computing.
- Bødal, Botterud & Korpås (2022), capacity expansion with stochastic rolling-horizon dispatch, EPSR 205.
