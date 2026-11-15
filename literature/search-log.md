# Literature search log

The literature review must describe how papers were found (search strategy, databases, keywords, selection criteria and snowballing).
Log every search here, so section 5.1 can be written from facts rather than memory.

## Selection criteria
_Agree on these, e.g.: does the title and abstract fit our scope? Is it peer-reviewed in a recognised journal (Norwegian register level 1–2, ABS)? Is it relevant to at least one review section?_

## Searches

| Date | Who | Database | Search string | Hits | Kept (bibkeys) |
|---|---|---|---|---|---|
| 2026-11-15 | Anders (Claude) | arXiv API | "stochastic dual dynamic programming" AND (hydro OR hydropower OR hydrothermal OR reservoir); SDDP AND (hydropower OR hydrothermal OR pumped OR hydroelectric) | 16 | hole2025capacity, bueno2023impact, vanackooij2020conditional |
| 2026-11-15 | Anders (Claude) | OpenAlex (full-text search, open access, from 2017) | "stochastic dual dynamic programming" hydropower; "stochastic dual dynamic programming" "pumped"; "SDDP" hydropower reserve price; and four variants with reserve, integer programming, Markov chain, environmental constraints | 402; 252; about 200 each (first 40–50 screened by title) | helseth2026considering, li2022solving, hjelmeland2018impact, garcia2025longterm, helseth2018optimal, helseth2020nonconvex |
| 2026-11-15 | Anders (Claude) | OpenAlex (title and abstract, from 2017) | "dual dynamic programming" AND (pumped OR pumping OR pump); (SDDP OR SDDiP) AND (pumped OR pumping); "dual dynamic" AND hydropower AND (reserve OR ancillary OR balancing); "dual dynamic" AND (hydropower OR hydro) AND (price-taker OR "price uncertainty" OR "electricity price") | 7; 2; 13; 9 | none new (no owner's pumped-storage study among the hits) |
| 2026-11-15 | Anders (Claude) | Web search | SDDP pumped storage reserve markets; Downward Dowson Baucke objective uncertainty; Philpott Downward JADE pumped storage | – | downward2020stochastic, philpott2023using |

## Snowballing
| Date | Who | From paper | Direction (backward/forward) | Kept (bibkeys) |
|---|---|---|---|---|
| 2026-11-15 | Anders (Claude) | hole2025capacity | backward | philpott2023using |

## Selection applied on 2026-11-15
Asked for by Anders: SDDP (or its integer variant), hydropower or pumped hydro, published after 2016, relevant to an owner's scheduling model. Only open-access copies from the publisher or an institutional repository were downloaded (Springer, Frontiers, IOP via the Norwegian research archive NVA, arXiv, Optimization Online, EPOC). Papers whose open copy could not be fetched are listed in `WANTED.md`.
