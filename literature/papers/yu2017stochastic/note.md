---
bibkey: yu2017stochastic
bibkey_provisional: true
title: "Stochastic valuation of energy storage in wholesale power markets"
authors: "Nanpeng Yu, Brandon Foggo"
year: 2017
venue: "Energy Economics 64, 177-185"
peer_reviewed: true
methods: [uncertainty-modelling, deterministic-lp-milp, heuristics-simulation]
review_sections: [market-participation, reservoir-sizing-capacity]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/109_Yu_2017_Stochastic_valuation_of_energy_storage_in_wholesale_power_markets.pdf
takeaway: "Monte Carlo valuation of an 8 MW / 32 MWh Li-ion battery in CAISO (2013-2014): 3-factor HJM futures-curve price paths feed a perfect-foresight LP that co-optimises DA energy and regulation up/down plus a capacity payment; 79% of revenue is regulation, expected 2-year net revenue $2.92M (CVaR95 $1.80M), and a 1:2 power-to-energy ratio beats the usual 1:4."
---

# Stochastic valuation of battery storage in CAISO (Yu and Foggo, 2017)

_**Version and page mapping:** published Elsevier version; journal page = PDF page + 176 (pp. 177-185 = PDF pp. 1-9)._

## Research question / purpose
- Build a valuation framework for grid-scale storage that considers **all key revenue streams simultaneously** (energy shifting, ancillary services, capacity) and characterises the **distribution** of value, i.e. investment risk, rather than a point estimate (p. 177).

## Setting
- **System:** lithium-ion battery modelled on the Tehachapi project: 8 MW / 32 MWh, AC round-trip efficiency 88%, usable range 95%, auxiliary load 0.875% of rated power, self-discharge 1.65%/month, capacity fade 2.5%/yr; capital $551/kW + $614/kWh, balance of plant 20%, fixed O&M $8.18/kW-yr, variable O&M $0.00548/kWh (p. 182).
- **Markets:** CAISO SP15 day-ahead energy, regulation up/down (frequency regulation, AGC-following), and resource adequacy capacity via net qualifying capacity (4-h discharge capability) (pp. 180-182).
- **Horizon and resolution:** valuation January 2013-December 2014, hourly dispatch (p. 182).

## Method
- **Model type:** price-based LP (after splitting discharge into ±) maximising DA energy revenue + regulation revenues − VOM, with state-of-charge dynamics including regulation utilisation factors, SoC bounds, joint power limits for energy + regulation (eqs. 29-38, pp. 181-182).
- **How uncertainty is represented:** (1) **Heath-Jarrow-Morton multi-factor model of the futures curve** with Nelson-Siegel-type volatility functions, estimated from SP15 on/off-peak futures 2009-2012 (Secs. 3.1-3.3, pp. 178-179); PCA: three factors explain more than 90% of futures-curve variation in California, versus 8 factors needed in the Nordic market (Koekebakker and Ollmar 2005) (p. 179). (2) 1,000 Monte Carlo monthly price paths (p. 182), converted to hourly LMPs by scaling the actual 2012 hourly profile (p. 182). (3) Regulation prices via a regression of the regulation/energy price ratio on hydro generation and renewable variability with seasonal dummies (eq. 28, Table 3, p. 181).
- **Solution method:** for each price scenario the LP is solved with **perfect foresight within the scenario**, so the valuation is an upper bound on realistic value (p. 182).
- **Key modelling choices and assumptions:** price-taker; no bidding strategy under uncertainty; capacity value blended from short-run RFO bids and long-run cost of new entry (p. 182).

## Data / case
- CAISO SP15 futures (ICE) 2009-2012, start date chosen at the April 2009 market redesign (MRTU) (p. 179); CAISO regulation, hydro and renewable data 2010-2011 for the regulation price model (p. 181).

## Key findings
- (p. 182, Fig. 3) Net revenue over 2 years is roughly log-normal; expected **$2.92M**, CVaR at 95% **$1.80M**.
- (p. 183, Table 4) Revenue breakdown: energy shifting $121,367; regulation up $1,254,524; regulation down $812,698; capacity $430,240; costs (aux load $53,619, fixed O&M $130,720); **79% of revenue from regulation** (p. 183).
- (p. 183, Fig. 4) Each percentage point of round-trip efficiency adds about 1% to expected net revenue, with diminishing returns (1.03% → 0.87% per pp from 80% to 94%); energy-shifting revenue is much more sensitive to efficiency than regulation revenue.
- (p. 183, Fig. 5) Power-to-energy ratio varied 1:1 to 1:8 at fixed 8 MW: best return per dollar near **1:2**, not the industry nominal 1:4; switching 1:4 → 1:2 adds $27,687 per $1M invested over two years, because at 50% SoC the battery can offer full up and down regulation.
- (p. 181) Hydro generation affects regulation-up supply and prices in CAISO (high hydro in spring/winter tightens upward headroom).

## Strengths
- Joint treatment of energy, regulation and capacity revenue streams with a distributional (risk) view of storage value.
- Futures-curve based price simulation consistent with market forward information; reports CVaR of value.
- Shows how design ratio (power vs energy) depends on which services dominate.

## Weaknesses / limitations
- Perfect foresight within each scenario (upper bound); hourly shape fixed to 2012, uncertainty only in monthly levels.
- Short 2-year horizon; battery-specific; CAISO market rules.
- Regulation-price model is simple and in-sample.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: multi-service storage valuation | Energy + regulation + capacity co-optimised; 79% from regulation | pp. 181-183, Sec. 3.6, Table 4 |
| Lit review: sizing, power-to-energy ratio | 1:2 better than 1:4 for regulation-heavy battery | p. 183, Sec. 5.3, Fig. 5 |
| Lit review: efficiency sensitivity | ~1% value per pp of round-trip efficiency | p. 183, Sec. 5.2, Fig. 4 |
| Method: perfect foresight per scenario is an upper bound | Explicit statement | p. 182 |
| Background: futures-curve modelling (HJM, PCA factors) | 3 factors >90% in CAISO vs 8 in Nordic (cited) | pp. 178-179, Secs. 3.1-3.2 |
| Model: SoC with regulation utilisation factors | eqs. (29)-(38) | pp. 181-182 |

## Useful quotes (with page numbers)
> "Therefore, the valuation provided in this study serves as an upper bound of the battery storage system's realistic value." (p. 182)

## Follow-up references to check (backward snowballing)
- Koekebakker and Ollmar (2005), forward curve dynamics in the Nordic electricity market (8 factors for 90% variance).
- Bakke, Fleten et al. (2016), real options investment in electric energy storage, Comput. Manag. Sci. 13.
- Sioshansi et al. (2009), value of storage in PJM.
- Walawalkar, Apt and Mancini (2007), storage arbitrage and regulation in New York.
- Jiang and Powell (2014), ADP for battery bidding in real-time market.

