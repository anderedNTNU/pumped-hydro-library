"""Profile a draft literature review against the reference reviews (same metrics as measure.py).

Input: a .tex file (citations rendered from references.bib as Author (year) / (Author, year)) or a plain-text
file with blank-line-separated paragraphs. Output: each metric next to the corpus range, with a flag when the
draft lies outside the closest-four range.

Run:  py profile_draft.py <file.tex|file.txt> [--bib ../../../../pumped-hydro-thesis/references.bib]
"""
import csv, re, statistics as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from measure import citations, words, NUMBER_UNIT, HEDGES, CONNECT, SELF, AUTHOR_START, CLOSEST4, BORE2

HERE = Path(__file__).resolve().parent
DEFAULT_BIB = HERE.parents[3] / "pumped-hydro-thesis" / "references.bib"


def load_bib(path):
    """key -> (first author surname(s) rendered, year)."""
    keys = {}
    if not Path(path).exists():
        return keys
    txt = Path(path).read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", txt, flags=re.S):
        key, body = m.group(1).strip(), m.group(2)
        a = re.search(r"author\s*=\s*\{(.*?)\}\s*,?\n", body, flags=re.S)
        y = re.search(r"(?:year|date)\s*=\s*\{?(\d{4})", body)
        year = y.group(1) if y else "n.d."
        if a:
            authors = [x.strip() for x in re.split(r"\s+and\s+", a.group(1).replace("\n", " "))]
            surnames = []
            for au in authors:
                au = re.sub(r"[{}]", "", au)
                surnames.append(au.split(",")[0].strip() if "," in au else au.split()[-1])
            if len(surnames) == 1:
                name = surnames[0]
            elif len(surnames) == 2:
                name = f"{surnames[0]} and {surnames[1]}"
            else:
                name = f"{surnames[0]} et al."
        else:
            name = key
        keys[key] = (name, year)
    return keys


def render_tex(tex, bib):
    tex = re.sub(r"(?m)^%.*$", "", tex)
    tex = re.sub(r"\\todonote\{.*?\}", "", tex, flags=re.S)
    tex = re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", "", tex, flags=re.S)
    tex = re.sub(r"\\begin\{(?:landscape|table|figure)\}.*?\\end\{(?:landscape|table|figure)\}", "", tex, flags=re.S)

    def one(key):
        name, year = bib.get(key.strip(), (key.strip(), "n.d."))
        return name, year

    def citet(m):
        return "; ".join(f"{one(k)[0]} ({one(k)[1]})" for k in m.group(1).split(","))

    def citep(m):
        return "(" + "; ".join(f"{one(k)[0]}, {one(k)[1]}" for k in m.group(1).split(",")) + ")"

    tex = re.sub(r"\\citet\{([^}]*)\}", citet, tex)
    tex = re.sub(r"\\(?:citep|parencite|cite)\{([^}]*)\}", citep, tex)
    tex = re.sub(r"\\textcite\{([^}]*)\}", citet, tex)
    tex = re.sub(r"\\SI\{([^}]*)\}\{[^}]*\}", r"\1 MW", tex)
    tex = re.sub(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{([^}]*)\}", r"\n\n", tex)
    tex = re.sub(r"\\label\{[^}]*\}|\\ref\{[^}]*\}|\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", tex)
    tex = tex.replace("~", " ").replace("{", "").replace("}", "").replace("``", '"').replace("''", '"')
    return tex


def paragraphs(text):
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if words(p) >= 12]


def sentences(p):
    p = re.sub(r"\bet al\.", "et al", p).replace("e.g.", "eg").replace("i.e.", "ie")
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", p) if words(s) >= 3]


