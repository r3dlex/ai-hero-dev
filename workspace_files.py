import os, stat

files = {}

files[".gitignore"] = """\
# macOS
.DS_Store
.AppleDouble
.LSOverride

# Node / pnpm
node_modules/
.pnpm-store/
pnpm-lock.yaml

# Env & secrets
.env
.env.local
.env.*.local

# Build artifacts
dist/
build/
/.react-router/
*.tsbuildinfo

# SQLite (from cohort-003-project)
*.db
*.db-journal
*.db-wal
*.db-shm

# Claude Code
.claude/settings.local.json

# IDEs
.idea/
.vscode/

# Logs
*.log
npm-debug.log*

# Cloned subrepos — managed by setup.sh, not tracked in git
/cohort-003-project/
/cohort-003-skill-building/
/skills/
/ai-hero-cli/
"""

files[".omc"] = """\
{
  "workspace": "ai-hero-dev",
  "description": "AI Coding for Real Engineers — cohort 003 (March–April 2026) learning workspace",
  "owner": "andreburgstahler@gmail.com",
  "agentEntrypoint": "AGENTS.md",
  "claudeEntrypoint": "CLAUDE.md",
  "subrepos": [
    {
      "name": "cohort-003-project",
      "origin": "https://github.com/ai-hero-dev/cohort-003-project",
      "localPath": "./cohort-003-project",
      "role": "main-exercise-repo",
      "tech": ["React Router v7", "TypeScript 5.9", "SQLite", "Drizzle ORM", "Tailwind CSS 4", "Vitest"]
    },
    {
      "name": "cohort-003-skill-building",
      "origin": "https://github.com/ai-hero-dev/cohort-003-skill-building",
      "localPath": "./cohort-003-skill-building",
      "role": "skill-exercises",
      "tech": ["TypeScript", "pnpm", "ai-hero-cli"]
    },
    {
      "name": "skills",
      "origin": "https://github.com/mattpocock/skills",
      "localPath": "./skills",
      "role": "claude-code-skills",
      "tech": ["Shell", "Markdown"]
    },
    {
      "name": "ai-hero-cli",
      "origin": "https://github.com/mattpocock/ai-hero-cli",
      "localPath": "./ai-hero-cli",
      "role": "exercise-runner-cli",
      "tech": ["TypeScript", "pnpm"]
    }
  ],
  "conventions": {
    "packageManager": "pnpm",
    "nodeVersion": "22+",
    "language": "TypeScript",
    "formatter": "Prettier"
  }
}
"""

files["CLAUDE.md"] = """\
# Claude Code Workspace

This is the **AI Hero Dev** learning workspace for the *AI Coding for Real Engineers* cohort (2026-04).

→ See **[AGENTS.md](./AGENTS.md)** for the full agent guide: repo layout, coding conventions, task patterns, and context rules.

→ See **[COURSE.md](./COURSE.md)** for course structure, what each section covers, and lesson-by-lesson notes.

→ See **[spec/](./spec/)** for detailed specifications of each sub-repository.
"""

