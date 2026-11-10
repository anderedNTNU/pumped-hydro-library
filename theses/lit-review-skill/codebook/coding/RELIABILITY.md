# Codebook reliability

Two independent coders: coder 1 = Claude (Fable) in the session with Anders, coder 2 = a separate Claude (Sonnet) agent given only CODEBOOK.md v1 and the paragraphs. Gate: at least 80 % agreement on the role and on each B field.

**Result on Bore 2026 (v1):** passed on every field. Role 86 % (kappa 0.83); B5 consequence 83 % (0.67) and B6 link 81 % (0.58) were the weakest, and their definitions were sharpened in v1.1 together with the CLAIM/GROUP boundary, the STUDY threshold, a `pointer` value for B7 and the note that B4 is independent of the role. The ambiguities coder 2 listed are in `bore-2026.coder2.notes.md`.

## bore-2026: 36 paragraphs, two independent coders

| Field | Agreement | Cohen's kappa | Disagreements |
|---|---|---|---|
| role | 86 % | 0.83 | P08 (COMPARE/CLAIM), P09 (GROUP/CLAIM), P13 (CLAIM/GROUP), P16 (STUDY/CLAIM), P19 (CLAIM/CRITIQUE) |
| b1_opener | 100 % | 1.00 |  |
| b2_backing | 97 % | 0.96 | P23 (2/3+) |
| b3_limitation | 97 % | 0.92 | P07 (group/none) |
| b4_compare | 97 % | 0.91 | P06 (yes/no) |
| b5_consequence | 83 % | 0.67 | P05 (yes/no), P06 (yes/no), P08 (yes/no), P19 (no/yes), P30 (yes/no), P35 (yes/no) |
| b6_link | 81 % | 0.58 | P02 (explicit/none), P03 (explicit/none), P09 (explicit/implicit), P11 (none/implicit), P15 (none/implicit), P16 (implicit/none), P17 (explicit/implicit) |
| b7_closer | 92 % | 0.88 | P08 (consequence/study), P16 (claim/limitation), P34 (claim/consequence) |
| b8_number | 100 % | 1.00 |  |
| c1_position | 100 % | 1.00 |  |

## Spot-check of the agent codings: 30 paragraphs (weighted to the closest four), coder 2 = Claude (Fable)

| Field | Agreement | Disagreements |
|---|---|---|
| role | 87 % | bore P10 (CLAIM/GROUP), norl P19 (GROUP/CRITIQUE), norl P17 (CLAIM/STUDY), norl P07 (GROUP/CLAIM) |
| b1_opener | 83 % | bore P21 (claim/transition), bore P34 (claim/transition), bore P02 (claim/transition), empi P02 (claim/transition), empi P07 (claim/transition) |
| b2_backing | 93 % | bore P03 (1/0), norl P19 (1/3+) |
| b3_limitation | 87 % | bore P10 (none/named), bore P18 (group/none), norl P17 (none/named), pred P19 (none/group) |
| b4_compare | 100 % |  |
| b5_consequence | 83 % | bore P27 (yes/no), norl P17 (yes/no), empi P07 (yes/no), hope P16 (no/yes), stai P37 (yes/no) |
| b6_link | 90 % | bore P02 (explicit/none), bore P03 (implicit/none), norl P19 (implicit/explicit) |
| b7_closer | 70 % | bore P27 (consequence/claim), bore P18 (consequence/claim), norl P17 (consequence/limitation), norl P07 (study/claim), empi P01 (claim/pointer), hope P16 (study/consequence), stai P08 (consequence/claim), well P04 (claim/pointer), well P26 (study/claim) |
| b8_number | 100 % |  |

**Spot-check verdict:** every field at or above 83 % except B7 (70 %), where the coders split between "consequence" and "claim" on evaluative last sentences. Merged into two values (evaluative close = consequence or limitation; descriptive close = study, claim or pointer) B7 agrees on 87 %, so the skill uses B7 only in that merged form. Role agreement 87 % matches the Bore 2026 test (86 %). The agent codings are therefore used as they stand.

