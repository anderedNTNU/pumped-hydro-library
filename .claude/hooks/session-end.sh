#!/usr/bin/env bash
# SessionEnd hook: a safety net only. It commits and pushes uncommitted workspace changes
# so nothing is lost if someone forgets /wrap-up. It never touches the thesis repo
# (Overleaf conflicts must be handled by a person) and it never writes a summary.

WS="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$WS" || exit 0

[ -d .git ] || exit 0
[ -n "$(git status --porcelain)" ] || exit 0

who="$(git config user.name || echo unknown)"
git add -A
git commit -q -m "auto: unsaved changes at session end ($who) — no /wrap-up was run" || exit 0

if git remote get-url origin >/dev/null 2>&1; then
  git pull -q --rebase --autostash >/dev/null 2>&1 && git push -q >/dev/null 2>&1
fi
exit 0