files["AGENTS.md"] = """\
# Agent Guide — AI Hero Dev Workspace

## Purpose

This workspace supports learning and practice from the **AI Coding for Real Engineers** cohort (March–April 2026), led by Matt Pocock at [AI Hero](https://www.aihero.dev). The course teaches real-world Claude Code workflows: agent steering, skills, planning, multi-phase execution, and test-driven development.

---

## Repository Layout

```
ai-hero-dev/
├── AGENTS.md                    ← you are here
├── CLAUDE.md                    ← Claude Code entrypoint (points here)
├── COURSE.md                    ← full course map and lesson notes
├── README.md                    ← workspace overview
├── .gitignore                   ← excludes all subrepos and build artifacts
├── .omc                         ← Open Memory Context (workspace AI config)
├── setup.sh                     ← clones all subrepos (idempotent)
├── spec/
│   ├── workspace.md             ← this workspace's architecture
│   ├── cohort-003-project.md    ← main exercise repo spec
│   ├── cohort-003-skill-building.md
│   ├── skills.md                ← mattpocock/skills spec
│   └── ai-hero-cli.md
│
├── cohort-003-project/          ← cloned, no .git — DO NOT git add
├── cohort-003-skill-building/   ← cloned, no .git — DO NOT git add
├── skills/                      ← cloned, no .git — DO NOT git add
└── ai-hero-cli/                 ← cloned, no .git — DO NOT git add
```

**Subrepos are cloned without `.git`** — they live here for reference and local development but are not tracked by this workspace's git. Run `./setup.sh` to clone or refresh them.

---

## Subrepos

### cohort-003-project
- **Origin:** https://github.com/ai-hero-dev/cohort-003-project
- **What it is:** The main exercise codebase — a mini course platform (React Router v7, TypeScript, SQLite, Drizzle ORM, Tailwind CSS 4, shadcn/ui, Vitest). This is the repo you modify during each lesson.
- **Key commands:** `pnpm dev`, `pnpm test`, `pnpm db:migrate`, `pnpm reset <commit>`, `pnpm cherry-pick <commit>`
- **Skills live at:** `.claude/skills/`

### cohort-003-skill-building
- **Origin:** https://github.com/ai-hero-dev/cohort-003-skill-building
- **What it is:** Standalone TypeScript exercises for building Claude Code skills. Uses `ai-hero-cli` for exercise navigation.
- **Key commands:** `pnpm install`, `ai-hero exercise`

### skills
- **Origin:** https://github.com/mattpocock/skills
- **What it is:** Matt Pocock's personal Claude Code skills library. Install any skill with `npx skills@latest add mattpocock/skills/<name>`.
- **Skills include:** `write-a-prd`, `prd-to-plan`, `prd-to-issues`, `grill-me`, `tdd`, `triage-issue`, `git-guardrails-claude-code`, `write-a-skill`, and more.

### ai-hero-cli
- **Origin:** https://github.com/mattpocock/ai-hero-cli
- **What it is:** CLI for navigating AI Hero exercises. Provides interactive exercise selection and `n`/`p` shortcuts for next/prev.

---

## Working with Subrepos

```bash
./setup.sh          # clone any missing subrepos

# Add a skill to the project
cd cohort-003-project
npx skills@latest add mattpocock/skills/write-a-prd

# Reset to a lesson checkpoint
pnpm reset 03.04.01
pnpm cherry-pick 03.04.01
```

---

## Coding Conventions

- **Language:** TypeScript everywhere. No `any` without justification.
- **Package manager:** `pnpm` (not npm or yarn).
- **Node:** v22+. Enable corepack: `corepack enable`.
- **Formatting:** Prettier. Run before committing.
- **Testing:** Vitest. Red-green-refactor: write the failing test first.
- **DB changes:** Always run `pnpm db:migrate` after schema changes.
- **Commits:** Small, atomic. One vertical slice per commit.

---

## Agent Task Patterns

### Building a feature (Days 1–3 pattern)
1. Run `/write-a-prd` to write a PRD filed as a GitHub issue.
2. Run `/prd-to-plan` to create a multi-phase tracer-bullet plan.
3. Execute phase by phase. Clear context between phases.
4. Use `/tdd` for implementation within each phase.

### Writing a new skill
1. Run `/write-a-skill` in the target repo.
2. Follow the progressive-disclosure pattern.
3. Test it with `/grill-me`.

---

## Context Rules

- Keep context windows focused. Clear between major phases.
- Use `AGENTS.md` (this file) at the start of any agent session in this workspace.
- For the exercise repo, also read `cohort-003-project/.claude/skills/` for project-specific instructions.
- Do not commit subrepo contents — they are in `.gitignore`.
"""

files["setup.sh"] = """\
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
  header="$(printf '> **Source repo:** [%s](%s)\\n> This folder is a git-free snapshot. For the live repo, visit the link above.\\n\\n---\\n\\n' "$orig_url" "$orig_url")"

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
"""

