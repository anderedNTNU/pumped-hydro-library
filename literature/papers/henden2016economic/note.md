---
bibkey: henden2016economic
bibkey_provisional: false
title: "Economic analysis of large-scale pumped storage plants in Norway"
authors: "Arild Lote Henden, Gerard Doorman, Arild Helseth"
year: 2016
venue: "Energy Procedia 87, 116-123 (5th International Workshop on Hydro Scheduling in Competitive Electricity Markets)"
peer_reviewed: true
methods: [deterministic-lp-milp, heuristics-simulation]
review_sections: [reservoir-sizing-capacity, phs-technology, ldes-seasonal-storage, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "EMPS + ReOpt 2030 Northern-Europe study of 0-14,250 MW new Norwegian PSP x 4,900-18,300 MW interconnection: large PSP arbitrages away its own profit; only ~950 MW is socio-economically best, and owners need >~11 GW interconnection (energy-only, no reserves)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/02_Sesonglagring_og_systemmodeller/Henden2016.pdf
---

# Large-scale PSP in Norway, economic analysis (Henden et al., 2016)

DOI: 10.1016/j.egypro.2015.12.340. Open access (CC BY-NC-ND). Based on the first author's 2014 NTNU master thesis done with Statnett (p. 122, ref. [15]).
**Page mapping:** journal p. 116 = PDF p. 1; p. 117-119 = PDF 2-4; p. 120 = PDF 5-7 (equations split by pdftotext); p. 121-123 = PDF 8-10.

## Research question / purpose
How profitable is large-scale pumped storage (PSP) in Norway, for the plant owners and for Scandinavian socio-economic surplus, when only **energy sales** are considered, and how does this depend on the amount of new PSP capacity and the transmission capacity from Norway to Germany, the Netherlands and the UK? (p. 116-117). Technical, environmental and practical challenges are explicitly neglected (p. 117).

## Setting
- **System:** Northern-European power system projected to 2030. 32 regions (15 in Norway, 4 Sweden, 2 Finland, 4 Denmark, 1 each elsewhere), >1000 hydro plants; Germany, Poland, Netherlands, UK exogenous with fixed price series from Pöyry's BID model (p. 118). New PSP: 15 candidate projects of 950 MW each, 14 in south-western Norway and 1 in Central Norway (p. 118).
- **Markets:** day-ahead energy only. Intraday and balancing markets are named as further work that would "most probably increase PSP profitability" (p. 122).
- **Horizon and resolution:** 2030 static system; 47 historical weather years 1962-2008; weekly decision problems with 56 time steps of 3 h (p. 118).

## Method
- **Model type:** two-step SINTEF model chain. (1) **EMPS** (multi-area, aggregate water-value strategy + weekly simulation) gives water values and target reservoirs (p. 117-118). (2) **ReOpt** re-optimises each weekly problem as an **LP** using EMPS target reservoirs, so PSP can operate with full flexibility within the week; seasonal pumping comes in through the targets (p. 118). In EMPS alone, the heuristic drawdown model lets PSP pump only seasonally (p. 118).
- **How uncertainty is represented:** historical weather (inflow, wind, temperature) years; exogenous continental prices fixed per scenario (p. 117-118).
- **Solution method:** EMPS water-value method (strategy) + LP weekly re-optimisation (simulation).
- **Key modelling choices and assumptions:**
  - Pump efficiency 90 %; generation efficiency from the original plants, mostly 80-92 % (p. 118). Minimum arbitrage needed ≈ the cycle loss, "minimum 20 %" (p. 118).
  - No ramping limits on generation or transmission; no time-delay constraints (p. 118, 122). Hydro plants have min/max discharge and min/max reservoir (p. 118).
  - Continental prices exogenous, so they do not react to more transmission, "a major assumption" (p. 118-119).
  - 25 cases: new PSP 0 / 950 / 6,650 / 9,500 / 14,250 MW × total NO→DE/NL/UK transmission 4,900 / 7,700 / 10,500 / 14,100 / 18,300 MW (Table 1, p. 119).
  - Costs: PSP 0.25-0.5 M€/MW (ref. [13]); totals 0 / 343 / 2,413 / 3,133 / 5,251 M€. Cables 1.231 / 1.275 / 1.694 M€/MW to DE/NL/UK; NPV at 4 % discount rate; lifetimes 60 y (PSP), 40 y (lines); half of transmission cost and congestion rent allocated to Scandinavia (p. 119).
  - Metrics (eqs. 1-5, p. 119-120): change in consumer, producer and socio-economic surplus vs. base case; pump utilisation time (full-load pumping hours/year); owner surplus per MW = Σ price × (generation − pumping) change, minus annuitised PSP cost.

## Data / case
2030 Northern-Europe data set, base-case total Norwegian export capacity 11,800 MW, of which 4,900 MW to DE/NL/UK (p. 118). Norway holds "nearly 50 %" of European reservoir capacity, ~85 TWh (p. 117). ENTSO-E asked Norway/Statnett to verify a 14,000 MW PSP potential; SINTEF estimates ≥ 20,000 MW technical balancing potential by 2030; Sira-Kvina PSP project cancelled in 2011 due to income uncertainty (p. 117).

## Key findings
- (p. 120, Fig. 1a) More transmission raises the price standard deviation in southern Norway (prices converge to the more volatile continental prices); more PSP lowers it.
- (p. 120) Consumers lose from more transmission and gain from more PSP; transmission affects surpluses more than PSP does.
- (p. 121, Fig. 2b) Socio-economic surplus rises up to 14,100 MW transmission and falls beyond for 4 of 5 PSP sizes; the best Scandinavian solution is to use existing hydro flexibility "or only invest in one PSP".
- (p. 121, Fig. 3b) PSP owners need "a lot of new transmission capacity" before building is attractive. Non-monotone results (9,500 MW better than 950 and 6,650 at low transmission) because the candidate projects differ in cost, efficiency and price area.
- (p. 121-122, Fig. 3a) At low transmission, pump utilisation is low and most income comes from better use of inflow; at high transmission, utilisation is high (e.g. ~1,100 h for 6,650 MW) but revenue nearly zero: large PSP "arbitrages away its own profitability".
- (p. 122) Reasons: the existing Scandinavian hydro system is already very flexible (85 TWh storage) and the model has no ramping/time-delay constraints; fixed continental prices.
- (p. 122) If continental parties covered 50 % of the PSP cost (average 16.3 k€/MW/year), 950, 6,650 and 9,500 MW would be profitable at ~11,000 MW transmission. "It is not realistic to assume that investors make a multi-billion Euro investment with revenues based on expected spot prices."
- (p. 122, conclusion) With >11,000 MW exchange capacity only about 950 MW of PSP is profitable, increasing yearly income by 800 M€ vs. no investment (abstract: 14,100 MW transmission + 950 MW PSP gives the highest socio-economic surplus, +800 M€/year).

## Strengths
- Full-system Nordic model with endogenous Nordic prices, so it captures the price-cannibalisation effect a price-taker model cannot.
- Systematic 5 × 5 grid of PSP and interconnector sizes; separates owner economics from socio-economic surplus.
- Transparent cost assumptions (p. 119).

## Weaknesses / limitations
- Energy-only (no reserves, intraday or balancing), which the authors themselves expect to underestimate PSP value (p. 122).
- Exogenous fixed continental prices; no ramping constraints, so existing hydro is over-flexible (p. 118, 122).
- 3-hour resolution, deterministic weekly LP with EMPS targets (no stochastic intra-week decision).
- Short conference paper; equations garbled in the PDF; some inconsistencies (14,100 vs 18,100 vs 18,300 MW transmission on p. 120-122; Fig. 3a vs 3b referencing on p. 122).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background: Norway's storage share | ~85 TWh, "nearly 50 %" of European reservoir capacity; ENTSO-E 14 GW PSP query; ≥20 GW potential; Sira-Kvina cancelled 2011 | p. 117, Sec. 1 |
| Lit. review: reservoir-sizing / capacity | 5×5 PSP vs interconnector grid; only ~950 MW profitable; owner surplus per MW | p. 119 Table 1; p. 121-122 Figs. 2-3; p. 122 Sec. 4 |
| Lit. review: price-taker limitation / cannibalisation | Large PSP "arbitrages away its own profitability"; more PSP reduces price std. dev. | p. 120 Fig. 1a; p. 122 |
| Lit. review: market participation / gap | Only energy sales; intraday and balancing "will most probably increase PSP profitability" | p. 116-117, p. 122 |
| Model parameters | Pump eff. 90 %, gen. eff. 80-92 %, min. spread ~20 %, PSP capex 0.25-0.5 M€/MW, 60 y lifetime, 4 % discount | p. 118-119 |
| Lit. review: modelling PHS (within-week flexibility) | EMPS heuristic allows only seasonal pumping; LP re-optimisation (ReOpt) needed for within-week pumping | p. 118, Sec. 2.2 |
| Background: price volatility & interconnection | Interconnection raises southern Norway price volatility | p. 120 |

## Useful quotes (with page numbers)
> "the large PSP capacity will depress the high and increase the low power prices, arbitraging away its own profitability." (p. 122)

## Follow-up references to check (backward snowballing)
- [10] Warland, Mo, Helseth (2011), "Handling balancing power in a power market with a large share of hydropower", IEEE PowerTech (ReOpt).
- [8] Wolfgang et al. (2009), "Hydro reservoir handling in Norway before and after deregulation", Energy 34(10).
- [13] Solvang, Harby, Killingtveit (2012), SINTEF TR A7126, balance power capacity in Norwegian hydro (cost data).
- [5] Graabak & Skjelbred (2010), SINTEF TR A7200, large-scale balancing exchange Norway-Europe.
- [15] Henden (2014), NTNU master thesis "Storskala pumpekraftverk".


## Checked against the figures (2026-11-10, Anders/Claude)
Read off Figs. 1-3 in the PDF; values are approximate (read from the plots).
- **Fig. 1b (consumer surplus):** dominated by transmission (0 to about -2,300 MEUR/a from 4,900 to 18,300 MW). The PSP levels differ by only about 100-300 MEUR/a, with more PSP slightly less negative. So consumers gain only a little from PSP. **Inconsistency:** the conclusion (p. 122) says "consumers will lose and the producers will gain a benefit if large-scale PSP should be constructed", the opposite of the results text (p. 120) and of Figs. 1b/2a. Do not cite the paper for the direction of the consumer effect of PSP without this caveat.
- **Fig. 2a (producer surplus incl. PSP investment):** rises with transmission (0 to about +3,500 MEUR/a); more PSP lowers it (at 4,900 MW: about 0 / -50 / -150 / -250 / -400 for 0 / 950 / 6,650 / 9,500 / 14,250 MW).
- **Fig. 2b (socio-economic surplus):** 0 MW and 950 MW PSP almost coincide (about +800 MEUR/a at 14,100 MW, 950 marginally higher). At the same transmission, 6,650 / 9,500 / 14,250 MW give clearly less (about +550 / +400 / +250 at 18,300 MW). So the system model does not favour large PSP either.
- **Fig. 3b (owner surplus per MW, net of investment):** all levels about -15 kEUR/MW/a at 4,900 MW. 950 MW: about 0 at 7,700, +25-30 at 10,500, +40 at 14,100, +48 at 18,300. 6,650 and 9,500 MW: about +10 at 18,300. 14,250 MW: about 0.
- **What this supports:** at the socio-economic optimum (950 MW, 14,100 MW transmission) the owners also earn a return, so system and owner optima coincide here. The paper's value for the system-vs-owner argument is that it reports consumer, producer and owner surplus separately (the owner's share must be computed from the system's prices and dispatch, eq. 5), that consumer and producer surplus move in opposite directions, and that "a significant share of the benefits occurs in continental Europe" while the investor bears the full cost (p. 122). It does **not** show a case where the system model recommends PSP that gives the owner nothing.
