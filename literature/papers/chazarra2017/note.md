---
bibkey: chazarra2017
title: "Optimal Energy and Reserve Scheduling of Pumped-Storage Power Plants Considering Hydraulic Short-Circuit Operation"
authors: "Manuel Chazarra, Juan Ignacio Pérez-Díaz, Javier García-González"
year: 2017
venue: "IEEE Transactions on Power Systems, 32(1), 344–353"
peer_reviewed: true
methods: [deterministic-lp-milp, hydro-production-function]
review_sections: [modelling-phs-plants, market-participation, electricity-markets, phs-technology, reservoir-sizing-capacity]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Deterministic hourly MILP for a price-taking closed-loop PHS in Spanish day-ahead + secondary regulation (aFRR-type) markets; reserve capacity is the main revenue source and hydraulic short-circuit (ternary units) raises max theoretical income by ~141–166% vs a conventional plant."
---

# Energy and reserve scheduling of PHS with hydraulic short-circuit (Chazarra et al., 2017)

## Research question / purpose
Two aims (p. 345): (1) formulate an MILP for the hourly energy and reserve scheduling of a realistic **closed-loop, daily-cycle** pumped-storage hydropower plant (PSHP) that can run in **hydraulic short-circuit (SC)** mode (pump and turbine running at the same time); (2) quantify how much hydraulic SC operation raises the income of a **price-taker** PSHP that sells in the day-ahead (spot) market and in the Spanish **secondary regulation** service (reserve capacity + real-time regulation energy). The model extends the authors' earlier variable-speed model [12] to several units, head dependency of power and of available spinning reserve, and SC operation (p. 345).

## Setting
- **System:** single pumped-storage plant, closed loop (no natural inflow to the upper reservoir, no release from the lower, footnote 1 p. 345), daily cycle, two identical units. Three configurations compared (Table I, p. 346; Sec. III, pp. 347–348):
  - **Conv:** binary units (reversible Francis pump-turbine), fixed-speed pumping, single penstock, so no unit can generate while another pumps (eq. 36); no reserve while pumping.
  - **SC-B:** binary units, but one unit may pump while another generates (eq. 35 only forbids simultaneous modes in the same unit).
  - **SC-T:** ternary units (Pelton turbine + fixed-speed pump + motor/generator on one shaft with a clutch); pump and turbine of the same unit can run together, so the plant regulates power while consuming (pp. 345–346). Real examples of SC operation: Kops II (Austria, 2008), Malta, Geesthacht, Lünersee (p. 345–346).
- **Markets:** Spanish day-ahead market (DM) + secondary regulation reserve market (SM; capacity, cleared at 17:30 of D-1 after the spot market, paid at the marginal price) + real-time secondary regulation-up/-down **energy** (paid at the marginal tertiary regulation price) (p. 345). The Spanish TSO fixes an hourly ratio of up-reserve to total reserve, R_t^SM (eq. 31, p. 348). No intraday, no tertiary (future work, p. 352). Secondary regulation is the Spanish counterpart of aFRR (our mapping; the paper never uses the term aFRR).
- **Horizon and resolution:** daily problems (24 hourly periods), run day by day over two representative weeks (summer 30/06–06/07/2014, late autumn 10/11–16/11/2014), with initial = final upper-reservoir volume of 2.5 hm³ each day (p. 349).

## Method
- **Model type:** deterministic MILP (perfect foresight) maximising net income (eq. 1, p. 347): regulation-up energy income − regulation-down energy cost + Σ(generation − pumping)·spot price + (up + down reserve)·SM price − start-up costs of turbines and pumps.
- **How uncertainty is represented:** none. All prices, the real-time use of reserves and R_t^SM are historical and known in advance; results are a **maximum theoretical income** (pp. 349, 352). Stochastic prices and reserve activation are explicitly left for future work (p. 352).
- **Solution method:** CPLEX branch and cut; hundreds of CPU seconds per week per plant (p. 349).
- **Key modelling choices and assumptions:**
  - *Water balance* (eq. 2, p. 347): v_t = v_{t−1} + l_t·Σ_c(q^p − q^d); no inflow; storage bounds (eq. 3); lower reservoir not modelled "for the sake of clarity" (p. 347).
  - *End condition:* **target final volume** v_T = f_v, set equal to the initial volume (eq. 4, p. 347). No water value / terminal value function.
  - *Head dependency* (eqs. 5–24, p. 347–348): two generation/consumption curves k1/k2 for two reservoir levels (gross head 300 m and 310 m), chosen by a binary δ_t depending on whether the upper-reservoir volume is below or above the midpoint (eqs. 5–6); big-M constraints switch power, min/max discharge, pumping power and pumped flow between the two curves. Hydraulic losses 3 % of gross head (p. 349). Linear discharge–power relation within each curve (p. 349).
  - *Reserve in the water balance:* total discharge includes extra flow for expected regulation-up energy and the flow kept upstream for regulation-down energy, using the activation percentages α_t^up, α_t^dw and the head-dependent energy coefficient (eqs. 13–16, p. 347–348).
  - *Reserve headroom* (eqs. 27–31, p. 348): up-reserve ≤ head-dependent max power − current generation; down-reserve ≤ generation − head-dependent min power (auxiliary variable avoids a bilinear term); reserve only if the turbine is on (eq. 29); up/(up+down) = R_t^SM (eq. 31).
  - *Regulation energy settlement* (eqs. 32–34, p. 348): net regulation energy is paid at the up price if positive, charged at the down price if negative (binary γ_t).
  - *Fixed-speed pumps:* single operating point, efficiency 90 %; no regulation in pumping mode (pp. 346, 349).
  - *Start-up costs* via binaries (eqs. 25–26), values from Nilsson & Sjelvgren [27] (p. 349).
  - *Activation assumption:* real-time use of reserves = historical hourly ratio of aggregate delivered to aggregate assigned secondary reserve for the whole Spanish system, max 100 %; R_t^SM = historical system ratio (p. 348–349). Individual plant activation data are not public (p. 348).

