# 5.3: what each citation rests on (2026-11-10)

"paper.txt" = passage read in the paper text on 2026-11-10; "note" = only the paper note checked.

| Citation | Claim | Passage | Checked in |
|---|---|---|---|
| belsnes2016applying | stochastic strategy earns more in every case; sees the spill risk | Tables 3–5 (+0.39 %, +0.01 %, +8.9 %); p. 177 "the deterministic model do not see the same risk of spill" | paper.txt |
| lohndorf2013 | gain over a rolling deterministic plan grows with power capacity relative to the reservoir | p. 28: +0.7 % small, +8.5 % large; "a flexible storage system … benefits more from a stochastic solution" | paper.txt |
| lohndorf2013, helseth2016, kleiven2023, alic2023optimal, bore2026assessing | inflow and energy prices stochastic | notes (Markov lattice of prices and inflow; price chain + AR inflow; joint chains) | note |
| helseth2016, helseth2017iet | reserve-capacity prices stochastic | helseth2016 p. 935; helseth2017iet text l. 130 "treating both prices as stochastic" | paper.txt |
| helseth2016 | transition probabilities adjusted when few scenarios are available | pp. 938–939 (3×3 nodes from 80 scenarios) | note |
| kleiven2023 | negative price–inflow correlation; ignoring it changes water values and operation; revenue loss small | p. 303; p. 524 (0.06 %); takeaway (0.17–0.30 %) | paper.txt |
| helseth2016 | prices assumed independent of inflow because the method requires it | p. 937 | paper.txt |
| helseth2013 | the week's stochastic variables known in advance; too coarse for wind balancing | p. 1432: "the values of the stochastic variables are known for a whole week in advance … not fine enough to capture the actual need for balancing wind power" | paper.txt |
| bore2026assessing | inflow (and prices) for the period assumed known | p. 3: "inflow for the period are assumed to be known" | paper.txt |
| abgottspon2014 | known week overvalues water; stochastic within-week model higher expected profit with weekly reserves | p. 6: "it overvalues the water value"; Table II expected profit per method; the "only with reserves" part is from the note | paper.txt + note |
| ak2019quantifying | monthly reservoir decisions barely change, hourly allocation changes a lot; largest gain in the year with largest daily variation | pp. 746–747 | note |
| helseth2016, alic2023optimal, bore2026assessing | weekly states by clustering, transitions counted; 9, 5 and 3 states | notes; alic p. 25 | note |
| mo2001 | transition probabilities corrected to preserve conditional expected prices; Markov model forgets its initial state exponentially | text l. 295–296: "a Markov model will tend to forget its initial state at an exponential rate" (forgetting: paper.txt; correction: note) | paper.txt / note |
| alic2023optimal, ak2019quantifying, bore2026assessing | weekly average price with fixed profile; representative daily curves; hourly series per cluster | alic text l. 196, 602 "weekly average energy price" (fixed profile: note); ak note; bore note | partly |
| haldrup2006regime | long memory in Nordic prices, strongest in Norwegian areas, related to reservoirs | title/abstract (long memory); Norwegian areas and reservoir link: note | partly |
| henden2016economic | more transmission raises southern Norwegian price variability; more pumped storage lowers it | p. 120, Fig. 1a (figure read 2026-11-10) | paper.txt + figure |
| lohndorf2023 | coordination benefits pumped storage far more than a reservoir plant | text l. 1330–1345: pumped hydro +10.0–29.1 % over sequential; "gains for the less flexible reservoir are marginal" | paper.txt |

Not cited: bradbury2014economic (volatility raises storage return; note only), abgottspon2016multihorizon (daily vs hourly; note only, deterministic case), perezdiaz2020medium (energy–reserve price correlation; result not verified), faria2011day, aasgard2020value.

## After the precedent review (2026-11-10)
Added: helseth2016 p. 937 (the combined SDP/SDDP scheme requires the SDP-part processes to be independent of the SDDP-part processes) and kleiven2023 (joint price model in an MC-SDDP lattice, note) as the reason the two studies treat dependence differently; abgottspon2014 pp. 5–6 (method 4: information arrives within the week). The section-level close was removed to match Bore 2026 §4.2, which has none. The sentence "the timing of information should be chosen in line with the products the plant sells, since reserves are committed before the energy prices are known" is the authors' reasoning (the market sequence is in the background chapter), not a cited finding.

## Verification pass on the note-only claims (2026-11-10, after Anders asked)
| Claim | Result |
|---|---|
| abgottspon2014: within-week model higher expected profit only with reserves | **verified**, Table II: method 3 (deterministic intrastage) 34.80 / 35.85 vs method 4 (stochastic) 33.40 / 39.14 without / with reserves |
| mo2001: probabilities corrected to preserve the conditional expected price | **verified**, text l. 174 ("to maintain the conditional expected spot price") |
| kleiven2023: joint price–inflow model | **verified**, l. 22, 130, 167 ("joint dynamics of prices and inflows") |
| ak2019quantifying: largest gain in the year with the largest daily variation | **verified**, p. 748: "2016 electricity prices resulted in the largest percent net revenue gain … 2016 has the largest daily variation with many outliers" |
| haldrup2006regime: long memory strongest in the Norwegian areas; reservoir link | **verified**, Table 3 (d = 0.52 for SNO and MNO vs 0.31–0.44 elsewhere); "Price persistence within the year can be partially explained by seasonal variation due to hydropower reservoir levels" |
| alic2023optimal: fixed daily profile | **verified in substance**, l. 192: "scaling factor for price variability in sub-interval k for stage t"; wording changed to "scaled by fixed sub-interval factors" |
| helseth2016: transition probabilities adjusted because few scenarios | **not found** in the text; the sentence now says what p. 938 states: (NE × NC)² transition probabilities to identify |
| bore2026assessing: hourly series per cluster (median) | note only; the paper text has no "median"; left as "an hourly series for each cluster" |
