---
bibkey: chazarra2018
title: "Optimal Joint Energy and Secondary Regulation Reserve Hourly Scheduling of Variable Speed Pumped Storage Hydropower Plants"
authors: "Manuel Chazarra, Juan Ignacio Pérez-Díaz, Javier García-González"
year: 2018
venue: "IEEE Transactions on Power Systems, 33(1), 103–115 (doi:10.1109/TPWRS.2017.2699920)"
peer_reviewed: true
methods: [two-stage-stochastic, risk-averse-cvar, deterministic-lp-milp, hydro-production-function, uncertainty-modelling]
review_sections: [market-participation, modelling-phs-plants, phs-technology, reservoir-sizing-capacity]
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/Innlimte_referanser_2026-10-29/chazarra2018.pdf"
takeaway: "Scenario-based, CVaR-weighted daily MILP for a closed-loop daily-cycle PHS in the Iberian day-ahead + secondary regulation (aFRR-type) markets; variable-speed units that can hold reserve while pumping raise real income by 97–163 % vs fixed speed, reserve capacity is the main revenue source, and indicative payback falls from 5–36 to 3–16 years."
---

# Variable-speed PHS in joint energy and secondary reserve scheduling (Chazarra et al., 2018)

Journal page = PDF page + 102 (article runs pp. 103–115). Tables I–III (p. 110) are images and did not extract to text; the numbers below come from the running text.

## Research question / purpose
(1) Formulate an MILP for the hourly joint energy and secondary regulation reserve scheduling of a realistic **closed-loop, daily-cycle, price-taking variable-speed (VS) PSHP**, with uncertainty in day-ahead and reserve prices and **risk aversion (CVaR)**; (2) quantify how much VS technology (synchronous vs doubly-fed asynchronous machines, with or without bypassing the converter in generating mode, with and without perfect information) raises income compared with a fixed-speed (FS) plant, in the day-ahead market (DM) alone and in DM + the Spanish secondary regulation service (SRS) (abstract p. 103; p. 104). It complements the authors' hydraulic short-circuit paper (`chazarra2017`) and extends their 2014 EEM conference version (p. 104–105).

## Setting
- **System:** single closed-loop PSHP (no inflow to upper reservoir, no release from lower; footnote p. 104), two identical reversible Francis pump-turbines, single penstock (so no simultaneous pumping and generating, eq. 43, p. 108). Partly based on Guillena PSHP (Spain): gross head 244 m (high) / 219 m (low), upper reservoir 0–2.21 Mm³, flows set to empty the reservoir in at least **5.95 h**; hydraulic losses 3 % of gross head (p. 109). Two Hill diagrams (Raabe textbook; Mt. Elbert PSHP) give 8 cases: FS, VS (synchronous + full converter, 98 % electrical efficiency), B (converter bypassed when generating, as at Grimsel II), VS-A (doubly fed asynchronous, 99.7 %) (p. 109).
- **Markets:** Iberian DM + Spanish SRS = day-ahead reserve capacity market cleared after the DM, paid at marginal price, plus real-time delivery paid at the tertiary regulation price (p. 105). The paper notes similar secondary-regulation procurement in Norway, Sweden, Finland and others (short-term, < 1 week) and Denmark, Netherlands, Germany etc. (long-term, > 1 week), citing an ENTSO-E 2014 survey (p. 105). TSO-set up/total ratio R_t^SM imposed (eq. 38, p. 108).
- **Horizon and resolution:** daily 24-hour problems, run day by day over one representative week with initial = final upper-reservoir volume 1.105 Mm³ (half full) (p. 109). Sensitivity day 11/11/2014 (pp. 112–113).

