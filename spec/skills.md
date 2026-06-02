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
