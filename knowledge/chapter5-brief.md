# Chapter 5 brief: the facts the literature review may use

The literature-review skill takes style from the reference theses and content from the papers; what it may say about *our own* work comes only from here. Keep it current: update after every session that changes a decision, a number or a research question. Items marked TODO need the group's wording.

## The thesis in five sentences (check against ch. 1 and ch. 6; TODO Anders)
1. The project report studies the long-term operating value of a Norwegian pumped-storage hydropower plant with natural inflow, from the owner's perspective, as a price-taker in the day-ahead and reserve-capacity markets.
2. Operation is optimised with a Markov-chain SDDP: weekly stages, joint price–inflow states from clustering, hourly decisions inside a week whose inputs are known once it starts, reserve activation excluded (confirm in ch. 6).
3. The question is how pumping power, generating power and reservoir capacity, individually and together, affect that value.
4. A related question is how the answer changes with the volatility and persistence of electricity prices.
5. The contribution is a comparative understanding of these capacity interactions under uncertainty, positioned against the reviewed studies in Table 3.

## Research questions
TODO: paste the exact wording from chapter 1. Until then the review refers to "the research questions" without quoting them.

## Decisions that bind the review
- D-001 (2026-11-09): six-part structure of the chapter; the literature chapter lives in `drafts/` until the group moves it to Overleaf.
- D-002 (2026-11-10): the review is written with the `literature-review` skill; the closest four theses decide ties.
- Thesis-side: SDDP bounds and stopping rule follow helseth2016 (thesis commit 2026-11-10, "D-024"); ch. 6 is marked DRAFT.
- Group rules from the 2026-11-09 handoff: one theme per subsection; no SDP/SDDP/two-stage/rolling-horizon before the methods subsection; the own model only briefly at the end and in the last table row; a table positioning our study.

## Reportable numbers, each with its source and check status
| Number | Source | Checked in |
|---|---|---|
| Net revenue gain 2.9–10.4 % (avg 6.0 %) from running a Turkish cascade as pumped storage, five price years 2013–2017 | ak2019quantifying, abstract and Table 2 p. 747 | paper.txt |
| Median revenue +2.35 % from a 38 MW pump added to a Norwegian cascade (energy only) | alic2023optimal, p. 30 | paper.txt |
| Stochastic over deterministic: +0.39 %, +0.01 %, +8.9 % in three cascade cases; spill cut 60–90 % | belsnes2016applying, Tables 3–5, pp. 176–178 | paper.txt |
| Stochastic policy over a rolling deterministic plan: +0.7 % (small power capacity) vs +8.5 % (large) for a pumped-storage plant | lohndorf2013, p. 28 | paper.txt |
| Ignoring the price–inflow correlation costs 0.17–0.30 % of expected revenue (0.06 % in a local example) | kleiven2023, p. 524 and takeaway | note (0.06 % in paper.txt) |
| Price-maker vs price-taker water values in the aFRR market: +0.09–0.12 % profit, −29 % spillage | perezdiaz2020medium, pp. 7–8 | note |
| 1 GW storage device in PJM loses about 10 % of its price-taker arbitrage value (more than 20 % in earlier years) | sioshansi2009estimating, pp. 274–275 | paper.txt |
| Only about 950 MW of new Norwegian pumped storage is socio-economically justified; large capacity "arbitrages away its own profitability" | henden2016economic, pp. 121–122 and figures | paper.txt and figures |
| Stochastic within-week model about 10 % higher expected profit, only with weekly reserves | abgottspon2014, note | note |
| Primary reserves raise expected operating profit 7–11 % for a single Norwegian reservoir | helseth2017iet, note | note |
| Helseth 2016: 3×3 price nodes from 80 EMPS scenarios, probabilities adjusted | helseth2016, pp. 938–939 | note |
| Forward trading raises simulated profit about 20 % (24 vs 20 M€) for a price-making Swiss plant | abgottspon2013stochastic, p. 6 | note |

Numbers not in this table are not reported in the review until they are added here with a check.

## Notation and terms
`knowledge/glossary-notation.md`. The review uses words, not symbols.

## Must-contain, per section (from `topics.md` and the group's structure)
| Section | Must contain | Source pack (read first) |
|---|---|---|
| 5.1 Scope and search | how the review was built, criteria, snowballing (TODO: the search log is empty) | `literature/search-log.md`, Bore 2026 §4.1 |
| 5.2 Perspective | system vs owner; what system models optimise and produce; price-maker representations and limits; why price-taking is assumed | `knowledge/topics/valuation-perspective.md`; notes: helseth2013, henden2016economic, helseth2017, dallinger2019socioeconomic, helseth2023hydropower, ak2019quantifying, alic2023optimal, abgottspon2013stochastic, baslis2011midterm, helseth2016, bore2026 |
| 5.3 Uncertainty | why stochastic; inflow; prices by market; dimensionality; dependence; timing of information; representation by weekly states; volatility and persistence | notes: belsnes2016applying, lohndorf2013, helseth2016, helseth2017iet, kleiven2023, alic2023optimal, bore2026, abgottspon2014, abgottspon2016multihorizon, mo2001, haldrup2006regime, bradbury2014economic, lohndorf2023, schaffer2022stochastic |
| 5.4 Markets | energy, reserve capacity, activation; what each adds and costs; comparability caveat before numbers | notes: helseth2016, helseth2017iet, chazarra2017, perezdiaz2020medium, bore2026, dallinger2019socioeconomic, abgottspon2014, faria2011day |
| 5.5 Capacities | adding a pump; upgrading units; large expansions and price effects; reservoir sizing | notes: ak2019quantifying, alic2023optimal, schuller2024practical, helseth2017iet, bore2026, helseth2017, henden2016economic, zisos2023mixing, sioshansi2009estimating, bradbury2014economic |
| 5.6 Methods | two-stage, rolling horizon, SDP, SDDP and extensions, applications to owners; physical detail retained | notes: faria2011day, helseth2017, sioshansi2009estimating, alic2023optimal, helseth2017iet, abgottspon2014, pereira1991, helseth2013, helseth2016, hjelmeland2019energies, helseth2024approximating, bore2026, abgottspon2016multihorizon, schuller2024practical |
| 5.7 Gap and contribution | the gap in the nearest studies' own terms; what this study does; Table 3 with our row | `knowledge/decisions.md`, STATUS |

## Missing from the library or the bib (do not cite until fixed)
McDermott 2020 (Q-001); Baslis & Bakirtzis 2011 not in references.bib (Q-002); two owner studies from the old text (Q-003); warland2016stochastic not in references.bib.
