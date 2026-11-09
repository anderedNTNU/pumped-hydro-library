---
bibkey: pitorac2020technical
bibkey_provisional: false
title: "Technical Review of Existing Norwegian Pumped Storage Plants"
authors: "Livia Pitorac, Kaspar Vereide, Leif Lia"
year: 2020
venue: "Energies 13(18), 4918 (MDPI), doi:10.3390/en13184918"
peer_reviewed: true
methods: [hydro-production-function]
review_sections: [phs-technology, ldes-seasonal-storage, reservoir-sizing-capacity]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/11_Web_search_2026-11-04/pitorac2020technical.pdf
takeaway: "Data review of all 10 Norwegian PSPs (1369 MW turbine, 997 MW pump, >5 TWh upper storage): all open-loop, built for seasonal pumping of flood inflow; Aurland III = 270/258 MW, 400 m head, 2 vertical RPTs at 500 rpm, upper 448 Mm3 (440 GWh) vs lower 10 Mm3 (10 GWh), i.e. ~1:45 reservoir ratio."
---

# Technical review of Norwegian pumped storage plants (Pitorac, Vereide & Lia, 2020)

_Energies 2020, 13, 4918, 20 pages; journal page = PDF page (pp. 1–20). The text extraction garbles Tables 2, 4 and 5 in `-layout` mode; values below were re-read with `pdftotext -raw`. Figures (map, tunnel layouts Fig. 6, efficiency curves Fig. 7) are images and could not be read; anything only in a figure is not in this note._

## Research question / purpose
First published technical review of the **ten existing pumped storage plants (PSPs) in Norway**, as a basis for future research (p. 1–3). Data come from owner questionnaires and interviews, unpublished design reports, as-built drawings and efficiency curves (p. 4). Covers energy production and storage, construction and specific costs, tunnel system layout and hydraulic transients, electromechanical equipment, start-up procedures, round-trip efficiency, and operational experience; ends with a discussion of trends in the European market (abstract, p. 1; p. 3).

## Setting
- **System:** all 10 Norwegian PSPs (Aurland III, Brattingfoss, Duge, Herva, Jukla, Nygard, Saurdal, Stølsdal, Tevla, Øljusjøen), all in Central and West Norway (p. 3).
- **Markets:** not modelled. Qualitative remarks on Nordic market, reserves and price spreads (p. 4, 17–18).
- **Horizon and resolution:** not applicable (descriptive review; cost figures in "today's prices", ~2020).

## Method
- **Model type:** descriptive technical/economic review; no optimisation.
- **How uncertainty is represented:** none.
- **Cost estimation:** construction costs recomputed in today's prices with NVE's national cost base for hydropower [33] (p. 6). Specific cost per stored kWh uses the **upper** reservoir energy and ignores the lower-reservoir limit, justified by natural inflow to both reservoirs (p. 6). Costs ignore the open-loop net production and the value to downstream cascades (p. 6).
- **Round-trip efficiency calculation (p. 12–13):** waterway head loss via Manning–Strickler M = 33 (unlined tunnels) and M = 85 (steel-lined penstocks); generator-motor 98 % and transformer 99 % assumed; real (anonymised) turbine/pump curves; operation at full capacity assumed (conservative, largest head loss).

## Data / case

### Table 1 (p. 5): the ten Norwegian PSPs
| Plant | Turbine MW | Pump MW | Gross prod. GWh/yr | Pump cons. GWh/yr | Net prod. GWh/yr | Gross head m | Commissioned |
|---|---|---|---|---|---|---|---|
| **Aurland III** | **270** | **258** | **350** | **280** | **70** | **400** | **1979** |
| Brattingfoss | 11 | 11 | 33 | 3 | 30 | 118 | 1955 |
| Duge | 200 | 170 | 303 | 55 | 248 | 220 | 1979 |
| Herva | 35 | 31 | 142 | 24 | 118 | 257 | 1962 |
| Jukla | 40 | 41 | 76 | 22 | 54 | 230 | 1974 |
| Nygard | 57.5 | 52 | 138 | 49 | 89 | 450 | 2005 |
| Saurdal | 640 | 320 | 1285 | 333 | 952 | 465 | 1985 |
| Stølsdal | 17 | 6 | 61 | 10 | 51 | 103 | 1986 |
| Tevla | 50 | 42 | 125 | 18 | 107 | 164 | 1994 |
| Øljusjøen | 49 | 39 | 78 | 50 | 42¹ | 212 | 1974 |
| Sum | 1369 | 997 | 2591 | 844 | 1761 | – | – |

¹ Øljusjøen's upper reservoir also feeds Borgund HPP, so gross ≠ net + consumption (p. 5).

