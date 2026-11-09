---
bibkey: drury2011value
bibkey_provisional: true
title: "The value of compressed air energy storage in energy and reserve markets"
authors: "Easan Drury, Paul Denholm, Ramteen Sioshansi"
year: 2011
venue: "Energy 36, 4959-4973"
peer_reviewed: true
methods: [deterministic-lp-milp, heuristics-simulation]
review_sections: [market-participation, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/105_Drury_2011_The_value_of_compressed_air_energy_storage_in_energy_and_reserve_markets.pdf
takeaway: "Perfect-foresight MILP dispatch of CAES on historical US day-ahead energy and spinning/non-spinning reserve prices (CAISO, MISO, NYISO, PJM, 2002-2010): co-optimising reserves adds $23±10/kW-yr (conventional) and $28±13/kW-yr (adiabatic); design parameters mainly move arbitrage revenue, except generator (expander) size, which reserves reward."
---

# Value of CAES in energy and reserve markets (Drury, Denholm and Sioshansi, 2011)

_**Version and page mapping:** published Elsevier version; journal page = PDF page + 4958 (pp. 4959-4973 = PDF pp. 1-15). The PDF header gives "Energy 36 (2011) 4959-4973" (no issue number shown)._

## Research question / purpose
- Quantify (1) the added value of providing operating reserves on top of energy arbitrage for CAES, (2) how a co-optimised device dynamically allocates capacity between energy and reserves, and (3) the sensitivity of net revenues to design and performance parameters (efficiency, storage hours, compressor/expander size, minimum output) (p. 4959).

## Setting
- **System:** single CAES device, conventional (gas-fired, heat rate 4,220 kJ/kWh, energy ratio 0.72) and adiabatic (round-trip efficiency 0.72); reference case 20 h storage at full expander output, expander:compressor 1:1, minimum load 20% (Table 2, p. 4960). PHS is named as the other bulk long-term technology (p. 4959).
- **Markets:** hourly day-ahead energy, spinning and non-spinning reserves; price-taker (p. 4961). Reserves rarely called, so revenue is essentially capacity payment (footnote 5, p. 4961). Regulation and capacity payments not modelled (pp. 4965, 4971).
- **Horizon and resolution:** hourly, optimised in two-week windows (p. 4961), for each market-year: CAISO 2009-2010, MISO 2009, NYISO 2002-2009, PJM 2005-2009, at a reference (proposed CAES site) and a high-value location (Table 1, p. 4960).

## Method
- **Model type:** MILP maximising net revenue from energy and reserve sales minus electricity, gas and O&M costs, with compressor/expander on-off and start-up binaries, minimum loads, storage balance and no simultaneous compression and expansion (Appendix A, eqs. 4-11, p. 4971).
- **Reserve rules (p. 4961, Fig. 1):** spinning reserve only when online: while charging, up to the charging power (by switching the compressor off); while generating, up to unused expander capacity; non-spinning reserve up to expander capacity while idle or charging.
- **How uncertainty is represented:** deterministic, perfect foresight of historical prices within each two-week window (p. 4961); a one-day "back-casting" rule (apply yesterday's optimal schedule) gives a lower bound (Sec. 4.5, p. 4970).
- **Key modelling choices and assumptions:** price-taker; historical prices; economics judged by dividing annual net revenue by an 11% capital charge rate to get the supportable capital cost (p. 4964).

## Data / case
- Historical nodal/zonal DA energy and reserve prices and EIA monthly state gas prices (pp. 4960, Table B.1 p. 4972). Eight system variants per market and year (conventional/adiabatic × reference/high-value × arbitrage-only/co-optimised) (p. 4961).

## Key findings
- (p. 4959, 4964) Co-optimising reserves raises annual net revenue by **$23 ± 10/kW-yr (conventional)** and **$28 ± 13/kW-yr (adiabatic)**; typically $10-30/kW-yr per case (p. 4964). Added revenue ≈ $15/kW-yr + 0.13 × arbitrage revenue (conventional, R² 0.95) and ≈ $16/kW-yr + 0.22 × arbitrage revenue (adiabatic, R² 0.89) (p. 4964).
- (p. 4962, Fig. 2-3) Co-optimised CAES spends much more time **partially discharging** (up to 50% of hours in the NYISO reference zone) selling energy and spinning reserve at the same time; arbitrage-only CAES runs at full charge/discharge or idles.
- (pp. 4962-4963, Fig. 4) The optimal energy/reserve allocation has seasonal patterns but shifts strongly week to week and year to year, so a fixed or rule-based split cannot capture the full value; storage must be allocated dynamically.
- (p. 4962, Table 3) Inter-annual prices and location change revenues by a factor 2-3; reserve add-on is much less location- and year-dependent ($21-26/kW-yr in 5 of 6 NYISO cases).
- (p. 4964) Co-optimised devices also have lower operating cost: in low-spread hours they sell reserves instead of cycling.
- (p. 4965) Arbitrage alone rarely supports CAES investment; arbitrage + reserves could support conventional CAES in several markets, adiabatic CAES mostly not. European (Danish) arbitrage values are lower because hydropower flattens prices (p. 4965).
- (p. 4967) A 10% better heat rate or energy ratio adds about $5/kW-yr; a 10% better adiabatic round-trip efficiency about $10/kW-yr. Efficiency affects arbitrage, not reserve revenue (p. 4966).
- (pp. 4967-4968, Fig. 10) **Storage duration:** 20 → 40 h adds less than $5/kW-yr; 20 → 12 h loses less than $5/kW-yr; below about 10 h revenue drops sharply (4 h earns $20-30/kW-yr less than 20 h at high-value sites, $5-10 at reference sites). Duration mainly affects arbitrage; nearly identical for co-optimised and arbitrage-only.
- (pp. 4968-4970, Figs. 11-13) **Power sizing:** doubling the expander (generator) relative to the compressor adds $25-50/kW-yr for co-optimised systems but only ~$10/kW-yr for arbitrage-only; relative ROI +30-50% vs +10-20%. Reserves are a capacity product, so generator capacity is rewarded; for co-optimised systems there is no clear optimum expander size (keeps rising). Oversizing the compressor pays for adiabatic arbitrage-only devices.
- (p. 4970, Fig. 14) Lowering minimum expander output from 20% to 10% adds $2-6/kW-yr (more spinning headroom at low output); raising it to 40% loses $5-10/kW-yr.
- (pp. 4970-4971, Table 5) One-day back-casting captures 63-85% of perfect-foresight revenue; co-optimised systems capture more (73-85%) because reserve prices are steadier than energy spreads.
- (p. 4971) Conclusion: optimal CAES design is largely independent of dispatch strategy, except the expander size.

## Strengths
- Clean, multi-market, multi-year empirical valuation of a bulk storage device in energy + reserves, with sizing sensitivities (duration, charge vs discharge power, minimum load) that map directly to PHS design questions.
- Explicit reserve-provision logic for a device with distinct charging and generating machines.

## Weaknesses / limitations
- Perfect foresight (upper bound) plus a crude back-casting lower bound; no stochastic optimisation.
- US markets 2002-2010, gas-dependent conventional CAES economics; no regulation or capacity revenues; price-taker.
- Two-week windows with no end-of-window storage value.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: energy + reserve co-optimisation of bulk storage | +$23±10 / +$28±13 per kW-yr from reserves | p. 4959 (abstract); p. 4964, Sec. 3.2 |
| Lit review: dynamic allocation between energy and reserves | Allocation shifts weekly and yearly; partial discharge selling both | pp. 4962-4963, Figs. 2-4 |
| Lit review: sizing of storage duration | Diminishing returns beyond ~10-20 h; sharp loss below 10 h | pp. 4967-4968, Sec. 4.2, Fig. 10 |
| Lit review: charge vs discharge power sizing | Oversized expander pays when reserves are co-optimised | pp. 4968-4970, Sec. 4.3, Figs. 11-13 |
| Model: reserve headroom rules for a pump/generator device | Spinning reserve from charging power or unused generating capacity | p. 4961, Fig. 1; Appendix A p. 4971 |
| Method: perfect foresight vs implementable policy | Back-casting captures 63-85% of perfect-foresight value | pp. 4970-4971, Sec. 4.5, Table 5 |
| Background: storage economics and capital charge | 11% capital charge rate translation to supportable $/kW | p. 4964-4965 |

## Useful quotes (with page numbers)
> "CAES resources need to be dynamically allocated at these short time scales to capture the full value provided by storage devices." (p. 4971)

## Follow-up references to check (backward snowballing)
- Sioshansi, Denholm, Jenkin and Weiss (2009, ref. [10]), value of storage in PJM, Energy Economics 31: 269-277 (the arbitrage-only base model extended here).
- Sioshansi, Denholm and Jenkin (2011, ref. [8]), pure vs hybrid storage value, Energy Economics 33: 55-66.
- Lund and Salgi (2009, ref. [6]), role of CAES in future sustainable energy systems (Denmark), Energy Conversion and Management 50(5).
- Eyer and Corey (2010), Sandia storage benefits report.
- Walawalkar, Apt and Mancini (2007), storage arbitrage and regulation in NYISO.

