---
bibkey: perezdiaz2020medium
bibkey_provisional: true
title: "Medium-term scheduling of a hydropower plant participating as a price-maker in the automatic frequency restoration reserve market"
authors: "Juan I. Pérez-Díaz, Ignacio Guisández, Manuel Chazarra, Arild Helseth"
year: 2020
venue: "Electric Power Systems Research, 185, 106399 (doi:10.1016/j.epsr.2020.106399)"
peer_reviewed: true
methods: [sdp, uncertainty-modelling, deterministic-lp-milp, heuristics-simulation, hydro-production-function]
review_sections: [market-participation, modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/49_Perez-Diaz_2020_Medium_term_scheduling_hydropower_price_maker_automatic_frequency_restoration_reserve_market.pdf"
takeaway: "One-year SDP with daily stages and Markov-chain inflow/price/reserve-RDC states computes water values for a Spanish reservoir plant selling energy and aFRR; including aFRR in the water-value model raises simulated profit 4.5–4.6 %, adding price-maker effects only +0.12 % but cuts spillage ~29 % because price-taker reserve assumptions overestimate water values."
---

# Medium-term scheduling with price-maker aFRR participation (Pérez-Díaz et al., 2020)

Article number 106399; page numbers below are the article's own pages 1–9 (= PDF pages 1–9).

## Research question / purpose
(1) Present a medium-term scheduling model that computes the **water value** of a hydropower plant selling energy as a price-taker in the Spanish day-ahead market (EM, OMIE) and **automatic frequency restoration reserve (aFRR) capacity as a price-maker** in the day-ahead aFRR market (RM, REE); (2) assess how the producer's price-making ability in the RM affects profit and operation (p. 3). Motivation: all earlier multi-market water-value papers assume price-taking in both markets (p. 3); in Spain on two sample days in 2018 only 4/43 and 10/40 aFRR bidders would count as price-takers under Pousinho et al.'s criterion (p. 3).

## Setting
- **System:** one existing conventional (no pumping) reservoir hydropower plant in north-west Spain with seasonal storage, also used for flood control (p. 5, p. 7). Table 1 (p. 5): reservoir 71.0–644.6 Mm³, water level 270.0–329.5 masl, tailwater 198.0 masl, 3 Francis units with 3 penstocks, max flow 279 m³/s (3 × 93), min flow 40 m³/s, max power 312.6 MW (3 × 104.2), min power 22.3 MW. Each unit has 81.9 MW spinning reserve capacity; with three units, 27 %/35 % of the RM's max hourly up/down requirement (900/700 MW) (p. 5). Emptying at full flow takes about 3.5 weeks (p. 5). Mean annual inflow 2876 Mm³ (footnote, p. 7).
- **Markets:** Spanish EM (price-taker) and day-ahead aFRR capacity market RM (gate closure 4 pm, results 4:30 pm, pay-as-cleared marginal price; real-time use paid at the mFRR/tertiary price) (p. 3). TSO up/total reserve ratio R_t imposed (eq. 23, p. 4). Intraday and mFRR markets are future work (p. 9).
- **Horizon and resolution:** 1 year with **daily decision stages**, each with 24 hourly periods (p. 3). Daily stages chosen because (a) assuming perfect foresight of RM prices for a whole week inside a stage is too optimistic (p. 4), and (b) the reservoir can be emptied in ~3.5 weeks (p. 5).

## Method
- **Model type:** risk-neutral **SDP** (Bellman recursion, eq. 1, p. 4) over a discretised storage state; each daily subproblem is an **MIQP** (eqs. 2–23, p. 4): quadratic because the reserve price is a linear function of the producer's own offer (residual demand curve, RDC, price = I_t + S_t·r_up/R_t); binaries for unit status, start-ups/shut-downs. SDP chosen precisely because it handles non-convexities such as unit commitment that SDDP cannot (p. 4).
- **How uncertainty is represented:** three exogenous state variables, all **lag-1 Markov chains**: daily inflow (5 states: lowest/highest historical value representing the 2 % tails, plus three equal-frequency central groups; 43-year CEDEX series 1963–2005, lag-1 autocorrelation 0.80), daily average EM price, and daily average RDC (intercept, slope) of the RM (p. 5). Prices: GARCH-ARIMAX (EM) and SARIMA (RDC) models generate 200-year synthetic series; **k-means clustering into 3 states per day**, k-means rerun a few hundred times to pick the most frequent quasi-equal clustering; the state values are the samples nearest to the centroids (pp. 5–6). Two variants: independent EM and RDC chains (3 × 3), or a **joint** 3-state chain (pp. 5–6). Historical 2010–2015: lag-1 autocorrelation of daily EM price 0.77, reserve price 0.66, EM–reserve cross-correlation −0.43 (p. 5); price–inflow correlations (−0.34/0.14) ignored (p. 6). Storage discretised into **9 equidistant values** (p. 5).
- **Solution method:** backward SDP iterations until the relative change in z̃ is below a tolerance (pseudocode, p. 5); z̃_{d+1} is linearly interpolated between storage grid points (p. 4). Water values = discrete derivative of the expected future profit w.r.t. storage (p. 5). CPLEX 12.2; CPU 52–392 s, 3–4 iterations (Table 2, p. 7).
- **Key modelling choices and assumptions:**
  - Water balance with evaporation (as a function of flooded area), bottom outlets and storage-dependent spillway capacity (eqs. 3–10, p. 4).
  - **Head effects:** plant aggregate piecewise-linear power–discharge curve chosen from the initial storage of each day, so head varies between days but **intraday head effects are neglected**; justified ex post since daily head variation ≤ 2.24 % of max gross head on 99 % of days (p. 4–5, p. 8).
  - No ramping or min up/down; instead **wear-and-tear cost on hourly power changes** and start-up/shut-down costs (from EPRI and Nilsson & Sjelvgren) (p. 4).
  - Reserve headroom: up ≤ Σ online Gmax − g; down ≤ g − Σ online Gmin (eqs. 21–22, p. 4).
  - **Activation is ignored in the medium-term model**; it is included only in the short-term simulation (eqs. 25–27, p. 6), justified because net real-time use is small (6.6 % in H1 2017) (p. 7).
- **Evaluation:** the water-value tables feed a day-ahead **short-term MIQP** (24 h, eqs. 24–27) run on a rolling basis through a **100-year synthetic scenario** with perfect next-day foresight of inflow, prices, RDCs, activation prices and activation shares (p. 6). Four water-value models compared: M1 EM only; M2 price-taker in EM and RM; M3 price-maker in RM, independent chains; M4 as M3 with joint EM–RDC chain (p. 6, Fig. 1). Different ending volumes are valued with M3's water values for a fair comparison (p. 7).

## Data / case
- OMIE and REE (ESIOS) data 2010–2015 for prices and RDCs; CEDEX inflows 1963–2005 (p. 5).
- Plant data in Table 1 (p. 5) as above.

## Key findings
- (Table 3, p. 7; M€ over 100 years) Profit: M1 5590.42, M2 5840.49, M3 5847.68, M4 5842.32. EM revenue 4337.85 / 4482.26 / 4487.62 / 4482.33; RM revenue 1361.20 / 1480.22 / 1478.71 / 1479.05. (Reconstructed from the garbled extraction; rows add up.)
- (p. 8) Including the RM when computing water values raises profit by **4.47–4.60 %**, "appreciably higher" than reported for Norway (Helseth et al. 2016, 2017) and Switzerland (Abgottspon & Andersson 2012), which found about 1 %.
- (p. 7, p. 8) Price-maker water values add only **0.09–0.12 %** profit over price-taker ones, but cut **spillage by 29 %**; extra spillage with M2 is 5.85·10³ Mm³ over 100 years. M2 overestimates water values (ignores price depression from its own offers), keeps the reservoir higher (average 558 vs 495 Mm³, ~4 m head) and spills more.
- (p. 7) With M1 water values the reservoir is kept lowest; the resulting lower head even reduces **EM** revenue below M2's, a counter-intuitive result caused by inconsistency between medium- and short-term models (M1 underestimates water value when the short-term model also sells reserves).
- (p. 8) Cross-correlation of EM and RM prices is not significant enough to matter for water values (M3 ≈ M4).
- (p. 8, Table 4) Sensitivity with RDC intercept/slope scaled 0.5–1.5: price-maker profit difference −0.27 % to +0.32 %; spillage reduction 19.63–35.54 % in all cases; RM/EM revenue ratio 9.9 %–63 %.
- (p. 8) Forecast errors for comparison: EM price MAPE 15–20 %, RM RDC MAPE 20–25 %, so the 0.12 % gain is small relative to day-ahead uncertainty.
- (p. 9) The SDP model can benchmark linear (SDDP-type) policies and quantify their approximation errors.

## Strengths
- Directly addresses how reserve participation enters **water values**, with a clean medium-term → short-term → long simulation evaluation design, and fair valuation of end storage.
- Markov-chain construction by k-means clustering of synthetic price series, close in spirit to ours.
- Handles non-convexities (unit commitment, quadratic price-maker term) by using SDP.
- Useful literature summary of earlier multi-market water-value work (Abgottspon, Helseth, Hjelmeland) on p. 3.

## Weaknesses / limitations
- Single conventional reservoir plant, no pumping; one storage state only (SDP curse of dimensionality).
- Activation energy only in the short-term model, so a residual inconsistency remains (p. 7).
- Perfect next-day foresight in simulation; risk-neutral; synthetic RDC variants rather than other real markets.
- Spillage result partly reflects modelling inconsistency rather than market value per se.
- The reported gains of 4.47–4.60 % are relative to M1 water values used in a short-term model that still sells reserves, so they mix "value of reserve-aware water values" with model inconsistency.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (market participation): reserves in water-value computation | 4.47–4.60 % profit gain; Norway/Switzerland ~1 % | p. 3, p. 7 (Table 3), p. 8 |
| Lit review: price-taker assumption in reserve markets | Only 4/43 and 10/40 Spanish aFRR bidders price-takers; price-maker effect on profit 0.12 % but spillage −29 % | p. 3, pp. 7–8 |
| Lit review (research gap): earlier multi-market medium-term models all price-taker, mostly LP-based SDP/SDDP | Literature survey | p. 3 |
| Method: Markov-chain construction by k-means | 3 states per day, rerun k-means, nearest sample as state value; inflow chain with tail states | pp. 5–6 |
| Method: stage length choice | Daily stages to avoid weekly perfect foresight of reserve prices; reservoir empties in 3.5 weeks | p. 4, p. 5 |
| Model: neglecting intrastage head effects | Daily head variation ≤ 2.24 % of max gross head on 99 % of days | p. 4, p. 8 |
| Model: ignoring activation in medium-term model | Net real-time aFRR use 6.6 % in H1 2017 | p. 7 |
| Model: reserve headroom with unit status; TSO up/total ratio | Eqs. 21–23 | p. 4 |
| Evaluation design: medium-term policy → short-term simulation, end-storage valuation | 100-year synthetic simulation, Fig. 1 | pp. 6–7 |
| Background (price volatility): EM and reserve price autocorrelation and cross-correlation | 0.77, 0.66, −0.43 (Spain 2010–2015) | p. 5 |
| Background (markets): Spanish aFRR market design | Gate closure 4 pm, marginal pricing, activation at mFRR price | p. 3 |

## Useful quotes (with page numbers)
> "for practical purposes it is not satisfactory to operate with wrong water values." (p. 8)

## Follow-up references to check (backward snowballing)
- [14] Abgottspon & Andersson (2012), ancillary services in medium-term hydro optimisation, SEPOPE (Swiss PHS, ~1 % effect).
- [17] Helseth, Mo, Fodstad (2015) co-optimizing energy and capacity, PowerTech; [18] Helseth, Fodstad, Mo (2016) Optimal medium-term hydropower scheduling considering energy and reserve capacity markets, IEEE TSTE 7(3) (not in our library; our `helseth2017` is a different paper).
- [15] Abgottspon & Andersson (2014) PSCC, already in library as `abgottspon2014`; [20] Helseth et al. (2013) IET GTD, in library as `helseth2013`.
- [19] Hjelmeland, Helseth, Korpås (2016) medium-term scheduling with sales of capacity, Energy Procedia 87.
- [25] Helseth et al. (2017) Assessing hydropower operational profitability considering energy and reserve markets, IET RPG 11(13).
- [26] Baslis & Bakirtzis (2011) mid-term stochastic scheduling of a price-maker hydro producer with pumped storage, IEEE TPWRS 26(4) (in inbox as Baslis2011).
- [30] Chazarra et al. (2017) value of perfect information of spot prices in joint energy and reserve scheduling of PHS, EPSR 148.
- [38] Chazarra et al. (2019) forecasting inaccuracies in aFRR for PHS, EPSR 174.

