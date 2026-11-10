"""Agreement between two codings of the same paragraphs (codebook reliability test).

Run:  py compare.py <id>   e.g.  py compare.py bore-2026
Reads coding/<id>.coder1.csv and coding/<id>.coder2.csv, prints and appends a table to RELIABILITY.md.
"""
import csv, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIELDS = ["role", "b1_opener", "b2_backing", "b3_limitation", "b4_compare", "b5_consequence", "b6_link", "b7_closer", "b8_number", "c1_position"]


def load(p):
    with open(p, encoding="utf-8-sig") as f:
        return {r["para"].strip(): {k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)}


def kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb.get(k, 0) for k in ca) / (n * n)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    tid = sys.argv[1]
    c1, c2 = load(HERE / f"{tid}.coder1.csv"), load(HERE / f"{tid}.coder2.csv")
    keys = sorted(set(c1) & set(c2))
    lines = [f"## {tid}: {len(keys)} paragraphs, two independent coders", "", "| Field | Agreement | Cohen's kappa | Disagreements |", "|---|---|---|---|"]
    for f in FIELDS:
        a = [c1[k][f] for k in keys]
        b = [c2[k][f] for k in keys]
        agree = sum(1 for x, y in zip(a, b) if x == y)
        dis = ", ".join(f"{k} ({c1[k][f]}/{c2[k][f]})" for k in keys if c1[k][f] != c2[k][f])
        lines.append(f"| {f} | {100 * agree / len(keys):.0f} % | {kappa(a, b):.2f} | {dis} |")
    txt = "\n".join(lines) + "\n\n"
    print(txt)
    with open(HERE / "RELIABILITY.md", "a", encoding="utf-8") as f:
        f.write(txt)


if __name__ == "__main__":
    main()
