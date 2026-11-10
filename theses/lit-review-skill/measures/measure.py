"""Measure the literature reviews of the reference theses (D-002, step 1).

Reads theses/corpus/segmented/<id>.jsonl and manifest.csv, and writes
  units.csv       one row per review unit (a thesis's literature review)
  sections.csv    one row per leaf section of a review
  paragraphs.csv  one row per prose paragraph of a review
  REPORT.md       medians and ranges for all reviews, the closest four and the two Bore theses

Run:  py measure.py   (from this folder; Python 3.12, standard library only)
"""
import csv, json, re, statistics as st
from pathlib import Path
from collections import defaultdict, Counter

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent.parent / "corpus"
SEG = CORPUS / "segmented"

# Which chapter / section prefixes form the literature review of each thesis.
# (chapter, section prefix or None for the whole chapter)
UNITS = {
    "bore-2026": [("4", None)],
    "bore-brensholm-2025": [("4", None)],
    "empire-2024": [("3", None)],
    "norland-2025": [("6", None)],
    "hansen-pinderud-2024": [("3", None)],
    "hope-kvamme-2025": [("3", None), ("4", "4.4")],
    "predel-2020": [("2", None)],
    "wendelborg-2020": [("2", None)],
    "rognes-2023": [("2", "2.2")],
    "stai-2023": [("2", None)],
    "bjornstad-2024": [("3", "3.2"), ("6", "6.2")],
    # green-hydrogen-2024: its reviews sit inside the two papers (3.2, 5.2), whose
    # prose is not in the segmented corpus, so it cannot be measured.
    "wellnitz-2022": [("3", "3.2"), ("5", "5.2")],
}
CLOSEST4 = ["bore-2026", "bore-brensholm-2025", "empire-2024", "norland-2025"]
BORE2 = ["bore-2026", "bore-brensholm-2025"]

# ---------- citation detection ----------
NAME = r"(?:[A-ZÆØÅ][\w'’\-]+|de |van |von |der )+"
YEAR = r"(?:19|20)\d{2}[a-z]?"
# narrative: Name (2020) | Name et al. (2020) | Name and Name (2020) | Name & Name (2020)
NARR = re.compile(rf"\b({NAME}(?:,? et al\.?|(?: and | & ){NAME})?)\s*\(({YEAR})(?:[,;][^)]*)?\)")
# parenthetical: (Name et al., 2020; Name and Name, 2019, p. 3)
PAREN = re.compile(r"\(([^()]*?\b(?:19|20)\d{2}[a-z]?[^()]*)\)")
PAREN_ITEM = re.compile(rf"({NAME}(?:,? et al\.?|(?: and | & ){NAME})?),?\s*({YEAR})")
NUMERIC = re.compile(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]")
NUMBER_UNIT = re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:%|percent|MW|GW|kW|TWh|GWh|MWh|kWh|EUR|€|NOK|USD|\$|h\b|hours|years|days|km|m³|Mm3|Mm³)")
HEDGES = re.compile(r"\b(may|might|could|likely|possibly|suggest(?:s|ed)?|appear(?:s|ed)?|seem(?:s|ed)?|tend(?:s|ed)? to|potentially|arguably|generally|often|typically)\b", re.I)
LIMIT = re.compile(r"\b(however|although|while|limitation|limited|neglect(?:s|ed)?|ignor(?:es|ed)|does not|do not|did not|cannot|not (?:consider|include|account|capture)|without|only|lack(?:s|ed)?|omit(?:s|ted)?|simplif)", re.I)
CONNECT = re.compile(r"\b(however|therefore|thus|hence|consequently|furthermore|moreover|in contrast|in addition|similarly|nevertheless|although|whereas|overall|accordingly|building on)\b", re.I)
BOOSTERS = re.compile(r"\b(clearly|significantly|substantially|strongly|highly|very|considerably|particularly|especially|crucial|essential|critical|key|vital|extremely|greatly|remarkably|notably|undoubtedly|certainly)\b", re.I)
WE = re.compile(r"\b(we|our|us)\b", re.I)
CONNECTIVE_START = re.compile(r"^(However|Therefore|Thus|Hence|Consequently|Furthermore|Moreover|Additionally|In addition|In contrast|Similarly|Nevertheless|Nonetheless|Although|Whereas|While|Accordingly|Further|On the other hand|Conversely|Overall|Finally|First|Second|Third|Also|Still|Yet|Instead|Likewise|Specifically|For example|For instance|In particular|As a result|Building on this|Taken together|To recap)\b", re.I)