## Method
- **Model type:** MILP. Objective (1)–(2) maximises (1−β)·expected net income + β·CVaR (p. 106); net income = regulation-up energy income − regulation-down energy cost + DM net energy revenue + reserve capacity revenue (up and down, in generating **and pumping** modes) − start-up costs.
- **How uncertainty is represented:** **100 equiprobable scenarios**, each a 24-h DM price profile combined with a 24-h reserve price profile: 10 × 10 representative profiles obtained by sampling 500 profiles from a GARCH-ARIMAX model (DM, MAPE 17.8 % in 2014) and a SARIMAX model (reserve price, MAPE 21.2 %), then clustering (p. 109). All decisions are taken in **one stage** (no recourse), justified because DM clearing reveals little about reserve prices (correlation −0.47 in 2013) (p. 106). Prices chosen as uncertain because their value of perfect information is significant: DM price VPI up to 26 % of maximum theoretical income with SRS participation, 36 % with DM only; reserve-price VPI up to 10 %; VPI of regulation-energy prices and activation much smaller (unpublished) (p. 106). Activation and energy prices deterministic (historical).
- **Risk:** VaR/CVaR via Rockafellar–Uryasev linear constraints (eqs. 3–4, p. 106); β = 0.1, α = 95 % in the case study (p. 109).
- **Solution method:** CPLEX branch and cut; 3–17 min per daily problem, ~100 min per week and case (p. 109).
- **Key modelling choices and assumptions:**
  - Water balance of upper reservoir only (eq. 5); lower reservoir omitted; **target end volume** equal to initial (eq. 7, p. 107). Extension to open loop (inflow + lower reservoir) said to be easy (p. 107).
  - **Head dependency:** two I/O curves (k1, k2) for two upper-reservoir levels selected by a binary from the volume (eqs. 8–9); generation/consumption and min/max flows switched by big-M (eqs. 10–29, pp. 107), based on Conejo et al. (2002); lower-reservoir level effect neglected (p. 107).
  - **Activation in the water balance:** discharge includes extra flow for expected up-regulation energy and retained flow for down-regulation energy; in pumping mode the analogue (eqs. 16–19, 26–29, p. 107–108).
  - **Reserve headroom** in generating mode (up = max − current, down = current − min) and, for VS, **in pumping mode** (up = current − min consumption, down = max − current consumption) (p. 106; eqs. 30–37, p. 108). FS units pump at a single point, so no reserve while pumping (p. 108).
  - **Regulation energy settlement** on hourly net energy: positive net paid at up price, negative net charged at down price (eqs. 39–41, p. 108).
  - **Activation shares and R_t^SM** = historical hourly system-wide ratios of delivered to assigned reserve (plant data not public) (p. 109).
  - **Evaluation:** Real Income (RI) = schedule valued ex post at real historical prices; compared with Maximum Theoretical Income (MTI) under perfect information (p. 109).

## Data / case
- Iberian/Spanish historical hourly DM prices, secondary reserve prices, up/down regulation energy prices, real-time use of reserves, R_t^SM (p. 108–109). 2014 means: DM 42.15 €/MWh, up energy 47.36, down energy 31.34 €/MWh (p. 111).
- Technical data in Table I (p. 110, image); start-up costs from Nilsson & Sjelvgren (p. 109).
- Investment cost references used in discussion: 470–2170 €/kW (Connolly et al.), 775–1280 €/kW (Steffen, Germany/Luxembourg), VS adds 7–15 % (Botterud et al.); the paper assumes +11 % (p. 111).

## Key findings
- (p. 111) DM only: VS raises RI by 3.7–8.2 % and MTI by 2.5–3.8 % (synchronous) and RI by 10.1–12.2 %, MTI 6–7.2 % (asynchronous), due to wider operating range and efficiency.
- (p. 111) DM + SRS: VS raises RI by **97–159 %** (synchronous) and **102–163 %** (asynchronous); MTI by 91–145 % / 95–150 %. Drivers: SRS participation, wider generating range, and **regulation in pumping mode**.
- (p. 111) Bypassing the converter helps in DM-only (higher efficiency) but hurts with SRS (narrower range).
- (p. 111) "In all cases, a big part of the revenue is obtained from the secondary regulation reserve market"; the DM becomes a "subsidiary means" to maximise reserve participation.
- (p. 111, Fig. 2) Risk aversion: raising β lowers expected income by 0.1–0.27 % while raising VaR/CVaR by 0.38–0.99 %; RI exceeds EI by < 4 %, suggesting appropriate scenarios.
- (p. 111–112) Indicative economics (one week extrapolated to a year): weekly RI for FS 240–376 k€ (with SRS) vs 92–114 k€ (DM only); VS 586–761 k€ vs 100–125 k€. Investment FS 96–462 M€, VS 105–517 M€. Payback FS 5.1–35.9 y (SRS) vs 17–93.1 y (DM); VS 2.8–16.3 y vs 17.2–94 y. Caveat: effect on prices if many PHS provide SRS while pumping not considered (p. 112).
- (p. 112, Fig. 3) VS plant offers reserve in every hour, including while pumping, and benefits from reserve prices that are higher off-peak (negatively correlated with DM prices, unpublished) (p. 112).
- (p. 113, Figs. 5–7) Income varies fourfold when the mean reserve price varies sixfold (roughly linear, steeper for VS); sensitivity to up/down energy prices is driven mostly by the accompanying reserve price. Sensitivity profiles chosen by clustering 2010–2014 daily profiles into four groups and taking the closest real day (p. 112).
- (p. 114) Conclusion: VS-PSHP income up to +12.2 % (DM only) and up to +163 % (DM + SRS) vs FS. Future work: uncertainty in regulation energy prices and activation, price-maker in SRS, intraday and tertiary markets.

