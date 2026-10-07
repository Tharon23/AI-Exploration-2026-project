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

## Installed Agency Agents (`.gemini/agents/`)
- **Core AI**: AI Engineer, Multi-Agent Architect, RAG Pipeline, Prompt Engineer
- **Support**: Software Architect, Codebase Onboarding, Git Workflow Master, Tech Writer
- **Strategy**: Product Manager, Senior PM, Research Synthesist, Trend Researcher, UX Researcher

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

### Wytyczne dla Agentów podczas Brainstormingu

Gdy użytkownik omawia lub testuje pomysły na projekt:
1. **Tryb Grill-Me / Stress-Test**:
   - Przeanalizuj pomysł pod kątem: unikalności (względem 30+ projektów z 2024-2026), wykonalności w 12-14 sprintach, dostępności modeli/danych i cyberbezpieczeństwa.
   - Wskaż potencjalne pułapki (np. brak obiektywnego ground truth, zbyt wysokie koszty API, brak możliwości stworzenia kontenera demonstracyjnego).
2. **Optymalizacja pod "3 punkty"**:
   - Zadbaj o element zautomatyzowanej ewaluacji (np. architektura wieloagentowa z sędzią AI, syntetyczny dataset testowy, automatyczny pomiar metryk).
   - Zaplanuj demonstrator (interaktywny web UI / CLI / dashboard wizualny w Dockerze).
3. **Szablon Pierwszego Issue**:
   Pomóż sformułować zgłoszenie na GitLab w standardzie:
   - **Cel projektu** (problem, teza badawcza, dlaczego to ważne).
   - **Eksperymenty** (konkretna lista scenariuszy i wariantów).
   - **Co chcemy sprawdzić** (mierzalne pytania badawcze).
   - **Porównanie modeli** (zestawienie modeli komercyjnych i lokalnych).
   - **Oczekiwany wynik / Deliverable** (demonstrator, kontener Docker, raport).