def rhythm(sent_texts, text, nwords):
    """Sentence-length spread, boosters, we, punctuation and connective openers; shared by measure.py and profile_draft.py."""
    L = [words(s) for s in sent_texts]
    if not L:
        return {}
    L2 = sorted(L)
    mean = sum(L) / len(L)
    sd = (sum((x - mean) ** 2 for x in L) / len(L)) ** 0.5
    p10 = L2[int(0.1 * (len(L2) - 1))]
    p90 = L2[int(0.9 * (len(L2) - 1))]
    k = 1000 / max(1, nwords)
    return {
        "sent_sd": round(sd, 1), "sent_p10": p10, "sent_p90": p90,
        "share_sent_over_40": round(100 * sum(1 for x in L if x > 40) / len(L), 1),
        "boosters_per_1000w": round(k * len(BOOSTERS.findall(text)), 1),
        "we_per_1000w": round(k * len(WE.findall(text)), 1),
        "colons_per_1000w": round(k * text.count(":"), 1),
        "semicolons_per_1000w": round(k * text.count(";"), 1),
        "parens_per_1000w": round(k * text.count("("), 1),
        "dashes_per_1000w": round(k * (text.count("—") + text.count(" – ") + text.count(" - ")), 1),
        "questions_per_1000w": round(k * text.count("?"), 1),
        "connective_start_pct": round(100 * sum(1 for s in sent_texts if CONNECTIVE_START.match(s.strip())) / len(sent_texts), 1),
    }


SELF = re.compile(r"\b(this thesis|this study|this work|our (?:model|thesis|study|approach|contribution|work|methodology)|the present (?:thesis|study|work)|in this (?:thesis|study|work))\b", re.I)
AUTHOR_START = re.compile(rf"^(?:{NAME}(?:,? et al\.?|(?: and | & ){NAME})?)\s*\(")


