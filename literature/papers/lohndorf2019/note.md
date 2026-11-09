---
bibkey: lohndorf2019
title: "Modeling time-dependent randomness in stochastic dual dynamic programming"
authors: "Nils Löhndorf, Alexander Shapiro"
year: 2019
venue: "European Journal of Operational Research 273(2), 650-661"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, uncertainty-modelling, risk-averse-cvar, benders-decomposition]
review_sections: [modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Head-to-head comparison of Markov-chain SDDP (lattice built by optimal quantization, transitions by counting) and time-series SDDP on the Brazilian hydro system: MC-SDDP gives tighter bounds and a slightly better policy, and significantly lower cost on historical data, but its bound is valid only for the discretised problem."
---

# Markov-chain vs time-series SDDP (Löhndorf and Shapiro, 2019)

_Page mapping: PDF page n = journal page 649 + n (journal pp. 650-661). The text extraction drops most Greek letters; where symbols are reconstructed from the equations this is said explicitly._

_Notation in the paper: cost minimisation. "TS-SDDP" = autoregressive model with lagged data in the state; "MC-SDDP" = Markov-chain discretisation (called ADDP in Löhndorf et al. 2013 and Löhndorf and Wozabal 2017) (p. 650)._

## Research question / purpose
- SDDP needs stagewise independence so that cost-to-go functions do not depend on the data process. Many applications have Markovian dependence. Two fixes exist: (i) TS-SDDP, which models the data as an autoregressive process and adds the lagged data as state variables, and (ii) MC-SDDP, which discretises the Markov process into a Markov chain (lattice) using optimal quantization (p. 650).
- Which approach gives the better policy "in practice has not yet been studied". The paper compares them theoretically (lower bounds) and numerically on the Brazilian long-term hydrothermal planning problem (pp. 650-651).

## Setting
- **System:** Brazilian interconnected power system (in 2010: over 200 plants, 109.6 GW, 79.1% hydro; 141 hydro plants). For the long-term model the hydro plants are aggregated into four energy-equivalent reservoirs (EERs): Southeast, South, Northeast, North, plus one transshipment node; transmission arcs with limited capacity; load curtailment penalised by a convex cost (p. 654, Fig. 1 p. 655). Not pumped storage; no individual plants.
- **Markets:** none. Central cost minimisation (thermal generation plus curtailment cost) to meet load (p. 654).
- **Horizon and resolution:** monthly stages. Typical planning horizon is 60 months because of multi-season reservoirs (p. 654), but the experiments use a 120-month horizon as in Shapiro et al. (2013) (p. 655). Historical evaluation reports only the intermediate 12 months of each 120-month run (pp. 658-659).

## Method
- **Model type:** risk-neutral or risk-averse (nested, conditional mean-AV@R) multistage linear stochastic program with random right-hand sides; four reservoir state variables, four random inflows (pp. 651-653, 661).
- **How uncertainty is represented:** monthly inflows into the four EERs, two stochastic models fitted to ONS data 1931-2008 (78 years):
  - *GPAR* (geometric periodic AR(1)): ln b_t = mu_t + Phi_t ln b_{t-1} + eps_t, eps_t ~ N(0, Sigma_t), parameters periodic over 12 months, errors stagewise independent (eq. 4.1, p. 655). Handles positivity and reduces asymmetry, but destroys convexity of the cost-to-go in the state, so it **cannot be used with TS-SDDP**; with MC-SDDP convexity in xi_t is not needed (p. 655).
  - *STCS* (Shapiro-Tekaya-da Costa-Soares): first-order linearisation of the log model, b_t = e^{eps_t} ∘ (a_t + Gamma_t b_{t-1}) (eq. 4.2, p. 655), usable with TS-SDDP.
  - Joint R2: STCS 78.5%, GPAR 78.2% (p. 655, footnote 4). STCS has heavier tails and overestimates long-term mean inflow into SE and S; GPAR deviates less (Figs. 3-4, p. 655).
  - In TS-SDDP the stagewise-independent errors are discretised either by Monte Carlo sampling or by k-means partitioning of the error distribution (p. 656; Table 1 p. 658).
- **Markov-chain construction ("lattice quantization", Sec. 3.1, pp. 653-654):**
  - Goal: minimise the discretisation error, which (following Bally and Pagès 2003) depends on the stagewise Wasserstein distance between the process and its discretisation (p. 653).
  - At each stage t find K_t quantizers (centres) minimising E[min_i ||xi_t - xi_ti||_p^p] (eq. 3.1, p. 653). The cells are the Voronoi partition of the centres (eq. 3.2). For p = 2 each centre equals the conditional mean of its cell, xi_ti = E[xi_t | xi_t in cell i] (p. 653). With p = 2 this is the k-means (sum-of-squares) problem; finding optimal centres is NP-hard (Aloise et al. 2009) (p. 653).
  - Solved by stochastic approximation (Bally and Pagès 2003): draw S random sample paths from the continuous process and, for each sample, move only the nearest centre towards it with step size beta_s (eq. 3.3, p. 654). If sum beta_s = infinity and sum beta_s^2 < infinity, the centres converge to local minimisers of (3.1) (p. 654).
  - Transition probabilities between layers t and t+1 estimated by counting sample transitions between successive cells: p_tij = (number of sample paths in cell i at t and cell j at t+1) / (number in cell i at t) (eq. 3.4, p. 654).
  - Result is a recombining scenario tree (lattice) with K_t nodes per stage; the number of scenarios grows as the product of K_t, but the DP equations stay tractable because cost-to-go depends only on the current node (p. 653).
  - Settings used: K_t = K = 100 nodes per stage, lattice trained with 100,000 simulated inflow scenarios from the fitted model (p. 655). Sensitivity: K from 10 to 1000 (Fig. 6, p. 658).
- **Solution method (Sec. 3.2, p. 654):**
  - TS-SDDP: forward pass with one sampled scenario per iteration (eq. 3.5); AR state transition added as equality constraints; backward pass over m sampled error realisations (eq. 3.9).
  - MC-SDDP: one cost-to-go approximation per lattice node; expected cost-to-go at node i is the transition-weighted sum over successor nodes (eq. 3.8). In the forward pass the sampled continuous realisation is mapped to the **closest node** (eq. 3.7) and that node's cuts are used (eq. 3.6). Backward pass solves at every node of the next stage (eq. 3.10).
  - Policy for continuous sample paths: find the closest lattice scenario and use its cost-to-go approximation (p. 653, citing Bonnans et al. 2012).
  - 1000 iterations, single forward pass per iteration; both methods receive the same forward inflow sequences for pairwise comparison; five independent runs (pp. 655-656). Python, QUASAR software (Löhndorf 2017) (p. 655).
  - Upper bound estimates smoothed by a right-centred moving average (window 100) and, for the aggregate, by fitting a convex monotone decreasing function with a QP (p. 655).
- **Theory on bounds (Sec. 2, pp. 651-653):**
  - Static case: with partition means, Jensen's inequality gives a lower bound (eqs. 2.2-2.4, p. 651); the gap can be made arbitrarily small by a fine enough partition, but the number of cutting planes needed grows exponentially with dimension d (Remark 2.1, p. 651). Risk-averse extension via the dual representation of coherent risk measures (eqs. 2.7-2.8) and for mean-AV@R via the variational form (eqs. 2.9-2.13, p. 652).
  - Multistage, stagewise independent: discretising each stage at conditional means gives a lower bound (eq. 2.18, p. 652).
  - Markovian data: DP equations with cost-to-go Q_t(x_{t-1}, xi_t) depending only on xi_t (eqs. 2.19-2.20, p. 652). For TS the bound (2.18) carries over by discretising the error (p. 653). For MC it is "not clear how to construct a lower bound" for the true problem, because the conditional means of successor cells depend on xi_t (eqs. 2.23-2.24, p. 653). The MC lower bound is valid for the discretised problem only (pp. 653, 654).
  - Footnote 2 (p. 651): with fixed recourse the second-stage value is convex in (B, b) and concave in the cost vector c, i.e. uncertainty in objective coefficients breaks the convexity TS-SDDP needs.
- **Key modelling choices and assumptions:** linear stage problems with uncertainty only in the RHS (inflows); four aggregated EERs (no head effects, no individual plants); risk measure rho_t(Z) = (1 - lambda_t) E[Z] + lambda_t AV@R_alpha_t(Z) (eqs. 2.9 and 2.25, pp. 652-653); same system parameters as Shapiro et al. (2013, Sec. 5) (pp. 654-655). Terminal value: not discussed; end effects handled by the long horizon and evaluating only the intermediate year (pp. 658-659).

## Data / case
- ONS historical inflows 1931-2008, 78 years; partial autocorrelation of de-seasonalised log-inflows remains significant and high (Fig. 2, p. 655-656).
- Fan charts from 1000 simulated paths vs 78 historical paths (Fig. 3); Q-Q plots of annual mean inflows (Fig. 4) (p. 655).
- Historical evaluation: the 78 years are cut into 68 overlapping 120-month windows; the policy after 1000 iterations is run on each; only the cost of the intermediate 12 months is reported ("steady-state cost") to avoid initialization and end-of-horizon bias (pp. 658-659).

## Key findings
- (p. 650, abstract) For this problem the MC-SDDP bounds close faster than TS-SDDP and the MC-SDDP policy dominates the TS-SDDP policy; on real data both method and stochastic-model quality matter; AV@R robustifies against a misspecified stochastic model.
- (p. 651) Earlier work (Shapiro et al. 2013) found TS-SDDP cannot close the bound gap when an appropriate AR model is used.
- (p. 653) TS-SDDP: valid statistical lower bound, but more state variables and only RHS uncertainty; otherwise convexity is destroyed. MC-SDDP: needs only the Markov property, no linearity of the transition, but no valid bound for the true problem.
- (p. 656, Fig. 5) MC-SDDP consistently gives a slightly better policy than TS-SDDP and its lower bound converges faster towards the upper bound. The MC lower bound, although not theoretically valid for the true problem, is closer to the upper bound than the Monte Carlo (TS) lower bound. K-means partitioning of the TS error distribution is only marginally different from Monte Carlo sampling; the Monte Carlo lower bound varies a lot between runs.
- (p. 656) Authors' conjecture: TS-SDDP adds state dimensions that the policy cannot control and that are only sampled at random in forward passes, so they are poorly explored; building the MC lattice in advance ensures a diverse set of inflow states.
- (p. 658, Table 1) Cumulative cost distribution after 1000 iterations (bn $): MC-SDDP dominates the Monte Carlo TS policy at all quantiles (median 238.2 vs 239.5; 0.99-quantile 758.7 vs 766.9). TS with k-means has a heavier upper tail (0.99-quantile 786.5).
- (p. 658, Fig. 6) Increasing MC nodes per stage from 10 to 1000 gives a better policy and a lower bound closer to the upper bound (finer partition, Remark 2.1), but the gap does not close within 1000 iterations.
- (p. 658, Fig. 7) With AV@R (alpha = 0.1, lambda = 0.25; symbols reconstructed) TS-SDDP gives a **higher** lower bound than MC-SDDP for the same number of outcomes; only with K = 1000 nodes is the MC bound higher again. The bound is more sensitive to K and more variable with AV@R; effect on policy quality unknown (no valid upper bound).
- (pp. 659-660, Figs. 8-9; paired t-tests over the 68 historical windows):
  - MC-SDDP gives significantly lower cost than TS-SDDP with STCS inflows (p < 0.001, t = 4.15).
  - MC-SDDP with GPAR gives significantly lower cost than TS-SDDP with STCS (p < 0.01, t = 3.34).
  - AV@R (alpha = 0.1, lambda = 0.05) significantly reduces cost for TS-SDDP with STCS (p < 0.05, t = 2.56).
  - AV@R (alpha = 0.1, lambda = 0.15) does not significantly change cost for MC-SDDP with GPAR (p = 0.52, t = 0.64).
  - MC-SDDP/GPAR without AV@R vs TS-SDDP/STCS with AV@R: no significant difference (p = 0.93, t = -0.09).
- (p. 660, Fig. 10) AV@R increases the energy held in the Southeast reservoir; with AV@R both policies produce nearly the same reservoir trajectories. Introducing AV@R can lower expected cost when the stochastic model is misspecified.
- (p. 661) Conclusions: MC-SDDP gives tighter lower bounds and consistently better policies for STCS; the advantage is largest in early iterations and vanishes as iterations increase. On historical data MC-SDDP is significantly cheaper irrespective of inflow model; GPAR beats STCS because STCS overestimates high inflows.
- (p. 661) Caveats: results are for one low-dimensional problem (4 states, 4 random variables). TS advantage: randomised scenarios allow statistical testing of bounds. MC advantage: broader class of processes, not limited to RHS uncertainty. Moving from stagewise-independent to AR(1) inflows (4 extra state variables) in TS-SDDP increased the computed gap from 4% to about 18%, while the true gap was considerably smaller. In high dimensions the number of MC nodes needed may grow exponentially.
- (p. 661) Future work: extend conditional cost-to-go functions to time-dependent randomness **in the objective function**, "particularly interesting for modeling price uncertainty".

## Strengths
- The cleanest single source comparing MC-SDDP and TS-SDDP on the same problem, with the same forward samples, five repetitions and significance tests.
- Gives a complete, reproducible recipe for building the Markov chain: quantization objective, Voronoi cells, stochastic-approximation algorithm, counting estimator for transitions, nearest-node rule for continuous paths.
- Honest about what the MC bound means (valid only for the discretised problem) and about the limits of generalisation.
- Evaluates policies on historical data with a design that removes start and end effects (intermediate year only), and separates method effects from stochastic-model effects.
- Links risk aversion (AV@R) to robustness against model misspecification with empirical evidence.

## Weaknesses / limitations
- Single, low-dimensional, aggregated case (4 EERs); uncertainty only in inflows (RHS); no prices in the objective, so the setting where MC-SDDP is strictly needed is not tested (stated as future work, p. 661).
- MC lattice is trained on 100k paths simulated from a fitted parametric model, not on raw historical data; sensitivity to the size of the training sample is not studied.
- Gap never closes within 1000 iterations (Figs. 5-6), so "better policy" claims are relative.
- Cost-minimising system planner; no market prices, no pumping, no head effects.
- Greek symbols in AV@R parameters are not readable in our text extraction; check the PDF if exact lambda values are quoted.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDDP needs stagewise independence; many processes are Markovian | Intro statement of the problem and the two remedies | p. 650 |
| Theory: Markov property, cost-to-go depends only on current state | DP equations (2.19)-(2.20) for Markovian data | p. 652 |
| Theory: TS-SDDP (AR model, lagged data as state, RHS only, convexity) | AR(1) reformulation (2.21); pros and cons; GPAR not usable with TS | pp. 652-653, p. 655 |
| Theory: MC-SDDP definition, lattice, transition probabilities | Eq. (2.22), recombining tree, MC approach | p. 653 |
| Theory: MC-SDDP vs TS-SDDP computational trade-off | Extra state variables vs per-node approximations; 4% to 18% gap from 4 AR states | p. 653, p. 661 |
| Theory: lower bound of MC-SDDP valid only for discretised problem | Explicit statements | p. 653, p. 654 (end of Sec. 3.2) |
| Theory: Jensen lower bound from partition means; refinement | Eqs. (2.2)-(2.5), Remark 2.1 (exponential growth with dimension) | p. 651 |
| Theory: uncertainty in objective breaks convexity (concave in c) | Footnote 2 | p. 651 |
| Model: building Markov states by clustering (k-means / optimal quantization, Wasserstein error) | Eqs. (3.1)-(3.2), conditional-mean centres, NP-hardness | p. 653 |
| Model: stochastic-approximation quantization algorithm | Eq. (3.3), step-size conditions | p. 654 |
| Model: transition probabilities by counting transitions | Eq. (3.4) | p. 654 |
| Model: using the policy on continuous / unseen data (nearest node) | Eqs. (3.6)-(3.8); Bonnans et al. 2012 | pp. 653-654 |
| Method: number of Markov states (sensitivity) | K = 10 to 1000; more nodes, better policy, tighter bound | p. 658, Fig. 6; p. 655 (K = 100 default) |
| Method: out-of-sample / historical evaluation design | 68 overlapping 120-month windows, report intermediate 12 months only | pp. 658-659 |
| Method: end-of-horizon effects, longer planning horizon than reported horizon | 120-month horizon, only middle year evaluated to avoid end-of-horizon bias | p. 655, pp. 658-659 |
| Method: paired comparison of policies, significance tests | Same forward samples; t-tests n = 68 | p. 655, pp. 659-660 |
| Method: convergence plots / smoothing upper bound | Moving average (window 100), convex monotone QP fit | p. 655 |
| Theory/Method: risk aversion (AV@R) as robustness to model misspecification | Nested mean-AV@R; historical results; reservoir trajectories | pp. 652-653, 658-660, Fig. 10 |
| Literature review: MC-SDDP applied to hydro scheduling (Brazil) | Case description, 4 EERs, 141 hydro plants, 60-month typical horizon | p. 654 |
| Research gap: price uncertainty in objective not covered | Future work statement | p. 661 |

## Useful quotes (with page numbers)
> "lower bound computed by the MC approach is valid for the MC discretized problem" (p. 653)

(The sentence continues: rather than for the original continuous data problem.)

Other key statements, paraphrased: MC-SDDP allows modelling any parameter as a Markovian process, while TS-SDDP is restricted to linear transitions and RHS uncertainty (p. 650); future work should extend conditional cost-to-go functions to randomness in the objective, especially price uncertainty (p. 661).

## Follow-up references to check (backward snowballing)
- Shapiro, A., Tekaya, W., da Costa, J.P., Soares, M.P. (2013). Risk neutral and risk averse SDDP. EJOR 224(2), 375-391. (Case parameters, STCS model, TS-SDDP gap.)
- Löhndorf, N., Wozabal, D., Minner, S. (2013). Optimizing trading decisions of hydro storage plants using approximate dual dynamic programming. Operations Research 61(4), 810-823. (MC-SDDP/ADDP with prices for a hydro storage plant; very close to our setting.)
- Bonnans, J.F., Cen, Z., Christel, T. (2012). Energy contracts management by stochastic programming techniques. Annals of OR 200, 199-222. (Quantization and nearest-scenario policy.)
- Philpott, A.B., de Matos, V.L. (2012). Dynamic sampling algorithms for multi-stage stochastic programs with risk aversion. EJOR 218(2), 470-483. (Markov-chain SDDP with risk aversion; in bib as `philpott2012`.)
- Bally, V., Pagès, G. (2003). A quantization algorithm for solving multidimensional discrete-time optimal stopping problems. Bernoulli. (Quantization theory and stochastic approximation.)
- Shapiro, A., Dentcheva, D., Ruszczyński, A. (2014). Lectures on Stochastic Programming, 2nd ed., pp. 258-259 (MC-SDDP description).
- Löhndorf, N., Wozabal, D. (2017). Indifference pricing of natural gas storage contracts. Working paper.
- Pereira, M.V.F. (1989). Optimal stochastic operations scheduling of large hydroelectric systems. (TS approach origin.)