## Data / case
- Spanish market, 2014 historical hourly prices: spot, secondary reserve price, secondary up/down energy prices, real-time use of reserves, R_t^SM (p. 348–349). 2014 means: spot 42.15 €/MWh, secondary up energy 47.36 €/MWh, secondary down energy 31.34 €/MWh (p. 350).
- Technical data per unit, Table II (p. 349), lower/higher reservoir level: max discharge 115.7 m³/s; max generation 297.4/314.1 MW; turbine efficiency at max flow 90/92 %; min discharge 49.77 m³/s (Francis) vs 23.15 m³/s (Pelton); min generation 107.9/114.5 MW (Francis) vs 52.87/55.99 MW (Pelton); efficiency at min flow 76/78 % (Francis) vs 80/82 % (Pelton); pumped flow 115.7 m³/s; pumping power 389.8/402.8 MW; pump efficiency 90 %; start-up cost turbine 1650.6 €, pump 1321.5 €.
- Upper reservoir 0–5 hm³; flows chosen so the reservoir can be emptied/refilled in a minimum of **6 h** (p. 349). (Our back-of-envelope, not in the paper: 5 hm³ × ~291 m net head × 0.9 ≈ 3.6 GWh.)
- Round-trip efficiency: ternary 78 %–69.5 % (higher head) and 76.3 %–67.8 % (lower head); binary 78 %–66.1 % and 76.3 %–64.4 % (max to min operating point) (p. 349).

## Key findings
- (p. 349–350, Table III) All three plants earn **most of their income from the secondary reserve (capacity) market**; the more flexible the plant, the higher the SM and total income and the lower (even negative) the spot-market revenue. The spot market becomes a "subsidiary" means of enabling reserve participation.
- (p. 350, Table III, 10³ €) Summer week totals: Conv 515.31, SC-B 529.80, SC-T 1368.28 (SM: 707.28 / 728.43 / 1682.55; DM net: −58.25 / −69.38 / −397.93). Autumn week totals: Conv 1245.84, SC-B 1289.39, SC-T 3006.56 (SM: 1163.93 / 1180.58 / 2969.99). Day 11/11/2014: Conv 158.29, SC-B 166.19, SC-T 380.57.
- (p. 350) SC-T vs Conv: **+165.5 %** (summer week) and **+141.33 %** (autumn week). SC-B vs Conv only +2.81 % and +3.5 %, because in SC-B one unit must pump and another generate, and Francis units have a narrower regulation range than Pelton turbines. (The conclusion, p. 352, says "up to 162.3 %", inconsistent with 165.5 % in Sec. IV-C.)
- (p. 350) Reason: a conventional plant cannot offer reserve while pumping; the SC-T plant offers reserve in every hour with a range equal to all turbines in operation.
- (p. 350–351) Both plants pump off-peak and generate on-peak; the Conv plant makes some arbitrage profit, while SC-T has negative spot revenue. Secondary reserve prices are (per unpublished studies by the authors) **negatively correlated with spot prices**, so higher off-peak (p. 351).
- (p. 351) The Conv plant avoids offering reserve in hour 3 because ~85 % expected activation could empty the upper reservoir, i.e. **storage limits constrain reserve provision through activation energy**.
- (p. 351) The Conv plant uses the whole storage capacity while SC-T uses only a small fraction; the authors suggest this could affect **storage sizing and investment cost**, but leave it to future work.
- (p. 351–352, Figs. 7–9) Sensitivity: income varies roughly linearly and almost sixfold when the mean SM price varies sixfold; it is more sensitive for SC-T. Sensitivity to up/down energy prices is smaller and mostly driven by the accompanying SM price.
- (p. 351) Sensitivity price profiles: daily historical profiles 2010–10/11/2014 clustered into **four daily groups** (squared Euclidean distance, Everitt et al. [28]); the real day closest to each centroid is used.
- (p. 352) Caveats stated by the authors: price-taker, perfect information; stochastic prices and reserve use, price-maker behaviour in the SM, intraday/tertiary markets and optimal sizing are future work.

