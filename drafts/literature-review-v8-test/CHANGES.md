# 5.3.1 user test: what each citation rests on (checked in paper.txt on 2026-11-10)

| Citation | Claim in the draft | Passage |
|---|---|---|
| belsnes2016applying | stochastic earns more in every case, mainly by seeing the spill risk | Tables 3–5: +0.39 %, +0.01 %, +8.9 % (pp. 176–178); p. 177: "the deterministic model do not see the same risk of spill" |
| lohndorf2013 | gain over a rolling deterministic plan small for small power capacity, several times larger for large | p. 28: "+0.7 %" small system, "+8.5 %" large; "a flexible storage system that possesses the ability to quickly change the reservoir content benefits more from a stochastic solution" |
| abgottspon2013stochastic | inflow stochastic over a year | p. 2–3: random data = inflows, one-year horizon |
| helseth2016, helseth2017iet, bore2026assessing | inflow stochastic in medium-term owner models | notes: AR(1) inflow in SDDP (helseth2016 p. 935); weekly inflow states (helseth2017iet); inflow–price clusters (bore2026 p. 3–4) |
| helseth2017 (2018) | system models draw inflow, temperature and wind from historical weather years | note: historical records of inflow, wind, temperature, snow and prices, each year with equal probability (p. 443) |
| chazarra2017 | closed-loop plant without natural inflow | p. 345: closed-loop, daily-cycle PSHP |
| lohndorf2013 … bore2026assessing (group) | prices and inflow both stochastic | notes of each: Markov lattice of prices and inflows (lohndorf p. 10); inflow and prices (abgottspon2014); price chain + AR inflow (helseth2016); joint price–inflow chain (schaffer2022; kleiven2023; alic2023 p. 25; bore2026 p. 3–4) |
| faria2011day, aasgard2020value | short-term bidding models: price uncertainty only | faria p. 77–78 (ARMA-GARCH prices, inflow not random); aasgard note (72-h bidding, price and balancing uncertainty) |
| ak2019quantifying, chazarra2017 | prices known, each year/case solved separately | ak p. 741 scenario-based, deterministic per year; chazarra p. 352 "price-taker, perfect information" |
| helseth2016 | nine price states from 80 simulated scenarios, transitions adjusted | p. 938–939 (note: 3×3 nodes from 80 EMPS scenarios; probabilities adjusted) |
| kleiven2023 | ignoring the price–inflow correlation lowers water values, keeps the reservoir higher in autumn, costs a fraction of a per cent of revenue | takeaway and p. 524: "around 0.06 % higher expected revenue"; note: 0.17–0.30 % of expected revenue over the horizon; higher autumn reservoir |
| perezdiaz2020medium | cross-correlation −0.43 between energy and reserve prices; independent and joint chains compared; inflow correlation ignored | p. 4: "the cross-correlation between the two variables was −0.43 … two different ways, namely: each as an independent lag-1 …"; p. 5: "correlation between the daily average EM/RM prices and the daily average water inflow was −0.34/0.14, and has therefore been ignored"; results M3 vs M4 (p. 7) |
| helseth2016 | prices assumed independent of inflow because the method requires it; justified from experience | p. 937: "the combined SDDP/SDP algorithm generally requires the stochastic processes being modelled in the SDP part to be independent … Thus, the weekly price processes are assumed independent of the inflow. In our experience, for a regional system … it is difficult" |

Not checked in paper.txt (note only): helseth2017iet reserve prices stochastic; schaffer2022stochastic joint chain; aasgard2020value.
