# What is said under each theme, and how it is argued

From part E of the coding (`theses/lit-review-skill/codebook/THEMES_RESULTS.md`): every paragraph's point in one line, how it is argued, and how many works' findings are reported. The themes below are the ones our chapter shares with the closest four theses. Points are given as functions ("inflow is the key uncertainty"), never as the theses' sentences; our chapter fills them with our papers and drops what does not apply to pumped storage.

## How points are argued (closest four, 106 paragraphs)
| Argument | Share | What it looks like |
|---|---|---|
| finding | 35 % | the point *is* what a named study found, reported with its method or markets |
| claim-evidence | 24 % | the authors state the point, then report findings of named studies as evidence |
| claim-backup | 13 % | the authors state the point with citations attached, findings not reported |
| reasoning | 13 % | the authors argue from logic, no source carries it (syntheses, gaps) |
| description | 15 % | no argument: openers, search strategy, what a table shows |

Findings reported per paragraph: none 31 %, one 33 %, two 15 %, three or more 7 %. So in a typical theme the pattern is: a claim paragraph with two or three findings as evidence, then one or two paragraphs built on a single study's finding, then a synthesis argued without sources.

By theme (all reviews): uncertainty is argued mostly as **claim-evidence** (59 %) and rarely as a single finding (11 %); markets, physical modelling and methods are argued mostly as **findings** (47–67 %); investment as findings and claim-evidence; contribution and gap as **reasoning** (50 %) and description.

## Theme: uncertainty (Bore 2026 has 10 paragraphs; Bore & Brensholm 5; EMPIRE 2; Norland 2)
Points, in the order the closest theses make them; (argument · works whose finding is reported):
1. Modelling uncertainty pays (profit, spillage, robustness), more so the longer the horizon. (claim-evidence · 1–2) — all four
2. Inflow is the key uncertainty because it governs long-term availability. (claim-evidence · 1–3) — Bore ×2
3. Weather variables (temperature, wind) can also be stochastic; temperature drives inflow and demand-based prices. (claim-evidence · 3+) — Bore ×2
4. Prices are modelled as stochastic in most owner studies; reserve and regulation prices less so; every price stochastic would blow up the scenario count. (claim-backup · 1–3) — Bore ×2
5. Price-taking is standard in day-ahead, less clear in smaller markets; one study with price-making is reported. (claim-evidence · 3+) — Bore 2026
6. Bid volume and activation are uncertain too and deserve modelling. (claim-backup · 3) — Bore 2026
7. Synthesis: prices and inflow are the uncertain variables; their number is kept small for tractability. (reasoning · 0) — Bore ×2, EMPIRE
8. Data must preserve statistical properties; correlations reported in the literature differ, so absence of correlation is not evidence of none. (claim-evidence · 3+) — Bore 2026
9. Scenario trees and Markov chains are built in common steps; data length and number of states vary and set computational effort. (claim-evidence · 3+) — Bore 2026
10. Input granularity (hourly vs weekly averages) differs and should match the purpose; weekly averaging hides intra-week opportunity. (claim-evidence, comparison · 3) — Bore 2026
11. Tractability: scenario reduction and collapsed stages are how multi-market models stay solvable. (claim-evidence · 2–3) — Norland

## Theme: markets (Bore 2026: 9; Bore & Brensholm: 8; Norland: 6)
1. Opener: which market combinations have been studied, and whether from an investment angle. (description)
2. Caveat: results depend on market design, region, case and inputs and are not directly comparable. (claim-backup · 1) — Bore 2026; also Bore & Brensholm inside a comparison
3. Coordinated vs sequential bidding as the basic distinction; coordinated is the more studied. (claim-backup · 1) — Bore 2026, Norland
4. Day-ahead plus intraday adds little; reserve markets attract more attention. (claim-evidence / finding · 1–2) — Bore ×2
5. Day-ahead plus aFRR: profit gains from about one per cent to a quarter depending on country and approach; production shifts to fewer full-load hours. (finding, comparison · 3+) — Bore 2026
6. Day-ahead plus symmetric reserves: gains of several per cent; a hypothetical product earned little. (finding · 2–3) — Bore 2026
7. Coordinated beats sequential, both beat energy-only; withholding capacity can pay; the value of coordination grows with uncertainty. (finding · 1 each, two consecutive studies) — Bore 2026, Norland
8. Ignoring activation underestimates cost; a fixed activation share overstates gains. (finding · 1–2) — Bore & Brensholm
9. Forward contracts and price-making noted and placed out of scope. (finding · 1) — Bore & Brensholm
10. Gap for the theme: the joint value of all eligible markets is absent; none assesses capacity expansion. (claim-evidence · 0–3+) — Bore & Brensholm, Norland

