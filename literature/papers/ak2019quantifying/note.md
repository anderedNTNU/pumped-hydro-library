---
bibkey: ak2019quantifying
title: "Quantifying the revenue gain of operating a cascade hydropower plant system as a pumped-storage hydropower system"
authors: "Ak, Mümtaz; Kentel, Elcin; Savasaneril, Secil"
year: 2019
venue: "Renewable Energy 139, 739–752"
peer_reviewed: true
methods: [deterministic-lp-milp, hydro-production-function, uncertainty-modelling]
review_sections: [modelling-phs-plants, market-participation, reservoir-sizing-capacity, phs-technology]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Deterministic NLP (monthly decisions, hourly DA prices aggregated into representative-day price-duration functions) shows that converting an existing 3-reservoir Turkish cascade to open-loop PHS raises net revenue by 2.9–10.4% (avg 6.0%); energy market only, no reserves."
---

# Revenue gain of operating a cascade as PHS (Ak et al., 2019)

_Page numbers are journal pages (739–752). PDF page p = journal page 738 + p._

## Research question / purpose
How much additional revenue does a price-taking owner earn by operating an **existing** conventional cascade of hydropower plants (HPP) as a pumped-storage system (PSH), by replacing the turbines of the upstream plants with reversible pump-turbines? The paper builds one optimisation model for both modes (HPP is the special case with pumping set to zero) and compares the maximised revenues (pp. 740–741). Stated contributions (pp. 740–741): (1) a method to quantify the revenue increase from conversion to PSH, (2) a model that produces monthly operating rule curves (end-of-month storage) while accounting for hourly prices within each month, (3) operating insights for the Çoruh cascade.

