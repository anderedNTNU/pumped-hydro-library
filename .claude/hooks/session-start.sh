#!/usr/bin/env bash
# SessionStart hook: pull both repos and show recent activity.
# Everything printed to stdout is given to Claude as context at the start of the session.

WS="${CLAUDE_PROJECT_DIR:-$(pwd)}"
THESIS="$WS/../pumped-hydro-thesis"

pull_repo () {
  local dir="$1" name="$2"
  if [ ! -d "$dir/.git" ]; then
    echo "WARNING: $name not found at $dir. Clone it next to this repo."
    return
  fi
  if ! git -C "$dir" remote get-url origin >/dev/null 2>&1; then
    echo "NOTE: $name has no GitHub remote yet; skipping pull."
    return
  fi
  if out=$(git -C "$dir" pull --rebase --autostash 2>&1); then
    echo "Pulled $name: $(echo "$out" | tail -n 1)"
  else
    echo "WARNING: git pull FAILED for $name. Resolve it with the user before editing anything:"
    echo "$out" | tail -n 8
  fi
}

echo "=== Sync ==="
pull_repo "$WS" "pumped-hydro-library"
pull_repo "$THESIS" "pumped-hydro-thesis"

# Thesis repo: Overleaf (remote "overleaf") is the source of truth; GitHub (remote "origin") is a backup mirror.
if [ -d "$THESIS/.git" ]; then
  if git -C "$THESIS" remote get-url overleaf >/dev/null 2>&1; then
    git -C "$THESIS" push -q origin HEAD:main >/dev/null 2>&1 && echo "GitHub backup of thesis updated." \
      || echo "NOTE: could not update the GitHub backup of the thesis (not critical)."
  else
    echo "NOTE: thesis repo has no 'overleaf' remote. Ask Anders for the Overleaf git URL."
  fi
fi

echo
echo "=== Recent commits (library) ==="
git -C "$WS" log --since="10 days ago" -n 12 --pretty=format:'%ad  %an  %s' --date=short 2>/dev/null
echo
if [ -d "$THESIS/.git" ]; then
  echo
  echo "=== Recent commits (thesis / Overleaf) ==="
  git -C "$THESIS" log --since="10 days ago" -n 8 --pretty=format:'%ad  %an  %s' --date=short 2>/dev/null
  echo
fi

echo
echo "=== Latest session logs ==="
ls -1 "$WS/sessions" 2>/dev/null | grep -E '^[0-9]{4}-' | sort | tail -n 5

echo
echo "Reminder: read knowledge/STATUS.md and the newest session log before starting (CLAUDE.md §1)."
exit 0