## Theme: physical modelling (Bore 2026: 3; Bore & Brensholm: 5; EMPIRE: 5)
1. Non-convex unit and generation characteristics must be modelled when co-optimising energy and reserves, or reserve sales are overestimated. (finding · 1) — Bore 2026
2. Non-convexities matter at all horizons and more with renewables; Norwegian high-head plants make head effects small. (finding + own context · 2) — Bore 2026
3. Production-function methods (piecewise linear, MILP with binaries, efficiency correction, successive LP) trade accuracy against computation and should fit the model purpose. (claim-evidence / finding · 1–2 each) — Bore ×2
4. Synthesis: detail decides performance but raises complexity; fit it to purpose. (reasoning · 0) — Bore & Brensholm
5. In system models: hydro as generator vs storage; perfect foresight problem; separating or merging pumped and regulated hydro. (finding, comparison · 1–2) — EMPIRE

## Theme: solution methods (Bore 2026: 7; Bore & Brensholm: 9)
1. Opener: which methods are reviewed and why (to position the work). (description)
2. Deterministic equivalent with short horizons and MILP handles realistic multi-market scheduling. (claim-evidence · 4) — Bore 2026
3. SDP suits small systems that need non-convex detail (binaries in stage problems); ignoring binaries overestimates reserve ability. (claim-backup · 4) — Bore 2026
4. SDDP removes SDP's dimensionality limit and is the state of the art for medium-term scheduling in hydro-dominated systems. (claim-backup · 3) — Bore 2026
5. One study in depth: how SDDP works and what it achieved. (finding · 1) — Bore 2026
6. Extensions (risk, cuts, multi-horizon) improved the method, but none addressed multiple markets. (finding, group · 4, ends on the group's omission) — Bore 2026
7. Multi-market SDDP applications exist, but investment implications are unexplored. (finding, group · 3, ends on the gap) — Bore 2026
8. Related methods (Benders, successive LP, multi-objective) and when they apply. (finding · 1–3 each) — Bore & Brensholm
9. Synthesis: method choice follows stochasticity, non-linearity, stages, horizon and objective. (reasoning · 0–1) — Bore & Brensholm

## Theme: investment / capacity (Bore 2026: 1; Norland: 7)
1. The investment perspective is the least explored; the nearest studies did not include it; it adds a dimension. (claim-evidence · 2, written as a gap) — Bore 2026
2. Price volatility and carbon costs change the value of storage and flexibility, which current expansion models undervalue. (claim-evidence · 1) — Norland
3. Studies of flexibility options find value but ignore uncertainty or investment. (finding, group · 2–3, ends on the group's omission) — Norland

## Theme: contribution (all four)
1. Opener of the chapter: the themes and that the review will compare, criticise and connect. (description)
2. Synthesis of the chapter: the two or three things the literature shows matter. (reasoning · 0–1)
3. Gap, from a named earlier study that pointed to it, then what the thesis asks. (reasoning · 1)
4. What the thesis contributes, as a list, and the table. (description · 0)

## Search strategy (both Bore theses)
How the earlier review was extended; databases and keywords or the prior work; quality questions; backward snowballing with a cited method. Past tense, description, one source.

## How to use this when planning a section
1. Take the theme's list above and keep the points that apply to our question; add points our papers force (for pumped storage: pumping cost, price spreads, within-week pattern).
2. Give each point its argument mode from the list: a claim with evidence where the field agrees, a finding where one study carries it, reasoning only in synthesis and gap paragraphs.
3. Fill the works from our library; one finding reported per study paragraph, two or three per claim-evidence paragraph.
4. Keep the theme's shape: claim first, findings in the middle, synthesis or gap last.
