---
bibkey: helseth2017
title: "Detailed long-term hydro-thermal scheduling for expansion planning in the Nordic power system"
authors: "Arild Helseth, Birger Mo, Arild Lote Henden, Geir Warland"
year: 2018
venue: "IET Generation, Transmission & Distribution, 12(2), 441–447"
peer_reviewed: true
methods: [two-stage-stochastic, benders-decomposition, heuristics-simulation, uncertainty-modelling, hydro-production-function]
review_sections: [modelling-phs-plants, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "SINTEF scenario-fan simulator: each week a two-stage stochastic LP (Benders) over historical weather/price scenarios in a rolling horizon, with the full Nordic hydro system unaggregated (1265 modules); used to value HVDC and Duge PHS capacity expansions, giving smoother marginal benefits than EMPS but lower marginal value of extra PHS capacity."
---

# Scenario-fan long-term hydro-thermal scheduling for Nordic expansion planning (Helseth et al., 2018)

_Bibkey says 2017 (E-First 1 Nov 2017); the journal issue is 2018, Vol. 12, Iss. 2._

## Research question / purpose
Present and verify a long-term hydro-thermal scheduling (LTHTS) method that keeps the **detailed** hydropower system (no aggregation into equivalent reservoirs) in the strategy computation, under uncertainty in weather and exogenous prices (p. 441). Motivation: aggregation–disaggregation models (e.g. EMPS) struggle to value hydropower flexibility as short-term wind and daily price variations increase, and SDDP-based strategies for the detailed Norwegian system perform poorly when simulated on historical data and handle non-convexities/stage-wise dependencies with difficulty (pp. 441–442). Contribution: first application of a stochastic LTHTS to the full Nordic system without aggregation, used to evaluate changes in expected socio-economic surplus from (i) more Norway–Germany cable capacity and (ii) upgrading the Duge pumped-storage plant (p. 442). Extends the scenario-fan method of [29] (Helseth, Mo, Warland 2010, aggregate hydro) to detailed hydro (p. 442).

## Setting
- **System:** the Nordic power system as provided by the Norwegian TSO, about year 2020, 26 price zones (15 NO, 4 SE, 2 DK, 2 FI, 3 Baltic), new HVDC to GB and DE (p. 445). 1265 hydro modules (one reservoir + one station each), 737 with reservoir > 2 Mm³ (p. 445). Duge pumped-storage plant (200 MW) in the Sira-Kvina watercourse, southern Norway (p. 445).
- **Markets:** no market products. System cost minimisation ≡ socio-economic surplus maximisation (p. 445); exogenous market areas (GB, DE, NL, PL, RU) with stochastic prices from a fundamental model with a wider boundary (p. 445). No reserves, no intraday.
- **Horizon and resolution:** weekly decision stages in a rolling horizon; each weekly decision looks ahead along scenarios of fixed length (52 weeks in the case study) (pp. 442, 445). Within the week: 5 time steps (cable case) or 56 time steps (PHS case, i.e. 3-h steps, our calculation) in the operational problem; coarser along the scenarios (p. 445).

## Method
- **Model type:** Scenario Fan Simulator (SFS). For each week t along an operational scenario o, solve a **scenario fan problem (SFP)**: a two-stage stochastic LP whose first stage is this week's operation (uncertainty known for the current week) and whose second stage is a set of deterministic scenario problems, one per scenario s, covering weeks t+1 … T̂ (pp. 442–443, eq. 3). A scenario fan is a special scenario tree where all uncertainty is resolved in the second stage (p. 442). The first-stage decision is stored, the state is passed on, and the procedure rolls forward one week (p. 442).
- **How uncertainty is represented:** historical records: inflow, wind, temperature, snow and exogenous prices; "history may repeat itself with equal probability" from any point in time, so N_S historical years give N_S scenarios; ~80 years usually available; corrected for climate change (p. 443). Scenarios are **corrected to the current state** of the simulated scenario o by assuming a first-order autoregressive model for the normalised series: the deviation decays as φ^(t), eqs. 1–2 (p. 443). Snow-based conditioning possible but not used (p. 443). Scenario reduction by fast forward selection (Gröwe-Kuska et al. [31]), weighting scenarios by the sum of inflow and wind energy (p. 443). Stochastic demand also appears (temperature-dependent; nomenclature p. 441).
- **Solution method:** Benders (L-shaped) decomposition of each SFP into the operational problem (eq. 4) and scenario problems (eq. 5); cuts on the end-of-week state (eqs. 6, 11) (p. 443–444). SFP converges on average in ~20 iterations (cable case, p. 445). Parallel over scenario problems; Fortran, CPLEX 12.6 dual simplex, MPI (pp. 444–445).
- **Key modelling choices and assumptions:**
  - *End-of-horizon value* Φ(x_T̂): conceptually zero if the horizon is long enough, but >5 years would be needed for the Nordic system; in practice taken from another model or a longer, simpler SFS run (p. 444). Case study: from EMPS (p. 445).
  - *Hydropower production:* piecewise-linear concave power–discharge curve (decreasing segment efficiencies) at a nominal head H⁰, scaled by actual head H/H⁰ from the initial volume of the week; head is a parameter, so only its immediate effect is in the constraints; **precomputed head sensitivities** c^W in the objective capture the future value of head (procedure of Gjelsvik et al. 2010 [8]) (p. 444, eqs. 7, 9). Pump consumption factor may depend on the head between the two reservoirs (p. 444). In the scenario problems, head = mid-week head from the previously solved SFP (p. 444).
  - *Hydro topology:* discharge, bypass, spillage waterways and pumps (eq. 8); seasonal reservoir/discharge/bypass restrictions; storage-dependent constraints pre-processed per scenario from the previous SFP solution (p. 444).
  - *Market/grid:* zonal power balances with price-elastic demand steps, curtailment, exchange with exogenous markets, transmission limits with linear losses, dumping of excess power to avoid negative prices (p. 444). Start-up costs and DC power flow are available but not discussed (p. 444).
  - *Speed-ups:* reduced number of scenarios (19 in the case), gradually coarser time resolution along the scenario horizon (p. 444–445).

## Data / case
- Inflow years 1962–2012, 228 inflow records; 85 wind and 15 temperature records for the same years (p. 445).
- 52-week scenarios, end valuation from EMPS, 19 scenarios after reduction; server with 2 × 10-core Xeon E5-2640, 128 GB RAM (p. 445). The N_S scenarios are simulated in sequence (expansion study, so results should not depend much on the initial state) (p. 444).
- **Cable case** (p. 445): 5 steps/week operational, 1 step/week in scenarios; scenario problem 68,917 constraints, 451,655 variables; ~20 Benders iterations, slightly over 1 min per SFP; total SFS run 50 h vs EMPS 10 min. Cable to Germany increased by 200 MW in 10 MW steps.
- **PHS case** (p. 445): Duge (200 MW) capacity increased incrementally up to +2000 MW; NO–DE exchange set to 5000 MW to create intra-week price differences that trigger pumping; 56 steps/week operational, 5 steps/week for the first 10 scenario weeks and 1 step afterwards; 120,957 constraints, 749,455 variables per scenario problem; 3.5 min per SFP; total 156 h. The paper does not say whether pump and turbine capacity are increased separately (unverified).

## Key findings
- (p. 445, Fig. 3) Socio-economic surplus should be non-decreasing in cable capacity; neither model is strictly so, but SFS results are more consistent and less "noisy" than EMPS.
- (p. 445, Fig. 4) With 230 MW at Duge, SFS pumps with frequent on/off decisions driven by intra-week price differences; EMPS heuristics mainly give **seasonal** pumping and miss intra-week price differences.
- (p. 446, Fig. 5) Marginal benefit of extra PHS capacity is smoother with SFS. SFS uses the plant more efficiently, but the **marginal value of additional capacity is lower** because SFS sees the detailed watercourse constraints.
- (p. 444) Head representation via parameters + head sensitivities is a reasonable accuracy/computation compromise for many Nordic watercourses; it costs little extra time (first SFP solved twice).
- (p. 446) Conclusion: suited to valuing hydropower flexibility under more volatile prices; the trade-off between computation time and strategy quality (scenario count, horizon, resolution) needs further work.

## Strengths
- Detailed (unaggregated) hydro in the strategy, at Nordic scale.
- Uses historical weather directly, keeping spatial/temporal correlation, with a simple AR(1)-based state correction (eqs. 1–2).
- Directly values a PHS capacity expansion and shows that model detail changes the marginal value of capacity.
- Transparent problem sizes and run times.

## Weaknesses / limitations
- Two-stage fan: all uncertainty resolved after the first week (no recourse beyond stage 2), so the strategy is anticipative along each scenario.
- Depends on an external end-of-horizon water value (EMPS).
- Very long run times (50–156 h) even with 19 scenarios and coarse scenario resolution.
- System perspective; no reserves or market products; PHS revenue not reported separately; expansion evaluated by enumeration, not optimised.
- Only two expansion cases; few numbers reported (results mostly figures).

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (modelling PHS): alternatives to SDDP | Scenario-fan two-stage LP in a rolling horizon; motivation vs SDDP and aggregation | pp. 441–443, Secs. 1–2 |
| Lit review: limitations of aggregated models (EMPS) | Aggregation struggles to value flexibility; EMPS pumping mainly seasonal | p. 442, p. 445 (Fig. 4) |
| Lit review (sizing): value of PHS capacity expansion | Duge +0…2000 MW; marginal surplus smoother but lower with detailed model | pp. 445–446, Fig. 5 |
| Method: historical scenarios and state correction | Equal-probability historical years; AR(1)-based deviation decay | p. 443, eqs. 1–2 |
| Method: scenario reduction | Fast forward selection weighted by inflow+wind energy | p. 443 |
| Model: end-of-horizon water value | Needed because >5-year horizon impractical; taken from EMPS | p. 444, p. 445 |
| Model: head effects in an LP | Head as parameter + head sensitivities in objective; head-dependent pump factor | p. 444 (Sec. 3.2–3.3) |
| Model: intra-week time steps | 5 vs 56 steps/week; finer steps let PHS exploit price differences | p. 445 |
| Motivation: flexibility value rises with intermittent RES | Introduction argument for valuing hydropower flexibility | p. 441 |
| Comparison table row | System, two-stage SLP in rolling horizon, weather + prices, no markets | whole paper |

## Useful quotes (with page numbers)
> "the marginal value of additional plant capacity is lower due to the detailed constraints" (p. 446)

> "the heuristics in the EMPS model primarily allows for seasonal pumping" (p. 445)

## Follow-up references to check (backward snowballing)
- [29] Helseth, Mo, Warland (2010), long-term scheduling using scenario fans, Energy Systems 1(4).
- [8] Gjelsvik, Mo, Haugstad (2010), SDDP in hydro-dominated systems, Handbook of Power Systems I (head sensitivities).
- [11] Gjerden et al. (2015), hydrothermal scheduling in Norway using SDDP: large-scale case study, PowerTech.
- [5] Wolfgang et al. (2009), hydro reservoir handling in Norway before and after deregulation (EMPS).
- [21] Kelman et al. (1990), sampling SDP.
- [14] Abgottspon et al. (2014), risk-averse medium-term hydro with spinning reserves (also cited in our table).

