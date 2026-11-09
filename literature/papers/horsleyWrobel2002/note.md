---
bibkey: horsleyWrobel2002
title: "Efficiency rents of pumped-storage plants and their uses for operation and investment decisions"
authors: "Anthony Horsley, Andrew J. Wrobel"
year: 2002
venue: "Journal of Economic Dynamics and Control 27(1), 109-142 (repo PDF: LSE STICERD Discussion Paper TE/00/405, Nov. 2000)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [modelling-phs-plants, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "For a price-taking pumped-storage plant facing a known cyclic price, LP duality gives a shadow price of stored energy psi: pump when p < psi, generate when p > psi; the marginal value of reservoir capacity is the total rise of psi over the cycle and of converter capacity the integral of |p - psi|, which in turn give the optimal reservoir/converter ratio and investment."
---

# Efficiency rents of pumped-storage plants (Horsley and Wrobel, 2002)

_**Version warning.** The PDF in the repo is the LSE STICERD Discussion Paper TE/00/405 (November 2000, 32 pp.), not the JEDC article cited in `references.bib`. All page numbers below are the **printed page numbers of the discussion paper** (Introduction = p. 1, which is PDF page 3). Section and equation numbers are probably the same in the JEDC version (unverified), so cite by section/equation, not page, until the JEDC version is checked._

_**Text-extraction warning.** `paper.txt` is unreadable after page 2: the PDF font is shifted by 3 character codes (e.g. "Lqwurgxfwlrq" = "Introduction"). A decoded copy (letters readable, math symbols still garbled) was made with `tr '\044-\176' '\041-\173'`; most mathematical symbols (p, psi, k_St, k_Co) had to be reconstructed from context. Numbers inside formulas are not reliable in our text copy._

_Notation (reconstructed): p(t) = given cyclic time-of-use (TOU) price of the good; psi(t) = shadow price of stock; k_St = reservoir (storage) capacity [kWh]; k_Co = converter (pump-turbine) capacity [kW]; y(t) = net output (positive = generation, negative = pumping); s(t) = stock; T = cycle length; Pi_PS(p, k) = maximum short-run operating profit._

## Research question / purpose
- How to operate a pumped-storage plant optimally against a given cyclic TOU price, and how to value its two kinds of capacity, the reservoir and the converter (pump-turbine), by their marginal contributions to the operating profit ("efficiency rents"), and use these values for investment (pp. 1-2).
- Existing models ignore one or both capacity costs: Pyatt (1978) has no stock capacity constraint, Nguyen (1976) ignores both capacity costs, Gravelle (1976) uses a two-subperiod model that loses the distinction between storage and conversion costs (p. 1, footnote 1).
- Inspired by Koopmans (1957) on hydro-thermal water storage, but (i) covers pumped storage, (ii) gives unique, profit-imputed rents instead of Koopmans' nonunique cost-saving rents, and (iii) obtains them directly from a dual programme (p. 2).

## Setting
- **System:** generic single pumped-storage (PS) plant: a reservoir of capacity k_St charged and discharged by a converter of capacity k_Co; the good (electricity) is nonstorable and must be converted to a storable medium (p. 4, Sec. 2). Closest physical example in the paper is SMES; pumped-water and compressed-air storage are covered by the imperfect-efficiency extension in their companion paper [9] (p. 4).
- **Markets:** price-taker facing a known, exogenous, cyclic TOU price p(t) (short-run profit maximisation in competitive markets) (pp. 1-2). No reserves, no uncertainty.
- **Horizon and resolution:** one price cycle [0, T] in **continuous time**; periodicity (stock at end = stock at start) imposed; the initial stock level is a free decision (p. 6, eq. 2.2).

