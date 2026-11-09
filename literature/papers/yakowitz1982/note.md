---
bibkey: yakowitz1982
title: "Dynamic Programming Applications in Water Resources"
authors: "Sidney Yakowitz"
year: 1982
venue: "Water Resources Research, 18(4), 673-696"
peer_reviewed: true
methods: [dynamic-programming, sdp, uncertainty-modelling, heuristics-simulation, deterministic-lp-milp, risk-averse-cvar]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Classic survey of deterministic and stochastic DP in water resources (reservoir operation, irrigation, project sizing). Standard source for the OCP/SDP formulation (pp. 674-675), the curse of dimensionality under discretisation (pp. 674, 688, 691), Markov vs independent inflow states (p. 685) and discretisation errors (p. 692). Predates SDDP; no electricity markets or pumped storage."
---

# DP applications in water resources (Yakowitz, 1982)

## Research question / purpose
A survey of dynamic programming (DP) **models** for water-resource problems and of the **computational techniques** used to solve them (abstract, p. 673). Problem areas: aqueduct design, irrigation control, project development (sizing, timing, sequencing), water-quality maintenance and reservoir operation. The author tries to separate successful applications from open problems and offers "speculative ideas" for problems not yet solved satisfactorily (p. 673). A recurring theme is that computational considerations "impose severe limitation on the scale" of DP problems that can be solved (abstract, p. 673), and that the influence of DP on water-resource practice is still "modest" (p. 673).

Structure (contents list, p. 673): §1 introduction (p. 673); §2 notation and preliminaries (pp. 673–675); §3 hydrologic models: water quality, project development, irrigation, other applications (pp. 675–682); §4 reservoir operations, deterministic (pp. 682–685) and stochastic (pp. 685–688); §5 computational aspects, deterministic (pp. 688–691) and stochastic (pp. 691–694); §6 list of symbols (p. 694); references (pp. 694–696).

## Setting
- **System:** generic water-resource systems. Reservoir studies range from a single reservoir (Little 1955, Grand Coulee; Young 1967) to multireservoir systems (four-reservoir benchmark of Heidari et al. 1971; 10-reservoir case of Murray and Yakowitz 1979; six reservoirs in California, Trott and Yeh 1973; Central Valley Project, Becker and Yeh 1974b) (pp. 683–684). **No pumped storage.** Hydropower appears as one reservoir purpose among water supply, irrigation, flood control and recreation.
- **Markets:** none in the modern sense. The closest is Hall et al. (1968), whose loss function uses "scheduled unit prices" of released water and of power supplied in **peak and nonpeak hours**, Eq. (33), applied to Shasta Dam (p. 683). Most hydropower objectives are meeting a power demand at minimum cost (Little 1955; Gessford and Karlin 1958) (pp. 685–686).
- **Horizon and resolution:** varies by study. Examples: Little (1955) uses N = 26 stages of 2 weeks (one year) (p. 685); Buras (1972) uses monthly stages (p. 681); Bogle and O'Sullivan (1979b) use annual stages (p. 677). Infinite-horizon discounted problems with stationary strategies are also covered (pp. 679, 686, 693).

## Method
- **Model type:** a literature survey. It casts every application in one common framework, the **(stochastic) optimal control problem (OCP)** (pp. 673–675):
  - Deterministic OCP: dynamics x_{t+1} = f_t(x_t, u_t) (Eq. 1), additive objective J(u) = Σ_t L_t(x_t, u_t) (Eq. 2), state–stage constraints g_t(x_t, u_t) (Eq. 3), backward functional equation V_t(x) = min_u [L_t(x,u) + V_{t+1}(f_t(x,u))] with V_{N+1} = 0 (Eq. 4), and the optimal policy built forwards from the minimisers (Eq. 5) (p. 674).
  - Stochastic OCP: the dynamics are replaced by a **probabilistic transition function P_t(y; x, u)**, the density of the next state given state x and control u at stage t. The single-stage loss may depend on the successor state, L_t(x_t, x_{t+1}, u_t). A **strategy** S is a sequence of functions u_t = S_t(x). The objective is the expectation J(S) = E[Σ_t L_t(X_t, X_{t+1}, S_t(X_t))] (Eq. 7). The functional equation becomes V_t(x) = min_u ∫ [L_t(x,y,u) + V_{t+1}(y)] p_t(y | x, u) dy (Eq. 8), and with a discretised state space a sum over a probability mass function (Eq. 9) (pp. 674–675).
  - "Discrete dynamic programming" (DDP, after Bellman and Dreyfus 1962): discretise state and control into finite grids and solve the functional equation at grid nodes (Eq. 6). Interpolation is needed because f_t(x(i), u(j)) need not land on a grid node, and errors "thereby arise" (p. 674).
  - The stage index need not be time. In §3 it indexes river positions, number of completed projects, etc., so "dynamic" is "somewhat of a misnomer" (p. 674).
