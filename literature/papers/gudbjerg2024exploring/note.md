---
bibkey: gudbjerg2024exploring
bibkey_provisional: true
title: "Exploring the Integration of Pumped Hydro Energy Storage on the Operation of the Eastern Røldal-Suldal Hydropower System"
authors: "Karoline Josefine Gudbjerg"
year: 2024
venue: "Master's thesis (30 ECTS), Environmental Physics and Renewable Energy, Faculty of Science and Technology, Norwegian University of Life Sciences (NMBU). Handle: https://hdl.handle.net/11250/3147994"
peer_reviewed: false
methods: [sddp-markov-chain, hydro-production-function]
review_sections: [modelling-phs-plants, reservoir-sizing-capacity, phs-technology]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Adds a separate pump (10–40 MW, η=0.8) between Kvanndalsfoss and Sandvann at Kvanndal (40 MW turbine) in SINTEF's ProdRisk (SDP/SDDP) model of eastern Røldal-Suldal; 30 serial EMPS 2030 price/inflow years: revenue +1.05% to +2.56% and gross production +1.5% to +3.7%, but net production falls; no investment costs, no reserves."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Medium_term_pumpekraft/Gudbjerg2024.pdf
---

# Adding pumping to the eastern Røldal-Suldal system (Gudbjerg, 2024)

NMBU master's thesis, supervisor Leonardo Rydin Gorjão; ProdRisk access and help from Stefan Rex, SINTEF (p. iii). CC BY-NC-ND 4.0. SINTEF's NVA record also lists supervisors as authors (KILDEINFO).
**Page convention:** printed page = PDF page − 8 (PDF 9 = p. 1); front matter in roman numerals (abstract p. i = PDF 3). 79 PDF pages, read in full (appendix figures skimmed).

## Research question / purpose
"How does employing PHES with the SDDP method impact the eastern Røldal-Suldal hydropower system's operations? How do pump size variations affect the Kvanndal power plant's efficiency and performance?" Also: which pump size is most economically beneficial (p. 10).

## Setting
- **System:** eastern part of Røldal-Suldal (RSK), Suldal municipality, Rogaland (NO2), owned by Lyse Kraft DA (p. 8). Four reservoirs: Holmevann 96 Mm³, Sandvann 66 Mm³ (924–950 masl), Isvann 16 Mm³, Kvanndalsfoss 1.6 Mm³ (620–630 masl); two stations: **Kvanndal** (1967, one Francis, 40 MW, 15 m³/s, gross head 314 m, 188.9 GWh/yr) and **Suldal II** (1967, two Francis, 150 MW, 31.5 m³/s, gross head 559 m, 738.6 GWh/yr) (pp. 9–10). Open-loop, existing conventional plant retrofitted with a separate pump at Kvanndal using the turbine's waterway, pumping Kvanndalsfoss → Sandvann (pp. 26–27).
- **Markets:** day-ahead energy only (prices exogenous). Reserves described (FFR, FCR, aFRR, mFRR, pp. 7–8) and proposed as future work (p. 48), not modelled.
- **Horizon and resolution:** 208-week (4-year) simulation interval starting 7 Jan 2030; weekly SDDP stages with 56 three-hour time steps per week; 50 SDDP iterations; 30 scenarios run in **serial mode** (end reservoir of year k is start of year k+1, cyclic), results reported per 52 weeks (pp. 27–28).