files["README.md"] = """\
# AI Hero Dev — Learning Workspace

Personal workspace for the **AI Coding for Real Engineers** cohort (2026-04) by [Matt Pocock](https://github.com/mattpocock) at [AI Hero](https://www.aihero.dev).

## What's Here

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Full agent guide: repo layout, conventions, task patterns |
| `CLAUDE.md` | Claude Code entrypoint (points to AGENTS.md) |
| `COURSE.md` | Course structure, lesson map, skill reference |
| `spec/` | Detailed specs for each sub-repository |
| `setup.sh` | Clones all subrepos without `.git` (idempotent) |
| `.omc` | Open Memory Context — workspace AI configuration |

## Subrepos

These folders are **not tracked in git** (see `.gitignore`). Run `./setup.sh` to populate them.

| Folder | Origin | Purpose |
|--------|--------|---------|
| `cohort-003-project/` | [ai-hero-dev/cohort-003-project](https://github.com/ai-hero-dev/cohort-003-project) | Main exercise codebase |
| `cohort-003-skill-building/` | [ai-hero-dev/cohort-003-skill-building](https://github.com/ai-hero-dev/cohort-003-skill-building) | Skill-building exercises |
| `skills/` | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt's Claude Code skills library |
| `ai-hero-cli/` | [mattpocock/ai-hero-cli](https://github.com/mattpocock/ai-hero-cli) | Exercise navigation CLI |

## Quick Start

```bash
./setup.sh
cd cohort-003-project && pnpm install && pnpm db:migrate && pnpm db:seed && pnpm dev
```
"""

files["COURSE.md"] = """\
# Course Map — AI Coding for Real Engineers (Cohort 003, 2026-04)

**Instructor:** Matt Pocock | **Platform:** [AI Hero](https://www.aihero.dev) | **Start:** March 30, 2026

---

## Before We Start

| # | Lesson | Notes |
|---|--------|-------|
| 01 | Where We're Going | Course overview and final demo |
| 02 | Navigating the Discord | Channels, office hours, getting help |
| 03 | Repo Setup | Clone exercise repo, install deps, run dev server |
| 04 | Choosing Your Model / Subscription | Opus 4.6 on 5× Max recommended; Sonnet 4.6 on Pro |
| 05 | How to Take This Course | `pnpm reset` and `pnpm cherry-pick` lesson navigation |
| 06 | Office Hours | Reference page for live session links |

---

## Getting to Know Claude Code

| # | Lesson | Core Concept |
|---|--------|-------------|
| 01 | Managing Your Claude Code Session | Session lifecycle, context windows, when to start fresh |
| 02 | Prompting in the Terminal | Effective terminal prompting: examples, XML tags |
| 03 | Claude and Your IDE | VS Code / Cursor integration, diff view |
| 04 | Going Forwards and Backwards in Time | `git checkpoint`, undoing Claude's changes |
| 05 | Running Bash Commands | `!` prefix, backgrounding with `&`, suspending Claude |
| 06 | Permissions | Trust levels, `--allowedTools`, dangerous operations |

---

## Day 1 — Claude Code Fundamentals

| # | Lesson | Core Concept |
|---|--------|-------------|
| 01 | The Constraints of LLMs | Context window limits, why compaction matters |
| 02 | What Are Subagents | Explore/Plan/Build agents; reading the agent trace |
| 03 | Codebase Exploration | Explore subagent, `@` file references |
| 04 | Build a Feature | End-to-end feature: prompt → implementation → commit |
| 05 | Showing Context in the Status Line | Token count + percentage in status line via AGENTS.md |
| 06 | What Is Plan Mode | Plan Mode vs. direct execution; reviewing plans |
| 07 | The Plan-Execute-Clear Loop | Multi-phase: plan → execute → clear → repeat |
| 08 | Compaction | Auto-compaction, manual `/compact`, when to clear |

---

## Day 2 — Steering

| # | Lesson | Core Concept |
|---|--------|-------------|
| 01 | What Is an AGENTS.md File | AGENTS.md/CLAUDE.md convention; scope levels |
| 02 | Steering an Agent with the AGENTS.md File | Coding conventions, banned patterns, context rules |
| 03 | Progressive Disclosure | Structuring AGENTS.md to load detail on demand |
| 04 | What Are Agent Skills | Skills as reusable `/skill-name` workflows |
| 05 | A Skill for Writing Skills | `/write-a-skill`; anatomy of a SKILL.md |
| 06 | Automatic Memory | Claude Code auto-writing memories; managing drift |

---

## Day 3 — Planning

| # | Lesson | Core Concept |
|---|--------|-------------|
| 01 | How to Tackle Massive Tasks | Why big prompts fail; decomposing into phases |
| 02 | Write Great PRDs with This Skill | `/write-a-prd`: interview-driven PRD → GitHub issue |
| 03 | Split Features Across Multiple Context Windows | `/prd-to-plan`: PRD → multi-phase tracer-bullet plan |
| 04 | What Are Tracer Bullets | Thin vertical slices; reduce risk, enable parallelism |
| 05 | Use Tracer Bullets in Our Multi-Phase Plan | Applying tracer-bullets to a real plan |
| 06 | Executing Our Multi-Phase Plan | Phase-by-phase execution; context hygiene |
| 07 | The /grill-me Skill | Stress-testing plans via adversarial interview |

---

## Day 4 — Feedback Loops *(upcoming)*

TDD with AI: red-green-refactor, the `/tdd` skill, safe refactoring with test coverage.

## Day 5 — Ralph *(upcoming)*

Autonomous agent loops, backgrounding, scheduling, AFK vs. Human-in-the-Loop task classification.

## Day 6 — Human in the Loop *(upcoming)*

Kanban workflows, research phases, prototyping, AI-friendly codebase architecture, `/improve-codebase-architecture`.

---

## Live Office Hours

| Date | Time UTC | YouTube | Status |
|------|----------|---------|--------|
| Mon Mar 30 | 08:30 | [Watch](https://www.youtube.com/watch?v=DvYDilOsQ8w) | Aired |
| Mon Mar 30 | 11:30 | [Watch](https://www.youtube.com/watch?v=hFCq28OFHG8) | Aired |
| Fri Apr 03 | 08:30 | [Watch](https://www.youtube.com/watch?v=7Fa4w_Bed2g) | Aired |
| Fri Apr 03 | 11:30 | [Watch](https://www.youtube.com/watch?v=ap8443Fuxp8) | Aired |
| Fri Apr 10 | 08:30 | [Watch](https://www.youtube.com/watch?v=EI-vFgL_YBM) | Upcoming |
| Fri Apr 10 | 11:30 | [Watch](https://www.youtube.com/watch?v=OiClFlJY-yo) | Upcoming |

---

## Key Skills (mattpocock/skills)

| Skill | Purpose |
|-------|---------|
| `write-a-prd` | Interview-driven PRD → GitHub issue |
| `prd-to-plan` | PRD → multi-phase tracer-bullet plan |
| `prd-to-issues` | PRD → vertical-slice GitHub issues |
| `grill-me` | Stress-test a plan via adversarial interview |
| `tdd` | Red-green-refactor loop |
| `triage-issue` | Investigate bug, file TDD-based fix plan |
| `write-a-skill` | Create skills with progressive disclosure |
| `git-guardrails-claude-code` | Block dangerous git commands |
| `improve-codebase-architecture` | Architectural review |
| `design-an-interface` | Parallel sub-agent interface design |
| `ubiquitous-language` | DDD glossary from conversation |
"""

