# 5.3.1 user test: what each citation rests on (checked in paper.txt on 2026-11-10)

| Citation | Claim in the draft | Passage |
|---|---|---|
| belsnes2016applying | stochastic earns more in every case they test, mainly by seeing the spill risk and producing earlier when the reservoir is high | Tables 3–5: +0.39 %, +0.01 %, +8.9 % (pp. 176–178); p. 177: "the deterministic model do not see the same risk of spill" |
| lohndorf2013 | in their case the gain over a rolling deterministic plan is small for small power capacity, several times larger for large | p. 28: "+0.7 %" small system, "+8.5 %" large; "a flexible storage system that possesses the ability to quickly change the reservoir content benefits more from a stochastic solution" |
| abgottspon2013stochastic | inflow the only random input of their pumped-storage model | p. 2–3: random data = inflows (Table I), one-year horizon |
| helseth2016, helseth2017iet, bore2026assessing | inflow stochastic in medium-term owner models | notes: AR(1) inflow in SDDP (helseth2016 p. 935); weekly inflow states (helseth2017iet); inflow–price clusters (bore2026 p. 3–4) |
| helseth2017 (2018) | system models draw inflow, temperature and wind from historical weather years | note: historical records of inflow, wind, temperature, snow and prices, each year with equal probability (p. 443) |
| chazarra2017 | closed-loop plant without natural inflow | p. 345: closed-loop, daily-cycle PSHP |
| lohndorf2013 … bore2026assessing (group) | prices and inflow both stochastic | notes of each: Markov lattice of prices and inflows (lohndorf p. 10); inflow and prices (abgottspon2014); price chain + AR inflow (helseth2016); joint price–inflow chain (schaffer2022; kleiven2023; alic2023 p. 25; bore2026 p. 3–4) |
| faria2011day | short-term models treat inflow as known over their horizon | p. 77–78: prices from an ARMA-GARCH model; inflow is not a random input (aasgard2020value dropped: its paper.txt pp. 165–171 treats prices and balancing volumes as stochastic, so "only the energy price" was wrong) |
| ak2019quantifying | each historical price year solved separately | p. 741: scenario-based approach, one deterministic model per price year |
| chazarra2017 | representative weeks scheduled with known prices | p. 352: "price-taker, perfect information"; two representative weeks (note) |
| helseth2017iet | reserve-capacity prices treated as stochastic | p. 130 of the text: "reserve capacity and energy, treating both prices as stochastic"; abstract: capacity prices through a discrete Markov chain |
| helseth2016 | joint energy- and reserve-price states built from a limited set of simulated scenarios; transition probabilities adjusted | p. 938–939 (note: 3×3 nodes from 80 EMPS scenarios; probabilities adjusted) |
| kleiven2023 | starts from the negative price–inflow correlation; ignoring it changes water values and operation; revenue loss small in their case | p. 303: "underestimates the marginal water value if it ignores the negative correlation between objective uncertainty (price) and constraint uncertainty (inflow)"; p. 524: "around 0.06 % higher expected revenue"; note: 0.17–0.30 % over the horizon; higher autumn reservoir |
| perezdiaz2020medium | energy and reserve prices modelled both as independent and as a joint process (the result of the comparison is not claimed in the draft) | p. 4: "the cross-correlation between the two variables was −0.43 … two different ways, namely: each as an independent lag-1 …"; p. 5: "correlation between the daily average EM/RM prices and the daily average water inflow was −0.34/0.14, and has therefore been ignored"; results M3 vs M4 (p. 7) |
| helseth2016 | prices assumed independent of inflow because the method requires it; justified from experience | p. 937: "the combined SDDP/SDP algorithm generally requires the stochastic processes being modelled in the SDP part to be independent … Thus, the weekly price processes are assumed independent of the inflow. In our experience, for a regional system … it is difficult" |

All citations in the third version are checked in paper.txt except the Helseth 2016 state construction (note, pp. 938–939) and Chazarra's two representative weeks (note).

## Fourth version (after review round 2)
| Citation | Claim | Passage |
|---|---|---|
| belsnes2016applying | deterministic plan does not see the spill risk and keeps the reservoir too high; stochastic produces more to avoid spill | p. 177: "the deterministic model do not see the same risk of spill"; p. 176 (text l. 492): the stochastic solution reduces "the reservoir volume by producing more in order to avoid spill" |
| kleiven2023, helseth2016 | both concern conventional plants without pumping | kleiven: Norwegian producer, conventional reservoir (note); helseth2016 p. 934–935: watercourse of seven conventional plants (note: no pumping) |
| perezdiaz2020medium | removed from the dependence paragraph: the result of its independent-vs-joint comparison is not verified in paper.txt |
| helseth2017 | removed: a system model, not an owner study scheduling a plant |
