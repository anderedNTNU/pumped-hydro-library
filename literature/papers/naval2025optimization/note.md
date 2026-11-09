---
bibkey: naval2025optimization
title: "Optimization of pumped hydro storage management with renewable generation under wind uncertainty using chance-constrained programming"
authors: "Naval, Natalia; Yusta, Jose M."
year: 2025
venue: "Sustainable Energy, Grids and Networks 43, 101889"
peer_reviewed: true
methods: [deterministic-lp-milp, risk-averse-cvar, uncertainty-modelling]
review_sections: [modelling-phs-plants, market-participation]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Hourly MILP for a Spanish hybrid wind+PV+closed-loop PHS (4 variable-speed units, 5750 MWh) serving a fixed industrial load over one year (12 linked months), with wind forecast error handled by chance constraints on renewable demand coverage; prices deterministic (OMIE 2023), DA energy only."
---

# PHS management with wind under chance constraints (Naval & Yusta, 2025)

_Article-numbered paper; page numbers are the article's own pages 1–15._

## Research question / purpose
"How does wind power uncertainty affect the operational decisions of hybrid generation facilities with energy storage?" (p. 4). The aim is an hourly scheduling model for a closed-loop reversible PHS hybridised with wind and PV that maximises the monthly operating profit in a liberalised market, extended over a whole year, with wind uncertainty handled by chance-constrained programming (CCP) (p. 4). Claimed gap: hourly techno-economic dispatch models that combine several renewables with long-term grid-connected PHS and renewable uncertainty; most studies use short horizons (p. 3).

## Setting
- **System:** one hybrid plant in Spain (a project under development; data from a Spanish wind/PV developer): wind farm, PV plant and a **closed-loop** reversible PHS with **4 variable-speed pump-turbines**, all behind one grid connection, supplying a **fixed electricity demand of an electro-intensive industry** (pp. 4, 7).
- **Table 1 data (p. 7)** _(the column is garbled in the text extraction; this mapping is my reconstruction and is checked against the results where possible)_: demand 396 MW (constant; 3,468,960 MWh/yr = 396 MW × 8760 h, Table 3 ✓); grid connection 396 MW; wind 465 MW; PV 860 MW; 4 units; per unit: minimum turbine power 33.96 MW, rated turbine power 99 MW, minimum pump power 38.93 MW, rated pump power 113.5 MW; pump-turbine efficiency 0.9 (hydraulic, motor and transformer); **PHS storage capacity 5750 MWh**; start-up cost 10 € [45]; O&M wind 15 €/MWh, PV 8 €/MWh, pumping/turbining 3.5 €/MWh; required demand coverage with local production 60%; prices: Spanish market OMIE, year 2023, purchases through a contract indexed to wholesale prices, sales at hourly wholesale prices with a 7% generation tax. (Checks: 3.5 €/MWh × 810,271 MWh pumped = 2.836 M€ and 15 €/MWh × 1,109,977 MWh wind = 16.65 M€ both appear in Table 4, p. 13.)
- **Derived (my calculation, unverified):** with 4 × 99 MW = 396 MW turbine power (equal to the grid connection), the storage lasts about 5750/396 ≈ **14.5 h** at full output, so it is a daily-to-multi-day store, not seasonal. Pump power 4 × 113.5 = 454 MW.
- **Markets:** energy only. Purchases and sales at hourly Spanish wholesale (day-ahead, OMIE) prices via an indexed pass-through contract with a retailer (pp. 4, 7). Contribution text says "dynamic energy trading strategies in the day-ahead electricity market" (p. 4). No intraday, no reserves. Price-taker (implied; prices are exogenous).
- **Horizon and resolution:** hourly decisions; 12 monthly periods y over a year, linked by storage continuity between months (Eq. 16) and cyclic storage over the year (Eq. 17); objective sums profit over all months and hours (Eq. 1) (pp. 5–6). One month was chosen as the optimisation period for computational feasibility and planning accuracy (p. 5).

