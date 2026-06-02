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
