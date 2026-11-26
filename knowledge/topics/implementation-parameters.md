# Implementation parameters: the simplified Duge configuration

**Checked 2026-11-14 (Claude with Anders).** A group member posted the configuration file of the SDDP notebook (asset `duge_simplified`, zone NO2) and asked which values to use. Each value is checked below against a source in the library or a public data set. The group has not decided anything yet (Q-007). The code repository is not on Anders' machine, so only the posted file was checked, not the code.

## 1. Plant data
| Parameter | In the file | Source says | Recommendation |
|---|---|---|---|
| `P_G_max_MW` | 200 | 200 MW, 2 x 100 MW reversible units (`pitorac2020technical` Tables 1 and 5, pp. 5, 11) | keep |
| `P_P_max_MW` | 170 | 170 MW, motors 2 x 85 MW (same tables) | keep |
| `V_max_Mm3`, `V_min_Mm3` | 1398, 0 | upper reservoir 1398 Mm3 = 755 GWh (`pitorac2020technical` Table 2, p. 5) | keep; V is the usable volume |
| `H_m` | 236.6 | gross head 220 m (`pitorac2020technical` Table 1); the owners' web pages say 240 m. 236.6 m was not found in any source (NVE's plant API answered 502 on 2026-11-14) **(unverified)** | 220 m, or name the source of 236.6 |
| `eta_G` | 0.90 | 755 GWh / 1398 Mm3 = 0.540 kWh/m3, which is exactly 220 m at 0.90 (our arithmetic). The file gives 0.580 kWh/m3, 811 GWh, 7 % above Pitorac | keep 0.90 with 220 m |
| `eta_P` | 0.85 (round trip 0.765) | round trip 65-80 % for the ten Norwegian plants; waterway loss up to 15 % at Duge, the highest; round-trip electromechanical loss 20-25 % (`pitorac2020technical` p. 12). No value per plant. Duge is therefore near the low end (our inference) | 0.80 (round trip 0.72, mid-range) as base; 0.72 (round trip 0.65) as the Duge-like sensitivity |
| `inflow_scale_factor` | 7.4935 = 488.97 / 65.252 | The NVE figure 488.97 Mm3/year could not be opened (API down) **(unverified)**. Cross-check: Pitorac's gross production 303 GWh and pumping 55 GWh imply about 480 Mm3/year of natural inflow at 0.540 kWh/m3 (our arithmetic) | keep; state that Jogla's pattern is a proxy |

The reservoir holds 1398 / 489 = 2.9 years of mean inflow. This matters for the end of the horizon (Section 3).

## 2. Start and end volume
- **What the two numbers are.** 62.1 % and 65.5 % equal NVE's reported NO2 filling on 2023-01-08 (week 1 of 2023, 0.6212) and 2025-12-28 (week 52 of 2025, 0.6548). Source: NVE magasinstatistikk API, `HentOffentligData`, read 2026-11-14. They are single observations, not normal levels. Whether the group picked them from those two weeks is our inference from the match.
- **Normal level.** NVE's median for NO2 is 72.1 % in week 52 and 71.7 % in week 1 (`HentOffentligDataMinMaxMedian`; the median covers 2006-2025, confirmed by recomputing it from the weekly series).
- **Recommendation.** If the price scenarios describe a future system year (Q-006) and not a replay of 2023-2025, use the same normal level at both ends: about 72 % (1007 Mm3) at the start and as the end target. With 260 = 5 x 52 weeks the horizon ends at the same point of the year as it starts (assuming the model starts in week 1). Equal start and end volume is the condition of `bore2026` (eq. 15, see `sddp-setup-vs-bore.md`).
- **Limit.** The regional figure covers all NO2 reservoirs. Svartevatn is a multi-year reservoir, so its seasonal swing is smaller than the region's. It is a proxy.

