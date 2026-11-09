---
bibkey: helseth2013
title: "A model for optimal scheduling of hydro thermal systems including pumped-storage and wind power"
authors: "Arild Helseth, Anders Gjelsvik, Birger Mo, Úlfar Linnet"
year: 2013
venue: "IET Generation, Transmission & Distribution, 7(12), 1426–1434"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "SINTEF system-level SDDP for medium/long-term hydro-thermal scheduling (weekly stages, intra-week sub-periods) with VAR(1) inflow, exogenous price as discrete Markov states (SDP-in-SDDP), DC power flow and linearised pump start-up costs; Icelandic case shows grid constraints and pump start-up costs change PHS and cable use."
---

# Hydro-thermal SDDP with pumped storage and wind (Helseth et al., 2013)

## Research question / purpose
Extend an existing SINTEF SDDP-based model for stochastic hydro-thermal scheduling (Gjelsvik, Belsnes, Haugstad 1999 [13]) with three features (p. 1426): (1) linearised (DC) power-flow constraints and nodal prices; (2) approximate, linear start-up costs for generating units and **pumps**, whose operating state enters the SDDP cuts; (3) wind power as energy time series with at least hourly resolution, treated stochastically in the forward simulation (and optionally in the backward recursion). The model is meant for medium- and long-term scheduling with a fine time resolution (p. 1426–1427).

## Setting
- **System:** whole hydro-thermal power system with multiple reservoirs: the Icelandic system (Landsvirkjun data, transmission data from Landsnet), 12 hydro plants in 5 watercourses, plus planned expansions (p. 1431, Table 1).
- **Markets:** no explicit market products. A single **exogenous market price** (UK via a planned 350 MW HVDC-light cable) is stochastic; power can be bought/sold as price-quantity options; nodal prices come out as duals (pp. 1428, 1430–1431). No reserves, no intraday.
- **Horizon and resolution:** typical horizon 3–5 years, **weekly stages**, each week split into K sub-periods: "aggregate" (hours lumped by load level) or "sequential" (chronological) (p. 1427). Case study: 169 weeks (from week 40, full reservoirs, to end of year 4), 7 aggregate or 24 sequential sub-periods per week (p. 1431).

## Method
- **Model type:** multistage stochastic LP, objective = maximise expected income from sales minus generation and purchase costs, with end-of-horizon water value F(V_T) (eq. 1, p. 1427). Weekly subproblem eqs. 2–8 (p. 1427).
- **How uncertainty is represented:**
  - *Inflow:* normalised inflow z_t follows a **lag-1 vector autoregressive model** z_t = Φ z_{t−1} + ε_t, with the noise taking N_V discrete values; inflow q_t = Q_t z_t + μ_t (eqs. 3–4, 9, p. 1427). Negative inflows can arise; they are kept (convexity) and compensated by high-cost artificial variables (p. 1427).
  - *Exogenous price:* given as equally probable price scenarios (at least one per inflow/wind scenario). **Forward pass uses the scenarios directly; backward pass uses a Markov chain** estimated from the scenarios (method in Mo et al. 2001 [26]) (p. 1429). The price dimension is handled "in an SDP manner": the backward step for each week is repeated N_P times, once per discrete price state (p. 1429). This is the SDP/SDDP hybrid that is the forerunner of Markov-chain SDDP.
  - *Wind:* historical hourly records in the forward pass. Optional backward model: weeks grouped by weekly wind energy into N_W groups with given probabilities, so N_V × N_P × N_W outcomes per week (p. 1430). Assumes wind independent of other variables and of previous weeks, and known for the whole week (p. 1430). Case study uses **mean wind in the backward recursion** (p. 1430, 1433).
  - *Forward scenarios:* historical records of inflow, price and wind, each historical year equally probable from the start week, updated by the current state (e.g. snow); this preserves correlations not captured by the stochastic models (pp. 1429–1430).
