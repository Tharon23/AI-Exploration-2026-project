# System Verification & Onboarding Prompt (Copy & Paste)

> Wklej poniższy prompt do swojego asystenta AI (Antigravity, Cursor, Claude Code, Copilot) w świeżo sklonowanym repozytorium, aby przeprowadzić pełny audyt środowiska i gotowości do pracy zespołowej.

---

```markdown
Jesteś agentem AI w projekcie **AI Exploration 2026** (AGH UST, Cyber rok 3).
Twoim celem jest przeprowadzenie pełnego testu diagnostycznego i audytu gotowości środowiska dla zespołu (Kalab, Bartek, Kamil).

Wykonaj poniższe kroki weryfikacyjne punkt po punkcie, uruchamiając komendy w terminalu i sprawdzając pliki:

### 1. Weryfikacja Git & Hooków
- Sprawdź bieżącą gałąź (`git branch --show-current`).
- Upewnij się, że nie commitujesz bezpośrednio do `main`.
- Sprawdź, czy hook `.git/hooks/pre-commit` istnieje i jest wykonywalny. Jeśli nie, uruchom `setup.bat` (Windows) lub `bash setup.sh` (Linux).

### 2. Weryfikacja Środowiska Python & Zależności
- Sprawdź wersję Pythona (`python --version`, wymagany Python 3.11+).
- Uruchom test importów podstawowych bibliotek:
  `python -c "import pydantic, tabulate, dotenv; print('Core dependencies OK!')"`
- Sprawdź czy `src/core/interfaces.py` oraz `src/pipeline/providers/jev.py` importują się poprawnie:
  `python -c "from src.core.interfaces import ModelRequest, DecisionRequest; from src.pipeline.providers.jev import JevProvider; print('Interfaces & Jev Provider OK!')"`

### 3. Weryfikacja Konfiguracji Środowiskowej (.env)
- Sprawdź, czy plik `.env` istnieje w katalogu głównym.
- Upewnij się, czy zmienna `CONTRIBUTOR_NAME` jest ustawiona na jedno z: `kalab`, `bartek`, `kamil`.

### 4. Weryfikacja Agency Agents (.gemini/agents/)
- Sprawdź obecność 13 agentów w katalogu `.gemini/agents/`:
  - Core AI: `engineering-ai-engineer.md`, `engineering-multi-agent-systems-architect.md`, `engineering-rag-pipeline-engineer.md`, `engineering-prompt-engineer.md`
  - Support: `engineering-software-architect.md`, `engineering-codebase-onboarding-engineer.md`, `engineering-git-workflow-master.md`, `engineering-technical-writer.md`
  - Strategy: `product-manager.md`, `project-manager-senior.md`, `research-synthesist.md`, `product-trend-researcher.md`, `design-ux-researcher.md`
- Potwierdź, że potrafisz przeczytać i wcielić się w te persony podczas realizacji zadań.

### 5. Weryfikacja Pamięci Trwałej .mex/ (Promexeus)
- Uruchom komendę audytu dryfu pamięci:
  `npx promexeus check`
- Upewnij się, że wynik wynosi dokładnie **Drift score: 100/100 (0 errors, 0 warnings)**.
- Przeczytaj `.mex/ROUTER.md` i podaj bieżący stan projektu oraz reguły zachowania.

### 6. Weryfikacja Danych Badawczych GitLab
- Sprawdź obecność skatalogowanych projektów w `research/`:
  - `research/previous-projects/full-project-catalog.md` (30+ projektów z 2024-2026)
  - `research/previous-projects/instructor-evaluation-analysis.md` (kryteria oceny dr. Bułata)
  - `research/trending_and_jev_analysis.md` (analiza Jev AI i trendów)

Po wykonaniu testów wygeneruj podsumowanie w formie tabeli:
| Krok | Status | Szczegóły |
i potwierdź: "Środowisko jest w 100% gotowe do współpracy zespołowej."
```
