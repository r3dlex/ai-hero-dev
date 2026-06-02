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
