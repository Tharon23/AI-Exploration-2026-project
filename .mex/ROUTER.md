---
name: router
description: Session bootstrap and navigation hub. Read at the start of every session before any task. Contains project state, routing table, and behavioural contract.
edges:
  - target: context/architecture.md
    condition: when working on system design, integrations, or understanding how components connect
  - target: context/stack.md
    condition: when working with specific technologies, libraries, or making tech decisions
  - target: context/conventions.md
    condition: when writing new code, reviewing code, or unsure about project patterns
  - target: context/decisions.md
    condition: when making architectural choices or understanding why something is built a certain way
  - target: context/setup.md
    condition: when setting up the dev environment or running the project for the first time
  - target: context/team.md
    condition: when checking contributor ownership, branching, or dividing work
  - target: patterns/INDEX.md
    condition: when starting a task — check the pattern index for a matching pattern file
last_updated: 2026-10-07
---

# Session Bootstrap

If you haven't already read `AGENTS.md`, read it now — it contains the project identity, non-negotiables, and commands.

Then read this file fully before doing anything else in this session.

## Current Project State

**Working:**
- GitLab materials scraped and analyzed (`research/gitlab-scrape/`, `research/previous-projects/`)
- 13 specialized agency agents installed (`.gemini/agents/`)
- Project scaffold and directory structure created
- `.mex/` persistent memory scaffold initialized and configured for 3 contributors
- Course rules and project catalog documented (`docs/course-rules.md`, `research/previous-projects/full-project-catalog.md`)
- Final project concept selected: Dual-Dimension Benchmark (Security ASR vs Technical Planning Ground Truth) with Jev System-1 routing (`group_BlueMoon`), proposal drafted in `docs/gitlab-issue-draft.md`

**Not yet built:**
- Core source modules (`src/core/`, `src/pipeline/`, `src/evaluation/`, `src/deploy/`, `src/ui/`)
- GitLab issue #1 (team registration) and initial project proposal issue submission
- Docker containerization for final deliverable

**Known issues / Risks:**
- Need consensus on exact OpenRouter API keys / budget for commercial models
- Local Ollama CPU performance validation for 7B/8B models on student laptops

## Routing Table

Load the relevant file based on the current task. Always load `context/architecture.md` first if not already in context this session.

| Task type | Load |
|-----------|------|
| Team coordination, ownership, branch rules | `context/team.md` |
| Understanding how the system works | `context/architecture.md` |
| Working with a specific technology | `context/stack.md` |
| Writing or reviewing code | `context/conventions.md` |
| Making a design decision | `context/decisions.md` |
| Setting up or running the project | `context/setup.md` |
| Course rules, grading, GitLab workflow | `docs/course-rules.md` |
| Any specific task | Check `patterns/INDEX.md` for a matching pattern |

## Behavioural Contract (3-Contributor Aware)

For every task, follow this loop:

1. **CONTEXT** — Load the relevant context file(s) from the routing table above. Check `context/team.md` to ensure your task doesn't conflict with another contributor's domain. Check `patterns/INDEX.md` for a matching pattern.
2. **BRANCH** — Ensure you are on a properly named feature branch (`feat/<name>-<topic>`). Never work directly on `main`.
3. **BUILD** — Do the work within your assigned module (`src/<module>/`). Keep changes isolated. Follow established patterns.
4. **VERIFY** — Run the Verify Checklist from `context/conventions.md`. Check that linting passes and tests succeed.
5. **MEX CHECK** — If your change modified architecture, interfaces, or conventions, update the corresponding `.mex/context/` file in the same change.
6. **GROW** — After completing the task:
   - If no pattern exists for this task type, create one in `patterns/`.
   - Update "Current Project State" above if significant milestones were reached.
