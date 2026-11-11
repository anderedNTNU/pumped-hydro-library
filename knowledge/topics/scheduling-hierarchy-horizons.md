# The scheduling hierarchy: which level each source sits on, and whether the horizons agree with the TET4565 lecture

Written 2026-11-11 (Claude with Anders) after Anders brought in lecture 6 of TET4565 (`farahmand2026hydropower`) as a source on the perspectives in hydropower scheduling. Horizons below come from the "Horizon and resolution" line of each `note.md` (pages there) and from the sentences quoted in §2, read in `paper.txt` on 2026-11-11. Papers not about hydro or storage operation (textbooks, technology reviews, market documents) are left out.

## 1. What the lecture says (slides 6–8)
| Level | Horizon | Model type | Output | Norwegian tool (slide 7) |
|---|---|---|---|---|
| Long-term scheduling | 1–5 years | stochastic optimisation and simulation | reservoir levels, marginal water values; price forecast; system analyses, expansion and maintenance planning | EMPS (SDP, aggregation/disaggregation) |
| Seasonal scheduling (slide 7 calls it medium-term) | 3–18 months | stochastic or multi-scenario deterministic optimisation | marginal water values, reservoir boundaries | ProdRisk (SDP/SDDP) |
| Short-term scheduling | 1–2 weeks | deterministic optimisation | plans; portfolio bidding, production plans | SHOP (MIP/SLP) |
| Detailed simulation | 1–12 weeks | non-linear simulation | verification of plans | |

Down the hierarchy: shorter horizon, less uncertainty, smaller system boundary, more detail. Two equivalent objectives (slide 8): cost minimisation in centralised systems (Brazil, Iceland, Norway before 1991); profit maximisation per company in decentralised markets, with prices from a market simulation. Slide 6 cites the course compendium and Helseth & Geber de Melo (2020), whose published version is `helseth2023hydropower`.

## 2. How the literature defines the levels
| Source | Long-term | Medium-term / seasonal | Short-term | Where |
|---|---|---|---|---|
| Lecture (compendium) | 1–5 years | 3–18 months | 1–2 weeks | slide 6 |
| `gjelsvik2010` | 3–5 years or longer | "medium-term or seasonal", 1–2 years | days to 1 week | p. 35 |
| `fullnerRebennack2025` | 3–5 years ("long-term operational planning") | 1–2 years | a few days or weeks | p. 457 |
| `seranilla2025` | ≥ 3 years, monthly stages | 1–2 years, weekly or monthly | hours to days | p. 6 |
| `helseth2023hydropower` | EMPS 3–5 years; NEWAVE 5 years monthly | ProdRisk years (regional); DECOMP a few months (Brazil) | SHOP 1–2 weeks; DESSEM 1 week | pp. 4–5 |
| `hjelmeland2019phd` | 5–10 years for price forecasting, longer for expansion | MTHS 1–3 years (`hjelmeland2019energies` p. 1: "normally covers … one to three years") | 1–2 weeks | pp. 25–28 |
| `helseth2016` | | 1–3 years | | p. 936 |
| `helseth2013`, `helseth2015efficient` | "a typical scheduling horizon is three to five years", weekly stochastic resolution (Nordic players) | | | p. 1427; p. 14293 |
| `hagenvik2022comprehensive`, `schuller2024practical` | | 104–208 weeks (2–4 years), weekly stages | weekly deterministic problems (SHOP-type) | p. 2 in both |
| `gudbjerg2024exploring` | | 2–3 years | | l. 1157 |
| `larsen2015evaluation` | 1–5 years | | | p. 1 |
| `alic2023optimal` | | "up to a year" | days | l. 324 |
| `kong2020overview` | | | 1 day to 1 week | abstract |
| `belsnes2016applying` | | | 1–2 weeks, hourly | p. 170 |
| `ahlfors2021weekly` | years or several months | months or weeks | week or days; the definitions are "ambiguous and vary"; weekly planning should count as mid-term | Fig. 1, p. 1; p. 4 |
| `tilmant2008` | | monthly steps "fairly common in midterm (strategic) studies", with a 5-year horizon | | p. 3, p. 11 |
| `yeh1985reservoir` | long-range: monthly or yearly, stochastic | | short-range: hourly or daily, usually deterministic | p. 1803 |