## Setting
- **System:** open-loop cascade of three existing reservoirs/plants on the Çoruh River, NE Turkey: Arkun (upstream), Yusufeli (middle), Artvin (downstream) (p. 744, Table 1 p. 746). In PSH mode, Arkun and Yusufeli get reversible turbines; water can be pumped from each downstream reservoir to the one above. No pumping into Artvin (most downstream) (pp. 746–747). Both upper and lower reservoirs receive natural inflow, i.e. open-loop PSH (p. 740).
- **Plant data (Table 1, p. 746; columns Arkun / Yusufeli / Artvin):** installed capacity 238 / 540 / 332 MW; design discharge 124.98 / 321.00 / 160.89 m³/s; gross head 225.86 / 208.90 / 116.20 m; net head 222.65 / 199.68 / 107.21 m; maximum storage 283.24 / 2156.68 / 166.80 hm³; active storage 119.59 / 1463.98 / 68.20 hm³; average annual flow 1860.70 / 3684.24 / 3754.32 hm³. _(Column alignment reconstructed from garbled text extraction; Yusufeli's 540 MW and 1464 hm³ are confirmed in the text on p. 747.)_
- **Markets:** day-ahead only. Owner is "a small company who acts as a price-taker"; hourly day-ahead market-clearing prices (Turkey, EPİAŞ) are the selling price and the pumping cost (p. 741). All power is sold to / bought from the grid (p. 741). No intraday, no reserves, no forward market.
- **Horizon and resolution:** planning horizon one year (12 monthly stages) for the rule curve, but the model is solved jointly over **19 years of historical monthly inflows** (1993–2011, 228 monthly values) with the constraint that end-of-month storage is the same in every year (Eq. 13, S_t = S_{t−12}), so one rule curve is derived that is used for "the upcoming year" (pp. 741–743). Decisions are **monthly** (water turbined and pumped per month); hourly prices enter only through aggregated representative price functions (Sec. 3.3, p. 744).

## Method
- **Model type:** deterministic **nonlinear programme** (NLP), maximising average annual energy revenue AAER = (1/n) Σ_i Σ_t [E_t,i · P_t(Tm_t,i) − EPump_t,i · PPump_t(Tmpump_t,i)] (Eq. 1, p. 742). Implemented in GAMS 24.2.3, solved with **CONOPT**, about 60 CPU [seconds] per run (pp. 745–746).
- **How uncertainty is represented:**
  - *Inflow:* not stochastic optimisation. All 19 historical inflow years are included in one deterministic model with a common (non-adaptive) rule curve, so the curve must work for all past years; the authors say inflow stochasticity is "incorporated implicitly" (p. 741). In our terms: a sample-average, open-loop policy over 19 inflow years.
  - *Price:* "scenario-based approach": each historical price year 2013–2017 is a separate scenario, and the model is solved separately for each (deterministic per scenario), giving a range of revenue gains (pp. 740–741, 746). In total 10 models: 5 price years × {HPP, PSH} (p. 746).
- **Within-month price representation (Variable Price Method, VPM, Sec. 3.3, p. 744):** for each month a representative 24-h day is built by averaging prices hour by hour. Water turbined in a month is spread in equal daily amounts and generated in the x highest-price hours of the representative day; pumping happens in the x lowest-price hours. P_t(x) = average of the x highest hourly prices, PPump_t(x) = average of the x lowest, for x = 1..24; a second-degree polynomial is fitted so that non-integer daily durations are allowed (Eqs. 14a–b, p. 744; Figs. 2–3). Daily turbining hours Tm = monthly turbined volume / (30 · discharge) (Eq. 5a, p. 742–743), and turbining + pumping hours ≤ 24 per day (Eq. 6).
- **Key modelling choices and assumptions:**
  - **Head effects, explicit:** gross head from a second-degree head–volume polynomial of the *average* storage of the month, minus constant tailwater (Eq. 4; Figs. 5–7, pp. 745–746); head loss h_loss(q) quadratic in discharge with tunnel and penstock coefficients and diameters (p. 743); turbine efficiency as a function of q/Q_design from a Francis-turbine curve, **same efficiency curve used for pumping** (p. 743).
  - Energy generated E = (H − h_loss(Q)) · Q · 30 · Tm · μ(Q/Qd) · γ, converted to kWh (Eq. 2); pumping energy uses net head and divides by efficiency (Eq. 3) (pp. 742–743).
  - Water balance with upstream outflow as inflow to the next plant, pumped water as negative/positive flows (Eqs. 7–8); storage bounds (Eq. 9); minimum environmental release (Eq. 10); discharge between Q_min and design discharge for both turbining and pumping (Eq. 12); **initial = final storage**, with initial storage at maximum (Eq. 11, p. 743).
  - Simplifications stated in the conclusion (p. 751): fixed environmental flows; evaporation and precipitation neglected; constant tailwater elevations; all generated electricity is sold.
  - End-of-horizon value: none; handled by cyclic storage (Eq. 11) and the periodic rule-curve constraint (Eq. 13).

## Data / case
- Monthly inflows 1993–2011 from two streamgauges, from the State Hydraulic Works of Turkey (DSİ) (pp. 744, 751).
- Hourly day-ahead prices 2013–2017 from EPİAŞ (Energy Markets Management Inc., Turkey), in TL (pp. 744, 748, 751; Fig. 10).
- Reservoir topography gives head–volume curves (Sec. 4.1, pp. 745–746).

## Key findings
- (p. 746) Turbining revenue rises 22.7–31.9% when the cascade runs as PSH, but net of pumping cost the gain is **2.9–10.4%, average 6.0%** (Table 2, p. 747). Net revenue: HPP average 620.70 M TL/yr vs PSH 657.81 M TL/yr; pumping cost averages 134.78 M TL/yr.
- (p. 747, Table 2) Per price year, net gain: 2013 5.9%, 2014 2.9%, 2015 8.1%, 2016 10.4%, 2017 3.1%.
- (pp. 746–747) Yusufeli (middle, 540 MW, 1464 hm³ active) contributes most of the gain; Artvin's net revenue falls under PSH because nothing is pumped into it.
- (p. 748) Price variability drives the gain: 2016 had the largest intra-day variation and the largest gain, 2014 the smallest; the relation between price range and gain is not one-to-one (month-to-month changes, head also matter).
- (p. 748) Investment check: reversible-turbine electromechanical cost from a regression in installed capacity and net head (Eq. 15); ≈ 20% more than conventional turbines; extra investment ≈ 23.5 M€; with 8.96% rate and 50-year life, CRF ≈ 0.09, annuity ≈ 2.11 M€/yr vs annual gain ≈ 12.04 M€/yr → conversion is feasible.
- (p. 748) The authors expect gains to grow with more wind in the Turkish system, because low-demand/high-wind prices fall (stated as an expectation, not modelled).
- (pp. 749–750) Rule curves: Artvin kept at maximum level all year (small active storage, head matters most). Arkun and Yusufeli draw down in Feb–Apr ahead of May–June high inflows, stay full May–July, and draw down for high-price months (Aug, Nov, Dec).
- (p. 750) **Monthly (long-term) decisions barely change between HPP and PSH; what changes is the hour-of-day allocation (short-term decisions).** PSH rule curves lie slightly above HPP ones.
- (p. 750) Machine utilisation: Arkun 43.5% (HPP) → 71.2% (57% turbining + 14.2% pumping); Yusufeli 40.3% → 77.8% (58.7% + 19.1%). Gross generation rises (Arkun 758.1 → 934.7 GWh/yr, Yusufeli 1794 → 2451.6 GWh/yr), but total **net** energy falls 5.2% (3592.2 → 3403.6 GWh/yr) (pp. 750–751).
- (p. 751) Average extra revenue ≈ 37 M TL/yr (≈ 12.0 M€), range 18.67–64.22 M TL across price years.

## Strengths
- Explicit nonlinear head–volume, head-loss and efficiency modelling for a real multi-reservoir cascade.
- Clean comparison design: the HPP model is the PSH model with pumping forced to zero, both optimised, so the comparison is "fair" (p. 740).
- Simple and reusable idea for representing hourly price shape inside a long stage (price-duration curve of a representative day), which is the same problem we face with weekly stages.
- Uses several price years to show sensitivity of the PHS value to price variability.

## Weaknesses / limitations
- No real stochastic optimisation: one non-adaptive rule curve for all inflow years; prices are perfect-foresight within each historical year. Revenue is therefore an in-sample upper estimate; no out-of-sample evaluation.
- Monthly decisions with a representative day lose intra-month price dynamics, day-to-day storage limits and the chronology of pumping and generation (equal daily amounts, same hours every day). The "hours of the day" allocation is implied by the price functions, not scheduled.
- Same efficiency curve for pumping and turbining; constant tailwater; environmental flows fixed.
- Energy market only; no reserves, intraday or forward.
- Investment check is a back-of-the-envelope annuity, not an optimisation of pump or turbine size.
- Minor: ref. [6] Löhndorf, Wozabal & Minner is listed as Oper. Res. 61(4) (2017); that paper is from 2013. Conclusion mixes "$" and "€" (p. 751).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.3/5.4: owner-perspective PHS operation with DA prices only | Price-taker owner, hourly DA prices, no reserves | p. 741, Sec. 3 |
| Lit. review 5.5: value of adding pumping to existing plants | +2.9–10.4% net revenue (avg 6.0%); turbining revenue +22.7–31.9% | p. 739 (abstract), p. 746, Table 2 p. 747 |
| Lit. review 5.5: investment/feasibility of conversion | Reversible turbine cost regression; +20% vs conventional; annuity 2.11 M€ vs gain 12.04 M€ | p. 748, Eq. 15 |
| Model: representing hourly price shape inside a long stage | Variable Price Method: representative day, average of x highest/lowest hourly prices, polynomial fit | p. 744, Sec. 3.3, Eqs. 14a–b, Figs. 2–3 |
| Model: head effects / production function | Head–volume polynomial on average storage; quadratic head loss; efficiency vs q/Q_design (Francis curve) used for both modes | pp. 742–743, Eqs. 2–4; Figs. 5–7 |
| Model: cyclic end-of-horizon condition | Initial = final storage, start at maximum | p. 743, Eq. 11 |
| Discussion: pumping changes hourly dispatch more than seasonal allocation | Rule curves almost identical for HPP and PSH | p. 750, Sec. 5.2; p. 751 |
| Discussion: PHS value depends on price variability across years | 2016 largest spread → largest gain; 2014 smallest | p. 748, Fig. 10 |
| Background 2.2: PHS facts | PHS ≈ 99% of storage capacity; 15–25% round-trip losses; open-loop definition; reversible turbine modes | pp. 739–740 |
| Background: net energy consumer | PSH lowers total net generation by 5.2% | pp. 750–751 |

## Useful quotes (with page numbers)
> "the long-term decision of monthly discharges is not much affected by the system being a HPP or PSH" (p. 741)

_Further key statements are paraphrased with page numbers under Key findings._

## Follow-up references to check (backward snowballing)
- [23] Pritchard, Philpott & Neame (2005), Hydroelectric reservoir optimization in a pool market, Math. Program. — representing price variability within a long stage; relevant to our weekly stages.
- [21] Fleten et al. (2011), Bidding hydropower generation: integrating short- and long-term scheduling, PSCC.
- [20] Pérez-Díaz et al. (2015), Trends and challenges in the operation of pumped-storage hydropower plants, RSER 44 — review.
- [12] Connolly et al. (2011), Practical operation strategies for PHES utilising price arbitrage, Energy Policy.
- [13] Wilson et al. (2018), Storage revenues from time-shifting in Germany and GB 2010–2016, J. Energy Storage — year-to-year revenue variability.
- [25] Bozorg-Haddad et al. (2014), design-operation of pumped-storage and hydropower systems, J. Energy Eng.
- [16] Tica et al. (2017), annual performance of a multireservoir system incl. PSH, J. Energy Eng.
- [37], [38] Chazarra et al. (2016, 2017): weekly scheduling in DA and secondary reserve markets; joint energy and aFRR scheduling of variable-speed PSH — relevant to our reserve modelling.
- [7] Gimeno-Gutiérrez & Lacal-Arántegui (2013), JRC assessment of European PHS potential using existing reservoirs.

