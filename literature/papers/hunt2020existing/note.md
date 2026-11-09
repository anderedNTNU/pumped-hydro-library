---
bibkey: hunt2020existing
bibkey_provisional: true
title: "Existing and new arrangements of pumped-hydro storage plants"
authors: "Hunt, Julian David; Zakeri, Behnam; Lopes, Rafael; Barbosa, Paulo Sérgio Franco; Nascimento, Andreas; de Castro, Nivalde José; Brandão, Roberto; Schneider, Paulo Smith; Wada, Yoshihide"
year: 2020
venue: "Renewable and Sustainable Energy Reviews 129, 109914 (doi:10.1016/j.rser.2020.109914)"
peer_reviewed: true
methods: []
review_sections: [phs-technology, ldes-seasonal-storage]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/03_Konfigurasjoner_og_potensial/Hunt2020Arrangements.pdf
takeaway: "Review/classification of PHS by storage cycle (hourly, daily, weekly, seasonal, pluri-annual; Saurdal, Norway, as pluri-annual example), turbine speed (fixed/variable/ternary/quaternary) and arrangement (open-loop, closed-loop, pump-back, run-of-river SPHS), plus new three-reservoir concepts; GIS case in the Zambezi basin finds only the combined short+long-cycle SPHS cheaper than a conventional dam for water storage."
---

# Existing and new arrangements of PHS plants (Hunt et al., 2020)

_Article-numbered paper; page numbers are the article's own pages 1–14 (= PDF pages). The PDF is the publisher's version hosted by a Brazilian research-project site (projetouhr.com.br). Several tables (1, 6, 7) are scrambled in the text extraction; values below were checked against the raw extraction where possible._

## Research question / purpose
Critically review existing types of pumped-hydro storage plants (advantages and drawbacks), and propose new arrangements that make large-scale reservoirs for **long-term energy and water storage** possible in flat or arid regions; compare some of them in a case study for the upper Zambezi basin (p. 1).

## Setting
- **System:** review (global examples) + GIS case study for the upper Zambezi basin (Angola, Zambia; flat topography, high evaporation) (pp. 9–12).
- **Markets:** none modelled. Uses for PHS listed qualitatively (Table 3, p. 5), including reducing price fluctuations.
- **Horizon and resolution:** not applicable (no operational model).

## Method
- **Model type:** narrative review and classification (Sec. 2); conceptual design of new arrangements (Sec. 3); GIS siting and cost comparison with the authors' Python module using SRTM 90 m DEM, sizing reservoirs to store ≈ 50% of available flow; hydrology, component design and costs from refs [85]–[88], method in ref. [23] (p. 10).
- **How uncertainty is represented:** none.
- **Key classifications (Sec. 2):**
  - **By storage cycle (Table 1, p. 3):** typical reservoir volume — pluri-annual (PAPHS) 100–5 km³; seasonal (SPHS) 30–1 km³; weekly (WPHS) 5–0.1 km³; daily (DPHS) 1–0.001 km³; hourly (HPHS) 1–0.001 km³, with the occasions when each pumps and generates (e.g. seasonal: pump in wet/melt seasons, summer solar, low-demand season; generate in dry/freezing winters, low solar, high-demand season).
  - **Examples (p. 2):** hourly = Kops II (Austria, ancillary services, > 100 reversions/day in short-circuit mode); daily = Goldisthal (Germany); weekly = La Muela (Spain); seasonal = Limberg (Austria); **pluri-annual = Saurdal (Norway)**. Countries already combining energy and water storage with PHS: Austria, Switzerland, **Norway** (p. 2).
  - **Seasonal PHS layout (p. 2, Fig. 2):** small lower reservoir (≈ month-long storage), large upper reservoir with level variation up to 250 m, tunnel and pump-turbine; can combine daily, weekly and yearly cycles (p. 3).
  - **By turbine speed (Sec. 2.2, p. 3):** fixed vs variable speed (variable ≈ 30% more expensive; e.g. 60–100 MW range for a 100 MW unit; better efficiency over large head variation); ternary (Pelton + Francis pump, fast mode switch); quaternary (separate pump and turbine with hydraulic short circuit, e.g. Gordon Butte 134 MW, switching ≈ 20 MW/s) (pp. 3–4).
  - **Head variation (Table 2, p. 4):** Nant de Drance 250–390 m (35.9%), Linthal 560–724 m (22.7%), Tehri 127–221 m (42.5%), Limberg II 273–432 m (36.8%). The paper assumes a **maximum 50% head variation** for SPHS design (p. 3, p. 7).
  - **By arrangement (Sec. 2.4, pp. 4–6, Fig. 4):** open-loop (significant natural inflow, often using an existing dam as lower reservoir, e.g. Seneca, USA); closed-loop (limited inflow, "usually limited to daily or weekly storage cycles", e.g. Marmora, Canada); **pump-back** (pump-turbines in a dam with another reservoir immediately downstream; usually low head, e.g. Kannagawa, Japan); run-of-river SPHS (Malta, Austria; Fig. 5).