## Method
- **Model type:** doubly infinite-dimensional linear programme in continuous time (primal: operation, eqs. 4.4-4.8, p. 9), its dual (capacity valuation, Theorem 1, eqs. 5.1-5.6, p. 11), and an equivalent unconstrained convex programme for the stock shadow price (Proposition 4, eqs. 7.5-7.7, p. 13). Analytical results with proofs (Appendix A, pp. 21-29).
- **How uncertainty is represented:** deterministic (perfect foresight of a periodic price).
- **Solution method:** duality theory (Rockafellar 1974 conjugate duality; Kuhn-Tucker conditions = feasibility plus complementary slackness, p. 12, Prop. 3). A specialised algorithm that solves the dual first by "levelling off" local extremes of p is outlined in [9] (p. 14).
- **Key modelling choices and assumptions:**
  - Lossless conversion (round-trip efficiency 1) in this paper; extension to efficiency < 1 in [9]; with losses the optimal output is nonunique but not at the times that matter, so the capacity derivatives still exist (p. 3, footnote 3; p. 4).
  - Symmetric reversible converter: same capacity k_Co in pumping and generating mode; instantaneous conversion (p. 4). For the dual, pump and turbine capacity increments are uncoupled so that each mode gets its own shadow value (p. 10).
  - No running cost and no stock loss in storage (p. 4).
  - k_St / k_Co is the time to fully charge or discharge the reservoir (storage duration) (p. 4).
  - Capacities constant over the cycle (needed for determinacy of rents, Lemma 8, Theorem 9) (p. 5).
  - Price p continuous in time is the only assumption needed for uniqueness of psi and hence differentiability of profit in the capacities (pp. 3, 15).
  - No head effects, no inflow (pure pumped storage); hydro with natural inflow is treated in separate papers [12], [13] (p. 21).

## Data / case
- None. Purely theoretical; illustrative figures (Fig. 1, p. 8: shadow price, output, stock; Fig. 2, p. 18: investment) and a two-period example (Example 10, p. 20).

