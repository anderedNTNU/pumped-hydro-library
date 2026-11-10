# Litteraturkapittel v5: hva er endret fra v4

Laget 2026-11-09 av Claude sammen med Anders. Filer: `literature_review.tex` (kapittelet), `main.tex` (frittstående forhåndsvisning).
Alle påstander er sjekket mot `literature/papers/<bibkey>/note.md`, og tallene mot `paper.txt`. Teksten er et utkast som dere skal skrive om (AI-bruk er logget i `ai-usage.md`).

## Struktur (avtalt med Anders)
5.1 Scope and Search · 5.2 Valuation of Pumped Storage and Its Capacities · 5.3 Uncertainty and Price Dynamics · 5.4 Market Participation · 5.5 Solution Methods (der fysisk detalj er flettet inn) · 5.6 Research Gap and Positioning.
SDP, SDDP, to-stegs programmering og rullerende horisont blir først nevnt i 5.5 (kontrollert med grep). Ingen avsnitt slutter med «taken together».

## Rettelser av påstander i v4 (punkt A og D)
| Studie (bibkey) | v4 sa | Riktig ifølge artikkelen |
|---|---|---|
| Helseth et al. 2018 (`helseth2017`) | «utvidelse fra 200 til 2000 MW» | Duge (200 MW) utvides **med inntil +2000 MW**. Artikkelen sier ikke om pumpe og turbin økes hver for seg. |
| Helseth & Mo 2023 (`helseth2023hydropowera`) | beregner feasibility-kutt før SDDP for en aggregert modell | Artikkelen ligger ikke i biblioteket, så dette er ikke kontrollert. Påstanden og tallene (−7,2 % kostnad, 2,7× kjøretid) hører til **Helseth 2024** (`helseth2024approximating`), som bygger på Helseth & Mo 2023. Teksten bruker nå 2024-artikkelen og nevner 2023 bare som grunnlaget. |
| Chazarra et al. 2017 | (usikkert om deterministisk og lineær) | Deterministisk, men **MILP** (ikke lineær), daglig horisont med samme start- og sluttnivå. Ternære enheter gir +141–166 %, binære SC bare +2,8–3,5 %. |
| Abgottspon & Andersson 2013 | price maker, DA + forward | Stemmer. 240 MW turbin, 46 MW pumpe, ca. 200 GWh. Forward-handel gir ca. +20 % (24 mot 20 M€). **Bare tilsig** er stokastisk; noen prismodell er ikke beskrevet. |
| Abgottspon & Andersson 2014 | stokastisk innen uken lønner seg bare ved kompleks marked/anlegg | Mer presist: det gir ca. +10 % profitt og CVaR **bare når sekundærreserver er med**. Uten reserver vinner modellen med kjent uke. At uka er kjent, overvurderer vannverdien. Om komplekse anlegg også gir gevinst, er lagt til fremtidig arbeid. Kapasitetene oppgis ikke. |
| Abgottspon & Andersson 2016 | rammeverk for ulike magasintyper | Multi-horisont-SDDP for KWO (10 magasiner, 1125 MW turbin, 424 MW pumpe). Gap 0,5 %, men **caset er deterministisk**. Står nå under metoder. |
| v4 5.7.4 / 5.8 | «eierperspektiv-studier av pumpekraft har bare brukt SDP eller scenariobaserte metoder» | **Feil.** Abgottspon 2016 og Schüller et al. 2024 (`schuller2024practical`, 90 MW pumpe i Sira-Kvina) bruker begge SDDP. Påstanden er tatt ut. |
| Helseth et al. 2017 (`helseth2017iet`) | sammenligner generatorkonfigurasjoner | Stemmer. To reinvesteringsalternativer på 24,8 MW. Reserver gir +7,3 % (Francis + Pelton) og +10,8 % (to Pelton). LP overvurderer med 2,3–5,2 prosentpoeng. |
| Hjelmeland et al. 2019 | «argue that co-optimising calls for a non-convex description» | Mer presist: forsterkede kutt gir bedre policy til ca. 5× kjøretid, men gapet er 36 % med prisusikkerhet. |
| Zisos et al. 2023 | 6 MW, ca. 315 000 m³ | Stemmer. Pumpe og turbin begge 6 MW (faste). 315 195 m³ deterministisk, ca. 330 000 m³ i snitt over 100 scenarier, mot 1,1 Mm³ i tidligere design. Driften er en fast regel, ikke optimering, og uten priser. |
| Alic et al. 2023 | 38 MW pumpe | Stemmer. Pumpe = turbin = 38 MW. Median inntektsøkning +2,35 %, bare energimarked. |
| Helseth et al. 2013 | 100 MW | Stemmer (Vörðufell, 100 MW, 20 Mm³, Island). |
| Ak et al. 2019 | inntektsgevinst | +2,9–10,4 % (snitt 6,0 %). Deterministisk NLP med månedlige beslutninger. |
| Bore & Brensholm 2026 | — | Tall fra EEM-artikkelen (`bore2026`): +25,8 % (0 MW) og +57,5 % (90 MW) med kapasitetsmarkeder. Resten fra masteroppgaven (`bore2026assessing`). |

