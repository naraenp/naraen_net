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

# Keep the committed public data in sync with the private master. content.yml is
# gitignored, so this is the only point where an edit to it reaches the site.
# No-ops (exit 0) when content.yml is absent, e.g. on a fresh clone.
if [[ -f content.yml ]]; then
  echo "Deriving _data/profile.yml from content.yml ..."
  python3 bin/build-content.py
  echo
fi

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