files["spec/workspace.md"] = """\
# Spec: AI Hero Dev Workspace

## Purpose

A local learning environment for the AI Coding for Real Engineers cohort. Contains all course-related repos under one root without using git submodules.

## Design Decisions

**No git submodules.** Subrepos are cloned, stripped of `.git`, and excluded via `.gitignore`. To update, delete the folder and re-run `setup.sh`.

**`setup.sh` is idempotent.** Skips folders that already exist.

**AGENTS.md is the agent entry point.** CLAUDE.md is thin — it just points here (progressive disclosure).

**`.omc` captures workspace metadata** as machine-readable JSON for AI tooling.

## Extending

To add a new repo: add a `clone_no_git` call to `setup.sh`, an entry to `.omc`, a line to `.gitignore`, and create `spec/<repo>.md`.
"""

files["spec/cohort-003-project.md"] = """\
# Spec: cohort-003-project

**Origin:** https://github.com/ai-hero-dev/cohort-003-project
**Role:** Main exercise codebase used throughout the course
**Tech:** React Router v7 (SSR), TypeScript 5.9, SQLite, Drizzle ORM, Tailwind CSS 4, shadcn/ui, Vitest, Vite 7, Ably

## What It Is

A mini course platform (think a small Udemy). Has users, courses, lessons, and real-time presence. You extend, refactor, and test it using Claude Code, lesson by lesson.

## Directory Structure

```
cohort-003-project/
├── app/               # React Router routes and components
├── drizzle/           # SQLite schema + migrations
├── scripts/           # DB seed and utilities
├── ralph/             # Ralph agent automation (Day 5)
├── _internal/         # Lesson reset tooling
├── .claude/skills/    # Project-specific Claude Code skills
├── course.md          # Instructor notes per lesson
└── commit-mapping.md  # Maps pnpm reset commits to lesson IDs
```

## Key Scripts

| Command | Description |
|---------|-------------|
| `pnpm dev` | Dev server at http://localhost:5173 |
| `pnpm test` | Run Vitest |
| `pnpm db:migrate` | Run Drizzle migrations |
| `pnpm db:seed` | Seed SQLite |
| `pnpm reset <commit>` | Reset to a lesson's starting commit |
| `pnpm cherry-pick <commit>` | Apply a lesson's solution |
"""

