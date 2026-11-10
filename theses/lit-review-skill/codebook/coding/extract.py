"""Write <id>.paragraphs.txt for every review unit, numbered [Pnn] with section and position (for coding)."""
import json, sys
from collections import OrderedDict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "measures"))
from measure import UNITS, SEG, in_unit

HERE = Path(__file__).resolve().parent
for tid, units in UNITS.items():
    recs = [json.loads(l) for l in open(SEG / f"{tid}.jsonl", encoding="utf-8")]
    heads = {r["number"]: r["text"] for r in recs if r.get("kind") == "heading"}
    paras = [r for r in recs if in_unit(r, units)]
    bysec = OrderedDict()
    for r in paras:
        bysec.setdefault(r["section"], []).append(r)
    out, n = [f"# {tid}: literature review paragraphs ({len(paras)})"], 0
    for s, ps in bysec.items():
        out.append(f"\n### {s} {heads.get(s, '')}  ({len(ps)} paragraphs)")
        for i, p in enumerate(ps, 1):
            n += 1
            out.append(f"\n[P{n:02d}] section {s}, pos {i}/{len(ps)}\n{p['text']}")
    (HERE / f"{tid}.paragraphs.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(tid, n)