- **New arrangements (Sec. 3, pp. 6–10):** CCSPHS (combined short- and long-cycle SPHS, three reservoirs so head variation can exceed 50%, Fig. 6); CHPHS (combined hydropower and PHS on the same pump-turbine, Fig. 7, Tables 4–5 with operating schemes A–C).

## Data / case
Six proposed projects in the Zambezi basin (Lungue, Cuando, Calunda, Sakafwapu, Mukwato, Luangwa; Table 6, p. 10 — table columns scrambled in extraction, values not reproduced here). Solar irradiation up to 2,300 kWh/m²/yr; few sites with wind > 7 m/s (p. 10, Fig. 9).

## Key findings
- (p. 1) "Currently most pumped-hydro storage (PHS) plants only store energy in daily storage cycles", which may not be competitive in the future because battery costs are falling; future PHS should serve both short- and long-term energy needs and water storage (p. 12).
- (p. 2) "The larger the upper reservoir storage size the higher the operational flexibility of the plant"; a large reservoir can provide the services of a small one and more.
- (p. 3) SPHS can be operated with a combination of daily, weekly and yearly cycles, for peak generation, ancillary services, VRE storage, hydropower optimisation and water supply.
- (pp. 5–6) Pump-back increases flexibility: in a drought, conventional generation falls but the plant can still act as pumped storage.
- (p. 5, Table 3) Seasonal storage argument for **high-latitude countries**: seasonal solar profile, heating demand in winter, and further winter demand growth with electrification of heating; peak national demand can be two to three times minimum demand.
- (p. 12) Zambezi: water storage cost Cuando conventional reservoir dam **0.014 US$/m³** vs Cuando CCSPHS **0.008 US$/m³**; CCSPHS with 600 MW better than with 103 MW because the turbine earns both energy and water revenue; for the other sites a conventional dam is cheaper (low head; Calunda needs a 23 km tunnel). Only CCSPHS proved competitive.
- (p. 12) "the topography will remain the main decision driver for future PHS projects".

## Strengths
- Clear taxonomy of PHS by storage cycle, machine type and hydraulic arrangement, with named examples (including Norway).
- Explicitly treats seasonal and pluri-annual PHS as categories and links them to water management.
- Head-variation data for real plants (Table 2) useful for discussing head effects.

## Weaknesses / limitations
- Mostly qualitative; no operational or market model; Zambezi costs depend on the authors' GIS method (refs [23], [85]) and are not detailed here.
- Table 1 reservoir-size ranges overlap (daily and hourly identical, 1–0.001 km³) and are indicative only; the source of the categorisation is ref. [13].
- Tables 6 and 7 are hard to read in the PDF text; claims about specific Zambezi project parameters should be checked against the PDF image.
- Some statements (e.g. variable speed ≈ 30% more expensive) rest on single references.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.2: classification of PHS by storage cycle | Hourly / daily / weekly / seasonal / pluri-annual, reservoir volumes, operating occasions | Table 1 p. 3; p. 2 |
| Background 2.2: Norwegian examples | Saurdal = pluri-annual PHS; Norway combines water and energy storage | p. 2 |
| Background 2.2: open-loop / closed-loop / pump-back definitions | Definitions, examples, closed-loop limited to daily/weekly | Sec. 2.4, pp. 4–6, Fig. 4 |
| Background 2.2: fixed vs variable speed, ternary, quaternary | Characteristics, cost premium ≈ 30%, power range | Sec. 2.2, pp. 3–4 |
| Background 2.2 / model discussion: head variation | Real plants with 23–43% head variation; 50% design limit | Table 2 p. 4; p. 3 |
| Background 2.1: why seasonal storage at high latitudes | Seasonal solar, winter heating demand, electrification | Table 3 p. 5 |
| Lit. review 5.5: reservoir size → flexibility | "The larger the upper reservoir storage size the higher the operational flexibility" | p. 2, Sec. 2.1 |

## Useful quotes (with page numbers)
> "The larger the upper reservoir storage size the higher the operational flexibility of the plant." (p. 2)

## Follow-up references to check (backward snowballing)
- [13] Hunt et al. (2018), comparison between seasonal pumped-storage and conventional reservoir dams, Energy Convers. Manage. (source of Table 1 categories).
- [22] Solvang, Charmasson, Sauterlaute, Harby, Killingtveit, Egeland et al., "Norwegian hydropower for large scale electricity balancing needs — pilot study of technical, environmental and social challenges", SINTEF Energy Research (CEDREN) report — source for Saurdal and Norway; **directly relevant grey literature**. Saurdal is also cited to [18] Torres (2011), LCA of a pumped storage plant, NTNU MSc thesis (which the text also groups with Swiss references [18–21], p. 2).
- [8] Dallinger et al. (2019), socio-economic benefit and profitability of Austrian hydro storage plants, RSER 107 — **owner-profitability study, relevant to our lit. review**.
- [4] Huertas-Hernando et al. (2017), hydro power flexibility for VRE (IEA Task 25), WIREs Energy Environ.
- [6] Kougias & Szabo (2017), PHS utilization assessment: forerunner or Trojan horse?, Energy 140.
- [9] Kougias et al. (2019), emerging technologies in the hydropower sector, RSER 113.
- [10] IHA pumped storage tracking tool (grey literature).

