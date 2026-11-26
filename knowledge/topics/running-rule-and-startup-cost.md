# Running rule for reserves and linearised start-up cost, in our symbols

Added 2026-11-26 (Anders' question). What has to be added to the weekly model in ch. 6 to include (A) the running rule for reserves from `helseth2016` and (B) the linearised start-up cost from `helseth2013`. The equations were read from the PDFs, not from the text copies. Nothing here is in Overleaf or in the code yet (Q-010).

## A. Running rule for reserves

### What the source has (`helseth2016`, p. 938, eqs. (6), (7), (12), (13))

Per station h and time step k, with e generated energy [MWh], τ the step length [h], r the allocated reserve [MW]:

- (6) γ_h r_kh − e_kh/τ_k ≤ 0
- (7) r_kh + e_kh/τ_k ≤ P_h^max
- (12) 0 ≤ r_kh ≤ R_h^max
- (13) γ_h = max{ P_h^min / R_h^max , 1.0 }

The reserve r is one symmetric, spinning quantity per station. (6) is the spinning requirement; with γ_h from (13) the reserve cannot reach R^max before the station produces at least P^min. The paper says the model is *discouraged* from running below minimum output to deliver reserves, not prevented (p. 938). Example in the paper: P^min = 50 MW, R^max = 33 MW, γ = 50/33. The model has no pumps. The paper notes that the symmetric and spinning requirement can be relaxed with separate up and down variables and by omitting (6) (p. 939).

Correction: Sections 1 and 7A of `model-precedents.md` called the factor β. The paper's symbol is γ_h; β is our discount factor.

### In our symbols

New parameters:

| Symbol | Meaning | Unit |
|---|---|---|
| P^{G,min} | minimum output of the generating unit | MW |
| P^{P,min} | minimum pumping power of the pumping unit | MW |
| γ^G = max{P^{G,min}/R^{G,max}, 1} | factor limiting reserves from the generating unit | – |
| γ^P = max{P^{P,min}/R^{P,max}, 1} | factor limiting reserves from the pumping unit | – |

Constraints, for all t:

- γ^G Σ_f r^{G+}_{f,t} ≤ p^G_t (new)
- γ^G Σ_f r^{G−}_{f,t} ≤ p^G_t (replaces p^G_t − Σ_f r^{G−}_{f,t} ≥ 0 in `eq:unit`)
- γ^P Σ_f r^{P+}_{f,t} ≤ p^P_t (new)
- γ^P Σ_f r^{P−}_{f,t} ≤ p^P_t (replaces p^P_t − Σ_f r^{P−}_{f,t} ≥ 0 in `eq:unit`)

Unchanged: the upper limits in `eq:unit` (Helseth's (7)), `eq:unit_reserve_limits` (Helseth's (12); ours are already summed over products, so γ keeps its meaning with several products), the water margin in `eq:reservoir` (Helseth's (8)). No new variables, no change to the objective, no new state.

### What is Helseth's and what is ours

- Helseth's: the form of (6) and the definition (13), for a generating unit.
- Ours: (i) Helseth's r is one symmetric quantity, we have separate up and down variables, so (6) is applied to each direction; (ii) the pump. Helseth 2016 has no pump, so γ^P and the two pump constraints are the same rule applied by analogy. Whether the pump can deliver reserves at all depends on the machine type (Q-007).
- Effect to expect: today the turbine can sell up-regulation from standstill (p^G = 0, r^{G+} = R^{G,max}). With the rule it must run to sell reserves, which costs water in low-price hours. This is the effect Helseth reports (station 5 runs at its minimum output, Fig. 6, p. 941).
- Data needed: P^{G,min} and P^{P,min} for the case plant. Not in `duge.yaml` (unverified; not checked in this session).

## B. Linearised start-up cost

### What the source has (`helseth2013`, Sec. 2.4, p. 1428, eqs. (14)–(19); Sec. 3.3, p. 1430, eqs. (20)–(24))

For each pump j with a start-up cost and each sub-period k, with u the pumping variable:

- (14) P_j^min u_L + (P_j^max − P_j^min) u_H − u = 0
- (15) u_L − u_H ≥ 0
- (16) u_L^k − u_L^{k−1} − δ^k ≤ 0
- (17) 0 ≤ u_L ≤ 1
- (18) 0 ≤ u_H ≤ 1 (relaxed in practice, since u already has an upper limit)
- (19) cost term for one week: Σ_k Σ_j c_j^s δ_j^k

u_L is the per-unit pumping below minimum capacity (the operating state), u_H the per-unit pumping above it, δ the start-up variable. Generating units follow the same structure (p. 1428). u_L is a state variable because (16) couples it in time; at the end of the week it enters the cuts with the dual of (16) in the first sub-period of the next week as coefficient (eqs. (21)–(24)). The forward simulation starts from a given initial operating state (Sec. 3.1.1). The paper states that the approximation is not perfect: the pump runs below minimum part of the time (p. 1432–1433). The size of the start-up cost in case E is not given in the text. `helseth2016` p. 938 says start and stop costs could be included in that model as described in `helseth2013`.

### In our symbols

New parameters:

| Symbol | Meaning | Unit |
|---|---|---|
| P^{G,min}, P^{P,min} | as in A | MW |
| C^{S,G}, C^{S,P} | cost per start of the generating and the pumping unit | EUR |
| U^{G,in}, U^{P,in} | operating state of each unit at the start of week 1 | – |

New variables, for all t (proposed symbols, not in the glossary yet):

| Symbol | Meaning | Range |
|---|---|---|
| u^{G,L}_t, u^{P,L}_t | operating state: share of minimum power in use | [0, 1] |
| u^{G,H}_t, u^{P,H}_t | share of the range above minimum power in use | [0, 1] |
| σ^G_t, σ^P_t | start-up variable | ≥ 0 |

Constraints, for all t, for the pump (the generating unit is identical with G for P):

- P^{P,min} u^{P,L}_t + (P^{P,max} − P^{P,min}) u^{P,H}_t = p^P_t
- u^{P,L}_t ≥ u^{P,H}_t
- u^{P,L}_t − u^{P,L}_{t−1} ≤ σ^P_t
- 0 ≤ u^{P,L}_t ≤ 1, 0 ≤ u^{P,H}_t ≤ 1, σ^P_t ≥ 0

Objective: subtract Σ_t (C^{S,G} σ^G_t + C^{S,P} σ^P_t) from the weekly profit.

Non-negativity of the start-up variable is not written out in the paper; it is needed (otherwise a stop would give income).

### State between weeks (this is the part that changes the method)

- u^{G,L}_0 and u^{P,L}_0 are the values of u^{G,L}_T and u^{P,L}_T from the week before; in week 1 they are U^{G,in} and U^{P,in}.
- The state between weeks becomes (v, u^{G,L}, u^{P,L}) instead of v alone. F_{s,m} and Q_{s,m} get three arguments.
- Each cut gets two more slopes: α ≤ ẑ_ℓ + λ_ℓ (v_T − v̂_ℓ) + μ^G_ℓ (u^{G,L}_T − û^G_ℓ) + μ^P_ℓ (u^{P,L}_T − û^P_ℓ), where μ are the duals of the constraints that fix u^{G,L}_0 and u^{P,L}_0 in the next week, found the same way as λ from `eq:initial_state`.
- The problem stays a linear programme, so SDDP applies as before.
- Not Helseth's: setting u_0 to a fixed value every week to avoid the extra states. That would be our own simplification and charges or forgives a start at every week boundary.

### Together with A

Both use the same P^{G,min} and P^{P,min}. The constraints do not overlap: A limits reserves by scheduled power, B splits scheduled power into a part below and a part above minimum. `eq:unit` upper limits are unchanged.
