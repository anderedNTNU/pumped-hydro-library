---
bibkey: helseth2020scheduling
title: "Scheduling Toolchains in Hydro-Dominated Systems: Evolution, Current Status and Future Challenges for Norway and Brazil"
authors: "Arild Helseth, Albert Cordeiro Geber de Melo"
year: 2020
venue: "SINTEF Energy Research report 2020:00757, Unrestricted, 2020-08-10, 72 pp., ISBN 978-82-14-06578-7; checked by Birger Mo"
peer_reviewed: false
methods: [sddp-markov-chain, sdp, uncertainty-modelling, deterministic-lp-milp]
review_sections: [modelling-phs-plants, electricity-markets, market-participation]
relevance: medium
read_by: []
added: 2026-11-11
takeaway: "The 72-page SINTEF report behind helseth2023hydropower and the TET4565 lecture: Norway's decentralised toolchain (EMPS 3-5 years weekly for price forecasts; ProdRisk 2-5 years weekly, SDP/SDDP with a price Markov chain and VAR(1) inflow, for water values; SHOP deterministic for plans) vs Brazil's centralised chain (NEWAVE/DECOMP/DESSEM, monthly stages, CVaR); the producer is price-taking and risk-neutral; the MTS is decomposed in space but not in time from the LTS; a price forecast with too little short-term variation under-values water at low reservoirs and over-values it at high ones; future long-term models are 'too flexible' for a capacity-constrained system."
source_path: C:/Users/Anders/OneDrive - NTNU/9.semester/Prosjektoppgave/Sources/TR_HydropowerSchedulingToolchains.pdf
---

# Scheduling toolchains in hydro-dominated systems, Norway and Brazil (Helseth & Geber de Melo, 2020)

SINTEF technical report, cited by lecture 6 of TET4565 (`farahmand2026hydropower`, slide 6–7) for the scheduling hierarchy. The peer-reviewed version is `helseth2023hydropower` (ASCE J. Water Resour. Plann. Manage., shorter, adds the US Colorado River chain). **Cite the 2023 paper where it says the same thing**; use this report for the Norwegian detail that the paper dropped (history of EFI/SINTEF tools, the price-forecast argument in Fig. 32, the Brazilian market sections).

**Page convention:** PDF page = printed page + 1 (printed "4 of 72" is PDF page 5). Pages below are PDF pages. Read: ch. 1 (pp. 5–11), ch. 2 §2.3.2.3–2.8 (pp. 22–35), ch. 4–5 (pp. 65–69) in full; the Brazil chapter skimmed.

## Research question / purpose
Describe the operational scheduling toolchains of Norway (SINTEF: EMPS, ProdRisk, SHOP) and Brazil (CEPEL: NEWAVE, DECOMP, DESSEM), their history, the information flow between the models, and what must change for a system with more wind and solar (pp. 5–6).

## Setting
- **System:** national hydro-dominated systems; Norway decentralised (the producer owns the scheduling problem), Brazil centralised dispatch by the ISO ONS (pp. 7–9).
- **Markets:** Nord Pool day-ahead (single hourly orders, −500 to 3000 EUR/MWh, up to 62 price steps), intraday, TSO balancing with two-price imbalance settlement, reserve capacity markets (pp. 21–22); Brazil: regulated and free contracting environments, spot price from the toolchain's marginal costs (pp. 42–50).
- **Horizon and resolution:** EMPS 3–5 years, weekly decision stages, uncertainties known one week ahead, sequential or aggregated time resolution down to hourly (p. 31); ProdRisk 2–5 years "depending on the regulation capability of the hydropower system", weekly stages, down to hourly (p. 34); SHOP deterministic over its planning horizon (p. 35); EFI-MTM (1980s) several weeks to one year, EFI-STM 1–10 days (pp. 27–28); Brazil: NEWAVE 5 years monthly, DECOMP months, DESSEM up to two weeks at 30 minutes (pp. 54–64).

