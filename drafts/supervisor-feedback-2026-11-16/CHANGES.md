# Supervisor feedback on the theory chapter and the literature review: what was changed and what was checked

**2026-11-16, Claude with Anders.** The group pasted the supervisor's feedback and its own working versions of the two chapters (another document than `../pumped-hydro-thesis`, with its own bib file). Anders asked for a revised version in the chat, with as few changes as possible, nothing in Overleaf, and every cited claim checked against its source. The revised texts are `theory-revised.tex` and `literature-review-revised.tex` in this folder. Both are drafts for the group to rework.

Page numbers are printed pages. "Checked" means read in the text copy in `literature/` on 2026-11-16.

## 1. Factual corrections to the group's text (source says something else)
| Where | The first draft said | The source says | Source |
|---|---|---|---|
| Lit. 3.4, Helseth 2013 | a pumped hydropower unit with several reservoirs | a hydro-thermal power system (Iceland) with several reservoirs and a pumped-storage plant among the planned expansions | `helseth2013` pp. 1426, 1431 |
| Lit. 3.4, Helseth 2013 | a time resolution of 1 hour | each week has 7 aggregate or 24 sequential sub-periods; only the wind record is hourly | `helseth2013` p. 1431 |
| Lit. 3.4, Helseth 2018 | the method was chosen to handle non-convexity | SDDP does not easily handle non-convexity, so its stochastic models must be designed with care; the scenario-fan simulator keeps every reservoir and uses historical weather records | `helseth2017` p. 442 |
| Lit. 3.4, Helseth 2018 | a yearly scheduling problem | weekly decisions over the historical years 1962–2012; each two-stage problem has scenarios of 52 weeks | `helseth2017` pp. 442, 445 |
| Lit. 3.4, Ak 2019 | dimensionality might be a problem with another case study | it may become a problem as the number of consecutive reservoirs increases | `ak2019quantifying` (read 2026-11-16) |
| Lit. 3.2, Ak 2019 | given as an example of scheduling under uncertain conditions | deterministic model; price uncertainty is handled by solving it once per historical price year (2013–2017) | `ak2019quantifying` pp. 3, 8 of the PDF |
| Lit. 3.2 | Alic 2023 cited for water values guiding short-term decisions | Alic does not say this; Helseth 2016 and the SINTEF toolchain report do | `helseth2016` pp. 936, 942; `helseth2020scheduling` pp. 31–35 |
| Lit. 3.2, Helseth 2016 | "and that the quality of this information matters" | not stated in the paper; clause removed | `helseth2016` p. 942 |
| Lit. 3.4, Alic 2023 | a more detailed representation of the constraints should be included in future analysis | future work: investment analysis, price-maker setting, more detailed machine description, ancillary services; and a weekly model may overestimate production and revenue | `alic2023optimal` pp. 38, 42 of the PDF |
| Lit. 3.4, Abgottspon 2014 | the market or plant structure must be very complex | the method makes sense only if the market structure is sufficiently complex (plants: possible future work) | `abgottspon2014` p. 7 |
| Lit. 3.5, Zhang 2026 | pumped hydropower is well suited for ancillary services and can therefore achieve great economic returns | a seasonal plant can technically provide them, but seasonal arbitrage is expected to give the larger return; the paper calls for co-optimisation of both | `zhang2026unlocking` pp. 19–20 |
| Lit. 3.5, Abgottspon 2013 | physical production and trading are considered separately | the forward position is the here-and-now decision of each stage; hourly production and day-ahead trades are recourse decisions | `abgottspon2013stochastic` pp. 1–2 |
| Table 1, Ak 2019 | uncertainty: water inflow and hourly electricity prices | none inside the model | as above |
| Table 1, Sauhats 2016 | uncertainty –, markets – | day-ahead price (several forecast realisations); day-ahead market (Nord Pool, Latvia) | `sauhats2016optimal` pp. 12444–12447 |
| Table 1, "Source 6" | placeholder | Zhang et al. (2026), Energy Conversion and Management 348, 120750 (PII S0196890425012749 confirmed in Crossref) | `zhang2026unlocking` |
| Commented-out subsection, Naval 2025 | 113.5 MW installed capacity | 113.5 MW is the pump power of one of four units (99 MW turbine each); storage 5750 MWh | `naval2025optimization` |
| Theory, caption of `fig:sddp_original` | "simplified Markov-chain SDDP ... three Markov states" | the figure shows stagewise-independent realisations with averaged cuts; step 4 says "Sample ω_4" where the figure uses ξ | the figure itself |
| Theory, terminal value | `tilmant2008`, `chazarra2017` cited for distorted end decisions and for extending the horizon | Tilmant has a terminal value function in the formulation; Chazarra has a target end volume. The other two statements are in `kleiven2023` (pp. 18–19) and `helseth2016` (p. 940) | read 2026-11-16 |

