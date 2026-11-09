---
bibkey: schuller2024practical
bibkey_provisional: true
title: "Practical Experiences from Application of a Comprehensive Simulator for Pumped Storage Hydropower Investment Decisions on a Real Investment Case"
authors: "Schüller, Kristine; Aaslid, Per; Vereide, Kaspar; Skjelbred, Hans Ivar"
year: 2024
venue: "2024 20th International Conference on the European Energy Market (EEM), IEEE (doi:10.1109/EEM60825.2024.10608922)"
peer_reviewed: true
methods: [sddp-time-series, deterministic-lp-milp, hydro-production-function, heuristics-simulation]
review_sections: [modelling-phs-plants, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/01_Produsentmodeller_og_tidsskalaer/Schuller2024.pdf
takeaway: "SINTEF ProdRisk–SHOP simulator on Sira-Kvina (Norway): SDDP water-value cuts (weekly, 3 h, aggregated) passed to an hourly detailed SHOP MILP simulation to value a 90 MW pumping plant at Tjørhom; corrected net income +1.9% (STM) vs +2.9% (MTM) over 11 of 30 weather years; detailed short-term limits reduce the investment's value."
---

# ProdRisk–SHOP simulator for a PHS investment at Sira-Kvina (Schüller et al., 2024)

_Author accepted manuscript (NVA, CC BY 4.0), 6 pages. Page numbers below are PDF pages 1–6 of the AAM (proceedings page numbers not shown). Inbox file name "Schuller2024"; first author's surname is Schüller._

## Research question / purpose
Share practical experience from using a combined medium-term (MTM) + short-term (STM) hydropower simulator for a real Norwegian pumped-storage investment decision, and show how detailed short-term physics changes the investment result (p. 1). Stated contributions (p. 2): (a) practical experience running an aggregated MTM with a detailed STM, (b) methods to keep the two model descriptions consistent, (c) numerical investment results.

## Setting
- **System:** Sira-Kvina hydropower system, south-western Norway: two river systems (Sira, Kvina) meeting at **Tonstad** (960 MW, Norway's highest annual production, very small intake reservoirs Ousdalsvann and Homstølvann). 7 plants, 18 turbines, **1,770 MW**, ≈ 6,800 GWh/yr (≈ 5% of Norwegian demand) (p. 2). Existing pumping at **Duge**; investment option = new **90 MW plant with pumping at Tjørhom** with a new outlet tunnel straight to Ousdalsvann (pp. 3–4).
- **Markets:** price-taker in an energy (spot) market; risk neutral (p. 2). No reserves.
- **Horizon and resolution:** MTM: weekly stages, 3-hour resolution, planning horizon typically **104–208 weeks** depending on largest reservoir (p. 2). STM: hourly, deterministic, run week by week over 52 weeks × scenarios; horizon extended from 7 to **10 days** with restart from end of day 7 (p. 3).

## Method
- **Model type:** two-model simulator (Python package, interfaces pyprodrisk and pyshop) (p. 2, Fig. 1).
  - **MTM = ProdRisk**: linear multistage stochastic program solved by **SDDP**, stochastic inflow and price, weekly LP stages; plants aggregated (generators in a plant merged); strategy = water-value cuts per week depending on reservoir storage, inflow and price (p. 2).
  - **STM = SHOP**: deterministic successive MILP / successive LP; individual units with head-dependent turbine and generator efficiency curves, tunnel flows and pressure limits, river and weir flows (p. 2).
- **How uncertainty is represented:** 30 historical weather years 1986–2015 with a 2035 price prognosis from Volue Insight consistent with those weather years (not published) (p. 4). The ProdRisk price model is not described here (see ref. [17]/[3]); "MTM with stochastic price and inflow" (p. 2). Classified as `sddp-time-series` because ProdRisk is not stated to use a Markov chain in this paper (unverified).
- **Solution method / workflow (p. 2):** run MTM → cuts; STM simulates forward sequentially week by week, scenario by scenario, using MTM cuts as end-of-week value; end reservoir of one STM run is the start of the next; 52 × 30 = 1,560 sequential STM runs (p. 4).
- **Key modelling choices and assumptions:**
  - **Consistency methods (p. 3):** hydraulically coupled reservoirs (lakes joined by uncontrolled crests/tunnels) are **one reservoir in the MTM** but separate in the STM, otherwise they get different water values; head–volume relation aggregated automatically.
  - **PQ curves for the MTM (p. 3):** STM optimises each plant at fixed head for a grid of discharge levels; the PQ points are **convexified** (non-convex points removed) and passed to the MTM; same for pumps. Head-dependent discharge capacity is **not** in the MTM, only in the STM (p. 4).
  - **Small reservoirs:** MTM undervalues water in small intake reservoirs because it misses head and pressure effects, so the STM empties them at the end of its horizon; fixed by 10-day overlapping horizons (p. 3).
  - **Bypass costs** penalise unwanted bypass in both models (p. 4).
  - **Robustness (p. 4):** soft constraints with penalty variables ("artificial water" at high cost); MILP tolerance 2,000 €(?) ("2000 C" in text, unit unclear); if no solution in time limit, the time step is doubled (−50% variables) until solved; continuous saving and restart.
  - **End-of-period correction (p. 4):** MTM sets initial levels so a sequential run over all 30 scenarios returns to them; with fewer scenarios, the residual volume difference is valued at the average obtained price and spread over scenarios.

## Data / case
Sira-Kvina topology (Figs. 2–3, pp. 3, 6). 30 weather years 1986–2015; 2035 price prognosis (Volue Insight). Hardware: AMD Threadripper 3990X, up to 4 cases in parallel × 16 cores. **Only 11 of 30 scenarios** were finished in the STM at the time of writing; MTM ≈ 4 h, STM ≈ 3–5 min per weekly case, ≈ 5 days for all 30 scenarios (p. 4).

## Key findings
- (p. 4) Both models show higher net income with the Tjørhom pump investment: corrected net income **+2.9% (MTM, 11 scenarios), +1.9% (STM, 11 scenarios), +3.2% (MTM, all 30)**. Value of the residual water-volume difference as % of net income: STM 1.34% (base) / 0.57% (tjørhom); MTM 0.64% / 0.13%.
- (p. 5, Table I) Table I gives slightly different headline numbers (my reading of the extracted columns: corrected net income STM 2.02%, MTM 3.01%, MTM all 3.16%), so the text and table do not match exactly; Tjørhom plant income ≈ +15% (STM) / +21% (MTM); Tonstad slightly up; bypass lower in the STM. **Column-to-row mapping of Table I is uncertain from the text extraction (unverified).**
- (p. 4) The investment gives "significantly more income at Tjørhom", a slight increase at Tonstad (can sustain high output longer) and less bypass, an extra benefit not in the income figure.
- (p. 5) STM gain is smaller than MTM gain, plausibly because of detailed STM restrictions. Example (Fig. 4, scenarios 8–9): Duge cannot pump when downstream head is below 651/655 masl (licence); with a penalty on bypass the base case risks overflow at Gravatn, which happened to be profitable; the MTM strategy does not see these effects. Authors suggest not penalising bypass but reporting it.
- (p. 5) Consistency between MTM and STM is "adequate", best for the largest reservoirs; goal is not identical results but that the MTM gives a long-term target the STM refines.
- (p. 5) Because the STM formulation differs from the MTM, **global optimality cannot be guaranteed**; the STM still adds information.
- (p. 5) Further work: more extreme price scenarios (higher volatility) may make the STM step more important; trade-off between STM detail/resolution and runtime.

## Strengths
- Real Norwegian PHS investment case by the operator (Sira-Kvina co-author), with the industry-standard ProdRisk/SHOP tools.
- Explicit about the gap between a convex SDDP strategy model and a non-convex detailed operating model, and gives concrete consistency recipes (reservoir aggregation, convexified PQ curves, overlapping horizons, terminal-volume correction).
- Shows quantitatively that short-term physics lowers the estimated value of a pump investment (+1.9% vs +2.9%).

## Weaknesses / limitations
- Short conference paper; only 11 of 30 scenarios simulated; price prognosis not published; one investment option only (no sizing sweep).
- Price model in ProdRisk not described; no reserves or intraday.
- Small income differences (≈ 1–3%) with no confidence intervals; Table I and text figures not fully consistent.
- Results are relative percentages, no absolute NOK/EUR values or investment cost, so no NPV.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.3: SDDP + detailed simulator for PHS | ProdRisk (SDDP, weekly, 3 h) + SHOP (hourly MILP), cuts as water values | pp. 1–2, Sec. II, Fig. 1 |
| Lit. review 5.5: PHS investment valuation in Norway | 90 MW pump plant at Tjørhom, +1.9–3.2% net income | p. 4, Sec. V; Table I p. 5 |
| Method: out-of-sample / forward simulation with SDDP cuts | Sequential weekly STM runs, end state → next start, 52 × scenarios | p. 2, Sec. II |
| Method: terminal water value / residual volume | Residual volume valued at average obtained price | p. 4, Sec. IV-F |
| Method: PQ curves, convexification | STM-generated PQ points, convexified, also for pumps | p. 3, Sec. IV-C |
| Method: aggregating coupled reservoirs | Hydraulically coupled reservoirs as one in MTM | p. 3, Sec. IV-B |
| Discussion/limitations: convex strategy vs non-convex reality | "global optimality can not be guaranteed"; STM < MTM gain | pp. 1, 5 |
| Discussion: horizon length for SDDP | Typically 104–208 weeks depending on largest reservoir | p. 2 |
| Background: price volatility drives short-term limits | Intro: more VRE → volatility → operation near limits | p. 1 |

## Useful quotes (with page numbers)
> "global optimality can not be guaranteed" (p. 5)

## Follow-up references to check (backward snowballing)
- [3] Hagenvik, Mathisen, Helseth & Mo (2022), A comprehensive simulator for hydropower investment decisions, PMAPS — the framework paper.
- [2] Mo & Hågenvik (2020), Applying the ProdRisk-SHOP simulator for investment decisions (HydroCen report).
- [9] Hjelmeland, Korpås & Helseth (2016), Combined SDDP and simulator model with sales of capacity, EEM — reserves + SDDP.
- [13] Mo et al. (2019), Benchmarking hydro operation by use of a simulator.
- [8] Gjelsvik, Belsnes & Haugstad (1999), SDDP under spot price uncertainty (already in references.bib as `gjelsvik1999`).
- [6] Cerisola, Latorre & Ramos (2012), SDDP for non-convex hydrothermal models, EJOR.
- [4] Dorn et al. (2016), minimum pressure height in short-term planning, Energy Procedia.

