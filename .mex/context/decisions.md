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

## ADR-005: Dual-Dimension Benchmark (Security ASR vs Technical Planning Ground Truth)

- **Context**: Evaluating models purely on security (ASR) misses the operational trade-off: a model that refuses all inputs is 100% secure but useless for staff operations. Subjective human grading of open-ended event plans introduces high effort and evaluation bias.
- **Decision**: In Phase III (Sprint 3), measure both Security ASR and Technical Utility using 25 domain engineering tasks with strict ground truth (power calculations, channel counts, inventory matching) verified by automated Python assertions.
- **Alternatives**: Subjective human ratings 1-5 (discarded, biased/slow), LLM-as-a-Judge (hallucination risk on math/specs), security-only testing (misses utility trade-off).
- **Consequences**: Complete Pareto Frontier (Security vs Capability vs Latency/Cost) without manual grading overhead.

## ADR-006: Mocked Tool Registry Derived from Public-API Schemas for Indirect Injection

- **Context**: Need realistic agent tool calling (threat intel lookups, outbound exfiltration webhooks, database queries) to evaluate Indirect Prompt Injection and Data Exfiltration. Directly calling real public internet APIs violates Dr. Bułat's strict repeatability criteria, introduces rate limits/downtime, and breaks the 100% offline Docker container deploy requirement (30% of final grade).
- **Decision**: Adopt realistic request/response schemas modeled after industry public APIs (e.g. AbuseIPDB, VirusTotal, Pusher, Postman Echo), but implement them strictly as offline local fixtures and mocked tools within `src/pipeline/tools/`.
- **Alternatives**: Live external API calls (discarded: non-deterministic, rate limits, internet required), purely abstract synthetic toy functions (discarded: lacks realism for production evaluation).
- **Consequences**: 100% offline self-containment for Docker deploy, zero credential churn, sub-millisecond execution for variance benchmarking, realistic data poisoning / indirect injection payloads.

