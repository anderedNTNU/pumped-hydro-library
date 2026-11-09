# Our SDDP setup vs. Bore & Brensholm

Written 2026-11-09 (Claude, with Anders). The library text of Bore 2026 was checked against the final edition PDF (June 2026): identical. Sources: `theses/texts/bore-brensholm-2025.txt` (project report), `theses/texts/assessing-the-value-of-hydropower-capacity-upgrades.txt` (Bore 2026 master thesis, same authors), our `Sections/06_mathematical_model.tex`.

## The project report (2025) has no SDDP
Deterministic hourly LP over one year with perfect foresight (ch. 6), solved once in Pyomo/Gurobi. "Upper bound" there means the perfect-foresight revenue, not an SDDP bound. SDDP only appears in Bore 2026.

## How Bore 2026 runs SDDP (ch. 5.3, Algorithm 1)
- **Forward paths per iteration:** one. Each iteration samples one path through the Markov chain (3 joint DA-price/inflow states per week, k-means).
- **Backward pass:** one per iteration, from week W-2 to 0, at the visited reservoir level(s). Next week's subproblem is solved for every (current, next) state pair, weighted by P[curr,next] · π_curr, and **one cut is added to all state models of the week**. So the cuts are, as written, not state-dependent (unverified whether the code does the same).
- **Capacity prices:** a level (×0.75/1.00/1.25) is pre-assigned at random per week before training, so they are fixed during training.
- **End of horizon:** terminal constraint s_end = S0 in the last week; no cuts there.
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