- **How uncertainty is represented (in the surveyed studies):** deterministic expected or historical flows (pp. 675, 682); independent inflows, so the state is storage only (Gessford and Karlin 1958; Askew; Arunkumar) (pp. 685, 687, 692); **lag-1 Markov inflows**, so the state is (storage, previous inflow) (Little 1955; Butcher 1971; Su and Deininger 1974) (pp. 685–686); finite Markov chains for storage (Bogle and O'Sullivan 1979b, p. 677; Doran 1975, p. 692); Brownian-motion inflow in continuous time (Chernoff and Petkau 1978, p. 693).
- **Solution methods surveyed:** DDP; forward DP (Eq. 35, p. 683); minimax DP (Eqs. 36–37, p. 684); LP embedded inside DP (Becker and Yeh 1974b, p. 684); LP formulation of finite-state stochastic OCPs with randomised strategies (Gablinger and Loucks 1970, Eqs. 47–50, pp. 686–687); Lagrangian duality for chance-constrained SDP (Rossman 1977, Eqs. 55–57, pp. 687–688); discrete differential DP (DDDP), state incremental DP (IDP) and differential DP (DIFF DP) (pp. 689–691); Howard's policy iteration (p. 693); parametric approximation of the return function (Gal 1979, p. 692); structural (analytic) results on optimal policy shapes (pp. 685–686, 692); controlled diffusion (pp. 693–694).
- **Key modelling choices discussed:** mass balance with spill folded in as x_{t+1} = min{C, x_t + i_t − u_t} (Eq. 32, p. 682; Eq. 44, p. 685); multireservoir mass balance with an upstream-release index set K(j) (Eq. 34, p. 683); loss depending on state as well as release, which costs nothing computationally and allows flood and recreation desiderata (p. 683); seasonality through time-dependent Markov transition probabilities (Su and Deininger 1974, p. 686); stationarity of optimal strategies for long horizons (pp. 679, 681, 686).

## Data / case
None of its own. It is a survey of about 21 pages of text (pp. 673–694) plus references (pp. 694–696), with six summary tables of applications (Tables 1–6: pp. 675, 678, 680, 682, 684, 688). Case data mentioned in the surveyed studies include: Grand Coulee on the Columbia River, with transition matrix inferred from 39 years of historical flows (Little 1955, p. 685); Lake Superior (Su and Deininger 1974, p. 686); Lake Vyrnwy, Wales (Schweig and Cole 1968, p. 687); Shasta Dam (Hall et al. 1968, p. 683); the Central Valley Project, Shasta–Trinity subsystem (Becker and Yeh 1974b; Becker et al. 1976, p. 684).

## Key findings
- (p. 673) Water-resource problems "serve as an excellent impetus and laboratory" for DP development. Water allocation problems by Warren Hall appear in Bellman (1957, p. 144), and a reservoir problem is central to Larson's (1968) state increment DP.
- (p. 674) **Curse of dimensionality:** with 10 discretisation levels per state coordinate and 12 state variables, DDP needs 10^12 nodes, "an impossibly large number". The practical domain of DDP is "restricted to problems having at most four or five state and control variables". Yakowitz argues that extending this limit to *all* DP is unwarranted: large problems need a combination of analytic, nonlinear-programming and numerical-analysis ideas.
- (p. 674) Stochastic OCP: the transition function P_t(y; x, u) "is presumed to specify the probability distribution" of the next state, given the state x and control u at stage t.
- (p. 675) In the stochastic case, "discrete dynamic programming remains the only approach of any universality". Finding optimal strategies for realistic stochastic OCPs will require "considerable effort and analytic prowess".
- (pp. 676–677) **Design by nested optimisation:** Trott and Yeh (1973) size reservoirs by solving the optimal operating policy for a fixed capacity vector, then adjusting the capacities by nonlinear programming to maximise net annual benefits. Dudley and Burt (1973) do the same for reservoir capacity, irrigated acreage and distribution capacity (p. 679).
- (pp. 677–678) Bogle and O'Sullivan (1979b) model reservoir storage as a finite Markov chain. Their two-dimensional stochastic OCP was "too complex" for DDP, so they used a heuristic.
- (p. 679) If optimal strategies are stationary, the state process is a Markov chain, and the long-run expected loss of any stationary strategy can be found by solving a linear equation for the asymptotic state probabilities (Dudley and Burt 1973).
- (p. 682) The earliest stochastic DP algorithms in reservoir operation (Massé 1946; Little 1955) precede deterministic DP applications by over a decade.
- (p. 682) Two justifications for deterministic inflows: some rivers are regular enough that expectations represent them well, or the historical record gives retrospective insight into what would have been optimal. Young (1967) used a heuristic linear operating rule calibrated by regression.
- (p. 683) Hall et al. (1968) price released water and peak/nonpeak power (Eq. 33), with nonlinear energy functions. Letting the loss depend on state "In principle" has "no computational disadvantage", because the return function and strategy depend only on state anyway.
- (p. 684) Becker and Yeh (1974b) embed many small LPs in a DP over cumulative on-peak generation to derive monthly operating rules for the Central Valley Project. Becker et al. (1976) also derive daily and hourly rules.
- (p. 685) Massé (1946) is credited with the first satisfactory solution of an inventory problem with nonnegative variables, in reservoir operation. The origins of DP, inventory theory and reservoir management are "intimately intertwined".
- (p. 685) Little (1955): the hydro problem differs from business inventory because the *input* (river flow) is random, and because a fuller reservoir makes each unit of water more valuable, since head is higher.
- (p. 685) **Inflow model and state choice:** Little assumed lag-1 Markov inflows, p(i_t | i_{t−1}, …, i_1) = p(i_t | i_{t−1}) (Eq. 41), and rejected independence (Eq. 42) as "untenable for river flow". The state therefore becomes x_t = (s_t, i_{t−1}) (Eq. 43). Whether independence is tenable depends on the decision interval: for southwestern rivers it "may be tenable" weekly but not daily. Independence gives "much more elegant and easily computed" strategies.
- (p. 685) Little (1955) for Grand Coulee: N = 26 two-week stages, transition matrix from 39 years of flows. The optimal strategy improved on the rule curves in use by only about 1%, "but even that figure represents a substantial financial savings".
- (pp. 685–686) Under independent inflows, Gessford and Karlin (1958) and Russell (1972) prove structural results: optimal release strategies are piecewise linear in storage (Figs. 6–7).
- (p. 686) Su and Deininger (1974), Lake Superior: a strategy 15% better than the Army Corps of Engineers policy. They use **time-dependent Markov transition probabilities to capture seasonality**.
- (pp. 686–687) Gablinger and Loucks (1970) solve the discretised stochastic OCP as an LP over joint state–control probabilities. DP found a steady-state policy in about 1/20 of the LP time. The LP needs (states × controls × stages) variables against (states × stages) for DP, e.g. 10^4 vs 10^3.
- (p. 687) **Size limit of SDP:** "two-reservoir systems are the largest to be reported solved by stochastic dynamic programming", against up to 10 reservoirs in the deterministic case. Schweig and Cole (1968) report severe computational difficulties even with past inflows discretised into only two levels.
- (p. 687) A **proper state variable** is one for which the distribution of x_{t+1} depends on the history (x_t, u_t, x_{t−1}, …, x_1) only through (x_t, u_t). Sniedovich and Davis (1975) augmented the state with a "probability of no failure" for chance constraints but did not show it is a proper state.
- (pp. 687–688) Rossman (1977) handles a constraint on the expected number of failures by Lagrangian duality: SDP is solved for a fixed multiplier λ, and λ is searched to maximise the dual. With duality gaps, randomised strategies can help.
- (p. 688) The curse of dimensionality "is the greatest single hindrance" to DP for large-scale OCPs.
- (p. 689) Continuous-state numerical DP needs differentiable losses and dynamics, so "corners and steps must be approximated by smooth humps". There is a trade-off between modelling perfection and tractability. Successive-approximation methods can converge to local optima or not converge.
- (pp. 689–690) DDDP searches 3^n instead of about 101^n controls per state, but still grows exponentially. IDP reduces each iteration to a one-dimensional state and "does overcome the curse of dimensionality", but converges only linearly (it is a block Gauss–Seidel method). Reservoir operation suits IDP because the dynamics are linear and invertible in the release.
- (pp. 690–691) DIFF DP converges quadratically and also overcomes the curse. Yakowitz and Rutherford (1981) solved OCPs with up to 40 state variables. Nonlinear programming solved a 38-reservoir, 49-stage deterministic problem in about an hour of CDC 6400 time.
- (p. 691) **Stochastic case:** there are "no widely applicable computational devices other than" DDP. The largest numerical SDP solutions have "at most two or three state variables".
- (p. 692) **Discretisation error:** Doran (1975) found that Markov-chain models of reservoir storage give "incorrect and even nonsensical answers" when the storage interval is discretised too coarsely. Storages are a Markov process even when inflows are independent. Klemeš (1977) showed the computed loss becomes seriously wrong as storage capacity grows for a fixed number of levels, and derived minimum numbers of levels. Yakowitz: "One should be wary of proposed solutions until the deleterious effects of discretization have been somehow bounded and found acceptable."
- (pp. 692–693) Gal (1979) fits a parametric family v(x, a) to the return function at a finite set of states, stage by stage backwards. This avoids discretising the state space but needs a family rich enough for the true return function, and the parameter count grows fast with dimension (polynomials of degree 3: order n^3).
- (p. 693) Howard's policy iteration needs a linear system of M equations per iteration, with M limited to below about 1000 (1982 hardware). In its prototypical form it does not hold "great promise" for large stochastic OCPs.
- (pp. 693–694) Controlled diffusion (Chernoff and Petkau 1978, Brownian-motion inflow, potential function) gives PDEs with one variable per reservoir, which limits it to "three or four reservoirs at most".

## Strengths
- One unified notation (state, control, dynamics, single-stage loss, policy or strategy, functional equation) for both deterministic and stochastic DP (pp. 673–675). The definitions can be cited directly in a theory chapter.
- Gives explicit, quantified statements of the curse of dimensionality: 10^12 example (p. 674), 3^n vs 101^n (p. 689), "two or three state variables" for SDP (p. 691), two reservoirs for SDP vs ten deterministic (p. 687).
- Explicit about how the inflow model drives the state definition (Markov vs independent, pp. 685, 687), and about discretisation errors in Markov-chain models (p. 692). Both are relevant to any Markov-chain uncertainty model.
- Summary tables (Tables 1–6) list state, control, loss and dynamics for every surveyed study, so it works as a lookup of classic formulations.
- Candid about limits, e.g. the 1% improvement of Little's optimal policy (p. 685) and Howard's own sober assessment of policy iteration (p. 693).

## Weaknesses / limitations
- **Predates SDDP** (Pereira and Pinto, 1985/1991) and Benders-based multistage stochastic programming. Its claim that DDP is the only universal stochastic method (pp. 675, 691) is outdated. Don't cite it for the state of the art in stochastic hydro scheduling.
- No electricity markets, price uncertainty, reserves or pumped storage. Hydropower is treated as demand satisfaction or as scheduled peak/off-peak prices (p. 683).
- Computational limits are tied to 1982 hardware (e.g. M < 1000 states for policy iteration, p. 693; CDC 6400, p. 691).
- Deliberately restricted to continuous-state methods in §5 (p. 688), and written partly from the author's own preferences, e.g. his "increasing enthusiasm" for DIFF DP (p. 689).
- The text in our repo copy (`paper.txt`) is an OCR-like extraction with merged words and garbled equations (e.g. on p. 676). Equation details should be checked against the PDF.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3.x: DP definitions (state, control, dynamics, loss, policy) | Deterministic OCP, Eqs. (1)–(5); Bellman's definition of DP as "the theory of multistage decision processes" | pp. 673–674, §2 |
| Theory 3.x: SDP definition and recursion | Probabilistic transition function P_t(y; x, u); strategy S_t(x); expected objective (7); stochastic functional equation (8); discretised version (9) | pp. 674–675, §2 |
| Theory 3.x: choice of state variables / Markov property | "Proper state variable": distribution of x_{t+1} depends on the history only through (x_t, u_t) | p. 687 |
| Theory 3.x: state augmentation for serially dependent inflow | Little (1955): lag-1 Markov inflow, state (s_t, i_{t−1}), Eqs. (41)–(44); independence "untenable for river flow"; depends on time step (weekly vs daily) | p. 685 |
| Theory 3.x: curse of dimensionality | 10 levels and 12 states give 10^12 nodes; DDP limited to 4–5 state and control variables | p. 674 |
| Theory 3.x: SDP harder than deterministic DP | SDP solved for at most two reservoirs vs up to 10 deterministic; "at most two or three state variables" | pp. 687, 691 |
| Theory 3.x: motivation for value-function approximation | Gal (1979) parametric return-function approximation; DIFF DP and IDP sidestep the curse | pp. 689–693 |
| Method: Markov-chain discretisation and number of states | Doran (1975), Klemeš (1977): too coarse discretisation gives wrong or nonsensical results; minimum number of levels | p. 692 |
| Method: seasonal transition probabilities | Su and Deininger (1974): time-dependent Markov transition probabilities for seasonality | p. 686 |
| Method: benchmark / evaluation design | Little (1955): optimal SDP policy vs rule curves on 39-year record, about 1% gain; Su and Deininger: 15% over Army Corps policy | pp. 685–686 |
| Model: mass balance with implicit spill | x_{t+1} = min{C, x_t + i_t − u_t} (Eq. 32, 44); multireservoir Eq. (34) | pp. 682–683, 685 |
| Model: head effect on water value (historical remark) | Little: the fuller the reservoir, the more valuable each unit of water, because head is higher | p. 685 |
| Lit. review: history of DP/SDP in hydro operation | Massé (1946), Little (1955), Young (1967), Hall et al. (1968), multireservoir benchmarks, Tables 5–6 | pp. 682–688 |
| Lit. review: price-based hydro objective (early) | Hall et al. (1968): scheduled peak/nonpeak power prices, Eq. (33), Shasta Dam | p. 683 |
| Lit. review / sizing: nested design-operation optimisation | Trott and Yeh (1973): optimal operation for each capacity vector, NLP over capacities; Dudley and Burt (1973) similar | pp. 676–677, 679 |
| Lit. review: chance constraints and Lagrangian duality in reservoir SDP | Askew (1974–75), Sniedovich, Rossman (1977) | pp. 687–688 |
| **Not** for: SDDP, Benders, electricity markets, PHS | Not covered (predates SDDP) | — |

## Useful quotes (with page numbers)
> "... the most obvious computational device of simply discretizing the state space leads to an exponential growth in computational effort with increase in state dimension." (p. 673)

> "The main problem with the DDP approach is the phenomenon which is popularly known as the 'curse of dimensionality.'" (p. 674)

> "... the limit of the domain of computational applicability of DDP is restricted to problems having at most four or five state and control variables." (p. 674)

> "... two-reservoir systems are the largest to be reported solved by stochastic dynamic programming, whereas we have noted that deterministic reservoir systems of up to 10 reservoirs have been solved." (p. 687)

> "One should be wary of proposed solutions until the deleterious effects of discretization have been somehow bounded and found acceptable." (p. 692)

> Little (1955), quoted: the independence assumption is "... untenable for river flow. The flow this week is an indicator of next week's flow ..." (p. 685)

## Follow-up references to check (backward snowballing)
- Little, J. D. C. (1955), "The use of storage water in a hydroelectric system", *Operations Research* 3, 187–197: first English-language SDP for hydro, Markov inflow state (p. 685).
- Massé, P. (1946), *Les Réserves et la Régulation de l'Avenir dans la Vie Économique*: origin of water values / functional-equation reasoning (p. 685).
- Bellman, R. (1957), *Dynamic Programming*; Bellman and Dreyfus (1962), *Applied Dynamic Programming*: DDP and the curse of dimensionality (p. 674). Our thesis cites "Bellman, 1957" in plain text.
- Su, S. Y. and Deininger, R. A. (1974), WRR 10, 11–25: seasonal Markov transition probabilities (p. 686).
- Klemeš, V. (1977) and Doran, D. G. (1975): discretisation errors in Markov storage models (p. 692).
- Gablinger, M. and Loucks, D. P. (1970): LP formulation of stochastic reservoir OCP (p. 686).
- Gal, S. (1979): parametric value-function approximation (p. 692).
- Sobel, M. J. (1975), "Reservoir management models", WRR 11(6), 767–777: structured multireservoir policies (p. 692).
- Heidari et al. (1971) and Larson (1968): DDDP/IDP and the four-reservoir benchmark (p. 683).
- Trott and Yeh (1973): reservoir sizing by nested operation optimisation (pp. 676–677).

