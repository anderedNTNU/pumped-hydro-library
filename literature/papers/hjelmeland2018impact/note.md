---
bibkey: hjelmeland2018impact
bibkey_provisional: true    # not in references.bib yet (Zotero was not running 2026-11-15); key follows the Better BibTeX pattern
title: "Impact of Modelling Details on the Generation Function for a Norwegian Hydropower Producer"
authors: "Martin N. Hjelmeland, Arild Helseth, Magnus Korpås"
year: 2018
venue: "Journal of Physics: Conference Series 1042, 012010 (Current Research in Hydraulic Turbines VIII) (doi:10.1088/1742-6596/1042/1/012010)"
peer_reviewed: true
methods: [sddp-time-series, hydro-production-function]
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-15
takeaway: "SDDiP medium-term model (two years, weekly stages, 21 periods per week, energy and capacity market, deterministic prices) used to test how far a nonconcave piecewise-linear generation function can be simplified; the usual concave function raises the objective by about 2 % and overstates generation by 14 % when a minimum discharge forces operation at low output."
---

# Generation function detail in SDDiP (Hjelmeland et al., 2018)

_Open access (CC BY 3.0), published version from the Norwegian research archive (NVA), downloaded 2026-11-15 (hdl.handle.net/11250/2568296). The PDF has a cover page; page numbers below are the **printed article pages 1–8** (PDF page minus 1). Conference-series paper._

## Research question / purpose
How much can the nonconcave generation function of a hydropower station (discharge to power) be simplified without losing its shape, and what is lost when it is replaced by the concave function that linear scheduling models use (abstract, p. 1; contributions, p. 2)?

## Setting
- **System:** two Norwegian stations with Francis turbines: Station A, one unit of 45 MW; Station B, two units of 210 MW each (p. 5). No pumping.
- **Markets:** energy market and capacity (reserve) market at the same time; energy and capacity reserve prices are **deterministic** (p. 2, p. 5).
- **Horizon and resolution:** two years, weekly stages with inflow uncertainty; each week has 21 periods (morning, mid-day, evening for each day) (p. 5).

## Method
- **Model type:** medium-term hydropower scheduling as a multistage stochastic mixed-integer program, written in dense form (eqs. 1–7, p. 2).
- **How uncertainty is represented:** weekly inflow only (p. 2).
- **Solution method:** stochastic dual dynamic integer programming (SDDiP), as in hjelmeland2019tste (p. 2, p. 5). The expected future profit function is computed with the original generation function and then used to simulate each simplified function on 100 scenarios (p. 5).
- **Key modelling choices and assumptions:** generation depends on discharge only, which the authors call reasonable for high head and little reservoir regulation (p. 7).

## Model elements
- **Constraints named in the dense form (p. 3):** reservoir balances and generator-state time couplings (2); energy balance (3); the system's ability to provide capacity reserves (4)–(5); generation function, bypass limits, spillage limits and other system constraints (6).
- **Generation function (eqs. 8–11, p. 3):** piecewise linear in discharge; each segment has a minimum and maximum discharge and a minimum generation; a **binary variable per segment** marks the active segment. With a concave function no binaries are needed, because the most efficient segment is always used first (pp. 3–4).
- **Simplification methods:** a greedy area-removal algorithm (remove the point that changes the shape least; idea from bid-curve reduction) and segmented regression (pp. 4–5).

## Data / case
- Original functions have 18 points (System A) and 11 points (System B) (p. 6).
- A test with a minimum discharge during the summer months for environmental reasons (pp. 6–7).

## Key findings
- (p. 6, Tables 1–2) Removing points cuts the run time and barely changes the expected objective (within a few hundredths of a per cent until many points are removed).
- (p. 6, Tables 1–2) The concave function changes the objective by +2.22 % (System A) and +2.05 % (System B), and the shape of the duration curve by 13 % and 15 %.
- (p. 7) With the minimum discharge requirement, the concave function gave 14.1 % more expected generation than the original; in the other simulations 1.02 % and 0.34 %. A concave function overstates efficiency at low output.
- (p. 1) Earlier work found that LP-based scheduling tends to overestimate the reserve capacity a producer can deliver (their ref. [3], hjelmeland2016combined).

## Strengths
- Shows with numbers what the concave (linear) generation function hides.
- Open access.

## Weaknesses / limitations
- Deterministic prices; inflow is the only uncertainty.
- The equations are partly lost in our text copy (symbols missing); read the PDF for them.
- Station labels in the results text do not seem to match the case description (a best-efficiency point near 180 MW is discussed under "System A", which is described as 45 MW) **(unverified which label is wrong)**.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation of our linear model: constant efficiency / concave generation overstates low-load operation | +14.1 % generation with a minimum discharge; about +2 % objective | pp. 6–7, Tables 1–2 |
| Limitation: LP models overestimate deliverable reserve capacity | statement with reference | p. 1 |
| Model: 21 periods per week in a medium-term model | case description | p. 5 |
| Background: long-, medium- and short-term scheduling and the water value | Sec. 2 | pp. 1–2 |

## Useful quotes (with page numbers)
> "it overestimates the efficiency of the station" (p. 7, on the concave generation function)

## Follow-up references to check (backward snowballing)
- Fodstad, Aarlott & Midthun (2018), value-creation potential from multi-market trading for a hydropower producer, Energies 11(1) (their [2]).
