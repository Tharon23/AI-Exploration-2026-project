---
name: agents
description: Always-loaded project anchor. Read this first. Contains project identity, non-negotiables, commands, and pointer to ROUTER.md for full context.
last_updated: 2026-10-07
---

# AI Exploration 2026 — AGH UST Cyber Year 3

## What This Is
A university AI exploration and evaluation project by Kalab, Bartek, and Kamil for the AI Exploration course at AGH UST (Cybersecurity, 3rd year).

## Non-Negotiables (Hard Rules)
1. **Never commit directly to `main`**: All work via `feat/<name>-*` or `fix/<name>-*` branches. PR required with 1+ review.
2. **Never hardcode secrets or API keys**: Always load from `.env` via environment variables.
3. **Never modify `.mex/` architecture without updating code, and vice versa**: Keep docs and code in strict sync.
4. **Always record experiment metadata**: Model name, version, tier, prompt, and parameters must accompany all benchmark outputs (course requirement).
5. **No monolithic files**: Code strictly separated into `src/core/`, `src/pipeline/`, `src/evaluation/`, `src/deploy/`, `src/ui/`.

## Team Roles & Ownership
- **Kalab** (`Tharon23`): Architecture, AI pipelines, agent orchestration (`src/core/`, `src/pipeline/`)
- **Bartek**: Evaluation, benchmarks, data analysis (`src/evaluation/`)
- **Kamil**: Infrastructure, Docker, deployment, CLI/UI (`src/deploy/`, `src/ui/`)

## Commands
- Mex Drift Check: `npx promexeus check`
- Mex Sync: `npx promexeus sync`
- Format: `black .`
- Lint: `ruff check .`
- Test: `pytest`

## Scaffold Growth
After every task: if no pattern exists for the task type you just completed, create one. If a pattern or context file is now out of date, update it. The scaffold grows from real work, not just setup. See the GROW step in `ROUTER.md` for details.

## Navigation
At the start of every session, read `ROUTER.md` before doing anything else.
For full project context, patterns, and task guidance — everything is there.