def load_manifest():
    m = {}
    with open(CORPUS / "manifest.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            m[r["id"]] = r
    return m


def in_unit(rec, units):
    if rec.get("kind") != "prose":
        return False
    for ch, pre in units:
        if rec.get("chapter") != ch:
            continue
        if pre is None:
            return True
        s = rec.get("section", "")
        if s == pre or s.startswith(pre + "."):
            return True
    return False


def citations(text, style):
    """Return (n_narrative, n_parenthetical, works:set)."""
    works = set()
    narr = par = 0
    if style == "author-year-bracket":  # EMPIRE 2024 writes [Author et al., 2018]
        text = re.sub(r"\[([^\]]*\b(?:19|20)\d{2}[a-z]?[^\]]*)\]", r"(\1)", text)
    if style == "numeric":
        for m in NUMERIC.finditer(text):
            for part in re.split(r"\s*,\s*", m.group(1)):
                rng = re.split(r"\s*[–-]\s*", part)
                if len(rng) == 2 and rng[0].isdigit() and rng[1].isdigit():
                    for n in range(int(rng[0]), int(rng[1]) + 1):
                        works.add(str(n))
                        par += 1
                else:
                    works.add(part.strip())
                    par += 1
        return narr, par, works
    for m in NARR.finditer(text):
        works.add(re.sub(r"\s+", " ", m.group(1)).lower() + " " + m.group(2))
        narr += 1
    for m in PAREN.finditer(text):
        inner = m.group(1)
        # skip the narrative form "(2020)" alone handled above: PAREN also matches "(2020)" when preceded by a name
        items = list(PAREN_ITEM.finditer(inner))
        if not items:
            continue
        # if the whole parenthesis is just a year after a name, it was narrative
        if re.fullmatch(rf"\s*{YEAR}\s*", inner):
            continue
        for it in items:
            works.add(re.sub(r"\s+", " ", it.group(1)).lower() + " " + it.group(2))
            par += 1
    return narr, par, works


def words(text):
    return len(re.findall(r"[A-Za-zÆØÅæøå0-9][\w'’\-]*", text.replace("[EQ]", " ")))


def main():
    man = load_manifest()
    thesis_words = {}
    units_rows, sec_rows, par_rows = [], [], []
    sent_lengths = defaultdict(list)
    sent_texts = defaultdict(list)
    for tid, units in UNITS.items():
        style = man[tid]["citation_style"]
        recs = [json.loads(l) for l in open(SEG / f"{tid}.jsonl", encoding="utf-8")]
        total = sum(words(r["text"]) for r in recs if r.get("kind") == "prose")
        thesis_words[tid] = total
        headings = {r["number"]: r for r in recs if r.get("kind") == "heading"}
        prose = [r for r in recs if in_unit(r, units)]
        # group by leaf section in order
        sections = defaultdict(list)
        order = []
        for r in prose:
            s = r.get("section", "")
            if s not in sections:
                order.append(s)
            sections[s].append(r)
        all_works = set()
        n_cit = 0
        for s in order:
            paras = sections[s]
            sw = sum(words(p["text"]) for p in paras)
            sworks = set()
            scit = 0
            snum = 0
            for i, p in enumerate(paras):
                t = p["text"]
                narr, par, wk = citations(t, style)
                sworks |= wk
                scit += narr + par
                w = words(t)
                sents = p.get("sentences") or []
                nsent = len(sents) if isinstance(sents, list) else int(sents or 0)
                if isinstance(sents, list):
                    for sn in sents:
                        sent_lengths[tid].append(words(sn))
                        sent_texts[tid].append(sn)
                nn = len(NUMBER_UNIT.findall(t))
                snum += nn
                par_rows.append({
                    "thesis": tid, "section": s, "pos": i + 1, "n_in_section": len(paras),
                    "words": w, "sentences": nsent, "cit_narr": narr, "cit_paren": par,
                    "works": len(wk), "starts_with_author": int(bool(AUTHOR_START.match(t.strip()))),
                    "numbers_with_unit": nn, "hedges": len(HEDGES.findall(t)),
                    "limitation_words": len(LIMIT.findall(t)), "connectors": len(CONNECT.findall(t)),
                    "self_reference": int(bool(SELF.search(t))),
                    "first_words": " ".join(t.split()[:8]),
                })
            all_works |= sworks
            n_cit += scit
            title = headings.get(s, {}).get("text", "")
            level = headings.get(s, {}).get("level", s.count(".") + 1)
            first = paras[0]["text"].strip()
            last = paras[-1]["text"]
            sec_rows.append({
                "thesis": tid, "section": s, "level": level, "title": title,
                "words": sw, "paragraphs": len(paras), "citations": scit, "works": len(sworks),
                "cit_per_par": round(scit / len(paras), 2),
                "opens_with_author": int(bool(AUTHOR_START.match(first))),
                "opens_with_citation": int(bool(citations(first, style)[2])),
                "last_has_citation": int(bool(citations(last, style)[2])),
                "last_self_reference": int(bool(SELF.search(last))),
                "numbers_with_unit": snum,
            })
        uw = sum(r["words"] for r in sec_rows if r["thesis"] == tid)
        up = sum(r["paragraphs"] for r in sec_rows if r["thesis"] == tid)
        my_secs = [r for r in sec_rows if r["thesis"] == tid]
        leaf = [r for r in my_secs if r["level"] >= 2]
        units_rows.append({
            "thesis": tid, "closeness": man[tid]["closeness"], "style": style,
            "thesis_words": total, "review_words": uw, "share_pct": round(100 * uw / total, 1),
            "paragraphs": up, "sections_l2": sum(1 for r in my_secs if r["level"] == 2),
            "sections_l3": sum(1 for r in my_secs if r["level"] == 3),
            "leaf_sections": len(leaf), "words_per_leaf": round(uw / max(1, len(leaf))),
            "citations": n_cit, "works": len(all_works),
            "cit_per_100_words": round(100 * n_cit / uw, 1),
            "words_per_work": round(uw / max(1, len(all_works))),
            "median_par_words": st.median([p["words"] for p in par_rows if p["thesis"] == tid]),
            "median_sent_words": st.median(sent_lengths[tid]) if sent_lengths[tid] else "",
            "share_sent_over_35": round(100 * sum(1 for x in sent_lengths[tid] if x > 35) / max(1, len(sent_lengths[tid])), 1),
            "narrative_share_pct": round(100 * sum(p["cit_narr"] for p in par_rows if p["thesis"] == tid) / max(1, n_cit), 0),
            "numbers_with_unit_per_1000w": round(1000 * sum(p["numbers_with_unit"] for p in par_rows if p["thesis"] == tid) / uw, 1),
            "hedges_per_1000w": round(1000 * sum(p["hedges"] for p in par_rows if p["thesis"] == tid) / uw, 1),
            "connectors_per_1000w": round(1000 * sum(p["connectors"] for p in par_rows if p["thesis"] == tid) / uw, 1),
            "pars_starting_with_author_pct": round(100 * sum(p["starts_with_author"] for p in par_rows if p["thesis"] == tid) / up, 0),
            "pars_with_self_reference_pct": round(100 * sum(p["self_reference"] for p in par_rows if p["thesis"] == tid) / up, 0),
            "pars_without_citation_pct": round(100 * sum(1 for p in par_rows if p["thesis"] == tid and p["works"] == 0) / up, 0),
            **rhythm(sent_texts[tid], " ".join(p["text"] for p in prose), uw),
        })

    for name, rows in [("units.csv", units_rows), ("sections.csv", sec_rows), ("paragraphs.csv", par_rows)]:
        with open(HERE / name, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)

    # ---------- report ----------
    def med(vals):
        vals = [v for v in vals if v != "" and v is not None]
        if not vals:
            return "–"
        return f"{st.median(vals):g} [{min(vals):g}–{max(vals):g}]"

    groups = [(f"All reviews ({len(units_rows)})", [u["thesis"] for u in units_rows]), ("Closest four", CLOSEST4), ("Bore two", BORE2)]
    metrics = [
        ("Review share of thesis prose, %", "share_pct"), ("Review words", "review_words"), ("Paragraphs", "paragraphs"),
        ("Level-2 sections", "sections_l2"), ("Level-3 sections", "sections_l3"), ("Words per leaf section", "words_per_leaf"),
        ("Distinct works cited", "works"), ("Words per distinct work", "words_per_work"),
        ("Citations per 100 words", "cit_per_100_words"), ("Narrative citations, %", "narrative_share_pct"),
        ("Median paragraph words", "median_par_words"), ("Median sentence words", "median_sent_words"),
        ("Sentences over 35 words, %", "share_sent_over_35"),
        ("Paragraphs starting with an author, %", "pars_starting_with_author_pct"),
        ("Paragraphs without any citation, %", "pars_without_citation_pct"),
        ("Paragraphs referring to the thesis itself, %", "pars_with_self_reference_pct"),
        ("Numbers with a unit or % per 1000 words", "numbers_with_unit_per_1000w"),
        ("Hedges per 1000 words", "hedges_per_1000w"), ("Connectors per 1000 words", "connectors_per_1000w"),
        ("Sentence length s.d.", "sent_sd"), ("Sentence length p10", "sent_p10"), ("Sentence length p90", "sent_p90"),
        ("Sentences over 40 words, %", "share_sent_over_40"), ("Boosters per 1000 words", "boosters_per_1000w"),
        ("we/our/us per 1000 words", "we_per_1000w"), ("Colons per 1000 words", "colons_per_1000w"),
        ("Semicolons per 1000 words", "semicolons_per_1000w"), ("Parentheses per 1000 words", "parens_per_1000w"),
        ("Dashes per 1000 words", "dashes_per_1000w"), ("Questions per 1000 words", "questions_per_1000w"),
        ("Sentences opening with a connective, %", "connective_start_pct"),
    ]
    out = ["# Literature reviews of the reference theses: measurements", "",
           "Generated by `measure.py` from `theses/corpus/segmented/`. Median [min–max]. "
           "Units are defined in `UNITS` in the script (12 reviews; p2p-2020 has none and green-hydrogen-2024's sit inside papers not in the corpus). "
           "Citation detection is by regular expression (author–year or numeric); numbers are indicative, not exact.", "",
           "## Per review", "", "| Metric | " + " | ".join(g for g, _ in groups) + " |", "|---|" + "---|" * len(groups)]
    byid = {u["thesis"]: u for u in units_rows}
    for label, key in metrics:
        out.append(f"| {label} | " + " | ".join(med([byid[t][key] for t in ids if t in byid]) for _, ids in groups) + " |")

    out += ["", "## Per leaf section (sections with their own prose)", ""]
    sec_metrics = [("Words", "words"), ("Paragraphs", "paragraphs"), ("Citations", "citations"), ("Distinct works", "works"), ("Citations per paragraph", "cit_per_par"), ("Numbers with a unit", "numbers_with_unit")]
    out += ["| Metric | " + " | ".join(g for g, _ in groups) + " |", "|---|" + "---|" * len(groups)]
    for label, key in sec_metrics:
        out.append(f"| {label} | " + " | ".join(med([r[key] for r in sec_rows if r["thesis"] in ids and r["level"] >= 2]) for _, ids in groups) + " |")
    out += ["", "| Share of leaf sections that … | " + " | ".join(g for g, _ in groups) + " |", "|---|" + "---|" * len(groups)]
    for label, key in [("open with an author name", "opens_with_author"), ("open with a cited sentence", "opens_with_citation"), ("end on a paragraph with a citation", "last_has_citation"), ("end on a paragraph that refers to the thesis", "last_self_reference")]:
        vals = []
        for _, ids in groups:
            rs = [r for r in sec_rows if r["thesis"] in ids and r["level"] >= 2]
            vals.append(f"{100 * sum(r[key] for r in rs) / max(1, len(rs)):.0f} % (n={len(rs)})")
        out.append(f"| {label} | " + " | ".join(vals) + " |")

    out += ["", "## Per paragraph", ""]
    out += ["| Metric | " + " | ".join(g for g, _ in groups) + " |", "|---|" + "---|" * len(groups)]
    for label, key in [("Words", "words"), ("Sentences", "sentences"), ("Citations", "cit_narr"), ("Distinct works", "works")]:
        if key == "cit_narr":
            out.append(f"| Citations (narrative + parenthetical) | " + " | ".join(med([p["cit_narr"] + p["cit_paren"] for p in par_rows if p["thesis"] in ids]) for _, ids in groups) + " |")
        else:
            out.append(f"| {label} | " + " | ".join(med([p[key] for p in par_rows if p["thesis"] in ids]) for _, ids in groups) + " |")
    out += ["", "| Share of paragraphs that … | " + " | ".join(g for g, _ in groups) + " |", "|---|" + "---|" * len(groups)]
    for label, fn in [("start with an author name", lambda p: p["starts_with_author"]), ("cite nothing", lambda p: p["works"] == 0),
                      ("cite one work only", lambda p: p["works"] == 1), ("cite three or more works", lambda p: p["works"] >= 3),
                      ("contain a number with a unit or %", lambda p: p["numbers_with_unit"] > 0),
                      ("contain a limitation word (however, only, neglect …)", lambda p: p["limitation_words"] > 0),
                      ("refer to the thesis itself", lambda p: p["self_reference"])]:
        vals = []
        for _, ids in groups:
            ps = [p for p in par_rows if p["thesis"] in ids]
            vals.append(f"{100 * sum(1 for p in ps if fn(p)) / max(1, len(ps)):.0f} %")
        out.append(f"| {label} | " + " | ".join(vals) + " |")

    out += ["", "## Per thesis", "", "| Thesis | Closeness | Share % | Words | Paras | L2 | L3 | Works | Cit/100w | Narr % | Par words | Sent words | Num/1000w |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for u in units_rows:
        out.append(f"| {u['thesis']} | {u['closeness']} | {u['share_pct']} | {u['review_words']} | {u['paragraphs']} | {u['sections_l2']} | {u['sections_l3']} | {u['works']} | {u['cit_per_100_words']} | {u['narrative_share_pct']:.0f} | {u['median_par_words']:g} | {u['median_sent_words']} | {u['numbers_with_unit_per_1000w']} |")
    (HERE / "REPORT.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
