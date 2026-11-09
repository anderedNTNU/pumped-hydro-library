---
bibkey: sepulveda2021design
bibkey_provisional: true
title: "The design space for long-duration energy storage in decarbonized power systems"
authors: "Sepulveda, Nestor A.; Jenkins, Jesse D.; Edington, Aurora; Mallapragada, Dharik S.; Lester, Richard K."
year: 2021
venue: "Nature Energy 6, 506–516 (doi:10.1038/s41560-021-00796-8)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [ldes-seasonal-storage, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/113_Sepulveda_2021_The_design_space_for_long_duration_energy_storage_in_decarbonized_power_systems.pdf
takeaway: "GenX capacity-expansion LP (8,760 h, 17,920 cases, New England-/Texas-like zero-carbon systems): energy-capacity cost (US$/kWh) and discharge efficiency drive LDES system value; ≤US$20/kWh needed for a 10% cost cut; the most valuable LDES has optimised durations of 100–650 h (days to weeks, not months)."
---

# The design space for LDES (Sepulveda et al., 2021)

_Journal pages 506–516 = PDF pages 1–11 (offset 505). PDF pages 12–14 are Extended Data figures. Supplementary Information (formulation, input tables, Supplementary Figs.) is **not** in this PDF. Table 1 was decoded from the raw (non-layout) text extraction because the layout version scrambles it._

## Research question / purpose
What combinations of LDES cost and efficiency parameters (the "technology design space") make LDES valuable in fully decarbonised power systems: how much do they cut system cost, how much firm low-carbon generation and Li-ion storage do they displace, and what storage duration and charge/discharge power balance are optimal? (p. 507). Five parameters: charge power capacity cost, discharge power capacity cost, energy storage capacity cost, charge efficiency, discharge efficiency.

## Setting
- **System:** two stylised zero-carbon systems, "Northern" (New England / ISO-NE-like weather and demand, 181 TWh, 35.9 GW peak) and "Southern" (Texas / ERCOT-like, 441 TWh, 90.7 GW peak) (Table 2, p. 508). Only VRE (wind, solar PV), one firm low-carbon technology per scenario (nuclear, gas w/CCS or "blue H2" combustion), Li-ion and the generic LDES resource. **No hydropower** and no transmission constraints within each region (p. 515). The authors stress the systems are not realistic models of New England or Texas (p. 514).
- **Markets:** none; central least-cost planning. "System value" = % reduction in annualised system cost when LDES is added (pp. 508, 515).
- **Horizon and resolution:** one future year (2045 cost projections), **8,760 hourly** chronological steps, with "time wrapping" (formulation in Supplementary Note 4, not in this PDF) (p. 515).

## Method
- **Model type:** GenX capacity expansion LP with unit-commitment-style operating constraints (cycling, ramp limits, minimum stable output) and intertemporal storage constraints (p. 515). Investment and operation co-optimised.
- **How uncertainty is represented:** deterministic. Weather sensitivity via alternative "higher VRE" and "lower VRE" capacity-factor years (Scenarios 10–11), each re-optimised separately (p. 511, Extended Data Fig. 2). Cost uncertainty via NREL ATB 2018 low vs mid projections (Scenarios 12–14).
- **Solution method:** LP solved per case; 14 scenarios × 1,280 LDES parameter combinations = **17,920 cases** (pp. 507, 515).
- **Design space grid (p. 514):** charge and discharge power cost 100/300/600/900 US$/kW; energy capacity cost 1/5/10/20/50 US$/kWh; charge efficiency 30/50/70/90%; discharge efficiency 20/40/60/80%.
- **Key modelling choices and assumptions (p. 514):**
  - Energy, charge power and discharge power capacities sized **independently** (three degrees of freedom), even though not all technologies allow this.
  - Energy-to-power ratio bounded **10:1 to 1,000:1**; Li-ion 0.5:1 to 10:1. The 1,000:1 bound binds in only 60 cases (RTE ≤ 36%, US$1/kWh).
  - Efficiencies constant (no dependence on rate or state of charge); no self-discharge, no degradation.
  - 30-year capital recovery, 7.1% nominal WACC; no O&M on charge power and energy capacity.
  - **Duration definition (Eq. 1, p. 515):** d = E·η_d / P_d, i.e. discharge efficiency is included; E/P_d is called the "energy-to-power ratio". RTE = η_c·η_d (Eq. 2). Weighted power cost (Eq. 3) combines charge and discharge power cost by capacity.
  - Only one firm technology per scenario, which the authors admit is "more favourable (less realistic)" for LDES (p. 514).

## Data / case
NREL ATB 2018 (2045 low-cost projection for Scenarios 1–11, mid-cost for 12–14) for VRE and Li-ion (p. 515). High-electrification load for Northern System (Scenarios 7–9, 12–14): peak 36 → 77 GW, max hourly ramp 3.4 → 17.4 GW, plus a strong seasonal heating component (p. 510). Table 1 (p. 507) lists literature cost projections; **pumped hydro: discharge power cost US$600–2,000/kW (includes charging equipment), energy capacity cost US$20+/kWh (range subject to geological/geographic constraints), RTE 70–85%**. Compressed air: US$1–30+/kWh, RTE 42–67%; power-H2-power: US$1–15+/kWh, RTE 18–46%.

