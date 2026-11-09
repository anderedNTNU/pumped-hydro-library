---
bibkey: perezdiaz2015trends
bibkey_provisional: true
title: "Trends and challenges in the operation of pumped-storage hydropower plants"
authors: "Juan I. Pérez-Díaz, M. Chazarra, J. García-González, G. Cavazzini, A. Stoppato"
year: 2015
venue: "Renewable and Sustainable Energy Reviews, 44, 767–784 (doi:10.1016/j.rser.2015.01.029)"
peer_reviewed: true
methods: [sdp, deterministic-lp-milp, risk-averse-cvar, hydro-production-function]
review_sections: [modelling-phs-plants, market-participation, research-gap, phs-technology, electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Medium_term_pumpekraft/PerezDiaz2015.pdf"
takeaway: "Widely cited review of PHS scheduling models: price arbitrage alone is no longer viable and reserve markets are becoming the main PHS revenue (a shift to 'reserve-driven operation'); names three challenges: modelling real-time reserve activation, revising long-term guidelines (end targets and water values) to include reserve markets, and scheduling variable-speed/short-circuit plants."
---

# Trends and challenges in PHS operation (Pérez-Díaz et al., 2015)

Journal page = PDF page + 766 (article runs pp. 767–784). Review paper; numbers in brackets [n] are the review's own reference numbers.

## Research question / purpose
Review current trends in PHS operation, argue why current practice (price arbitrage, fixed end-of-day/week targets) should be re-examined given rising wind/solar and its effect on energy and ancillary-service prices, check whether existing models suit the new framework, and set out the main challenges for operators who must jointly optimise energy and ancillary-service markets (abstract p. 767; objectives p. 768). Small PHES in water-supply networks is out of scope (p. 768).

## Setting
- **Scope:** literature on scheduling and bidding models for PSHPs (closed-loop and open-loop, fixed and variable speed), in liberalised and centralised contexts, plus wind–hydro coordination (Sections 2.1–2.4, pp. 768–776).
- **Markets covered:** day-ahead, intraday, reserve/ancillary markets (spinning, secondary regulation, balancing), real-time activation.
- **Horizons:** short-term (1 day–1 week) scheduling and long-term (1 year) guidelines (water values, targets).

## Method
- **Model type:** narrative review with a classification table of ~40 models (Table 1, p. 777) by technologies, PSHP type (CL/OL, FS/VS), price-taker/maker in spot and reserve markets, treatment of real-time reserve use, horizon, algorithm and risk treatment; and a challenge table (Table 2, p. 778).
- Not a systematic review (no search protocol stated).

## Data / case
- Worldwide PHS capacity ≈ 130 GW; round-trip efficiency 70–80 %; cycles can be daily, weekly or seasonal (p. 768).
- Spain 2010: mean real-time use of committed regulation reserve **28.6 % up, 30.0 % down**; wind 22 % of installed capacity (p. 778, Fig. 1 p. 779).

## Key findings
- (p. 768) Rising wind/solar changes the level and the **shape** of hourly price profiles, threatening arbitrage profitability; PHS owners look to ancillary services for revenue.
- (p. 769) Deb [29] was the first to stress ancillary-service profits: a PSHP might almost double daily income by bidding in both energy and ancillary markets. Kanakasabapathy & Swarup [32]: **weekly operation** gave higher profit and better use of storage than daily cycles (4 %, 6 %, 24 % above other strategies).
- (p. 770) Pinto et al. [38]: optimal strategy gives **negative day-ahead revenue** and reserve revenue more than an order of magnitude larger. Connolly et al. [39]: across energy-only markets, the best arbitrage profit varies 20–23× between markets and strongly between years; even with low investment cost and interest rate, a PSHP relying on arbitrage is a risky investment. Investors therefore favour upgrading/repowering existing plants (citing Deane et al. 2010 [40]). Wind may or may not increase profitable pumping hours, depending on its covariance with load/prices [43].
- (p. 771) Uncertainty handling: risk-neutral (expected value) vs risk-averse (variance penalty, CVaR, minimum-profit, downside risk); a naive historical-price strategy was only 3–6 % below perfect knowledge in [30].
- (pp. 771–772) Price-maker models use residual demand curves (RDCs) in Spanish day-ahead, intraday and secondary reserve markets [56, 59]; reserve and balancing markets are small, so bids are more likely to move prices (p. 772). Adding the intraday market raised daily revenue 5 % in [37]. Swider [36]: expected profit "dominated by the reserve markets products".
- (p. 772) Authors' synthesis: "there should be a shift from the traditional price arbitrage based operation to a 'reserve driven operation'" for a PSHP to be profitable.
- (pp. 772–773) Head effects are of minor importance for closed-loop PSHPs with large rated head, so head is often taken as constant; not necessarily so for open-loop PSHPs.
- (p. 773) Real-time reserve use affects not only the current day's income but the fulfilment of end-of-day/week targets and hence the next period's income. Closed-loop plants normally use a target; open-loop plants targets or water value functions. In [39], the best strategy for a 6-h (daily-cycle) PSHP reached 97 % of perfect-forecast profit, but only 82 % for a 24-h (weekly-cycle) plant, so intraday arbitrage "may be far from the optimum" for weekly-cycle plants.
- (pp. 773–774) Deane et al. [72] (two-step stochastic targets for a large PHES) summarised as the main example of revised target setting.
- (p. 774) For open-loop PSHPs, targets/water values come from long-term models; **SDP** suffers the curse of dimensionality (one or few reservoirs), **SDDP** handles large systems; market features have entered long-term models "at a slower pace, and still today remains a challenging task". Löhndorf et al. [80] (ADDP, day-ahead + intraday) is the most detailed long-term price model; Helseth et al. [82] first included pump start-up costs in a long-term SDDP model.
- (p. 774) Irish study [71]: a 500 MW / 5 GWh PSHP justified from 8.5–9 GW installed wind (48–51 % wind energy), not very sensitive to discount rate and lifetime.
- (p. 776) Variable speed and hydraulic short circuit enable regulation while pumping; [99] (Chazarra et al. 2014) supports reserves as the main PSHP revenue regardless of speed technology; [101] VS adds 5.89 % energy at an existing plant. Only three plants operated in SC mode (Kops II, Malta, Geesthacht).
- (p. 776) Summary of trends: arbitrage/peak shaving "appear to be no longer economically feasible"; ancillary/balancing markets "emerge as the main source of revenue for PSHPs in liberalized market contexts".
- (p. 778) **Challenge 1:** model the uncertainty of real-time reserve use; no documented forecasting of real-time use existed. For open-loop PSHPs with large reservoirs, used reserves "do not have a significant impact on the available head or stored energy" but may affect the end-of-week target or the value of water [109]; for small closed-loop plants they matter more. Hydro-dominated systems (Norway, Canada) need relatively less balancing.
- (pp. 778–779) **Challenge 2:** revise long-term guidelines (targets, water values) for reserve participation. The "empty at 0:00" daily target prevents upward reserve in the first hours of the day. Abgottspon & Andersson [115] (Swiss, SDP with weekly stages, secondary control) found only a 1–2 % increase in expected profit, but "similar analyses should be carried out with other PSHP and electricity markets". For open-loop PSHPs in large hydro systems, an SDDP-based approach should be used, e.g. extending [80] with reserve/balancing markets (p. 779).
- (pp. 779–781) **Challenge 3:** scheduling of VS and SC plants: SC-mode curve is the generating curve shifted by pump flow/power (Figs. 2–3); n ternary units give regulation range equal to all turbines in operation; VS pump regulation up = actual − min consumption, down = max − actual (Fig. 5, p. 781); with m < n converters only m units can regulate while pumping (p. 781).
- (p. 781) Conclusions restate the three challenges and note a lack of studies with price-maker effects in energy and reserve bids.

## Strengths
- Authoritative, widely cited review by the group that produced most PHS–reserve scheduling papers (Chazarra, Pérez-Díaz, García-González); clear classification table of models.
- Explicitly identifies the link between reserve participation and **long-term water values** as an open challenge, which is our gap.

## Weaknesses / limitations
- 2015 snapshot; does not cover later SDDP work with reserves (e.g. Helseth et al. 2016–2017, Pérez-Díaz et al. 2020).
- Narrative, not systematic; Table 1 is dense and partly garbled in text extraction.
- Focus on Spanish/European short-term practice; little on seasonal storage or reservoir/pump sizing.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background (PHS technology): global capacity, round-trip efficiency, daily/weekly/seasonal cycles | ~130 GW, 70–80 % | p. 768 |
| Background (PHS technology): variable speed, ternary units, hydraulic short circuit; plants in SC mode | Kops II, Malta, Geesthacht; Figs. 2–5 | p. 776, pp. 779–781 |
| Background (markets/price volatility): RES changes level and shape of price profiles | Introduction | p. 768 |
| Lit review (market participation): reserves as main PHS revenue; "reserve driven operation" | Deb, Pinto, Swider, Chazarra 2014 | pp. 769–772, p. 776 |
| Lit review (market participation): arbitrage-only PHS is a risky investment | Connolly et al. results | p. 770 |
| Lit review (modelling PHS): classification of PHS scheduling models | Table 1 | p. 777 |
| Lit review (modelling PHS): daily vs weekly cycle; end targets vs water values; CL vs OL | | pp. 769, 773 |
| Lit review (modelling PHS): SDP vs SDDP for long-term guidelines | | p. 774, p. 779 |
| Lit review (research gap): long-term models with market detail still challenging; revise guidelines for reserves | Challenge 2 | p. 774; pp. 778–779; Table 2 |
| Model: activation has small effect on stored energy for large open-loop reservoirs | Challenge 1 discussion | p. 778 |
| Model: head effects minor for high-head closed-loop PHS | | pp. 772–773 |
| Model: reserve while pumping for VS / SC units | Fig. 3, Fig. 5 descriptions | pp. 780–781 |
| Data: Spanish real-time use of regulation reserve 2010 | 28.6 % up, 30.0 % down | p. 778, Fig. 1 |
| Lit review (sizing): PHS investment justified above 8.5–9 GW wind in Ireland | [71] | p. 774 |

## Useful quotes (with page numbers)
> "there should be a shift from the traditional price arbitrage based operation to a 'reserve driven operation', for a PSHP to be profitable." (p. 772)

## Follow-up references to check (backward snowballing)
- [29] Deb (2000) Operating hydroelectric plants and pumped storage units in a competitive environment, Electricity Journal.
- [36] Swider (2007) Simultaneous bidding in day-ahead auctions for spot energy and power systems reserve, IJEPES 29(6).
- [38] Pinto, de Sousa, Ventim Neves (2011) value of a pumping-hydro generator with wind, EEM.
- [39] Connolly et al. (2011) PHES arbitrage strategies, Energy Policy 39(7).
- [51] Kazempour et al. (2009) risk-constrained self-scheduling of a PSH in energy and ancillary markets, ECM 50(5).
- [80] Löhndorf, Wozabal, Minner (2013) ADDP for hydro storage trading, Operations Research 61(4) (not in library; our `lohndorf2019` is a different paper).
- [82] Helseth, Gjelsvik, Mo, Linnet (2013) hydrothermal scheduling with pumped storage and wind, IET GTD 7(12) (in library as `helseth2013`).
- [109] Olsson & Söder (2003) hydropower planning with energy–reserve trade-off, PowerTech.
- [115] Abgottspon & Andersson (2012) ancillary services in medium-term hydro optimisation, SEPOPE.