## Method
- **Model type:** mixed-integer linear programme (the paper says "mixed-integer mathematical model"); all constraints are linear once the chance constraints are converted to deterministic equivalents. GAMS with the **SCIP** solver (p. 7).
- **Objective (Eq. 1–8, p. 5):** max B = Σ_y Σ_h [export revenue − import cost − pumping O&M − turbining O&M − start-up cost − PV O&M − wind O&M].
- **Constraints (pp. 5–6):** hourly energy balance demand = import − export + wind + PV + turbined − pumped (Eq. 9); renewable output ≤ availability (Eqs. 10–11); no simultaneous import and export (binaries, Eq. 12); import ≤ demand (Eq. 13); export ≤ grid capacity (Eq. 14); **storage balance in energy units (MWh)**, with pumped energy multiplied by and turbined energy divided by the efficiency (Eq. 15); month-to-month and year-end/start linking (Eqs. 16–17); storage bounds (Eq. 18); per-unit min/max power in each mode with binaries (Eqs. 19–20); no pump and turbine at the same time per unit (Eq. 21) and **all units in the same mode in each hour** to avoid hydraulic short-circuit (Eqs. 22–26); start-up binaries and costs (Eqs. 27–29).
- **How uncertainty is represented:** only **wind forecast error**. Chance constraints on demand coverage by local renewable production (Eqs. 30–31, p. 7): the probability that local production covers at least a share γ (60%) of demand must be ≥ 1 − α (production-deficit risk), and a second constraint limits excess production with risk level β. The forecast error is assumed **normal with zero mean and σ = 10% of the wind forecast**, said to cover about 99.73% of errors within ±30% (Eq. 32, p. 7), truncated between the lower and upper limits of wind capacity (Eq. 33). The chance constraints become deterministic using the inverse of the conditional CDF (Eqs. 34–35). _(As far as the garbled equations can be read, the constraints apply to sums over the hours of the period, not to each hour.)_ Prices, demand and PV are deterministic.
- **Cases (Table 2, p. 8):** (1 − α, 1 − β) = Case 1 (95%, 90%), Case 2 (90%, 85%), Case 3 (85%, 80%), Case 4 (80%, 75%), Case 5 (75%, 70%).
- **Key modelling choices and assumptions (pp. 4–5):** closed loop (no inflow, no evaporation losses); variable-speed units only; **constant efficiency** over the whole operating range, justified by speed variation < 33% of rated speed (35 Hz minimum frequency); start-up costs included; **no head effects** (storage is in MWh); no end-of-horizon water value (cyclic storage instead).
- Paper argues CCP is cheaper than scenario-based stochastic programming (fewer variables, no large scenario set) and cites [44] finding higher benefits with CCP than with scenarios for a daily wind–PHS problem (pp. 6, 8).

## Data / case
Technical and economic data from a Spanish wind and PV developer (p. 7); 2023 OMIE prices; monthly PV and wind production profiles in Figs. 2–3 (p. 8). Data available on request (p. 14).

## Key findings
- (p. 1, p. 11, p. 13) Allowing more risk (Case 1 → Case 5) increases imports by **18%** (1,158,736 → 1,413,979 MWh), lowers exports by 42.3% (473,731 → 273,203 MWh) and cuts **import costs by 40%** (Table 4: 104.07 → 62.69 M€); renewable generation costs fall by 28%. The system buys cheap grid energy instead of producing or storing renewables.
- (p. 11, Table 3 p. 13) PHS use falls with higher risk: pumped energy 810,271 → 584,718 MWh (−27.8%), turbined energy 656,319 → 473,622 MWh (−27.8%). The turbined/pumped ratio is 0.81 = 0.9², consistent with 0.9 per mode (my check).
- (Table 3, p. 13) Annual demand coverage by renewables: 90%, 86%, 82%, 79%, 75% for Cases 1–5.
- (p. 11) Strong seasonality: average daily pumping 193 MWh/day (January) → 326 MWh/day (July); turbining 176 → 291 MWh/day. January has the highest imports (up to 396 MWh/h); in June–July imports fall 76% vs. January and exports rise 90%.
- (p. 11) The PHS pumps in low-price hours, which often coincide with high PV output, and generates in high-price hours.
- (p. 13) As imports shrink, pumping and turbining costs grow as a share of import costs (pumping 11.31% → 18.79%, turbining 12.74% → 23.11%).
- (p. 14) Conclusion: wind ≈ 65% and PV ≈ 15% of renewable production in the best case, falling to 55% and 10% at 75% reliability. **This does not match Table 3**, where PV (1.83 TWh) exceeds wind (1.11 TWh) in Case 1; treat these numbers as unreliable.

