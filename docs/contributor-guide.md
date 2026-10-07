# Przewodnik dla Kontrybutorów — Kalab, Bartek, Kamil

> Projekt: AI Exploration 2026 (AGH UST, Cyber rok 3)  
> Architektura: .mex/ (promexeus) persistent context  
> Workflow: Git Feature Branch + PR + Conventional Commits  

---

## 🚀 Pierwsze Kroki (Setup w 3 minuty)

### 1. Sklonuj repo i wejdź do folderu
```bash
git clone <URL_REPOZYTORIUM>
cd AI-Exploration-2026-project
```

### 2. Zainstaluj git hooki (OBOWIĄZKOWE)
- **Linux / macOS**:
  ```bash
  bash scripts/setup-hooks.sh
  ```
- **Windows (PowerShell)**:
  ```powershell
  powershell -ExecutionPolicy Bypass -File scripts\setup-hooks.ps1
  ```
> Hooki chronią branch `main` przed przypadkowym pushem i pilnują konwencji nazw gałęzi.

### 3. Skonfiguruj plik `.env`
```bash
cp .env.example .env
```
Otwórz `.env` i ustaw swoje imię:
```ini
CONTRIBUTOR_NAME=bartek   # lub kamil / kalab
```
oraz wklej klucze API modeli (nigdy nie commituj pliku `.env`!).

### 4. Sprawdź spójność pamięci `.mex/`
```bash
npx promexeus check
```
Powinieneś zobaczyć: `Drift score: 100/100 — 0 errors, 0 warnings`.

---

## 👥 Podział Ról i Modułów

Aby uniknąć konfliktów git i nakładania się pracy, każdy ma domyślny obszar odpowiedzialności:

| Kontributor | Główny obszar | Katalog roboczy | Prefix gałęzi |
|-------------|---------------|-----------------|---------------|
| **Kalab** (Lead) | Architektura, API, pipeline modeli | `src/core/`, `src/pipeline/` | `feat/kalab-*`, `fix/kalab-*` |
| **Bartek** | Ewaluacja, metryki, benchmarki, testy | `src/evaluation/` | `feat/bartek-*`, `fix/bartek-*` |
| **Kamil** | Docker, deploy, automatyzacja, UI/CLI | `src/deploy/`, `src/ui/` | `feat/kamil-*`, `fix/kamil-*` |

Wspólne interfejsy i modele danych znajdują się w `src/core/interfaces.py`. Wszelkie zmiany w tym pliku wymagają uzgodnienia z zespołem.

---

## 🌿 Zasady Pracy z Gitem

1. **Nigdy nie commituj bezpośrednio do `main`**.
2. **Nowe zadanie = nowa gałąź**:
   - `git checkout main`
   - `git pull origin main`
   - `git checkout -b feat/<twoje-imie>-<nazwa-funkcji>`
   - Przykłady: `feat/bartek-scoring-metrics`, `feat/kamil-dockerfile`, `fix/kalab-retry-logic`
3. **Format commitów (Conventional Commits)**:
   - `feat(pipeline): dodaj obsługę modelu gemini-2.5`
   - `fix(eval): popraw obliczanie średniego opóźnienia`
   - `docs(mex): zaktualizuj konwencje`
4. **Pull Request**:
   - Każdy PR musi mieć min. 1 akceptację drugiego członka zespołu.
   - Przed zrobieniem PR sprawdź: `npx promexeus check`

---

## 🤖 Praca z Asystentami AI (Cursor, Claude Code, Antigravity, Copilot)

Cały projekt korzysta z architektury `.mex/`. Jeśli używasz Cursor/Claude/innego AI:
1. Twoje AI automatycznie czyta `.mex/ROUTER.md` na początku każdej sesji.
2. Gdy AI ma napisać kod lub zrobić zadanie, sprawdza wzorce w `.mex/patterns/INDEX.md`.
3. Jeśli zmieniasz architekturę lub dodajesz bibliotekę, upewnij się że AI zaktualizowało odpowiedni plik w `.mex/context/`.

---

## 📊 Wymagania Kursu AGH (Prowadzący)

Każdy zarejestrowany eksperyment musi mieć nagłówek JSON ze szczegółami:
- Dokładna nazwa i wersja modelu (np. `gpt-4o-2024-11-20`)
- Wersja darmowa vs komercyjna
- Parametry (temperature, seed)
- Pełna treść promptu (tekst, NIE screenshot)
- Min. 3 powtórzenia tego samego zapytania dla oceny powtarzalności

Wszystkie aktywności sprintu raportujemy na GitLabie w Activity danego Issue z tagiem `~sprint_XX`.
