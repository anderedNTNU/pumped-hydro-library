---
bibkey: chazarra2016stochastic
bibkey_provisional: true
title: "Stochastic optimization model for the weekly scheduling of a hydropower system in day-ahead and secondary regulation reserve markets"
authors: "Manuel Chazarra, Javier García-González, Juan I. Pérez-Díaz, Montserrat Arteseros"
year: 2016
venue: "Electric Power Systems Research, 130, 67–77 (doi:10.1016/j.epsr.2015.08.014)"
peer_reviewed: true
methods: [multistage-scenario-trees, deterministic-lp-milp, hydro-production-function]
review_sections: [market-participation, modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/10_Chazarra_2016_Stochastic_optimization_weekly_scheduling_day_ahead_and_secondary_regulation_reserve_markets.pdf"
takeaway: "Weekly hourly stochastic MILP (scenario tree on inflow + DA + reserve prices) for a Spanish cascade with a PHS plant in day-ahead + secondary reserve (aFRR-type) markets; adds linear constraints that keep enough water/storage for an assumed share of reserve activation, which cuts reserve income but makes offers deliverable."
---

# Stochastic weekly scheduling in day-ahead and secondary reserve markets (Chazarra et al., 2016)

PDF page p = journal page 66 + p (article runs pp. 67–77).

## Research question / purpose
How should a price-taking hydro producer with a **cascaded, multi-reservoir system including a pumped-storage plant** schedule hourly generation and secondary regulation reserve (up and down) over one week so as to maximise expected profit in the day-ahead market (EM) and the secondary regulation reserve market (SM), while **protecting itself against water unavailability (up-activation) and storage unavailability (down-activation)** caused by the uncertain real-time use of the committed reserve (abstract p. 67; contributions p. 69). The authors argue that earlier co-optimisation models of energy and reserves ignore whether reserves can actually be delivered once deployed (p. 67, p. 69).

## Setting
- **System:** real-life-style Spanish hydro system with nine nodes: three reservoirs (E1, E2, E3), three natural-inflow points, three plants (C1, C3 with reserve-capable "bg" units; C2 a pumped-storage plant with three units) (Fig. 6, Table 1, pp. 72–73). Upper reservoir of the PHS (E2) is 15 hm³ max / 3 hm³ min (Table 1, p. 72). Pumping units run at a fixed point: 100 MW (G1, G2) and 50 MW (G3) (p. 75).
- **Markets:** Spanish day-ahead market + secondary regulation reserve (capacity) market, i.e. AGC participation (p. 69). Reserve **activation energy is not paid** in the objective (only capacity, eq. 3, p. 69); up/down energy prices are future work (p. 77). The Spanish up/total reserve ratio rule is deliberately **not** imposed "to present a more general case" (p. 74). Pumped-storage units are **excluded** from reserve provision (p. 72), stated as future work (p. 77).
- **Horizon and resolution:** one week (168 hourly periods), 15–21 March 2013 (p. 73). Rolling/daily use intended: first 24 h are here-and-now, remaining 144 h a look-ahead that is updated as forecasts arrive (p. 69, citing Deane et al. 2013).

## Method
- **Model type:** stochastic MILP (deterministic equivalent on a scenario tree), solved in GAMS/CPLEX 12.2 (p. 74). Strategy 3: 56,255 constraints, 39,673 variables (5,928 binary), about 10 min (p. 74).
- **How uncertainty is represented:** scenario tree on **natural inflows, day-ahead prices and secondary reserve prices** (p. 69, p. 73). Case tree: one scenario on day 1, branching to 2 for days 2–4, then each branch to 2 for days 5–7, i.e. **4 equiprobable scenarios** (Fig. 7, p. 73). How the scenarios were generated is not described. Reserve activation is **not** a random variable: it is a fixed conservative parameter (Fup, Fdw) (p. 72). Explicit activation uncertainty is future work (p. 77).
- **Solution method:** direct solution of the extensive form by branch and cut.
- **Key modelling choices and assumptions:**
  - *Topology:* node–arc representation after Chang et al. [8]: reservoirs, plants and inflow points as nodes; discharge and spillage arcs (p. 69). Water balance eq. (4) with **fractional water travel times** between nodes (e.g. 2.2 h: 20 %/80 % split over periods) (p. 70, Fig. 3).
  - *Head dependency:* two power–discharge curves (A, B) per unit, scenario and period, following Conejo et al. [17]; a binary per reservoir selects the curve based on the volume relative to a mid value VM computed from theoretical max/min volumes (eqs. 5–13, pp. 70–71). Triangulation, iterative, NLP and MINLP alternatives rejected for CPU time (p. 70).
  - *Unit commitment:* min up/down time, start-up/shut-down binaries, max manoeuvres per day (eqs. 15–18, p. 71).
  - *Pumped-storage units:* generation as for other units; pumping at a fixed operating point (max flow, max power) when on; no simultaneous pumping and generating in one unit (eqs. 20–24, pp. 71–72).
  - *Environmental and long-term coupling:* time-varying storage limits and min/max release obligations from water authorities (eqs. 25–26) and an **end-of-week target volume** v_{w,n,P} = vf_n "to take into account the results of a longer term scheduling procedure" (eq. 27, p. 72; also p. 69 citing [6]). No water value / future-profit function.
  - *Reserve headroom:* up-reserve ≤ head-dependent max power − generation; down-reserve ≤ generation − head-dependent min power, with an auxiliary variable to keep it linear; zero reserve when off (eqs. 28–31, p. 72).
  - *Core contribution, energy-feasibility of reserves (eqs. 32–33, pp. 72–73):* for every scenario, plant and hour, the water that could have been released so far without violating the tightest minimum-volume limit of the upstream reservoir must cover Fup % of cumulative scheduled up-reserve (converted to water with the **minimum** energy coefficient, a conservative choice); symmetrically, the free storage below the tightest maximum-volume limit must absorb Fdw % of cumulative down-reserve. With Fup = Fdw = 100 % the schedule is robust to full simultaneous deployment of both directions every hour, which the authors admit will "seldom take place" (p. 72).
  - Efficiency loss from operating away from best efficiency to hold reserve is captured through the curves (p. 69, citing Galvis et al. [7]).

## Data / case
- Spanish system, week 15–21 March 2013; three reservoirs, three inflow points, three plants (p. 73). Table 1 (p. 72) gives storage limits (E1 75/5 hm³, E2 15/3 hm³, E3 1000/30 hm³) and plant flow/power limits (partly garbled in the text extraction; verify in the PDF before reusing individual plant values).
- 2013 Spanish system averages of real-time use of secondary reserve: **31.9 % up, 23.7 % down** (p. 76).
- Industrial partner: Endesa's hydraulic management section (acknowledgements, p. 77).

## Key findings
- (p. 74, Table 2 p. 75) Four strategies: (1) EM only, reserves valued ex post; (2) EM + SM without the protection constraints (Fup = Fdw = 0); (2bis) as 2 without head dependency and travel times; (3) full model with Fup = Fdw = 100 %.
- (Table 2, p. 75; € for the week, expected) Total revenue: S1 1,764,203; S2 2,498,784; S2bis 2,440,510; S3 2,202,312. SM revenue: 256,957 / 1,477,216 / 1,441,304 / 947,760. EM revenue: 1,507,246 / 1,021,568 / 999,207 / 1,254,552. EM energy (MWh): 18,070.59 / 16,497.25 / 15,566.25 / 17,626.99. SM reserve (MW summed over hours): 16,055 / 38,617 / 36,939 / 19,972. Income per MWh: 98.87 / 153.68 / 159.56 / 126.63 €/MWh.
- (p. 74) Co-optimising reserves (S2) raises income per MWh about **55 %** over EM-only (S1); S2 earns 13 % more in total and 21 % more per MWh than S3, but S2 is "highly risky" because offered reserve may not be deliverable. S3 shifts volume back to the spot market, partly compensating the reserve loss.
- (p. 75) Ignoring head dependency and travel times (S2bis) loses 58,274 € (S2 is 2.39 % higher), with 931 MWh less spot energy and 1,677.91 MW less reserve: higher head gives both more energy and more reserve headroom.
- (p. 75, Figs. 12–13) The PHS plant pumps in low-price hours and generates in high-price hours (pure arbitrage, since its units hold no reserve).
- (pp. 76–77, Table 3, Fig. 14) Sensitivity on Fup = Fdw ∈ {0, 25, 2013 mean, 50, 75, 100 %}: total revenue falls monotonically 2,498,784 → 2,496,381 → 2,459,601 → 2,385,897 → 2,282,002 → 2,202,312 €; SM revenue falls 1.48 M → 0.95 M €, EM revenue rises 1.02 M → 1.25 M €. More conservative = less income but more reliable reserve commitments.
- (p. 77) Conclusion: joint participation gives "significantly higher expected income" than EM only "with the same consumed water volume", and deliverability can be protected while still keeping most of that gain.

## Strengths
- One of the first hydro scheduling models to make reserve offers **energy-feasible** (water and storage for activation) with simple linear constraints that are easy to transplant into other formulations.
- Joint stochasticity in inflow, spot price and reserve price; realistic topology, travel times and head effects.
- Clear strategy comparison isolating the value of reserves and of the deliverability constraints.

## Weaknesses / limitations
- One week only, one historical case week, and only 4 scenarios; scenario generation not documented.
- Fixed end-of-week target volume: no water values, so the trade-off between reserve participation and long-term storage value is not captured.
- Activation treated as a deterministic worst-case percentage, not as uncertainty; activation energy is not remunerated in the objective.
- The PHS units cannot provide reserve, so the paper says little about PHS reserve provision itself.
- Income per MWh in Table 2 (98.87 €/MWh for S1) differs from the text (97.63 €/MWh, p. 74); the table value is apparently the scenario mean of per-scenario ratios (p. 74 definition), the text value total/energy.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model: reserve headroom constraints | Up ≤ Pmax(head) − gen, down ≤ gen − Pmin(head), zero if off | p. 72, eqs. 28–31 |
| Model: energy-feasibility of reserve offers (water/storage for activation) | Cumulative water and free-storage constraints with Fup/Fdw | pp. 72–73, eqs. 32–33 |
| Model: activation-share parameter and calibration | Fup/Fdw as input; 2013 Spain means 31.9 %/23.7 % | p. 72; p. 76 |
| Model: end-of-horizon coupling via target volume from a longer-term model | Eq. (27) target vf_n | p. 69, p. 72 |
| Lit review (market participation): value of co-optimising reserves for hydro | +55 % income/MWh vs EM only; 13 % lost when protecting deliverability | p. 74, Table 2 p. 75 |
| Lit review (market participation): trade-off reserve vs spot as conservatism rises | Sensitivity table on Fup/Fdw | pp. 76–77, Table 3, Fig. 14 |
| Lit review (modelling PHS): short-term stochastic MILP with scenario trees, head effects and travel times | Formulation and topology | pp. 69–72 |
| Lit review: head effects matter for reserve value | S2 vs S2bis, 2.39 % | p. 75 |
| Lit review (research gap): short-term models need long-term signals | Target volumes from longer-term scheduling; here-and-now day + look-ahead | p. 69, p. 72 |
| Method: scenario-tree structure for weekly scheduling | 1–2–2 branching, 4 equiprobable scenarios | p. 69 (Fig. 2), p. 73 (Fig. 7) |

## Useful quotes (with page numbers)
> "As hydro power is an energy-constrained generation technology, it needs to be protected against any possible deployment of the scheduled reserves." (p. 67, abstract)

> "participating in both markets with the solution of Strategy 2 is highly risky" (p. 74)

## Follow-up references to check (backward snowballing)
- [1] Pérez-Díaz et al. (2015) Trends and challenges in PHS operation, RSER 44 (filed as `perezdiaz2015trends`).
- [3] De Ladurantaye, Gendreau, Potvin (2007) strategic bidding for price-taker hydro producers, IEEE TPWRS 22(4).
- [6] Borghetti et al. (2008) MILP short-term hydro scheduling with head-dependent reservoir, IEEE TPWRS 23(3).
- [10] Deane et al. (2013) intertemporal targets for large PHS (filed as `deane2013derivation`).
- [17] Conejo et al. (2002) self-scheduling of a hydro producer, IEEE TPWRS 17(4) (two-curve head approximation).
- [2] Kazempour et al. (2008) self-scheduling of price-taker hydro in energy and ancillary markets.