files["spec/cohort-003-skill-building.md"] = """\
# Spec: cohort-003-skill-building

**Origin:** https://github.com/ai-hero-dev/cohort-003-skill-building
**Role:** Standalone TypeScript exercises for practising Claude Code skill creation

## Usage

```bash
pnpm install
ai-hero exercise   # interactive picker — n/p for next/prev, q to quit
```

## Structure

```
exercises/
└── <section>/<exercise>/
    ├── main.ts      # entry point
    └── readme.md    # instructions
```

Used in Day 2 (Steering) and Day 3 (Planning) to practice writing and refining skills.
"""

files["spec/skills.md"] = """\
# Spec: mattpocock/skills

**Origin:** https://github.com/mattpocock/skills
**Role:** Matt Pocock's personal Claude Code skills library

## Installing Skills

```bash
npx skills@latest add mattpocock/skills/<name>
# Installs to .claude/skills/<name>/ in current project
```

## Skills Reference

| Category | Skill | What It Does |
|----------|-------|-------------|
| Planning | `write-a-prd` | Interview → PRD → GitHub issue |
| Planning | `prd-to-plan` | PRD → multi-phase tracer-bullet plan |
| Planning | `prd-to-issues` | PRD → vertical-slice GitHub issues |
| Planning | `grill-me` | Adversarial plan stress-test |
| Planning | `design-an-interface` | Parallel sub-agent interface designs |
| Planning | `request-refactor-plan` | Refactor plan → GitHub issue |
| Dev | `tdd` | Red-green-refactor loop |
| Dev | `triage-issue` | Bug investigation + TDD fix plan |
| Dev | `improve-codebase-architecture` | Architectural review |
| Dev | `scaffold-exercises` | Create exercise directory structures |
| Tooling | `setup-pre-commit` | Husky + lint-staged + Prettier + types + tests |
| Tooling | `git-guardrails-claude-code` | Block dangerous git commands |
| Writing | `write-a-skill` | Create skills with progressive disclosure |
| Writing | `edit-article` | Restructure and tighten articles |
| Writing | `ubiquitous-language` | DDD glossary from conversation |
| Writing | `obsidian-vault` | Manage Obsidian notes |
"""

files["spec/ai-hero-cli.md"] = """\
# Spec: ai-hero-cli

**Origin:** https://github.com/mattpocock/ai-hero-cli
**Role:** CLI for navigating and running AI Hero exercises

## Commands

```bash
ai-hero exercise        # interactive picker
ai-hero exercise 1      # run exercise 1 directly
ai-hero internal upgrade  # upgrade AI SDK packages
```

## Shortcuts (during exercise)

| Key | Action |
|-----|--------|
| Enter | Choose exercise |
| n | Next |
| p | Previous |
| q | Quit |
| h | Help |

## Expected Structure

```
exercises/
└── 1-section/
    └── 1-exercise/
        ├── main.ts
        └── readme.md
```
"""

# Write all files
base = os.path.expanduser(".")
os.makedirs(os.path.join(base, "spec"), exist_ok=True)

for path, content in files.items():
    full = os.path.join(base, path)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(full) else None
    with open(full, "w") as f:
        f.write(content)
    if path == "setup.sh":
        os.chmod(full, os.stat(full).st_mode | stat.S_IXUSR | stat.S_IXGRP)
    print(f"  wrote {path}")

print("\nDone. Run ./setup.sh to clone all subrepos.")
