---
bibkey: naversen2020accounting
bibkey_provisional: true
title: "Accounting for reserve capacity activation when scheduling a hydropower dominated system"
authors: "Christian Øyn Naversen, Hossein Farahmand, Arild Helseth"
year: 2020
venue: "International Journal of Electrical Power & Energy Systems, 119, 105864"
peer_reviewed: true
methods: [two-stage-stochastic, risk-averse-cvar, deterministic-lp-milp]
review_sections: [market-participation, modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Day-ahead hydro scheduling with symmetric spinning reserves on a 12-module Norwegian cascade: ignoring reserve activation (deterministic procurement) gives 7-8x higher expected balancing cost than two-stage stochastic/robust/hybrid models that check energy and storage availability for activation."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/16_Farahmand_2020_Stochastic_and_robust_optimization_approaches_for_reserve_procurement_bibliographic_mismatch.pdf"
---

# Reserve activation in hydro scheduling (Naversen, Farahmand & Helseth, 2020)

**Metadata note:** the inbox file name and the original source list say "Farahmand 2020, Stochastic and robust optimization approaches for reserve procurement". That title does not match the DOI. The DOI 10.1016/j.ijepes.2020.105864 and the PDF are this paper, first author **Naversen**. Key built from the real first author. Not in references.bib or Zotero yet.

## Research question / purpose
How much does it matter to represent the **activation** of reserved spinning capacity (not just its procurement) when scheduling a cascaded hydropower system, given that activation needs water upstream (up-regulation) and free storage space (down-regulation), and that changed releases propagate downstream (pp. 1–2)? The authors claim this was not addressed in detail before (p. 2). Contributions: (1) a new hybrid "mixed stochastic-robust" two-stage model; (2) quantification of the impact of accounting for activation in a cascade (p. 2).

## Setting
- **System:** a 12-module real Norwegian watercourse (cascade), total 537.4 MW (p. 6, Fig. 2). Several modules (1–3) sit in a string with very little storage between them (p. 9).
- **Perspective:** a **system operator** scheduling a fully renewable, hydro-dominated system (cost minimisation, not a price-taking producer) (p. 3).
- **Markets/products:** day-ahead schedule meeting forecast net load plus a static **symmetric spinning reserve** requirement R_t; no prices, no distinction between FCR/aFRR/mFRR ("the model does not distinguish between different types of reserves with different activation times", p. 4).
- **Horizon and resolution:** 24 h, hourly (p. 6). Net load profile from NO3 day-ahead volumes on 1 Jan 2019, scaled to 420 MW peak (p. 6).

## Method
- **Model type:** LP day-ahead scheduling problem (eqs. 2–16, p. 3): water balance with discharge, bypass and spill; piecewise-linear concave production curve (decreasing efficiency per segment, eq. 7); constant water values WV_m on end volumes; reserve bounds p + r ≤ P_max and p − r ≥ 0 (eqs. 9–10); system reserve requirement Σ r ≥ R_t (eq. 11). Linear, so production can go to 0 MW; symmetric reserve imposed to keep the reserve "spinning" (p. 3).
- **Second stage (balancing):** same constraints for balancing variables, net-load deviation ξ_t added to the power balance with load-shedding/dumping penalties; the only link to stage 1 is p̄ ∈ [p − r, p + r] (eqs. 17–21, p. 4). Activation lasts the whole hour (p. 4).
- **Uncertainty:** net-load forecast error ξ_t, i.i.d. truncated normal (μ = 0, σ = 16.8 MW, |ξ| ≤ 42 MW = 10 % of peak), no temporal correlation (p. 6).
- **Formulations compared:** deterministic (R_t = 42 MW); two-stage stochastic extensive form (eq. 22); two-stage robust with Bertsimas–Sim budget set Γ (eqs. 23–24), solved by **column-and-constraint generation** with a big-M MILP reformulation of the bilinear dual (eqs. 25–31, pp. 4–5); and the new **mixed model** (eq. 32): stochastic scenarios scaled by β plus the CCG worst-case scenarios as equiprobable extra scenarios with weight (1−β) (eqs. 33–35, p. 5).
- **Evaluation:** procurement cost K (increase of stage-1 cost vs. no-reserve schedule, eq. 36) and balancing cost B normalised by perfect foresight (eq. 37), simulated out of sample on 5000 normal and 5000 uniform (more extreme) deviations (p. 6). Pyomo + CPLEX 12.8 (p. 6).

## Data / case
Initial reservoirs 65 % (normal winter situation); water values 1200–9000 mu/Mm³ from the long-term model of Helseth et al. 2018 [19]; penalties 3000 mu/MW shedding, 1000 mu/MW dumping (p. 6).

## Key findings
- (p. 7) Robust model: Γ strongly drives K; higher Γ is not monotonically more robust; Γ = 15 best on 95th percentile.
- (pp. 7–8) Mixed model: best β ≈ 0.84–0.99; β = 1 (robust constraints without their cost in the objective) is clearly sub-optimal, because the stage coupling is weak and constraints alone barely move first-stage decisions (p. 6, p. 8).
- (p. 8, Table 1) Deterministic procurement: K = 0 but mean total cost 84.7 (normal batch) vs. ≈10–11 for stochastic/mixed, i.e. **7–8 times higher**; robust Γ = 15 is over-conservative (K = 28.8). Stochastic improves 50 → 200 → 1000 scenarios with diminishing returns; mixed model with only 12 extra robust scenarios matches or beats it on tail cost.
- (p. 9, Fig. 7) Deterministic model puts most reserve on plant 4 (bottom of the cascade, ample storage) by chance and allocates the rest arbitrarily; two-stage models coordinate spatially, e.g. reserve on low-storage modules 1–3 placed simultaneously so they ramp together.
- (p. 10) Conclusion: if activation is ignored, stored energy and free storage capacity can become binding in real time; future work: rolling-horizon over a season.

## Strengths
- Clean, reusable formulation of the activation problem: the only first/second-stage link is the reserve band around the schedule (eqs. 20–21).
- Out-of-sample evaluation against two different deviation distributions, including a misspecified (uniform) one.
- Real Norwegian cascade and SINTEF water values.

## Weaknesses / limitations
- System-operator cost minimisation, not producer profit; no reserve prices or activation payments.
- 24-hour horizon with constant water values; no pumping; symmetric reserves only; activation for full hours; no product distinction.
- i.i.d. deviations; solve times not reported (p. 5).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model limitations (06_mathematical_model, "Activation is not simulated") | Evidence that ignoring activation underestimates the cost of reserves; activation needs both upstream water and free storage | pp. 1–2 (intro), p. 8 Table 1, p. 10 conclusion |
| Literature review: market participation / reserves in hydro scheduling | Short survey of how reserves enter hydro models (Abgottspon 2014, Helseth 2016 ensure stored water for reserves but do not model activation; Chazarra 2016 assumes a fixed activation share) | pp. 1–2 |
| Modelling choice: storage margins for reserves | Formulation p − r ≥ 0, p + r ≤ P_max and the balancing band p̄ ∈ [p − r, p + r] | p. 3 eqs. 9–10, p. 4 eqs. 20–21 |
| Future work: two-stage activation model | Stochastic, robust (CCG) and mixed formulations; weight β tuning | pp. 4–5, Sec. 2.3–2.4; p. 7–8 |
| Evaluation design | Out-of-sample simulation on 5000 draws from a matching and a more extreme distribution | p. 6 |

## Useful quotes (with page numbers)
> "reserved capacity on hydropower plants should only be activated if there is sufficient energy or storage capacity" (p. 1, abstract)

## Follow-up references to check (backward snowballing)
- [1] Abgottspon et al. 2014 (risk-averse medium-term hydro with spinning reserves) — `abgottspon2014` already in papers/.
- [18] Helseth, Fodstad, Mo 2016 (medium-term hydro with energy and reserve capacity markets) — `helseth2016` already in papers/.
- [9] Chazarra et al. 2016 (weekly scheduling in day-ahead and secondary reserve markets) — `chazarra2016stochastic` already in papers/.
- [24] Kong & Skjelbred 2017 (post-spot distribution of reserve obligations).
- [8] Bruninx et al. 2016 (coupling pumped hydro storage with unit commitment; energy constraints for reserves).
- [35] Pandžić, Dvorkin, Carrión 2018 (merchant storage investment, energy vs. reserve markets).
- [33] Nasrolahpour et al. 2018 (bilevel storage participation in energy and reserve markets).

