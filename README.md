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
