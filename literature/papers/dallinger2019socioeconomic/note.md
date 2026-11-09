---
bibkey: dallinger2019socioeconomic
bibkey_provisional: true
title: "Socio-economic benefit and profitability analyses of Austrian hydro storage power plants supporting increasing renewable electricity generation in Central Europe"
authors: "Bettina Dallinger, Daniel Schwabeneder, Georg Lettner, Hans Auer"
year: 2019
venue: "Renewable and Sustainable Energy Reviews 107, 482–496 (doi:10.1016/j.rser.2019.03.027)"
peer_reviewed: true
methods: [deterministic-lp-milp, hydro-production-function]
review_sections: [market-participation, modelling-phs-plants, reservoir-sizing-capacity, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "TU Wien study in two parts: (i) a Central European 2030 cost-minimising dispatch model (EDisOn+Balancing) shows Austrian PHS/HS expansion cuts generation + aFRR/mFRR procurement costs (9–24 k EUR/MW turbine) and lowers PHS price spreads (storage self-cannibalisation); (ii) a deterministic single-plant MILP on 2015 EPEX day-ahead + Austrian aFRR shows that retrofitting a reservoir plant with pump-turbines, or halving its minimum load, makes reserve provision independent of natural inflow and raises profit, at the cost of more operating hours and machine wear."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/dallinger2019socioeconomic.pdf
---

# Austrian hydro storage: system benefits and single-plant profitability with aFRR (Dallinger et al., 2019)

_Page convention: journal p. = PDF page + 481 (PDF 1 = p. 482). Several tables (Table 1, A.1) are garbled in the text extraction; only numbers that could be read unambiguously are reproduced here._

## Research question / purpose
Two linked questions (p. 483):
1. **Socio-economic benefits** of further expanding Austrian pumped hydro (PHS) and hydro reservoir storage (HS) for the Central European system in 2030, measured with the benefit indicators the European Commission expects for Projects of Common Interest (PCIs): generation and balancing-procurement cost savings, CO2 and pollutant reductions, RES curtailment, peak-price shaving, reduced need for thermal reserve/peaking capacity, net imports (pp. 483–485).
2. **Profitability from the owner's point of view** of technical flexibility measures for a single hydro storage plant (retrofitting a reservoir plant with pump-turbines; reducing minimum load), when it sells on the EPEX day-ahead market and the Austrian aFRR market (pp. 485, 490–494).
Claimed novelty: no previous quantitative benefit analysis of storage according to the PCI indicators; plus business cases that can survive without subsidy (p. 483).

## Setting
- **System:** (i) Central European dispatch model for AT, BE, CH, CZ, DE, FR, HU, IT, NL, PL, SI, SK, with balancing procurement for AT, BE, DE, NL (p. 486, fn 6). Austrian PHS+HS today: up to 6.4 GW turbine, 3.4 GW pumping, reservoirs ~1730 GWh (p. 486); ~3.5 GW new PHS/HS planned by 2030 (p. 486, fn 9). (ii) A single Austrian storage plant with two reservoirs and four turbines (no pumps) in the reference case; the retrofit adds **two pump-turbines between the two reservoirs** (pp. 490–491, Fig. 8). Second case: a single-turbine reservoir plant with minimum load 33 % of nominal (p. 492).
- **Markets:** (i) wholesale + aFRR/mFRR capacity procurement (aFRR daily peak/off-peak, mFRR daily 4-h products, no cross-border balancing; p. 486, fn 10). (ii) EPEX day-ahead + Austrian **aFRR** for 2015 (p. 485). In 2015 Austrian aFRR capacity was procured in daily peak, off-peak and weekend products; weekly peak/off-peak from 2017 with German–Austrian common activation; daily 4-h products from mid-2018 (p. 485, fn 5).
- **Horizon and resolution:** (i) one target year 2030, hourly (h ∈ {1,…,8760}, p. 485). (ii) one historical year (2015); spot optimisation per calendar week with a two-week look-ahead, balancing activations simulated **quarter-hourly** (p. 485).

## Method
- **Model type:**
  - *EDisOn+Balancing* (pp. 484–485): fundamental cost-minimising dispatch LP. Wholesale objective (1): thermal SRMC × generation + start costs + small RES costs + VoLL × unserved energy (VoLL = 3000 EUR/MWh, the EPEX DE/AT day-ahead price cap; p. 485). Balancing extension (2)–(3): weighted sum w1·OF_wholesale + w2·OF_balancing, minimising dispatch and reserve-capacity costs **simultaneously**; storage reserve cost per MW = max(expected DA price − water value (or storage value), C_PS) (eq. 3, p. 485). The paper's own text says the details are in Dallinger et al. 2018, Appl. Energy 222 [30].
  - *Single-plant profitability tool* (p. 485): "linear mixed-integer optimisation problems" maximising spot profit while reserving capacity for balancing; pumps and turbines with "very accurate, piecewise-linear efficiency curves" (p. 485; curves from the technology provider, p. 490 fn 14). Implemented in Julia/JuMP (p. 485, fn 4).
- **Simulation procedure (p. 485):**
  1. Spot optimisation per calendar week: (a) try to keep storage volumes for up- and downward balancing for one week and optimise the remaining flexibility on day-ahead; optimisation horizon two weeks "to ensure that the initial storage level can be reached again", only the first week saved; (b) if infeasible, try to keep storage and balancing energy for one day; otherwise act on spot only.
  2. Balancing simulation: weekly merit-order curves of 2015 balancing-energy bids; activations of the plant derived from historical calls and its bidding strategy; machine reaction and storage effect simulated quarter-hourly over a year.
  - aFRR assumptions: daily peak, off-peak and weekend products; **capacity price bid = 0 EUR/MW**; provision level none / 5 MW (minimum) / 10 % of nominal capacity; energy-price bids of 2×, 5× and 10× the average day-ahead price (p. 485).
- **How uncertainty is represented:** none, deterministic (historical 2015 prices and activations; 2030 scenarios as deterministic sensitivities).
- **Key modelling choices and assumptions:** price taker in the single-plant part; no intraday or portfolio management (acknowledged, p. 490); no head effects mentioned; end-of-week condition = return to initial storage level (p. 485); no machine-wear costs in the objective (wear only discussed, p. 494).

## Data / case
- Three ENTSO-E TYNDP 2018 scenarios for 2030: Sustainable Transition (ST), Distributed Generation (DG), EU external scenario (EC) (p. 486). Fuel and CO2 prices in Table A.2 (CO2: 84.3 / 50 / 27 EUR/t for ST / DG / EC; p. 495).
- Expansion paths: A no new PHS/HS after 2018; B about one third of planned PHS turbine (1 GW) and pump (400 MW) capacity not realised; C all planned PHS/HS realised (p. 486; capacities and reservoir volumes in Table A.1, p. 495).
- Single plant: 2015 EPEX day-ahead prices and Austrian aFRR data (p. 485); turbine and pump-turbine efficiency curves from the technology provider (p. 490).

## Key findings
*System part (Section 4.1)*
- (p. 486) Austrian RES share in 2030 69.6 % (ST) to 87.5 % (EC) in path A; the storage expansion adds 2.4–2.8 percentage points. RES curtailment in Central Europe falls by 1.6 % (ST), 4.8 % (DG), 4.2 % (EC) (A→C).
- (p. 486) CO2 reductions 2–9.1 % in Austria and 0.1–0.5 % in Central Europe per year; monetised 100 / 24 / 48 MEUR/a (ST / DG / EC).
- (p. 488) Average spot price in path A: 88.04 (ST), 69.34 (DG), 45.36 (EC) EUR/MWh. **PHS price spreads decline as PHS capacity grows** (Table 1: ST 28.23 → 25.84 → 25.19; EC 17.03 → 15.87 → 15.61 EUR/MWh for A → B → C, p. 489), which "confirms the theory of economic self-cannibalism of storages" (p. 488).
- (p. 488) Generation + reserve procurement cost savings: path B vs A 100–200 MEUR/a (9,300–18,200 EUR per MW of turbine); path C 148–281 MEUR/a (12,400–23,600 EUR/MW).
- (p. 488) Solar and wind create midday price drops (even negative prices), breaking the classic night-pump/day-generate pattern and opening new storage business cases.
- (p. 489) Comparing the highest 876 residual-load hours, roughly a quarter of the added turbine capacity substitutes thermal capacity (mean/median −478 to −1006 MW); critical hours mainly autumn and winter (p. 488); Dunkelflaute periods need storage with reservoirs (p. 489).
- (p. 494) Abstract/conclusion: environmental damage costs up to 1300 MEUR/a avoided in Central Europe (p. 482, 493).

*Single-plant part (Section 4.2)*
- (p. 491) Without pumps, the plant's minimum load means it must run during the whole reserve product period; for negative reserve it must run above minimum load + offered capacity. With pump-turbines the operating range is about **−70 % to 100 %** of installed turbine capacity, so it does not need to generate to offer negative balancing. "for a pumped storage, the ability to provide enough capacity for a balancing product is independent of natural inflow. Crucial for this is the storage content at the beginning of the product time slice only." (p. 491)
- (p. 491, Fig. 11) Sample day 25 April 2015: the storage plant's natural inflow is insufficient for a whole aFRR product, so it sells only on spot in the highest-price hours; the pumped-storage variant provides balancing all day and does price arbitrage.
- (p. 491) Lower energy bids → more frequent activations; higher bids → higher price per MWh activated. Pumped storage has more operating hours; spot-only pumped storage runs more often at optimum efficiency.
- (p. 492, Fig. 12) Pumped storage earns more than storage (absolute and per MW). Offering 10 % of nominal capacity is "practically never possible" for the storage unit, but always possible for pumped storage (p. 492). Higher profits come with more operating hours and more machine starts.
- (p. 493) Halving the minimum load (33 % → 16.5 %): to reserve 16.7 % of nominal capacity the reference unit must run at ≥ 50 % for the whole product, the modified unit at ≥ 33 %. Minimum-load reduction adds **no value on the spot market alone** (the low-efficiency part-load range is never chosen), but with balancing it "can enable a significant increase in annual profits". Hours of balancing participation rise from ~1600 to ~5400; ~1000 h below the old minimum load; fewer machine starts.
- (p. 494) Both measures raise profits but also wear; "it is important to find the optimum in terms of machine starts and market benefits". Results given per MW turbine capacity for transferability. Future work: higher time resolution, re-dispatch.

## Strengths
- One of few studies that values a **retrofit to pumped storage** and a **minimum-load reduction** explicitly through reserve-market participation (aFRR), with real efficiency curves.
- Clear mechanism: pumping decouples reserve provision from natural inflow; reserve feasibility depends on stored energy at the start of the product window.
- Quantifies storage self-cannibalisation of price spreads at system level.
- Combines system (welfare) and owner (profit) perspectives.

## Weaknesses / limitations
- Deterministic, historical single year (2015) for profitability; no price or inflow uncertainty, no water-value method (weekly two-week rolling optimisation with return-to-initial-level).
- aFRR capacity offered at 0 EUR/MW, so capacity revenue is not really modelled; revenue is from activation energy via a historical merit-order simulation.
- Market rules dated (2015 daily aFRR products; Austria later moved to weekly and 4-h products, p. 485 fn 5; now PICASSO/15-min).
- No intraday, no portfolio effects (p. 490); no head dependence stated; wear not costed.
- Profit numbers mostly in figures (Fig. 12), not tables; Table 1 is hard to read. Some inconsistent wording: p. 492 first says 10 % provision is "hardly possible ... in the pumped storage use case", then that it is "always possible" for pumped storage and never for storage (the first sentence looks like a slip). The abstract says starts increase, p. 493 says minimum-load reduction reduces starts (both may be true for different measures).
- System model: perfect competition, no market distortions, no benefit allocation to individual plants (p. 494).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (market participation): PHS reserve provision independent of inflow | Pump-turbines allow −70 %…100 % range; reserve feasible regardless of inflow, depends on storage at start of product | p. 491, Sec. 4.2.1; Fig. 11 |
| Lit review (sizing / configuration): retrofit reservoir plant with pumps | Retrofit raises profit, operating hours and starts; 10 % reserve always feasible with pumps | pp. 490–492, Figs. 8–12 |
| Lit review / limitations: minimum load limits reserve provision | Halving min load: balancing hours ~1600 → ~5400; no value on spot alone | pp. 492–493, Sec. 4.2.2, Figs. 13–15 |
| Model: reserve requires running above minimum load (+ offered capacity for downward) | Qualitative constraint description | p. 491 |
| Background (price volatility): storage self-cannibalisation of spreads | PHS spreads fall with more PHS capacity, Table 1 | pp. 488–489 |
| Background: solar midday price dips change PHS arbitrage pattern | Qualitative | p. 488 |
| Background (electricity markets): Austrian/German aFRR product design history 2015–2018 | Daily peak/off-peak/weekend → weekly → 4-h products | p. 485, fn 5; p. 486 fn 10 |
| Background (PHS technology): repowering/retrofit trend, variable speed (Goldisthal) | Literature summary | p. 483 |
| Background: system value of Alpine PHS (cost savings per MW, thermal capacity substitution) | 9,300–23,600 EUR/MW; ~¼ of thermal capacity substituted | pp. 488–489 |
| Lit review: deterministic benchmark design | Weekly optimisation with 2-week horizon, keep first week, return to initial level | p. 485, Sec. 3.2 |

## Useful quotes (with page numbers)
> "for a pumped storage, the ability to provide enough capacity for a balancing product is independent of natural inflow. Crucial for this is the storage content at the beginning of the product time slice only." (p. 491)

> "a reduction in the minimum load for operation on the spot market does not add value." (p. 493)

## Follow-up references to check (backward snowballing)
- [30] Dallinger, Auer, Lettner (2018), Impact of harmonised common balancing capacity procurement in selected Central European electricity balancing markets, Applied Energy 222:351–368 (EDisOn+Balancing formulation).
- [17] Henden, Doorman, Helseth (2016), Economic analysis of large-scale pumped storage plants in Norway, Energy Procedia 87 (= `henden2016economic`, in our library).
- [13] Gimeno-Gutiérrez & Lacal-Arántegui (2015), European PHS potential from two existing reservoirs (= `gimeno2015assessment`, in our library).
- [10] Deane, Ó Gallachóir, McKeogh (2010), techno-economic review of PHS (cf. `deane2013derivation` for a different Deane paper).
- [12] Kougias & Szabó (2017), PHS utilisation assessment, Energy 140.
- [18] Karhinen & Huuki, private and social benefits of PHS with wind (Pyhäjärvi, Finland).
- [21] Anagnostopoulos & Papantonis (2012), pumped storage added to a conventional hydro plant (sizing guidelines).
- [38] Ehlers (2011), PhD TU Berlin, storage self-cannibalism.

