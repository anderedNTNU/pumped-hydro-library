# Reference theses

These are 14 earlier theses and project reports, mostly from NTNU IØT, that the group collected as examples of strong work. **Grades are not stated in the PDFs.** They are assumed to be A-level on Anders' word, which is still to be confirmed with the supervisor.

**Never copy or closely paraphrase their text.**

## Layout
| Path | Content |
|---|---|
| `texts/` | Text copies (`pdftotext -layout`) of all 14 |
| `pdf/` | The PDFs that are small enough to keep here (Bore & Brensholm 2025, Hansen & Pinderud 2024, Hope & Kvamme 2025), plus Bore's literature-review guide. The other PDFs are in Anders' OneDrive (`9.semester/Prosjektoppgave/Tidligere masteroppgaver/`); see `corpus/manifest.csv` |
| `profiles/<id>.md` | One reading of each thesis with the same template: topic, relevance, research questions, a chapter map with word shares, and the structure of each chapter |
| `corpus/manifest.csv` | id, title, year, type, citation style, closeness to our topic, original PDF location |
| `corpus/segmented/<id>.jsonl` | Each thesis split into chapters, sections, paragraphs and sentences (format in `corpus/README.md`). `<id>.outline.txt` holds the heading outline |

The scripts that built the corpus are in the old workspace (`pumped-hydro-workspace/style-references/corpus/build/`).

## The theses
Closeness is how close the thesis is to our topic (pumped hydro, multi-market operation, SDDP).

| id | Title | Year | Type | Closeness | Text |
|---|---|---|---|---|---|
| bore-2026 | Assessing the Value of Hydropower Capacity Upgrades (Bore & Brensholm, MSc) | 2026 | monograph | **closest** | `assessing-the-value-of-hydropower-capacity-upgrades.txt` |
| bore-brensholm-2025 | Multi-market optimization of flexible hydropower (project report) | 2025 | monograph | **closest** | `bore-brensholm-2025.txt` |
| empire-2024 | Integrating Technical Hydropower Planning into EMPIRE: A Node Formulation Approach | 2024 | monograph | **closest** | `integrating-technical-hydropower-planning-into-empire-a-node.txt` |
| norland-2025 | Capacity Expansion in Integrated Energy Systems | 2025 | monograph | **closest** | `capacity-expansion-in-integrated-energy-systems.txt` |
| hope-kvamme-2025 | EV charging and demand response with SDDP | 2025 | monograph | medium | `hope-kvamme-2025.txt` |
| hansen-pinderud-2024 | EV charging with MPC and SDDP | 2024 | monograph | medium | `hansen-pinderud-2024.txt` |
| stai-2023 | Optimizing and Evaluating Distributed Flexibility for Fast Frequency Reserve Provision and Demand Response | 2023 | monograph | medium | `optimizing-and-evaluating-distributed-flexibility-for-fast-f.txt` |
| rognes-2023 | A Novel Flexibility Market | 2023 | monograph | medium | `a-novel-flexibility-market.txt` |
| wendelborg-2020 | Sequencing of wholesale electricity markets (day-ahead and intraday) in a capacity expansion model under uncertainty | 2020 | monograph | medium | `sequencing-of-wholesale-electricity-markets-day-ahead-and-in.txt` |
| predel-2020 | The Potential of Power-to-Gas for Congestion Management | 2020 | monograph | far | `the-potential-of-power-to-gas-for-congestion-management.txt` |
| p2p-2020 | Impact of Local Electricity Markets and Peer-to-Peer Trading on Grid Operations | 2020 | monograph | far | `impact-of-local-electricity-markets-and-peer-to-peer-trading.txt` |
| wellnitz-2022 | Marketplaces for DSO-side flexibility providers | 2022 | paper-based | far | `marketplaces-for-dso-side-flexibility-providers-insights-reg.txt` |
| bjornstad-2024 | Towards a Sustainable Bolivian Power System | 2024 | paper-based | far | `towards-a-sustainable-bolivian-power-system.txt` |
| green-hydrogen-2024 | The Impact of Green Hydrogen and Seasonal Storage on Europe's Energy System Costs and Investments | 2024 | paper-based | far | `the-impact-of-green-hydrogen-and-seasonal-storage.txt` |

Supervisors, departments and authors are given in each profile.