## 2. Numbers added, with the passage relied on
| Statement | Source |
|---|---|
| Full export on the cable 67 % of the time without power-flow constraints, 62 % with | `helseth2013` p. 1432 |
| Standard deviation of the nodal price 11.12 % higher with pump start-up cost and minimum load | `helseth2013` p. 1433 |
| Run time about 5 h (case A) and 31 h (case E) | `helseth2013` p. 1433 |
| Median annual revenue +2.35 % with the pump, +0.47 % with ramping constraints on the reservoir level | `alic2023optimal` pp. 41–42 of the PDF |
| Stochastic intrastage problems: about 10 % higher expected profit, only with secondary reserves | `abgottspon2014` p. 7 |
| Forward trading: 24 against 20 million EUR, about 20 % | `abgottspon2013stochastic` p. 6 |
| Expected profit 107.33 % and 110.78 % of the energy-only case with primary reserves | `helseth2017iet` Table 2, p. 1645 |
| Pumped-storage data in Table 1 | `alic2023optimal`, `helseth2013` p. 1431, `helseth2017` p. 445, `naval2025optimization`, `zhang2026unlocking` p. 11, `sauhats2016optimal` p. 12450, `abgottspon2013stochastic` p. 3, `zisos2023mixing` pp. 5, 8 |

Not added: the size of the profit increase in `helseth2016` (Table II is an image in our copy and could not be read).

## 3. Could not be verified
- `helseth2023hydropowera` (Helseth & Mo 2023, IEEE document 9919382) is not in the library and the preprint site blocks automated reading. Checked: the abstract (feasibility cuts from the detailed system constrain the aggregated one; computed before or during SDDP) and the account in `helseth2024approximating` pp. 4–6 (3204 s with pre-computed cuts against 370 s for the reference). **Not checked:** that cuts computed beforehand give similar results at much lower computation time than cuts computed during the run.
- `castelletti2010`: abstract only. `cervellera2006`: title only. `bellman1957`: no copy; the principle is restated in `labadie2004` p. 99, which is now cited next to it.
- `lundgren2010`: no copy; the group decided on 2026-11-04 to accept its citations unchecked.

## 4. Sources confirmed for the new theory text
- Two-stage problem, recourse function: `birgeLouveaux2011` pp. 59–60, 104. Wait-and-see, recourse problem, EVPI: pp. 163–164; WS ≤ RP for minimisation: p. 166. Stages and periods: p. 58. Risk neutrality: p. 7. Scenario tree: pp. 22, 152. Multistage recursion and convexity of the value functions: pp. 150–151.
- Dynamic programming with discretised states and interpolation: `pereira1991` p. 360. Curse of dimensionality: p. 361; `labadie2004` p. 100. A stage as a time period: `labadie2004` p. 99.
- Cuts from dual values, piecewise linear future cost: `pereira1991` pp. 361–363. Bounds: pp. 363–364, 368. Convexity needed for convergence: p. 369.
- Value functions piecewise linear and convex in the state, concave in the objective coefficients: `fullnerRebennack2025` p. 429. Integer or non-convex stage problems: p. 506. Markov chain: pp. 495–497.
- Price as a state breaks the convexity requirement: `helseth2020scheduling` p. 31.
- TS-SDDP restricted to the linear case and right-hand-side uncertainty: `lohndorf2019` p. 650.
- Stagewise independence, state expansion, bounds: `shapiro2011` pp. 63, 66, 67.
- Water value as the multiplier of the mass balance and as the derivative of the benefit-to-go function: `tilmant2008` pp. 2–3. Shadow price of the stock and separate marginal values of the capacities: `horsleyWrobel2002` (abstract, Sections 1 and 3; the text copy is letter-shifted and was decoded).

## 5. Left for the group
1. `\ref{sec:Scheduling_Hierarchy}` needs a `\label` in the background chapter.
2. Helseth et al. (2018): the group's bib entry prints 2017. `references.bib` has 2018 (IET GTD 12(2), 441–447).
3. Citation keys: the group's document uses keys that are not in `references.bib` (`ak2019`, `naval2025`, `abgottspon2013`, `alic2023`, `zhang2026seasonal`, `chazarra2016`, `pereiraPinto1991`, `lohndorfShapiro2019`). New citations use `references.bib` keys.
4. Table 1, last row: "DA, mFRR, aFRR" is the group's entry. Chapter 6 names no reserve products and the implementation file sells FCR-N (Q-007).
5. Notation: the theory chapter uses t for the stage and ω for the Markov state; chapter 6 uses s and m, and t for the hour. The theory writes the expected future value as Q_{t+1}(x_t); chapter 6 writes Q_{s,m}(V) for the same function. `fig:sddp` indexes the cut sets by the successor state, while chapter 6 and `fullnerRebennack2025` (eqs. 14.12–14.15) keep one cut set per current state.
6. "SDDP is not widely used when modelling long-duration PHS": eleven of the 56 SDDP sources in the library model pumping (`knowledge/topics/sddp-model-comparison.md`), so the sentence should stay hedged.