def main():
    args = sys.argv[1:]
    bibpath = DEFAULT_BIB
    if "--bib" in args:
        i = args.index("--bib"); bibpath = Path(args[i + 1]); del args[i:i + 2]
    src = Path(args[0])
    text = src.read_text(encoding="utf-8", errors="ignore")
    if src.suffix == ".tex":
        text = render_tex(text, load_bib(bibpath))
    paras = paragraphs(text)
    full = " ".join(paras)
    nw = words(full)
    ncit = 0; nworks = set(); narr = 0
    pw, sw, author_start, nocite, three, selfref, numbers = [], [], 0, 0, 0, 0, 0
    for p in paras:
        n1, n2, wk = citations(p, "author-year")
        ncit += n1 + n2; narr += n1; nworks |= wk
        pw.append(words(p))
        author_start += bool(AUTHOR_START.match(p))
        nocite += (len(wk) == 0); three += (len(wk) >= 3)
        selfref += bool(SELF.search(p)); numbers += len(NUMBER_UNIT.findall(p))
        sw += [words(s) for s in sentences(p)]
    draft = {
        "Review words": nw, "Paragraphs": len(paras), "Distinct works cited": len(nworks),
        "Citations per 100 words": round(100 * ncit / nw, 2), "Narrative citations, %": round(100 * narr / max(1, ncit)),
        "Median paragraph words": st.median(pw), "Median sentence words": st.median(sw) if sw else 0,
        "Sentences over 35 words, %": round(100 * sum(1 for x in sw if x > 35) / max(1, len(sw)), 1),
        "Paragraphs starting with an author, %": round(100 * author_start / len(paras)),
        "Paragraphs without any citation, %": round(100 * nocite / len(paras)),
        "Paragraphs referring to the thesis itself, %": round(100 * selfref / len(paras)),
        "Numbers with a unit or % per 1000 words": round(1000 * numbers / nw, 1),
        "Hedges per 1000 words": round(1000 * len(HEDGES.findall(full)) / nw, 1),
        "Connectors per 1000 words": round(1000 * len(CONNECT.findall(full)) / nw, 1),
    }
    keymap = {"Review words": "review_words", "Paragraphs": "paragraphs", "Distinct works cited": "works",
              "Citations per 100 words": "cit_per_100_words", "Narrative citations, %": "narrative_share_pct",
              "Median paragraph words": "median_par_words", "Median sentence words": "median_sent_words",
              "Sentences over 35 words, %": "share_sent_over_35", "Paragraphs starting with an author, %": "pars_starting_with_author_pct",
              "Paragraphs without any citation, %": "pars_without_citation_pct", "Paragraphs referring to the thesis itself, %": "pars_with_self_reference_pct",
              "Numbers with a unit or % per 1000 words": "numbers_with_unit_per_1000w", "Hedges per 1000 words": "hedges_per_1000w",
              "Connectors per 1000 words": "connectors_per_1000w"}
    with open(HERE / "units.csv", encoding="utf-8") as f:
        units = list(csv.DictReader(f))
    def rng(key, ids):
        vals = [float(u[key]) for u in units if u["thesis"] in ids and u[key] != ""]
        return (min(vals), st.median(vals), max(vals)) if vals else (0, 0, 0)
    allids = [u["thesis"] for u in units]
    print(f"# Draft profile: {src.name}\n")
    print("| Metric | Draft | All reviews min/median/max | Closest four min/median/max | Flag |")
    print("|---|---|---|---|---|")
    for label, val in draft.items():
        k = keymap[label]
        a = rng(k, allids); c = rng(k, CLOSEST4)
        flag = "" if c[0] <= float(val) <= c[2] else ("LOW" if float(val) < c[0] else "HIGH")
        print(f"| {label} | {val:g} | {a[0]:g} / {a[1]:g} / {a[2]:g} | {c[0]:g} / {c[1]:g} / {c[2]:g} | {flag} |")
    long = [s for p in paras for s in sentences(p) if words(s) > 35]
    if long:
        print(f"\nSentences over 35 words ({len(long)}):")
        for s in long[:15]:
            print("- " + s[:160] + ("…" if len(s) > 160 else ""))


if __name__ == "__main__":
    main()
