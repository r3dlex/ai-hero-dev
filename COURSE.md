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
