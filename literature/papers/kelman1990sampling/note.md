---
bibkey: kelman1990sampling
bibkey_provisional: true
title: "Sampling Stochastic Dynamic Programming Applied to Reservoir Operation"
authors: "Jerson Kelman, Jery R. Stedinger, Lisa A. Cooper, Eric Hsu, Sun-Quan Yuan"
year: 1990
venue: "Water Resources Research, 26(3), 447-454"
peer_reviewed: true
methods: [sdp, uncertainty-modelling, heuristics-simulation]
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDP_i_vannkraft/Kelman1990.pdf"
takeaway: "Introduces sampling SDP (SSDP): instead of a fitted, discretised Markov inflow model, the expectation in the SDP recursion runs over M historical 12-month streamflow scenarios (57 years, PG&E Feather River, 35 storage states), optionally with a seasonal-forecast hydrologic state; matches a deterministic NLP under perfect foresight (0.09% gap), beats a trial-and-error rule curve, and forecasts add 0.2-2.5% value depending on the objective."
---

# Sampling SDP for reservoir operation (Kelman et al., 1990)

> **Text file note:** the PDF is a scan (CCITT images, author's website copy). `paper.txt` from `pdftotext` is **empty**. This note was written from the page images (journal pp. 447–454 = PDF pp. 1–8). Search the PDF, not the txt.

## Research question / purpose
How can a reservoir operating policy be derived by SDP that captures the complex temporal and spatial structure of streamflows (high cross-correlation among sites, autocorrelation, multimonth persistence) and uses the best available inflow forecast, without imposing a parametric streamflow model? The paper develops **sampling SDP (SSDP)**, in which the inflow distribution is represented implicitly by a large set of sample streamflow sequences (abstract, p. 447).

It lists five reasons why river-basin operation is hard (p. 447): uncertain future inflows; releases depend on local inflows to downstream powerhouses; high spatial correlation with varying autocorrelation; available streamflow forecasts; and **head effects plus daily/monthly load variation make the value of energy nonlinear in turbine flow**.

## Setting
- **System:** PG&E's North Fork Feather River hydroelectric system, California: one dominant reservoir (Lake Almanor, 1143 TAF ≈ 1406 × 10⁶ m³) upstream of a cascade; 10 powerhouses, 9 reservoirs, 11 inflow points (p. 448; Fig. 1 and Table 1, p. 451). Conventional hydro, **no pumping**.
- **Markets:** none. The objective is energy weighted by "subjective coefficients" c_t per month, which represent relative energy values (Tables 2 and 4, pp. 452–453). Benefit functions include avoided thermal costs and capacity benefits in the general formulation (p. 448).
- **Horizon and resolution:** annual cycle of T = 12 monthly stages (p. 449). The boundary value is iterated over years (p. 449).

## Method
- **Model type:** SDP over storage (and optionally a hydrologic state). Decision is the **target release** R*_t (or target end storage); actual release R_t is clipped by storage bounds (Eq. 4, p. 448).
- **How uncertainty is represented:**
  - M streamflow **scenarios**, each a historical (or synthetic) 12-month sequence of all local inflows (p. 449). The joint spatial and within-year temporal distribution is taken directly from the sample (pp. 449–450).
  - Value function f_t(k, l, i) is indexed by storage k, forecast class l **and scenario i** (p. 449). Recursion Eq. (5): max over R* of Σ_i P_t(i|l)[B_t + α Σ_v PX_t(v|l,i) f_{t+1}(S_{t+1}, v, i)] (p. 449).
  - Scenario-to-scenario transitions between years, P_scenario(j|i), can encode a lag-1 Markov model of annual flows. In the case study year-to-year correlation was small, so P_scenario = 1/M (p. 449).
  - A **hydrologic state variable** X_t (forecast of remaining snowmelt runoff, or previous month's flow) is discretised into L classes. P_t(i|X_t) is computed with **Bayes' theorem** from the regression of forecasts on actual seasonal flow (Eq. 10, p. 450). Forecast-to-forecast transitions PX_t(v|l, i) also use Bayes (Eq. 11, p. 451).
  - With M = 1 SSDP reduces to deterministic DP; with L = 1 it is the no-forecast case (Eq. 8, p. 450).
- **Solution method:** backward recursion t = T,…,1 over K storage × L forecast states, then repeat with the boundary condition updated from the previous iteration (p. 449). A simple **simulation model** routes flows through the cascade to compute energy for a given Almanor release and the 11 inflows (p. 451).
- **Key modelling choices and assumptions:**
  - Only Lake Almanor storage is a state variable. The other reservoirs' carryover fraction (Δ) is set equal to Almanor's (the "Δ simplification", p. 451).
  - **End-of-horizon value:** initially zero, or "potential energy of stored water times the average value of energy" (p. 449). In the case study, iteration 1 used storage × total average water duty, and later iterations used the January value from the previous iteration; policy converged after 2 iterations (p. 452).
  - **Head effects:** water duty varies with Almanor level only for Butt Valley powerhouse; the others have constant heads (p. 451).
  - Minimum energy requirement per powerhouse via minimum capacity factor (~10% summer, ~8% other months) (pp. 451–452).
  - Monthly discount factor α (p. 449).

## Data / case
- 57 historical 12-month streamflow scenarios and 35 storage states (p. 452).
- Historical forecasts of Lake Almanor inflow 1950–1984 used to build P_t(i|X_t) (p. 453).
- Forecast state: L = 5 classes at standard normal quantiles ±1.72, ±0.76, 0 with probabilities 0.107, 0.245, 0.296 (p. 453).
- State variable by month (Table 3, p. 453): seasonal forecast X_t Jan–June; previous month's flow Q_{t−1} July–Sept; none Oct–Dec.

## Key findings
- (p. 450) Advantage 1 of SSDP: avoids imposing a specific streamflow model and avoids discretising a fitted continuous distribution and describing persistence by a Markov chain, "a process almost certain to underestimate the severity of droughts". The implicit Thomas–Fiering model in most SDP gives very little year-to-year correlation.
- (p. 450) Advantage 2: captures the full joint empirical distribution of within-year flows at all sites without increasing the dimension of the hydrologic state.
- (p. 452) **Perfect-foresight check:** with a single scenario of mean monthly inflows, SSDP and PG&E's deterministic NLP model HYSS gave nearly identical storage paths (Fig. 2) and objective values 4395 vs 4391 (0.09%). So the Δ simplification does not noticeably degrade the policy.
- (pp. 452–453) **No-forecast case vs rule curve:** release rules for various minimum Almanor storage levels were tested in PG&E's daily planning simulation model. SSDP produced a slightly better rule than the trial-and-error rule curve, and rules for other minimum levels, "with much less time and effort" (Fig. 3).
- (p. 453) Marginal scenario probabilities from Eq. (10) deviated from 1/M because the streamflow record was longer than the forecast record. Fixed by adjusting priors with a first-order Newton scheme.
- (pp. 453–454) **Value of forecasts** (Table 5): with all c_t = 1 (pure energy maximisation), forecasts add < 0.4%. With realistic relative energy values (high summer/fall, low May; Table 4), forecasts add **1.5–2.5%**, increasing with the minimum storage level; "more than one million dollars per year".
- (p. 453) SSDP release rules keep Almanor storage low so winter and spring inflows can be stored and used when spills are less likely; about half of basin inflow enters below Almanor and is essentially uncontrollable monthly.
- (p. 454, conclusion) The value of forecasts depends on the objective function and system configuration. SSDP is useful at PG&E because it generates efficient policies for alternative and proposed configurations faster than trial-and-error rule curves.

## Strengths
- Simple, transparent way to use the empirical joint distribution of inflows (and, by extension, any correlated stochastic inputs) in SDP.
- Clean validation design: reduce to perfect foresight and compare to a deterministic optimiser; then compare to the incumbent rule in the operator's own simulation model.
- Shows that the value of information depends on how differentiated the objective (prices) is across seasons.

## Weaknesses / limitations
- Single main state reservoir; Δ simplification for the rest.
- No electricity prices or market; energy values are subjective coefficients.
- The value function is indexed by scenario, so state space grows with M; the paper does not report run times.
- Monthly resolution; no within-month operation, no pumping.
- Results are in relative units ("value of energy"), so economic magnitudes are hard to compare.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory / lit review: SDP variants for reservoirs | Definition of sampling SDP; recursion with scenario index | pp. 448–450, Eqs. (3), (5)–(9) |
| Limitation: Markov chain may understate persistence / droughts | Explicit critique of discretised Markov-chain inflow models | p. 450 (Advantages of SSDP, item 1) |
| Uncertainty modelling: empirical scenarios vs fitted model | SSDP uses historical 12-month traces of all sites | pp. 449–450, p. 454 |
| Model: end-of-horizon value | Zero, or storage × average energy value, then iterate boundary | p. 449 (Boundary Condition); p. 452 |
| Validation design | One-scenario SSDP vs deterministic NLP (0.09% gap) | p. 452, Fig. 2 |
| Benchmark vs rule curve | SSDP rules vs trial-and-error rule curve in daily simulation | pp. 452–453, Fig. 3 |
| Value of information / forecasts | 0.2–0.4% (flat values) vs 1.5–2.5% (seasonal values) | p. 453, Tables 4–5; p. 454 |
| Head effects in early SDP | Head variation only for one powerhouse; value of energy not linear in flow | p. 447; p. 451 |

## Useful quotes (with page numbers)
> "a process almost certain to underestimate the severity of droughts" (p. 450, on discretised Markov-chain inflow models)

## Follow-up references to check (backward snowballing)
- Stedinger, Sule & Loucks (1984), WRR 20(11) — forecast as hydrologic state (filed as `stedinger1984stochastic`).
- Yeh (1985), WRR 21(12) — review (filed as `yeh1985reservoir`).
- Yakowitz (1982), WRR 18(4) — already `yakowitz1982`.
- Pereira, Oliveira, Costa & Kelman (1984), "Stochastic streamflow models for hydroelectric systems", WRR 20(3).
- Araujo & Terry (1974); Dias, Pereira & Kelman (1985) — earliest SSDP applications.
- Faber & Stedinger (2001), J. Hydrol. 249 — SSDP with ensemble streamflow forecasts (cited by Wu et al. 2018).

