---
bibkey: bore2026
title: "Economic assessment of hydropower capacity expansions and multi-market participation using a multi-stage stochastic framework"
authors: "Martin Bore, Sigurd S. Brensholm, Stian Backe, Kasper E. Thorvaldsen, Anders S. Ryssdal, Ivar Refsdal"
year: 2026
venue: "2026 22nd International Conference on the European Energy Market (EEM), IEEE"
peer_reviewed: true
methods: [sddp-markov-chain, uncertainty-modelling, hydro-production-function]
review_sections: [market-participation, reservoir-sizing-capacity, modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/bore2026.pdf"
takeaway: "Closest related work (same NTNU group, conference version of the A-grade Bore & Brensholm 2025 project): Markov-chain SDDP (K-means, K=3 price–inflow states per week, hourly weekly stages) for a price-taking NO2 conventional hydro plant selling DA, ID, aFRR and FCR capacity; capacity-market participation raises revenue 26–57% and NPV ~12×, but a 90 MW upgrade is still not commercially viable at industry discount rates."
---

# Capacity upgrades and multi-market participation with MC-SDDP (Bore et al., 2026)

> **Version:** author accepted manuscript (NVA, CC BY 4.0), 6 pages. Page numbers below are AAM pages 1–6; proceedings pagination unknown. The two-column `pdftotext` output interleaves the nomenclature with the abstract and garbles Table IV, so check the PDF for the case data.

## Research question / purpose
Two research questions (pp. 2–3): (1) can the additional value from capacity-market participation (CMP) justify a capacity upgrade of a hydropower plant; (2) how do different upgrade configurations influence revenues across energy and capacity markets. Contributions: a stochastic medium-term hydropower scheduling (MTHS) model with multiple energy and capacity markets, used to evaluate upgrades (p. 2).

## Setting
- **System:** a single conventional reservoir hydropower plant in NO2, price taker (p. 3). **No pumping, no lower reservoir.** Production limits roughly Cmin = 15.5 MW, Cmax = 79.04 MW; reservoir and supply limits in Table IV (p. 6, garbled in text extraction: values such as 101.2 GWh and 30/8/32 MW appear, mapping unverified).
- **Markets:** energy: day-ahead (DA), intraday sell and buy (ID, limited to a 10% market share of hourly volume, p. 6, unverified mapping); capacity: aFRR up/down, FCR-N, FCR-D (set C, p. 1). Capacity sold without activation; markets assumed unsaturated (p. 3). mFRR excluded (p. 5).
- **Horizon and resolution:** one year of weekly stages with hourly operation (Table IV, p. 6; p. 3). Ending storage equals initial storage (Eq. 4, p. 4).

## Method
- **Model type:** weekly LP stage problems (hourly), chained by SDDP; cuts then embedded in a separate simulation model (Fig. 2, p. 3).
- **How uncertainty is represented:**
  - Spot prices: THEMA Power Market Outlook simulations of the 2030 power system over 40+ weather years (hydro years 1980–2024) (p. 4; Table IV, p. 6).
  - Inflow: historical series 1980–2024 scaled to plant size (Table IV, p. 6).
  - Weekly price–inflow combinations clustered with **K-means, K = 3** per week; Markov chain with transition probabilities estimated from transition frequencies between clusters (p. 3). Scenario tree propagation illustrated in Fig. 4 (p. 6).
  - Within each weekly stage, price and inflow are known when the stage is solved (p. 3).
  - Capacity-market prices deterministic (2024 NO2), intraday prices NO2 2024 (p. 5; Table IV).
- **Solution method:** SDDP, Algorithm 1 (p. 3): one forward path per iteration (multiple possible); backward pass over all current regimes × next regimes, averaging cut coefficients with Markov transition probabilities; one cut per week per iteration. Stopping: change in mean lower bound below a threshold and two consecutive "valid" (penalty-free) LBs (p. 3). 10–31 iterations across instances (p. 4).
- **Key modelling choices and assumptions:**
  - Objective (Eq. 1, p. 4): energy and capacity revenue minus ID buy cost minus emergency-water penalty L_em plus future value α_w.
  - **Emergency water:** the stage may buy water at a high penalty to keep SDDP feasible in early iterations (p. 4, Eq. 5).
  - **Production function:** linearised PQ curve with slopes M_i (Eq. 8); appears to be constant head (unverified).
  - Reserve headroom: down-capacity ≤ p − Cmin, up-capacity ≤ Cmax − p (Eqs. 10–11, p. 4); storage margins for up/down regulation energy in Eq. (5).
  - No start/stop (p. 3).
  - Evaluation: 100 simulation iterations per instance, average revenue; NPV with 40-year lifetime, constant annual cash flow, r = 3, 7, 10% (p. 4; Fig. 5, p. 6).
  - The authors note that a weekly Markov chain "may limit the persistence and severity of extreme price-inflow combinations" (p. 3).

## Data / case
- Eight instances: upgrades 0, 30, 60, 90 MW, each with and without CMP (p. 4).
- Motivated by Tussa II (Tussa Group, January 2026: billion-NOK, 90 MW upgrade) (p. 2).

## Key findings
- (p. 4, Table I) Total revenue with CMP vs without: 0 MW 23.71 vs 18.84 mEUR (+25.8%); 30 MW 26.47 vs 19.06 (+38.9%); 60 MW 28.32 vs 18.79 (+50.7%); 90 MW 30.56 vs 19.41 (+57.5%). The abstract's "75% capacity upgrade … nearly 50%" corresponds to the 60 MW instance (60/79 MW ≈ 76%, +50.7%).
- (p. 4) Absolute gain grows at a diminishing rate; capacity revenue ~30% of total at 90 MW vs ~20% at 0 MW. Energy revenues barely change with capacity: limited water means extra MW cannot become extra energy (pp. 4–5).
- (p. 5, Fig. 3) Strong seasonality in capacity revenue: low in late winter/early spring, high around spring flood (April–May), more spread in second half of year.
- (p. 5, Table II) Annual capacity revenue mean 5.63 (0 MW) to 11.46 mEUR (90 MW); 95% CI about −10% to +8% around the mean.
- (p. 5, Table III) 90 MW upgrade NPV per MW with CMP (without): 1.76 (0.15) at 3%, 1.01 (0.08) at 7%, 0.74 (0.06) mEUR/MW at 10%. Total 158.25 / 91.27 / 66.95 mEUR.
- (p. 5) NPV with CMP covers ~50–75% of the reported Tussa II investment cost; without CMP only 4–5.5%.
- (p. 5, conclusion) Upgrade "not sufficient to make the investment commercially viable under industry-specific discount rates", but CMP gives ~12× higher NPV.
- (p. 5) Limitations: deterministic capacity prices; no mFRR or activation; no market saturation; no tax. Spot and balancing prices weakly related (Klæboe et al.; Backe et al.), so stochastic capacity prices would need separate clustering; a coarser time resolution could offset the computational cost.

## Strengths
- Very close to our framework (MC-SDDP with clustered weekly price–inflow states, hourly weekly stages, price taker, Norwegian, reserves).
- Explicit link from operations to investment (NPV per MW).
- Forward-looking 2030 prices across many weather years, with uncertainty bands on revenue.

## Weaknesses / limitations
- Only K = 3 states per week; deterministic capacity prices; capacity markets assumed unsaturated (an optimistic bias the authors flag).
- Convergence judged only by lower-bound stabilisation; no upper bound or statistical gap reported.
- One forward path per iteration and 10–31 iterations is few; differences between instances may partly reflect convergence (the authors note this themselves, pp. 4–5).
- Ending storage fixed to initial storage (Eq. 4) rather than an end-of-horizon water value.
- Conventional hydro only; no pumping, no storage-duration dimension; upgrade = generator capacity only.
- Out-of-sample evaluation is not clearly separated from in-sample scenario generation (simulation uses the same Markov model, unverified).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: research gap / closest work | MC-SDDP for multi-market hydro and capacity upgrades | pp. 2–3 (I-B, I-C) |
| Method: Markov-chain construction by K-means | K = 3 clusters per week, frequency-based transitions | p. 3 (II-A1) |
| Method: SDDP algorithm with Markov chain | Algorithm 1, cut aggregation over next regimes | p. 3 |
| Model: emergency water / feasibility penalty | Penalised water purchase in intermediate iterations | p. 4, Eqs. (1), (5) |
| Model: reserve headroom constraints | y_down ≤ p − Cmin; y_up ≤ Cmax − p | p. 4, Eqs. (10)–(11) |
| Market participation: value of capacity markets | +26% to +57% revenue with CMP | p. 4, Table I |
| Sizing / investment: NPV per MW | 1.76 / 1.01 / 0.74 mEUR/MW at 3/7/10% | p. 5, Table III; Fig. 5 p. 6 |
| Background: Norwegian upgrade trend | Tussa II 90 MW upgrade, Jan 2026 | p. 2 |
| Limitation: Markov chain and persistence | Weekly chain may limit persistence of extremes | p. 3 |
| Limitation: spot vs balancing price relation | Separate clustering needed for stochastic reserve prices | p. 5 |

## Useful quotes (with page numbers)
> "Long-term uncertainty is represented through a weekly Markov chain, which may limit the persistence and severity of extreme price-inflow combinations." (p. 3)

## Follow-up references to check (backward snowballing)
- Helseth, Fodstad & Mo (2016), IEEE TSTE — already `helseth2016`.
- Helseth, Mo, Fodstad & Hjelmeland (2015), PowerTech — co-optimising energy and capacity (check whether we have it).
- Hjelmeland, Helseth & Korpås (2019), Energies — already `hjelmeland2019energies`.
- Pérez-Díaz et al. (2020), EPSR 185 — already `perezdiaz2020medium`.
- Helseth & Mo (2023), IEEE TSTE — hydropower aggregation by spatial decomposition.
- Brekke (2016), NTNU thesis — capacity reserves and inertia.
- Klæboe, Eriksrud & Fleten (2013), Energy Systems 6(1); Backe et al. (2023), EEM — balancing price forecasting.

