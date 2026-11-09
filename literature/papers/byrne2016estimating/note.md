---
bibkey: byrne2016estimating
bibkey_provisional: true   # not yet in Zotero/references.bib; ask the group to add it
title: "Estimating potential revenue from electrical energy storage in PJM"
authors: "Raymond H. Byrne, Ricky J. Concepcion, César A. Silva-Monroy"
year: 2016
venue: "IEEE PES General Meeting 2016 (Sandia report SAND2016-1080C) (venue unverified)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [market-participation]
relevance: medium
read_by: []
added: 2026-11-05
takeaway: "Perfect-foresight LP (Pyomo, monthly runs) maximising day-ahead arbitrage plus PJM regulation revenue (capability + performance/mileage payments) for a 20 MW / 5 MWh flywheel; regulation capacity sold reduces the charge/discharge headroom available for arbitrage, and known historical activation fractions keep the state-of-charge balance linear; the optimum is regulation ~97 % of hours, and a simple heuristic captures 92.5 % of the LP upper bound."
---

# LP for arbitrage plus regulation revenue in PJM (Byrne et al., 2016)

_Four-page conference paper without journal pagination; "p." below means PDF page 1-4._

## Research question / purpose
How can the maximum potential revenue of a storage device that sells energy arbitrage and frequency regulation under PJM's pay-for-performance rules be computed as a best-case benchmark, and how close does an implementable strategy without foresight come (abstract, p. 1)?

## Setting
- **System:** a 20 MW / 5 MWh storage plant modelled after the Beacon Power Hazle Township flywheel plant; conversion efficiency 0.85, storage efficiency 0.98 per period, performance score 0.95 (Table II, p. 3).
- **Markets:** day-ahead energy (arbitrage) and the PJM regulation market (single RegUp/RegDown product) with capability (RMCCP) and performance (RMPCP × mileage ratio) payments (pp. 1-2).
- **Horizon and resolution:** June 2014-May 2015, hourly, optimised month by month (p. 3).

## Method
- **Model type:** LP (Pyomo). Objective: arbitrage revenue minus charge/discharge costs plus regulation capability and performance payments (Eq. 15, p. 2). Constraints: state of charge with storage and conversion losses (Eq. 7); with regulation, the state of charge also moves with the activated share of regulation up and down (Eq. 11); energy bounds (Eq. 12); **regulation capacity plus charging, and regulation capacity plus discharging, must stay within the power limits** (Eqs. 13-14, p. 2).
- **How uncertainty is represented:** deterministic, perfect foresight of prices and of the regulation signal. The activated fractions of regulation up and down are taken from the historical 2-second PJM signal, so the balance stays linear (p. 2).
- **Key modelling choices and assumptions:** price-taker ("only valid for scenarios where the size of the storage is such that it does not impact market prices", p. 1); accepted regulation equals the bid; negligible ramp time; day-ahead price also used for real-time settlement of regulation energy (p. 3).

## Key findings
- (p. 3, Table III) The optimal policy sells regulation in about 96-99 % of hours; maximum potential revenue is about $6.4 M for the year, varying by month from about $0.34 M to $1.0 M.
- (p. 4, Table IV) Capability payments are about 75 % of revenue and mileage (performance) payments about 24 %; arbitrage is about 0.2 % and negative in most months because energy is bought to keep the state of charge needed for regulation.
- (p. 4) A simple heuristic (bid 20 MW every hour, stop when the state of charge is violated) captures 92.5 % of the LP upper bound.

## Strengths
- Clear LP formulation of joint energy and reserve participation for storage, with the headroom coupling between reserve capacity and charging/discharging, and with activation in the state-of-charge balance kept linear through known activation shares.
- Explicitly presents the perfect-foresight LP as an upper bound for scoring implementable strategies.

## Weaknesses / limitations
- A short-duration flywheel, not PHS; one year; perfect foresight of prices and the regulation signal.
- US pay-for-performance rules differ from Nordic aFRR/FCR products.
- Conference paper; the venue is taken from the Sandia report number and has not been verified.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review, markets: LP co-optimisation of energy and reserves for storage | Eqs. 11-15 | p. 2, Secs. III-IV |
| Model: reserve headroom constraint precedent | Regulation + charge/discharge ≤ power limit | p. 2, Eqs. 13-14 |
| Assumptions: perfect foresight as upper bound; heuristic gap | 92.5 % captured by heuristic | pp. 1, 4 |
| Assumptions: activation handled through known shares | Historical activation fractions keep the LP linear | p. 2 |

## Useful quotes (with page numbers)
> "The problem of maximizing revenue from an energy storage device is naturally formulated as an LP optimization problem" (p. 2)

## Follow-up references to check (backward snowballing)
- Byrne & Silva-Monroy (2012), *Estimating the maximum potential revenue for grid connected electricity storage: arbitrage and regulation*, SAND2012-3863 (CAISO).
- Byrne & Silva-Monroy (2014, 2015), ERCOT revenue studies, IEEE PES GM.
- Mokrian & Stephen (2006), *A stochastic programming framework for the valuation of electricity storage*, USAEE/IAEE.

