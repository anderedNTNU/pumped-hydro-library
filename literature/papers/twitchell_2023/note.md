---
bibkey: twitchell_2023
title: "Defining long duration energy storage"
authors: "Jeremy Twitchell, Kyle DeSomber, Dhruv Bhatnagar"
year: 2023
venue: "Journal of Energy Storage, 60, 105787"
peer_reviewed: true
methods: []
review_sections: [ldes-seasonal-storage]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "PNNL survey of LDES definitions (emerging consensus: at least 10 h at rated power; Table 2 lists 8–12 h, 10+ h, 10–100 h, 8–24 h, 4/6/8/10 h) plus an illustrative decarbonised-California analysis concluding that two LDES classes are needed: up to 20 h for daily cycles and weeks-to-months for seasonal cycles."
---

# Defining long duration energy storage (Twitchell et al., 2023)

_Article number 105787, pages 1–7 (PDF page = article page)._

## Research question / purpose
How are industry and academia defining "long-duration" energy storage (LDES), and what durations will a decarbonised grid actually need? The paper (i) reviews current storage uses and how they change, (ii) surveys existing LDES definitions, and (iii) uses an illustrative decarbonised California grid to quantify the depth and breadth of generation–load mismatches and derive the durations needed (abstract, p. 1).

## Setting
- **System:** US grid in general; California (CAISO) for the illustrative example (pp. 2–5).
- **Markets:** CAISO day-ahead, hour-ahead (15-min), Western Energy Imbalance Market, ancillary services, resource adequacy/capacity (pp. 2–3); PJM capacity market rules (p. 4).
- **Horizon and resolution:** one year of hourly EIA load and generation data, Aug 2020–Jul 2021, analysed hourly and aggregated weekly (p. 4–5, Figs. 6–7).

## Method
- **Model type:** review of definitions plus a simple scaling (energy-balance) exercise, no optimisation.
- **How uncertainty is represented:** none (historical year, deterministic).
- **Solution method:** remove 71.3 % of ineligible generation (41.7 % fossil + nuclear to retire + 24.2 % imports assumed unavailable; 47.1 % in-state replacement) and scale wind and solar each by a factor **4.628**, preserving their ~2:1 solar:wind ratio and existing profile shapes, until annual energy balances (p. 5).
- **Key modelling choices and assumptions:** storage round-trip losses ignored (no extra generation added for them); no overbuilding, regional coordination, offshore wind or electrification considered (stated limitations, p. 5).
- **Duration definition (p. 2, Table 1, eq. 1):** duration = the length of time a technology can sustain its **full rated power output**; E (MWh) = P (MW) × t (h). Duration depends on discharge rate: a 1 MW/4 MWh system lasts ~4 h at full power but ~8 h at 0.5 MW (p. 2).

## Data / case
- EIA Hourly Electric Grid Monitor, California, Aug 2020–Jul 2021 (p. 4). US storage statistics from EIA and Wood Mackenzie/ESA (p. 2).

