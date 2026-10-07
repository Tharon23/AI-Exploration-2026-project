# AI Exploration 2026 — AGH Cyber Year 3

## Project Context
University project for AI Exploration course at AGH UST, Cybersecurity 3rd year.
Full project managed via GitLab (source of truth for grading, sprint issues, wiki archive).
This GitHub repo = working space for our 3-person team: **Kalab** (lead), **Bartek**, **Kamil**.

## Persistent Memory: .mex/
This project uses `.mex/` as canonical persistent context across all AI harnesses (Antigravity, Cursor, Claude Code, Copilot).
- Always read `.mex/ROUTER.md` before starting any session.
- Keep `.mex/context/` synchronized with code changes.

## Team Structure & Ownership
| Contributor | Focus | Modules | Branch Prefix |
|-------------|-------|---------|---------------|
| **Kalab** (Lead) | Architecture, AI pipelines, agents | `src/core/`, `src/pipeline/` | `feat/kalab-*` |
| **Bartek** | Evaluation, benchmarks, metrics | `src/evaluation/` | `feat/bartek-*` |
| **Kamil** | Infra, Docker deploy, CLI/UI | `src/deploy/`, `src/ui/` | `feat/kamil-*` |

## Non-Negotiables
1. **Never commit directly to `main`**: Always use feature branches (`feat/<name>-<topic>`). PR required.
2. **Never hardcode secrets/keys**: Use `.env` with python-dotenv.
3. **Always record experiment metadata**: Model name, version, tier, prompt, and parameters in every output.
4. **No monolithic files**: Modular architecture strictly separated by ownership.
5. **Sync mex with code**: If architecture or conventions change, update `.mex/context/` in the same commit.

## Installed Agency Agents (`.gemini/agents/`)
- **Core AI**: AI Engineer, Multi-Agent Architect, RAG Pipeline, Prompt Engineer
- **Support**: Software Architect, Codebase Onboarding, Git Workflow Master, Tech Writer
- **Strategy**: Product Manager, Senior PM, Research Synthesist, Trend Researcher, UX Researcher

## Workflow Rules
1. Feature branches → PR with at least 1 team review → merge to `main`
2. Conventional Commits enforced (`feat(...)`, `fix(...)`, `docs(...)`)
3. Issue-driven: GitLab issue with `grupa:group_nazwa_grupy` and `~sprint_XX` tags
4. Sprint lifecycle: `Open` → `Doing` → `Review` (day before lab) → `Closed` (after wiki update)

## Current Phase
**Phase 0: Discovery** — GitLab scraped, team environment configured, brainstorming project ideas.
