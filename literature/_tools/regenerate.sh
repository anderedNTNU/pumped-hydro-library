#!/usr/bin/env bash
# Rebuild the generated literature lists from the YAML front matter of every note.md:
#   literature/INDEX.md, literature/by-method/<tag>.md, literature/by-review-section/<tag>/papers.md
# Text above the line "<!-- GENERATED BELOW -->" in each file is kept.
# Usage (from anywhere):  bash literature/_tools/regenerate.sh
set -u
LIT="$(cd "$(dirname "$0")/.." && pwd)"
MARK='<!-- GENERATED BELOW -->'
TMP="$(mktemp)"

# 1. One TSV row per note: key, dir, year, title, methods, sections, relevance, peer_reviewed, read_by, takeaway
for n in "$LIT"/papers/*/note.md "$LIT"/grey-literature/*/note.md; do
  [ -f "$n" ] || continue
  awk -v dir="$(basename "$(dirname "$(dirname "$n")")")/$(basename "$(dirname "$n")")" '
    function v(s){ sub(/^[^:]*:[ \t]*/,"",s); sub(/[ \t]+#.*$/,"",s); gsub(/^"|"$/,"",s); gsub(/\r/,"",s); return s }
    function lst(s){ s=v(s); gsub(/[\[\]]/,"",s); gsub(/[ \t]*,[ \t]*/,", ",s); return s }
    NR==1 && $0 !~ /^---/ { exit }
    NR>1 && /^---/ { printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n", key, dir, year, title, meth, sec, rel, pr, rb, tk; exit }
    /^bibkey:/ {key=v($0)} /^year:/ {year=v($0)} /^title:/ {title=v($0)}
    /^methods:/ {meth=lst($0)} /^review_sections:/ {sec=lst($0)} /^relevance:/ {rel=v($0)}
    /^peer_reviewed:/ {pr=v($0)} /^read_by:/ {rb=lst($0)} /^takeaway:/ {tk=v($0)}
  ' "$n"
done | sort -t$'\t' -k1,1 > "$TMP"

keep_head () { # print the part of $1 above the marker (or a default header)
  if [ -f "$1" ] && grep -qF "$MARK" "$1"; then sed "/$MARK/q" "$1"; else printf '%s\n\n%s\n' "$2" "$MARK"; fi
}
relorder='BEGIN{o["high"]=1;o["medium"]=2;o["background"]=3}'

# 2. INDEX.md
{ keep_head "$LIT/INDEX.md" "# Literature index"
  echo
  echo "_$(wc -l < "$TMP" | tr -d ' ') sources. Regenerated $(date +%Y-%m-%d) by \`literature/_tools/regenerate.sh\`._"
  echo
  echo "| Key | Year | Title | Methods | Review sections | Relevance | Peer-reviewed | Read by |"
  echo "|---|---|---|---|---|---|---|---|"
  awk -F'\t' '{printf "| [`%s`](%s/note.md) | %s | %s | %s | %s | %s | %s | %s |\n",$1,$2,$3,$4,$5,$6,$7,$8,$9}' "$TMP"
} > "$LIT/INDEX.md.new" && mv "$LIT/INDEX.md.new" "$LIT/INDEX.md"

# 3. by-method/<tag>.md and 4. by-review-section/<tag>/papers.md
gen_list () { # $1 = column (5 methods | 6 sections), $2 = tag, $3 = output file, $4 = link prefix
  { keep_head "$3" "# $2"
    echo
    rows=$(awk -F'\t' -v c="$1" -v t="$2" "$relorder"'{ n=split($c,a,", "); for(i=1;i<=n;i++) if(a[i]==t){ print (o[$7]?o[$7]:9) "\t" $0 } }' "$TMP" | sort -t$'\t' -k1,1n -k4,4r)
    if [ -z "$rows" ]; then echo "_No papers tagged yet._"; else
      echo "| Key | Year | Relevance | Takeaway |"; echo "|---|---|---|---|"
      echo "$rows" | awk -F'\t' -v p="$4" '{printf "| [`%s`](%s%s/note.md) | %s | %s | %s |\n",$2,p,$3,$4,$8,$11}'
    fi
  } > "$3.new" && mv "$3.new" "$3"
}
for f in "$LIT"/by-method/*.md; do gen_list 5 "$(basename "$f" .md)" "$f" "../"; done
for d in "$LIT"/by-review-section/*/; do gen_list 6 "$(basename "$d")" "$d/papers.md" "../../"; done

# 5. Report unknown tags (not matching a by-method file or by-review-section folder)
awk -F'\t' '{print $5}' "$TMP" | tr ',' '\n' | sed 's/^ *//;/^$/d' | sort -u | while read -r t; do [ -f "$LIT/by-method/$t.md" ] || echo "WARNING unknown method tag: $t"; done
awk -F'\t' '{print $6}' "$TMP" | tr ',' '\n' | sed 's/^ *//;/^$/d' | sort -u | while read -r t; do [ -d "$LIT/by-review-section/$t" ] || echo "WARNING unknown review_sections tag: $t"; done
echo "Regenerated lists from $(wc -l < "$TMP" | tr -d ' ') notes."
rm -f "$TMP"
