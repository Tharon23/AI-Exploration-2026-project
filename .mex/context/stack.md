---
name: stack
description: Technologies, libraries, tools, and runtime environment for AI Exploration 2026.
triggers:
  - "stack"
  - "tech"
  - "library"
  - "dependencies"
  - "framework"
edges:
  - target: context/architecture.md
    condition: when understanding how these technologies fit together
  - target: context/setup.md
    condition: when installing or configuring the stack
last_updated: 2026-10-07
---

# Tech Stack

## Core Technologies

- **Runtime**: Python 3.11+
- **Package & Environment Manager**: `uv` or `pip` + `venv`
- **Linting & Formatting**: `ruff` + `black`
- **Testing**: `pytest`
- **Configuration & Validation**: `pydantic` (v2), `pydantic-settings`
- **Containerization**: Docker, Docker Compose (course deliverable requirement)

## AI & LLM Integrations

- **API SDKs**: `openai`, `anthropic`, `google-genai`
- **Local Inference**: Ollama API, vLLM / HuggingFace Transformers
- **Agent Orchestration**: Native lightweight Python pipelines (Ponytail philosophy: minimal dependencies, standard library first)
- **Data Handling**: `pandas`, `numpy`, `tabulate` for benchmark outputs

## Development & Automation

- **Git & CI**: Git feature-branch workflow, pre-commit hooks
- **Scaffold / Memory**: `promexeus` (`.mex/`)
- **Documentation**: Markdown, GitLab Wiki, GitHub Flavored Markdown
