---
bibkey: philpott2023using
bibkey_provisional: false   # in references.bib since 2026-11-15 (added through Zotero, key pinned)
title: "Using JADE to analyse pumped storage in New Zealand"
authors: "Andy B. Philpott, Anthony Downward"
year: 2023
venue: "Technical report, Electric Power Optimization Centre (EPOC), University of Auckland, 28 March 2023; www.epoc.org.nz/papers/JADEOnslow.pdf"
peer_reviewed: false
methods: [sddp-time-series, uncertainty-modelling]
review_sections: [ldes-seasonal-storage, modelling-phs-plants, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-15
takeaway: "SDDP study (JADE on SDDP.jl, infinite horizon, weekly stages, system cost minimisation) of a seasonal pumped storage, Lake Onslow (1500 MW, 5000 GWh, 77 % round trip), in a renewable New Zealand system in 2035: the storage lowers prices in most years but empties after consecutive dry years, and its simulated operating profit never recovers the NZD 15.7 billion investment; reserve capacity is not modelled."
---

# Pumped storage in an SDDP system model: Lake Onslow (Philpott & Downward, 2023)

_Technical report (grey literature, not peer reviewed), 31 pages, downloaded 2026-11-15 from the EPOC web site. Page numbers are the report's pages (= PDF pages). The model and the Onslow case reappear in the peer-reviewed `hole2025capacity`._

## Research question / purpose
What does a proposed seasonal pumped storage (Lake Onslow) do to the operation, prices and costs of a fully renewable New Zealand electricity system in 2035, compared with building more wind only or wind plus peaking plant (abstract, p. 1; aim, p. 2)? The report shows what an SDDP model can say about such a storage; it is not a full cost-benefit analysis (p. 2).

## Setting
- **System:** New Zealand, 11 transmission regions, existing hydro reservoirs and river chains, new wind, optional peakers; **Lake Onslow pumped storage: 3,100 Mm3, 5,000 GWh, 1,500 MW pumping and generation** (p. 5, p. 11).
- **Markets:** none modelled. Central planning: minimise expected fuel cost plus cost of shed load; corresponds to a market where all agents offer at marginal cost and are risk neutral (p. 2). Prices are read from the duals.
- **Horizon and resolution:** infinite horizon in a 52-week cycle ("steady state"); each week is represented by blocks of a load duration curve (pp. 4, 9–10).

## Method
- **Model type:** multistage stochastic linear program, weekly stage problem given in full with indices, parameters and variables (pp. 3–4).
- **How uncertainty is represented:** weekly inflows, stagewise independent, sampled from historical years 1990–2019 with an adjusted variance (p. 2, p. 11). Wind and demand enter through the load duration curves and are deterministic within the model (pp. 9–10).
- **Solution method:** SDDP with SDDP.jl on a cyclic policy graph; annual discount factor 0.9, applied as a weekly factor (annual factor to the power 1/52) (p. 4, p. 11). The report notes that the infinite-horizon training needs many more iterations than a finite-horizon one (p. 4).
- **Evaluation:** continuous simulation over the historical inflow years 1932–2020, so the storage at the end of one year is the start of the next; 1000 sampled hydrological years for price risk; 1000 sequences of 25 years for the net present value (pp. 11–12, 15, 17).
- **Capacity choice:** wind capacity is found by re-running the model for different capacities until the generation-weighted average price of wind equals its levelised cost (p. 11). The storage size is fixed.

## Model elements (pp. 3–5)
- **Sets:** weeks, network nodes, load blocks, plants, reservoirs, load types.
- **Parameters:** peaker marginal cost; cost of each load-shedding tranche (Table 5, p. 11: 530 to 10,580 $/MWh); conversion factor from water flow to power; demand per node and block; hours per block; plant capacity in m3/s; spillway capacity; reservoir capacity; river-chain incidence matrix; transmission limits.
- **Constraints:** demand balance per node and block; water balance; capacity bounds; minimum flows from environmental consents in some cases (p. 4).
- **Pumped storage:** two arcs, a release arc and a pumping arc, with a **constant pumping efficiency of 77 %**: the conversion factor of the release arc is 0.77 times that of the pumping arc (p. 5). The same variables and constraints serve for pumping, with a negative conversion factor (p. 4).
- **Not in the model:** reserve capacity (p. 21); unit commitment; head effects.

## Data / case
- Demand for 2035 from the Climate Change Commission's 2021 draft advice ("Demonstration" scenario), scaled from 2020 half-hourly data (pp. 6–8, 10).
- Three cases (p. 11): wind only, 4,800 MW of new wind; Onslow with 3,725 MW of wind; green peakers, 500 MW at 160 $/MWh fuel cost, with 3,900 MW of wind.
- Estimated capital cost of Onslow: NZD 15.7 billion (p. 2).

## Key findings
- (p. 12, Fig. 3) Onslow is almost full at the start of 25 % of the simulated years, and the other reservoirs can then be kept lower, which reduces spill.
- (p. 13) Marginal water values are centred lower with Onslow, but their maxima are much higher: after consecutive dry years (1977–1978) the storage runs very low.
- (p. 13, Table 7 on p. 15) Load-weighted average price: 75.8 $/MWh with Onslow, 116.0 with peakers, 181.0 with wind only. The average cost of pumping is about 18 $/MWh.
- (p. 16) Average annual load-shedding cost: 314.4 M$ (wind only), 96.4 M$ (Onslow), 81.8 M$ (peakers).
- (p. 17) Including the annualised investment, the Onslow case is 1.11 billion $ a year more expensive than the wind-only case; a discount rate of 2.5 % for Onslow would be needed for parity.
- (p. 17) Net present value of Onslow's operating profit over 25 years at a discount factor of 0.9: no simulated sequence recovers the 15.7 billion $ cost, and only 1 of 1000 recovers 4 billion $. Most of the profit comes in dry years when prices are set by load shedding.
- (p. 20) Onslow lowers the break-even level of wind investment (3,725 MW against 4,800 MW), contrary to the idea that pumping puts a floor under wind prices.
- (p. 20) Onslow does not remove the dry-winter problem: extreme shortages still occur after consecutive dry years.

## Strengths
- A seasonal (multi-year) pumped storage inside an SDDP model, with the full stage problem written out.
- Long historical simulation (89 years) in sequence, which shows what happens after consecutive dry years.
- Openly lists what is missing (p. 21).

## Weaknesses / limitations
- Not peer reviewed.
- System cost minimisation with fixed demand; no owner perspective, no reserve markets (p. 21).
- Inflows stagewise independent; load blocks instead of chronological hours, so short cycles are only roughly represented.
- The discount factor of 0.9 was chosen "for convenience" (p. 21).
- Storage size and pump capacity are fixed; only wind capacity is varied.

## Use it for… (lookup guide)
| Use in our thesis | What the report provides | Where (page/section) |
|---|---|---|
| Literature review 5.5 and gap 5.7: SDDP applied to seasonal pumped storage | Onslow study; system model, no reserves | pp. 1–5, 21 |
| Model: pump as a separate arc with constant round-trip efficiency | 77 % assumption | p. 5 |
| Model: infinite horizon with weekly discounting | steady-state optimisation | p. 4 |
| Method: evaluation on a continuous sequence of historical years | 1932–2020 simulation | pp. 11–12 |
| Results chapter: seasonal storage empties after consecutive dry years; value concentrated in few years | water values, NPV distribution | pp. 13, 17, 20 |
| Limitation shared with us or not: reserve capacity not modelled | further work item 4 | p. 21 |

## Useful quotes (with page numbers)
> "Reserve capacity has not been considered in this study." (p. 21)

## Follow-up references to check (backward snowballing)
- Majeed (2019), PhD thesis, University of Waikato: a multi-use seasonal pumped storage scheme in New Zealand's South Island (their [9]).
- Bardsley (2005), note on the pumped storage potential of the Onslow–Manorburn depression (their [1]).
- Dowson & Kapelevich (2021), SDDP.jl (their [5]).