### Table 2 (p. 5): energy storage
The third column of each block is printed as "10³ GWh/MW", but the values match **hours of full-capacity operation** (mean of the column 21,678/10 ≈ 2168 h ≈ 90 days and 5391/10 ≈ 539 h ≈ 22 days, exactly the "over 90 days" and "22 days" stated in the text, p. 5). The header is a typo; read as hours (our inference).

| Plant | Upper Mm³ | Upper GWh | Upper h | Lower Mm³ | Lower GWh | Lower h |
|---|---|---|---|---|---|---|
| **Aurland III** | **448** | **440** | **1556** | **10** | **10** | **36** |
| Brattingfoss | 107 | 31 | 2480 | 8 | 2 | 218 |
| Duge | 1398 | 755 | 3879 | 926 | 500 | 2570 |
| Herva | 109 | 69 | 1747 | 22 | 14 | 389 |
| Jukla | 236 | 116 | 2124 | 31 | 15 | 272 |
| Nygard | 103 | 114 | 1715 | 43 | 47 | 761 |
| Saurdal | 3105 | 3331 | 4978 | 230 | 247 | 737 |
| Stølsdal | 2.4 | 1 | 31 | 1 | 0.5 | 37 |
| Tevla | 204 | 82 | 1650 | 5 | 2 | 43 |
| Øljusjøen | 161 | 84 | 1518 | 27 | 14 | 328 |
| Sum | 5873 | 5023 | 21,678 | 1303 | 851 | 5391 |

### Table 3 (p. 6): construction and specific costs (EUR, today's prices)
Aurland III 212 M€, 787 €/kW, 0.51 €/kWh · Brattingfoss 30, 2834, 1.14 · Duge 300, 1501, 0.39 · Herva 60, 1721, 0.99 · Jukla 146, 3654, 1.72 · Nygard 41, 739, 0.43 · Saurdal 995, 1555, 0.31 · Stølsdal 64, 3760, 121.6 · Tevla 103, 2079, 1.25 · Øljusjøen 79, 1612, 1.06. (Currency symbol is € in the PDF; dropped in `paper.txt`.)

### Tables 4–5 (p. 11): electromechanical equipment
| Plant | Units | Pump start-up | Start time | Generator MVA / MW | Motor MVA / MW | rpm | Transformer kV |
|---|---|---|---|---|---|---|---|
| **Aurland III** | **2 vertical RPT** | **In air with an 11.4 MVA frequency converter** | **9 min** | **2×150 / 2×135** | **2×150 / 2×126** | **500** | **420/15.5** |
| Brattingfoss | 1 horiz. Francis + 1 pump | In air, mechanical back-to-back | N.A. | 14 / 11 | 14 / 10.6 | 428 | 66/6.3 |
| Duge | 2 vertical RPT | In air, 5 MW pony motor | 15 min | 2×120 / 2×100 | 2×106 / 2×85 | 375 | 320/13 |
| Herva | 1 horiz. unit, 2 runners + 1 motor-generator | Mechanical back-to-back | 10 min (first hours) | 45 / 35 | 32 / 31 | 500 | 132/8 |
| Jukla | 1 vertical RPT | Pony motor 4.3 MVA | 11 min | 44 / 40 | 48 / 41 | 500/375 | 67/12 |
| Nygard | 1 vertical RPT | In air, frequency converter | 6.5 min | 65 / 57.5 | 65 / 52.3 | 750 | 300/11.4 |
| Saurdal | 2 vertical Francis + 2 vertical RPT | Electrical back-to-back | 7 min | 4×185 / 4×160 | 2×185 / 2×160 | 428 | 324/18.5 |
| Stølsdal | 1 Francis + 2 pumps | Direct start | N.A. | 20 / 17 | N.A. / 2×3 | 375 | 300/6.6 |
| Tevla | 2 vertical RPT | In air, frequency converter | N.A. | 2×30 / 2×24.8 | 2×30 / 2×21.1 | 500 | 132/8.8/4.4 |
| Øljusjøen | 1 vertical RPT | Direct start | 3 min | 55 / 49 | 50 / 38.6 | 428 | 300/7 |

