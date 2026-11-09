---
bibkey: stedinger1984stochastic
bibkey_provisional: true
title: "Stochastic Dynamic Programming Models for Reservoir Operation Optimization"
authors: "Jery R. Stedinger, Bola F. Sule, Daniel P. Loucks"
year: 1984
venue: "Water Resources Research, 20(11), 1499-1505"
peer_reviewed: true
methods: [sdp, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDP_i_vannkraft/Stedinger1984.pdf"
takeaway: "Classic SDP paper on the choice of hydrologic state variable: a stationary SDP that uses the best forecast of the current period's inflow (instead of the previous period's inflow) gives clearly better simulated operation of the High Aswan Dam (up to 32% lower losses when the system is stressed), and can even beat a nonstationary adaptive-control SDP; SDP is only optimal within the class of policies its state allows."
---

# SDP with forecast as hydrologic state (Stedinger, Sule & Loucks, 1984)

## Research question / purpose
Most SDP reservoir models derive stationary policies using the **previous period's inflow Q_{t−1}** as the hydrologic state. The paper asks whether using the **best forecast of the current period's inflow** as the hydrologic state gives better policies, and how this relates to nonstationary "adaptive-control" SDP (abstract, p. 1499).

## Setting
- **System:** High Aswan Dam, Nile (single reservoir, 169 × 10⁹ m³ capacity, 110 m height; mean annual flow ~84 × 10⁹ m³; Sudan withdrawals 18.5 × 10⁹ m³/yr) (p. 1501). Multipurpose: irrigation, flood control, hydropower. Not pumped storage.
- **Markets:** none. Losses are weighted quadratic shortfalls against irrigation, maximum release (flood) and monthly power targets PT (Eq. 8, p. 1502).
- **Horizon and resolution:** monthly periods, stationary (infinite-horizon, average-gain) policies; simulation with 1912–1965 historical flows (pp. 1499, 1502).

## Method
- **Model type:** discrete SDP, stationary (Howard policy-iteration-type average-gain formulation, Eq. 1, p. 1499) and nonstationary adaptive control (Eqs. 2–3, p. 1500).
- **Models compared (p. 1502):**
  - SSDP0: classic stationary SDP, state (S_t, Q_{t−1}), lag-1 correlations as reported by Bras et al. (1983).
  - SSDP1: same, but transition probabilities from the authors' recomputed lag-1 correlations.
  - ADP: adaptive-control SDP of Buchanan & Bras (1981).
  - PDP1: "predictive" stationary SDP, Eq. (6), with state (S_t, Q̂_t) where Q̂_t is the authors' one-step-ahead forecast.
  - PDP2: PDP1 with Curry & Bras (1980) forecast equations.
- **How uncertainty is represented:** discrete Markov chain. Discrete values are the 97.5, 83.125, 59.375, 35.625 and 11.875 percentiles of the unconditional distributions (medians of intervals of probability 0.05, 0.2375, 0.2375, 0.2375, 0.2375). Transitions from a bivariate normal with historical correlations (p. 1501).
- **Key formulation (Eq. 6, p. 1500):** f(S_t, Q̂_t) + g = max_R E_{Q_t|Q̂_t}{B(S_t, Q_t, R*) + E_{Q̂_{t+1}|Q_t}[f(S_{t+1}, Q̂_{t+1})]}. Two nested conditional expectations: actual inflow given forecast, then next forecast given actual inflow.
- **Key modelling choices:**
  - Release R* equals target R unless storage bounds bind (p. 1499).
  - Discussion of decision variable choice: release target vs ending-storage target (rule-curve style) (p. 1501).
  - Policies of the form R(S_t, Q_{t−1}) are optimal only within a restricted class (p. 1500).

## Data / case
- Wadi Halfa / Aswan monthly flows; 1912–1965 for simulation, extended 1906–1967 for forecast models (Tables 1–2, p. 1501).
- Loss weights 10⁷ (irrigation), 10⁴ (max release), 10⁻³ (power) from Bras et al.; PT = 1280 GWh/month originally (p. 1502).

## Key findings
- (p. 1500) Esmaeil-Beik & Yu (1984) found simulated weekly losses almost doubled when Q_{t−1} instead of Q_t was used in the policy: state choice matters even with short time steps.
- (p. 1502, Table 3) Base case: SSDP0 5735, SSDP1 5381, PDP1 5330, ADP 5083, PDP2 4878 average annual cost. All achieve near-perfect operation; differences (~200 standard error) are too small and flood-sensitive to rank the models strictly.
- (p. 1502) Coarse five-point discretisation is a crude description of flood risk; finer description needed for flood control.
- (p. 1503, Table 4) Lowering the power target to stress the system: PDP beats SSDP by 1.0% (1280 GWh/mo), 5.9% (1000) and **32.0%** (750).
- (p. 1503, Table 5) With reduced capacity (85 and 127.5 × 10⁹ m³) and no flood objective, PDP losses are 20% and 18% lower than SSDP.
- (p. 1503) Information beyond the previous inflow (snowpack, soil moisture, upstream gauges, ARMA(1,1) structure) can be used as hydrologic state; the largest gains arise where such supplementary information exists.
- (pp. 1503–1504, conclusion) Nonstationary adaptive procedures are expensive to rerun every month and in Monte Carlo studies. A **stationary policy with a good hydrologic state** (PDP2) outperformed the nonstationary adaptive SDP. SDP only finds the optimum within the class of policies examined.

## Strengths
- Clear demonstration that the information content of the state variable drives policy quality.
- Honest about statistical significance (standard errors reported, p. 1502).
- Shows both stationary and nonstationary formulations side by side.

## Weaknesses / limitations
- Single reservoir, coarse 5-point discretisation.
- Policies evaluated partly on the same flows used to fit forecasts (p. 1502), which the authors flag.
- No market prices; penalty-weighted targets.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: choice of state variables in SDP | Q_{t−1} vs forecast Q̂_t as hydrologic state; policy class argument | pp. 1500–1501 ("State and decision variable selection") |
| Theory: stationary vs nonstationary SDP | Steady-state Eq. (1), adaptive Eqs. (2)–(5), predictive Eq. (6) | pp. 1499–1500 |
| Uncertainty modelling: Markov-chain discretisation | Percentile-based discrete values and bivariate-normal transitions | p. 1501 |
| Lit review: value of better state information | 1–32% loss reductions depending on stress | p. 1503, Tables 4–5 |
| Limitation: coarse discretisation and flood tails | Crude description of flood risk with 5 points | p. 1502 |
| Decision variable: release vs end-storage target | Rule-curve style end-storage targets | p. 1501 |

## Useful quotes (with page numbers)
> "policies of the form R(S_t, Q_{t−1}) are optimal only among a very restricted class of release rules" (p. 1500)

## Follow-up references to check (backward snowballing)
- Bras, Buchanan & Curry (1983), WRR 19(1) — adaptive closed-loop control, High Aswan.
- Gal (1979), WRR 15(4) — parametric SDP for multireservoir systems.
- Turgeon (1980, 1981), WRR — aggregation/decomposition SDP for multireservoir power systems.
- Yakowitz (1982) — already `yakowitz1982`.
- Howard (1960) — policy iteration.