## Method
- **Model type:** SINTEF **ProdRisk** (combined SDP/SDDP) via its Python API (`ProdriskCore`); weekly LP subproblems; system built from SINTEF's existing RSK model, with a pump module added (pp. 24–27).
- **How uncertainty is represented:** inflow (NVE local inflow 1981–2010, 30 years) paired one-to-one with 30 price scenarios (p. 27, 44). ProdRisk treats price as an exogenous stochastic variable handled by an outer SDP layer and inflow through SDDP (p. 25). Prices: HydroCen "Low Emission" 2030 EMPS scenario (Schäffer & Graabak), **scaled to an average of ~210 EUR/MWh** (NO2 2022 average) (p. 28); the source scenario itself gives ~39 EUR/MWh for southern Norway in 2030 (p. 45).
- **Solution method:** SDDP forward/backward passes, 50 iterations; head coefficients from an initial run reused in the final run (p. 46).
- **Key modelling choices and assumptions:** P = f(Q)·h/h₀ with concave piecewise-linear f(Q) and a head-correction factor (p. 23, Eq. 9); PQ curve for Kvanndal (Fig. A.12, p. 68); pump efficiency fixed at 0.8; pump heads from min/max reservoir-level differences; pump discharge from Eq. (3) (p. 27); turbine and pump never simultaneous (p. 22). Price-taker, single-company system (p. 25). No maintenance, no investment cost, no taxes in the model (pp. 45–46).

## Data / case
Pump sizes 0 (baseline), 10, 20, 30, 40 MW (p. 27). SINTEF RSK system data, NVE inflow, HydroCen/EMPS 2030 prices (53 areas, 58 weather years) (pp. 28, 44). Norwegian context: ten existing Norwegian PHS plants, 1369 MW, 5 TWh storage, commissioned 1955–2005, all open-loop, gross 2.6 TWh / pumping 0.8 TWh / net 1.8 TWh per year, designed for seasonal pumping (upper reservoirs much larger than lower) (pp. 2–3, citing Pitorac et al. 2020). Lyse applied for a concession for **Kvanndal 2 PHES** in March 2024 (Holmevann as upper, Kvanndalsfoss as lower, Holmevann regulation extended by 5 m), motivated by spill at Kvanndalsfoss and more near-zero/negative price hours (pp. 10, 38–39).

## Key findings
- (p. 35, Fig. 14) Mean annual gross production (Kvanndal + Suldal II) rises from 962.92 GWh (0 MW) to 1000.03 GWh (40 MW): +1.51 %, +2.31 %, +3.18 %, +3.74 % for 10–40 MW.
- (p. 35–36, Fig. 15, A.6) Net production falls: 962.92 → 961.18, 957.29, 956.33, 955.01 GWh; pumping energy 16.76, 28.58, 38.10, 45.02 GWh/yr.
- (p. 37, Fig. 16) Mean annual revenue relative to no pump: +1.05 %, +1.55 %, +2.12 %, +2.56 % for 10, 20, 30, 40 MW; absolute ≈ 239 MEUR (0 MW) vs ≈ 245 MEUR (40 MW), inflated by the price scaling (p. 45).
- (p. 34, Table 1) Turbine running time 60.53 % (0 MW) → 69.15 % (40 MW); pump running time 19.32 % (10 MW) → 14.06 % (40 MW); idle time 39.47 % → 16.78 %.
- (p. 33–34, Figs. 12–13) Turbine efficiency falls slightly with pump size (0.9116 → 0.9042) because pumping lowers Sandvann levels (lower head) and moves operation along the PQ curve; plant efficiency 0.911 (no pump) vs ≈ 0.878–0.882 with pump; back-calculated pump efficiency ≈ 0.77 instead of the input 0.8 (pp. 41–42, 46).
- (p. 29–30, 39–40) Pumping lowers Sandvann's reservoir level before the spring flood (more flexible use of water); Kvanndalsfoss level fluctuates strongly regardless of pump size. Effect of the pump on turbine operation is largest in low-inflow years and negligible in high-inflow years.
- (p. 42–43) Recovered energy 37.1 GWh from 45 GWh pumped (≈ 82.4 %) for 40 MW, vs a cycle efficiency 0.904 × 0.773 = 0.698 from Eq. (5); required price ratio 1/η_cycle = 1.43 (p. 44).
- (p. 48, A.2) Pumping from lateral reservoirs breaks even energetically when the pump head is ≤ η_t·η_p ≈ 70 % of the turbine head (220.0 m vs 314.8 m nominal).
- (p. 45–46) Results do not establish profitability: no investment, maintenance or downtime costs; Norwegian resource-rent tax (effective 45 %, marginal 67 % in 2022) and the 2022–2023 high-price contribution would cut post-tax earnings.

