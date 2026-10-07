# AI Exploration 2026 — AGH Cyber Year 3

## Project Context
University project for AI Exploration course at AGH UST, Cybersecurity 3rd year.
Course Instructor: **dr hab. inż. Jarosław Bułat** (`kwant`, Instytut Telekomunikacji AGH).
Source of truth for grading, sprint issues, wiki archive: GitLab (`gitlab.tele.agh.edu.pl/kwant/ai-exploration-2026`).
Active development repo: GitHub (team: **Kalab** [lead], **Bartek**, **Kamil**).

## Persistent Memory: .mex/
This project uses `.mex/` as canonical persistent context across all AI harnesses (Antigravity, Cursor, Claude Code, Copilot).
- Always read `.mex/ROUTER.md` before starting any session.
- Keep `.mex/context/` synchronized with code changes.
- Drift check command: `npx promexeus check` (target: 100/100).

## Team Structure & Ownership
| Contributor | Focus | Modules | Branch Prefix |
|-------------|-------|---------|---------------|
| **Kalab** (Lead) | Architecture, AI pipelines, agents | `src/core/`, `src/pipeline/` | `feat/kalab-*` |
| **Bartek** | Evaluation, benchmarks, metrics | `src/evaluation/` | `feat/bartek-*` |
| **Kamil** | Infra, Docker deploy, CLI/UI | `src/deploy/`, `src/ui/` | `feat/kamil-*` |

## Non-Negotiables
1. **Never commit directly to `main`**: Always use feature branches (`feat/<name>-<topic>`). PR required.
2. **Never hardcode secrets/keys**: Use `.env` with python-dotenv.
3. **Always record experiment metadata**: Model name, exact version, tier, prompt (as text, NO screenshots), and parameters in every output.
4. **No monolithic files**: Modular architecture strictly separated by ownership.
5. **Sync mex with code**: If architecture or conventions change, update `.mex/context/` in the same commit.
6. **Mandatory Agency Agent Consultation**: Before designing architecture, pipelines, prompts, or workflows, agents MUST read and embody the corresponding specialist from `.gemini/agents/`.

---

## 🤖 Installed Agency Agents Enforcement (`.gemini/agents/`)

Every agent operating in this repository MUST explicitly reference and load instructions from `.gemini/agents/` based on task type:

| Task Type | Required Agency Agent | Path |
|---|---|---|
| **AI Model Pipeline & LLM Integrations** | AI Engineer | `.gemini/agents/engineering-ai-engineer.md` |
| **Multi-Agent Systems & Decision Routing** | Multi-Agent Systems Architect | `.gemini/agents/engineering-multi-agent-systems-architect.md` |
| **RAG, Vector & Embedding Workflows** | RAG Pipeline Engineer | `.gemini/agents/engineering-rag-pipeline-engineer.md` |
| **Prompt Engineering & Evaluation Design** | Prompt Engineer | `.gemini/agents/engineering-prompt-engineer.md` |
| **System Architecture & Boundaries** | Software Architect | `.gemini/agents/engineering-software-architect.md` |
| **Onboarding & Environment Verification** | Codebase Onboarding Engineer | `.gemini/agents/engineering-codebase-onboarding-engineer.md` |
| **Git Branching, PRs, Hooks Enforcement** | Git Workflow Master | `.gemini/agents/engineering-git-workflow-master.md` |
| **Reports, GitLab Issue & Wiki Content** | Technical Writer | `.gemini/agents/engineering-technical-writer.md` |
| **Brainstorming, Scope & MVP Slicing** | Senior Project Manager / PM | `.gemini/agents/project-manager-senior.md` |
| **Literature, SOTA & Previous Work Review** | Research Synthesist | `.gemini/agents/research-synthesist.md` |

---

## 🧰 Configured Tools & Technologies Checklist

- [x] **Python 3.11+ Core**: `pydantic` v2, `pydantic-settings`, `tabulate`, `python-dotenv`.
- [x] **Dev & Linting**: `black`, `ruff`, `pytest`.
- [x] **Model Providers (System Two)**: Standard generative client abstractions for OpenAI, Anthropic, Gemini, and Ollama.
- [x] **Decision Models (System One)**: Jev API (`typesafe.ai`), `codaaiteam/jev-ai` integration + local fallback in `src/pipeline/providers/jev.py` for sub-100ms routing and guardrails.
- [x] **Turnkey Onboarding**: `setup.bat` (Windows) and `setup.sh` (Linux) for instant environment provisioning.
- [x] **Git Protection**: Pre-commit hooks blocking `main`, enforcing branch naming (`feat/<name>-*`), and protecting against secret leaks.
- [x] **MEX Context Scaffold**: 100/100 drift score across all 16 context files.
- [x] **System Verification Prompt**: Available in `docs/system-check-prompt.md` to run self-tests anytime.

---

## 🎯 Current Phase: Phase 0 — Brainstorming & First Issue Creation

We are actively selecting our project topic and preparing our team registration (`#1`) and project issue on GitLab.

### Instructor (Jarosław Bułat) Grading Criteria & Preferences

Understanding the evaluation system is essential for achieving the highest grade (5.0 / max points):

1. **Sprint Evaluation Scale (Weekly / Bi-weekly)**:
   - `0 pkt`: Nic zrobione / brak wpisu w Activity.
   - `1 pkt`: "Tak sobie" — mały postęp, niekompletne testy, brak ustrukturyzowanych wniosków.
   - `2 pkt`: "Wszystko zrobione" — plan sprintu zrealizowany (suma 2 pkt = 70% oceny końcowej, ocena 4.0).
   - `3 pkt`: **"Byłem pod wrażeniem pracy"** — cel dla naszego zespołu! Wymaga:
     - Działającego kodu / prototypu na wczesnym etapie.
     - Zautomatyzowanego potoku testowego (np. skrypt odpalający wiele zapytań z mierzeniem wariancji).
     - Porównania modeli komercyjnych (OpenAI, Anthropic, Google) z lokalnymi open-weight (Ollama / vLLM / HuggingFace).
     - Rygoru metodologicznego (brak halucynacji w raportach, surowe dane + synteza, powtarzalność).

2. **Ocena Końcowa (Wagi)**:
   - **70% — Suma punktów ze sprintów** (zajęcia laboratoryjne).
   - **30% — Działający deploy / demonstrator** (kontener Docker, docker-compose lub binarka, pozwalający uruchomić projekt za rok dla kolejnego rocznika bez asysty autorów).
   - **Ocena z Projektu** — Średnia z min. 3 prezentacji on-site na auli przed wszystkimi grupami.

3. **Wymogi Formalne Issue na GitLabie**:
   - Identyfikator grupy w opisie: `grupa:group_nazwa_grupy` (literalnie, wymagane dla skryptu sprawdzającego).
   - Tagi sprintów w Activity: `~sprint_01`, `~sprint_02`.
   - Przeniesienie do kolumny `Review` **dzień przed terminem labu**.
   - Po zakończeniu projektu: przeniesienie materiałów do GitLab Wiki i zamknięcie issue (`Closed`).
