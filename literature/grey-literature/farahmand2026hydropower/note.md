---
bibkey: farahmand2026hydropower
bibkey_provisional: true
title: "Hydropower Scheduling Hierarchy and Water Values (lecture 6, TET4565 Electricity Markets and Energy System Planning, Specialisation Course)"
authors: "Hossein Farahmand"
year: 2026
venue: "NTNU lecture slides, autumn 2026; 40 slides. Not published; not in references.bib"
peer_reviewed: false
methods: [sdp, dynamic-programming]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: [anders]
added: 2026-11-11
takeaway: "Teaching slides on the Norwegian scheduling hierarchy (long-term 1-5 years, seasonal 3-18 months, short-term 1-2 weeks, detailed simulation 1-12 weeks; EMPS -> ProdRisk -> SHOP), the two equivalent objectives (cost minimisation in centralised systems, profit maximisation per company in decentralised markets), and the water value as the expected marginal value of stored water, derived by SDP with weekly stages and the dual of the reservoir balance."
source_path: C:/Users/Anders/Downloads/L06-Hydropower Scheduling Hierarchy and Water Values-1 (1).pdf
---

# Hydropower scheduling hierarchy and water values (Farahmand, lecture 6, 2026)

Lecture slides from TET4565, brought in by Anders on 2026-11-11 as a source on *perspectives* (the levels of the scheduling hierarchy). Slide 6 cites two sources: the course compendium in hydropower scheduling and Helseth & Geber de Melo (2020), *Scheduling Toolchains in Hydro-Dominated Systems*, SINTEF report. The published version of that report is in the library as `helseth2023hydropower`, which is the citable source for the same content. **Do not cite the slides in the thesis unless the group decides to** (lecture material, not peer-reviewed; see Q-005).

**Page convention:** slide number as printed at the bottom right (1–40).

## What it says

### Scheduling hierarchy (slides 5–7)
- Slide 5: scheduling tasks differ in time horizon, geographical scope and degree of detail; the Norwegian reservoir year has a depletion season, a filling season (max inflow around week 20–30) and a new depletion season.
- Slide 6 (from the compendium): four levels with horizons and model types.
  | Level | Horizon | Model type | Output passed down |
  |---|---|---|---|
  | Long-term scheduling | 1–5 years | stochastic models for optimisation and simulation | reservoir levels, marginal water values |
  | Seasonal scheduling | 3–18 months | stochastic or multi-scenario deterministic optimisation | marginal water values, reservoir boundaries |
  | Short-term scheduling | 1–2 weeks | deterministic optimisation | plans |
  | Detailed simulation | 1–12 weeks | non-linear simulation | verification of plans |
- Slide 7 (from Helseth & Geber de Melo 2020): long-term = EMPS (SDP with aggregation/disaggregation) giving a price forecast; medium-term = ProdRisk (SDP/SDDP) giving water values; short-term = SHOP (MIP/SLP) for portfolio bidding and production plans. Long-term applications: system analyses, expansion planning, maintenance planning. Going down the hierarchy: shorter horizon, less uncertainty, smaller system boundary, more detail. No horizon numbers on this slide.
- Slide 8: two equivalent objectives. Cost minimisation (minimise expected operational costs over time) in centralised markets (Brazil, Iceland, Norway before 1991). Profit maximisation in decentralised markets: market simulation gives prices, then profit maximisation per company.
- Slide 9: geographical scopes (figure only).

### Water values (slides 11–17)
- Slide 11: "The water value is the expected marginal value of having an additional unit of water in the reservoir"; found with SDP.
- Slides 12–15: deterministic hydro-thermal example; the water value equals the marginal cost of the thermal plant the hydro replaces (hydro replaces oil → 90 €/MWh); it falls with more stored energy and rises with more power capacity (25 MW/100 MWh → 50; 25 MW/300 MWh → 40; 100 MW/150 MWh → 90).
- Slides 16–17: dispatch rule with a known water value (315 NOK/MWh) and a price curve: produce at full capacity when price > water value, nothing when below.

### Water-value calculation by SDP (slides 19–39)
- Slides 19–21: two-stage DP recap (discretise the first-stage state, solve the second stage per trial value, interpolate the future-cost function, solve the first stage).
- Slide 22: multi-stage SDP: backward recursion over weeks and reservoir levels with uncertain inflow; the converged value function gives the long-run policy.
- Slides 23–24: SDP steps; cyclic annual sweeps until the marginal water values stabilise (stopping test on the change of the terminal FCF between iterations), then a separate forward simulation.
- Slide 25: SDP for an aggregated reservoir: stage = one week, state = reservoir volume discretised into 51 levels, decision = hydro production, return = operation-dependent cost; local system with thermal, firm power and spot exchange.
- Slides 26–29: nomenclature and formulation (weekly stages; grid import, rationing, production, reservoir level, spill; stochastic inflow; power balance with dual = marginal cost of operation; reservoir balance with dual = marginal value of stored water); Bellman form with intermediate cost plus FCF.
- Slides 30–35: Lagrangian; the water value equals the dual of the reservoir balance; optimality: water value = marginal cost of operation, which in a perfectly competitive market equals the price at the end of the period; envelope theorem gives dFC/dx = water value; same price next period without other binding constraints.
- Slide 36: reservoir and production limits drive a wedge between the prices of weeks t and t+1.
- Slides 37–39: discrete inflow outcomes with probabilities; water-value table by reservoir level and week, updated every annual iteration; iso-price curves as a function of reservoir level and week.
- Slide 40 (conclusions): long-term = strategic resource planning; short-term = operational optimisation and market participation; the water value links the economic and physical layers; SDP derives it by backward recursion; final water values underpin bidding, system planning and portfolio optimisation.

## Use for the thesis
- Background chapter: the hierarchy table (slide 6) and the EMPS → ProdRisk → SHOP chain (slide 7) match ch. 4; cite `helseth2023hydropower` (pp. 4–5) and `gjelsvik2010` (p. 35) for the same content.
- The two objectives (slide 8) are the system and owner perspectives of 5.2; cite `helseth2023hydropower` p. 7.
- The horizon numbers on slide 6 (seasonal 3–18 months; long-term from 1 year) differ from the Norwegian producer papers, which call 1–3 years of weekly stages "medium-term". See `knowledge/topics/scheduling-hierarchy-horizons.md`.

## Limitations
Teaching material; no references for the numbers beyond the compendium; the example water values are illustrative; no pumped storage.
