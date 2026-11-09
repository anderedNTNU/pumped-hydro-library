---
bibkey: helseth2017iet
title: "Assessing hydropower operational profitability considering energy and reserve markets"
authors: "Arild Helseth, Marte Fodstad, Magnus Askeland, Birger Mo, Odd Bjarte Nilsen, Juan I. Pérez-Díaz, Manuel Chazarra, Ignacio Guisández"
year: 2017
venue: "IET Renewable Power Generation, 11(13), 1640–1647"
peer_reviewed: true
methods: [sdp, deterministic-lp-milp, uncertainty-modelling, hydro-production-function]
review_sections: [market-participation, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/21_Helseth_2017_Assessing_hydropower_operational_profitability_considering_energy_and_reserve_markets.pdf
takeaway: "SDP with MILP weekly subproblems (SOS-2 head-dependent PQ curves, unit commitment) and a joint inflow/energy/reserve-price Markov chain for a single Norwegian reservoir (Maudal, NO2); selling primary reserves raises expected operational profit by ~7–11%, steepens water values, and a pure LP overestimates profit by 2–5 percentage points."
---

# Operational profitability with energy and reserve markets (Helseth et al., 2017)

_PDF page 1 = journal p. 1640. Bibkey `helseth2017iet` distinguishes it from `helseth2017` (IET GTD scenario-fan paper)._

## Research question / purpose
How much operational profit (no investment costs) can a hydropower plant expect from selling **energy and spinning reserve capacity**, how do water values change when a reserve market is available, and how large is the error from **linearising non-convex** plant characteristics (head-dependent production function, unit commitment) in the water-value computation and in simulation (abstract, pp. 1640–1641)? The application is a generator reinvestment choice for a Norwegian producer (Lyse) (p. 1641, p. 1643). The model is proposed as a benchmark for linear models such as helseth2016 [17] (p. 1641).

## Setting
- **System:** single reservoir (63 Mm³) and one power station, Maudal watercourse, south-western Norway, price area NO2 (pp. 1643–1644, Fig. 2). Storable and non-storable inflow; minimum river flow requirement (15). No pumping.
- **Markets:** day-ahead energy + **primary reserve capacity** (symmetric, spinning), sold in blocks covering sets of hours, as in the Norwegian weekly primary reserve market (pp. 1642–1643). Reserve product tied to the whole station.
- **Horizon and resolution:** 1 year of weekly decision stages (p. 1641), with hourly-type time steps k within the week (number of steps not stated in the text; unverified). Cyclic end condition (water values at start of year reused at end of year until convergence) (p. 1643).

## Method
- **Model type:** stochastic dynamic programming (SDP, Algorithm 1, Fig. 1) with backward induction; each weekly decision problem is an **MILP** (eqs. 3–19, p. 1642).
- **How uncertainty is represented:** weekly inflow, weekly average energy price and weekly average reserve-capacity price as **Markovian** exogenous states; a discrete Markov chain captures auto- and cross-correlation up to lag 1 (p. 1641–1642). Expected future value = probability-weighted average over the N_E nodes in the next stage (eq. 2).
  - Case data: hourly day-ahead prices sampled from an ARIMA(2,0,3); reserve prices from GARCH(1,1) with ARMA(1,1) mean, both fitted to NO2 data 2013–2015; no significant correlation between day-ahead and reserve prices, so independent models. 1000 samples of each → **15 price nodes per stage (5 energy × 3 reserve)**, using the helseth2016 method (p. 1644).
  - No significant inflow–price correlation in history → separate inflow model; 1000 samples from a VAR(1) model → **5 inflow nodes per stage** (p. 1644).
  - State space per stage: N_P × N_E = 21 × 5 × 15 = 1575 discrete states (p. 1644).
- **Solution method:** loop over N_P = 21 equidistant reservoir levels and all Markov nodes, solve the weekly MILP, compute expected future profit and water values; iterate the 1-year cycle until water values stabilise (7–10 iterations, ~4 h each with MILP) (pp. 1643–1644). AMPL + CPLEX 12.6, MIP gap 1e-5; problem for one week: 1075 variables (443 binary), 800 constraints (p. 1644).
- **Key modelling choices and assumptions:**
  - Risk-neutral price-taker in both markets (p. 1641).
  - **End-of-week volume as a decision variable** ("re-optimisation", Tejada-Guibert et al. [25]); future profit as an SOS-2 combination of discrete values at volume points (eqs. 4–6, 20–21), so the future value function need not be concave (p. 1642).
  - **Head-dependent, non-concave PQ curve** per generator: SOS-2 over M_g discharge points, generation scaled by H/H₀ from initial head (eqs. 8–10, 22–23) (p. 1642).
  - Unit commitment with on/off binaries, P_min/P_max (11)–(12), start-up costs (16) (100 and 50 currency units for the two units, similar to Nilsson & Sjelvgren [27]; currency symbol lost in extraction, likely €) (pp. 1642–1643). Initial spinning state = end-of-week state (17), a simplification with little impact on water values (p. 1643).
  - Reserve as symmetric product: down-regulation (13) Σp − ΣP_min·u ≥ c_b; up-regulation (14) ΣP_max·u − Σp ≥ c_b. Can be relaxed into separate up/down variables (p. 1642–1643). **Water-for-reserve constraint omitted** (as in [17, 26]) since not important in the case (p. 1643).
  - Weekly stages are "the standard approach when computing water values for producers in the Nordic market" (p. 1641).

## Data / case
- Two reinvestment alternatives, both two generators totalling 24.8 MW (p. 1643, Table 1): **Case A** g1 Francis 21.11/6.57 MW (P_max/P_min, M_g = 10) + g2 Pelton 3.71/0.49 MW (M_g = 12); **Case B** g1 Pelton 16.06/2.34 MW + g2 Pelton 8.79/0.97 MW (M_g = 13 each). Francis has higher peak efficiency but cannot run at low output for reserves. Max symmetric reserve sales 8.87 MW (A) and 10.75 MW (B).
- Two modes: **E** (energy only, C_max = 0) and **E+C** (energy + capacity) (p. 1643).
- Three simulation runs over 1000 one-year scenarios sampled from the Markov model (pp. 1644–1645): Run 1 MILP water values + MILP simulation; Run 2 LP water values + LP simulation; Run 3 LP water values + MILP simulation (resembles industry practice).

## Key findings
- (p. 1645, Table 2) Expected profit relative to E mode in run 1: **Case A E+C 107.33% (energy 94.16 + capacity 13.17)**; **Case B E+C 110.78% (92.48 + 18.30)**. Reserve sales always increase total profit; energy revenue falls.
- (p. 1645) Relaxing to LP (run 2 vs run 1) **overestimates** E+C profit by 5.22 (A) and 2.27 (B) percentage points, mostly because reserves can be sold without respecting minimum output and the non-convex production function.
- (p. 1645) LP water values with MILP simulation (run 3 vs run 1) lose 1.03 (A) and 0.64 (B) percentage points: the approximation error from linearising non-convexities in the water-value computation.
- (p. 1644, Figs. 3–5) E+C water values are higher most of the time, **decrease faster with reservoir level** (more spillage risk because future up-regulation sales limit discharge), and are higher at low reservoir levels (water needed to keep units spinning). A pronounced increase around weeks 25–30 is due to expected high primary-reserve prices in summer.
- (p. 1645, Fig. 6) E+C keeps a higher reservoir in late winter (weeks 10–15, before snowmelt) to store water for summer, then uses water more aggressively to keep generators spinning in summer, giving lower levels in autumn/early winter.
- (p. 1645, Figs. 7–8) Units run a larger share of the time in E+C; in case A, g1 operates 30% of the time at ~15.44 MW (max reserve sale 8.87 MW) with g2 at minimum; in case B, g2 runs mainly at minimum to support up-regulation.
- (pp. 1645–1646) Conclusions: less seasonal shifting of energy with a reserve market; water values more sensitive to filling (risk of missing high-price periods and of spillage); linear models significantly overestimate operational profitability; reserve markets should be considered when upgrading plants given long asset lifetimes.

## Strengths
- Joint Markov chain over inflow, energy price and reserve price, with prices fitted to real NO2 market data.
- Exact treatment of non-convexities (MILP in SDP) and a clean three-run design that isolates linearisation error in water values vs simulation.
- Directly links reserve-market access to equipment/configuration choice (Francis vs Pelton mix).
- Reports problem sizes, run times and transparent percentages.

## Weaknesses / limitations
- Single reservoir; SDP does not scale (exponential in states) (p. 1641).
- One-year cyclic horizon assumes stationary prices/inflows.
- Only primary reserves, symmetric, no activation; no water-for-reserve constraint; no intraday.
- Evaluation is in-sample (scenarios sampled from the same Markov model), no historical backtest.
- Price models fitted to only 3 years (2013–2015).
- Profit numbers given only as percentages; no investment costs.
- Text mentions "case D" for problem size (p. 1644), apparently a typo.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (market participation): value of reserves for hydro | +7.33% / +10.78% expected profit with primary reserves | p. 1645, Table 2 |
| Lit review (sizing/capacity): configuration vs reserve value | Francis+Pelton vs two Peltons, same 24.8 MW; Pelton mix earns more reserves | pp. 1643, 1645 |
| Method: joint Markov chain inflow + energy + reserve price | 5 inflow × 15 price nodes; independence tests | pp. 1641–1642, 1644 |
| Method: price models for energy and reserve prices | ARIMA(2,0,3) day-ahead, GARCH(1,1)/ARMA(1,1) reserve prices, NO2 2013–2015 | p. 1644 |
| Limitations: LP overestimates reserve profits | +5.22 / +2.27 pp; 1.03 / 0.64 pp from LP water values | p. 1645 |
| Model: reserve headroom constraints | Up/down symmetric reserve (13)–(14) | p. 1642 |
| Model: head-dependent production function | SOS-2 PQ curves scaled by H/H₀ | p. 1642, eqs. 8–10, 22–23 |
| Model: end-of-horizon value | Cyclic one-year iteration until water values stabilise | p. 1643 |
| Background: weekly stages are standard in Nordic water-value computation | Statement | p. 1641 |
| Results discussion: water values and trajectories with reserves | Steeper water values; higher late-winter storage | pp. 1644–1645, Figs. 3–6 |

## Useful quotes (with page numbers)
> "the linear approximation significantly overestimated the operational profitability" (p. 1646)

> "The use of weekly decision stages is the standard approach when computing water values for producers in the Nordic market." (p. 1641)

## Follow-up references to check (backward snowballing)
- [20] Hjelmeland, Helseth, Korpås (2016), case study on medium-term scheduling with sales of capacity, Energy Procedia 87 (approximation error with reserves).
- [24] Guisández, Pérez-Díaz, Wilhelmi (2016), environmental constraints and water value, Energies.
- [26] Chazarra et al. (2016), weekly scheduling in day-ahead and secondary reserve markets, EPSR.
- [25] Tejada-Guibert, Johnson, Stedinger (1993), re-optimisation in SDP policies.
- [28] Martino et al. (2014), statistical properties of inflow series (VAR(1) inflow).