## Strengths
- Detailed unit-level PHS operation: variable-speed units, min/max power per mode, common-mode constraint across units, start-up costs.
- A full year of hourly operation with linked months (8760 h) instead of a single day or week.
- Clear, simple way to add a reliability (renewable-coverage) requirement under wind uncertainty via chance constraints; shows the cost of reliability across risk levels.

## Weaknesses / limitations
- Only wind uncertainty; **prices are deterministic and known for the whole year** (perfect foresight, 2023), so storage arbitrage value is overstated and not tested out of sample.
- The chance constraint applies to aggregated monthly coverage, not to hourly operation, so it is closer to a soft renewable-share target than to operational risk management. The underlying error model (normal, σ = 10%) is assumed, not estimated.
- Energy-only market; no reserves or intraday, although variable-speed units are well suited to reserves.
- Constant efficiency, no head effects; closed loop with no inflow.
- Results are reported as energy and cost components; total profit per case is not reported directly.
- Presentation issues: a placeholder was left in the published text ("xxx continuous variables and xxx integers", p. 8); Table 1 column misalignment; Table 4 headers seem shifted (the columns labelled C_PV and C_wind hold 3.5 €/MWh × pumped/turbined energy, while those labelled C_pumping and C_turbining hold 8 and 15 €/MWh × PV and wind energy — my check); the Case 1 percentages on p. 13 cannot be reproduced from Table 4; the wind/PV shares in the conclusion contradict Table 3.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.3: PHS with fixed configuration, hourly operation | Closed-loop PHS, 4 × 99 MW turbine / 113.5 MW pump variable-speed units, 5750 MWh | p. 7, Table 1 |
| Lit. review 5.4: DA-only market participation | Buy/sell at OMIE hourly prices via indexed contract; no reserves | p. 4, p. 7 |
| Lit. review: uncertainty methods overview (SP, SDP, RO, CCP) | Short review of methods and their trade-offs | p. 3, Sec. 1.2 |
| Model: unit commitment of pump-turbines | Min/max power per mode, common mode across units, start-up cost | pp. 6, Eqs. 19–29 |
| Model: storage balance in energy units with efficiency | Eq. 15 (pump × η, turbine ÷ η) | p. 6 |
| Model: variable-speed constant-efficiency justification | < 33% speed deviation, 35 Hz minimum | p. 5 |
| Method: chance constraints as an alternative to scenarios | Normal wind error σ = 10%, deterministic equivalents | p. 7, Eqs. 30–35; p. 8 |
| Background 2.2: PHS share of storage, European fleet | > 90% of world storage; Europe 160 plants / 55 GW; EU 140 plants / 45 GW turbine (39 GW pumping), from IHA 2022 | p. 1 |
| Background: wind forecast errors | 15–20% forecast error (citing [18]) | p. 3 |

## Useful quotes (with page numbers)
> "maximizing the profit is prioritized over the coverage of demand with renewable resources" (p. 1)

_Further key statements are paraphrased with page numbers under Key findings._

## Follow-up references to check (backward snowballing)
- [29] Toufani, Karakoyun, Nadar, Fosso & Kocaman (2023), Optimization of pumped hydro energy storage systems under uncertainty: a review, J. Energy Storage 73 — **high priority** for our lit. review.
- [23] Toufani, Nadar & Kocaman (2022), Short-term assessment of PHES configurations: up, down, or closed?, Renew. Energy 201 — configuration comparison with SDP under price uncertainty.
- [25] Fernández-Muñoz, Pérez-Díaz & Chazarra (2019), two-stage stochastic model for water value calculation in a hybrid diesel/wind/pumped-storage system.
- [44] Ding, Hu & Song (2012), stochastic daily operation of wind farm and PHS, Renew. Energy 48 — CCP vs scenarios.
- [49] Toubeau, Vallée & Bruninx (2020), chance-constrained scheduling of underground PHS, IEEE TSTE.
- [7] Papaefthymiou & Papathanassiou (2014), optimum sizing of wind-pumped-storage hybrids in islands.
- [14] Kyrimlidou et al. (2024), sizing and long-term operation of RES-BESS in all market segments (DA, reserve, balancing).

