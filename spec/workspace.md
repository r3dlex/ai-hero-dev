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
