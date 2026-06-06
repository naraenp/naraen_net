#!/usr/bin/env bash
#
# Commit every pending change and push to main, which triggers the GitHub
# Actions deploy to naraen.net. Use this after writing a post or editing the
# reading list (_data/reading.yml).
#
#   bin/publish.sh                       # default message
#   bin/publish.sh "Update reading list" # custom message
#
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "Nothing to publish: the working tree is clean."
  exit 0
fi

echo "Changes to publish:"
git status --short
echo

msg="${*:-Update site content}"
git add -A
git commit -m "$msg"
git push

echo
echo "Pushed. GitHub Actions will rebuild and deploy to naraen.net shortly."
