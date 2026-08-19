#!/usr/bin/env bash
# Move this research into its own GitHub repository.
#
# The session that produced this work could not create a repository itself
# (the GitHub App integration lacked repo-creation scope), so the tree was
# committed to a branch of an existing repo. This script lifts it out.
#
# Usage:
#   1. Create an EMPTY repo on GitHub, e.g. github.com/<you>/freight-revenue-recovery
#      (no README, no .gitignore, no licence — it must be empty)
#   2. ./scripts/publish-to-new-repo.sh git@github.com:<you>/freight-revenue-recovery.git
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <new-repo-url>" >&2
  exit 1
fi

NEW_REMOTE="$1"
STAGING="$(mktemp -d)"
SRC="$(git rev-parse --show-toplevel)"

echo "Copying tracked files to ${STAGING}..."
git -C "$SRC" archive HEAD | tar -x -C "$STAGING"

cd "$STAGING"
git init -q -b main
git add -A
git commit -q -m "Freight revenue recovery: venture research

Multi-agent competitive and economic research into automated recovery of
unbilled freight accessorial revenue. See outputs/ for the ten
deliverables and research/raw/ for the underlying evidence base."
git remote add origin "$NEW_REMOTE"
git push -u origin main

echo
echo "Published to ${NEW_REMOTE}"
echo "Working copy left at ${STAGING} — delete it when you are done."
