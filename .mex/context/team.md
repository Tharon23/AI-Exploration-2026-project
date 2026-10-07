---
name: team
description: Multi-contributor team structure, responsibilities, branching rules, and collaboration contract for Kalab, Bartek, and Kamil.
edges:
  - target: context/architecture.md
    condition: when dividing work across architectural modules
  - target: context/conventions.md
    condition: when creating branches, naming PRs, or resolving ownership
last_updated: 2026-10-07
---

# Team & Collaboration Contract

## Contributors

| Contributor | GitHub / Handle | Primary Focus | Branch Pattern |
|-------------|-----------------|---------------|----------------|
| **Kalab** (Lead) | `Tharon23` | Architecture, AI pipelines, agent orchestration | feat-kalab-*, fix-kalab-* |
| **Bartek** | TBD | Evaluation, benchmarks, data pipelines | feat-bartek-*, fix-bartek-* |
| **Kamil** | TBD | Infra, tooling, deployment (Docker/Ansible), docs | feat-kamil-*, fix-kamil-* |

> Roles are flexible but serve as default ownership to avoid merge conflicts and overlapping work.

## Multi-Contributor Rules (Non-Negotiable)

1. **Branch Isolation**: NEVER push directly to main branch. Every change via feature or fix branch.
2. **Module Ownership**: Before starting a task, claim it by creating an issue or assigning in ROUTER.md Current State.
3. **No Overlapping Edits**: Two contributors must never work on the same source file simultaneously. Architecture is deliberately modularized so each contributor has independent domains.
4. **PR Review**: Every PR requires at least 1 approval before merge to main. No self-merging without review.
5. **Sync Before Build**: Always git pull origin main before creating a new branch or starting work.
6. **Mex Sync Contract**: If your change modifies architecture, dependencies, or conventions, you MUST update `.mex/context/` in the same PR.

## Conflict Prevention Architecture

```
src/
├── core/         ← Shared interfaces & types (Kalab owns, changes require team consensus)
├── pipeline/     ← AI & Agent logic (Kalab / Bartek)
├── evaluation/   ← Benchmarks, metrics, testing suites (Bartek)
├── deploy/       ← Docker, CI/CD, scripts, infrastructure (Kamil)
└── ui/           ← CLI / Web interface / visualization (Kamil / Bartek)
```

Each contributor works in their designated subdirectory. Cross-module communication happens strictly through interfaces defined in `src/core/interfaces.py`.