## Key findings
- (p. 6, Sec. 3) **Decentralisation by the stock price:** if psi(t) is known, the plant separates into a reservoir that buys/sells stock at psi and a converter that buys/sells the good at p. A unit converter earns (psi - p)^+ when pumping and (p - psi)^+ when generating, and earns only at full capacity utilisation; so a unit converter is worth the integral over the cycle of |p - psi|. A unit reservoir earns psi(t2) - psi(t1) by buying at t1 and selling at t2 > t1, so it is worth the sum of all rises of psi over the cycle (the cyclic positive variation, eq. 3.1).
- (p. 7, eq. 3.2) The correct psi minimises the total value of the fixed resources, k_St Var+(psi) + k_Co integral |p - psi| dt: a trade-off between a flat psi (low variation) and psi = p (low integral). Peaks of p are "shaved off" and troughs "filled in"; in the simple case psi is constant on intervals of length k_St/k_Co around each local peak and trough. Optimal output is bang-coast-bang: full generation when p > psi, full pumping when p < psi, idle when p = psi; the reservoir goes alternately from empty to full (Figs. 1b-1c, p. 8).
- (p. 11, Theorem 1) Dual of the operation LP = minimise the value of the plant's fixed inputs subject to decomposing the price p into the stock shadow price plus the pump and turbine capacity charges (eq. 5.6).
- (p. 12, Prop. 3) Optimality conditions: the reservoir capacity multiplier is nonzero only when the reservoir is full, the floor multiplier only when empty; the turbine charge only when generating at full capacity, the pump charge only when pumping at full capacity.
- (p. 13, eq. 7.4) Pump charge = (psi - p)^+, turbine charge = (p - psi)^+. psi is the shadow price of stock at each time (p. 13-14); formally, psi equals the derivative of profit with respect to an exogenous inflow of the medium (p. 14, footnote 8).
- (p. 14, Prop. 6, eq. 8.2) If p has no plateau, the optimal operation is unique and given by y = +k_Co if p > psi, 0 if p = psi, -k_Co if p < psi.
- (p. 25, Appendix) psi can rise only while the reservoir is full and fall only while it is empty; it is constant on every interval where the reservoir is strictly between empty and full; a rent is earned only at full capacity utilisation.
- (p. 15, Cor. 7, eq. 9.1) Operating profit = k_St Var+(psi) + k_Co integral |p - psi| dt. Profit is linearly homogeneous in the capacities (Euler, eq. 9.2).
- (p. 15, Lemma 8) If p is continuous, the optimal psi is unique and continuous.
- (pp. 15-16, **Theorem 9**, eqs. 9.3-9.4) With continuous p, profit is differentiable in the capacities: dPi/dk_St = Var+(psi) (total rise of the stock price over the cycle) and dPi/dk_Co = integral |p - psi| dt. Reservoir and converter are perfect complements yet have definite, separate marginal values (p. 1).
- (p. 16, Sec. 10) Bounds: dPi/dk_Co <= integral |p - median(p)| dt (eq. 10.1); dPi/dk_St <= Var+(p) (eq. 10.2). Marginal values depend only on the capacity ratio f = k_Co/k_St. As f rises (shorter storage duration), the reservoir's marginal value rises and the converter's falls towards 0. For small enough f (reservoir so large it cannot be fully charged and discharged in one cycle) an extra unit of reservoir is worth **zero**. If the price peaks and troughs are strict, extra converter capacity is always useful (footnote 13).
- (pp. 17-18, Sec. 11) Investment: converter unit cost r_Co constant; reservoir cost c(k_St) strictly convex and increasing because the best parts of a site are developed first (PWES, CAES) (p. 17). Maximise Pi - c(k_St) - r_Co k_Co in two steps: first the ratio f from r_Co = dPi/dk_Co (eq. 11.6), then the scale from dPi/dk_St in the subdifferential of c (eq. 11.7). Investment is nonzero only if r_Co is below the maximum converter value. Unique optimum for continuous, plateau-less p of bounded variation (p. 18).
- (p. 19, Comments) The optimal capacity ratio depends only on r_Co (and p), not on the reservoir cost function: a fall in reservoir cost changes the scale but not the ratio, so optimality is restored by proportional expansion. All sites of the same technique have the same optimal ratio. Site rent = shaded area in Fig. 2b.
- (pp. 19-21, Sec. 12, Example 10) **Discrete time breaks uniqueness:** with a piecewise-constant (two-valued) price, profit = (price spread) x min{k_St, d k_Co} and is nondifferentiable in the capacities at the efficient ratio; optimal psi and marginal capacity values are indeterminate. The efficient ratio depends on the price duration d, not on the price levels (p. 19).
- (p. 3) Discretising time is still useful for computation; uniqueness of the continuous-time solution ensures the discrete approximations converge as the grid is refined.
- (p. 21) Conclusion: first sound basis for valuing and operating existing PS plants and for investment; marginal capacity values are well defined when the TOU price is continuous and can be computed by an LP or equivalent convex programme.

## Strengths
- Only source we have that separates the value of stored energy (psi) from the values of reservoir capacity and pump/turbine capacity, with closed-form expressions.
- Gives the economic logic of PHS operation (pump below psi, generate above psi, idle at psi) and of the relation between storage duration k_St/k_Co and the price cycle.
- Direct link from marginal values to an investment rule (optimal ratio then scale), and a clear comparative-statics result (ratio independent of reservoir cost).
- Explicit warning that discrete time can make duals and capacity values nonunique.

