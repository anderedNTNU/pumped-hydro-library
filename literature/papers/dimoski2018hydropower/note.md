---
bibkey: dimoski2018hydropower
bibkey_provisional: false
title: "Hydropower reservoir management using multi-factor price model and correlation between price and local inflow"
authors: "Joakim Dimoski, Sveinung Nersten, Stein-Erik Fleten, Nils Löhndorf"
year: 2018
venue: "Paper submitted to the IAEE International Conference 2018 (dated 8 May 2018); NTNU / WU Vienna"
peer_reviewed: false
methods: [sddp-markov-chain, uncertainty-modelling, sdp]
review_sections: [price-volatility, modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/11_Web_search_2026-11-04/dimoski2018hydropower.pdf
takeaway: "Two-reservoir Norwegian plant (Søa, NO3) scheduled over 105 weekly stages with ADDP (SDDP on a 100-node/stage price-inflow lattice built from an HJM multi-factor forward model + GPAR inflow): ignoring the weak price-inflow correlation (rho = -0.18) or using a one-factor price model each cost about 2-3 % of expected revenue."
---

# Multi-factor price model and price–inflow correlation in reservoir management (Dimoski, Nersten, Fleten & Löhndorf, 2018)

_16-page conference paper ("Submitted to the IAEE International Conference 2018", p. 1); page numbers = PDF pages = printed pages. The footnote marks **Sveinung Nersten as lead/corresponding author**, but Dimoski is listed first; `kleiven2023` cites it as "Nersten et al. (2018)". Table 3 is garbled in the extraction; values reconstructed with care._

## Research question / purpose
Build a medium-term (2-year, weekly) scheduling model for a price-taking Norwegian hydropower producer in which (i) spot prices follow a **multi-factor forward-curve (HJM) model** instead of the usual one-factor AR(1), and (ii) price and local inflow are **correlated**. Main contribution: quantify the expected-revenue loss of (a) assuming independence and (b) using a one-factor price model, when the "true" process is correlated and multi-factor (abstract, p. 1).

## Setting
- **System:** Søa hydropower plant (TrønderEnergi), NO3, mid-sized: two reservoirs (Søvatn → Vasslivatn, controllable transfer), one Francis turbine, outlet to Hemnefjorden (p. 7). Conventional, no pumping.
- **Markets:** day-ahead spot only; system price used as proxy for NO3 price (p. 11). Price-taker, complete and arbitrage-free market, risk-neutral measure (p. 3).
- **Horizon and resolution:** 105 weekly stages (2 years); weekly average price; decisions weekly (p. 2, 9, 11).

## Method
- **Model type:** Markov decision process / stochastic DP (Bellman eq. 2, p. 3); linear reformulation (p. 7–8).
- **Objective:** max discounted expected revenue under Q; CF_t = P_t · ρ · w_t with constant energy coefficient ρ (p. 8). Discount factor exp(−rt), r = NIBOR 6-month on 7 Jan 2013 (p. 8).
- **Price model (Sect. 2.2–2.3, p. 4–5):** HJM multi-factor model dF/F = Σ σ_i(T−t) dZ_i, discretised (eq. 10–11); spot = forward with immediate delivery, so the forward curve supplies seasonality and market expectations (no deterministic seasonal function needed) (p. 4). Volatility functions from **PCA** on daily log-returns of historical forward curves by time-to-maturity (Koekebakker & Ollmar 2005 method, continuous returns) (eq. 12–13, p. 5).
- **Inflow model (Sect. 2.4, p. 5–6):** geometric periodic AR(1) (GPAR, Shapiro et al. 2013): AR(1) on deviations of log inflow from weekly mean, φ_t and σ_t week-dependent (eq. 14–19). Lognormal-type, no negative inflows.
- **Correlation:** between the inflow error term and the **first principal component** only (other factors uncorrelated) (p. 10).
- **Scenario lattice (Sect. 2.5, p. 6):** Löhndorf & Wozabal (2017): Monte Carlo paths → nodes per stage by **minimising Wasserstein distance**; transition probabilities by counting simulated paths moving between nearest nodes. Constant nodes per stage (vs exponential growth of trees).
- **Solution method:** **ADDP** (Löhndorf, Wozabal & Minner 2013) = SDDP-type outer approximation (cuts) of value functions on the scenario lattice, via the QUASAR solver (p. 6–7).
- **Key modelling choices and assumptions:**
  - **Constant head and efficiency** → constant energy coefficient (linear objective). Justified for high-head plants (>250–300 m, citing Madani & Lund 2009); at Søa (273.1 m production-weighted head) the power error is within ±3.7 % (p. 8).
  - Only aggregated inflow known; split by historical share (39.5 % Vasslivatn, 60.5 % Søvatn) (p. 8).
  - Summer minimum level at Søvatn (25 May–15 Oct) as soft constraint with a large penalty slack (p. 8).
  - **No end-of-horizon water value or end-level constraint**: reservoirs are emptied in the last stage (p. 12); authors argue first-stage decisions are unaffected.
  - No start-up costs (cash flow = revenue) (p. 3).

## Data / case
- **Plant (Table 1, p. 7):** max power 36 MW; mean yearly production 191.3 GWh; average yearly inflow 311 Mm³ (60.5 % to Søvatn, 39.5 % directly to Vasslivatn); energy coefficient 0.6748 kWh/m³; turbine capacity 17 m³/s.
- **Reservoirs (Table 2, Table 3, p. 7–8):** Vasslivatn 260.00–279.83 masl (max 44.5 Mm³); Søvatn 275.00–279.83 masl (max 22.5 Mm³), regulatory min 278.33 masl 25 May–15 Oct (≈ 15.05 Mm³ in Table 3); weekly seconds τ = 604,800; r ≈ 0.0198 (Table 3, reconstructed).
- **Forward data (p. 8):** NASDAQ Commodities weekly, monthly, quarterly, yearly contracts, 28 Apr 2011 – 30 Dec 2016, 1,450 forward curves (linear interpolation); returns matrix 1449 × 104.
- **Inflow data (p. 10):** daily inflow 1958–2016.
- **Lattice:** 380,000 Monte Carlo paths; **100 nodes per stage**, 10,401 nodes in total; 50,000 simulated evaluation paths (p. 11–12).

## Key findings
- (p. 9, Table 5) First PC explains **73 %** of forward-return variance; 2 → 88 %, 3 → 92 %, 6 → **96 %** (6 factors used). Overall volatility decreases with maturity (**Samuelson effect**); strong inter-correlation decaying with maturity spread (Fig. 3–4).
- (p. 10) Inflow: right-skewed; PACF significant only at lag 1 → AR(1) sufficient; spring snow-melt peak and autumn rain peak (Fig. 7).
- (p. 10–11) **Pearson correlation between weekly inflow residual and first PC = −0.1765** (248 weeks, 95 % CI [−0.28, −0.06]): weak negative.
- (p. 12, Table 6) Expected discounted revenue 13.8–16.0 M€ over 105 weeks for five start dates; first-week production zero in some winter starts because forward curve signals higher prices ahead (value of waiting).
- (p. 12–13) **Backtest** 7 Jan 2013 – 11 Jan 2015: model 11.69 M€ vs realised 10.89 M€ (≈ +0.4 M€/yr), partly due to end-of-horizon emptying; first 52 weeks 6.34 vs 6.22 M€; revenue per MWh 38.92 vs 39.00 €/MWh. Model is "less risk-averse than the real-life production planner" (p. 12). Real planner has hourly decisions, intraday market and weather forecasts; model has no maintenance (p. 13).
- (p. 13, Table 7) EDR with ρ = 0 / −0.18 / −0.35: 16.10 / 15.93 / 15.83 M€.
- (p. 14, Table 8) Policy built with ρ = 0, evaluated where true ρ = −0.1765 / −0.353: **−2.5 % / −3.1 %** expected revenue.
- (p. 14, Tables 9–10) More factors → higher EDR (15.80 with 1 factor to 16.00 with 10). One-factor policy evaluated on 3/6/10-factor processes: **−2.1 % / −2.0 % / −2.3 %**.
- (p. 15) Conclusion: correlation and multi-factor price dynamics both matter (≈ 2–3 %, "multiple 100,000 EUR yearly"); Nordic forwards need more factors than typical commodities (confirming Koekebakker & Ollmar 2005).

## Strengths
- Combines market-consistent (forward-based, risk-neutral) price scenarios with a realistic two-reservoir plant and an SDDP-on-lattice solver.
- Quantifies misspecification losses by evaluating a policy on a lattice generated from a different ("true") process.
- Includes a backtest against real operation.

## Weaknesses / limitations
- Conference paper, not peer-reviewed journal version (unverified whether a later journal version exists).
- Correlation is a single Pearson coefficient with the first PC only; `kleiven2023` later finds much smaller losses (0.17–0.30 %) with a structural hydrology-price model and explicitly contradicts this paper's 2.5–3.1 %.
- Loss comparison: the ρ = 0 policy and the true-ρ policy use different lattices; node placement differences may contribute to the gap (our concern, not discussed by the authors).
- No end-of-horizon water value; reservoirs emptied at T (p. 12).
- Constant head; weekly average prices (no intra-week flexibility); system price instead of NO3 price.
- Backtest favours model partly through end-of-horizon emptying.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.5: Nordic forward volatility structure | 1st PC 73 %, 6 factors for 96 %; Samuelson effect | Table 5, Figs. 3–4, p. 9 |
| Background 2.5: weak negative price–inflow correlation | ρ = −0.1765, CI [−0.28, −0.06], weekly, 2011–2016 | p. 10–11 |
| Method: lattice / Markov-chain construction | Monte Carlo → Wasserstein-optimal nodes; transition counting; 100 nodes/stage | Sect. 2.5 p. 6; Sect. 3.6 p. 11 |
| Method: SDDP on Markov lattice (ADDP) | Cuts on lattice nodes, forward/backward passes | Sect. 2.6, p. 6 |
| Method: inflow process | GPAR (log AR(1) with weekly mean, φ_t, σ_t); PACF lag-1 | Sect. 2.4 p. 5–6; Sect. 3.4 p. 10 |
| Method: constant head assumption | Valid for high-head plants >250–300 m; ±3.7 % error at 273 m | p. 8 |
| Method: end-of-horizon effects | No end value → reservoirs emptied; argue first-stage unaffected | p. 12 |
| Lit. review 5.3: value of price–inflow correlation | 2.5–3.1 % loss if ignored | Table 8, p. 14 |
| Lit. review 5.3: value of multi-factor price model | ≈ 2 % loss with one factor | Table 10, p. 14 |
| Lit. review 5.6 research gap | Conflicts with Kleiven 2023 (0.17–0.30 %); nothing on PHS | p. 14–15 |
| Evaluation design: backtest vs real operation | Policy applied to realised prices/inflows, compared with plant income | Sect. 3.8, p. 12–13 |

## Useful quotes (with page numbers)
> "if the real correlation is ρ = −0.1765, the policies will provide expected discounted revenues that are 2.5% lower than if the policies incorporated this correlation." (p. 14)

## Follow-up references to check (backward snowballing)
- Löhndorf, Wozabal & Minner (2013), Operations Research 61(4): ADDP for hydro storage trading.
- Löhndorf & Wozabal (2017): lattice construction / QUASAR (indifference pricing of gas storage).
- Koekebakker & Ollmar (2005), Managerial Finance: Nordic forward curve dynamics (>10 factors).
- Shapiro, Tekaya, da Costa & Soares (2013), EJOR: GPAR inflow model, risk-averse SDDP.
- Mo, Gjelsvik & Grundt (2001), Porto PowerTech: price modelling in hydro operation (`mo2001`).
- Boger, Fleten, Pichler, Keppo & Vestbøstad (2017), IAEE: local vs national inflow correlation.
- Fleten & Lemming (2003), Energy Economics: forward curve construction.