## Key findings
- (p. 2) Storage is measured in two dimensions: power rating (kW/MW) and energy rating (kWh/MWh). Ancillary services can be provided by storage with **≤ 2 h** duration; 59 % of US storage since 2016 provides frequency regulation; in 2020 shares providing spinning reserve, arbitrage and load following grew to 39 %, 37 % and 26 %; average duration of new US systems grew from ~1 h (2013) to ~3.7 h (H1 2021).
- (p. 3) As storage serves resource adequacy, remaining peaks get flatter and longer, raising duration requirements; e.g. a 4-h battery for a 6-h peak is credited for only 2/3 of its capacity.
- (p. 3) No standard definition, but an "emerging consensus that LDES means at least 10 h".
- (pp. 3–4, Table 2) Definitions: DOE Storage Shot **10+ h**; CPUC IRP long duration **8–12 h** (short ≤ 4 h); California Energy Commission **10+ h**; ARPA-E DAYS **10–100 h**; LDES Council **8–24 h** (two archetypes: 8–24 h and ≥ 24 h); PJM capacity rules **4, 6, 8, 10 h** classes (original 10-h requirement criticised and revised).
- (p. 4) Literature: LDES necessity manifests above ~80 % variable renewable generation (Shaner et al. [9]); a decarbonised system with ≥ 100 h LDES would likely cost less than one with shorter storage (Sepulveda et al. [10]).
- (p. 5) Decarbonised California example: insufficient energy in **61 % of hours**; largest hourly deficit 44.9 GW, largest surplus 60.9 GW; **23 surplus weeks and 29 deficit weeks**; overnight deficits last **12–19 h, average 14.6 h** → first LDES class with up to **20 h** duration for diurnal cycles. Surplus weeks run mid-Feb to early Aug, deficit weeks early Aug to mid-Feb → second class, **seasonal** storage that shifts energy over several weeks to months (Fig. 7).
- (p. 5) Wind-heavy regions may show inverse cycles (daytime and summer deficits) (Dowling et al. [16]).
- (p. 6) Real examples: California 14–15 Aug 2020 shortfalls; PJM July 2020 wind below 10 % of monthly average for 72 h (3 GW shortfall); Costa Rica uses hydropower reservoirs for seasonal dry periods.
- (p. 6, conclusion) Two classes of LDES needed; apart from pumped hydro and compressed air, other LDES technologies are not mature; PHS and CAES have **geographic constraints** limiting their ability to meet the scale of LDES needs; charging schemes and the economics of long vs multiple short-duration systems left for further work.

## Strengths
- Compact, citable survey of definitions (Table 2) and a precise duration definition at rated power.
- Links duration needs to observable diurnal vs seasonal mismatch patterns.

## Weaknesses / limitations
- US/California-centric and policy-driven; illustrative only (authors say it is not a prediction, p. 5).
- Simple scaling of existing profiles; no storage operation, losses or costs.
- Inconsistent description of the seasonal class: "weeks or months" (abstract), "days or weeks" (p. 1 intro), "several weeks to months" (p. 5).
- Does not distinguish discharge duration from how long energy is held in storage (storage time), which our background treats separately.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background (LDES): no universal definition; ≥ 10 h consensus | Survey of definitions | p. 3 (Sec. 4), p. 4 (Table 2), p. 6 (Sec. 7) |
| Background (LDES): list of thresholds | 10+ h, 8–12 h, 10–100 h, 8–24 h / ≥ 24 h, 4/6/8/10 h | pp. 3–4, Table 2 |
| Background (LDES): definition of duration at rated power | Duration = time at full rated output; E = P·t; duration varies with discharge rate | p. 2 (Sec. 2, Table 1, eq. 1) |
| Background (LDES): two classes, daily ≤ 20 h and seasonal | Illustrative decarbonised California analysis | p. 1 (abstract), p. 5 (Sec. 5.2), p. 6 |
| Background (LDES): mismatches grow with VRE share | Mismatch argument; > 80 % VRE threshold [9] | p. 1, p. 4 |
| Background (markets): ancillary services need short duration | ≤ 2 h for ancillary services; US storage use shares | p. 2 (Sec. 3) |
| Background (PHS): PHS mature but geographically constrained | Only PHS and CAES mature LDES | p. 6 (Sec. 7) |

## Useful quotes (with page numbers)
> "an emerging consensus that LDES means at least 10 h" (p. 3)

## Follow-up references to check (backward snowballing)
- [10] Sepulveda et al. (2021), The design space for long-duration energy storage in decarbonized power systems, Nature Energy 6 (also cited by zeng_2025).
- [16] Dowling et al. (2020), Role of long-duration energy storage in variable renewable electricity systems, Joule 4.
- [9] Shaner et al. (2018), Geophysical constraints on the reliability of solar and wind power in the US, Energy Environ. Sci. 11.
- [6] LDES Council & McKinsey (2021), Net-zero power: long duration energy storage for a renewable grid (grey literature).

