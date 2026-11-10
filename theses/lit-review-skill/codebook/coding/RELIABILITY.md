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

