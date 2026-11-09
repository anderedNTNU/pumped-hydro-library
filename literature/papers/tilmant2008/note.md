---
bibkey: tilmant2008
title: "Assessing marginal water values in multipurpose multireservoir systems via stochastic programming"
authors: "A. Tilmant, D. Pinte, Q. Goor"
year: 2008
venue: "Water Resources Research 44(12), W12431"
peer_reviewed: true
methods: [sddp-time-series, sdp, benders-decomposition, uncertainty-modelling, hydro-production-function]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Marginal water values are the Lagrange multipliers of the reservoir mass-balance constraints in an SDDP model; applied to a 7-reservoir hydropower-irrigation cascade (Euphrates) they give monthly distributions of water values that are higher in the low-flow season, lower downstream, and most dispersed in the high-flow month."
---

# Marginal water values via SDDP (Tilmant, Pinte and Goor, 2008)

_Page mapping: article W12431 has 17 pages numbered "1 of 17" to "17 of 17"; PDF page n = article page n. Paragraph numbers [n] are given where useful._

_Sign convention: the model **maximises** benefits, so the cuts are upper approximations of the benefit-to-go function, the forward simulation gives the lower bound and the stage-1 value gives the upper bound (pp. 5, 7-8). Same direction as our profit-maximising SDDP._

## Research question / purpose
- How to assess the marginal value of water and its statistical distribution at different points in space (reservoirs, intermediate catchments) and time (months) in a stochastic, multipurpose multireservoir system (pp. 1-2, [3], [5]).
- Most valuation studies treat long-run, single-use problems with given water availability; none tracks site- and time-dependent values across hydrologic conditions (p. 2, [5]).
- Method: SDDP with hydropower and irrigation benefits in the objective; marginal water values = Lagrange multipliers of the reservoir mass-balance equations (abstract p. 1; p. 2 [7], [9]).

## Setting
- **System:** cascade of 7 multipurpose reservoirs with hydropower plants on the Euphrates in Turkey and Syria (Keban, Karakaya, Atatürk, Birecik, Karkamis, Tishreen, Tabqa); irrigation withdrawals at Atatürk, Birecik and Tabqa (Table 1, p. 10). Conventional reservoir hydro; no pumped storage.
- **Markets:** no market model. Energy prices are exogenous short-run marginal costs (SRMC) of the thermal system: about US$40/MWh in Turkey (gas-fired marginal plants) and above US$55/MWh in Syria (oil-fired) (p. 11, [43]). Irrigation benefits from crop yields, farm-gate prices and costs (pp. 10-11).
- **Horizon and resolution:** monthly time step, 5-year horizon (T = 60) (p. 11, [44]). Monthly step motivated as common in mid-term (strategic) hydropower studies (p. 3, [10]).

## Method
- **Model type:** multistage stochastic LP solved by SDDP, maximising expected net benefits from hydropower plus irrigation minus penalties (eqs. 1, 23-31, pp. 3, 6-7). Objective (eq. 1, p. 3) is the expected sum of stage benefits plus a **terminal value function v(u_{T+1})**.
- **How uncertainty is represented:** natural inflows only. Lag-one autoregressive model of monthly inflows, q_{t+1} = mu_{t+1} + rho_{t+1,t} (sigma_{t+1}/sigma_t)(q_t - mu_t) + xi_t sigma_{t+1} sqrt(1 - rho^2), with cross-correlated residuals (eq. 14, p. 5). The previous inflow q_{t-1} is a hydrologic state variable (pp. 3, 5). K = 20 backward openings and M = 20 forward simulation sequences (p. 11, [44]). Forward sequences can be historical or synthetic (p. 5, [18]).
- **Solution method:**
  - SDP recapped first: benefit-to-go F_{t+1}(s_{t+1}, q_t), periodic infinite-horizon recursion to steady state, discretised state grid, effort exponential in the number of reservoirs, unsuitable for more than 3-4 reservoirs (eqs. 3-6, pp. 3-4).
  - SDDP: piecewise-linear outer approximation of F_{t+1} by hyperplanes (Benders cuts) built from primal and dual information of the stage LP (p. 4 [17], p. 5 [19], Fig. 2).
  - Cut construction (pp. 5-6): for a sampled pair (s_{t+1}, q_t), K inflow vectors are generated with (14); the dual of the water-balance constraint gives the storage slope, phi = (1/K) sum_k lambda_w (eqs. 17-18); the slope with respect to the hydrologic state follows from the chain rule through the AR model, using the water-balance and cut duals (eqs. 19-20); constant term eq. 21.
  - Irrigation: "dummy reservoirs" y_t of accumulated water diverted to crops added to the state; benefits only at harvest stage t_f; cuts get an extra slope for y (eqs. 22-34, pp. 6-7, Fig. 3).
  - Bounds and stopping: mean and standard deviation of M simulated benefit sums (eqs. 35-36), 95% CI (eq. 37); stage-1 cut value overestimates benefits (eq. 38); stop when the upper bound lies inside the CI (p. 8, [31]). Converged after 11 iterations (Fig. 6, p. 11).
  - Code: MATLAB with LPSOLVE (p. 8, [32]).