- **Solution method:** SDDP (sampling-based multistage Benders) combined with SDP over price states (p. 1429). Cuts α_t + κ^T V_t + μ^T z_t (+ γ^T u^L) ≥ β, i.e. reservoir volumes, inflow state and pump/unit operating states are cut variables (eqs. 6, 20–24, pp. 1427, 1430). Cut sharing across forward scenarios is valid under the lag-1 inflow model (Infanger & Morton [27], p. 1429). Convergence: compare forward sample cost with backward lower bound; in practice stop after a fixed maximum number of iterations or when trajectories stop changing (p. 1429). Cuts and power-flow constraints are added by relaxation (only when violated) (p. 1430). Parallel processing; CPLEX 11 (p. 1433).
- **Key modelling choices and assumptions:**
  - Stochastic variables are known for the whole week at its start (p. 1427, 1429); the authors note this is too coarse to capture real wind-balancing needs (p. 1430).
  - Hydropower: piecewise-linear conversion factors (matrix A_k) in the power balance (eq. 10, p. 1428); no explicit head model is described (unverified whether head effects are included).
  - A "dump" option at negligible income at each busbar keeps nodal prices positive so the piecewise-linear efficiency curve is loaded in the right order (p. 1428).
  - **Pumps:** simplified model with min and max pumping capacity (p. 1428). Start-up costs with a **continuous** operating state u^L ∈ [0,1] instead of binaries (binaries would break the convexity SDDP needs and cost much computation time) (eqs. 14–19, p. 1428). The aim is the general effect on operation and prices, not accurate unit commitment (p. 1428).
  - DC power flow with PTDFs (eqs. 11–13, p. 1428); quadratic losses possible but not addressed.

## Data / case
- Iceland 2008: 16.5 TWh, ~70 % hydro, ~30 % geothermal (geothermal subtracted from load) (p. 1431). Landsvirkjun: ~1750 MW in 11 stations; 87 % of consumption is power-intensive industry with a flat profile (p. 1431).
- Table 1 (p. 1431): Laxá 1 plant, 18 MW, 0 Mm³ (b1); Thjórsá/Sog 7 plants, 1068 MW, 2028 Mm³ (b4); Blanda 1 plant, 150 MW, 420 Mm³ (b10); Kárahnjúkar 2 plants, 677 MW, 2148 Mm³ (b11); **Vörðufell PHS 1 plant, 100 MW, 20 Mm³** (b4); total 12 plants, 2013 MW, 4616 Mm³.
- Expansions (p. 1431): 350 MW HVDC-light to UK at b4 (UK price as exogenous series, one per inflow/wind record); Vörðufell pumped storage, 100 MW with 20 Mm³ upstream and downstream storage; 100 MW wind park.
- 54 historical weather scenarios; inflow daily, wind hourly (p. 1431). Backward: 12 inflow noise levels × 7 price states = 84 outcomes per week; max 60 SDDP iterations; 54 × 169 = 9126 subproblems per forward pass (p. 1433).
- Cases (Table 2, p. 1431): A aggregate, no power flow, no PHS start-up cost; B aggregate + power flow; C sequential, no power flow; D sequential + power flow; E sequential + power flow + PHS start-up cost.

## Key findings
- (p. 1432, Fig. 3) With grid constraints (B vs A) the large Hálslón reservoir is kept higher and the risk of emptying it in extreme cases is lower, because its bus sees less of the export option.
- (p. 1432, Fig. 4) Sigalda (160 MW, large upstream storage) follows UK prices: up at daytime peaks, down at night and weekends. Nodal prices at b4 follow UK prices except at peaks (limited HVDC capacity).
- (p. 1432, Fig. 5) Maximum export on the HVDC cable 67 % of the time in case A, 62 % in B. Cases A–C overestimate cable use (export and import) and thus cable profitability; fine time resolution plus power flow (D, E) is needed.
- (p. 1432–1433, Fig. 6) Adding a pump start-up cost (case E; with a 30 MW minimum for the PHS) reduces pump use. Switching from generating to pumping occurs in 6.54 % of sub-periods in D vs 0.12 % in E. The pump still runs a lot below its minimum capacity, so the approximation is "not perfect" (p. 1432). Start-up costs raise mean and standard deviation of the b4 nodal price by 0.34 % and 11.12 % (p. 1433).
- (p. 1430) Initial tests: wind stochasticity in the backward pass has little effect on the strategy in systems with large storage and a modest wind share.
- (p. 1433) Run time on 12 cores: case A ~5 h, case E ~31 h; the increase comes mainly from the larger LP per stage with sequential sub-periods.
- (p. 1433) Conclusion: finer time resolution and more system constraints give more realistic simulations; ignoring power flow overestimates export capability and gives unrealistic reservoir operation; pump start-up costs change PHS schedules and prices.

