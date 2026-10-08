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
- **Decision**: Build an isolated laboratory benchmark testing Dual-LLM security (public bot vs private employee panel) with Jev API / System-1 fast routing (<100ms) and Canary Tokens for deterministic exfiltration detection. Deliverable in Streamlit + Docker. Group registered as `group_BlueMoon`. Scope expanded to include: (1) full test application environment preparation (Sprint 0: copy prod→test, dual chatbot roles, seed data), (2) model efficiency benchmark (Sprint 2.5: model-vs-task analysis, minimum viable model per task category), (3) integration with dr. Bułat's AGH infrastructure (Gemma 4, Qwen 3 via OpenAI-compatible API at zero cost), (4) evaluation of latest 2026 models (DeepSeek V4.1-Flash, Qwen3.8-Omni-Flash, Kimi K3).
- **Alternatives**: Poker assistant (discarded, duplicate), production repo coupling (discarded, unsafe).
- **Consequences**: Clear cybersecurity relevance, high reproducibility under course criteria, clean separation of team roles. Additional efficiency analysis adds practical value (cost optimization for student budget) and demonstrates infrastructure awareness (AGH GPU server utilization).

## ADR-005: Dual-Dimension Benchmark (Security ASR vs Technical Planning Ground Truth)

- **Context**: Evaluating models purely on security (ASR) misses the operational trade-off: a model that refuses all inputs is 100% secure but useless for staff operations. Subjective human grading of open-ended event plans introduces high effort and evaluation bias.
- **Decision**: In Phase III (Sprint 3), measure both Security ASR and Technical Utility using 25 domain engineering tasks with strict ground truth (power calculations, channel counts, inventory matching) verified by automated Python assertions.
- **Alternatives**: Subjective human ratings 1-5 (discarded, biased/slow), LLM-as-a-Judge (hallucination risk on math/specs), security-only testing (misses utility trade-off).
- **Consequences**: Complete Pareto Frontier (Security vs Capability vs Latency/Cost) without manual grading overhead.

## ADR-006: Red-Blue Głośniej — Cross-Group Red Teaming & Blue Teaming

- **Context**: Project format aligned with collaborative security testing between university groups. Need a realistic business domain with clear exfiltration targets and attack detection.
- **Decision**: Orient the application around an event sound reinforcement company ("Red-Blue Głośniej"). Blue Team scope: synthetic business data with canary flags, AI chatbot, defense mechanisms, and central audit logging for attack detection. Red Team scope: offensive security testing of counterpart group's LLM application using OWASP Top 10 for LLM Applications, custom scripts, and open-source / AGH institute LLMs.
- **Alternatives**: Unilateral benchmark without counterpart group interaction.
- **Consequences**: Realistic business threat modeling, objective success metrics via canary flags, dual-perspective evaluation (defense/logging vs offense).

