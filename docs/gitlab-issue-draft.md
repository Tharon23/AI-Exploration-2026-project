# Zgłoszenie projektu na GitLab: AI Exploration 2026

Gotowe teksty do wklejenia na GitLabie kursowym (`gitlab.tele.agh.edu.pl/kwant/ai-exploration-2026`).

---

## 1. Tytuł issue

```text
Red-Blue Głośniej: Bezpieczeństwo i testy penetracyjne asystenta AI w branży nagłośnieniowo-eventowej
```

---

## 2. Opis issue (Description)

> Pierwsza linijka z prefiksem `grupa:group_` jest wymagana przez skrypt weryfikacyjny kursu.

```markdown
grupa:group_BlueMoon

# Red-Blue Głośniej: Bezpieczeństwo i testy penetracyjne asystenta AI w branży nagłośnieniowo-eventowej

## 1. Cel projektu
Celem projektu jest stworzenie aplikacji biznesowej zawierającej asystenta AI w formie chatbota oraz przeprowadzenie wzajemnych testów bezpieczeństwa (w formule Red Team vs Blue Team) we współpracy z drugą grupą projektową.

Aplikacja ma odzwierciedlać realne środowisko biznesowe firmy zajmującej się nagłaśnianiem imprez, eventów i koncertów. Nasz zespół (Blue Team) przygotuje kompletną aplikację z asystentem AI, opracuje realistyczne scenariusze biznesowe, spreparuje dane, zdefiniuje listę celów i metryki sukcesu ataków, a także wdroży mechanizmy obronne oraz system zbierania logów w celu detekcji incydentów. 

W drugim etapie projektu nasz zespół przyjmie rolę atakującego (Red Team) i przeprowadzi testy penetracyjne aplikacji przygotowanej przez drugą grupę, wykorzystując m.in. metodykę OWASP Top 10 for LLM Applications, autorskie skrypty oraz zróżnicowane modele językowe (open-source i infrastrukturę Instytutu).

## 2. Architektura i funkcjonalności aplikacji (Blue Team)
- **Środowisko biznesowe:** Wzorowane na firmie nagłośnieniowej (baza sprzętu audio, ridery techniczne, cenniki, harmonogramy realizacji, dane kontaktowe organizatorów i artystów).
- **Asystent AI (Chatbot):** Asystent wspierający użytkowników (np. obsługa zapytań o wyceny, dobór sprzętu pod rider, informacje organizacyjne).
- **Spreparowane dane i cele (Flags / Canary Data):** Przygotowanie bazy danych z kontrolowanymi danymi wrażliwymi stanowiącymi cele dla grupy atakującej (umożliwiające jednoznaczną weryfikację wycieku).
- **Dostępność dla atakujących:** Architektura zaprojektowana w sposób transparentny i dostępny dla drugiej grupy (konteneryzacja, udostępnione endpointy/interfejs).

## 3. Ochrona, detekcja i metryki sukcesu
- **Lista celów i metryki sukcesu ataków:** Jasno zdefiniowane kryteria sukcesu dla grupy atakującej (np. wyciek poufnych cenników, ominięcie ograniczeń ról, zmiana instrukcji systemowych).
- **Mechanizmy ochronne:** Wdrożenie zabezpieczeń przed atakami typu Prompt Injection, Jailbreak oraz nieautoryzowaną eksfiltracją danych.
- **System zbierania logów:** Rejestracja zapytań i odpowiedzi (prompty, kontekst, metadane) w celu wykrywania i analizy prób ataków w czasie rzeczywistym oraz post factum.

## 4. Faza ofensywna (Red Team)
- Przeprowadzenie kontrolowanych ataków na analogicznie przygotowaną aplikację drugiej grupy.
- Zastosowanie technik zgodnych z OWASP Top 10 for LLM Applications (Direct/Indirect Prompt Injection, Sensitive Information Disclosure, Insecure Output Handling).
- Wykorzystanie modeli open-source, lokalnego LLM z infrastruktury Instytutu oraz ręcznie opracowanych skryptów testowych.

## 5. Plan pracy
1. **Przygotowanie aplikacji bazowej:** Adaptacja aplikacji, spreparowanie danych biznesowych i uruchomienie chatbota.
2. **Definicja scenariuszy i celów:** Opracowanie scenariuszy użycia, listy celów (flag) oraz metryk sukcesu ataków dla grupy atakującej.
3. **Mechanizmy obrony i audytu:** Wdrożenie zabezpieczeń promptu oraz systemu logowania zdarzeń w celu detekcji ataków.
4. **Konfiguracja modeli:** Podpięcie modeli open-source oraz lokalnego LLM z infrastruktury Instytutu.
5. **Testy penetracyjne (Red Teaming):** Przeprowadzenie ataków na aplikację drugiej grupy, zbieranie dowodów podatności.
6. **Raportowanie:** Opracowanie raportu końcowego podsumowującego skuteczność obrony, wykryte ataki oraz wyniki fazy ofensywnej.
```

---

## 3. Pierwszy komentarz w Activity (Podział ról i organizacja pracy)

```markdown
## Organizacja pracy i podział ról w zespole (group_BlueMoon)

### Założenia organizacyjne
1. **Współpraca z drugą grupą:** Wymiana dostępów do skonteneryzowanych środowisk testowych oraz uzgodnienie formatu metryk sukcesu (flagi wycieku danych).
2. **Detekcja w logach:** Wszystkie interakcje z chatbotem będą logowane w ustrukturyzowanym formacie (timestamp, IP/sesja, prompt wejściowy, odpowiedź, flagi anomalii), co pozwoli zweryfikować, kiedy i jak atakujący próbowali przełamać zabezpieczenia.
3. **Infrastruktura:** Wykorzystanie lokalnych modeli oraz zasobów Instytutu (OpenAI-compatible API) do testów i ewaluacji.

### Wstępny podział ról
- **Kamil:** Przygotowanie i konteneryzacja aplikacji bazowej (branża nagłośnieniowa), spreparowanie danych biznesowych oraz implementacja asystenta AI.
- **Bartek:** Opracowanie scenariuszy ataków (OWASP Top 10 for LLM), skryptów testowych dla fazy Red Team oraz definicja metryk sukcesu wycieków.
- **Kalab:** Wdrożenie mechanizmów ochronnych (guardrails), systemu zbierania i analizy logów (detekcja ataków Blue Team) oraz konfiguracja modeli na infrastrukturze Instytutu.
```
