---
bibkey: abdelfattah2023optimal
bibkey_provisional: true
title: "Optimal Management of Seasonal Pumped Hydro Storage System for Peak Shaving"
authors: "Abdelfattah, Asmaa I.; Shaaban, Mostafa F.; Osman, Ahmed H.; Ali, Abdelfatah"
year: 2023
venue: "Sustainability 15(15), 11973 (MDPI) (doi:10.3390/su151511973)"
peer_reviewed: true
methods: [deterministic-lp-milp, hydro-production-function]
review_sections: [ldes-seasonal-storage, modelling-phs-plants, reservoir-sizing-capacity]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/02_Sesonglagring_og_systemmodeller/Abdelfattah2023.pdf
takeaway: "Deterministic nonlinear dynamic economic dispatch (GAMS/BARON, DC power flow, IEEE 24-bus, UAE demand) of a small seasonal PHS (1,500 MWh, 210 m head, variable upper-reservoir head, Darcy–Weisbach losses); a year is compressed to four representative 24-h days (96 steps); PHS pumps in winter, empties in summer, cuts cost 2.6–22 MUSD/yr."
---

# Seasonal PHS for peak shaving in the UAE (Abdelfattah et al., 2023)

_Article-numbered paper; page numbers are the article's own pages 1–23 (= PDF pages)._

## Research question / purpose
Develop an energy management system that optimally operates a grid-connected **seasonal** PHS for seasonal peak shaving, and offer a framework for one-year profitability assessment of PHS in regions without PHS tradition (UAE, strong summer air-conditioning peak) (pp. 1, 4). Claimed gap: "a lack of PHS long-term profitability analysis" (p. 4).

## Setting
- **System:** modified **IEEE 24-bus RTS** (12 thermal units, 3,375 MW max output, peak demand ≤ 2,850 MW) with one PHS at bus 19 (p. 14). Demand profile from **Sharjah Electricity, Water and Gas Authority (SEWA)**, UAE (p. 14).
- **PHS:** open-loop; lower reservoir = sea-level natural water source with **fixed level**; upper reservoir = man-made cylindrical tank 210 m above, cross-section 25,510 m², height 90 m; **1,500 MWh** base case (Table 4, p. 19); single reversible Francis pump-turbine; penstock 490 m carbon steel, diameter 2.02 m, 5 m/s design velocity (Table 3, p. 16).
- **Markets:** none; central thermal-cost minimisation (dynamic economic dispatch, DED). No prices, no reserves.
- **Horizon and resolution:** one year, but each ≈ 90-day season is represented by **one average 24-h day** → 4 days × 24 h = **96 time steps** (p. 14). The objective multiplies daily cost by 90 (Eq. 45, p. 12).

## Method
- **Model type:** deterministic **nonlinear** program (quadratic thermal cost curves, head-dependent pump/turbine power) with DC power flow, solved globally with **BARON** in GAMS (pp. 11–13, 16). (Tagged `deterministic-lp-milp` as the closest available tag; it is NLP.)
- **How uncertainty is represented:** none (perfect foresight of seasonal average demand). Authors note decisions depend on "knowing the yearly demand trends from the beginning" (p. 20).
- **PHS physics (pp. 8–10):**
  - Darcy–Weisbach head loss h_L = R·Q² with resistance from friction factor (Eq. 20 approximation of Colebrook) and fittings (K ≈ 10); **resistance estimated once and held constant** (p. 9).
  - Pump: P_mech = η_m·P_el, Q = η_p·P_mech/(ρ g H_pump), H_pump = static head + losses; static head = fixed elevation + previous upper-reservoir level (Eqs. 24–29).
  - Turbine: P = η_t ρ g Q H_net, H_net = static head − losses (Eqs. 31–34).
  - Upper reservoir level: L_t = L_{t−1} + (Q_p − Q_t)Δt/A (Eq. 30).
  - **Constant pump, motor and turbine efficiencies**; head varies with level (variable head is the main head effect).
- **Season linking (pp. 12–13, Eqs. 47–50):** start level of next season = start level + 90 × (end-of-day level − start-of-day level) of the representative day; cyclic over the year (season 4 links back to season 1). This is how seasonal storage is represented with only 96 steps.
- **Power sizing rule (p. 15, Eq. 61, Table 2):** max power = E_max / (daily hours × days). Charging 6 h/day over 270 days (3 seasons), discharging 6 h/day over 90 days (1 season). **My derivation:** 1,500 MWh / (6 h × 90 d) ≈ 2.8 MW turbine and 1,500 / (6 × 270) ≈ 0.9 MW pump, i.e. a very small unit relative to the 2.85 GW system and an energy-to-power ratio of ≈ 540 h (not stated in the paper).

