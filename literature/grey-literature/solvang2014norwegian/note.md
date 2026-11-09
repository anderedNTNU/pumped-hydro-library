---
bibkey: solvang2014norwegian
bibkey_provisional: true
title: "Norwegian hydropower for large-scale electricity balancing needs: Pilot study of technical, environmental and social challenges"
authors: "Eivind Solvang (lead), Julie Charmasson, Julian Sauterleute, Atle Harby, Ånund Killingtveit, Helene Egeland, Oddgeir Andersen, Audun Ruud, Øystein Aas"
year: 2014
venue: "SINTEF Energy Research report TR A7227 (CEDREN), version 1.0, 14 Feb 2014, project 12X757, unrestricted"
peer_reviewed: false
methods: [heuristics-simulation]
review_sections: [ldes-seasonal-storage, phs-technology, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/solvang2014increasing.pdf
takeaway: "CEDREN pilot study: ~20,000 MW of new balancing capacity (about 10,000 MW with pumping) can be added in Norway using existing reservoirs within current HRWL/LRWL (12 southern sites, 11,200-18,200 MW, <=13-14 cm/h level change); daily simulation of three PHS reservoir pairs shows turbine capacity and lower-reservoir live volume limit balancing provision; fixed-speed pump-turbines cannot control pumping power."
---

# Norwegian hydropower for large-scale balancing (Solvang et al., 2014, SINTEF TR A7227)

_Inbox file was named `solvang2014increasing`; the document is SINTEF/CEDREN report TR A7227 (2014), whose title differs from the 2012 preliminary study it builds on ("Increasing balance power capacity in Norwegian hydroelectric power stations", Solvang, Harby & Killingtveit 2012). **Printed page = PDF page − 2** (PDF 17 = p. 15). 100 pages. Read: chs. 1–3, 5, 7, 8 in full; ch. 4 (societal legitimacy) via its summary in ch. 8; ch. 6 (grid) skimmed._

## Research question / purpose
Pilot study of technical, environmental and social challenges of using Norwegian hydropower as a large-scale "green battery" for balancing wind power in Northern Europe (pp. 7–8): (i) where new capacity/pumping could be built using existing reservoirs; (ii) how pumped-storage balancing would change reservoir water levels and what limits balancing provision; (iii) stakeholder acceptance; (iv) PHS machine technology; (v) grid; (vi) impact on the European system (EMPS).

## Setting
- **System:** southern Norwegian reservoir hydropower; three PHS reservoir-pair cases: **Tonstad** (Nesjen upper 275 Mm³ / Sirdalsvatn lower 56 Mm³), **Rjukan** (Møsvatn 1064 Mm³ / Tinnsjø 204 Mm³), **Holen** (Urarvatn 253 Mm³ / Bossvatn 296 Mm³) (Table 3.3, p. 26).
- **Markets:** no market model in ch. 3 (balancing demand derived from North Sea wind); EMPS market simulation of Europe 2030/2050 in ch. 7.
- **Horizon and resolution:** ch. 3: daily time steps, wind years 2000–2006 (pp. 20, 22); ch. 7: 2030 and 2050 stages.

## Method
- **Site screening (ch. 2, from Solvang, Harby & Killingtveit 2012):** new tunnels and power stations between existing reservoirs/sea, sized so reservoir level change ≤ 13 cm/h (salmon-stranding rule of thumb, Harby et al. 2004), 14 cm/h for Nesjen and Juklavatn (pp. 15–16).
- **Reservoir simulation (ch. 3):** Excel model, daily water transfers between reservoir pair; balancing operation **added on top of observed current operation**; volume–stage curves from 20 years of observations; head-dependent energy equivalent recomputed each step; transfer = min(demand, available/free volume within HRWL/LRWL, turbine capacity) (pp. 20–22). Assumptions: new reversible pump-turbines, efficiency 0.9, share of the 20,000 MW balancing need = installed capacity share (0.07 Tonstad, 0.07 Holen, 0.14 Rjukan) (pp. 22, 25).
- **Balancing demand scenarios (pp. 22–25):** from TradeWind 94.6 GW North Sea offshore wind 2030, hourly 2000–2006 → **7Days-Avg** (deviation of daily wind from 7-day moving average; pumping/generation phases 2–4 days) and **Dev-Avg** (deviation beyond ±25 % of long-term average; phases 1–2 weeks; ~50 % less volume exchanged).
- **EMPS (ch. 7):** one node per country, SUSPLAN/ZEB Blue scenario; Norway pumping 1,572 MW vs 11,572 MW plus +20,000 MW interconnection (pp. 81–82).

## Data / case
- **Table 2.1 main scenario (p. 15): 12 new stations, 11,200 MW**, of which **5 PHS = 5,200 MW**: A2 Tonstad PHS 1,400 MW; B3 Holen PHS 700; B6a Kvilldal PHS 1,400 (Blåsjø upper); C1 Tinnsjø PHS 1,000 (Møsvatn upper); E3 Tysso PHS 700 (Langevatn upper); conventional: B7a Jøsenfjorden 1,400 (Blåsjø), D1 Lysebotn 1,400, E1 Mauranger 400, E2 Oksla 700, F1 Sy-Sima 700, **G1 Aurland 700 (upper Viddalsvatn, 12 cm/h)**, G2 Tyin 700. All conventional except G2 discharge to the sea. (Lower-reservoir column mapping is garbled in the extraction; Aurland G1 likely discharges to Aurlandsfjorden — unverified.)
- **Table 2.2 Scenario 3 (p. 16): 18,200 MW** with ≤ 14 cm/h (e.g. Kvilldal PHS 2,400, Jøsenfjorden 2,400, Tinnsjø PHS 2,000 + 2,400, Lysebotn 1,800; Aurland still 700). Adding northern sites → **20,000 MW** total (p. 17).
- **Wind (Table 1.1, p. 10):** 94.6 GW North Sea; mean 38.7 GW, 339 TWh/yr, CF 0.41; output ≤ 20 % of capacity 76 times/yr, mean 30 h, 2,276 h/yr; ≤ 30 % 91 times/yr, mean 40 h.
- **Construction (pp. 18–19):** 20,000 MW ≈ 2/3 of current Norwegian hydro capacity; 5 × 1,000 MW + 60 × 250 MW plants; 7 years per 250 MW project; 2,000 m³ excavation per MW; ~30,000 man-years.

## Key findings
- (p. 7, 20) Technical potential **20,000 MW of new hydro capacity, about 10,000 MW with pumping**, using existing reservoirs within current regulations, leaving existing operation unchanged.
- (p. 7) The **downstream reservoir often limits generation**; night pumping relieves it and extends generation periods.
- (pp. 42–45) 7Days-Avg: balancing demand met on **71 % (Tonstad), 77 % (Holen), 76 % (Rjukan)** of days; Dev-Avg: 53 %, 53 %, 57 %. Main limits: **turbine capacity** (16–17 % of days in pumping) and **free volume in the lower reservoir** during generation (Tonstad 16 % of days; up to 34 % in Dev-Avg). Doubling the capacity share → 43–47 % (turbine capacity binding) (p. 45).
- (p. 45, 49) Overall the most limiting factor is lower-reservoir volume (HRWL reached because of current operation), then turbine capacity; longer (weekly) balancing cycles make reservoir volumes bind more often.
- (p. 86) Reservoirs are rarely completely filled or emptied in the cases; storage volume not fully used.
- (pp. 29–33, 49) Pumping changes seasonal patterns and adds short-term fluctuations, still below critical rates of change; effects are site-specific (shallow lower reservoirs with ~4 m regulation height are most affected).
- (p. 66) "In Norway, pumped storage power plants have so far only been constructed for seasonal storage."
- (pp. 69–72) PHS technology: reversible Francis pump-turbines dominate in Norway; twin (ternary) systems more efficient and faster switching, used for heads >400–600 m; head loss ~5 % each way; **fixed-speed synchronous machine: "constant load in pump mode (no power control)"** (Table 5.2, p. 71), and for a reversible pump-turbine "the power during pump operation cannot be controlled" (p. 69); adjustable speed (±10 % speed → ±30 % power) enables pumping-power control and reserves (p. 71); full-rated converters limited to ~100 MW, DFIM preferred for large units (pp. 72–73). Round-trip >80 % (p. 65); modern units start in 30 s (p. 65).
- (pp. 82–84) EMPS: +10,000 MW Norwegian capacity/pumping and +20,000 MW interconnection cut European CO₂ by **10 Mt/yr (2030) and 26 Mt/yr (2050)**, but much of this comes from the added transmission, not the hydro; only 11.4 TWh net pumped in 2050 case; GB offshore wind surplus 53.4 → 45.3 TWh.
- (pp. 86–87) Stakeholders support the idea but doubt its realism by 2020; key barriers: grid policy (Statnett mandate), benefit sharing with host municipalities, biodiversity, and **uncertain commercial basis because pumped storage depends on persistent price variation**.

## Strengths
- Concrete, site-level Norwegian figures (MW, reservoirs, level-change rates) widely cited for the "~20 GW" balancing potential.
- Clear identification of physical limits (turbine capacity vs lower-reservoir volume) for PHS balancing.
- Useful compact primer on fixed vs adjustable speed PHS machines.

## Weaknesses / limitations
- Pilot study with simple tools (Excel, daily steps, efficiency 0.9, no economics/prices in ch. 3) (pp. 7, 87).
- Balancing demand derived from wind deviations, not from market prices.
- EMPS results confound hydro and transmission changes (p. 84).
- 2014 assumptions (TradeWind 2030 wind, pre-NordLink/NSL).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.1/2.2: Norway's balancing potential | 20,000 MW new capacity, ~10,000 MW with pumping, existing reservoirs | pp. 7, 17, 20, 85 |
| Background 2.2: Norwegian PHS seasonal only | "only been constructed for seasonal storage" | p. 66 |
| Background 2.2: fixed vs adjustable speed | Fixed speed: no pump power control; adjustable: ±30 % power; DFIM >100 MW | pp. 69–73, Tables 5.2–5.4 |
| Model: discrete pumping for fixed-speed units | Pump power set by pump characteristic at given head | p. 69; Table 5.2 p. 71 |
| Lit. review 5.5: what limits PHS provision | Turbine capacity and lower-reservoir live volume | pp. 41–45, 49, 86 |
| Lit. review 5.5: site list incl. Aurland | 12 sites, Aurland 700 MW conventional (Viddalsvatn) | Tables 2.1–2.2, pp. 15–16 |
| Background: environmental constraint on ramping | ≤13 cm/h level change rule of thumb | pp. 15–16, 22 |
| Background 2.1: wind variability durations | Low-wind events ~30–40 h, 76–91 times/yr | Table 1.1, p. 10 |
| Motivation: commercial uncertainty of PHS | Depends on prices continuing to vary | pp. 86–87 |

## Useful quotes (with page numbers)
> "In Norway, pumped storage power plants have so far only been constructed for seasonal storage." (p. 66)

## Follow-up references to check (backward snowballing)
- Solvang, Harby & Killingtveit (2012), SINTEF TR A7126 (unverified number): "Increasing balance power capacity in Norwegian hydroelectric power stations" — the original site study.
- Graabak & Skjelbred (2012): EMPS analysis of Norwegian balancing for Europe.
- Grøv, Bruland, Nilsen, Panthi & Lu (2011), CEDREN HydroPEAK: resources needed for 20,000 MW.
- Nysveen & Molinas (2012); Hamnaberg (2011): PHS machine configurations.
- Harby et al. (2004): water level ramping and fish stranding.
- Charmasson et al. (2017), CEDREN roadmap (later follow-up; cited in `pitorac2020technical`).

