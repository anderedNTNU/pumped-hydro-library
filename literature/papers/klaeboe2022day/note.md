---
bibkey: klaeboe2022day
bibkey_provisional: true
title: "Day-ahead market bidding taking the balancing power market into account"
authors: "Gro Klæboe, Jørgen Braathen, Anders Lund Eriksrud, Stein-Erik Fleten"
year: 2022
venue: "TOP 30, 683-703"
peer_reviewed: true
methods: [multistage-scenario-trees, deterministic-lp-milp, uncertainty-modelling, hydro-production-function]
review_sections: [market-participation, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/102_Klboe_2022_Day_ahead_market_bidding_taking_the_balancing_power_market_into_account.pdf
takeaway: "Three-stage stochastic MILP for a price-taking Norwegian reservoir producer bidding into day-ahead and the (mFRR-type) balancing energy market: coordinated bidding gains only 0.1% under 2012 conditions, but 3.9-6.0% if balancing frequency and volume double; joining the balancing market at all adds 3.1-14.4%."
---

# Day-ahead bidding with the balancing market (Klæboe et al., 2022)

_Page mapping: journal page = PDF page + 682 (journal pp. 683-703). Open access (CC BY 4.0). An SSRN version from 2019 is cited by Schindler et al. (2024) as "Klæboe et al. (2019)"._

## Research question / purpose
- Does it pay for a flexible, price-taking generator to **coordinate** its day-ahead (DA) bids with the subsequent energy-only **balancing market (BM)** (Nordic regulating power market, i.e. manually activated tertiary reserve/mFRR energy), compared with **myopic** (sequential) bidding (pp. 683, 685)?
- Three insights claimed (pp. 685-686): (1) near-zero coordination gains in the current Nordic market; (2) gains of about 4% if the need for balancing doubles in frequency and volume, about 6% if the balancing supply curve is also convex; (3) coordinated DA bid curves look like exercise of market power although the producer is a price-taker.

## Setting
- **System:** Norwegian cascade with a large upper reservoir (178 Mm³) and small lower reservoir (1.6 Mm³); one 45 MW unit upstream, two units totalling 150 MW downstream; no time delays; **no pumping** (pp. 692, 697-698, Fig. 1).
- **Markets:** Nord Pool day-ahead (hourly bids, no block bids) and Norwegian balancing market for up- and down-regulation (energy only; capacity markets not modelled) in NO2, with **dual imbalance pricing** (in force until 1 November 2021) (pp. 690-691). Intraday ignored as smaller than BM in the Nordic market (BM about 1% of consumption; DA about 80%) (p. 690).
- **Horizon and resolution:** four days, hourly; bidding and balancing only on day 1, later days valued at scenario prices without bidding (pp. 690-691, 698).

## Method
- **Model type:** stochastic MILP, collapsed to **three stages** (instead of 25 per day): (1) DA bids; (2) DA prices revealed, commitments by simple recourse; (3) BM states, volumes, prices and later DA prices observed, BM commitments, generation, imbalances (pp. 690-691). The producer chooses BM commitments after seeing BM prices, argued to introduce only modest bias (p. 691).
- **Market constraints (pp. 691-692):** DA commitment by interpolation of fixed price points (eq. 1); non-decreasing bids (eq. 2); DA bids ≤ installed capacity (eq. 3); BM commitment ≤ realised BM volume (eq. 4) — volumes are **bounded and event-driven**, not modelled by a price response; up-regulation ≤ capacity − DA commitment (eq. 5); down-regulation ≤ DA commitment (eq. 6); energy balance with imbalance variables (eq. 7); **expected imbalance zero** (eq. 8, Nordic planned-balance obligation; failure "can lead to loss of licence to operate").
- **Hydropower (pp. 692-694):** water balance (eq. 9); concave production-discharge envelope per unit (eq. 10, as Fleten and Kristoffersen 2008), no head-loss interaction between units; start-up costs with binaries (eq. 11); min/max generation (eq. 12); **head variation left for future work** (p. 692).
- **End-of-horizon water value:** linear cuts "supplied from a seasonal planning model (Gjelsvik et al. 2010)" — future income, reference levels and marginal water values (eq. 13, p. 694); seven cuts in the case (p. 698).
- **How uncertainty is represented (pp. 695-697):** DA price = producer's deterministic forecast + ARMA error fitted to the producer's last eight weeks of forecast errors. BM: **balancing state** (none/up/down) with arrival probability as a slow moving-average process (Croston-type separation of event arrival and size), BM volume as unevenly spaced AR(1), BM premium regressed on volume, DA price and total generation (EXO model of Klæboe et al. 2015). DA scenarios reduced with SCENRED; 30 DA × 10 BM = 300 scenarios (p. 697). Almost 50% of Nordic hours have no balancing activation (p. 689).
- **Scenario sets (p. 695, Table 3 p. 696):** A = current Norwegian BM (up-regulation in 24.7% of hours, down 25.6%; mean volume 109/129 MW; mean premium 52.11/54.45 NOK/MWh); B = balancing in every hour with higher volumes (up 49.1%/down 50.9%; 280/286 MW; premium 65.84/65.13); C = as B but up-regulation premium raised disproportionately (88.66 NOK/MWh), emulating a convex supply curve. (Column assignment of Table 3 reconstructed from the extraction.)

## Data / case
- Price forecasts and hydrological data for **week 40 of 2012** from the producer Hydro; production, BM and DA prices from Nord Pool Spot, area NO2 (p. 697).
- GAMS 23.6.5 + CPLEX 12.2; coordinated problem 8,700 s; myopic 23,000 s + 3,270 s (p. 697).
- Gains reported relative to day-ahead revenue from myopic bidding, because the water value term dominates the objective (footnote 3, p. 698).

## Key findings
- (Table 4, p. 697; p. 698) Gain from **participating** in the BM: 3.1% (A), 12.2% (B), 14.4% (C). Gain from **coordinated** bidding over myopic: 0.1% (A), 3.9% (B), 6.0% (C).
- (p. 698) Gains much lower than Boomsma et al. (2014), who report 8-25%, because this model bounds BM liquidity and imposes planned balance (eq. 8). Without eq. (8) the model withholds DA volume and sells "imbalance" — a modelling flaw, not a profit opportunity (p. 699).
- (p. 699) Doubling frequency and volume of balancing means about 4% of annual consumption, "not unrealistic" with more wind and transmission to wind/PV areas.
- (pp. 699-700, Fig. 3) Coordinated DA bids offer more volume at low prices (keep the option of down-regulation, especially at night) and less at high prices (keep capacity for up-regulation); the shape resembles a price-maker's curve and may attract unwarranted regulatory scrutiny (pp. 700-701).
- (p. 700) Out-of-sample simulation of set A gives the same gain as in-sample. Profit standard deviation similar for both strategies except under asymmetric costs (C), where coordination adds variability (Table 5).
- (pp. 700-701) Conclusion: coordination not worthwhile today, consistent with Aasgård (2022) and Löhndorf and Wozabal (2022/2023); but flexible generators should monitor it because modest increases in post-DA volumes make it profitable.

## Strengths
- Realistic Nordic market rules: bounded event-driven BM volumes, zero expected imbalance, dual pricing; careful discussion of why earlier studies overestimated gains (pp. 688-689, 698-699).
- Scenario model of the BM that separates event arrival from magnitude.
- Forward-looking scenarios (B, C) linking balancing needs to renewable growth.
- Detailed hydro: start-up costs, concave PQ curves, water-value cuts from the seasonal model.

## Weaknesses / limitations
- One week of 2012 data, one producer, no pumping; BM is energy-only (no capacity payments, no aFRR/FCR).
- Clairvoyance in BM commitments (decided after prices are known) overestimates profit slightly (p. 691).
- Bidding only on day 1 of a four-day horizon; no long-term uncertainty.
- Market rules have since changed (single imbalance price from November 2021; 15-min MTU, new mFRR energy activation market), so the numerical gains may be outdated.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Literature review 5.4: value of balancing market participation for Nordic hydro | 3.1/12.2/14.4% (participation), 0.1/3.9/6.0% (coordination) | p. 697 (Table 4), p. 698 |
| Literature review 5.4: why earlier coordination gains were too high | No planned-balance rule, unbounded BM volumes, price response | pp. 688-689, 698-699 |
| Background 2.4: Nordic balancing market design | Up-regulation price ≥ DA, marginal pricing, dual imbalance pricing until 1 Nov 2021, BM ~1% vs DA ~80% of consumption | pp. 687, 690 |
| Background 2.4: balancing is event-driven | ~50% of hours without activation | p. 689 |
| Model: planned balance / zero expected imbalance | Eq. (8) and legal justification | p. 692 |
| Model: limits on up/down reserve given DA position | Eqs. (5)-(6) | p. 692 |
| Model: water value cuts at end of short-term horizon | Eq. (13), cuts from seasonal model | p. 694 |
| Uncertainty modelling: balancing state + volume + premium model | Moving-average arrival, unevenly spaced AR(1), EXO premium | pp. 695-697 |
| Research gap: future growth of balancing needs | Scenario B/C reasoning, ~4% of consumption | p. 699 |

## Useful quotes (with page numbers)
> "only a modest increase in the demand for balancing energy will make coordination profitable" (p. 683)

## Follow-up references to check (backward snowballing)
- Boomsma, Juul, Fleten (2014). Bidding in sequential electricity markets: the Nordic case. EJOR 238(3), 797-809.
- Aasgård (2022). The value of coordinated hydropower bidding in the Nordic day-ahead and balancing market. Energy Systems 13, 53-77.
- Kongelf et al. (2019). Portfolio size's effects on gains from coordinated bidding in electricity markets. Energy Systems 10(3), 567-591.
- Klæboe, Eriksrud, Fleten (2015). Benchmarking time series based forecasting models for electricity balancing market prices. Energy Systems 6(1), 43-61.
- Aasgård, Fleten, Kaut et al. (2019). Hydropower bidding in a multi-market setting. Energy Systems 10(3), 543-565.
- Jaehnert, Farahmand, Doorman (2009). Modelling of prices using the volume in the Norwegian regulating power market.