## Key findings
- (p. 506, p. 508) **Energy storage capacity cost is the most important parameter**, then discharge efficiency; charge/discharge power cost and charge efficiency are secondary. Regression on 7,680 points: energy cost coefficient −9.94, discharge efficiency +7.30, charge efficiency +3.21, discharge power cost −3.26, charge power cost −2.89 (Table 3, p. 510). Discharge efficiency has about twice the effect of charge efficiency (p. 509).
- (p. 506, p. 507) Energy capacity cost must be **≤ US$20/kWh** to cut system cost by 10%. Max cost reduction ≈ 50% over the full design space, ≈ 40% within "future feasible" regions of known technologies.
- (p. 508) Largest reductions (45–50%) when nuclear is the only firm option; with gas w/CCS or blue H2: 30–35% (full space), 20–25% (geographically constrained technologies, e.g. PHS, CAES), 10–15% (unconstrained technologies). Region matters little (+0.3% Northern vs Southern).
- (p. 509) In the highest-value cases, the **marginal 1% of LDES energy capacity cycles fewer than 10 times a year**, so very low energy cost is needed. LDES spends more hours charging than discharging, so discharge power is more valuable than charge power.
- (pp. 509–510) Northern electrification reduces LDES value (feasible-region maximum for unconstrained technologies drops from 25–35% to 15–20%) because seasonal heating load and ramps raise the value of firm capacity.
- (p. 511) With very low energy cost (US$1/kWh), LDES acts as a **hedge against low-VRE years** (cost in a low-VRE year approaches the base-weather cost).
- (p. 512) Full displacement of gas w/CCS or H2 needs ≈ US$1/kWh, ≈ US$400/kW and RTE ≥ 50%, outside projected feasible ranges. LDES at US$10–50/kWh deploys at < 50 h and competes mainly with Li-ion, which can even increase nuclear capacity by up to 10%.
- (p. 513) LDES does not meaningfully displace Li-ion until weighted power cost ≤ US$800/kW at 70% RTE. Li-ion = "fast burst" resource; LDES substitutes for firm generation. Moving from US$10 to US$1/kWh shifts LDES from multiple full cycles to **a single cycle spanning seasons** (Supplementary Fig. 22).
- (pp. 513–514) **Duration results:** ≈ 100 h at US$10/kWh (energy-to-power ratio up to 300:1 when efficiency is low); ≈ 400 h at US$1/kWh (ratio up to 900:1); up to **≈ 650 h** with northern electrification. "the maximum sustained discharge period required for LDES capacity generally ranges from several days to a few weeks, rather than months or seasonally" (p. 514), although charging and energy use can show seasonal patterns. Abstract: most valuable LDES has duration > 100 h (p. 506); summary: 100–650 h (≈ 4–27 d) (p. 508).
- (p. 514) Optimised power capacities are usually **unbalanced, with more discharge than charge capacity**, except where charge power and energy are both very cheap.
- (p. 515) Limitations: single generic LDES at a time, no transmission constraints, no non-cost criteria.

## Strengths
- Very large, systematic design-space sweep; separates power and energy cost and charge/discharge efficiency, so it shows which parameter matters.
- Clear, quantitative definition of duration including discharge efficiency (Eq. 1) and the distinction between duration and energy-to-power ratio.
- Hourly full-year chronology with co-optimised investment; captures declining marginal value.
- Highly cited Nature Energy reference for LDES cost targets and the > 100 h duration finding.

## Weaknesses / limitations
- Deterministic single-year model with perfect foresight; storage operation is therefore an upper bound on value, and inter-annual storage cannot appear (time wrapping over one year).
- No hydropower in the system, so the role of existing reservoir hydro (Nordic case) is absent; transferability to Norway is limited.
- One firm technology at a time, no transmission (authors note both, pp. 514–515).
- System value ≠ owner's revenue; no market prices.
- Results mostly in Northern System figures; Southern results and the formulation are only in the Supplementary Information (not available here).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.1: LDES definition (days–weeks, ARPA-E 10–100 h) | LDES "sustain electricity production over periods of days or weeks"; ARPA-E DAYS targets 10–100 h, < US$1,000/kW, < US$100/kWh | p. 506 |
| Background 2.1: duration definition | d = E·η_d/P_d; E/P_d = energy-to-power ratio | p. 513, p. 515 Eq. 1 |
| Background 2.1: what durations a decarbonised system values | 100–650 h (≈ 4–27 d); "several days to a few weeks, rather than months" | pp. 506, 508, 513–514 |
| Background 2.1: LDES cost targets | ≤ US$20/kWh for 10% cost cut; ≈ US$1/kWh to displace firm generation | pp. 506–507, 512 |
| Background 2.2: PHS cost and efficiency projection | PHS US$600–2,000/kW, US$20+/kWh, RTE 70–85% (geographically constrained) | Table 1, p. 507 |
| Lit. review 5.5: energy vs power capacity value | Energy capacity cost dominates; discharge power more valuable than charge power; unbalanced charge/discharge capacity optimal | Table 3 p. 510; pp. 509, 514 |
| Lit. review 5.5 / discussion: rarely used marginal storage | Marginal 1% of energy capacity cycles < 10×/yr | p. 509 |
| Discussion: storage as hedge against bad weather years | Low-cost LDES dampens cost of low-VRE years | p. 511, Ext. Data Fig. 2 |
| Discussion: Li-ion vs LDES roles | "fast burst" vs firm substitute | p. 513 |

## Useful quotes (with page numbers)
> "the maximum sustained discharge period required for LDES capacity generally ranges from several days to a few weeks, rather than months or seasonally" (p. 514)

## Follow-up references to check (backward snowballing)
- [1] Sepulveda et al. (2018), role of firm low-carbon resources, Joule 2.
- [9] Guerra et al., value of seasonal energy storage technologies, Energy Environ. Sci.
- [10] Dowling et al. (2020), role of LDES in VRE systems, Joule 4.
- [14] Albertus, Manser & Litzelman (2020), long-duration electricity storage applications, economics and technologies, Joule 4 (> 100 h, < US$40/kWh).
- [15] Ziegler et al. (2019), storage requirements for shaping renewables, Joule 3.
- [13] ARPA-E DAYS programme (grey literature, 10–100 h definition).

