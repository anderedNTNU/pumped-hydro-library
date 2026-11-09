---
bibkey: nordictsos2022
title: "Explanatory document for the amended Nordic synchronous area methodology for additional properties of FCR in accordance with Article 154(2) of Commission Regulation (EU) 2017/1485"
authors: "Nordic TSOs (Energinet, Fingrid, Statnett, Svenska kraftnät)"
year: 2022
venue: "Nordic TSOs explanatory document, dated 27 June 2022 (file name 29.06.2022); 16 pp. + 9-page consultation appendix"
peer_reviewed: false
methods: []
review_sections: [electricity-markets, phs-technology]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Explains the 2022 Nordic FCR requirements: FCR-N full at ±100 mHz with ~63 % in 60 s / 95 % in 3 min; FCR-D 49.9–49.5 Hz with ≥ 86 % in 7.5 s; dynamic vs static FCR-D; LER (< 2 h) energy management; 5-year transition; hydro penstock dynamics may limit qualification."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/Innlimte_referanser_2026-10-29/nordictsos2022.pdf
---

# Explanatory document, Nordic additional FCR properties (Nordic TSOs, 2022)

**Source file:** `source.pdf` / `source.txt` (copied from the inbox; same file as the bib URL on statnett.no). Printed page numbers = PDF pages 1–16 for the main text; the consultation appendix restarts numbering (appendix p. 1–9 = PDF pp. 17–25). Below, "App. p. X (PDF p. Y)".

## Research question / purpose
Explain and justify the third (amended) Nordic methodology for "additional properties of FCR" under SO GL Art. 154(2) (`sogl2017`): new dynamic-performance and stability requirements for FCR-N, FCR-D upwards and FCR-D downwards, rules for limited energy reservoirs (LER), measurement accuracy, and the transition timeline (pp. 2, 5).

## Setting
- **System:** Nordic synchronous area.
- **Markets:** FCR products (FCR-N, FCR-D up, FCR-D down); the document states that the requirements do **not** change how BSPs bid and sell FCR, only the required response (p. 7).
- **Horizon and resolution:** n/a.

## Method
- **Model type / uncertainty / solution method:** n/a (regulatory explanatory document).
- Background work: Nordic project "Revision of the Nordic Frequency Containment Process" 2014–2017, pilot tests autumn/winter 2021/22 with consumption, production and storage, stakeholder workshop March 2022 (pp. 6–7).

## Data / case
n/a.

