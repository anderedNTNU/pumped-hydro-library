---
bibkey: agneholm2019fcrd
bibkey_provisional: true
title: "FCR-D design of requirements – phase 2"
authors: "Evert Agneholm (DNV GL), Soroush Afkhami Meybodi (Energinet), Mikko Kuivaniemi, Pia Ruokolainen (Fingrid), Jon Nerbø Ødegård (Statnett), Niklas Modig, Robert Eriksson (Svenska kraftnät)"
year: 2019
venue: "ENTSO-E / Nordic TSOs external report, Version 1, 13 January 2019; 82 pp. (hosted by Energinet)"
peer_reviewed: false
methods: []
review_sections: [phs-technology, electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Nordic TSO design study for FCR-D requirements using hydro governor models: qualifiable FCR-D capacity of hydro units depends strongly on water time constant Tw and loading (80 % vs 70 %); energy markets, not reserve markets, set the operating point; Norway meets its FCR-D need easily (Tw 1.2–1.6 s)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/03_Agneholm_2019_FCR_D_design_of_requirements_Phase_2.pdf
---

# FCR-D design of requirements, phase 2 (Agneholm et al., 2019)

**Source file:** `source.pdf` / `source.txt` (copied from the inbox; original `https://energinet.dk/media/ljtfnuru/fcr-d-design-of-requirements-phase-2.pdf`, see `03_Agneholm_2019_KILDEINFO.md`). Printed "Page X of 82" = PDF page. A **design study** feeding the later Nordic FCR requirements (`nordictsos2022`, `ph24_nordic_tsos_fcr_requirements_2025`); its numbers are not the final rules.

## Research question / purpose
Phase 2 of the Nordic "Revision of the Frequency Containment Process" (FCP) project: relax the phase-1 FCR-D requirements so that enough **hydro** capacity qualifies in Finland, set requirements for units that **switch between FCR-N and FCR-D**, and verify the simplified single-machine model against full-scale PSS/E simulations (Sec. 1.1–1.3, pp. 5–6).

## Setting
- **System:** Nordic synchronous area; hydro units in Norway, Sweden, Finland (Denmark has no hydro FCR).
- **Markets:** FCR-D (capacity products); the study is technical, not market design.
- **Horizon and resolution:** second-scale dynamics; dimensioning incident 1 450 MW, nadir ≥ 49.0 Hz (pp. 7–8).

## Method
- **Model type:** single-machine lumped-mass Simulink model of hydro governor + turbine with water time constant Tw, PID governor, droop, backlash (pp. 5, 12–17); 163 200 parameter combinations (Table 3, p. 16: Kp 2–10, Ki 0.05–5 s⁻¹, droop 2–8 %, Tw 1.2–2.2 s, loading Pset 40–80 %); full-scale Nordic PSS/E model for verification (Ch. 4, pp. 57–78).
- **How uncertainty is represented:** n/a (parameter sweeps over system kinetic energy and unit parameters).
- **Key modelling choices and assumptions:** units assumed to operate at **80 % loading** when qualifying (p. 7); performance requirement = power (0.93 pu) + energy condition at a fixed time after a 49.9 → 49.0 Hz ramp (p. 17); capacity estimated from a survey of Nordic hydro units > 10 MVA (~45 GW installed) by Tw class (Table 1, p. 11).

## Data / case
- (Table 1, p. 11) Installed hydro by Tw: Norway mostly Tw ≤ 1.2 s (≈ 21.4 GW) plus 1.21–1.6 s (≈ 6.6 GW); units with Tw > 2.2 s cannot qualify; no capacity qualifies above Tw ≈ 1.8 s at the inertia levels studied (p. 11).
- (Figs. 7–8, pp. 20–21) Norway's national FCR-D obligation in the study: 537 MW.

## Key findings
- (p. 7) **Loading has a significant impact on qualification** because the effective Tw (non-minimum-phase behaviour) varies with loading; lower loading qualifies more capacity. But **"the energy markets (day-ahead and intra-day) have a stronger influence on the operating point than the ancillary services markets"**, so the operating point is not treated as controllable.
- (pp. 19–21, Sec. 2.5.1) **Norway:** comparatively low Tw (1.2–1.6 s); national obligation reached already at low kinetic energy (~100 GWs); Norway and Sweden reach 150–200 % of obligation with the phase-1 requirements.
- (pp. 33–34, Sec. 2.8) Finland needs a design kinetic energy > 300 GWs (80 % loading) or ~220 GWs (70 % loading) to qualify 100 %; Nordic total of 1 450 MW qualifies at ~110 GWs. Relaxing FCR-D raises the need for FFR.
- (p. 54, Sec. 3.3–3.4) Switching governor parameters between FCR-N and FCR-D is acceptable if PID parameters (not droop) change; a unit delivering both must deliver **the sum of FCR-N and FCR-D** at any deviation and operate within the range prequalified for each.
- (p. 78, Sec. 4.5) Full-scale PSS/E results are slightly better than the simplified model, so the simplified model is adequate for requirement design.
- (p. 79, Ch. 5) "It is reasonable to assume that producers will prioritize the delivery of energy and therefore qualification for FCR-D will be based on typical operating ranges of the unit"; reducing Tw would require a larger tunnel area.

## Strengths
- Hydro-specific, quantitative analysis by the TSOs of how plant physics (Tw, loading, governor) limit fast-reserve capability.

## Weaknesses / limitations
- Superseded by the final technical requirements; parameter values are design-stage.
- Control engineering, not economics; Finland-focused.
- Conventional hydro; nothing specific on pumping mode.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where |
|---|---|---|
| Background 2.2/2.4: hydro dominates Nordic FCR | FCR-N and FCR-D mostly delivered by the same hydro units | p. 5 |
| Background 2.4: why FCR is technically demanding for hydro | Water time constant and loading limit qualifiable FCR-D | p. 7; p. 11; p. 79 |
| Modelling assumption: energy markets set the operating point | Quote, p. 7; producers prioritise energy, p. 79 | p. 7; p. 79 |
| Background: Norway's FCR position | Norway qualifies FCR-D easily (Tw 1.2–1.6 s) | pp. 19–21 |
| Background: combined FCR-N + FCR-D delivery | Must deliver the sum; within prequalified ranges | p. 54 |

## Useful quotes (with page numbers)
> "the energy markets (day-ahead and intra-day) have a stronger influence on the operating point than the ancillary services markets" (p. 7)

## Follow-up references to check (backward snowballing)
- Eriksson, Modig, Kuivaniemi (2017), "FCR-D design of requirements" (phase 1).
- Ørum et al. (2017), "Future System Inertia 2".