- **Key modelling choices and assumptions:**
  - **Head effects linearised:** hydropower is nonlinear in head and release; to keep the stage problem convex they assume production is dominated by the release term, valid "as long as the difference between the maximum and minimum heads is small compared to the maximum head"; immediate benefit uses a constant production coefficient ch(j) (eqs. 2, 7, p. 5 [20]-[21]). Strongly nonlinear systems need other methods (neuro-DP, Q-learning) (p. 5).
  - Convex (LP) stage problems are required so that the KKT conditions are necessary and sufficient and the duals give the gradients of F_{t+1} (p. 5, [19]).
  - Water balance with spills, evaporation, withdrawals and connectivity matrices for reservoirs and irrigation return flows (eqs. 4, 24, pp. 3, 6); 30% of withdrawn water returns to the river (p. 10, [39]).
  - Short-run values: fixed (capital) costs are sunk and ignored (p. 3 [10], p. 11 [45], p. 15 [54]).
  - Basin-wide coordinated operation of Turkey and Syria assumed (not the real situation) (p. 10, [36]); Iraq excluded for lack of data (p. 15, [53]).
  - How v(u_{T+1}) is set in the case study is not stated (unverified).

## Data / case
- Table 1 (p. 10): Keban 1240 MW / 31.0 km3; Karakaya 1800 MW / 9.58 km3; Atatürk 2400 MW / 48.7 km3 (irrigation); Birecik 672 MW / 1.22 km3 (irrigation); Karkamis 180 MW / 0.157 km3; Tishreen 630 MW / 1.88 km3; Tabqa 880 MW / 14.16 km3 (irrigation).
- 13 state reservoirs in the model: 7 storage reservoirs plus 3 accumulated-water reservoirs for wheat and 3 for cotton (p. 10, [38]).
- Irrigation of more than 1 million ha; gross demand 14,000 m3/ha/yr, i.e. 14.5 km3, about 50% of natural flow at Hit (p. 10, [38]). Crop parameters (Table 2, p. 10): cotton net return US$800/ton, yield 2.4 t/ha, harvest November; wheat harvest July. Yield response via Doorenbos-Kassam (eqs. 39-42, pp. 10-11). Prices from 2003.
- Hydrology: high-flow season from December/spring snowmelt (April-June, about 70% of annual flow), low-flow season from July (p. 10, [37]).

## Key findings
- (p. 2, [7]; p. 11, [45]; p. 15, [52]) Marginal water values are the Lagrange multipliers of the mass-balance equations; they give the change in operational benefits for a small change in water availability, and would equal market prices if water were traded.
- (p. 2, [8]) In hydropower the marginal value of water is key for scheduling releases; a release is optimal when the immediate and expected future water values are equal (citing Wallace and Fleten 2003). Deterministic models tend to overestimate system performance; stochastic models give hedging policies.
- (p. 3, [15], Fig. 1) DP principle: the optimum maximises immediate plus benefit-to-go; the derivatives of the immediate and benefit-to-go functions are the immediate and future water values, which must be identical at the optimum.
- (p. 6, [25]) If irrigation is only a constraint, the multipliers reflect hydropower only, i.e. saved costs of avoided thermal production.
- (pp. 11-12, [46], Fig. 7a, Table A1 p. 15) Average water values fall downstream because upstream water can be reused by every downstream plant (non-consumptive use); Keban's values are more than six times those at Tabqa (e.g. January 46.8 vs 3.8 US$/1000 m3).
- (p. 12, [47]) Water values vary over the year: lower in the high-flow season (March-July), higher in the low-flow season; Keban loses about 30% of its value in the high-flow season.
- (p. 12, [48], Fig. 7b, Table A2) Dispersion (coefficient of variation) of water values is proportional to inflows: peak in May (CV about 0.6-0.7 at all sites), low in the dry season when reservoirs are drawn down; downstream reservoirs show smaller seasonal differences because upstream storage regulates their inflows.
- (p. 12, [49], Fig. 8) Water value at a site = direct (in situ) value + indirect value generated downstream; Atatürk (largest plant and irrigation area) has the largest direct values.
- (pp. 13, 15, [50], Fig. 9) CDFs of water values in May vs November: smaller and more variable in the high-flow season; in May the values at Keban, Karakaya and Atatürk become almost identical about 20% of the time, in wet years.
- (p. 15, [51], Fig. 10) Water values also have a spatial dimension: every unit of lateral inflow into an intermediate catchment has the value of the reservoir that drains it; mapping them can prioritise conservation measures.
- (p. 15, [52]-[55]) The SDDP water value contains two of Rogers et al.'s five value components (marginal value of product, return-flow benefits); results are illustrative; short-run values suit mid-term allocation.