## Data / case
SEWA one-year demand, averaged per hour within each quarter (p. 14). Thermal unit cost coefficients and ramp limits in Table A1 (p. 22). Peak-shaving test: ramp constraints removed and thermal minimum output set to zero (pp. 16–17).

## Key findings
- (pp. 16–17, 19) With 1,500 MWh PHS: thermal production rises 1,791 MWh/yr (valley filling) and falls 1,512 MWh/yr (peak shaving), of which **1,224 MWh/yr from expensive units**; the difference reflects round-trip losses.
- (pp. 19–20) Upper-reservoir trajectory: most pumping in **winter** (lowest demand), level roughly flat in fall and spring, **fully emptied in summer**. With larger charge/discharge power the PHS also cycles **daily on top of the seasonal cycle** (Fig. 12); with smaller power it also charges in fall/spring (Fig. 11).
- (p. 19, Table 5) Operating cost without PHS 7,181 MUSD/yr; reduction 0.98 MUSD/yr (200 MWh), 2.6 MUSD/yr (1,500 MWh); 15,000 MWh value missing in the text extraction but abstract/conclusion give a range up to **22 MUSD/yr** (pp. 1, 20). Larger charge/discharge power at 1,500 MWh: 5.5 MUSD/yr (Table 6).
- (p. 20) Conclusions: trade-off between construction cost of a larger PHS and its benefit; a daily PHS cannot store seasonally; "The larger the size of the upper reservoir, the more storage cycles it can perform"; capacity depends on upper-reservoir volume, head and water availability.
- (p. 2, Table 1 p. 3) Background: PHS efficiency 70–85%, time scale "hours–months"; 1 m³ at 100 m ≈ 0.272 kWh. Closed-loop PHS "typically limited to daily or weekly storage cycles" (p. 4); open-loop more likely seasonal (p. 7). Hydraulic losses typically < 2% of gross head (p. 7).

## Strengths
- Explicit physical PHS model with variable head and pipe friction losses, solved to global optimality.
- Simple, transparent way to represent a seasonal cycle with representative days linked by a ×90 rule.
- Shows that sufficient power capacity lets a seasonal store also do daily cycling (value stacking across time scales).

## Weaknesses / limitations
- Each season compressed to one average day: no within-season variability, no chronology; the ×90 linking assumes identical days, so seasonal value is crudely approximated.
- Deterministic, system-cost view, no prices or markets; seasonal charge/discharge pattern partly imposed by the sizing assumptions (Table 2).
- Constant efficiencies; constant hydraulic resistance; fixed lower reservoir level.
- Tiny PHS relative to the system (my derivation ≈ 3 MW), so results say little about large seasonal PHS.
- Internal inconsistencies (my checks): a cost cut of 2.6 MUSD/yr from shifting ≈ 1.5 GWh/yr implies ≈ 1,700 USD/MWh, far above the Table A1 fuel cost coefficients; operating cost of 7,181 MUSD/yr seems high for a ≈ 2.85 GW system; Table 5 and Table 2 lose values in extraction. Several unrelated references (e.g. Li-ion parameter identification, converters, refs [2]–[6]) are cited for ESS categories. Typo "BHS unit" (p. 12).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.2: open vs closed loop and seasonal capability | Closed-loop typically daily/weekly; open-loop more suited to seasonal | p. 4, Sec. 2.1; p. 7 |
| Background 2.2: binary/ternary/quaternary sets | Configuration definitions | p. 4, Sec. 2.1 |
| Background 2.2: PHS efficiency and energy density | 70–85%; 0.272 kWh per m³ at 100 m; losses < 2% of gross head | pp. 2–3, Table 1; p. 7 |
| Lit. review 5.3: seasonal PHS operation with head and losses | Variable-head NLP, Darcy–Weisbach, BARON | pp. 8–13, Sec. 3.1 |
| Lit. review 5.5: storage size vs benefit | 200 / 1,500 / 15,000 MWh → 0.98 / 2.6 / up to 22 MUSD/yr; bigger power → daily cycling too | pp. 19–20, Tables 5–6, Figs. 10–12 |
| Lit. review 5.6: gap (deterministic, representative days) | 96-step representative-day year, perfect foresight | p. 14, Sec. 3.2.1; p. 20 |

## Useful quotes (with page numbers)
> "a daily PHS plant cannot store energy seasonally" (p. 20)

## Follow-up references to check (backward snowballing)
- [1] Uddin et al. (2018), review of peak load shaving strategies, RSER 82.
- [9] Díaz-González et al. (2012), review of energy storage technologies for wind power, RSER 16.
- [21] ESA, "Surface reservoir pumped hydroelectric storage" (web page) and [22] Hunt, Zakeri, Nascimento & Brandão, "Pumped Hydro Storage (PHS)", in *Storing Energy* (2nd ed.) — sources for the closed- vs open-loop statement (p. 4); the text attributes the definitions to FERC.