## 3. Horizon, end condition and discounting
- **`reported_weeks` 104, `extension_weeks` 156.** Precedents: two years of weekly stages (`helseth2016` p. 939; `kleiven2023`, who interpret only the first year because the reservoir is drained at the end, p. 18-19); 60 extra monthly stages added to 60 (`shapiro2020` p. 14; `lohndorf2019` p. 655). A physical reason for three extra years: the extension is about as long as natural inflow needs to fill the reservoir (2.9 years). Keep, and test a shorter and a longer extension as ch. 6 already promises.
- **End condition: conflict with ch. 6.** The file has a soft end target with a penalty of 1,000,000 EUR/Mm3. Ch. 6 (`eq:terminal_value`) has zero value after week N and no end requirement. With zero end value the start stock (868 Mm3, 1.8 years of inflow) is sold within the horizon: total water is 868 + 5 x 489 = 3313 Mm3 against 2445 Mm3 of inflow, 35 % more (our arithmetic). `shapiro2020` (Sec. 6.2) shows that the end-of-horizon effect remains in a 120-stage problem when the discount factor is close to one. Recommendation: keep the end target, set it equal to the start volume, and change ch. 6 to say so. The alternative is ch. 6 as written plus the extension test.
- **Penalty size.** 1,000,000 EUR/Mm3 is about 1,850 EUR/MWh at 0.540 kWh/m3. `bore2026` uses a penalty on emergency water in the same way. It only has to exceed the highest water value; a few times the highest price in the data is enough (our judgement). A very large penalty inflates the bound on future profit.
- **`annual_discount_factor` 0.97.** No source in the library uses 3 %. `kleiven2023` uses 2 % a year as a risk-free rate (p. 18); `helseth2016` and `bore2026` do not discount. Recommendation: 0.98 (weekly 0.98^(1/52) = 0.99961), citing Kleiven, unless the group has a source for 3 %. The rate must be real, since the LA25 prices are in fixed 2023 kroner.

## 4. Reserves
- **`R_G_max_MW` 20 and `FCR_N_max_MW` 20.** 10 % of installed capacity, the limit of `helseth2016` (p. 939). Keep and cite. Statnett's terms allow at most 70 MW of FCR per unit (`statnett2026c` Art. 12), and Norway's FCR-N need is about 230 MW per hour in 2026 (`statnett2026b`), so 20 MW is about 9 % of the market. The two limits are redundant while FCR-N is the only product.
- **`R_P_max_MW` 20: no source.** Duge's units are fixed-speed (375 rpm, pump start with a pony motor; `pitorac2020technical` Tables 4-5), and fixed-speed pumps cannot regulate active power (`entsoe2019psh` slide 5). Recommendation: 0 MW for the existing plant; for a variable-speed pump 0.3 x pump capacity (regulating range about 70-100 %, same slide), written as a share so that it follows the pump size in the capacity cases.
- **`FCR_N_symmetric` true, downward price 0, `period_hours` 1.** In line with the product (60-minute periods, `statnett2026c`) and with ch. 6. Keep.

## 5. Training settings: conflict with ch. 6
- Ch. 6 follows `helseth2016` (pp. 939-940): K forward paths per iteration, stop when the upper bound lies inside the confidence interval of the simulated profit. Helseth uses 200 forward scenarios, at most 60 iterations and 1000 scenarios in the final simulation.
- The file trains with one forward path per iteration and stops when the upper bound changes by less than 25,000 EUR in three iterations in a row. `confidence_level` is unused. One path gives no confidence interval.
- Precedents for the file's way: one path per iteration (`bore2026`); stopping on a stable upper bound (`helseth2022hydropower` pp. 4, 7; `seifert2025` p. 13, with a much longer window). See the stopping-rule tables in the old workspace (`../pumped-hydro-workspace/knowledge/topics/sddp.md`).
- Recommendation: choose one and make ch. 6 match. If one path per iteration is kept: (a) lengthen the window from 3 to at least 10 iterations, because a single path can leave the bound unchanged by chance; (b) state the tolerance relative to the bound (25,000 EUR is roughly 0.03 % if the five-year profit is around 80 MEUR, a rough estimate); (c) add a final simulation of 1000 paths (`helseth2016`, `kleiven2023`) and report whether the upper bound lies inside its 95 % interval; (d) evaluate also on the 30 weather years (Q-006).
- `max_iterations` 300 and `max_runtime_hours` 6 are caps, not results. Report how many iterations were run.