## Method
- **Model type:** descriptive review of two toolchains with figures summarising each model's characteristics (Figs. 30–31, pp. 66–67).
- **How uncertainty is represented:** Norway uses historical weather records directly (inflow, temperature-dependent load, wind) to preserve correlations in time and space; Brazil uses dedicated stochastic inflow models (p. 67). ProdRisk: VAR(1) model of normalised weekly inflow in the backward pass, market price as a discrete Markov chain built from the price forecast, and historical price–inflow scenarios in the forward pass, which "preserves the correlation between inflows and market prices" (p. 34).
- **Solution method:** EMPS = water-value method per price area plus heuristic drawdown and LP area optimisation (pp. 31–32); ProdRisk = combined SDP (price) and SDDP (reservoirs, inflow) because expected profit is convex in the price state and the standard SDDP convexity requirement fails (p. 33); SHOP = successive LP with MIP (p. 35).
- **Key modelling choices:** hazard-decision stages of one week because inflow is predictable for about a week (p. 8); the producer is price-taking and risk-neutral, "a necessary condition for a free market to be economically efficient, and is believed to hold fairly well for the Nordic market" (p. 7); no grid constraints in ProdRisk, all power through one busbar (p. 34); coupling by cuts, prices, volumes, penalty functions or trust regions (p. 11); no upstream feedback in either toolchain (p. 11).

## Data / case
No own case; Figure 9 (p. 23) shows Norwegian generation and exchange in week 2 of 2019 (export at daytime, import at night and weekends); Figure 12 (p. 29) weekly Oslo spot price vs reservoir filling 2000–2019.

## Key findings
- (p. 6) The scheduling problem is "minimize the expected cost of operating the system over the planning period"; in Norway it is reformulated for the producer as "given a forecast of future market prices: maximize the expected profit over the planning period" (p. 7).
- (p. 6) The opportunity cost of water "is derived from all other costs for operating the system"; the horizon must cover the dynamics of the largest reservoirs, measured by the degree of regulation (reservoir capacity over mean annual inflow), which is several years for the largest Norwegian and Brazilian reservoirs.
- (p. 8) A producer "is not obliged to cover a specific part of the load", so its problem is much smaller; once a price forecast exists, "the producer should trust that the other player's planning is properly reflected in the forecast".
- (p. 8) Fundamental market models for price forecasting "typically take the cost-minimizing scope of the central dispatch models"; hydropower scheduling is an integral part of them.
- (p. 10) Long-term models are strategic and stochastic; short-term models are operational, detailed and "often deterministic". In Norway the MTS "is decomposed in space, but not in time" from the LTS (same horizon, smaller system), and the STS is decomposed in time from the MTS; in Brazil all models cover the whole system and only the horizon shrinks.
- (p. 28) Price forecasts can come from futures prices, historical prices or fundamental models; fundamental models became the preferred option because futures carry little uncertainty information and historical series are not representative of the future market. "The correlation between inflow and spot price as well as the price autocorrelation are significant and should be taken into account."
- (p. 29) The 1990s medium-term model was multi-scenario deterministic with joint inflow–price scenarios from EMPS; ProdRisk replaced it.
- (p. 33) ProdRisk needs at least three state variables: reservoir volume, inflow and market price, because of the price's strong autocorrelation.
- (p. 33) An earlier ProdRisk combined operation with hedging by futures under revenue targets; the current version is risk-neutral, "leaving financial trade as a separate activity".
- (p. 35) ProdRisk extensions: start-up costs, reserve capacity sales [28 = `helseth2016`], SHOP coupling, SDDiP (not operational because of computation time), and runs as a market model for Iceland [27 = `helseth2013`] and the detailed Norwegian system with 279 reservoirs [31].
- (p. 35) Long- and medium-term models are techno-economic models whose key output is the expected marginal value of water; the short-term model takes water values as input.
- (p. 67) Costs not captured by the decentralised toolchain: TSO redispatch within price zones and ancillary services, although reserve capacity prices can be embedded [28].
- (p. 67) Weekly stages in Norway and monthly in Brazil "date back to the early creation of the scheduling models" and reflect hydrology.
- (p. 68, Fig. 32) A price forecast that is right on expectation but has too little short-term variation gives a future-profit function that underestimates profit; water values are then underestimated at low reservoir volumes and overestimated at high ones, and these errors are passed to the short-term model.
- (p. 68) Risk aversion is explicit in Brazil (CVaR) and absent in SINTEF's models; Norway is integrated with Europe and producers adjust risk in financial markets.
- (p. 69) Future: more wind and solar move hydro systems "from an energy-constrained to a capacity-constrained system"; more system services from hydro need finer time resolution; the approximation error of weekly (Norway) or monthly (Brazil) stages will grow; "current long-term models are too flexible for the future system, and thus are not capable of accurately valuating the water"; climate change weakens reliance on historical records; no upstream information flow exists and reserve capacity prices should flow downstream from long-term models; time inconsistency between levels should be quantified with a simulator.

