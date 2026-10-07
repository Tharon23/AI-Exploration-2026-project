---
name: add-model-provider
description: How to add support for a new LLM provider (API or local) to the pipeline.
triggers:
  - "add provider"
  - "new model"
  - "ollama"
  - "vllm"
  - "api wrapper"
edges:
  - target: context/architecture.md
    condition: when wiring provider into pipeline
  - target: context/stack.md
    condition: when checking provider SDK dependencies
last_updated: 2026-10-07
---

# Add Model Provider Pattern

## Context
Load `context/architecture.md` to review the `src/core/` provider interface contract.

## Steps
1. Create a provider client class in `src/pipeline/providers/<provider_name>.py`.
2. Implement the `BaseModelProvider` interface from `src/core/interfaces.py`.
3. Support streaming or non-streaming responses, structured outputs, and raw token usage extraction.
4. Add provider credentials to `.env.example` and Pydantic settings.
5. Write a unit test in `tests/test_<provider_name>.py` with mocked API responses.

## Gotchas
- Handle API rate limits and backoff retries using exponential backoff.
- Normalize output tokens and cost across different vendor formats.

## Verify
- [ ] Provider implements all methods of `BaseModelProvider`.
- [ ] Returns standardized `ModelResponse` with content, latency, and token counts.
- [ ] Error handling does not leak sensitive API keys in tracebacks.
