---
bibkey: ph24_nordic_tsos_fcr_requirements_2025
title: "Technical Requirements for Frequency Containment Reserve Provision in the Nordic Synchronous Area"
authors: "Nordic TSOs (Energinet, Fingrid, Statnett, Svenska kraftnät)"
year: 2025
venue: "Nordic TSOs technical requirements, Version 1.1, 28 March 2025 (ENTSO-E template); PDF, 75 pp., via statnett.no"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Formal Nordic FCR prequalification requirements: activation bands (Table 1), max 70 MW per unit (100 MW FCR-N+FCR-D), FCR-D 86 % at 7.5 s, LER = reservoir < 2 h of full activation, and Sec. 3.6: an entity providing several reserves must be able to fully activate all of them at the same time."
---

# Nordic technical requirements for FCR provision (Nordic TSOs, 2025)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04 from the bib URL on statnett.no; listed on `statnett2026b` as "v2025-03-28"). Cover: "Version 1.1, 28 March 2025". Printed page numbers = PDF page numbers. Formulas are garbled in `source.txt` (math fonts); read the PDF for equations.

## Research question / purpose
Specifies the technical requirements, prequalification process, tests, measurement and data requirements for providing FCR-N, FCR-D upwards and FCR-D downwards in the Nordic synchronous area, based on SO GL (p. 6).

## Setting
- **System:** Nordic synchronous area; any technology (generation, load, storage, aggregated).
- **Markets:** FCR-N, FCR-D up, FCR-D down (technical side; market rules are national, e.g. `statnett2026c`).
- **Horizon and resolution:** n/a (dynamic performance in seconds/minutes).

## Method
- **Model type:** n/a. Requirements are expressed as time-domain step/ramp tests and frequency-domain (sine) stability/performance tests.
- **Key modelling choices:** hydro units must document water starting time constant Tw at rated head (p. 10) — relevant for hydro dynamics but not for our energy-scheduling model.

## Data / case
n/a.

## Key findings
- (pp. 7–10, Sec. 2) Prequalification: verification of properties, tests, telemetry; valid 5 years (reassessment). Hydro units document Tw, governor type/settings; storage documents MWh capacity, SoC limits and energy management (p. 10).
- (p. 11, Table 1) Steady-state activation: **FCR-N** 100 % up at f ≤ 49.9 Hz, 100 % down at f ≥ 50.1 Hz; **FCR-D up** 0 % at ≥ 49.9 Hz, 100 % at ≤ 49.5 Hz; **FCR-D down** 0 % at ≤ 50.1 Hz, 100 % at ≥ 50.5 Hz. FCR stays active as long as the deviation persists.
- (p. 11) **Max provision per single point of failure 70 MW up and 70 MW down; when providing FCR-N and FCR-D at the same time, combined max 100 MW up and 100 MW down.** FCR contribution disabled when not procured (footnote: Statnett's mandatory "grunnleveranse" stays active).
- (p. 12, Table 2) List of requirements and tests (steady state, power and energy at 7.5 s, deactivation, stability, performance, linearity, endurance, mode shifting) and test conditions (high/low load × high/low droop).
- (pp. 13–15, Sec. 3.1.1) FCR-N step tests 49.9/50.1 Hz; endurance test 15 min steps for non-LER; reduction factor < 0.9 → fail (p. 15).
- (p. 18, Sec. 3.1.2) **FCR-D Requirement 2: |ΔP(7.5 s)| ≥ 0.86 × steady-state response; Requirement 3: energy in first 7.5 s ≥ 3.2 s × steady-state response**; power must not drop below the 7.5-s value afterwards; waterway oscillations accepted if damped.
- (p. 38, Sec. 3.5) **LER definition: energy reservoir smaller than two hours of continuous full activation of the prequalified FCR capacity.** LER units need NEM/AEM energy management (pp. 40–47); endurance formula uses reservoir max/min thresholds, current level, setpoint and inflow (p. 48, Eqs. 27–28).
- (p. 48, Sec. 3.6) **"An entity providing several reserves (e.g. FCR, FRR, FFR, and LFSM) at the same time shall always activate each of these reserves according to their individual prequalification/specification, and the total power of the entity should reflect the sum of the reserves. The baseline of the entity must allow full activation of all the contracted reserves at the same time."**
- (pp. 48–49, Sec. 3.6.1) FCR-N + FCR-D: activate the sum at any frequency deviation (Figure 22).
- (p. 50, Sec. 3.7) Start/end of provision during a disturbance; FCR-D may ramp down 15 min after scheduled end (over 5 min) if deviation persists. FCR-N changes between MTUs follow the bid for the second MTU.
- (pp. 51–52, Sec. 3.9 Capacity calculation / Figure 25) Maintained capacity calculation subtracts sold FRR and FFR capacity in the relevant direction from the available headroom; Figure 25 shows how capacities of different reserves **add up** when several products are provided. **If headroom is insufficient for all sold capacities, maintained FCR-D capacity is limited first, then FFR, then FCR-N, then FRR** (because FRR and FCR-N can still be fully activated during a disturbance that activates FCR-D/FFR) (p. 52).
- (pp. 58–60, Sec. 4) Measurement accuracy, resolution, sampling; (p. 65, Sec. 6) real-time telemetry and logging.

## Strengths
Formal, harmonised Nordic source; the only primary source for the simultaneous-delivery principle and the LER threshold.

## Weaknesses / limitations
- Very technical (control engineering); FCR-N performance is specified in the frequency domain, so the simple "63 % in 60 s / 95 % in 3 min" statement is **not** in this document (it is on `ph24_statnett_reserve_overview` and in `ph24_entsoe_frequency_control_2024` p. 10).
- Does not cover market rules (deadlines, prices, bid sizes).

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (page/section) |
|---|---|---|
| Background/model: simultaneous deliverability of reserves | Baseline must allow full activation of all contracted reserves at the same time; total power = sum of reserves | p. 48, Sec. 3.6; pp. 51–52, Sec. 3.9, Figure 25 |
| Model: priority if headroom insufficient | FCR-D limited first, then FFR, FCR-N, FRR | p. 52 |
| Background 2.4: activation bands | Table 1 | p. 11 |
| Background: max per unit | 70 MW per product, 100 MW combined | p. 11 |
| Background 2.4: FCR-D speed | 86 % at 7.5 s; energy ≥ 3.2 s × capacity | p. 18, Sec. 3.1.2 |
| Background/model: storage endurance | LER < 2 h full activation; endurance formula with reservoir thresholds and inflow | p. 38, Sec. 3.5; p. 48, Eqs. 27–28 |
| Background: hydro prequalification data | Tw at rated head, governor data | p. 10, Sec. 2.3 |

## Useful quotes (with page numbers)
> "The baseline of the entity must allow full activation of all the contracted reserves at the same time." (p. 48)

## Follow-up references to check (backward snowballing)
- Test Program for Prequalification of FCR (v2025-03-28) and Implementation and Tuning Guideline (linked from `statnett2026b`).
- SO GL art. 154–156.

