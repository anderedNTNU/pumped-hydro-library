# Litteraturkapittel v6: v4-teksten i Bore-stil

Laget 2026-11-10 av Claude sammen med Anders. Anders likte teksten i v4 og ønsket den bare mer lik Bore og Brensholm (2026), uten mange tall. v5 (`../literature-review-v5/`) var skrevet om fra bunnen og hadde om lag 30 tall, så den er erstattet av v6.

Filer: `literature_review.tex` (kapittelet), `main.tex` (frittstående forhåndsvisning) og `literature_review_v6_preview.pdf` (laget via HTML, ikke satt med LaTeX).

## Grunnlaget
- **v4-setningene beholdes** der de er riktige. Ny tekst er lagt til bare der det trengs for rettelser, overganger og punkt G.
- **Tall:** omtrent like mange som hos Bore og Brensholm. De har rundt 10 i hele litteraturkapittelet (om lag 3850 ord), og nesten alle står i markedsdelen. v6 har rundt 9:
  - anleggsstørrelser: Duge 200 MW utvidet med inntil 2000 MW, pumpe på 38 MW, oppgraderinger på 30/60/90 MW, 6 MW;
  - tre gevinster i markedsdelen: ca. 6 % (Ak), 7–11 % (Helseth 2017) og ca. 4,5 % (Pérez-Díaz).
- **Lengde:** om lag 4100 ord, mot 3500 i v4.

## Hva som er gjort som hos Bore og Brensholm
- **Struktur:** den avtalte seks-delte strukturen (D-001), med nummererte underdelkapitler (5.2.1, 5.3.1–5.3.4, 5.5.1–5.5.4) og egne overskrifter i teksten («Energy markets», «Reserve capacity», «Reserve activation», «Extending the method», «Applications to individual owners»).
- **Forbehold om sammenlignbarhet** står først i markedsdelen, før tallene, slik Bore og Brensholm gjør.
- **Avslutninger:** delkapitlene slutter med en lærdom eller en «none of these …»-setning som bygger opp forskingsgapet, ikke med «Taken together».
- **Fysisk detalj** fra v4 5.5 er flyttet inn i metodedelen (Chazarra under deterministisk, Alic og Helseth 2017 under SDP, Helseth 2013 og Hjelmeland under SDDP). Avsnittet om rangering av konfigurasjoner er beholdt som eget avsnitt.
- **Abgottspon 2016** er flyttet fra usikkerhetsdelen til SDDP-delen.

## Rettelser av v4 (detaljene står i `../literature-review-v5/CHANGES.md`)
- **Helseth et al. 2018:** «assess transmission and generation expansions» er rettet til at Duge (200 MW) utvides med inntil 2000 MW. Det står nå også at artikkelen ikke skiller mellom pumpe og turbin.
- **Abgottspon og Andersson 2014:** at uka beskrives som usikker, gir bare gevinst når reserver er med, og når uka er kjent, overvurderes vannet. v4 sa «complex market or plant».
- **Helseth og Mo 2023:** påstanden om feasibility-kutt er flyttet til Helseth 2024, som bygger på Helseth og Mo 2023.
- **Helseth et al. 2018:** «simplifications in … constraints» er rettet til færre scenarier og grovere tidsoppløsning.
- **SDDP for pumpekraft:** «owner-oriented pumped-storage studies have relied on SDP or scenario-based optimisation» stemte ikke. Abgottspon 2016 og Schüller 2024 bruker SDDP. Nå står det at studier av pumpekraft *med reservemarkeder* har brukt SDP eller deterministisk optimering.
- **Forskningsgapet:** «… or are confined to short horizons and small state spaces» er justert tilsvarende.

## Lagt til (kort og uten mange tall)
- **5.2.1:** Dallinger 2019 og Henden 2016 (prisforskjellene krymper når mer lagring bygges, og en stor utbygging gir eierne lite inntekt).
- **5.2.2:** Schüller 2024 (én pumpe lagt til).
- **5.3.2:** et avsnitt om korrelasjon (Kleiven 2023, Pérez-Díaz 2020).
- **5.3.4 Price volatility and persistence (punkt G):** Haldrup og Nielsen 2006, Mo 2001, Sioshansi 2009, Bradbury 2014 og Löhndorf og Wozabal 2023. Avsnittet starter med v4s egen setning om at det ikke er nok å si at en studie «includes uncertainty».
- **5.4:** Pérez-Díaz 2020 og Dallinger 2019 (pumpen gir reserve uten å produsere).

## Fortsatt åpent
1. **5.1:** søkeprosessen mangler, og den røde TODO-boksen står fortsatt.
2. **Tabell 3:** v4-tabellen, med Dallinger og Schüller lagt til. Reserveproduktene i raden «This study» avhenger av Q-002.
3. **Kompilering:** filen er ikke kompilert med LaTeX. PDF-en er bare en forhåndsvisning.
