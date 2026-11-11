# 5.2: what each citation rests on (2026-11-10)

All passages were checked in `paper.txt` on 2026-11-10 unless marked "note". Full detail in `knowledge/topics/valuation-perspective.md`.

| Citation | Claim in the draft | Passage |
|---|---|---|
| helseth2013 | schedules the Icelandic hydro-thermal system as a whole under one objective | p. 1427: "The objective of the scheduling is to maximise the expected value of income from power sales, minus generation and purchase costs" for the whole system; p. 1431: case study of the Icelandic system (Landsvirkjun and Landsnet data, 12 hydro plants in 5 watercourses) |
| henden2016economic | values pumped-storage expansions by socio-economic surplus; prices come out of the model as results; computes the owners' share separately | pp. 117–118: EMPS "maximize the socio-economic surplus"; p. 118: "Simulation results are power prices, reservoir level, exchanges between areas, production on each power station and more"; pp. 119–120, eqs. 1–5 |
| helseth2017 (2018) | values a pumped-storage expansion by the change in expected socio-economic surplus; exogenous markets outside the Nordic region | p. 441: "evaluate the changes in expected socio-economic surplus when … upgrading an existing pumped-storage plant"; p. 445: cost minimisation "equivalent to maximising socio-economic surplus"; exogenous markets GB, DE, NL, PL, RU |
| helseth2023hydropower | no obligation to cover demand; the problem is distributed to the producer as expected-profit maximisation given price forecasts; the long-term model is a fundamental market model; price-taking a condition for an efficient market that holds fairly well in the Nordic market | p. 7 "Decentralized Approach": "The price-taking assumption is a necessary condition for a free market to be economically efficient and is believed to hold fairly well for the Nordic market"; p. 8 "the LTS model takes a fundamental market modeling approach" |
| ak2019quantifying | existing cascade operated as pumped storage; net revenue gain that varies with the price year; price-taker justified by the small size of the company | pp. 739–740: existing conventional cascade (HPP) compared with pumped-storage operation (PSH); abstract and Table 2 p. 747 (2.9–10.4 % over 2013–2017); p. 741: "a small company who acts as a price-taker" |
| alic2023optimal | only a small gain from a pump added to a Norwegian cascade with environmental restrictions; price-taker in a competitive market | pp. 16–22: minimum environmental flow, ramping and state-dependent abstraction constraints; p. 30: "only" +2.35 % median revenue; p. 24: "a price-taker agent operating in a competitive energy market" |
| perezdiaz2015trends | reserve markets are small, so bids there move prices more | p. 772: bids in balancing or reserve markets "are more likely to have an impact … due to the relatively small volume" |
| perezdiaz2020medium | influence depends on the producer's size relative to the market; price-maker in the reserve market only; profit changes very little, operation does | p. 3: "depends on the producer's size relative to each market's demand"; pp. 7–8: +0.09–0.12 % profit, −29 % spillage |
| abgottspon2013stochastic | linear price–quantity dependency, estimated from experience, constant over the stages | p. 1; p. 4 |
| fullnerRebennack2025 | price-maker revenue functions non-convex; SDDP needs tailor-made extensions | p. 460 |
| helseth2016 | price-taking producer; prices as uncertain inputs | p. 934: "hydropower producers will typically act as price-takers trying to optimize … expected profit" |
| bore2026assessing | plant "sufficiently small to operate as a price taker within the relevant price zone" | p. 3 |
| sioshansi2009estimating | price-taking keeps the scheduling problem linear | p. 270: "Because of the price-taking assumption, the model is a linear program" (the draft claims nothing beyond this) |
| henden2016economic | a large expansion in Norway largely removes its own profitability | p. 122: "the large PSP capacity will depress the high and increase the low power prices, arbitraging away its own profitability"; Fig. 3b: owner surplus near zero for 6,650 MW and more |
| dallinger2019socioeconomic | price spreads of pumped storage decline as storage capacity grows | pp. 488–489, Table 1 |

Not cited: Baslis and Bakirtzis (2011) and McDermott (2020), neither in `references.bib` (Q-001, Q-002); Schüller et al. (2024), whose finding rests on the note only and was dropped after review.

## Three-paragraph version (2026-11-10, after Anders' judgement)
Claims removed: "system models supply the price forecasts rather than the decisions" (true only of the Norwegian planning chain as described by helseth2023hydropower p. 8, not of helseth2013, which is a production-planning model for the Icelandic system). Added: lohndorf2013 (price-taking pumped-storage owner, day-ahead; p. 2, 6); helseth2013 described as optimising all plants under one objective with prices as a result (p. 1427). Dallinger 2019 no longer cited.