## Strengths
- Explicit, reusable formulation of reserve provision **in pumping mode** for VS units, alongside generating-mode reserve, activation energy in the water balance and net-energy settlement.
- Uncertainty in both DM and reserve prices from fitted time-series models with scenario reduction; risk aversion via CVaR; ex-post evaluation against real prices and perfect-information bound (RI vs MTI).
- Links operational value to investment (payback periods) for technology choice.

## Weaknesses / limitations
- Daily horizon with fixed start/end volume (half reservoir): no inter-day value of storage, no water values.
- Single-stage decisions (no recourse); activation and regulation-energy prices deterministic and system-level.
- One representative week extrapolated to annual payback; price-taker in a market where a PHS could be large.
- Closed loop, lower reservoir ignored; technical data partly hypothetical (Hill diagrams from literature).
- Key result tables are images in this PDF copy (verify numbers in the PDF before quoting table values).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background (PHS technology): variable-speed units, synchronous vs doubly-fed machines, converter ratings 20–30 %, Grimsel II bypass | Technology description | pp. 105, 109 (Sec. II, IV-A2) |
| Background (PHS technology): VS can regulate while pumping | Fig. 1 and text | p. 105–106 |
| Model: reserve headroom in pumping mode | Up/down reserve limits while pumping | p. 106; eqs. 34–37, p. 108 |
| Model: activation energy in water balance | Extra/retained flows for up/down activation | p. 107–108, eqs. 16–19, 26–29 |
| Model: settlement of activation energy on net energy | Eqs. 39–41 | p. 108 |
| Model: activation-share assumption | Historical system ratio of delivered to assigned reserve | p. 109 |
| Lit review (market participation): reserves dominate PHS revenue | "big part of the revenue" from SRS; DM subsidiary | p. 111 |
| Lit review (sizing/investment): reserves shorten payback | Payback ranges FS/VS with/without SRS; investment cost ranges | pp. 111–112 |
| Background (markets): Spanish SRS design; similar procurement in Nordics | p. 105 | p. 105 |
| Background (price volatility): DM–reserve price correlation −0.47 (2013); reserve prices higher off-peak | p. 106, p. 112 | |
| Method: scenario generation from GARCH-ARIMAX/SARIMAX + clustering | 10 × 10 profiles, 500 samples | p. 109 |
| Method: value of perfect information of DM vs reserve prices | VPI up to 26/36 % (DM), 10 % (reserve) | p. 106 |
| Method: CVaR in a linear scheduling model | Eqs. 1, 3–4; β = 0.1 | p. 106, p. 109 |
| Evaluation design: Real Income vs Maximum Theoretical Income | Ex-post valuation at real prices | p. 109 |

## Useful quotes (with page numbers)
> "the secondary regulation reserve market might be the main source of revenue for the power plant." (p. 103, abstract)

## Follow-up references to check (backward snowballing)
- [4] Connolly et al. (2011) PHES arbitrage strategies, Energy Policy 39(7).
- [5] Steffen (2012) Prospects for pumped-hydro storage in Germany, Energy Policy 45.
- [7] ENTSO-E WG AS (2015) Survey on ancillary services procurement 2014.
- [15] Kazempour et al. (2009) risk-constrained self-scheduling of PSH in energy and ancillary markets.
- [22] Chazarra et al. (2016) value of perfect information of spot prices, EEM (later EPSR 148, 2017).
- [27] Fodstad, Henden, Helseth (2015) hydropower scheduling in day-ahead and balancing markets, EEM.
- [34] Botterud, Levin, Koritarov (2014) Pumped storage hydropower: benefits for grid reliability, ANL/DIS-14/10.

