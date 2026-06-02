#!/usr/bin/env bash
# Clone all course-related repos into subrepo folders (without .git).
# Safe to re-run: skips folders that already exist.
set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")" && pwd)"
log() { echo "  [$(date +%H:%M:%S)] $*"; }

clone_no_git() {
  local repo_url="$1"
  local dest="$2"
  local orig_url="$3"

  if [[ -d "$dest" ]]; then
    log "SKIP (exists): $dest"
    return
  fi

  log "Cloning $repo_url -> $dest"
  git clone --depth 1 "$repo_url" "$dest"
  rm -rf "$dest/.git"
  log "Removed .git from $dest"

  local readme="$dest/README.md"
  local header
  header="$(printf '> **Source repo:** [%s](%s)\n> This folder is a git-free snapshot. For the live repo, visit the link above.\n\n---\n\n' "$orig_url" "$orig_url")"

  if [[ -f "$readme" ]]; then
    local tmp
    tmp=$(mktemp)
    printf '%s' "$header" | cat - "$readme" > "$tmp" && mv "$tmp" "$readme"
    log "Injected source reference into $readme"
  else
    printf '%s' "$header" > "$readme"
    log "Created $readme with source reference"
  fi
}

cd "$WORKSPACE"

clone_no_git "https://github.com/ai-hero-dev/cohort-003-project"      "cohort-003-project"      "https://github.com/ai-hero-dev/cohort-003-project"
clone_no_git "https://github.com/ai-hero-dev/cohort-003-skill-building" "cohort-003-skill-building" "https://github.com/ai-hero-dev/cohort-003-skill-building"
clone_no_git "https://github.com/mattpocock/skills"                    "skills"                   "https://github.com/mattpocock/skills"
clone_no_git "https://github.com/mattpocock/ai-hero-cli"               "ai-hero-cli"              "https://github.com/mattpocock/ai-hero-cli"

echo ""
echo "Setup complete. All repos cloned without .git."
echo "Next: cd cohort-003-project && pnpm install && pnpm db:migrate && pnpm db:seed"