## Strengths
- Explicit, reusable MILP formulation of **joint day-ahead + reserve capacity + activation energy** for a PHS, including how reserve activation affects the water balance and how storage limits restrict reserve offers.
- Head dependency of both power and available reserve via two I/O curves, with realistic per-unit data (Table II) and round-trip efficiencies.
- Clean comparison of plant configurations (Conv / SC-B / SC-T) with a revenue breakdown by market.

## Weaknesses / limitations
- Deterministic, perfect foresight: income is an upper bound (p. 352).
- Daily horizon with fixed start/end volume (2.5 hm³): no inter-day or seasonal value of water, no water values.
- Only two representative weeks of Spanish 2014 data; results are market- and period-specific.
- Activation modelled with system-wide historical ratios, not plant-specific; activation known in advance.
- Lower reservoir not modelled; closed loop (no inflow).
- Minor inconsistency: 162.3 % (p. 352) vs 165.5 % (p. 350).

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: PHS operation (pump/generate linked by reservoir balance, efficiency, capacity limits) | Water balance, storage bounds, generation/pumping limits, efficiencies, round-trip efficiency | pp. 347–349, eqs. 2–3, 7–24, Table II |
| Theory/model: end-of-horizon treatment | Target final volume equal to initial volume (eq. 4); daily start/end 2.5 hm³ | p. 347 (eq. 4), p. 349 |
| Model: reserve capacity headroom constraints | Up/down reserve bounded by max/min head-dependent power; reserve only when turbine on | p. 348, eqs. 27–31 |
| Model: activation energy in the water balance | Extra discharge for up-activation, retained water for down-activation | pp. 347–348, eqs. 13–16, 32–34 |
| Model: activation assumption | Real-time use = historical system ratio of delivered/assigned reserve, max 100 % | pp. 348–349 (Sec. IV-A1) |
| Model: head effects | Two I/O curves at two reservoir levels switched by a binary; 3 % head losses | p. 347 (eqs. 5–24), p. 349 |
| Lit review (market participation): reserves as main revenue | SM income dominates; spot market subsidiary | p. 349–350, Table III; p. 352 |
| Lit review (modelling PHS): deterministic MILP with reserves | Example of perfect-foresight daily MILP; contrast with our stochastic approach | Sec. III, pp. 347–348; p. 352 caveats |
| Background (PHS technology): hydraulic short-circuit, ternary units, variable speed | Explanation of SC, ternary vs binary units, Kops II etc. | pp. 345–346, Table I, Figs. 1–2 |
| Background (markets): Spanish secondary regulation design | Reserve market at 17:30 D-1, marginal pricing, energy at tertiary price, TSO up/total ratio | p. 345, p. 348 (eq. 31) |
| Background (price volatility / reserve prices) | Reserve prices negatively correlated with spot (authors' unpublished studies) | p. 351 |
| Lit review (sizing): flexibility reduces storage use | SC-T uses small fraction of storage; sizing as future work | p. 351, p. 352 |
| Method: clustering daily price profiles | Four daily clusters via squared Euclidean distance; closest real day to centroid | p. 351 (Sec. IV-E) |
| Motivation: PHS investment cost range and profitability barriers | 470–2170 €/kW (citing Connolly et al. [3]); arbitrage alone often insufficient | p. 345 (Introduction) |

## Useful quotes (with page numbers)
> "the secondary regulation reserve market might be the main source of revenue" (p. 344, abstract)

> "the spot market would assume a subsidiary role" (p. 352)

## Follow-up references to check (backward snowballing)
- [3] Connolly et al. (2011), PHES arbitrage strategies, Energy Policy 39(7) (investment costs, arbitrage profitability).
- [7] Pérez-Díaz et al. (2015), "Trends and challenges in the operation of pumped-storage hydropower plants", RSER 44 (review).
- [8] Pinto, Sousa, Neves (2011), value of a pumping-hydro generator with wind, EEM (secondary reserve as main income).
- [12] Chazarra et al. (2014), variable-speed PSHP in secondary reserve markets, EEM (base model).
- [15] Chazarra et al. (2016), stochastic weekly scheduling in day-ahead and secondary reserve markets, EPSR 130 (stochastic extension; close to our setting).
- [20] Kazempour et al. (2009), risk-constrained self-scheduling of PSH in energy and ancillary markets.
- [24] Conejo et al. (2002), self-scheduling of a hydro producer (I/O curve formulation).