## Kilder som er lagt til
- **Punkt G (prisdynamikk og lagerverdi):** `haldrup2006regime` (nordisk prispersistens), `mo2001` (en Markov-kjede glemmer tilstanden sin), `sioshansi2009estimating` (lagringstimer mot arbitrasjeverdi), `bradbury2014economic` (volatilitet øker avkastningen, men bestemmer ikke lagringsvarighet), `lohndorf2023` (korttidsvariasjon betyr mer for pumpekraft) og `kleiven2023` (korrelasjonen mellom pris og tilsig betyr lite for inntekten).
- **Verdsetting og kapasiteter:** `henden2016economic` og `dallinger2019socioeconomic` (lagring kannibaliserer prisforskjellene), `schuller2024practical` (90 MW pumpe), `perezdiaz2020medium` (aFRR i vannverdimodellen).
- **Tatt ut:** Sauhats et al. 2016 og Zhang et al. 2026 (sesongbasert kontra konvensjonell pumpekraft, Energy Conversion and Management). Begge er i biblioteket, men den første er et 6-timers lager uten vannverdier, og den andre er et systemstudie uten marked. Ta dem inn igjen hvis dere vil ha med system- eller sesongperspektivet. `dimoski2018hydropower` er heller ikke brukt, fordi den ikke er fagfellevurdert.

## Det dere må gjøre
1. **5.1:** søkeloggen (`literature/search-log.md`) er tom, så den røde TODO-boksen står fortsatt. Ikke skriv om søket før det er logget.
2. **Zotero:** `bore2026assessing`, `bradbury2014economic` og `abgottspon2016multihorizon` ble lagt inn 2026-11-10 (thesis-commit 6ded326), så `supplementary.bib` er fjernet.
3. **Tabell 3, raden «This study»:** reserveproduktene er holdt generiske til Q-002 er avgjort. Raden sier «varied price volatility and persistence», men det finnes ennå ikke noe kapittel om metoden for dette (kap. 7 er bare kommentarer).
4. **Kryssreferanser:** teorikapittelet refereres nå med `subsec:two_stage_stochastic_optimisation`, `subsec:stochastic_dynamic_programming` og `subsec:stochastic_dual_dynamic_programming`, og bakgrunnen med `sec:ph25-volatility-persistence`. I forhåndsvisningen vises de som ??.
5. **Kompilering:** LaTeX er ikke installert på denne maskinen, så filen er **ikke kompilert**. Kjør den i Overleaf eller lokalt (pdflatex → biber → pdflatex ×2). Den trenger `siunitx` i tillegg til booktabs, tabularx, longtable, pdflscape og array.
