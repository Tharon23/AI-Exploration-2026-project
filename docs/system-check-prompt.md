# System Verification & Onboarding Prompt (Copy & Paste)

> Wklej poniższy prompt do swojego asystenta AI (Antigravity, Cursor, Claude Code, Copilot) w lokalnym repozytorium po wykonaniu `git pull origin main`, aby przeprowadzić pełny audyt środowiska, działania Jev AI i gotowości do pracy zespołowej.

---

```markdown
Jesteś agentem AI w projekcie **AI Exploration 2026** (AGH UST, Cyber rok 3).
Twoim celem jest przeprowadzenie pełnego testu diagnostycznego i audytu gotowości środowiska dla zespołu (Kalab, Bartek, Kamil).

Wykonaj poniższe kroki weryfikacyjne punkt po punkcie, uruchamiając komendy w terminalu i sprawdzając pliki:

### 0. Synchronizacja Repo & Przeładowanie Hooków
- Upewnij się, że masz najnowsze zmiany: `git pull origin main`.
- Jeśli instalowałeś repo wcześniej, przeładuj hooki:
  - Windows: `setup.bat` (lub `powershell -ExecutionPolicy Bypass -File scripts\setup-hooks.ps1`)
  - Linux/macOS: `bash setup.sh` (lub `bash scripts/setup-hooks.sh`)

### 1. Weryfikacja Git & Jev Pre-Commit Hooków
- Sprawdź bieżącą gałąź (`git branch --show-current`). Upewnij się, że pracujesz na gałęzi `feat/<twoje_imie>-*`.
- Przetestuj działanie skryptu Jev Guardrail:
  `python scripts/jev_guardrail.py`
  (Powinno zakończyć się kodem 0 bez błędów).
- Upewnij się, że hook `.git/hooks/pre-commit` zawiera odwołanie do `scripts/jev_guardrail.py`.

### 2. Weryfikacja Środowiska Python, Zależności & Jev Provider
- Sprawdź wersję Pythona (`python --version`, wymagany Python 3.11+).
- Uruchom test importów podstawowych bibliotek:
  `python -c "import pydantic, tabulate, dotenv; print('Core dependencies OK!')"`
- Uruchom test JevProvider (System One) oraz interfejsów modeli:
  `python -c "from src.core.interfaces import ModelRequest, DecisionRequest, DecisionQuestion; from src.pipeline.providers.jev import JevProvider; p = JevProvider(); r = p.decide(DecisionRequest(questions=[DecisionQuestion(id='test', type='noul', question='test')])); print(f'Jev Provider OK! Model: {r.model_name}, Latency: {r.latency_ms:.1f}ms')"`

### 3. Weryfikacja Serwera MCP Jev (dla Google Antigravity / Claude Code)
- Uruchom szybki test działania serwera MCP Jev:
  `python -c "import subprocess; p = subprocess.Popen(['python', 'scripts/mcp_jev_server.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True); p.stdin.write('{\"jsonrpc\": \"2.0\", \"id\": 1, \"method\": \"initialize\"}\n'); res = p.stdout.readline(); print('Jev MCP Server OK!' if 'jev-mcp-server' in res else 'FAIL'); p.stdin.close(); p.wait()"`

### 4. Weryfikacja Konfiguracji Środowiskowej (.env)
- Sprawdź, czy plik `.env` istnieje w katalogu głównym.
- Upewnij się, czy zmienna `CONTRIBUTOR_NAME` jest ustawiona na jedno z: `kalab`, `bartek`, `kamil`.
- Upewnij się, że w `.env` znajdują się sekcje kluczy (w tym `TYPESAFE_API_KEY` z `.env.example` — klucz może być pusty, wtedy Jev działa w trybie offline fallback).

### 5. Weryfikacja Agency Agents (.gemini/agents/)
- Sprawdź obecność 13 agentów w katalogu `.gemini/agents/`:
  - Core AI: `engineering-ai-engineer.md`, `engineering-multi-agent-systems-architect.md`, `engineering-rag-pipeline-engineer.md`, `engineering-prompt-engineer.md`
  - Support: `engineering-software-architect.md`, `engineering-codebase-onboarding-engineer.md`, `engineering-git-workflow-master.md`, `engineering-technical-writer.md`
  - Strategy: `product-manager.md`, `project-manager-senior.md`, `research-synthesist.md`, `product-trend-researcher.md`, `design-ux-researcher.md`
- Potwierdź, że potrafisz przeczytać i wcielić się w te persony podczas realizacji zadań.

### 6. Weryfikacja Pamięci Trwałej .mex/ (Promexeus)
- Uruchom komendę audytu dryfu pamięci:
  `npx promexeus check`
- Upewnij się, że wynik wynosi dokładnie **Drift score: 100/100 (0 errors, 0 warnings)**.
- Sprawdź, czy plik `docs/gitlab-issue-draft.md` (Proposal BlueMoon dla dr. Bułata) oraz ADR-004 w `.mex/context/decisions.md` są obecne i spójne.

Po wykonaniu testów wygeneruj podsumowanie w formie tabeli:
| Krok | Status | Szczegóły |
i potwierdź: "Środowisko jest w 100% gotowe do współpracy zespołowej."
```
