---
bibkey: hjelmeland2016combined
bibkey_provisional: true
title: "Combined SDDP and simulator model for hydropower scheduling with sales of capacity"
authors: "Martin N. Hjelmeland, Magnus Korpås, Arild Helseth"
year: 2016
venue: "13th International Conference on the European Energy Market (EEM 2016), Porto, pp. 1–5 (doi:10.1109/EEM.2016.7521187)"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, deterministic-lp-milp, heuristics-simulation, hydro-production-function]
review_sections: [market-participation, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Article I of hjelmeland2019phd: cuts from a linear hybrid SDP/SDDP strategy model (day-ahead + weekly FCR-N capacity, 21 steps/week) are re-used in a MIP simulator with minimum generation, binary start-up, one-reservoir-at-a-time operation and a nonconvex PQ curve; on a Norwegian two-station system the LP overestimates capacity profit by 29.2 % while total profit falls only 0.93 %, because the LP runs stations at e.g. 10 MW to sell 10 MW of reserve below a 50 MW technical minimum."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/hjelmeland2016combined.pdf
---

# SDDP strategy model + MIP simulator for reserve sales (Hjelmeland, Korpås & Helseth, 2016)

_Page convention: the IEEE PDF has no printed page numbers; "p. X" = page X of the 5-page paper (= PDF page; proceedings pp. 1–5). The same paper is reprinted as **Article I** in `hjelmeland2019phd`, thesis pp. 81–86 (p. 81 = cover sheet, paper p. X = thesis p. 81 + X). The thesis synthesis summarises it on pp. 48–49 (see `literature/papers/hjelmeland2019phd/note.md`)._

## Research question / purpose
How large is the error of a **linear** SDDP scheduling model when reserve-capacity sales are added, given that spinning reserves interact with nonconvexities (minimum generation, unit commitment, nonconvex power–discharge curve) that an LP cannot represent (abstract, p. 1; p. 2)? Approach: build the profit-to-go function (cuts) with the LP "Strategy Model", then run a MIP "Simulator Model" with the same cuts and the same scenarios, and use the gap as an estimate of the LP approximation error, relevant both for water values handed to short-term models and "conceivably for making investment decisions" (abstract, p. 1).

## Setting
- **System:** a Norwegian hydropower system "under construction in south-west of Norway" (the Lysebotn system of `hjelmeland2016case`), two power stations of **13.8 MW and 400 MW**; station 2 has two operating points depending on which reservoir it draws from (p. 3–4, Fig. 5). No pumping.
- **Markets:** day-ahead energy + weekly primary frequency reserve (PFR) market for FCR-N; FCR-N in summer offers income potential because with high reservoirs, low prices and high inflow producers otherwise either run at maximum to avoid spill or stop (p. 2). Six weekly PFR time blocks; capacity committed for block 1 must be available in the same hours every weekday (time steps 1, 4, 7, 10, 13) (p. 3, Fig. 2).
- **Horizon and resolution:** two-year period of analysis; weekly stochastic stages; **21 time steps per week**, matching the PFR market resolution (pp. 2–3).

## Method
- **Model type:**
  - *Strategy Model* (pp. 2–3): updated version of the hybrid SDP/SDDP model of `helseth2015cooptimizing` [17]. One-stage dispatch LP (1)–(7): max L_t(x_t, u_t, c_t) + α_{t+1}; reservoir balance (2), energy balance with efficiencies (3), power–discharge and power limits including capacity c_t (4), bounds (5)–(7). State x_t = reservoir volumes **and the state of the power station** (on/off, linearly approximated); **linearised start-up costs** as in Warland et al. and Helseth et al. 2013 [19, 20] (p. 3). Objective: income from energy and capacity minus penalties (spill, "tank water", start-up) (p. 2).
  - *Reserve formulation in the Strategy Model* (p. 3): **symmetric** capacity — "for delivering a certain amount of capacity the power station must be able to regulate both up and down an equal amount" — in (4); PFR limited by the turbine governor, i.e. by droop setting and station size, as a bound on c_t in (7). Head variation not modelled ("minor significant impact" for this case, p. 3).
  - *Simulator Model* (p. 3): same system and time resolution, but MIP one-stage problem: binary state variables (unit commitment, minimum generation), **nonconvex power–discharge function**, and **one-reservoir-at-a-time** operation for station 2. Uses the Strategy Model's converged cuts; therefore "a distinct convergence gap is expected", seen as the main drawback but giving a quick evaluation (p. 3).
- **How uncertainty is represented:** weekly inflow from a first-order autoregressive model (can give negative inflow; costly "tank water" ensures relatively complete recourse) (p. 2); day-ahead price discretised into a **Markov chain** of price nodes, SDDP solved per node (p. 3, Fig. 2); **PFR price deterministic** (actual 2013 and 2014 prices), could be stochastic as in `helseth2016` [21] "this would however significantly increase the problem size" (p. 3).
- **Solution method:** SDDP forward/backward passes until convergence, then one simulation pass of the MIP simulator on the Strategy Model's last forward scenarios (pp. 2–4).
- **Key modelling choices and assumptions:** risk-neutral price taker in both markets; authors note PFR volumes are low, so price-taking there is questionable (p. 3).

## Data / case
- Capacity prices: actual 2013–2014 PFR prices; energy prices from a 2013 EMPS simulation, so capacity and energy prices are coupled in time (p. 3).
- 50 forward scenarios (same in simulator), 7 price nodes, 8 inflow samples in the backward pass, 15 Strategy iterations (p. 4).
- Problem size (Table I, p. 3; partly garbled): Strategy one-stage problem ≈ 1 036 variables and 567 constraints; Simulator ≈ 2 233 variables (585 binary) and 2 121 constraints (the thesis, p. 48, summarises this as about 2× the variables and 4× the constraints). Values in the "dispatch problems" row (5 200; 293 600) could not be assigned with confidence (unverified).
- CPU: Strategy 11 h 4 min, Simulator 41 min on a laptop i7-4600U, 16 GB (p. 4).

## Key findings
- (p. 3) Main LP weakness: "in time periods with low power prices and high PFR prices, the model tended to operate the power station at a minimum level. E.g. the power station was operated at 10 MW in order to provide 10 MW of PFR, even though the technical lower limit of the station was 50 MW." The authors restricted the solution space so that selling the maximum PFR requires operation above the minimum generation limit; in the Simulator the issue is removed by binaries. Together with the one-reservoir-at-a-time restriction this "significantly improved the validity of the results" (p. 3).
- (p. 4, Table II) Simulator relative to Strategy: generation −1.0 %, energy profit −0.99 %, **capacity profit −29.18 %**, profit −1.48 %, end value of water +3.26 %, **total profit −0.93 %**.
- (p. 4) The capacity-profit drop "comes as a result of the tightened system description with minimum generation and operating reservoir constraints, and it shows how vital the system description is when considering provision of PFR."
- (p. 4, Fig. 3) Strategy gap fluctuates because of resampling each iteration; Simulator convergence gap 0.68 %.
- (p. 4, Fig. 4) Duration curve: Simulator shifts generation to around 150 MW (good efficiency point of station 2); no generation below the minimum, unlike ~50 MW outputs in the Strategy Model.
- (pp. 4–5) Method does not improve the profit-to-go function, but gives "a rapid benchmark of how far away the linear approximation is from the true value", useful for **investment decisions** when extra markets are included, e.g. Pelton (flat efficiency, cheap reserves) vs Francis (higher peak efficiency, costlier reserves).
- (p. 5) Conclusion: the Strategy Model "overestimated the value of selling capacity by around 29 %. Even though this value is case-specific, it demonstrates the importance of detailed modelling". Further work: better profit-to-go for the simulator; better representation of capacity-market prices and volumes.

## Strengths
- Clean benchmark design: same scenarios, same cuts, only the one-stage problem differs, so the gap isolates the effect of nonconvex detail.
- Concrete, quotable mechanism for reserve overestimation in LP models (10 MW output to sell 10 MW reserve).
- Links the error to investment/turbine-choice questions.

## Weaknesses / limitations
- Simulator uses cuts from a different (convex) problem, so it is not optimal for its own model; the gap mixes policy and model error.
- Single small case, 50 scenarios, 15 iterations; deterministic historical reserve prices; unlimited market depth.
- Head effects not modelled; no pumping.
- Short conference paper: equations generic (matrix form), the exact reserve constraints and the minimum-output restriction are not written out (for that see `helseth2016` eqs. 6, 13 and `hjelmeland2019phd` Eq. 3.1).
- Abstract wording is muddled ("The overall profit loss was reduced by 0.93%"); read Table II instead.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation: LP overestimates reserve revenue | Capacity profit −29.18 %, total −0.93 % (MIP simulator vs LP) | p. 4, Table II; p. 5 conclusion; abstract p. 1 |
| Limitation: mechanism | 10 MW output to sell 10 MW reserve vs 50 MW technical minimum | p. 3, Sec. II-B |
| Model: minimum-output-linked reserve restriction | Selling max PFR requires operation above minimum generation (exact formula in hjelmeland2019phd Eq. 3.1) | p. 3 |
| Model: symmetric reserve, droop/size cap | Qualitative description of (4) and (7) | p. 3, Sec. II-A |
| Model: intra-week resolution | 21 steps/week, 6 PFR blocks | pp. 2–3, Fig. 2 |
| Method: policy evaluation by simulation with same scenarios and cuts | Strategy/Simulator design, Fig. 1 | pp. 2–4 |
| Lit review (sizing): reserve value depends on turbine type | Pelton vs Francis example | pp. 4–5 |
| Lit review (market participation): Norwegian FCR-N summer potential | Qualitative | p. 2 |

## Useful quotes (with page numbers)
> "the power station was operated at 10 MW in order to provide 10 MW of PFR, even though the technical lower limit of the station was 50 MW." (p. 3)

## Follow-up references to check (backward snowballing)
- [14] Abgottspon, Njálsson, Bucher, Andersson (2014), risk-averse medium-term hydro optimisation with spinning reserves, PMAPS (SDDP with local cuts; cf. `abgottspon2014`).
- [12] Cerisola, Latorre, Ramos (2012), SDDP for nonconvex hydrothermal models, EJOR.
- [13] Thomé, Pereira, Granville, Fampa (2013), nonconvexities in SDDP (PSR working paper).
- [19] Warland, Haugstad, Huse (2008), thermal start-up costs in long-term scheduling, PSCC (cf. `warland2016stochastic` for a different Warland paper).
- [17] = `helseth2015cooptimizing`; [21] = `helseth2016`.

