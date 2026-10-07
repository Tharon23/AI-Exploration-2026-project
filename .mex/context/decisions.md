---
name: decisions
description: Architectural and operational decisions, rationale, and alternatives considered.
triggers:
  - "decision"
  - "why did we"
  - "rationale"
  - "alternative"
edges:
  - target: context/architecture.md
    condition: when a decision shaped the system structure
  - target: context/team.md
    condition: when a decision affects multi-contributor workflow
last_updated: 2026-10-07
---

# Architecture Decisions (ADRs)

## ADR-001: Strict Modular Separation by Contributor

- **Context**: 3 developers (Kalab, Bartek, Kamil) working concurrently on a fast-paced university project. High risk of merge conflicts and overlapping edits.
- **Decision**: Divide `src/` into 5 strict directories (`core`, `pipeline`, `evaluation`, `deploy`, `ui`) with clear primary ownership. Shared types defined strictly in `core`.
- **Alternatives**: Monorepo with microservices (overkill), single flat package (high conflict rate).
- **Consequences**: Minimal merge conflicts, clear responsibility, easy independent testing.

## ADR-002: Ponytail / Minimal Dependency Approach

- **Context**: AI frameworks (LangChain, CrewAI) add massive abstraction overhead, fast-breaking API changes, and complex debugging.
- **Decision**: Prefer clean, native Python scripts with direct SDK calls over heavyweight agent frameworks, unless multi-agent complexity strictly requires them.
- **Alternatives**: LangChain, CrewAI, AutoGen.
- **Consequences**: Easier to debug, lower token overhead, robust and predictable execution.

## ADR-003: Mex Scaffold as Persistent Project Memory

- **Context**: Team members use various AI coding harnesses (Antigravity, Cursor, Claude Code, Copilot). Risk of AI drift across sessions.
- **Decision**: Adopt `.mex/` standard (`promexeus`) as canonical truth for architecture, conventions, and patterns across all tools.
- **Alternatives**: Plain READMEs, tool-specific prompts only.
- **Consequences**: Consistent AI behavior regardless of harness, persistent memory.

## ADR-004: Dual-LLM Security Benchmark and Jev System-1 Routing

- **Context**: Need a focused project topic for AI Exploration 2026 (Cybersecurity 3rd year). Evaluated alternatives: Poker bot analysis (redundant with 2024 UPOST project), direct production app modification (high risk).
- **Decision**: Build an isolated laboratory benchmark testing Dual-LLM security (public bot vs private employee panel) with Jev API / System-1 fast routing (<100ms) and Canary Tokens for deterministic exfiltration detection. Deliverable in Streamlit + Docker. Group registered as `group_BlueMoon`.
- **Alternatives**: Poker assistant (discarded, duplicate), production repo coupling (discarded, unsafe).
- **Consequences**: Clear cybersecurity relevance, high reproducibility under course criteria, clean separation of team roles.