**Reading.** The short-term level agrees everywhere (days to two weeks, hourly). The disagreement is the boundary between medium- and long-term. The lecture's compendium numbers put the seasonal level at 3–18 months and start the long-term level at one year. The Norwegian producer papers (SINTEF, NTNU: Helseth, Hjelmeland, Gjelsvik, Hagenvik, Schüller, Gudbjerg) and the two SDDP reviews put medium-term at one to three or four years of weekly stages and start long-term at three years. Only Alic (up to a year), Braaten ("seasonal", 52 weeks) and Brazil's DECOMP (a few months) fit the 3–18 month box. Slide 7 of the lecture itself, which places ProdRisk at the medium-term level, agrees with the papers; the numbers on slide 6 are the compendium's. Ahlfors et al. (2021) say outright that the definitions are inconsistent.

## 3. Every operational source placed on the hierarchy
"Lecture level" uses the numbers on slide 6; "paper's level" is what the paper calls itself or what §2 implies. ✔ = the two agree; ✘ = the horizon is long-term by the lecture's numbers but medium-term in the paper's own terms; ~ = one year, which lies on the lecture's boundary (seasonal up to 18 months, long-term from one year).

### 3a. Producer (owner) scheduling with water values or end-of-horizon values
| Source | Own label | Horizon | Stage / resolution | Lecture level | Paper's level | Agree |
|---|---|---|---|---|---|---|
| `abgottspon2013stochastic` | short- and medium-term | 1 year | daily → weekly → monthly stages, hourly within | seasonal/long | medium | ~ |
| `abgottspon2014` | medium-term | 1 year | 52 weekly, hourly within | seasonal/long | medium | ~ |
| `abgottspon2015hydro` (thesis) | medium-term, "months up to a few years" | typically 1 year | daily or weekly, hourly within | seasonal/long | medium | ~ |
| `abgottspon2016multihorizon` | medium-term | 1 year | daily stages, hourly within | seasonal/long | medium | ~ |
| `alic2023optimal` | medium-term | 1 year | 52 weekly, 3-hour | seasonal/long | medium | ~ (Alic's own definition "up to a year" fits the lecture) |
| `baslis2011midterm` | mid-term | 1 year | hourly | seasonal/long | medium | ~ |
| `bore2026` | not labelled ("long-term uncertainty … weekly") | 1 year | weekly, hourly within | seasonal/long | medium (weekly water values) | ~ |
| `braaten2016linear` | seasonal | 52 weeks | weekly | seasonal | medium | ✔ |
| `schaffer2022stochastic` | medium-term | 1 year | weekly, three 56-h price periods | seasonal/long | medium | ~ |
| `perezdiaz2020medium` | medium-term | 1 year | daily stages, hourly | seasonal/long | medium | ~ |
| `helseth2015cooptimizing` | medium-term | 1 year | weekly, 21 steps | seasonal/long | medium | ~ |
| `helseth2017iet` | medium-term | 1 year | weekly, intra-week steps | seasonal/long | medium | ~ |
| `larsen2015evaluation` | long-term (1–5 years) | 1 year | weekly | long | long | ✔ (the one paper that defines long-term as the lecture does) |
| `lohndorf2013` | not labelled (interday "long-term", intraday) | 1 year | 365 daily stages, hourly | seasonal/long | medium | ~ |
| `ak2019quantifying` | not labelled (rule curve) | 1 year, solved over 19 years of monthly inflow | monthly, plus hourly dispatch | seasonal/long | medium | ~ |
| `finnah2021` | not labelled | 1 year | 8760 hourly stages | seasonal/long | medium | ~ |
| `dimoski2018hydropower` | medium-term | 2 years | weekly | long | medium | ✘ |
| `grini2023` | medium-term | 2 years | weekly | long | medium | ✘ |
| `helseth2016` | medium-term (typical 1–3 years) | 2 years | weekly, 21 steps | long | medium | ✘ |
| `hjelmeland2016case`, `hjelmeland2016combined`, `hjelmeland2019energies` | medium-term (1–3 years) | 2 years | weekly, 21 steps | long | medium | ✘ |
| `hjelmeland2019tste` | medium-term | 1 year (52 stages) | weekly | seasonal/long | medium | ~ |
| `kleiven2023` | medium-term | 2 years (first year read) | weekly | long | medium | ✘ |
| `mo2001` | price forecasting for scheduling | 2 years (2–3 years ahead) | weekly | long | medium | ✘ |
| `gjelsvik1999` | medium-term | 1–3 years (test ≈ 3) | weekly | long | medium | ✘ |
| `gjelsvik2005considering` | medium-term | 3 years | weekly, price sub-intervals | long | medium | ✘ |
| `gudbjerg2024exploring` | medium-term (2–3 years) | 4-year serial simulation | weekly, 3-hour | long | medium | ✘ |
| `hagenvik2022comprehensive` | MTM 104–208 weeks; STM | 2–4 years; 1 week | weekly; hourly deterministic | long; short | medium; short | ✘ (MTM) / ✔ (STM) |
| `schuller2024practical` | MTM 104–208 weeks; STM | 2–4 years; 1 week (10 days) | weekly, 3-hour; hourly deterministic | long; short | medium; short | ✘ (MTM) / ✔ (STM) |
| `helseth2022hydropower` | medium-term ("water values for producers") | 3 years | weekly, no intra-week steps | long | medium | ✘ |
| `helseth2024approximating` | long-term (LTS) | 3 years | weekly, 4-hour | long | long | ✔ |
| `helseth2025` (grey) | not checked | multi-year (156 weeks) | weekly, 1–8-hour steps | long | medium/long | ✘ |
| `rex2024hydropower` (grey) | ProdRisk + SHOP | 2–5 years; 1 week | weekly; hourly | long; short | medium ("long-term strategy" in the report); short | ✘ / ✔ |
| `lohndorf2019` | long-term (planning horizon 60 months because of multi-season reservoirs) | 120 months | monthly | long (5–10 years) | long | ✔ |
| `tilmant2008` | midterm (strategic) | 5 years | monthly | long | mid by label, long by the other papers | ✘ |
| `trezos1987use` | targets for the next echelon | 12 months | monthly | seasonal/long | medium | ~ |
| `he2026crossseasonal` | medium-to-long-term, cross-seasonal | 1 year | sub-daily (not stated) | seasonal/long | medium/long | ~ |
| `sauhats2016optimal` | investment, medium, short | 30 years; 15 days; 24 h | hourly | long/short | long/short | ✔ (three levels in one paper) |

### 3b. System models (price forecasting, expansion valuation)
| Source | Own label | Horizon | Stage / resolution | Lecture level | Paper's level | Agree |
|---|---|---|---|---|---|---|
| `helseth2013` | system scheduling; typical 3–5 years | 169 weeks (3.25 years) | weekly, sub-periods | long | long | ✔ |
| `helseth2015efficient` | 3–5 years typical | 156 weeks | weekly, 7 sub-periods | long | long | ✔ |
| `helseth2017` | long-term system (rolling) | 52-week look-ahead per weekly decision | weekly, 5 or 56 steps | seasonal/long | long | ~ |
| `henden2016economic` | EMPS | 2030 system, 47 weather years | weekly, 3-hour | long | long | ✔ |
| `warland2016stochastic` | EMPS, long-term (up to 25 years in general) | 3 years | weekly, 4 load periods | long | long | ✔ |
| `philpott2012` | long-term hydrothermal | 1 year | 52 weekly, 3 load blocks | seasonal/long | long | ~ |
| `pereira1991` | long-term | 10 stages (monthly, unverified) | monthly | ≤ 1 year | long | ~ |
| `dematos2015improving` | long-term | 10 years | monthly | beyond the lecture's 5 years | long | ✔ (level), horizon longer |
| `fullnerRebennack2025` (LTOP) | long-term | 5 years | monthly, 60 stages | long | long | ✔ |
| `scarcelli2017ensemble`, `stedinger1984stochastic`, `wu2018stochastic`, `kelman1990sampling` | long-term SDP, stationary or cyclic | infinite or annual cycle | monthly | long | long | ✔ |
| `dallinger2019socioeconomic` (system part) | target year | 2030, 1 year | hourly | seasonal/long | long (system) | ~ |

### 3c. Short-term and bidding models
| Source | Horizon | Resolution | Stochastic? | Lecture level | Agree |
|---|---|---|---|---|---|
| `belsnes2016applying` | 1 week (typical 1–2 weeks) | hourly | yes | short | ✔ horizon; ✘ the lecture says short-term models are deterministic |
| `aasgard2020value` | 72 h | hourly | yes | short | ✔ / ✘ (stochastic) |
| `chazarra2016stochastic` | 1 week (rolling, 24 h here-and-now) | hourly | yes | short | ✔ (Ahlfors would call it mid-term) |
| `chazarra2017`, `chazarra2018` | 1 day | hourly | no | short | ✔ |
| `diniz2008fourdimensional` | 1 week | hourly | no | short | ✔ |
| `faria2011day` | 1 day | hourly | yes | short | ✔ / ✘ |
| `naversen2020accounting` | 24 h | hourly | no | short | ✔ |
| `klaeboe2022day` | 4 days | hourly | yes | short | ✔ / ✘ |
| `boomsma2014bidding` | 1 day | hourly, 26 stages | yes | short | ✔ / ✘ |
| `seifert2025` | 3 days | 4-hour blocks | yes | short | ✔ / ✘ |
| `lohndorf2023` | 1 day | hourly | yes | short | ✔ / ✘ |
| `finnah2022integrated` | 30 days | hourly / quarter-hourly | yes | between short (1–2 weeks) and seasonal | ✘ |
| `deane2013derivation` | 1 year of daily runs with 6-day look-ahead | 6-, 2-, 1-hour | no | short runs over a year | ✔ |
| `dallinger2019socioeconomic` (owner part) | weekly with 2-week look-ahead | hourly, quarter-hourly | no | short | ✔ |
| `kong2020overview` | 1 day to 1 week | hourly | deterministic by scope | short | ✔ |

The lecture's short-term level is deterministic because that is industry practice (SHOP, DESSEM, the STM of Hagenvik and Schüller). The research papers above mostly make the short-term problem stochastic (bidding under price uncertainty), so "short-term = deterministic" describes the toolchain, not the literature.

### 3d. Storage valuation outside the hierarchy
These optimise an hourly year (or a window of it) with known prices and no water value passed from a longer model, so they sit at the short-term level in resolution but have no level above them.
| Source | Horizon | Resolution | Comment |
|---|---|---|---|
| `sioshansi2009estimating` | two weeks at a time, 15-day horizon, years 2002–2007 | hourly, perfect foresight | the window plays the role of the lecture's short-term level; the carry-over value replaces a water value |
| `drury2011value` | two-week windows | hourly | as above |
| `byrne2016estimating` | month by month | hourly | |
| `bradbury2014economic`, `kloess2014bulk`, `nitsch2021economic`, `zhang2026unlocking`, `yu2017stochastic` | 1 year | hourly, perfect foresight (Yu: stochastic dispatch) | |
| `naval2025optimization` | 1 year in 12 linked months | hourly | |
| `zisos2023mixing` | 20 years | hourly simulation | |
| `sepulveda2021design`, `jacobson2023computationally`, `kaut2024`, `hummelen2025exploring` | capacity expansion, 1 year to several periods | hourly or representative weeks | investment models, above the hierarchy |

## 4. What this means for us
1. **Our model is medium-term scheduling in the literature's terms.** One year or more of weekly stages, water values (or cuts) as the output, hourly decisions inside the week, prices and inflow uncertain between weeks: this is the ProdRisk level, which Helseth 2016, Hjelmeland, Schüller, Alic and Schäffer all call medium-term. By the lecture's numbers a one-year horizon sits on the boundary between seasonal (3–18 months) and long-term (1–5 years). Recommended wording: call the model a medium-term scheduling model and cite `helseth2016` (p. 936) or `gjelsvik2010` (p. 35) for the level; do not call it long-term scheduling, which the papers reserve for system models and price forecasting (EMPS).
2. **"Long-term" in our title refers to the storage, not the scheduling level.** Long-duration energy storage (LDES) is a property of the plant (hours to seasons of discharge); long-term scheduling is a model level (3–5 years). The brief's working statement says "the long-term operating value" of the plant; that phrase mixes the two and should be reworded (brief updated 2026-11-11 with a TODO).
3. **The lecture's slide 6 numbers should not be quoted in the thesis** unless the compendium is cited; the papers in §2 give different numbers, and `helseth2023hydropower` is the citable version of slide 7.
4. **For 5.3 (why stochastic) and 5.5 (pump sizing):** the storage-valuation papers in §3d have no water value above them, which is why their results for pumped storage (Sioshansi, Bradbury, Kloess) are short-term arbitrage values under known prices, not the value of a reservoir plant with inflow. This is a comparability caveat to state before any of their numbers.
5. **Research gap wording:** none of the medium-term producer studies in §3a treats adding a pump or its charging capacity (Alic adds a 38 MW pump; Ak converts a cascade; Gudbjerg and Schüller study existing pumped storage), and none varies price volatility and persistence; the studies that vary price behaviour (§3d) are short-term and deterministic.

## 5. Open points
- Q-005: whether to cite the lecture or the compendium at all (grey, non-peer-reviewed); the group decides.
- `bore2026` never names its level; our comparison table (Table 3) should give the horizon and stage length rather than a level word.
- `helseth2025` (grey) and `pereira1991` stage lengths are from the notes only (not re-read).
