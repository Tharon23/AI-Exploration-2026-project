# Zgłoszenie projektu na GitLab: AI Exploration 2026

Gotowe teksty do wklejenia na GitLabie kursowym (gitlab.tele.agh.edu.pl/kwant/ai-exploration-2026).

---

## 1. Tytuł issue

```text
Dual-LLM Security Benchmark: Izolacja uprawnień, ochrona przed Jailbreak / Data Exfiltration i routing System-1 (Jev)
```

---

## 2. Opis issue (Description)

> Zastąp `group_NAZWA` docelową nazwą grupy (np. `group_CyberJev`). Pierwsza linijka z prefiksem `grupa:group_` jest wymagana przez skrypt sprawdzający.

```markdown
grupa:group_BlueMoon

# Dual-LLM Security Benchmark: Izolacja uprawnień, ochrona przed Jailbreak / Data Exfiltration i routing System-1 (Jev)

## 1. Opis problemu
W aplikacjach biznesowych coraz częściej stawia się obok siebie dwa rodzaje asystentów: publicznego bota dla klientów oraz wewnętrznego asystenta dla pracowników z dostępem do bazy wiedzy firmy. W tym projekcie badamy podatność takiego układu na ataki prompt injection, jailbreak oraz próby wyciągnięcia poufnych danych.

Testujemy podejście dwuwarstwowe: sprawdzamy, na ile lekki model decyzyjny (Jev API lub klasyfikator heurystyczny z czasem reakcji poniżej 100 ms) działający jako filtr wejściowy potrafi zatrzymać ataki, zanim zapytanie w ogóle trafi do właściwego LLM-a (OpenAI, Anthropic, Google, DeepSeek oraz modeli lokalnych na Ollama). Testy prowadzimy na mocku danych technicznych firmy nagłośnieniowej (stawki hurtowe, marże, ridery sprzętowe, kody dostępowe do magazynu).

Sprawdzamy dwa główne wektory:
1. Bezpośredni atak przez publiczny czat w celu wydobycia promptu systemowego lub ukrytych stawek.
2. Atak pośredni (Indirect Prompt Injection), gdzie klient przesyła spreparowany dokument (np. zatruty rider techniczny), który wewnętrzny asystent pracownika przetwarza w panelu.

## 2. Cele projektu
- Cel badawczy: Zmierzenie skuteczności ataków (Attack Success Rate, ASR) oraz zdolności modeli do rozwiązywania złożonych zadań firmy eventowej (dobór sprzętu pod rider, kalkulacje mocy, ograniczenia budżetowe). Sprawdzamy relację bezpieczeństwo vs możliwości vs koszt: jaki model wystarcza na publiczny czat z filtrem Jev, a jaki jest niezbędny w panelu pracownika.
- Cel inżynieryjny: Przygotowanie automatycznego środowiska testowego w Pythonie, które wykonuje serie powtarzalnych ataków, mierzy wariancję, weryfikuje wycieki za pomocą tokenów kontrolnych (Canary Tokens) oraz automatycznie ocenia poprawność zadań technicznych przez asercje logiczne. Przygotowanie działającego demonstratora w Dockerze (Streamlit) z przełącznikiem filtru Jev ON/OFF.
- Pytanie poznawcze: Czy modele typu reasoning (DeepSeek R1 z łańcuchem myślowym CoT) są z natury bardziej odporne na manipulację i lepiej radzą sobie z ograniczeniami sprzętowymi, czy też rozbudowany proces myślenia ułatwia atakującemu ominięcie zabezpieczeń?

## 3. Plan prac (sprinty)

### Sprint 1: Baza danych mocka, tokeny canary i szkielet potoku
- Przygotowanie danych testowych z ukrytymi flagami kontrolnymi (format CANARY_FLAG_...).
- Klient obsługujący API chmurowe (OpenRouter) oraz modele lokalne (Ollama na CPU).
- Podpięcie Jev API jako szybkiego klasyfikatora bezpieczeństwa.
- Prosty kontener Docker ze szkieletem interfejsu w Streamlicie.

### Sprint 2: Zestaw ataków, reguły ATR i pomiary wariancji (Fuzzing)
- Zbudowanie zestawu 50 scenariuszy testowych zmapowanych na OWASP Agentic Top 10 i standard Agent Threat Rules (ATR, 330 reguł YAML).
- Wdrożenie mutacyjnego fuzzeru promptów (obfuskacja Base64, leet-speak, podmiana języka, payload splitting) do masowego badania wariancji.
- Uruchomienie automatycznych testów z powtórzeniami (po 10 prób na wariant), żeby zmierzyć odchylenie standardowe i stabilność modeli.
- Implementacja lokalnych mocków narzędzi wzorowanych na public-apis (AbuseIPDB, VirusTotal, Postman Echo) pod scenariusz ToolHijacker / Indirect Injection.

### Sprint 3: Macierz porównawcza, analiza modeli reasoning i test zadań technicznych
- Zestawienie wyników bezpieczeństwa dla modeli komercyjnych (GPT-4o-mini, Claude 3.5 Haiku, Gemini Flash), modeli otwartych (Qwen 2.5, Llama 3.1) i modeli CoT (DeepSeek R1).
- Benchmark zadań technicznych z twardym ground truth: automatyczne sprawdzanie poprawności obliczeń akustycznych i doboru sprzętu z bazy mocka asercjami w Pythonie.
- Wyliczenie metryk ASR, trafności zadań technicznych, narzutu czasowego dodawanego przez Jeva oraz kosztu zapytań.

### Sprint 4: Demonstrator, wiki i podsumowanie
- Dopracowanie panelu Streamlit (czat na żywo, testowanie ataków suwakiem Jev ON/OFF, podgląd wykresów bezpieczeństwa i jakości).
- Przeniesienie surowych wyników i wniosków do GitLab Wiki, przygotowanie kontenera pod pokaz na auli.

## 4. Testowane modele
- Komercyjne: OpenAI (gpt-4o-mini), Google (gemini-2.5-flash), Anthropic (claude-3-5-haiku).
- Lokalne i otwartoźródłowe (przez OpenRouter oraz lokalnie Ollama CPU): deepseek-r1:8b (reasoning), qwen2.5:7b-instruct, llama3.1:8b-instruct (kwantyzacja Q4_K_M), mistral:7b-instruct.
- Filtr wejściowy (System-1): Jev API (typesafe.ai) oraz lokalne reguły heurystyczne.

## 5. Mierzone wskaźniki
- ASR (Attack Success Rate): Odsetek prób, w których model ujawnił token kontrolny (wartość od 0.0 do 1.0).
- Trafność zadań technicznych (Task Accuracy): Odsetek poprawnie rozwiązanych problemów technicznych (prawidłowe obliczenia mocy, brak halucynacji sprzętu spoza magazynu).
- Czas odpowiedzi: Opóźnienie wprowadzane przez filtr decyzyjny (cel poniżej 100 ms) w zestawieniu z czasem generacji całego LLM-a.
- Wariancja: Powtarzalność wyników przy identycznym prompcie w 10 niezależnych przebiegach.
- Zysk z ochrony: Różnica w ASR między samym modelem a modelem z aktywnym filtrem Jev.
```