## Key findings
- (p. 5) Three FCR products: **FCR-N** stabilises frequency within ±100 mHz and must suppress variations with periods of 10 s and slower (emphasis ~70 s); **FCR-D** acts below 49.90 / above 50.10 Hz, fully activated at 49.50 / 50.50 Hz, within 30 s. SO GL's ±500 mHz / 30 s full-activation values apply only to FCR-D, so FCR-N's response is specified as additional properties.
- (p. 5) Previous ("existing") requirement: **FCR-N ≥ 600 MW in the synchronous system** at 50.00 Hz, fully activated at ±0.10 Hz within 2–3 minutes (this is the pre-2022 rule as described in the document).
- (p. 6) Previous FCR-D up/down: 50 % within 5 s, 100 % within 30 s.
- (p. 6) Motivation: lower inertia → faster frequency changes → higher dynamic-performance demands; requirements set to balance system security and functioning FCR markets.
- (p. 7) **Hydro-relevant:** "some hydro power units may struggle due to penstock dynamics limiting the ability to respond quickly without being unstable"; some existing providers will lose capacity or fail to qualify.
- (p. 10, Sec. 6.1.2) **New FCR-N response:** ~**63 % of final value in 60 s and ~95 % in 3 min** for a ±100 mHz step; same for deactivation.
- (pp. 10–11, Sec. 6.2.1–6.2.2) **FCR-D up:** linear activation 49.9–49.5 Hz; for a frequency ramp 49.9 → 49.0 Hz at −0.24 Hz/s, **activated power after 7.5 s ≥ 0.86 × steady-state FCR-D** and an energy condition on the first 7.5 s (≥ 3.2 s × steady-state power, as rendered in the text); static FCR-D: response delay ≤ 2.5 s. FCR-D down mirrors FCR-D up (p. 12).
- (p. 11, Sec. 6.2.3) **Dynamic vs static FCR-D:** dynamic FCR-D must follow frequency variations and damp oscillations; static FCR-D need only not harm damping; a minimum share of dynamic FCR-D is set in the separate dimensioning methodology.
- (pp. 12–13, Sec. 6.4) **LER:** activate as long as the deviation persists unless the reservoir is exhausted; units with **endurance < 2 h of full activation must implement Normal-state (NEM) and Alert-state (AEM) energy management**, reserving extra power and energy for NEM; **FCR-N from LER must be continuously available during the whole contracted period**; FCR-D from LER must restore full capacity within 120 min of allowed recovery start.
- (p. 15, Sec. 8) Transition: TSOs implement after NRA approval and finalised prequalification (≤ 1 year); existing providers get **at most five years from NRA approval** to transition; review within two years.
- (App. pp. 7–8, PDF pp. 23–24, comment 12, Statkraft) Stricter FCR requirements may **narrow the operating window** in which a unit can provide FCR, which limits simultaneous FCR, aFRR and mFRR delivery from the same unit, because offered capacity in the different reserve markets must not overlap in the same MTU. TSOs reply that FCR cannot be provided outside the prequalified operating range.
- (App. pp. 3–4, PDF pp. 19–20, comments 5–6, Skellefteå Kraft) Hydro producer argues the 7.5-s energy requirement penalises hydro units because of the initial reverse power response ("inertia of the water"); TSOs keep the requirement as technology neutral.

## Strengths
- Clear statement of FCR-N / FCR-D performance numbers and the reasoning behind them, plus hydro-producer concerns in the consultation appendix.

## Weaknesses / limitations
- Explanatory document for a 2022 proposal; the binding numbers are in the approved methodology and the technical requirements document (`ph24_nordic_tsos_fcr_requirements_2025`), which should be cited for values.
- FCR is outside our model scope.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where |
|---|---|---|
| Background 2.4: FCR-N purpose and band | ±100 mHz, periods ≥ 10 s, emphasis ~70 s | p. 5; p. 10 |
| Background 2.4: FCR-N response time | ~63 % in 60 s, ~95 % in 3 min | p. 10, Sec. 6.1.2 |
| Background 2.4: FCR-D response | Linear 49.9–49.5 Hz; ≥ 86 % after 7.5 s; full at 30 s per SO GL | pp. 5, 10–11 |
| Background: dynamic vs static FCR-D | Definitions and purpose | p. 11, Sec. 6.2.3 |
| Background: LER rules | < 2 h endurance → NEM/AEM; FCR-N continuously available; 120-min recovery | pp. 12–13, Sec. 6.4 |
| Background 2.2: hydro limitations for fast reserves | Penstock dynamics may limit fast stable response | p. 7; App. pp. 3–4 |
| Model: simultaneous reserve provision from one unit | Offered capacity in FCR/aFRR/mFRR must not overlap per MTU; FCR operating window | App. pp. 7–8 (PDF pp. 23–24) |
| Background: history of FCR requirements | Old FCR-N 600 MW, 2–3 min; old FCR-D 50 %/5 s, 100 %/30 s | pp. 5–6 |

## Useful quotes (with page numbers)
> "some hydro power units may struggle due to penstock dynamics limiting the ability to respond quickly without being unstable" (p. 7)

## Follow-up references to check (backward snowballing)
- Nordic methodology for additional properties of FCR (the approved legal text, Art. 3–10).
- Nordic FCR dimensioning methodology (SO GL Art. 153) and its explanatory document.
- Technical Requirements for FCR Provision in the Nordic Synchronous Area (= `ph24_nordic_tsos_fcr_requirements_2025`).