## Strengths
Written by the ProdRisk and SHOP developers; gives the reasons behind the design choices (weekly stages, price in the state space, historical weather years) that the papers state without explanation; Fig. 32 is a clear argument for why price variability inside the forecast matters for water values.

## Weaknesses / limitations
Not peer-reviewed; descriptive, no results; the toolchain figures are "indicative for the typical case"; pumped storage appears only as a topology feature ("complex topologies including pumps", pp. 31, 33); the Brazilian half is irrelevant for us.

## Use it for… (lookup guide)
| Use in our thesis | What the report provides | Where in the report (PDF page) |
|---|---|---|
| Background: scheduling hierarchy and horizons | EMPS 3–5 years; ProdRisk 2–5 years by regulation capability; weekly hazard-decision stages; EFI-MTM/STM horizons | pp. 8, 27–28, 31, 34 |
| 5.2 Perspective: system vs owner objective | cost minimisation vs producer profit maximisation given a price forecast; price-taking "believed to hold fairly well"; producer not obliged to serve load | pp. 6–8 (prefer `helseth2023hydropower` p. 7) |
| 5.2: what system models produce | fundamental market models take the central-dispatch scope and give the price forecast | pp. 8, 28–29 |
| 5.3 Uncertainty: why prices are in the state | strong price autocorrelation; inflow–price correlation; VAR(1) inflow and price Markov chain; historical scenarios in the forward pass | pp. 28, 33–34 |
| 5.3: price variability and water values | Fig. 32 argument: too little short-term variation under-values water at low volumes | pp. 68 |
| 5.3 / 5.7: weekly stage as an approximation | weekly stages are historical; their error grows with renewables and small storages | pp. 67, 69 |
| 5.4 Markets: costs not in the owner model | ancillary services and reserve capacity prices; reserve prices should come from long-term models | pp. 67, 69 |
| 5.7 Gap: capacity-constrained future | "long-term models are too flexible"; need for short-term detail in long-term scheduling | p. 69 |
| Ch. 6: risk neutrality | ProdRisk risk-neutral; financial trade separate | p. 33 |

## Useful quotes (with page numbers)
> "Given a forecast of future market prices: Maximize the expected profit over the planning period while satisfying all relevant constraints." (p. 7)
> "The price-taking assumption is a necessary condition for a free market to be economically efficient, and is believed to hold fairly well for the Nordic market. It also significantly simplifies the generation scheduling models." (p. 7)
> "the MTS model is decomposed in space, but not in time from the LTS model. The STS model is decomposed in time from the MTS." (p. 10)
> "When used for operational scheduling purposes, ProdRisk is normally set up for a horizon of 2-5 years, depending on the regulation capability of the hydropower system." (p. 34)
> "The price needs to be considered a part of the state space in the SDDP algorithm due to its strong autocorrelation." (p. 33)
> "with an approximate price forecast, if the reservoir volume is low, water values (gradients of the future expected cost function) are underestimated. Conversely, if the reservoir volume is high, water values are overestimated." (p. 68)
> "it is reason to believe that current long-term models are too flexible for the future system, and thus are not capable of accurately valuating the water." (p. 69)

## Follow-up references to check (backward snowballing)
- [2] Fosso, Gjelsvik, Haugstad, Mo & Wangensteen (1999), "Generation scheduling in a deregulated system. The Norwegian case", IEEE TPWRS 14, 75–81; [3] Haugstad & Rismark (1998), price forecasting by system simulation, EPSOM 98 (pp. 28–29). Neither in the library.
- [15] = `gjelsvik1999` (PSCC 1999, the ProdRisk formulation); [24] = `gjelsvik2010` (Handbook of Power Systems I); [26] = `mo2001` (price Markov chain). All three in the library (reference list p. 70).
- [31] Gjerden, Helseth, Mo & Warland, "Hydrothermal scheduling in Norway using SDDP; a large-scale case study", IEEE PowerTech (p. 35). Not in the library.
- [77] Brigatto, Street & Valladão (2017), "Assessing the Cost of Time-Inconsistent Operation Policies in Hydrothermal Power Systems", IEEE TPWRS (p. 69). Not in the library.
