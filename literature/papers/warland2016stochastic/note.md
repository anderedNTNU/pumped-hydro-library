---
bibkey: warland2016stochastic
bibkey_provisional: true
title: "Stochastic optimization model for detailed long-term hydro thermal scheduling using scenario-tree simulation"
authors: "Geir Warland, Birger Mo"
year: 2016
venue: "Energy Procedia 87, 165–172 (5th International Workshop on Hydro Scheduling in Competitive Electricity Markets)"
peer_reviewed: true
methods: [two-stage-stochastic, benders-decomposition, sdp, heuristics-simulation]
review_sections: []
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/74_Warland_2016_Stochastic_optimization_detailed_long_term_hydrothermal_scheduling_scenario_tree_simulation.pdf"
takeaway: "SINTEF case study: the prototype SOVN model (scenario-fan two-stage LPs solved by Benders, detailed hydro) gives more hydro output, less spillage and higher surplus than the EMPS model (aggregate SDP + heuristic drawdown) on a 4-area test system."
---

# SOVN vs EMPS: detailed long-term hydrothermal scheduling (Warland & Mo, 2016)

> **Page convention.** Journal page = PDF page + 164 (PDF p. 1 = p. 165, PDF p. 8 = p. 172). Workshop proceedings, peer review "under responsibility of SINTEF Energi AS" (p. 165).

## Research question / purpose
Compare the established Nordic market-simulation model **EMPS** (aggregate hydro, SDP + heuristics) with a new SINTEF prototype, **SOVN**, which uses formal stochastic optimisation with a detailed hydro representation, in terms of hydro scheduling, prices and socio-economic surplus (p. 165).

## Setting
- **System:** fictitious 4-area hydrothermal test system; areas 1–3 each have a real, complex Norwegian watercourse (50 hydro modules in total); area 4 is thermal + wind without hydro (pp. 169–170).
- **Markets:** system-wide market clearing (socio-economic surplus maximisation / expected cost minimisation); no individual producer, no reserves.
- **Horizon and resolution:** 3 years (156 weeks), weekly stages, 4 load periods per week; 38 historical weather years (p. 170). EMPS in general: weekly time step, horizon up to 25 years, intra-week resolution ≥ 1 h (p. 167).

## Method
- **Model type:**
  - *EMPS:* strategy part computes incremental water values per area with SDP on aggregated reservoirs, coupled across areas by an iterative heuristic market description; simulation part clears the market weekly by LP with water values as hydro marginal costs, and distributes aggregate production to plants with a rule-based drawdown model (pp. 167–168).
  - *SOVN:* simulates a sequence of "scenario fan problems" (SFP). Each SFP is a two-stage stochastic LP: stage 1 = the current week with known stochastic values; stage 2 = the remaining horizon under scenarios taken from historical weather records, with an AR(1)-based smoothing from the first-stage state. Only the first week's decision is used (rolling horizon) (p. 168).
- **How uncertainty is represented:** historical weather (inflow, temperature, etc.) scenarios; in SOVN as a scenario fan (two-stage), in EMPS via SDP on aggregate reservoirs.
- **Solution method:** SFP solved by Benders decomposition (L-shaped): first-stage LP gives initial reservoirs, each scenario LP returns a cut (p. 169, Fig. 4).
- **Key modelling choices and assumptions:** detailed reservoir balances per module in SOVN; aggregation + disaggregation in EMPS. Both minimise expected system cost.

## Data / case
Tables 1–3 (pp. 169–170): firm load 1,000–2,925 GWh/yr per area; transfer capacities 100–200 MW; aggregate hydro 535–820 MW and 1,530–2,860 GWh reservoir per hydro area; price-dependent thermal supply in steps.

## Key findings
- (pp. 170–171, Fig. 6) Both models give similar aggregate reservoir trajectories.
- (p. 171, Table 4) SOVN − EMPS over 156 weeks: +787 GWh hydro, −605 GWh spillage, −672 GWh thermal, +41.1 Mkr socio-economic surplus.
- (p. 172, Figs. 7–8) SOVN prices are lower, because more hydro displaces a few large thermal units in area 4 and EMPS has more curtailment.
- (p. 172) Conclusion: replacing aggregation and heuristics with formal optimisation gives better utilisation of hydro and is expected to suit investment analysis better; more testing needed on real systems.
- (p. 166) Motivation: more short-term price variation will "increase use of pumped storage plants and open for investment in new pumping capacity", and existing detailed models do not capture the link between short-term variability and pumped-hydro operation.

## Strengths
- Clear description of the EMPS logic (strategy vs simulation, water values per area, rule-based drawdown), useful as background on Nordic practice.
- Illustrates the value of formal optimisation over aggregation heuristics with concrete numbers.

## Weaknesses / limitations
- Short workshop paper; a full description is deferred to "a future paper" (p. 166).
- Fictitious test system; SOVN lacks some hydro constraints (ramping, time delays) (p. 172).
- Two-stage scenario fans are not a proper multistage policy (non-anticipativity only in week 1).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background: Nordic long-term scheduling practice (EMPS) | EMPS structure: SDP on aggregate areas, heuristics, weekly LP market clearing, rule-based drawdown | pp. 166–168, Sec. 3 |
| Theory: role of long-term models as boundary conditions | Long-term models provide boundary conditions for medium/short term | p. 166, Sec. 2 |
| Motivation: pumped storage and short-term variability not captured by existing detailed models | Explicit statement | p. 166, Sec. 1 |
| Lit. review: two-stage scenario fan + Benders as alternative to SDDP | SFP description | pp. 168–169, Sec. 4 |

## Useful quotes (with page numbers)
> "More short-term price variations will change the operation and increase use of pumped storage plants and open for investment in new pumping capacity." (p. 166)

## Follow-up references to check (backward snowballing)
- [7] Helseth, Mo & Warland (2010), long-term scheduling of hydro-thermal power systems using scenario fans, *Energy Systems* 1(4).
- [2] Wolfgang et al. (2009), hydro reservoir handling in Norway before and after deregulation, *Energy* 34.
- [1] Fosso et al. (1999), generation scheduling in a deregulated system: the Norwegian case, *IEEE TPWRS* 14(1).
- Helseth et al. (2018), detailed long-term hydro-thermal scheduling for expansion planning in the Nordic power system, *IET GTD* 12(2) (follow-up of SOVN, cited by Ahlfors & Amelin 2021). Our library has `helseth2017`, which may be related (unverified).