## Strengths
- Shows how an exogenous stochastic price can be added to SDDP as a **discrete Markov chain with SDP over price states**, keeping convexity (p. 1429) — the same idea we use (Markov-chain SDDP).
- Combines stochastic models in the backward pass with historical scenarios in the forward pass (p. 1429–1430), a design worth contrasting with our out-of-sample evaluation.
- Convex (LP) treatment of pump start-up costs compatible with SDDP, with an honest evaluation of its imperfection.
- Large realistic case with several model variants (A–E).

## Weaknesses / limitations
- System cost/income perspective, not a single price-taking PHS owner; PHS is a small part of the case.
- Pumps modelled only by min/max capacity; no head dependence described for pumping (unverified).
- No reserve or intraday markets; within-week information is perfect.
- Wind stochasticity is effectively ignored in the strategy (mean in backward pass) in the reported results.
- Convergence assessed loosely (fixed max of 60 iterations; no reported gap).
- Markov-chain estimation for prices is only referenced ([13], [26]), not described.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDDP vs SDP (curse of dimensionality, cuts) | Short history: water value method (SDP), SDDP allows many more state variables | p. 1426, Introduction |
| Theory/method: Markov-chain price in SDDP | Price as Markov chain in backward pass, SDP over N_P price states | p. 1429, Sec. 2.5 and 3.1 |
| Method: inflow model in cuts | Lag-1 VAR inflow, inflow state in cuts, negative-inflow handling | p. 1427, eqs. 3–4, 6, 9 |
| Method: forward pass on historical scenarios | Forward simulation uses historical inflow/price/wind records to keep correlations | pp. 1429–1430, Sec. 3.2 |
| Method: convergence in practice | Upper/lower bound comparison; stop after max iterations | p. 1429 |
| Model: weekly stages with sub-periods | Aggregate vs sequential sub-periods; values known within week | p. 1427, Sec. 2.1 |
| Lit review (modelling PHS): PHS in system SDDP | Vörðufell 100 MW PHS; linearised pump start-up costs and effect on pump use | p. 1428 (Sec. 2.4), p. 1431–1433 |
| Lit review: limitation of weekly stochastic resolution | Week-long stochastic resolution too coarse for wind balancing | p. 1430 |
| Lit review: importance of grid/time resolution | Without power flow / with aggregate sub-periods, export and cable value overestimated | p. 1432, Fig. 5 |
| Comparison table row | System, SDDP (+SDP price states), inflow/wind/price uncertainty, no explicit markets | whole paper |

## Useful quotes (with page numbers)
> "a Markov chain model is used to describe the stochastic price" (p. 1429)

> "the approximate modelling is not perfect" (p. 1432)

## Follow-up references to check (backward snowballing)
- [13] Gjelsvik, Belsnes, Haugstad (1999), SDDP medium-term scheduling under spot price uncertainty, PSCC (origin of SDDP with Markov price states).
- [26] Mo, Gjelsvik, Grundt, Kåresen (2001), hydropower in a liberalised market with focus on price modelling, PowerTech (Markov-chain estimation).
- [18] Gjelsvik, Mo, Haugstad (2010), Handbook of Power Systems I chapter on SDDP in hydro-dominated systems.
- [17] Røtting & Gjelsvik (1992), SDDP for seasonal scheduling in Norway.
- [15] Warland, Haugstad, Huse (2008), start-up costs in long-term hydro-thermal model.
- [27] Infanger & Morton (1996), cut sharing with interstage dependency.