## Weaknesses / limitations
- Deterministic, perfectly known periodic price; no inflow, no uncertainty, no reserves.
- Lossless, symmetric converter in this paper (efficiency handled only in companion paper [9]); no head effects, no separate pump and turbine capacities in the main theorem (only as dual increments).
- Single price cycle with periodicity; no seasonal storage or multi-cycle carry-over.
- Very technical (infinite-dimensional LP, measure theory); results are qualitative, no numerical case.
- Our repo copy is the 2000 discussion paper; page numbers differ from the cited JEDC article.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
_Pages = discussion paper TE/00/405; check against JEDC 27(1) before citing pages._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: PHS operation rule (pump if price below value of stored energy, generate if above) | Decentralisation by psi; bang-coast-bang output | Sec. 3 (p. 6-7); Prop. 6, eq. (8.2) (p. 14); Fig. 1 (p. 8) |
| Theory: water value as shadow price of stock / derivative w.r.t. stored medium | psi = shadow price; formal derivative w.r.t. exogenous inflow | Sec. 7 (pp. 12-14), footnote 8 (p. 14) |
| Theory: water value constant while reservoir is between bounds; changes only when full/empty | Appendix argument for Lemma 8 | p. 25 |
| Theory: value of stored water vs value of capacities | Theorem 9: dPi/dk_St = Var+(psi), dPi/dk_Co = integral abs(p - psi) | Sec. 9, eqs. (9.1)-(9.4) (pp. 15-16) |
| Theory: separate values of pump and turbine capacity | Uncoupled increments; pump charge (psi - p)^+, turbine charge (p - psi)^+ | Sec. 5 (pp. 10-11); eq. (7.4) (p. 13) |
| Theory: uniqueness of duals requires continuous price; nonuniqueness in discrete time | Lemma 8; Sec. 12, Example 10 | p. 15; pp. 19-21 |
| Background/Theory: storage duration = energy capacity / power capacity | k_St/k_Co = time to fully charge or discharge | Sec. 2 (p. 4) |
| Lit. review (reservoir-sizing-capacity): value of reservoir vs power capacity depends on capacity ratio; extra reservoir worthless if it cannot be cycled | Sec. 10 bounds and ratio argument | p. 16 |
| Lit. review (reservoir-sizing-capacity): optimal investment rule, convex reservoir cost, linear converter cost | Eqs. (11.1)-(11.7), Fig. 2, comments | pp. 17-19 |
| Lit. review (reservoir-sizing-capacity): optimal ratio independent of reservoir cost; proportional expansion | Comment 3 | p. 19 |
| Lit. review: earlier economic storage literature ignoring capacity costs | Footnote 1 (Pyatt, Nguyen, Gravelle); Koopmans comparison | pp. 1-2 |
| Model: LP formulation of PHS operation with storage and power limits and periodicity | Eqs. (2.2), (4.4)-(4.8) | pp. 6, 9 |
| Research gap: deterministic, lossless, no reserves | Assumptions | Sec. 2 (p. 4); p. 3 footnote 3 |

## Useful quotes (with page numbers)
> "the unit reservoir rent equals the total positive variation of [psi] over the cycle" (abstract, PDF p. 2 of the discussion paper; symbol lost in extraction)

Other key statements, paraphrased: with a continuous TOU price the reservoir and the converter have definite and separate marginal values even though they are perfect complements (p. 1); the switch from cost minimisation to profit maximisation is essential for removing the indeterminacy of marginal capacity values (p. 2).

## Follow-up references to check (backward snowballing)
- Koopmans, T.C. (1957). Water storage policy in a simplified hydroelectric system. Proc. First Int. Conf. on Operational Research, 193-227. (Classic water-value/storage-rent paper.)
- Horsley, A., Wrobel, A.J. (1996). Efficiency rents of storage plants in peak-load pricing, I: pumped storage. STICERD DP TE/96/301. (Imperfect conversion efficiency, algorithm.)
- Horsley, A., Wrobel, A.J. (1999). Efficiency rents of storage plants in peak-load pricing, II: hydroelectricity. STICERD DP TE/99/372. (Hydro with natural inflow.)
- Gravelle, H.S.E. (1976). The peak-load problem with feasible storage. Economic Journal 86, 256-277.
- Pyatt, G. (1978). Marginal costs, prices and storage. Economic Journal 88, 749-762.
- Nguyen, D.T. (1976). The problems of peak loads and inventories. Bell Journal of Economics 7, 232-241.
- Bauer, W., Gfrerer, H., Wacker, H. (1984). Optimization strategies for hydro energy storage plants. Zeitschrift für OR B 28, 103-131.