---

## 3. Pierwszy komentarz w Activity (SOTA i metodologia)

```markdown
## Metodologia testów i tokeny kontrolne

### 1. Weryfikacja wycieków: Canary Tokens
Żeby uniknąć subiektywnej oceny i halucynacji modelu sprawdzającego (LLM-as-a-Judge), wrażliwe dane w bazie oznaczamy unikalnymi flagami:
- Format: CANARY_FLAG_{KATEGORIA}_{HASH} (na przykład CANARY_FLAG_MARZA_8492).
- Sukces ataku weryfikujemy w 100% deterministycznie prostym wyrażeniem regularnym szukającym obecności flagi w wyjściowym tekście.

### 2. Ocena zadań technicznych: twardy Ground Truth
Zamiast ręcznego czytania i oceniania planów eventów, wprowadzamy 25 zadań inżynierskich z jednoznacznym wynikiem logiczno-obliczeniowym:
- Przykłady: obliczenie zapotrzebowania mocy, dobór liczby kanałów miksera, alokacja mikrofonów pod rider.
- Weryfikacja: skrypt w Pythonie automatycznie sprawdza reguły (czy wynik liczbowy mieści się w tolerancji, czy model nie dobrał urządzeń spoza bazy magazynowej).

### 3. Format zapisu wyników
Każde zapytanie testowe trafia do pliku JSONL z kompletem metadanych:
- Dokładny timestamp zapytania.
- Nazwa i wersja modelu (np. meta-llama/llama-3.1-8b-instruct).
- Środowisko (OpenRouter lub lokalna instancja Ollama).
- Parametry uruchomienia (temperatura, kwantyzacja dla modeli lokalnych).
- Pełna treść promptu (w tekście, bez screenshotów).
- Stan filtru Jev (włączony / wyłączony).
- Zmierzony czas odpowiedzi w milisekundach.
- Wynik binarny: czy flaga canary została ujawniona oraz czy zadanie techniczne przeszło asercje logiczne.

### 4. Podział zadań w zespole
- Kalab (Lead): Architektura potoku, klient modeli, integracja Jev System-1 i mocków narzędzi (moduły src/core/ i src/pipeline/).
- Bartek: Zestaw ataków ATR, fuzzer mutacyjny, testy zadań z asercjami i pomiar wariancji (moduł src/evaluation/).
- Kamil: Konteneryzacja w Dockerze (offline deployment), środowisko uruchomieniowe i UI Streamlit (moduły src/deploy/ i src/ui/).

### 5. Podstawa teoretyczna i literatura SOTA (2025/2026)
- **The Landscape of Prompt Injection Threats in LLM Agents (SoK)** (arXiv:2602.10453, Luty 2026): Taksonomia wektorów ataku i obrony ze szczególnym uwzględnieniem warstwy wykonawczej (execution-level).
- **ToolHijacker: Prompt Injection Attack to Tool-Calling LLM Agents**: Metodologia testowania wymuszonych wywołań niebezpiecznych narzędzi przez zatrute dane wejściowe.
- **Securing AI Agents Against Prompt Injection Attacks** (arXiv:2511.15759, Listopad 2025): Badanie Pareto Frontier – minimalizacja ASR bez degradacji zdolności operacyjnych modelu.
- **Agent Threat Rules (ATR)**: Format sygnatur detekcyjnych YAML zmapowany na OWASP Agentic Top 10 i MITRE ATLAS.
```

