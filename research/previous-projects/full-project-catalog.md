# AI Exploration — Pełny Katalog Projektów z GitLab AGH

> Scraped: 2026-10-07 | Source: gitlab.tele.agh.edu.pl/kwant/
> Prowadzący: kwant (prof. z Instytutu Telekomunikacji AGH)

---

## Spis Treści

1. [Zasady kursu](#zasady-kursu)
2. [Projekty 2026 (bieżący rok)](#projekty-2026)
3. [Projekty 2024/2025 (poprzedni rok)](#projekty-20242025)
4. [Analiza tematów i inspiracje](#analiza-tematów-i-inspiracje)
5. [Grupy i format pracy](#grupy-i-format-pracy)

---

## Zasady Kursu

- **Grupy**: 2–4 osoby
- **Sprinty**: tygodniowe (wyjątkowo 2-tygodniowe)
- **Ocenianie sprintów**: 0 (nic), 1 (tak sobie), 2 (zrobione), 3 (pod wrażeniem)
- **Ocena lab**: 70% sumy sprintów + 30% działający projekt (kontener/deploy/binarka)
- **Ocena projekt**: średnia z prezentacji
- **Workflow**: issue-based na GitLab Boards (Open → Doing → Review → Closed)
- **Raportowanie**: Activity w issues z etykietą sprintu (~sprint_XX)
- **Wiki**: po zakończeniu tematu → przenieść do wiki, uporządkować, zamknąć issue
- **Prezentacje**: min. 3x w semestrze, on-site
- **Pokazy**: 11.12.2026 12:00–15:00, budynek B9, 2. piętro

### Wymagania do wyników
- Podawać: model, wersję, datę testu, plan (free/paid), ustawienia, prompt (nie screenshot)
- Powtarzać ten sam prompt wielokrotnie → sprawdzić wariancję
- Testować darmowe i komercyjne modele

---

## Projekty 2026

### #17: AI jako asystent diagnostyki GNU/Linux
**Grupa**: group_Radio17
**Temat**: Testowanie LLM jako interaktywny diagnostyk Linux (Arch, Gentoo).
**Kluczowe**: Czy model zbiera właściwe logi? Czy radzi sobie z nietypowym sprzętem (NVIDIA Optimus, Dual-Boot)? Czy unika halucynacji w komendach CLI?

### #16: Video-to-Audio — AI jako dźwiękowiec
**Grupa**: group_RNG
**Temat**: Udźwiękowienie niemych klipów wideo. Model video-to-audio (MMAudio) vs pipeline LLM+TTS (Gemini+ElevenLabs).
**Ocena**: Ślepa ankieta, skala 1-5 (dopasowanie, sync, realizm).

### #15: LLM Paragrafy i Role — Gry Paragrafowe i AI
**Grupa**: group_Archmagosi_Omnisjasza

### #14: Generowanie gier przez LLM
**Grupa**: group_ZyblikiSlowiki
**Temat**: Snake, Tetris, Saper w HTML/JS generowane przez komercyjne LLM.
**Modele**: flagowe OpenAI, Anthropic, Google.
**Eksperymenty**: one-shot, naprawa (limit 10 tur), rozbudowa jednej gry.

### #13: Chatbot AI jako algorytm rekomendacji mediów społecznościowych
**Grupa**: group_Radio17
**Temat**: Czy LLM zastąpi klasyczny algorytm rekomendacyjny? Profilowanie z historii, skalowalność kontekstu, porównanie AI vs tradycyjny silnik.

### #12: AI Crime Benchmark
**Temat**: Fikcyjne sprawy kryminalne. Tryby: pełna sprawa, etapowa, z fałszywym tropem, ze sprzecznością, z ograniczonym kontekstem.

### #11: LLM zawód typer
**Grupa**: grupa_hazard

### #10: Ewaluacja modeli decyzyjnych
**Grupa**: group_motor

### #8: Analiza cenzury i wariancji geolokalizacyjnej LLM
**Temat**: Wpływ kraju pochodzenia modelu i geolokalizacji (VPN) na prezentację kontrowersyjnych faktów historycznych. Eksperyment 1: cenzura, Eksperyment 2: VPN, Eksperyment 3: symetria etyczna.

### #7: Wirtualny radiowiec — alter AI ego
**Grupa**: group_Radio17
**Temat**: Klonowanie głosu prowadzącego radiowego. Test odsłuchowy: czy ludzie odróżnią AI od prawdziwego?

### #6: AI jako projektant sieci teleinformatycznych
**Grupa**: group_Radio17
**Temat**: Projektowanie złożonej sieci dla firmy 100-300 osób. Przełączniki, routery, firewall, VLAN, UPS, redundancja.

### #5: AI vs Code Rot
**Grupa**: group_Radio17
**Temat**: Czy AI naprawi stary kod, który nie kompiluje się na nowym GCC? Ubuntu 8.04 → 22.04.

### #4: Inżynieria wsteczna protokołów sieciowych z AI
**Grupa**: group_Radio17
**Temat**: Analiza dumpów Wireshark. Identyfikacja pól, komunikatów, generowanie dokumentacji Protocol Buffers.

### #3: Portowanie starego kodu między platformami
**Grupa**: group_Radio17
**Temat**: MASM→NASM, DOS→SDL, Amiga/C64. Testowanie na kodzie Doom, Hexen, Quake, FreeDOS.

---

## Projekty 2024/2025

### Automatyzacja & Orkiestracja
| Projekt | Grupa | Opis |
|---------|-------|------|
| DeepShorts | CyberSzpont | Pełny pipeline YouTube Shorts: n8n + LLM + DALL-E + ElevenLabs |
| AI Beta Tester | spiruś | Autonomiczny agent testujący web app wizualnie (screenshot→LLM→akcja) |
| Agent AI — asystent planowania | RTN | Planowanie dnia na 2 tygodnie, integracja z kalendarzem |
| Theory of Mind w LLM (multi-agent) | Ekipa_z_Jeepa | CrewAI/LangChain, 3 agenci: Generator, Tester, Sędzia |

### Multimodal AI
| Projekt | Grupa | Opis |
|---------|-------|------|
| MacroCalc AI | JuiceSellers | VLM analiza zdjęć jedzenia → makroskładniki |
| No-Keyboard Design | pszczoly | UI design tylko głosem + Visual Grounding |
| Promptografia | prompciki | Fotorealizm bez aparatu, prompty do text-to-image |
| Generowanie komiksów | modelivo | Spójność postaci, emocje, układ stron |
| Pose Estimation | Mocnygas | MediaPipe vs YOLO-Pos vs OpenPose |

### Audio & Video
| Projekt | Grupa | Opis |
|---------|-------|------|
| Audiodeskrypcja filmów | ruterki | Streszczanie + generowanie opisów audio/wideo |
| Egalitarian Monologue | KoszenieTrawnikówTANIO | Speaker diarization: pyannote, diart, resemblyzer |

### Gry & Symulacje
| Projekt | Grupa | Opis |
|---------|-------|------|
| Poker Battle Royale LLM | UPOST | Texas Hold'em między LLM, analiza blefowania |
| G(ame)AIboy | MPM | Reinforcement Learning w grach |

### NLP & Analiza Tekstu
| Projekt | Grupa | Opis |
|---------|-------|------|
| Radca Prawny AI | JuiceSellers | Ocena porad prawnych z ChatGPT, Gemini, Grok |
| Analiza regulaminów | ruterki | Wykrywanie klauzul niedozwolonych |
| Context poisoning | Żymianie | Podatność LLM na fałszywe informacje |
| Wpływ promptów na jakość | Mocnygas | Systematyczna analiza prompt engineering |
| Jakość tłumaczeń | Żymianie | Porównanie jakości tłumaczeń między modelami |
| Dylematy moralne vs AI | petarda | Rozumowanie etyczne modeli |

### Security & Forensics
| Projekt | Grupa | Opis |
|---------|-------|------|
| Boty/ekstremiści na forach | Mocnygas | Wykrywanie botów i kont ekstremalnych |
| Nauka języków z AI | giga_hackerzy | TalkPal, SpeakPal, Talkio, Loora, Gliglish |

### Muzyka & Media
| Projekt | Grupa | Opis |
|---------|-------|------|
| Modele do muzyki | rybak2 | Analiza artefaktów, ankiety, rola AI w kulturze muzycznej |

---

## Analiza Tematów i Inspiracje

### Trendy wspólne
1. **LLM Evaluation** — większość projektów to benchmarki: "czy model X radzi sobie z Y"
2. **Multi-agent** — Theory of Mind, AI Beta Tester, DeepShorts pipeline
3. **Multimodal** — VLM, TTS, image gen, video gen
4. **Cybersecurity-adjacent** — reverse engineering, code rot, protocol analysis, bot detection
5. **Autonomous agents** — samodzielne testowanie, planowanie, diagnostyka

### Luki do wypełnienia (nikt tego nie robił)
- **Red Team / Blue Team LLM** — wspomniane jako inspiracja ale niezrealizowane
- **Rozproszone LLM** — wspomniane (4×GTX4090) ale brak projektu
- **Prompt injection attacks** — wymienione jako kategoria, brak realizacji
- **Rozpoznawanie zwierząt z kamer** — niepodjęte
- **Długi kontekst (1M tokens)** — niezbadane
- **Lokalne LLM (7-14B, kwantyzacja, telefon)** — wspomniane, brak pełnego projektu

### Inspiracje dla naszego projektu (Cyber 3 rok)
1. **Automated Pentesting** — agent AI atakujący web app (rozszerzenie AI Beta Tester)
2. **Malware deobfuskacja** — LLM vs obfuscated code
3. **Multi-agent security pipeline** — Generator exploitów → Tester → Ewaluator
4. **Prompt injection benchmark** — systematyczne testowanie guardrails
5. **AI forensics** — analiza logów, PCAP, timeline reconstruction

---

## Grupy i Format Pracy

### Format issue na GitLab
```
Opis: cel, eksperymenty, co chcemy sprawdzić
Linia identyfikująca: grupa:group_nazwa_grupy
Activity: raport z bieżącego sprintu + etykieta ~sprint_XX
```

### Specjalne issues
- `#1` — podział na grupy
- `#2` — aktualne punkty/oceny

### Harmonogram
Google Doc z podziałem na czwartki: [link w wiki]

### Wiki
Po zakończeniu projektu → wiki z raportem, materiały w repozytorium (tekst, obrazki, audio, filmy).
