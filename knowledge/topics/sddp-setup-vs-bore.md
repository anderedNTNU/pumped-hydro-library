# Our SDDP setup vs. Bore & Brensholm

Written 2026-11-09 (Claude, with Anders). The library text of Bore 2026 was checked against the final edition PDF (June 2026): identical. Sources: `theses/texts/bore-brensholm-2025.txt` (project report), `theses/texts/assessing-the-value-of-hydropower-capacity-upgrades.txt` (Bore 2026 master thesis, same authors), our `Sections/06_mathematical_model.tex`.

## The project report (2025) has no SDDP
Deterministic hourly LP over one year with perfect foresight (ch. 6), solved once in Pyomo/Gurobi. "Upper bound" there means the perfect-foresight revenue, not an SDDP bound. SDDP only appears in Bore 2026.

## How Bore 2026 runs SDDP (ch. 5.3, Algorithm 1)
- **Forward paths per iteration:** one. Each iteration samples one path through the Markov chain (3 joint DA-price/inflow states per week, k-means).
- **Backward pass:** one per iteration, from week W-2 to 0, at the visited reservoir level(s). Next week's subproblem is solved for every (current, next) state pair, weighted by P[curr,next] · π_curr, and **one cut is added to all state models of the week**. So the cuts are, as written, not state-dependent (unverified whether the code does the same).
- **Capacity prices:** a level (×0.75/1.00/1.25) is pre-assigned at random per week before training, so they are fixed during training.
- **End of horizon:** no terminal value function. Hard constraint s_end = S0 in the last week (eq. 15), no cuts there, "the model does not explicitly value water left" (ch. 7). Feasibility in training via emergency water in the last week at a penalty of 10 mEUR/GWh (eq. 16); removed in simulation, so 4 of 44 years (1981, 1996, 2002, 2010) become infeasible (ch. 9.2). They attribute it to dry years with low last-week inflow.
- **Bounds and convergence:** no UB/LB computed or reported. Fixed 50 iterations, no convergence test; "a convergence criterion was initially tested" without effect on the policy (no details given). Checked instead against the deterministic 2025 model on 2024 data (ch. 9.1), then out-of-sample simulation on historical years (ch. 5.4).
- Extra analysis (ch. 10): a binary Cmin/Cmax constraint is added only in the forward simulation, since binaries break the cuts in training.
- Known weakness they report: marginal water value does not fall near full reservoir, explained by limited exploration of the state space (ch. 9).

## How ours differs (ch. 6 draft as of 2026-11-09)
- Pump + turbine (separate units, both supply reserves) vs. their turbine-only plant.
- DA + reserve-capacity products vs. their DA + ID + aFRR + FCR; no ID in ours.
- Constant head/energy constant vs. their concave PQ curve.
- State-dependent cuts per (week, Markov state), each holding the expectation over successor states (single-cut).
- K forward paths per iteration; UB = first-week value U_n; policy value estimated by L independent simulations (mean ± SE, not a deterministic LB); stop when U_n is within tolerance of the lower confidence limit, or at N_max. Values of K, L, tolerance not yet chosen.
- Extended horizon with zero terminal value vs. their s_end = S0.
- Weekly discounting β; Bore 2026 shows none in the SDDP recursion (unverified).

## Bore 2026: input data and how the Markov states are built (added 2026-11-12, Anders' question)
Source: the master thesis text, ch. 5.1–5.2 (pp. 28–29), 5.4 (p. 33), 8.1–8.2 (pp. 45–46), 8.6 (pp. 51–52); the conference paper `bore2026` p. 3 and p. 6 says the same more briefly.
- **Day-ahead prices:** 44 simulated DA price series for NO2 from THEMA Consulting Group's fundamental market model (Power Market Outlook), calibrated to an expected **2030** system (more renewables and demand, rising CO2 prices, flexible hydrogen, stable gas prices). Each series is one historical weather year run through the 2030 system, so prices are forward-looking but weather-driven (p. 45). Annual averages vary a lot across the 44 years (Fig. 12).
- **Inflow:** historical NO2 inflow 1981–2024 (NVE data, supplied by THEMA), scaled to the plant with the producer's own 2019 and 2024 observations; assumes the local-to-NO2 ratio of those two years holds historically (p. 46). The same weather years drive the price simulations, so each year gives one joint (price, inflow) trajectory and the price–inflow correlation is kept.
- **Clustering (p. 28):** for each week, the 44 joint price–inflow observations are clustered with K-means into **three** clusters; the **median time series** of each cluster (hourly DA profile plus inflow) is the representative input. The clusters come out as high price–low inflow, medium–medium and low price–high inflow (Fig. 10). The thesis does not say whether price and inflow were standardised before clustering, nor which distance was used.
- **Markov chain (p. 29):** transition probabilities between the three clusters of consecutive weeks are the observed transition frequencies in the clustered data. "The Markov chain logic is applied to the inflow process, while preserving its correlation with spot prices."
- **Capacity prices:** not clustered. Synthetic series built from historical 2022–2025 capacity prices (1, 8, 17 and 18 series from those years; 2022 down-weighted for its abnormal aFRR prices), assigned at random to the DA–inflow trajectories, each with three level outcomes ×0.75 / ×1.00 / ×1.25 (pp. 29, 51–52). Justified by Klæboe et al. (2013) and Backe et al. (2023) finding no significant DA–balancing price relation; the thesis lists this as a limitation (pp. 51–52).
- **Within the week:** prices and inflow known once the week starts (ch. 7.1.1, p. 37).
- **Simulation (p. 33):** the 44 historical trajectories are run week by week with the cuts, no Markov chain, a new random seed for the capacity-price assignment, and s_end = S0; so training and evaluation use different draws of the capacity prices but the same 44 weather years.
- **What this means for us:** they have 44 observations per week for 3 states; our data set and number of states should be stated the same way (years of data, states per week, representative series = median or centroid, how capacity prices enter). The price data are proprietary (THEMA), which matters for what we can reuse.

