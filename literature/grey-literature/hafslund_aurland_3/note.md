---
bibkey: hafslund_aurland_3
title: "Aurland 3"
authors: "Hafslund"
year: 2026
venue: "hafslund.no, power plant page (Norwegian; the /en/ page shows the same Norwegian body text)"
peer_reviewed: false
methods: []
review_sections: [phs-technology]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Owner's fact page for our case plant: 2 reversible Francis pump-turbines, 2x135 MW = 270 MW, 400 m head, pumps 56 m3/s from Vetlebotnvatn up to Nyhellermagasinet, 351 GWh/yr, built 1979, soft starter 2016."
---

# Aurland 3 plant page (Hafslund, accessed 2026)

**Fetched:** 2026-11-04 from https://www.hafslund.no/no/kraftverk/aurland-3 (HTTP 200). Text snapshot `source.txt`, raw `source.html`. The English URL (`/en/kraftverk/aurland-3`, saved as `source_en.txt`) has translated labels only; the body text stays Norwegian ("All or part of this page is not available in English").
The page is a short web page with no page numbers. "Location" below means the fact box or the paragraph of the body text.
CMS timestamps in the HTML: the page data was last updated `2026-06-19` / `2026-08-06`. The plant record was created around December 2024.

## Research question / purpose
n/a. This is the owner's public information page for the plant: a fact box and three paragraphs.

## Setting
- **System:** Aurland 3, a pumped-storage plant (*pumpekraftverk*) in the Aurlandsvassdraget watercourse, Aurland municipality, Vestland, Norway. Hafslund (formerly E-CO) owns and operates it. Price area NO5 (unverified: the page does not name the bidding zone).
- **Markets:** not discussed. The page only says the plant pumps "when there is little need for power and power prices are low" and generates "when demand is high and prices are higher".
- **Horizon and resolution:** n/a.

## Method
n/a (descriptive web page).

## Data / case: every technical number on the page

**Fact box** (labels from the NO/EN page):

