---
bibkey: sintef2025emps
bibkey_provisional: true
title: "EMPS – multi area power-market simulator"
authors: "SINTEF (contact: Birger Mo)"
year: 2025
venue: "SINTEF software web page (sintef.no)"
peer_reviewed: false
methods: []
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "SINTEF product page: EMPS optimises and simulates hydrothermal multi-area systems with transmission constraints; it is widely used to forecast Nordic spot prices and for investment analyses, used by most major Nordic players, and recently extended with batteries/short-term flexibility and flow-based coupling."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/55_SINTEF_2025_EMPS_Multi_area_power_market_simulator_NETTSIDE.pdf
---

# EMPS product page (SINTEF, 2025)

**Source file:** `source.pdf` / `source.txt` (1-page snapshot made 28.10.2026). URL: https://www.sintef.no/en/software/emps-multi-area-power-market-simulator/. In English.

## Research question / purpose
Product description of EMPS (EFI's Multi-area Power-market Simulator) and Vansimtap.

## Setting
Nordic and other hydro-dominated systems; long- and medium-term.

## Method
- **Model type:** optimisation and simulation of hydrothermal power systems with transmission constraints and regional hydrology (p. 1).
- The page does not describe the algorithm. In the literature EMPS is an aggregate SDP water-value model with a heuristic drawdown; that comes from other sources, not this page. (unverified here)

## Data / case
n/a.

## Key findings
- (p. 1) Used for **spot price forecasting** and **investment analyses** (transmission lines, power plants); outputs include generation, reservoir levels, inflow, consumption, rationing, imports and exports.
- (p. 1) "Used by most major players in the Nordic power market"; recently enhanced for **short-term flexibility including batteries, and flow-based market coupling**.
- (p. 1) EMPS and Vansimtap are among the most used Nordic energy models; best suited for systems with a large hydro share; available via Python functions.

## Strengths
Authoritative for statements on EMPS's role and use in the Nordic industry.

## Weaknesses / limitations
Marketing-level page; no method details. For the method, cite academic EMPS papers (e.g. Wolfgang et al. 2009).

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where |
|---|---|---|
| Literature review: industry models for Nordic hydro | EMPS scope, users, uses | p. 1 |
| Discussion: where price scenarios come from in practice | EMPS used for spot price forecasts | p. 1 |

## Useful quotes (with page numbers)
> "The model is used by most major players in the Nordic power market." (p. 1)

## Follow-up references to check (backward snowballing)
- Wolfgang et al. (2009), *Energy* (EMPS/SAMLAST); SINTEF Vansimtap documentation.

