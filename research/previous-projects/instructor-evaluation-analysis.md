# Analiza Oceniania i Wymagań Prowadzącego (dr hab. inż. Jarosław Bułat)

> Na podstawie analizy GitLab: `AI_Exploration_2024` (Issue #2, #3, #111) oraz `ai-exploration-2026` (Board, Work Items, Issue #2).

---

## 1. Analiza Ocen z Poprzedniego Roku (Tabela `oceny` #2)

Baza punktowa: **14 sprintów × 2 pkt = 28 punktów bazowych** (odpowiednik 70% oceny końcowej, ocena 4.0).

### Najwyżej ocenione grupy (Top Performers):
| Grupa | Punkty (na 28) | Procent | Temat projektu | Dlaczego dostali max / bonus? |
|-------|----------------|---------|----------------|-------------------------------|
| **`group_CyberSzpont`** | **30.0** | **107.1%** | DeepShorts (n8n + ElevenLabs + DALL-E) | Pełny zautomatyzowany potok, działające demo, łańcuch modeli. |
| **`group_Ekipa_z_Jeepa`** | **30.0** | **107.1%** | Theory of Mind (architektura wieloagentowa) | Rygorystyczny sampling (N=18 prób), modele lokalne vs komercyjne, analiza ARC-AGI-2, embeddingi. |
| **`group_petarda`** | **30.0** | **107.1%** | Dylematy moralne vs AI | Połączone sprinty na 4 pkt, usystematyzowana metodologia, testy etyczne. |
| **`group_spiruś`** | **29.0** | **103.6%** | AI Beta Tester (autonomiczny tester) | Agent wizualny testujący web-app, screenshot→LLM→akcja. |
| **`group_tele_misie`** | **29.0** | **103.6%** | Analiza i synteza głosu | Wybitny sprint 2-tygodniowy (4 pkt), duża liczba próbek. |

---

## 2. Na Co Prowadzący Zwraca Uwagę i Co Ceni (Kluczowe Obserwacje)

Bezpośrednie cytaty z feedbacku Jarosława Bułata w komentarzach sprintów (`Issue #111`):

> **"sampling (wiele razy zapytać o to samo, obliczyć jaka będzie statystyka, użyć llm-as-a-judge)"**  
> *Prowadzący nie akceptuje pojedynczego zapytania! Wymaga wielokrotnego odpytania (min. 5-10 prób), policzenia Accuracy / Pass@k i statystycznej wariancji.*

> **"przykłady po 2-3 z każdego scenariusza, różnego stopnia skomplikowania (własne - podobne do publicznych datasetów)"**  
> *Ceni własne, unikalne datasety testowe, a nie tylko kopiowanie znanych benchmarków z HuggingFace (ochrona przed data contamination).*

> **"sami przeanalizujcie wynik, przykłady/wyniki w activity"**  
> *Wpisy w Activity muszą zawierać surowe przykłady rozumowania modeli, a nie tylko suche cyfry. Trzeba pokazać DLACZEGO model się pomylił (np. błąd perspektywy, błąd wszechwiedzy).*

> **"zastanowić się który framework agentowy wybrać, czy w ogóle użyć"**  
> *Prowadzący docenia świadomy dobór narzędzi (np. CrewAI vs LangGraph vs natywny skrypt), a nie bezmyślne dorzucanie frameworków.*

> **"porównywać w zanurzeniu" / "rozwinąć w kierunku ARC Prize"**  
> *Gdy zespół robił dobre postępy, prowadzący aktywnie kierował ich na trudniejsze, ambitniejsze tory (badanie przestrzeni embeddingów, testy abstrakcyjnego rozumowania).*

### Skrócona skala oceniania sprintów:
- **0 pkt**: Brak wpisu w Activity przed labem / brak postępu.
- **1 pkt**: "Tak sobie" — mało testów, brak ustrukturyzowanych danych, spóźniony wpis.
- **2 pkt**: "Wszystko zrobione" — regularna, poprawna praca laboratoryjna.
- **3 pkt** (oraz 4-5 pkt za sprinty podwójne): **"Byłem pod wrażeniem"** — działający kod, statystyki, lokalne modele (Ollama) zestawione z komercyjnymi, estetyczne wykresy i tabele w Activity.

---

## 3. Aktualny Stan Tablicy 2026 (Board & Work Items — stan na 2026-10-07)

### Kolumna `Doing`:
- `#17` AI jako asystent diagnostyki GNU/Linux (group_Radio17)
- `#15` LLM Paragrafy i Role (group_Archmagosi_Omnisjasza)
- `#14` Generowanie gier przez LLM (group_ZyblikiSlowiki)
- `#13` Chatbot jako algorytm mediów społecznościowych (group_Radio17)
- `#7` Wirtualny radiowiec (group_Radio17)
- `#6` AI jako projektant sieci (group_Radio17)
- `#5` Czy AI może walczyć z code rot (group_Radio17)
- `#4` Inżynieria wsteczna protokołów sieciowych (group_Radio17)
- `#3` Portowanie starego kodu (group_Radio17)

### Kolumna `Open` (Nowe zgłoszenia z dziś):
- `#20` Dynamiczna Visual Novel (Godot + LLM)
- `#19` Among Us (LLM blefowanie, dezinformacja, dedukcja)
- `#18` Rekrutacja AI (HR vs kandydat — wykrywanie manipulacji)
- `#16` Video-to-audio (AI dźwiękowiec)
- `#12` AI Crime Benchmark
- `#11` LLM zawód typer
- `#10` Ewaluacja modeli decyzyjnych (Jev vs Laya/Kev)
- `#8` Analiza cenzury i geolokalizacji LLM

---

## 4. Wnioski dla Naszego Zespołu (Cyberbezpieczeństwo 3 rok)

1. **Format formalny Issue**:
   - Tytuł: Chwytliwy, inżynierski.
   - Opis: Cel projektu, Zakres eksperymentów, Co chcemy sprawdzić (hipotezy), Zestawienie modeli, Oczekiwany wynik (Deliverable / Demo).
   - Linijka obowiązkowa: `grupa:group_<nasza_nazwa>` w opisie.
2. **Architektura pod 3 punkty**:
   - Musimy mieć **zautomatyzowany runner testów** (wielokrotne zapytania, badanie wariancji).
   - Zestawienie: **API (GPT-4o, Claude 3.5, Gemini 2.5) vs Lokalne (Llama 3.1, Qwen 2.5, DeepSeek)**.
   - **Docker** od początku jako standard uruchomieniowy.