| Item | Value as written | Notes |
|---|---|---|
| Type / *Type* | *Pumpekraftverk* / "Pumped-storage power plant" | |
| Watercourse / *Vassdrag* | Aurlandsvassdraget | |
| Area / *Område* | Aurland | |
| Annual production / *Årsproduksjon* | **351,00 GWh** | The page doesn't say whether this is gross generation (including generation from pumped water) or net of pumping energy. It also doesn't give a reference period. Treat it as Hafslund's stated mean annual production, basis (unverified). |
| Capacity / *Effekt* | **2 × 135 MW** (= 270 MW) | Generating capacity. The body text confirms 270 MW. |
| Head / *Fallhøyde* | **400 metres** | Gross head between Nyhellermagasinet and Vetlebotnvatn, presumably (the page doesn't say gross vs net). |
| Construction year / *Byggeår* | **1979** | Commissioning year. |

**Body text:**
- Machines: **two reversible Francis pump-turbines** (*to reversible Francis pumpeturbiner*). So this is a binary set, not a ternary one (compare EERA's binary/ternary distinction in `eera_2016`).
- **Lower reservoir: Vetlebotnvatn.** **Upper reservoir: Nyhellermagasinet**, "400 metres higher". The power station "is located at Vetlebotnvatn and uses the drop from Nyhellermagasinet to Vetlebotnvatn".
- **Pumping flow: 56 thousand litres per second (56 m³/s) lifted 400 m.** The page gives **no pumping power in MW**.
  - *Derived by us, not on the page:* hydraulic power for pumping ≈ ρ·g·Q·H = 1000 · 9.81 · 56 · 400 ≈ 220 MW. Electrical pump input would be higher, about 240–260 MW at 85–90 % pump efficiency (unverified).
- Generation: "When it produces from this water it can generate **270 MW**. That corresponds to about **5,400 fast chargers for electric cars at full power**." This implies about 50 kW per charger, our arithmetic.
- Operating logic: pump up when power demand is low and prices are low; generate from the same water when demand is high and prices are higher. Hafslund calls it "like a giant battery".
- **2016: a soft starter (*mykstarter*) was installed.** It allows the station to be used for pumping over shorter periods, so the reservoir ("the hydropower battery") can be "fast-charged". This matters for our model: shorter pumping runs become economic, so start-up for pumping is less of a constraint after 2016.
- Context: the Aurland development is "an intricate network of dams, tunnels and power stations". The same water is used several times on its way from the high mountains to the fjord. This is a cascade, so Nyhellermagasinet receives natural inflow and the plant is **open-loop** in the DOE sense (`doe_pumped_storage`). That classification is our inference; the page doesn't use the term.

**Not on the page** (needed for the model; find another source such as NVE's plant database, the concession documents or Hafslund annual reports):
- reservoir volumes (Mm³) and regulation heights (HRV/LRV) for Nyhellermagasinet and Vetlebotnvatn
- pumping power (MW), turbine and pump efficiencies, the turbine discharge capacity
- natural inflow to either reservoir
- minimum-flow or other concession constraints
- which reserve markets the plant is prequalified for.

**Other Aurland plants (from data embedded in the same HTML, "related plants"; not visible body text):**

| Plant | Type | Capacity | Annual production | Head | Built |
|---|---|---|---|---|---|
| Aurland 1 | Reservoir (*magasinkraftverk*) | 3 × 280 MW | 2,297 GWh | 870 m | 1973 |
| Aurland 2 | Reservoir | "2x31,5 / 72" (MW) | 418 GWh | 110/480 m | 1982 |
| Aurland 3 | Pumped storage | 2 × 135 MW | 351 GWh | 400 m | 1979 |
| Aurland 4 Vangen | Reservoir | 38 MW | 109 GWh | 55 m | 1980 |
| Aurland 5 Reppa | Reservoir | 9 MW | 32 GWh | 439 m | 1983 |

Company context (embedded text): Hafslund owns, fully or partly, 83 hydropower plants and three wind farms. Mean production is about 18.3 TWh/yr from 5,250 MW, which makes Hafslund "Norway's second largest power producer".

## Key findings
- (fact box) 2 × 135 MW, 400 m head, 351 GWh/yr, 1979.
- (body ¶1–2) Two reversible Francis pump-turbines; they pump from Vetlebotnvatn to Nyhellermagasinet, 400 m higher, at low demand and low prices.
- (body ¶3) Pumping 56 m³/s; generating 270 MW ≈ 5,400 EV fast chargers.
- (body ¶4) A soft starter installed in 2016 enables shorter pumping periods ("fast-charging").

## Strengths
- The primary owner source for the plant. The numbers come straight from the operator.
- It states the reservoir pair, head, machine type, flow and capacity explicitly.

## Weaknesses / limitations
- No reservoir volumes, pumping MW, efficiencies, inflow or operating restrictions, so the page alone can't parametrise the model.
- The basis of "annual production" is unclear (gross vs net, reference period).
- It is a web page that may change. Keep the snapshot. It is in Norwegian, so the thesis must translate.

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where on the page |
|---|---|---|
| Background 2.3: Aurland 3 description | Type, watercourse, 2 reversible Francis pump-turbines, upper reservoir Nyhellermagasinet, lower Vetlebotnvatn, 400 m head | Fact box; body ¶1–2 |
| Case study: generating capacity | 2 × 135 MW = 270 MW | Fact box "Effekt"; body ¶3 |
| Case study: pumping capability | 56 m³/s lifted 400 m (no MW figure) | Body ¶3 |
| Case study: annual production | 351 GWh (basis unstated) | Fact box "Årsproduksjon" |
| Background: plant age, lifetime argument | Built 1979, soft starter retrofitted 2016. Pairs with EASE/EERA lifetimes of 40–80+ years | Fact box "Byggeår"; body ¶4 |
| Model: pump start-up / minimum run assumptions | The soft starter makes shorter pumping periods possible | Body ¶4 |
| Background: open-loop vs closed-loop | Cascade in a natural watercourse, so open-loop (our inference) | Body ¶1 |
| Context: the Aurland cascade | Capacities, heads and years of Aurland 1–5 | Embedded HTML data (not visible text) |
| Intro hook | "270 MW ≈ 5,400 EV fast chargers at full power" | Body ¶3 |

## Useful quotes (with page numbers)
> "Kraftverket kan pumpe 56 tusen liter vann i sekundet 400 meter opp." (body ¶3)

## Follow-up references to check (backward snowballing)
- NVE plant and reservoir database (NVE Atlas / *vannkraftdatabase*): reservoir volumes and HRV/LRV for Nyhellermagasinet and Vetlebotnvatn, plus the turbine and pump data.
- The Aurland concession (*konsesjon*) and its *manøvreringsreglement* (operating rules): minimum flows and reservoir restrictions.
- Hafslund annual reports for Aurland production statistics.