## Strengths
- Clear and explicit link between the SDDP dual information and the economic notion of marginal water value, including how cut slopes are computed from the water-balance duals (pp. 5-6).
- Shows water values as **distributions** (by month and hydrologic condition), not only averages, and explains their seasonal and spatial pattern.
- Clean statement of the "immediate vs future water value" optimality condition with a figure (Fig. 1, p. 4; text p. 3).
- Explicit assumption for linearising head effects and when it is valid (p. 5).
- Maximisation-form SDDP with bounds stated in that direction (pp. 7-8).

## Weaknesses / limitations
- No market prices: electricity valued at an assumed constant SRMC; no price uncertainty or price dynamics.
- No pumping, no reserves, no hourly resolution (monthly stages only).
- Linearised hydropower (constant production coefficient).
- Convergence after 11 iterations with K = M = 20 is a weak statistical test (CI-based stopping rule).
- Terminal value function appears in the objective but its specification is not described (unverified), and end-of-horizon effects are not discussed.
- Minor inconsistency: [57] (p. 16) says Table A2 lists direct water values, but Table A2 (p. 15) is titled "Coefficient of Variation: Monthly Water Values".

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: water value = Lagrange multiplier of reservoir mass balance (shadow price) | Definition, equality with market price if water traded | p. 1 (abstract); p. 2 [7]; p. 11 [45]; p. 15 [52] |
| Theory: immediate vs future water value, optimal release when equal | Verbal statement and Fig. 1 | p. 2 [8]; p. 3 [15]; Fig. 1 p. 4 |
| Theory: water value as derivative of benefit-to-go function | Derivatives of immediate and benefit-to-go functions | p. 3 [15] |
| Theory: SDDP cut slopes from water-balance duals | Eqs. (15)-(21) | pp. 5-6 |
| Theory: convexity / LP needed for dual-based gradients | KKT argument | p. 5 [19] |
| Theory: SDDP in maximisation form (bounds reversed) | Cuts are upper bounds of future benefits; simulated lower bound, CI, stage-1 upper bound | p. 5 [24]; pp. 7-8 eqs. (35)-(38) |
| Theory: terminal value function in the objective | v(u_{T+1}) in eq. (1) | p. 3 [12] |
| Theory: SDP curse of dimensionality (3-4 reservoirs) | Effort proportional to (Ns Nq)^J | p. 4 [16] |
| Model: head effects / constant production coefficient assumption | Release-dominated production valid if head range small relative to max head | p. 5 [20]-[21], eq. (7) |
| Model: AR(1) inflow model with lagged inflow state (TS-SDDP example) | Eq. (14), cross-correlated residuals | p. 5 [24] |
| Results interpretation: seasonal pattern of water values | Higher in low-flow season, lower in high-flow season | p. 12 [47]; Table A1 p. 15 |
| Results interpretation: variability of water values across states | CV peaks in high-flow month; CDFs | p. 12 [48]; p. 13 Fig. 9; Table A2 p. 15 |
| Literature review (modelling-phs-plants): SDDP for multireservoir hydro with water values | Euphrates cascade, monthly, 5 years, K = M = 20, 11 iterations | pp. 8-11 |
| Short-run vs long-run values (capital sunk) | Assumption and justification | p. 3 [10]; p. 11 [45]; p. 15 [54] |

## Useful quotes (with page numbers)
> "the marginal water values are the Lagrange multipliers associated with the mass balance equations" (p. 1, abstract)

Other key statements, paraphrased: a release is optimal when the immediate and expected future water values are equal (p. 2, [8]); the derivatives of the immediate and benefit-to-go functions are the immediate and future water values and must be identical at the optimum (p. 3, [15]).

## Follow-up references to check (backward snowballing)
- Tilmant, A., Kelman, R. (2007). A stochastic approach to analyze trade-offs and risks associated with large-scale water resources systems. Water Resources Research 43, W06425. (Base SDDP model and cut notation.)
- Wallace, S.W., Fleten, S.-E. (2003). Stochastic programming models in energy. Handbooks in OR & MS vol. 10, 637-677. (Water value as key scheduling quantity.)
- Tejada-Guibert, J.A., Johnson, S., Stedinger, J. (1995). The value of hydrologic information in stochastic dynamic programming models of a multireservoir system. WRR 31, 2571-2579. (Hydrologic state variable.)
- Labadie, J.W. (2004). Optimal operation of multireservoir systems: state-of-the-art review. (In repo: `labadie2004`.)
- Scott, T., Read, E. (1996). Modelling hydro reservoir operation in a deregulated electricity market. Int. Trans. OR 3, 243-253.
- Young, R. (2005). Determining the Economic Value of Water. (Deductive valuation methods.)
- Rogers, P., de Silva, R., Bhatia, R. (2002). Water is an economic good. Water Policy 4, 1-17. (Five value components.)