## Four-paragraph version, correction after Anders' check (2026-11-10)
Removed: "the surplus … does not by itself say what the owner of a plant earns". Wrong as stated: Henden et al. 2016 compute producer surplus (eq. 2) and surplus to PSP owners (eq. 5, Fig. 3b) from the system model's simulated prices (pp. 119–120, 122), and in Helseth et al. 2013 the system's income is Landsvirkjun's, which owns the Icelandic system (p. 1431). Replaced by: the objective is the system's cost or surplus, not a producer's profit (helseth2023hydropower p. 7: "Minimize the expected system operating costs" vs "maximize the profit"); what a producer earns can be read from the resulting prices and dispatch, but that dispatch is the system's optimum, not the owner's.

## Anders' own 5.2 ("Scheduling Hierarchy and Valuation Perspective"), fourth paragraph rewritten (2026-11-11)
File `5-2-anders-p4.tex`. Model: bore-brensholm-2025 P23 (GROUP) with the closer of bore-2026 P33. All passages read in `paper.txt` on 2026-11-11.

| Citation | Claim | Passage | Checked in |
|---|---|---|---|
| ak2019quantifying | price-taking owner; monthly rule curves for one year using hourly prices within each month; five price years | p. 741 ("company who acts as a price-taker"; "rule curves provide guidance on the long-term decisions of the amount of monthly discharges for the upcoming year, while taking into consideration the hourly prices within each month"); p. 748 (2013–2017, Fig. 10) | paper.txt |
| ak2019quantifying | nearly the same monthly turbining with and without pumping; gain from the hours of the day; net of pumping cost | p. 751 ("similar amounts of water are turbined monthly under both systems, however PSH alters the hours of the day during which water is turbined and pumped"); Table 2 p. 747 (net revenue after pumping cost) | paper.txt |
| alic2023optimal | upper station cannot pump today; hypothetical pump of the turbine's size | p. 27 ("the upstream HPP of the considered site cannot currently operate as a PSHP because the turbine in the upper power station is not able to operate in pumping mode"); p. 29 (38 MW in both modes, note) | paper.txt / note |
| alic2023optimal | SDP with weekly stages; joint inflow–price Markov chain; minimum flow, seasonal water-level restriction, ramping | pp. 11–12 (note); pp. 16–22 (note); abstract l. 16–18 ("medium-term scheduling model … subject to three types of environmental constraints") | note + paper.txt |
| alic2023optimal | pump raises revenue even with the ramping limits that lower the conventional plant's revenue | p. 32: Case A +2.35 %, Case B −1.01 %, Case C +0.47 %; "overcome the limitations imposed by the ramping constraints" (l. 1563–1571) | paper.txt |
| helseth2016 | price-taking, risk-neutral producer selling energy and reserve capacity; both prices stochastic; seven reservoirs; two years of weekly stages | p. 934 (abstract l. 10); p. 935 (note); p. 939 (note) | paper.txt / note |
| helseth2016 | a large part of the capacity income without changing the schedule; water values change | p. 940 ("A significant part of the profit from capacity sales in cases B-C is obtained without changing the generation schedule", l. 505); p. 941 ("water values generally seems to be lower", l. 585) | paper.txt |
| closer | none of the three varies the pump size | Ak: fixed reversible-turbine capacities (Table 1 p. 746); Alic: one 38 MW pump; Helseth 2016: no pump | note |

### After the first independent review (2026-11-11)
- The opener no longer says the prices come from long-term models: Ak et al. use "the past realized prices" and call forecasting neither possible nor meaningful (p. 741, l. 180); only Helseth 2016 takes its price scenarios from EMPS (p. 940). Anders' own sentence ("can use the price forecasts from the Long-term Scheduling models") should be read with that in mind.
- "In their case" added to the Ak and Helseth findings; the Alic finding put in the past tense as their result.
- Helseth 2016 tied to the next paragraph: "which matters for short-term scheduling" rests on p. 942 (improved end-value settings for short-term tools).
- The closer says "none of the three varies the pumping capacity", a statement about these three studies only.
- Length cut from about 215 to about 193 rendered words; the model paragraph (bore-brensholm-2025 P23) has 178 with two studies.

### After the second independent review (2026-11-11)
- Opener limited to "studies such as these"; "expected" dropped because Ak et al. average realised years rather than maximise an expectation (p. 741).
- Year counts ("five years", "two years") removed: no numbers before the comparability caveat.
- Ak's gain hedged with "may" (p. 751: "may result in significant gain").
- Helseth 2016 given its reason for being in the paragraph (what an added source of income does to the water values, Fig. 7 p. 941); the short-term consequence left to Anders' next paragraph, which cites it for that.
- "Much of" changed to the source's "a significant part of" (p. 940).
- Length 202 rendered words against the 178 of the model paragraph with two studies; the reviewer accepted this under the precedent rule. A third review round was not run; the remaining fixes were mechanical.

