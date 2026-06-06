#!/usr/bin/env bash
#
# Scaffold a new Log post with correct front matter, dated today.
#
# Usage:
#   bin/new-post.sh "Title of a general note"      # plain note
#   bin/new-post.sh -p "Title of the paper"        # paper review (paper card + 'paper' tag)
#   bin/new-post.sh -b "Title of the book"         # book note ('books' tag)
#   bin/new-post.sh -t "meta,random" "Some title"  # extra tags on any kind
#
# Canonical tags (keep within this set): paper, books, meta, random.
#
# Prints the path of the new file (and opens it in $EDITOR if set).
set -euo pipefail

kind="note"
extra_tags=""

while getopts ":pbt:" opt; do
  case "$opt" in
    p) kind="paper" ;;
    b) kind="book" ;;
    t) extra_tags="$OPTARG" ;;
    \?) echo "unknown option -$OPTARG" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))

title="${1:-}"
if [[ -z "$title" ]]; then
  echo "usage: bin/new-post.sh [-p|-b] [-t tag1,tag2] \"Post title\"" >&2
  exit 2
fi

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
date_str="$(date +%Y-%m-%d)"
time_str="$(date '+%H:%M:%S %z')"

# Slug: lowercase, non-alphanumerics -> hyphens, collapse + trim hyphens.
slug="$(echo "$title" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"

file="$repo_root/_posts/${date_str}-${slug}.markdown"
if [[ -e "$file" ]]; then
  echo "already exists: $file" >&2
  exit 1
fi

# Assemble tags by kind, then append any -t extras.
case "$kind" in
  paper) tags="paper" ;;
  book)  tags="books" ;;
  note)  tags="" ;;
esac
if [[ -n "$extra_tags" ]]; then
  cleaned="$(echo "$extra_tags" | sed -E 's/,/, /g; s/  +/ /g')"
  tags="${tags:+$tags, }$cleaned"
fi

{
  echo "---"
  echo "layout: post"
  echo "title: \"${title//\"/\\\"}\""
  echo "date: ${date_str} ${time_str}"
  echo "tags: [${tags}]"
  if [[ "$kind" == "paper" ]]; then
    cat <<'YAML'
paper:
  title: ""
  authors: ""
  venue: ""        # e.g. "Nature, 2024"
  link: ""         # DOI or URL
  verdict: ""      # optional one-line take
YAML
  fi
  echo "---"
  echo
  case "$kind" in
    paper) echo "_What problem does it tackle, what's the key idea, and does it hold up? Replace the \`paper:\` block above with the citation._" ;;
    book)  echo "_A short note on what I took from this one._" ;;
    note)  echo "Write here." ;;
  esac
  echo
} > "$file"

echo "$file"
[[ -n "${EDITOR:-}" ]] && "$EDITOR" "$file" || true
