# Wanted: sources still missing (web search 2026-11-04)

Found by a quick web search aimed at the gaps the notes pointed to. **None of these is filed yet.** "Mentioned in N notes" means existing notes already cite it, which is a strong sign it matters.
To add one: download the PDF → `literature/inbox/<key>.pdf` → "process the inbox".

## Status 2026-11-04
**Filed:** pitorac2020technical, dimoski2018hydropower, boomsma2014bidding, hagenvik2022comprehensive, haldrup2006regime, gimeno2015assessment, solvang2014norwegian. **Already in the repo** (inside `hjelmeland2019phd`): both Hjelmeland 2016 papers. **Still wanted (NTNU access):** Dallinger 2019 (https://doi.org/10.1016/j.rser.2019.03.027) and Helseth et al. 2015, PowerTech (https://doi.org/10.1109/PTC.2015.7232252). Fleten, Seim & Thorsnes 2010 could not be found and has been dropped.

## Priority 1: directly relevant to our model or gap
| Paper | Why | Where to get it |
|---|---|---|
| Hjelmeland, Korpås & Helseth (2016). *Combined SDDP and simulator model for hydropower scheduling with sales of capacity*. EEM 2016. DOI 10.1109/EEM.2016.7521187. Plus the companion Energy Procedia case study (2016) | SDDP with reserve-capacity sales. The simulator shows a 40% lower capacity profit than the strategy model, which is the original source for our LP reserve-overestimation limitation. Mentioned in 5 notes | IEEE Xplore (NTNU); also in [Hjelmeland PhD](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2597127) |
| Dimoski, Nersten, Fleten & Löhndorf (2018). *Hydropower reservoir management using multi-factor price model and correlation between price and local inflow* | Joint price–inflow modelling with a weekly lattice and ADDP, the same family as our model. Kleiven 2023 builds on it | [NTNU Open](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2582011) (free) |
| Boomsma, Juul & Fleten (2014). *Bidding in sequential electricity markets: The Nordic case*. EJOR 238(3), 797–809 | The classic Nordic DA + balancing multistage bidding paper (coordination gain). Mentioned in 5 notes | [NTNU Open](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2461546) (free) |
| Hågenvik et al. (2022). *A comprehensive simulator for hydropower investment decisions*. PMAPS 2022 | The ProdRisk–SHOP investment simulator behind `schuller2024practical` and `rex2024hydropower`; the Norwegian method for valuing upgrades and pumps. Mentioned in 4 notes | [SINTEF](https://sintef.brage.unit.no/sintef-xmlui/handle/11250/3007499) |
| Pitorac, Vereide & Lia (2020). *Technical review of existing Norwegian pumped storage plants*. Energies 13, 4918 | All 10 Norwegian PHS plants, ~1400 MW, several seasonal. **Likely has Aurland 3 data.** Mentioned in 3 notes | [MDPI, open access](https://www.mdpi.com/1996-1073/13/18/4918) |

## Priority 2: strengthens background or discussion
| Paper | Why | Where |
|---|---|---|
| Dallinger, Schwabeneder, Lettner & Auer (2019). *Socio-economic benefit and profitability analyses of Austrian hydro storage power plants…* RSER 107, 482–496 | PHS profitability including reserves, Central Europe | [TU Wien repository](https://repositum.tuwien.at/handle/20.500.12708/143284) |
| Gimeno-Gutiérrez & Lacal-Arántegui (2015). *Assessment of the European potential for pumped hydropower energy storage based on two existing reservoirs*. Renew. Energy 75, 856–868 | European PHS potential (29 TWh realisable); a standard background citation. Mentioned in 3 notes | [CORE](https://core.ac.uk/download/32322978.pdf) (free) |
| Solvang et al. (CEDREN). *Increasing balance power capacity in Norwegian hydroelectric power stations* | ~20 GW of extra Norwegian balancing capacity possible; PHS case studies. Mentioned in 2 notes | [CORE](https://core.ac.uk/download/249959331.pdf) (free) |
| Fleten, Seim & Thorsnes (2010), IEEE | Dependent vs independent price–inflow modelling costs 2–4% revenue for 3 Norwegian producers | IEEE Xplore (NTNU) |

## Priority 3: price volatility (thin academically)
| Paper | Why | Where |
|---|---|---|
| Haldrup & Nielsen (2004/2006). *A regime switching long memory model for electricity prices* (Nordic) | Regime switching and persistence in Nordic prices, which justifies discrete Markov price states | [Aarhus working paper](https://repec.econ.au.dk/repec/afn/wp/04/wp04_02.pdf) (free) |
| Markov regime-switching / MS-GARCH Nordic price papers (e.g. *Risks* 13(3), 58, 2025) | Recent evidence on regimes in Nordic prices | [MDPI](https://www.mdpi.com/2227-9091/13/3/58); verify the authors first |

## Deterministic LP storage models for price-taking profit maximisation (web search 2026-11-05)
These are precedents for our weekly LP. None found so far combines an LP, pumped hydro, several markets and a weekly horizon.

**Status 2026-11-05:**
- **Filed** with provisional keys: `sioshansi2009estimating`, `bradbury2014economic`, `kloess2014bulk`, `byrne2016estimating`. All still need to be added to Zotero.
- **Still wanted:** Connolly et al. (2011). The CORE/VBN file holds only the figure correction; the full text needs NTNU access, https://doi.org/10.1016/j.enpol.2011.04.032.
- **New leads from snowballing:** Walawalkar, Apt & Mancini (2007), Energy Policy 35, 2558–2568 (arbitrage + regulation, New York).

| Paper | Why | Where |
|---|---|---|
| Sioshansi, Denholm, Jenkin & Weiss (2009). *Estimating the value of electricity storage in PJM: Arbitrage and some welfare effects*. Energy Economics 31(2), 269–277 | **Verified from the author PDF:** price-taking storage as an **LP** with perfect foresight, hourly, **two weeks at a time with a 15-day horizon** so stored energy keeps carry-over value; device modelled on pumped storage (80 % round trip, Bath County PHS); energy arbitrage only; varies hours of storage (8 h ≈ 85 %, 20 h ≈ 95 % of the value, p. 3). The closest LP precedent for our weekly model and for the end-of-horizon problem | [author PDF](https://www.cmu.edu/ceic/people/rsioshan/docs/pjm_arbitrage.pdf) (free) |
| Bradbury, Pratson & Patiño-Echeverri (2014). *Economic viability of energy storage systems based on price arbitrage potential in real-time U.S. electricity markets*. Applied Energy 114, 512–519 | Linear optimisation of power and energy capacity for 14 storage technologies including PHS (optimal ~7–8 h for PHS, per abstract); real-time arbitrage only. A sizing precedent (unverified beyond the abstract) | [RePEc](https://ideas.repec.org/a/eee/appene/v114y2014icp512-519.html); DOI 10.1016/j.apenergy.2013.10.010 (NTNU access) |
| Byrne, Concepcion & Silva-Monroy (2016). *Estimating potential revenue from electrical energy storage in PJM*. IEEE PES GM (Sandia SAND2016-1080C) | **Verified from the PDF:** LP for maximum revenue from **arbitrage + regulation** in day-ahead markets (PJM 2014–2015); the device is a 20 MW flywheel, not PHS. A method precedent for energy + reserve co-optimisation as an LP | [Sandia PDF](https://www.sandia.gov/app/uploads/sites/163/2021/09/SAND2016-1080C.pdf) (free) |
| Connolly, Lund, Finn, Mathiesen & Leahy (2011). *Practical operation strategies for pumped hydroelectric energy storage (PHES) utilising electricity price arbitrage*. Energy Policy 39(7), 4189–4196 | PHES (360 MW pump, 300 MW turbine, 2 GWh) on 13 spot markets; day-ahead optimal strategy captures ~97 % of the perfect-foresight profit; annual profit varies by more than 50 %. Method (LP or algorithm) unverified | [CORE](https://core.ac.uk/download/60476934.pdf) (free) |
| Kloess & Zach (2014). *Bulk electricity storage technologies for load-leveling operation*. Int. J. Electr. Power Energy Syst., 111–122 | Economics of PHS vs CAES/H2/CH4 in the German–Austrian market; method unverified | DOI 10.1016/j.ijepes.2014.02.002 (NTNU access) |

## Aurland 3 data (for the case study)
- Not found on Hafslund's page. Try **NVE's Innsjødatabase** and the revision of terms for Aurlandsvassdraget (NVE case 201400584). Pitorac et al. (2020) above may also list it.
- The web sources disagree on capacity: 270 MW (Hafslund, Power Technology) vs 290 MW (GEM). Use Hafslund.
- Vetlebotnvatn is an intake reservoir with little seasonal storage. The main storage is Nyhellervatnet–Øljuvatnet–Kongshellervatnet ([lokalhistoriewiki](https://lokalhistoriewiki.no/wiki/Aurland_III_kraftverk); [NVE document](https://webfileservice.nve.no/API/PublishedFiles/Download/d26a4f04-e9da-4ad3-9652-9e9acd6a450e/201400584/3439802)).

## Cited in the group's drafts but not in the library (2026-11-10)
| Paper | Why | Status |
|---|---|---|
| McDermott (2020), cited in the 5.2 draft for Norwegian producers restricting production when their market position strengthens | Empirical support for price-making behaviour in Norway | Not in the library or in references.bib; the claim is **(unverified)** until the paper is filed |
| NVE (2025), *Langsiktig kraftmarkedsanalyse 2025* (LA25), and the data set *Timespriser for norske prisområder fra LA25* (published 2025-06-20) | Source of the simulated hourly prices (30 weather years, model years 2030–2050) proposed for the Markov states; needed in Zotero to cite the data | [NVE](https://www.nve.no/energi/analyser-og-statistikk/langsiktig-kraftmarkedsanalyse/langsiktig-kraftmarkedsanalyse-2025/) |
