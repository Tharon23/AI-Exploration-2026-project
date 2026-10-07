---
name: architecture
description: How the major pieces of this project connect and flow. Modularized for 3 concurrent contributors. Load when working on system design, integrations, or component interactions.
triggers:
  - "architecture"
  - "system design"
  - "how does X connect to Y"
  - "integration"
  - "flow"
edges:
  - target: context/stack.md
    condition: when specific technology details are needed
  - target: context/decisions.md
    condition: when understanding why the architecture is structured this way
  - target: context/team.md
    condition: when assigning or dividing work across modules
last_updated: 2026-10-07
---

# Architecture

## System Overview

```
[Input / CLI / UI] 
       │
       ▼
[Core Interfaces] ──── (contracts in src/core/interfaces.py)
       │                 • System One: Decision Models (Jev/Laya)
       │                 • System Two: Generative LLMs (OpenAI/Claude/Ollama)
  ┌────┴──────────────────────────┐
  ▼                               ▼
[AI / Agent Pipeline]   [Evaluation / Benchmark Engine]
  │                               │
  ▼                               ▼
[Model Providers API]   [Metrics & Reports Output]
(OpenAI, Anthropic,           (Markdown, JSON, CSV)
 Local Ollama/vLLM,               │
 Jev API / Laya ONNX)             ▼
                        [Deploy / Docker Artifact]
```

Flow: Input trigger (CLI argument, config file, or test case) → loaded through Core Interfaces → dispatched to AI Pipeline (with optional fast sub-100ms routing by Decision Models) → responses evaluated by Evaluation Engine → structured results saved to output directory + formatted for GitLab reporting.

## Key Components

- **`src/core/`** — Shared data contracts, types, and abstract base classes (`ModelRequest`/`Response`, `DecisionRequest`/`Response`). Any change here touches all 3 contributors and requires team consensus.
- **`src/pipeline/`** — Model interaction layer, prompt templates, agent orchestration, and API wrappers (OpenAI, Anthropic, Google, Ollama, Jev/Laya). Owned by Kalab / Bartek.
- **`src/evaluation/`** — Automated scoring, canary leakage regex matching, technical planning ground-truth assertions, metrics calculation (ASR, accuracy, latency, cost, variance), and report generation. Owned by Bartek.
- **`src/deploy/`** — Containerization (Dockerfile, docker-compose), environment provisioning, reproduction scripts, and CI automation. Owned by Kamil.
- **`src/ui/`** — Visual interface, CLI commands, or dashboard for displaying results and running live demos. Owned by Kamil / Bartek.

## External Dependencies

- **LLM APIs** — OpenAI (GPT-4o/mini), Anthropic (Claude 3.5/Sonnet), Google (Gemini 2.5/Flash), local Ollama/vLLM for open-weight models.
- **Decision Models** — Jev API (`typesafe.ai`) or local `laya` (ModernBERT ONNX) for sub-100ms classification and guardrails.
- **GitLab (AGH)** — Source of truth for grading, issue tracking (~sprint_XX), wiki documentation, and final deliverable archiving.
- **Docker** — Required for 30% of grade: final project must be runnable as a container for next year's demonstration.

## What Does NOT Exist Here

- **No monolithic single-file scripts**: All code must reside in appropriate `src/` modules.
- **No hardcoded API keys or secrets**: Always use `.env` via environment variables.
- **No ad-hoc unversioned experiments**: Every test run must record model name, exact version, parameters, prompt, and timestamp.
- **No untested commits to main**: Main branch is protected; merge only via PR with green verification.
