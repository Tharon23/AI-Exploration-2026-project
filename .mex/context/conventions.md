---
name: conventions
description: Code style, naming, git branching, commit format, and verification checklist for the 3-person team.
triggers:
  - "convention"
  - "pattern"
  - "naming"
  - "style"
  - "how should I"
  - "what's the right way"
edges:
  - target: context/architecture.md
    condition: when a convention depends on system structure
  - target: context/team.md
    condition: when branching or assigning ownership
last_updated: 2026-10-07
---

# Conventions

## Git & Branching (3 Contributors)

- **Main Branch**: Protected. Direct pushes forbidden. All changes via Pull Request.
- **Branch Naming**: format `<type>/<contributor>-<short-description>`
  - Examples: feat/kalab-pipeline-core, feat/bartek-eval-metrics, feat/kamil-docker-setup
  - Types: feat, fix, docs, refactor, test, chore
- **Commit Format**: Conventional Commits strictly enforced:
  - Format: `<type>(<scope>): <short description in present tense>`
  - Max 72 chars for first line.

## Code Style & Structure

- **Language**: Python 3.11+ (typed, PEP 8)
- **Formatting**: `black` (line length 100) + `ruff` for linting
- **Type Hints**: Strict typing everywhere — all function signatures must have type annotations
- **File Naming**: snake_case for Python modules, kebab-case for documentation
- **Configs**: Pydantic `BaseSettings` for all configurations, loaded from `.env`
- **No Global State**: Pass dependencies explicitly

## Experiment Recording Convention (AGH Course Rule)

Every experiment output must include this metadata header:
```json
{
  "experiment_id": "exp-001",
  "timestamp": "2026-10-07T12:00:00Z",
  "contributor": "kalab",
  "model": {
    "name": "gpt-4o",
    "version": "2024-11-20",
    "provider": "openai",
    "tier": "paid",
    "parameters": {"temperature": 0.2, "max_tokens": 4096}
  },
  "prompt_template": "src/pipeline/prompts/template.txt",
  "raw_prompt": "...",
  "metrics": {}
}
```

## Verify Checklist

Before committing or opening a PR, every contributor must verify:
- [ ] Code is formatted with `black` and passes `ruff` checks
- [ ] All new functions/classes have type annotations
- [ ] No hardcoded API keys or secrets (check `.env` usage)
- [ ] Branch follows convention
- [ ] Commit message follows Conventional Commits
- [ ] If architecture, dependencies, or conventions changed: `.mex/` files updated in same commit
- [ ] Tests pass (if tests exist for touched module)
