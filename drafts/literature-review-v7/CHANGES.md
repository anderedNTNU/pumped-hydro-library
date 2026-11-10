# Litteraturkapittel v7: revidert struktur, dypere innhold

Laget 2026-11-10 av Claude sammen med Anders.

**Grunnlag:**
- strukturen og teksten i «Literature_review_pumpekraft_revidert (2).pdf» (5.1–5.7), som Anders liker;
- vurderingen han limte inn: tabellen over svakheter per delkapittel og de 16 diskusjonspunktene fra originalutkastet.

Påstandene er sjekket mot `literature/papers/<bibkey>/note.md` (notatene oppgir sidetall), ikke mot `paper.txt` direkte. Svakheter ved kildene er hentet fra feltet «Weaknesses» i notatene.

**Filer:**
- `literature_review.tex` (kapittelet)
- `main.tex` (frittstående forhåndsvisning)
- `literature_review_v7_preview.pdf` (laget via HTML, ikke LaTeX)

## Svakhetene fra vurderingen og hva som er gjort
| Del | Svakhet | Gjort i v7 |
|---|---|---|
| 5.1 | Søkeprosessen er ikke dokumentert | TODO-boksen står fortsatt, med henvisning til Bore og Brensholms snøballmetode. Søket kan ikke beskrives før det er logget. |
| 5.2 | Opplagte og gjentatte konklusjoner | Kortere: avsnittet «Taken together» er fjernet og investeringsavsnittet slått sammen. Zhang et al. 2026 (sesong- mot konvensjonell pumpekraft) er tatt med som eksempel på systemnytte mot kostnad (punkt 1). |
| 5.3 | For lite om avhengighet, persistens, sesong og aggregering | Ny 5.3.1 om avhengighet (Kleiven, Helseth 2016, Pérez-Díaz). 5.3.2 har punkt 2 (Ak: månedlige beslutninger endres lite, timefordelingen endres mye) og punkt 3 (Abgottspon 2014 med forbeholdet). Ny 5.3.3 om hvordan tilstander lages og hva aggregering skjuler. Ny 5.3.4 om volatilitet og persistens. |
| 5.4 | Stopper ved «inntektene øker» | Underoverskrifter som hos Bore. Konkrete driftsendringer (Helseth 2016: magasinbane og vannverdier; Helseth 2017: mindre sesongflytting, vannverdier som faller raskere). Konkurransen om fleksibiliteten (punkt 6). Forward-handel (punkt 4). Aktivering. Noen effektstørrelser, etter et forbehold om at de ikke er direkte sammenlignbare. |
| 5.5 | Mye om hva studiene ikke gjør | Fire underoverskrifter med funn: pumpe lagt til (punkt 8, brutto mot netto), generatoroppgradering, store utbygginger som påvirker prisene (punkt 9), magasinstørrelse (punkt 10). En avslutning om hva som begrenser verdien av en kapasitet. |
| 5.6 | Leser som teori; to- og rullerende-delen bygger på én studie | Kortere teoriinnledning. Nytt avsnitt om fysisk representasjon (fallhøyde, virkningsgrad, enhetsmoduser). Faria og Fleten 2011 lagt til under to-stegs; Sioshansi og Dallinger under rullerende horisont. Punktene 11–15 med konkrete konsekvenser. |
| 5.7 | Volatilitet kommer for brått | Bygges nå opp i 5.3.4. Punkt 16: syntesen viser hvilken bit av evidensen hver studie gir. |

## Kildesvakheter som er brukt i teksten (fra notatene)
- **Abgottspon og Andersson 2013:** beskrives som stokastisk i priser, men bare tilsiget er tilfeldig. Prisresponsen er anslått «by experience».
- **Abgottspon og Andersson 2014:** anlegget er ikke spesifisert, og profitten er evaluert med en dispatch-heuristikk.
- **Abgottspon og Andersson 2016:** caset er deterministisk.
- **Helseth et al. 2016 og 2017:** evaluering in-sample. Prismodellen i 2017-studien er tilpasset bare tre år.
- **Helseth et al. 2018:** utvekslingen til Tyskland er satt for å skape prisforskjeller. Uklart om pumpe og turbin utvides hver for seg. Sluttverdien er hentet fra en annen modell.
- **Helseth et al. 2013:** start-tilnærmingen lar pumpen gå under minimum.
- **Alic et al. 2023:** fast prisprofil innen uka. «Energiproduksjon» er brutto. Pumpe = turbin.
- **Ak et al. 2019:** representative døgnkurver per måned fjerner kronologien.
- **Chazarra et al. 2017:** to representative uker, med kjente priser og kjent aktivering.
- **Zisos et al. 2023:** fast driftsregel uten priser, og en egen optimal design for hvert scenario.
- **Dallinger et al. 2019:** kapasitet tilbys til 0 €/MW.
- **Haldrup og Nielsen 2006:** data fra 2000–2003, og regimer på timeskala.
- **Bore og Brensholm 2026:** én bane per iterasjon, fast antall iterasjoner, ingen skranker.
- **Sioshansi 2009 og Bradbury 2014:** kjente priser, bare arbitrasje.

## Rettelser av påstander i den reviderte teksten
- **Helseth et al. 2018:** «assess generation and transmission expansions» er endret til en utvidelse av Duge (200 MW) med inntil 2000 MW.
- **Abgottspon og Andersson 2016:** var omtalt som «different reservoir types». Nå står det at studien kobler sesongmagasiner og små utjevningsmagasiner, og at caset er deterministisk.
- **Bore og Brensholm 2026 / Shapiro:** beholdt.
- **«SDDP has become the standard approach»:** kilden er nå Helseth et al. 2016, s. 934 («state-of-the-art»), i stedet for Füllner og Rebennack 2025, der påstanden ikke er bekreftet.
- **Punkt 15 (feasibility-kutt):** vurderingen sier at studien sammenligner kutt laget inne i SDDP med kutt beregnet på forhånd. Det kan ikke bekreftes, fordi Helseth og Mo 2023 ikke ligger i biblioteket. Teksten bruker det Helseth 2024 rapporterer: forhåndsberegnede, lavdimensjonale kutt gir lavere kostnad enn ren aggregering, til nesten tre ganger så lang kjøretid, og er betydelig raskere enn de høydimensjonale kuttene til Helseth og Mo 2023.
- **Artikkel 4 og 10** (forslag til fremtidig forskning om systemtjenester) er ikke identifisert og er ikke tatt med.

## Tall
Om lag 15 tall, mest effektstørrelser i 5.3–5.5 (blant annet ca. 6 % og ca. 2 % for å legge til en pumpe, 7–11 % og ca. 4,5 % for reserver, ca. 20 % for forward-handel) og noen anleggsstørrelser. Bore og Brensholm har om lag 10. Metodedelen er bevisst holdt nesten fri for kjøretider og prosenter. Kutt flere hvis dere vil ha det nærmere Bore.

## Fortsatt åpent
1. **5.1:** søkeprosessen.
2. **Lengde:** om lag 5500 ord, mot om lag 3850 hos Bore. Kandidater å korte: avsnittet om fysisk representasjon i 5.6, Zhang i 5.2 og Faria i 5.6.1.
3. **Tabell 3:** samme kolonner som i den reviderte versjonen, med Abgottspon 2013, Schüller 2024 og raden «This study» lagt til. Reserveproduktene i raden «This study» avhenger av Q-002.
4. **Ikke kompilert med LaTeX.**
