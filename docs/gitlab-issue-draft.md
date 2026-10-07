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
- Cel badawczy: Zmierzenie skuteczności ataków (Attack Success Rate, ASR) na poszczególnych modelach oraz sprawdzenie, o ile punktów procentowych filtr System-1 (Jev) obniża wskaźnik wycieków. Porównujemy modele komercyjne, małe modele otwartoźródłowe (Qwen, Mistral, Llama) oraz modele z jawnym procesem rozumowania (DeepSeek R1).
- Cel inżynieryjny: Przygotowanie automatycznego środowiska testowego w Pythonie, które wykonuje serie powtarzalnych ataków, mierzy wariancję i weryfikuje wycieki za pomocą tokenów kontrolnych (Canary Tokens). Przygotowanie działającego demonstratora w Dockerze (Streamlit) z przełącznikiem filtru Jev ON/OFF.
- Pytanie poznawcze: Czy modele typu reasoning (DeepSeek R1 z łańcuchem myślowym CoT) są z natury bardziej odporne na manipulację, czy też rozbudowany proces myślenia ułatwia atakującemu ominięcie zabezpieczeń?

## 3. Plan prac (sprinty)

### Sprint 1: Baza danych mocka, tokeny canary i szkielet potoku
- Przygotowanie danych testowych z ukrytymi flagami kontrolnymi (format CANARY_FLAG_...).
- Klient obsługujący API chmurowe (OpenRouter) oraz modele lokalne (Ollama na CPU).
- Podpięcie Jev API jako szybkiego klasyfikatora bezpieczeństwa.
- Prosty kontener Docker ze szkieletem interfejsu w Streamlicie.

### Sprint 2: Zestaw ataków i pomiary wariancji
- Zbudowanie zestawu 50 scenariuszy testowych (OWASP LLM Top 10, obfuskacja Base64, podmiana języka, zatrute załączniki techniczne).
- Uruchomienie automatycznych testów z powtórzeniami (po 5 do 10 prób na prompt), żeby zmierzyć powtarzalność zachowania modeli.

### Sprint 3: Macierz porównawcza i analiza modeli reasoning
- Zestawienie wyników dla modeli komercyjnych (GPT-4o-mini, Claude 3.5 Haiku, Gemini Flash), modeli otwartych (Qwen 2.5, Llama 3.1) i modeli CoT (DeepSeek R1).
- Wyliczenie metryk ASR, narzutu czasowego dodawanego przez Jeva oraz kosztu zapytań.

### Sprint 4: Demonstrator, wiki i podsumowanie
- Dopracowanie panelu Streamlit (czat na żywo, testowanie ataków suwakiem Jev ON/OFF, podgląd wykresów).
- Przeniesienie surowych wyników i wniosków do GitLab Wiki, przygotowanie kontenera pod pokaz na auli.

## 4. Testowane modele
- Komercyjne: OpenAI (gpt-4o-mini), Google (gemini-2.5-flash), Anthropic (claude-3-5-haiku).
- Lokalne i otwartoźródłowe (przez OpenRouter oraz lokalnie Ollama CPU): deepseek-r1:8b (reasoning), qwen2.5:7b-instruct, llama3.1:8b-instruct (kwantyzacja Q4_K_M), mistral:7b-instruct.
- Filtr wejściowy (System-1): Jev API (typesafe.ai) oraz lokalne reguły heurystyczne.

## 5. Mierzone wskaźniki
- ASR (Attack Success Rate): Odsetek prób, w których model ujawnił token kontrolny (wartość od 0.0 do 1.0).
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

### 2. Format zapisu wyników
Każde zapytanie testowe trafia do pliku JSONL z kompletem metadanych:
- Dokładny timestamp zapytania.
- Nazwa i wersja modelu (np. meta-llama/llama-3.1-8b-instruct).
- Środowisko (OpenRouter lub lokalna instancja Ollama).
- Parametry uruchomienia (temperatura, kwantyzacja dla modeli lokalnych).
- Pełna treść promptu (w tekście, bez screenshotów).
- Stan filtru Jev (włączony / wyłączony).
- Zmierzony czas odpowiedzi w milisekundach.
- Wynik binarny: czy flaga canary została ujawniona.

### 3. Podział zadań w zespole
- Kalab (Lead): Architektura potoku, klient modeli, integracja Jev System-1 (moduły src/core/ i src/pipeline/).
- Bartek: Przygotowanie korpusu ataków, automatyczny skrypt ewaluacji i pomiar wariancji (moduł src/evaluation/).
- Kamil: Konteneryzacja w Dockerze, środowisko uruchomieniowe i interfejs w Streamlicie (moduły src/deploy/ i src/ui/).
```