## 6. Additions from the SDDP sources filed 2026-11-15
Read in the text copies on 2026-11-15. They add precedents; the recommendations above stand unless noted.
- **Round-trip efficiency (Section 1).** `philpott2023using` assumes a constant 77 % for a seasonal pumped storage (p. 5); `papavasiliou2018application` uses 76.5 % for aggregate pumped storage (note). The file's 0.90 × 0.85 = 0.765 is therefore what SDDP studies assume for a generic plant. Pitorac's data still place Duge near the low end of 65–80 %. Both can be said: 0.765 as the generic base case with these two citations, 0.65 as the Duge-like sensitivity.
- **Discount factor (Section 3).** `philpott2023using` and `hole2025capacity` use an annual factor of 0.9, applied as the annual factor to the power 1/52 per week; Philpott and Downward say the value was chosen "for convenience" (p. 21). `bore2026` uses 3 %, 7 % and 10 % for the net present value of the investment, outside SDDP. So 0.97 equals Bore's lowest investment rate, but no source uses it inside the weekly recursion. `kleiven2023` (2 %) remains the only owner model with a stated rate inside SDDP.
- **End condition (Section 3).** Three more ways used by others: solve twice the analysed horizon (`bueno2023impact` p. 22); a discounted infinite horizon on a yearly cycle (`hole2025capacity` p. 6, `philpott2023using` p. 4); end-value cuts taken from a four-year run (`helseth2018optimal` p. 7). `seifert2025` fixes start and end state of charge with a penalised slack (3,000 EUR/MWh), which is the file's construction for a battery.
- **Penalty size (Section 3).** `bueno2023impact` (pp. 2, 25): penalties on slack variables strongly affect the water values. Test the end-volume penalty at two or three values and report that the water values of the reported weeks do not move.
- **Reserve limit (Section 4).** 10 % of installed capacity also in `helseth2018optimal` p. 7. `seifert2025` limits the reservation of a battery to half its rated power as a conservative assumption (p. 12): the only SDDP source with a reserve limit on a storage that charges and discharges.
- **Stopping rule (Section 5).** `helseth2018optimal` p. 8 found the confidence-interval test sensitive to the case and the sampling settings and used stabilisation of the upper bound instead. `bueno2023impact` pp. 21–22: one forward path per iteration reached the same bound as ten, in more iterations. `hole2025capacity` p. 16 stops at a fixed 1000 iterations. One forward path with a stop on a stable bound is thus defensible, if ch. 6 says so.
- **Evaluation (Section 5).** `philpott2023using` (pp. 11–12) and `hole2025capacity` (p. 17) simulate the trained policy on sequences of historical inflow years, with the storage carried from one year to the next. This is the nearest precedent for testing on the weather years in sequence.

## 7. Reserve from a fixed-speed pump (added 2026-11-15)
Section 4 recommends `R_P_max_MW` = 0 for the existing plant. One nuance from the sources in `sddp-model-comparison.md` Section 9: a fixed-speed pump can give **upward** reserve by being switched off, up to its pumping power (`deane2013derivation` p. 2148; `drury2011value` p. 4961), but it cannot regulate continuously (`chazarra2017` p. 345). The file sells FCR-N as a symmetric product, which needs regulation in both directions, so 0 MW stands for FCR-N. If an upward-only product is added later, the pump could contribute to it while it is pumping.

## Pumping range of variable-speed units in operation (added 2026-11-26, web search, Anders' question)

Plant figures found on the web, not from papers in the library. None of these sources is in `references.bib`; add them through Zotero before citing. Percentages are our own division.

| Plant | Machine | Pumping range | Share of maximum pumping power | Source |
|---|---|---|---|---|
| Frades 2 (Portugal), 2 x 395 MW | doubly-fed | 300 to 390 MW; turbine 186.4 to 372.8 MW; speed 350 to 381 rpm | 77 to 100 % | Nicolet et al., XFLEX HYDRO, arXiv:2404.06275, Table 2 and text; arXiv:2404.06299 |
| Goldisthal (Germany), 2 variable-speed units of 265 MW | doubly-fed | 190 to 290 MW | 66 to 100 % | Renewable Energy World article on Goldisthal |
| Goldisthal, other figure | | 170 to 300 MW (attributed to Voith) | 57 to 100 % | Water Power Magazine |
| Linth-Limmern (Switzerland), 4 x 250 MW | doubly-fed | pumping power adjustable "by 30 %" (general statement by GE, not a plant band) | about 70 to 100 % | GE Vernova project page |
| Okawachi (Japan), 400 MW class | doubly-fed | steps of at least 80 MW in pump mode | band of about 20 % or more | OSTI record 276823 |
| Grimsel 2 (Switzerland), 1 of 4 units | full-size converter | 600 to 765 rpm, up to 94 MW; lower power limit not found (unverified) | not found | ABB reference note |

What limits the range (XFLEX paper): with fixed speed the pump input is set by speed and head; with variable speed the range is bounded by stability at low discharge and by cavitation and power limits at the other end, and by the converter rating (speed 350 to 381 rpm at Frades 2).

Reading: built doubly-fed units pump between roughly 60-77 % and 100 % of maximum pumping power. P^{P,min} = 0.7 P^{P,max} and R^{P,max} = 0.3 P^{P,max} sit inside what the plants report, consistent with `entsoe2019psh` slide 5.

Caveat for the running rule: with a linear model the rule lets the pump sell upward reserve (reduced pumping) also when it runs at its minimum, where it physically has none. `chazarra2018` p. 106 has the exact form (upward reserve = current minus minimum consumption), which needs an on/off variable.