### Everything the paper says about Aurland III (our case plant)
- **Capacity:** 270 MW turbine, **258 MW pump** (Table 1, p. 5). Table 5 gives motor consumption **2 × 126 MW = 252 MW** (p. 11): a 6 MW inconsistency between the two tables (not explained).
- **Units:** **2 vertical reversible pump-turbines (RPTs)** (Table 4, p. 11; also p. 18 list of RPT plants). Generator rating 2 × 150 MVA / 2 × 135 MW; motor 2 × 150 MVA / 2 × 126 MW (Table 5).
- **Speed / fixed vs variable speed:** a single synchronous speed of **500 rpm** is listed (Table 5). The paper never says Aurland III is variable-speed; the frequency converter (11.4 MVA, ≈ 4 % of 2 × 150 MVA) is described only as a **start-up** device for pumping mode (Table 4; p. 16). So Aurland III is, by all evidence in this paper, a **fixed-speed** plant (our inference; not stated in those words). Implication: pumping power is essentially on/off per unit (no continuous pump-power regulation), which matters for how we model pumping (binary or fixed-block pumping, or a relaxation).
- **Start-up:** pumping start "in air with an 11.4 MVA frequency converter", **9 min** (Table 4, p. 11). Upgraded in **2016–2017**: previously a **direct start at half nominal voltage** via two coupling windings in the transformer, which strained the equipment; now a frequency converter (p. 16, ref. [40]). **The two units are not started in pumping mode at the same time** (company decision to avoid failure risk) (p. 16). Plants with start-up below 10 min can provide tertiary reserves (mFRR) (p. 13), so Aurland III (9 min) qualifies on this criterion.
- **Head:** gross head **400 m** (Table 1).
- **Energy:** gross annual production **350 GWh**, pumping consumption **280 GWh**, net **70 GWh** per year (Table 1). Pumping consumption ≈ 80 % of gross production, by far the highest pump share of the ten plants: Aurland III is the most "pumping-intensive" Norwegian PSP.
- **Reservoirs:** upper **448 Mm³ = 440 GWh**, ≈ **1556 h** (≈ 65 days) of full-capacity operation; lower **10 Mm³ = 10 GWh**, ≈ **36 h** (≈ 1.5 days) (Table 2, p. 5). Upper:lower ≈ **1:45** (p. 17; "For Aurland III and Tevla PSPs, the proportion between the two reservoirs is around 1 to 45"). Reservoir names are not given in the text (possibly in Fig. 6, not readable).
- **Energy equivalents implied:** 440 GWh / 448 Mm³ ≈ 0.98 kWh/m³ upper; 10 GWh / 10 Mm³ ≈ 1.0 kWh/m³ (our arithmetic, consistent with ~400 m head).
- **Flow:** **no turbine or pump discharge is given for Aurland III** in this paper. (Our thesis uses 56 m³/s pump flow from Hafslund; not verifiable here.)
- **Seasonal storage:** like all ten plants, designed for **seasonal pumping of inflow during spring and autumn high-flow seasons** to the large upper reservoir (p. 4, 13, 17). The 1:45 ratio "demonstrates that the main purpose of the pumping in most of the schemes is to pump inflow and not water stored in the downstream reservoir" (p. 17). Seasonal storage is therefore delivered by the **upper** reservoir fed by pumped lower-reservoir **inflow**; the lower reservoir itself only holds ~36 h of full-load pumping.
- **Cost:** 212 M€ (today's prices), 787 €/kW, 0.51 €/kWh stored (Table 3, p. 6).
- **Round-trip efficiency:** not reported per plant; all ten lie in **65–80 %** (p. 12, 13). Efficiency curves are anonymised (Fig. 7).

## Key findings
- (p. 2, 5, 17) Norway has only 10 PSPs, **1369 MW** turbine and **997 MW** pump capacity; gross 2.6 TWh, pumping 0.8 TWh, net ≈ 1.8 TWh per year; Norway is 10th in Europe in PSP capacity (p. 3).
- (p. 5, 17, 18) **All are open-loop** with significant natural inflow; net production positive in all cases; they operate "primarily as a normal hydropower plant with shorter periods of pumping" (p. 18).
- (p. 5) Upper reservoirs >5 TWh in total vs 0.85 TWh lower; on average >90 days to fill the upper and 22 days to fill the lower at full capacity.
- (p. 4, 17) All were designed for **seasonal storage / pumping of flood inflow**, not system services or daily peaks, because the hydro-dominated system already had ample energy and reserves (so reserve prices were low) and because large reservoirs sit on plateaus at the top of catchments. No short-term PSPs exist (p. 4).
- (p. 17) "most of the schemes have sufficient size of the lower reservoir to also allow daily and weekly pumping of stored water to profit from variations in the power prices."
- (p. 6–7, 17) Specific costs low per kW and very low per stored kWh vs international figures, owing to topography; cost per kWh falls with upper-reservoir size (logarithmic) and head (almost linear; roughly halved from 200 m to 400 m head) (Fig. 2, p. 6).
- (p. 12–13, 18) Round-trip efficiency **65–80 %**; waterway losses <1 % (Nygard) to 15 % (Duge); electromechanical losses 20–25 % round trip; turbine BEP 90.4–93.5 %, pump BEP 87.4–90.8 % (7 of the RPTs/pumps known).
- (p. 10, 18) 7 of 10 plants use RPTs; 5 start-up procedures; most start pumps in air; start-up from 6.5 min to a few hours, 2.3 min for upgraded ones (p. 13); 5 of 7 known start below 10 min → can deliver tertiary reserves (p. 13).
- (p. 18) Operation is shifting from seasonal pumping towards **more frequent start–stop**; "Pumping during nighttime and no operation during daytime is becoming more frequent." Upgrading start mechanisms becomes attractive as price spreads widen and system services are priced higher.
- (p. 13–14) Duge: pump needs a minimum head, so only the upper intake is used in pumping at low upstream level; lower-reservoir pumping limit changed from 655 to 650 masl, causing sand/debris problems (p. 16). Jukla can run at 500 or 375 rpm by short-circuiting poles (two-speed) (p. 14).
- (p. 16, 18) Tunnel collapses in 3 of 10 plants; two may relate to cyclic pressure from pumping.
- (p. 17) Potential >60,000 MW of PSP in Norway identified in earlier studies [18]; new PSPs between existing reservoirs could be cheaper.

## Strengths
- Unique, previously unpublished owner data for every Norwegian PSP, in consistent tables (p. 1).
- Authoritative source (NTNU hydraulic engineering group, co-author from Sira-Kvina) and open access.

## Weaknesses / limitations
- Descriptive only; costs are re-estimates from a national cost base, not actual historical costs (p. 6).
- Several table inconsistencies: "10³ GWh/MW" header (values are hours); Aurland pump capacity 258 MW (Table 1) vs 2 × 126 MW (Table 5).
- No per-plant round-trip efficiency or discharge data; efficiency curves anonymised.
- Some figures in the PDF carry leftover headers from another MDPI template ("Int. J. Environ. Res. Public Health"), a production artefact.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.3 Aurland 3: capacity, head, year, production | 270 MW / 258 MW pump, 400 m, 1979, 350 GWh gross, 280 GWh pumping, 70 GWh net | Table 1, p. 5 |
| Background 2.3 Aurland 3: reservoirs | Upper 448 Mm³ (440 GWh, ≈1556 h), lower 10 Mm³ (10 GWh, ≈36 h); ratio ≈1:45 | Table 2, p. 5; p. 17 |
| Background 2.3 Aurland 3: machines, fixed speed, start-up | 2 vertical RPTs, 500 rpm, 2×150 MVA; 11.4 MVA start-up converter, 9 min; upgrade 2016–17; units not started together | Tables 4–5, p. 11; p. 16 |
| Model data: case parameters | As above; cost 212 M€, 787 €/kW, 0.51 €/kWh | Tables 1–3, pp. 5–6 |
| Background 2.2 PHS technology: round-trip efficiency | 65–80 % for Norwegian PSPs; turbine BEP 90.4–93.5 %, pump BEP 87.4–90.8 % | pp. 12–13, 18 |
| Background 2.2: open-loop vs closed-loop, seasonal design | All Norwegian PSPs open-loop, seasonal pumping of flood inflow | pp. 4, 5, 17, 18 |
| Background 2.1 LDES: seasonal PHS in Norway | >5 TWh upper storage in 10 PSPs, >90 days to fill at full power | p. 5; p. 18 |
| Background 2.4 reserves: start-up time and mFRR | Start-up <10 min → tertiary reserves; slow start limits FCR/aFRR (Herva) | pp. 13, 16 |
| Lit. review 5.5 sizing: cost vs reservoir size and head | Specific cost falls with upper-reservoir size and head | Fig. 2, p. 6 |
| Motivation: shift towards short-term operation | More start–stop, night pumping; upgrades attractive with larger spreads | pp. 18 |
| Background: Norwegian PSP capacity in Europe | 1369 MW, 10th in Europe; Europe 55 GW PHS | p. 3, 5 |

## Useful quotes (with page numbers)
> "For Aurland III and Tevla PSPs, the proportion between the two reservoirs is around 1 to 45." (p. 17)

> "Pumping during nighttime and no operation during daytime is becoming more frequent." (p. 18)

## Follow-up references to check (backward snowballing)
- [17] Lia, Vereide, Strypet & Kvaal (2016), Hydro 2016: new strategy for PSP in Norway, medium-sized projects in existing schemes.
- [18] Charmasson et al. (2017), CEDREN roadmap for large-scale balancing and storage from Norwegian hydropower.
- [19] NVE (2011), *Pumpekraft i Norge*.
- [27] Solvang et al. (2014), SINTEF: Norwegian hydropower for large-scale electricity balancing.
- [40] Breiland (2019), USN thesis on reconstruction of Duge (cited for the Aurland start-up upgrade).
- [7] Deane et al. (2010), techno-economic review of PHS; [8] Hunt et al. (2020), global seasonal PHS potential.