## Strengths
- Real Norwegian system and a real PHS-relevant question (adding pumping to an existing cascade), using the industry-standard ProdRisk SDDP model.
- Systematic pump-size sweep with a no-pump baseline; reports operational detail (duration curves, efficiencies, reservoir trajectories).
- Useful collection of Norwegian PHS facts and the Kvanndal 2 concession context.

## Weaknesses / limitations
- Revenue-only comparison; no investment cost, NPV or payback, so "most profitable pump size" is not answered (pp. 44–45, 50).
- Prices scaled to the 2022 crisis level (210 EUR/MWh), well above the scenario's own 2030 level; only one price scenario set; no sensitivity analysis (pp. 45, 47).
- Energy market only; 3-hour resolution; no maintenance.
- Pump fixed-speed at constant efficiency; back-calculated pump efficiency inconsistent with input (p. 46).
- Internal inconsistencies: Table 1 shows pump running time *decreasing* with size while p. 43 says larger pumps run longer; 30 MW production printed as "944.44 GWh" (p. 35) though +3.18 % implies ≈ 993.5 GWh; Holmevann levels given as 1048–1058 masl (p. 9) and 948–958 masl (p. 38); Isvann "1295 to 1985 masl" (p. 9) is a typo; "revenue" defined both as net of pumping cost (p. 37) and as sales income "not the profit" (p. 43).
- Literature review is short and almost only SINTEF/HydroCen SDDP reports (pp. 11–15).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review reservoir-sizing-capacity: pump size sweep | 0–40 MW pump, revenue +1.05 % to +2.56 %, net production falls | pp. 27, 35–37, Table 1 p. 34 |
| Lit review modelling-phs-plants: ProdRisk/SDDP applied to PHS retrofit | Model set-up (208 weeks, 56 × 3 h steps, 50 iterations, 30 serial scenarios) | pp. 24–28 |
| Background phs-technology: Norwegian PHS fleet | 10 plants, 1369 MW, 5 TWh, open-loop, seasonal design (secondary, from Pitorac et al. 2020) | pp. 2–3 |
| Background phs-technology: reversible vs ternary units, efficiencies | Ternary 400–600 m head, reversible < 400 m; round-trip 65–80 % Norway (secondary) | pp. 18–21 |
| Background: Kvanndal 2 PHES concession (Lyse, 2024) | Motivation: spill, near-zero/negative prices | pp. 10, 38–39 |
| Model: price ratio needed for pumping | 1/η_cycle (Eq. 8), 1.43 in their case | pp. 23, 44 |
| Model: head correction in SDDP | P = f(Q) h/h₀ with concave f | p. 23, Eq. (9) |
| Discussion: value of pumping is largest in dry years | Duration curves, min-output years | pp. 31–32, 39–40 |

## Useful quotes (with page numbers)
> "However, this thesis does not account for the investment costs associated with implementing a pump, which could significantly impact the analysis of annual revenue." (p. 44)

## Follow-up references to check (backward snowballing)
- [2] Pitorac, Vereide, Lia (2020), Technical review of existing Norwegian pumped storage plants, Energies 13(18):4918 (primary source for the Norwegian PHS fleet facts).
- [32] Otterdal (2024), Konsesjonssøknad for opprusting og utvidelse av Røldal-Suldal kraftverk (NVE) and [30] NVE case page "Kvanndal 2 pumpekraftverk".
- [51] Schäffer & Graabak, Power Price Scenarios (HydroCen) (cf. our `schaffer2022stochastic`, different work).
- [46] Johansen, Brødsjømoen, Pedersen (2023), Analyse av utbygging av ny pumpekraft, NTNU bachelor thesis.
- [33] ProdRisk portal documentation, combined SDP/SDDP algorithm.
- Related SINTEF report on the same system: `rex2024hydropower` (ProdRisk-SHOP simulator, includes eastern RSK).

