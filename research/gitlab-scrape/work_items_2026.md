# Work Items 2026

## [opened] Dynamiczna Visual Novel (#20)
**Author:** Krzysztof Dudzik
**Assignees:** Krzysztof Dudzik
**Created At:** 2026-10-07T10:20:25.811+02:00

### Description
# Dynamiczna Visual Novel

## Cel

Stworzenie interaktywnej gry Visual Novel w silniku Godot, w której fabuła, dialogi oraz tła są w 100% dynamicznie generowane w czasie rzeczywistym w odpowiedzi na swobodne komendy tekstowe gracza.

## Główne założenia i pętla rozgrywki
- Swoboda gracza: Brak sztywnych, predefiniowanych opcji wyboru. Gracz w oknie czatu wpisuje dowolne działanie lub kwestię dialogową
- LLM jako Narrator: Historia akcji gracza jest zapisywana i model kontynuuje historie w spójnym tonie
- Dynamiczne tła: Na podstawie wygenerowanego opisu sceny model generuje w tle aktualną lokację

## Badania
- Spójność narracyjna: Zdolność modelu do logicznego reagowania na nietypowe pomysły gracza bez gubienia wątku głównego
- Spójność wizualna
- Spójność stanu świata i faktów: Utrzymywanie niezmiennych atrybutów przedmiotów

---

## [opened] Among Us (#19)
**Author:** Krzysztof Dudzik
**Assignees:** Krzysztof Dudzik
**Created At:** 2026-10-07T10:19:05.885+02:00

### Description
# Among Us

## Cel:
Zbadanie zdolności modeli językowych do prowadzenia zaawansowanej dezinformacji, utrzymania spójnego alibi oraz logicznej dedukcji w kontrolowanym środowisku gry inspirowanej Among Us

## Opis działania:
Silnik gry (Game Master AI): W ukryciu losuje układ zdarzeń w turze (pozycja graczy na mapie, historia trasy, wykonane zadania, zabójstwo, zgłoszenie ciała) i generuje dla każdego agenta wyłącznie fragment wiedzy, który dana postać mogła zaobserwować.
Agenci Gracze:
- Niewinni: Dzielą się obserwacjami, konfrontują fakty i starają się wskazać niespójności w wypowiedziach innych
- Sabotażysta: Zna prawdę o zbrodni, ale ma za zadanie skonstruować wiarygodne alibi, manipulować faktami i przekierować podejrzenia na innych
Faza Debaty i Głosowania: Wymiana argumentów między agentami w rundzie dyskusyjnej, zakończona jawnym głosowaniem na eliminację podejrzanego lub pominięcie tury

## Główne wymiary badawcze
- Skuteczność blefu: odsetek partii, w których Impostor unika eliminacji lub doprowadza do wyrzucenia niewinnego gracza
- Odporność na manipulację: Zdolność Niewinnych do demaskowania fałszywych alibi i weryfikacji sprzeczności czasowo-przestrzennych (np. poruszania się po mapie)
- Odpowiedzi pod presją
- Efekt "kuli śnieżnej": Badanie, czy agenci w fazie głosowania bezkrytycznie popierają pierwsze rzucone oskarżenie

---

## [opened] Rekrutacja AI (#18)
**Author:** Krzysztof Dudzik
**Assignees:** Krzysztof Dudzik
**Created At:** 2026-10-07T10:09:38.174+02:00

### Description
# Rekrutacja AI
## Cel:

Projekt bada skuteczność i obiektywizm sztucznej inteligencji w procesie selekcji pracowników poprzez zderzenie ze sobą dwóch modeli językowych . Jeden model wciela się w rolę rekrutera, a drugi w kandydata. Kluczowym elementem metodologii jest nadawanie obu stronom zróżnicowanych, ukrytych założeń wstępnych (profili behawioralnych i kompetencyjnych), co pozwala na generowanie wielu unikalnych scenariuszy. Celem jest sprawdzenie, jak modele podejmują decyzje kadrowe, czy ulegają manipulacjom oraz jak radzą sobie z kłamstwem i brakiem wiedzy. 

## Opis działania:

Symulacja opiera się na modyfikowaniu instrukcji startowych dla obu uczestników wywiadu:

AI Rekruter: Otrzymuje profil stanowiska, rubrykę ocen oraz specyficzne wytyczne co do stylu prowadzenia rozmowy. Może dostać założenie bycia rygorystycznym i dociekliwym analitykiem, osobą skupioną na dopasowaniu kulturowym, lub rekruterem podatnym na znane marki w CV.

AI Kandydat: Otrzymuje zdefiniowany poziom wiedzy i ukryte motywacje. Może to być kompetentny ekspert, osoba odpowiadająca wyłącznie ogólnikami, lub kandydat bez doświadczenia

Pętla interakcji: Modele prowadzą autonomiczną wymianę zdań, a na koniec rekruter musi podjąć twardą decyzję wraz z punktacją i uzasadnieniem. 

## Główne obszary badawcze:

Statystyka decyzyjna: Jak różne postawy rekrutera wpływają na ostateczny werdykt. Mierzymy odsetek False Acceptance (zatrudnienie kandydata, który zmyślał) oraz False Rejection (odrzucenie merytorycznego eksperta ze względu na specyficzny styl komunikacji).

Weryfikacja prawdy i halucynacji: Badanie interakcji, w której zdesperowany Kandydat AI zaczyna samorzutnie wymyślać doświadczenie i fakty. Sprawdzamy, czy Rekruter AI zakwestionuje te konfabulacje, czy bezkrytycznie je zaakceptuje.

Odporność na manipulację: Weryfikacja zdolności Rekrutera do egzekwowania konkretów, gdy Kandydat unika odpowiedzi, używa pustego żargonu korporacyjnego lub stosuje techniki perswazyjne.

---

## [opened] AI jako asystent zaawansowanej konfiguracji i diagnostyki GNU/Linux (#17)
**Author:** Patryk Ordon
**Assignees:** Patryk Ordon
**Created At:** 2026-10-06T23:43:08.629+02:00

### Description
grupa:group_Radio17

# Cel
Konfiguracja i utrzymanie systemów z rodziny GNU/Linux (zwłaszcza dystrybucji nastawionych na zaawansowanych użytkowników, takich jak Arch Linux, Gentoo) stwarza liczne problemy, m.in. z powodu nietypowych konfiguracji sprzętowych (np. hybrydowe karty graficzne). Dokumentacja (np. ArchWiki) jest obszerna, ale wymaga od użytkownika umiejętności precyzyjnej diagnozy. Chcemy sprawdzić, na ile współczesne modele LLM potrafią pełnić rolę interaktywnego diagnosty i asystenta, prowadzącego użytkownika krok po kroku od instalacji, przez konfigurację sterowników i usług systemowych, po rozwiązywanie krytycznych awarii.

# Eksperymenty
Sprawdzić między innymi:
- Zbieranie danych diagnostycznych: ocena, czy model potrafi samodzielnie prosić o właściwe logi i wyniki komend diagnostycznych (np. journalctl, systemctl status) zamiast zgadywać przyczynę problemu.
- Radzenie sobie ze skomplikowanym/nietypowym sprzętem: scenariusze konfiguracji przełączania kart graficznych (NVIDIA Prime / Optimus), ustawianie podwójnego rozruchu (Dual-Boot z Secure Boot), konfiguracja niestandardowych modułów kernela.
- Rozwiązywanie awarii: generowanie instrukcji naprawczych i sprawne prowadzenie w nich użytkownika.
- Czytelność i precyzję instrukcji: spójność kroków, wykrywanie braku uprawnień (sudo), poprawna edycja plików konfiguracyjnych (np. /etc/fstab) oraz czytelność formatowania kodu.
- Wyszukiwanie rozwiązań w zewnętrznych źródłach: weryfikacja, czy model z dostępem do sieci potrafi skutecznie ekstrahować rozwiązania z ArchWiki, forów dystrybucyjnych czy bug trackerów i dostosowywać je do bieżącego kontekstu użytkownika.

# Co chcemy sprawdzić
Interesuje nas przede wszystkim, czy model:
- Stosuje bezpieczne podejście: czy przestrzega przed komendami destrukcyjnymi i sugeruje tworzenie kopii zapasowych przed edycją plików systemowych.
- Formułuje adekwatne pytania doprecyzowujące: czy potrafi wyciągnąć informacje o środowisku (architektura, używane środowisko graficzne Wayland/X11, wersja kernela), gdy użytkownik poda jedynie ogólny opis ("nie działa mi dźwięk").
- Poprawnie interpretuje błędy z logów: czy po wklejeniu surowego zrzutu trafnie wskazuje źródło problemu.
- Unika halucynacji w komendach i flagach: czy generuje istniejące opcje programów CLI i prawidłowe ścieżki do plików w danej dystrybucji (np. różnice między Debian a Fedora).
- Potrafi iteracyjnie korygować instrukcje: gdy wygenerowana komenda zwróci błąd, czy model rozumie komunikat błędu i proponuje właściwą poprawkę.

# Porównanie modeli
Eksperymenty wykonamy na kilku modelach (zarówno warianty z wbudowanym wyszukiwaniem internetowym, jak i bez dostępu do sieci oraz modele lokalne). Testy przeprowadzimy w kontrolowanych środowiskach maszyn wirtualnych i rzeczywistego sprzętu z wypreparowanymi, rzeczywistymi awariami i nietypowymi konfiguracjami sprzętowymi.

# Wynik
Ocena, czy współczesne modele AI mogą służyć jako praktyczny, bezpieczny i skuteczny asystent administracji systemami Linux, zdolny do prowadzenia precyzyjnej diagnostyki sprzętowej i programowej, czy też ich instrukcje wymagają ciągłej weryfikacji przez doświadczonego administratora ze względu na ryzyko podania błędnych komend lub nieznajomość specyfiki konkretnej dystrybucji.

---

## [opened] Udźwiękowienie niemego klipu - AI jako dźwiękowiec (video-to-audio) (#16)
**Author:** Arkadiusz Baran
**Assignees:** Arkadiusz Baran
**Created At:** 2026-10-06T23:17:40.093+02:00

### Description
grupa:group_RNG

### Cel

Sprawdzić, czy AI potrafi udźwiękowić niemy klip wideo, czyli wygenerować efekty dźwiękowe i dialogi, które pasują do obrazu, są w tempo i brzmią realistycznie.

### Jak

- zbieramy 15-20 krótkich klipów (5-10 s): własne nagrania i filmy z internetu na wolnej licencji, z różnymi dźwiękami (uderzenia, tło, rozmowa, zdarzenia poza kadrem); wycinamy z nich dźwięk, a oryginał zostaje jako punkt odniesienia,
- podejście 1: model video-to-audio (np. MMAudio),
- podejście 2: LLM (np. Gemini) ogląda klip i wypisuje dźwięki z czasami, generator efektów (np. ElevenLabs) je tworzy, a skrypt wkleja je w odpowiednie momenty (ffmpeg),
- dla klipów z rozmową: LLM wymyśla dialog pasujący do sceny (gesty, emocje, ruch ust), a TTS (np. ElevenLabs) go czyta; porównujemy go z tym, co naprawdę zostało powiedziane,
- kilka generacji tego samego klipu, żeby sprawdzić powtarzalność.

### Ocena

Ślepa ankieta: wersje AI i ukryty oryginał w losowej kolejności, oceny 1-5 (dopasowanie, synchronizacja, realizm) oraz pytanie "która wersja to oryginał?".

### Co chcemy sprawdzić

- czy model trafia z rodzajem dźwięku i synchronizacją,
- czy dodaje dźwięki, których nie ma w kadrze,
- czy wymyślony dialog pasuje do sytuacji i ruchu ust oraz czy przypomina prawdziwą rozmowę,
- które podejście wypada lepiej,
- czy ludzie odróżniają AI od oryginału.

Do każdego wyniku podajemy model, wersję, ustawienia i prompt.

### Comments
**Arkadiusz Baran** (2026-10-06T23:22:22.037+02:00):
@jzupnik

---

## [opened] LLM Paragrafy i Role, czyli Gry Paragrafowe i AI (#15)
**Author:** Adrian Sotomski
**Assignees:** Adrian Sotomski
**Created At:** 2026-10-06T22:47:03.930+02:00

### Description
grupa:group_Archmagosi_Omnisjasza

### Comments
**Adrian Sotomski** (2026-10-06T23:00:05.955+02:00):
## 1. Opis Projektu

Projekt zakłada zbadanie, w jaki sposób sposób promptowania zmienia **proces myślenia i decyzyjności** współczesnych modeli językowych (LLM) podczas rozgrywania paragrafówek (gamebooków). Model otrzymuje od nas **tę samą, przygotowaną wcześniej paragrafówkę** z formalnym grafem przejść, stanem początkowym, celem, postaciami i warunkami zakończenia. Następnie przechodzi ją kilka razy w różnych trybach promptowania.

Główne porównanie dotyczy dwóch skrajnych nastawień:

- **Tryb Speedrun / Zadanie najszybciej:** „Ukończ grę najszybciej. Minimalizuj liczbę kroków. Wybieraj optymalne ścieżki. Nie odgrywaj postaci.”
- **Tryb Roleplay / Wciel się w postać:** „Wciel się w postać, którą odgrywasz. Podejmuj decyzje zgodne z jej wiedzą, charakterem, celami, lękami i ograniczeniami. Nie kieruj się wiedzą gracza.”

Dodatkowo można wprowadzić tryb neutralny oraz warianty z Chain-of-Thought, aby sprawdzić, czy jawne „myślenie krok po kroku” zmienia perspektywę decyzyjną.

Celem nie jest więc tylko sprawdzenie, **czy** model wygrywa, ale **jak myśli** przy tym samym materiale: czy optymalizuje, czy wczuwa się w postać, czy miesza oba tryby, czy halucynuje stan gry, czy gubi konsekwencje wyborów. Właściwa analiza punktu myślenia, trajektorii decyzyjnych i typów uzasadnień jest wykonywana ręcznie przez zespół.

---

## 2. Cele Projektu

**Cel Badawczy:**  
Określenie, jak promptowanie typu „wykonaj zadanie najszybciej” vs „wciel się w postać” wpływa na wybory modelu, liczbę kroków, skuteczność, spójność postaci oraz sposób uzasadniania decyzji w tych samych punktach paragrafówki.

**Cel Inżynieryjny:**  
Zbudowanie potoku, który podaje modelowi tę samą paragrafówkę w różnych reżimach, zbiera decyzje, uzasadnienia i historię rozgrywki, a następnie umożliwia automatyczną wstępną ocenę oraz ręczną analizę jakościową.

**Cel Poznawczy:**  
Zidentyfikowanie i sklasyfikowanie różnic w „punkcie myślenia” modelu: czy model kieruje się celem gracza, celem postaci, wiedzą postaci, metawiedzą, optymalizacją, fabułą, moralnością czy przypadkową halucynacją. Chcemy też wykryć zjawisko **ukrytego meta-grania** — sytuacji, w której model deklaruje roleplay, ale faktycznie optymalizuje grę.

---

## 3. Zakres Działania

Projekt zostanie zrealizowany w czterech fazach.

### Faza I: Korpus paragrafówek i formalizacja

Przygotowanie zestawu paragrafówek, np. **10–30 gamebooków** lub ich starannie wyselekcjonowanych fragmentów. Dla każdej paragrafówki tworzymy:

- formalny graf przejść między akapitami,
- stan początkowy i ekwipunek,
- cel gracza i cel postaci,
- profil postaci (cechy, wiedza, lęki, motywacje),
- warunki zwycięstwa i porażki,
- ścieżkę optymalną oraz alternatywne ścieżki,
- punkty decyzyjne o wysokim znaczeniu.

Dzięki temu mamy **„złoty standard”**, do którego porównujemy zachowanie modeli.

### Faza II: Protokoły promptowania i agenci

Tworzymy zestaw promptów dla tego samego materiału:

- **P0 — Neutralny:** „Zagraj w tę paragrafówkę.”
- **P1 — Speedrun:** „Ukończ najszybciej, minimalizuj kroki, optymalizuj.”
- **P2 — Roleplay:** „Wciel się w postać, kieruj się jej wiedzą i charakterem.”
- **P3 — Roleplay + CoT:** jak P2, ale z wymuszonym myśleniem krok po kroku.
- **P4 — Speedrun + CoT:** jak P1, ale z jawnym planowaniem.

**Agenci:**

- **Agent Tester:** prowadzi rozgrywkę, wysyła kolejne stany paragrafówki do modelu i zbiera wybory oraz uzasadnienia.
- **Agent Sędzia (Evaluator):** dokonuje wstępnej, automatycznej oceny poprawności logicznej, zgodności z zasadami i osiągnięcia celu. 


### Faza III: Eksperyment

Każdy model przechodzi każdą paragrafówkę w każdym trybie promptowania, najlepiej kilka razy (różne temperatury / ziarna losowości). Weryfikujemy hipotezy:

- Czy Speedrun daje wyższy win rate i mniej kroków?
- Czy Roleplay obniża skuteczność, ale zwiększa spójność postaci?
- Czy modele w trybie Roleplay naprawdę korzystają tylko z wiedzy postaci, czy nadal używają metawiedzy?
- Czy CoT poprawia śledzenie stanu i planowanie, czy tylko wydłuża odpowiedzi?
- Czy większe modele lepiej rozdzielają perspektywę gracza od perspektywy postaci?
- W których punktach decyzyjnych tryby najbardziej się rozchodzą i dlaczego?

### Faza IV: Analiza ręczna i raportowanie

Analizujemy nie tylko wynik końcowy, ale całą ścieżkę decyzyjną. Ocena jakościowa i klasyfikacja punktu myślenia są robione ręcznie przez zespół na podstawie zebranych decyzji, uzasadnień i trajektorii.

**Metryki i analizy:**

- Win rate.
- Średnia liczba kroków do zakończenia.
- Optymalność ścieżki względem złotego standardu.
- Odsetek dead-endów i powrotów.
- Błędy stanu: zgubione przedmioty, błędne numery akapitów, zapomniane konsekwencje.
- Halucynacje i łamanie zasad paragrafówki.
- Zgodność z postacią (skala 1–5).
- Poziom meta-grania (IC vs OOC).
- Rozbieżność decyzji między trybami w tych samych punktach.
- Ręczna klasyfikacja uzasadnień: optymalizacyjne, narracyjne, postaciowe, logiczne, halucynacyjne.

Wyniki przedstawiamy jako:
- Macierze pomyłek.
- Wykresy ścieżek decyzyjnych.
- Porównania trajektorii oraz wnioski na temat tego, czy LLM zmienia punkt myślenia w zależności od promptu, czy tylko deklaruje zmianę perspektywy, pozostając w tym samym trybie optymalizacyjnym.

---

## [opened] Generowanie gier przez LLM: porównanie komercyjnych modeli (#14)
**Author:** Wojciech Pietras
**Assignees:** Wojciech Pietras
**Created At:** 2026-10-06T22:41:14.997+02:00

### Description
grupa:group_ZyblikiSlowiki

## Cel projektu

Sprawdzenie, jak daleko można zajść w tworzeniu prostych gier w HTML/JS, gdy kod pisze głównie komercyjny model językowy. Porównujemy modele różnych firm, wersje darmowe z płatnymi oraz tryb zwykły z trybem rozumowania (reasoning).

## Gry testowe

1. Snake
2. Tetris
3. Saper

## Modele

* flagowy model OpenAI
* flagowy model Anthropic
* flagowy model Google

Do każdego wyniku podajemy: nazwę, dokładną wersję, datę testu, plan (darmowy/płatny), ustawienia (np. tryb rozumowania) i pełny prompt.

## Mierzone wskaźniki

* czy gra działa od razu (tak/nie)
* ocena jakości 0-2 za: sterowanie, kolizje, wynik, game over/restart, zgodność z opisem
* liczba tur naprawczych do działającej wersji (limit 10)

## Zakres eksperymentów

* **Eksperyment 1: One-shot.** Ten sam prompt dla każdej gry i każdego modelu, ocena według wskaźników.
* **Eksperyment 2: Naprawa.** Dla gier, które nie działają, wklejamy opis problemu lub log z konsoli przeglądarki i liczymy tury do naprawy.
* **Eksperyment 3: Rozbudowa jednej gry.** Dokładamy po jednej funkcji (menu, punkty, poziomy, zapis rekordu, power-upy) i sprawdzamy..

---

## [opened] Chatbot AI jako algorytm mediów społecznościowych – rekomendacja treści (#13)
**Author:** Patryk Ordon
**Assignees:** Patryk Ordon
**Created At:** 2026-10-06T22:17:59.274+02:00

### Description
grupa:group_Radio17

# Cel
W mediach społecznościowych powszechnie stosuje się klasyczne algorytmy rekomendacyjne, które dobierają kolejne treści podczas "scrollowania" lub proponują materiały wideo na podstawie wcześniejszej aktywności użytkownika. Chcemy sprawdzić, na ile współczesne modele LLM potrafią zastąpić lub wspomóc dedykowane systemy w zadaniu profilowania preferencji i rekomendowania angażujących treści.

# Eksperymenty
Sprawdzić między innymi:
- Profilowanie użytkownika na podstawie historii: przekazywanie modelowi sekwencji interakcji (np. polubione/obejrzane posty, czas spędzony na treści, tematyka) i analiza trafności proponowanych rekomendacji.
- Skalowalność i wpływ wielkości kontekstu: badanie, jak ilość przekazanych danych historycznych wpływa na precyzję profilowania.
- Porównanie treści wygenerowanych wyłącznie z wiedzy własnej modelu z treściami wyszukanymi na żywo w sieci.
- AI vs. Klasyczny Algorytm Rekomendacyjny: bezpośrednie porównanie trafności propozycji generowanych przez LLM z rekomendacjami algorytmów dostępnych w internecie.
- Ocena skuteczności rekomendacji przy braku historii interakcji (tylko na podstawie pojedynczego wyboru użytkownika). 

# Co chcemy sprawdzić
Interesuje nas przede wszystkim, czy model:
- Poprawnie klasyfikuje intencje/zainteresowania użytkownika z surowego ciągu interakcji (profilowanie ukrytych preferencji).
- Czy potrafi równoważyć proponowanie treści ściśle związane z dotychczasowymi zainteresowaniami z trafnym wprowadzaniem nowych, powiązanych tematów.
- Skutecznie wykorzystuje wyszukiwanie internetowe do odnajdywania aktualnych i istniejących w sieci materiałów.
- Unika halucynacji dotyczących nieistniejących artykułów, filmów czy twórców
- Potrafi wyjaśnić powód rekomendacji, uzasadniając, dlaczego dana treść pasuje do profilu użytkownika.

# Porównanie modeli
Eksperymenty wykonamy na kilku modelach (darmowych i komercyjnych, z dostępem do sieci i bez). Ten sam prompt oraz ten sam zestaw danych wejściowych (zbiór historii użytkowników) uruchomimy wielokrotnie, aby zmierzyć powtarzalność propozycji.

Dla ewaluacji można zastosować ocenę trafności proponowanych treści przez testerów na podstawie stworzonych person.

# Wynik
Odpowiedź na pytanie, czy współczesne modele LLM posiadają wystarczające zrozumienie kontekstu i preferencji użytkownika, aby służyć jako elastyczny system rekomendacji treści, czy też lepiej sprawdzają się jedynie jako warstwa interpretująca (np. do generowania uzasadnień lub ekstrakcji słów kluczowych dla tradycyjnych algorytmów).

---

## [opened] AI Crime Benchmark (#12)
**Author:** Filip Trzciński
**Created At:** 2026-10-06T22:13:46.299+02:00

### Description
**Cel projektu**

Projekt zakłada zbadanie, jak modele AI radzą sobie z rozwiązywaniem fikcyjnych spraw kryminalnych na podstawie kontrolowanego zestawu dowodów, opartego na prawdziwych historiach. Jego celem jest sprawdzenie, czy model potrafi analizować informacje, łączyć fakty, wykrywać sprzeczności, odrzucać fałszywe tropy oraz wskazywać najbardziej logiczne rozwiązanie sprawy.

**Tryby eksperymentu**

- Pełna sprawa: model otrzymuje wszystkie materiały od razu.
- Sprawa etapowa: model otrzymuje informacje stopniowo 
- Sprawa z fałszywym tropem: do materiałów dodawany jest mylący dowód
- Sprawa ze sprzecznością: część dokumentów zawiera informacje niepasujące do reszty akt.
- Sprawa z ograniczonym kontekstem: model dostaje tylko część danych

---

## [opened] LLM zawód typer (#11)
**Author:** Jakub Dusza
**Assignees:** Jakub Dusza
**Created At:** 2026-10-06T21:08:39.842+02:00

### Description
grupa_hazard

### Comments
**Jakub Dusza** (2026-10-06T21:26:09.579+02:00):
### Cel projektu

Sprawdzenie, czy modele językowe potrafią typować wyniki różnych wydarzeń sportowych trafniej niż losowy wybór czy kopia typu bukmachera. Efektywność modeli językowych weryfikować będzie fikcyjne saldo portfela.

### Zakres

- Porównanie skuteczności przy zakładach pojedynczych oraz łączonych
- Różne dyscypliny
- Analiza uzasadnień modelu na temat wyborów
- Porównanie skuteczności przy pytaniu bez kontekstu i z kontekstem (historia meczy danej drużyny, zmiany składów, itp.)

### Plan działania

- Wybór dyscyplin/lig i modeli, dostęp do danych, format promptu, pierwsze typy.
- Rozliczenie pierwszych zakładów, założenie nowych, porównanie wyników.
- Porównanie jak zmieniły się wyniki zakładów po wprowadzeniu kontekstu.
- Próba analizy błędów wraz z modelami.
- Podsumowanie i wnioski.

---

## [opened] Ewaluacja modeli decyzyjnych: komercyjny Jev vs otwartoźródłowe Laya, Kev i NanoJev (#10)
**Author:** Karol Brodowicz
**Assignees:** Karol Brodowicz
**Created At:** 2026-10-06T19:01:00.342+02:00

### Description
grupa:group_motor

### Comments
**Karol Brodowicz** (2026-10-06T19:03:27.713+02:00):
 ### Cel projektu:

 Sprawdzenie, czy obietnice marketingowe nowej klasy modeli decyzyjnych (rezygnacja z powolnego generowania tekstu
 token-po-tokenie na rzecz natychmiastowych, typowanych decyzji w jednym przejściu sieci) sprawdzają się w praktyce,
 oraz czy lokalne odpowiedniki open-source (Laya, Kev, NanoJev) mogą zastąpić komercyjne API Jev.


 ### Opis działania:

 Porównanie modeli na wspólnym zbiorze danych w trzech podstawowych zadaniach decyzyjnych:
 1. Choice – klasyfikacja / routing zapytania do jednej z wielu kategorii.
 2. Score – ocena w zadanej skali (np. ocena ryzyka 1–5).
 3. Boolean – decyzja tak/nie i ocena prawdopodobieństwa (np. wykrywanie prompt injection).

 Zestawienie modeli w teście:
 - Jev (TypeSafe AI): Model referencyjny.
 - Laya: Otwarty model oparty na ModernBERT, zoptymalizowany pod inferencję ONNX / CPU / przeglądarkę.
 - Kev: Otwarta implementacja oparta na architekturze Qwen, serwowana lokalnie jako zamiennik SDK Jev.
 - NanoJev: Ultralekki mikro-model, nastawiony na skrajnie niskie opóźnienia w sterowaniu agentami.

 Mierzone wskaźniki:
 - Czas odpowiedzi: czy modele faktycznie działają w czasie <100 ms?
 - Trafność: jakość wyborów zero-shot.
 - Kalibracja prawdopodobieństwa: czy pewność modelu (np. 90%) odpowiada rzeczywistości.


 ### Problemy do rozwiązania:

 1. Przewaga komercyjnej kalibracji: Jev jest mocno dotrenowywany pod pewność ocen; czy mniejsze modele OS (NanoJev, Laya) nie wykazują nadmiernej pewności siebie bez dotrenowania pod konkretne zadanie?
 2. Odporność na szum w kontekście: Modele dyskryminatywne podejmują decyzję w jednym kroku (bez „myślenia” CoT). Jak Laya czy NanoJev radzą sobie, gdy stan wejściowy zawiera dużo zbędnego tekstu/kodu?
 3. Czy modele decyzyjne są rzeczywiście lepsze w decydowaniu od standardowego LLMa? Porównanie w zadaniach faworyzujących modele decyzyjne.

---

## [opened] Analiza cenzury, wariancji geolokalizacyjnej i oceny moralnej LLM w kontekście faktów historycznych (#8)
**Author:** Jakub Szymczak
**Assignees:** Jakub Szymczak
**Created At:** 2026-10-06T11:56:52.664+02:00

### Description
## Cel projektu

Zbadanie, w jaki sposób pochodzenie modelu (kraj powstania/twórca) oraz lokalizacja zapytania (IP/VPN) wpływają na prezentację, pomijanie lub wartościowanie kontrowersyjnych i tragicznych wydarzeń z historii nowożytnej i współczesnej.

## Zakres eksperymentów

**Eksperyment 1: Zatajanie i cenzura faktów historycznych w zależności od pochodzenia modelu**

Sprawdzenie, czy modele wykazują tzw. alignment bias zgodny z linią polityczną kraju pochodzenia lub regulacjami prawnymi danego regionu.

**Eksperyment 2: Wpływ geolokalizacji (VPN) na odpowiedzi systemów chatbotowych**

Weryfikacja hipotezy, czy platformy webowe/serwisy modeli dynamicznie zmieniają poziom filtracji i ton odpowiedzi w zależności od adresu IP użytkownika (geofencing system prompts / localized safety guardrails).

**Eksperyment 3: „Moralność” i symetria etyczna modeli wobec wydarzeń historycznych**

Zbadanie, czy modele zachowują neutralność encyklopedyczną, czy dokonują bezpośredniej oceny moralnej (relatywizm) oraz czy oceniają zbrodnie symetrycznie.

---

## [opened] Wirtualny radiowiec, czyli "alter AI ego" na antenie (#7)
**Author:** Piotr Róg
**Assignees:** Piotr Róg
**Created At:** 2026-10-06T11:43:27.944+02:00

### Description
grupa:group_Radio17

# Cel

Współczesne modele generatywne pozwalają na coraz dokładniejsze klonowanie ludzkiego głosu na podstawie stosunkowo niewielkiej liczby próbek. Chcemy sprawdzić, na ile możliwe jest stworzenie wirtualnego „alter AI ego” konkretnego prowadzącego radiowego na podstawie nagrań pochodzących z jego wcześniejszych audycji.

W eksperymencie wykorzystamy dostępne próbki głosu prowadzącego, pochodzące z audycji radiowych, i spróbujemy dostosować wybrany model generowania mowy tak, aby możliwie wiernie odwzorowywał jego głos. Następnie AI będzie wykorzystywane do przygotowania fragmentów audycji, które zostaną porównane z materiałami nagranymi przez rzeczywistego prowadzącego.

Nie chodzi wyłącznie o sprawdzenie, czy wygenerowany głos „brzmi podobnie”. Interesuje nas również, czy zachowuje charakterystyczne cechy głosu, sposób mówienia, intonację i emocje oraz czy człowiek jest w stanie odróżnić nagranie wygenerowane przez AI od prawdziwego nagrania.

# Eksperymenty

Sprawdzić między innymi:

- wykorzystanie próbek o różnej długości do stworzenia klonu głosu,

- porównanie kilku dostępnych modeli i metod klonowania/generowania głosu,

- sprawdzenie wpływu jakości i rodzaju próbek treningowych na rezultat,

- generowanie tych samych wypowiedzi przy różnych ustawieniach modelu,

- próbę odwzorowania charakterystycznego sposobu mówienia i intonacji prowadzącego,

- przygotowanie krótkich fragmentów audycji przez rzeczywistego prowadzącego oraz jego „alter AI ego”,

- przeprowadzenie testu odsłuchowego, w którym uczestnicy będą próbowali rozpoznać, które nagrania zostały wygenerowane przez AI.

W miarę możliwości sprawdzimy również, jak wynik zmienia się wraz z ilością dostępnych próbek głosu oraz czy model wymaga dużej ilości materiału, aby uzyskać przekonujący rezultat.

# Co chcemy sprawdzić

Interesuje nas przede wszystkim, czy:

- AI jest w stanie wiernie odwzorować konkretny głos na podstawie istniejących nagrań,

- niewielka ilość materiału wystarcza do uzyskania przekonującego rezultatu,

- model zachowuje charakterystyczne cechy głosu i sposób mówienia,

- człowiek jest w stanie odróżnić wygenerowany głos od prawdziwego,

- wynik zależy od rodzaju i długości wykorzystanych próbek,

- różne modele dają zauważalnie różniące się rezultaty.

Będziemy również zwracać uwagę na typowe artefakty generowanego głosu, takie jak nienaturalna intonacja, wymowa, pauzy czy problemy z emocjami.

# Porównanie modeli

Eksperymenty wykonamy na kilku modelach do generowania lub klonowania głosu, w miarę możliwości zarówno dostępnych lokalnie, jak i poprzez usługi komercyjne.

Dla każdego eksperymentu zapiszemy wykorzystany model, jego wersję i ustawienia oraz rodzaj i długość wykorzystanych próbek. Zachowane zostaną również teksty używane do generowania nagrań, tak aby eksperyment można było powtórzyć na nowszych modelach.

# Wynik

Chcemy odpowiedzieć na pytanie, czy współczesne modele generowania mowy są już w stanie stworzyć przekonujące „alter ego” konkretnej osoby, którego głosu przeciętny słuchacz nie będzie w stanie łatwo odróżnić od prawdziwego człowieka.

Dodatkowym rezultatem będzie ocena, jak szybko zmienia się jakość takich systemów i czy wraz z kolejnymi generacjami modeli coraz trudniej będzie człowiekowi rozpoznać, że słyszy głos wygenerowany przez AI.

---

## [opened] AI jako projektant sieci teleinformatycznych dla firm (#6)
**Author:** Piotr Róg
**Assignees:** Piotr Róg
**Created At:** 2026-10-06T11:37:25.410+02:00

### Description
grupa:group_Radio17

# Cel

Zaprojektowanie złożonej sieci teleinformatycznej dla przykładowej firmy zatrudniającej około 100–300 osób. Chcemy sprawdzić, na ile współczesne modele AI są w stanie przygotować kompletną koncepcję sieci na podstawie wymagań dotyczących liczby użytkowników, charakterystyki firmy, dostępnych pomieszczeń, usług oraz ograniczeń technicznych i organizacyjnych.

Nie oczekujemy od modelu wskazania konkretnych modeli urządzeń. Ważniejsze jest, aby potrafił określić odpowiednie parametry infrastruktury, np. liczbę i rodzaj przełączników, przepustowość połączeń, liczbę punktów dostępowych, wymagania dotyczące routerów, firewalli czy zasilania awaryjnego.

Istotnym elementem będzie uwzględnienie ograniczeń wynikających z charakterystyki firmy i budynku. Przykładowo w zabytkowym obiekcie może być niedopuszczalne prowadzenie nowych przewodów, co wymusza zastosowanie innych rozwiązań. Model powinien również uwzględniać podstawowe zależności techniczne i nie popełniać oczywistych błędów, takich jak dobranie UPS-a o mocy znacznie mniejszej niż rzeczywiste zapotrzebowanie serwerowni.

# Eksperymenty

Sprawdzić między innymi:

- zaprojektowanie sieci dla różnych wielkości firmy i liczby użytkowników,

- dobór parametrów przełączników, routerów, firewalli i punktów dostępowych,

- zaprojektowanie połączeń pomiędzy serwerownią i poszczególnymi częściami budynku,

- uwzględnienie redundancji i pojedynczych punktów awarii,

- zaplanowanie adresacji, VLAN-ów i podstawowej segmentacji sieci,

- dobór parametrów zasilania awaryjnego na podstawie podanego obciążenia,

- przygotowanie projektu dla budynku z dodatkowymi ograniczeniami, np. zabytkowego,

- modyfikowanie projektu po zmianie wymagań, np. zwiększeniu liczby pracowników lub dodaniu nowego oddziału.

# Co chcemy sprawdzić

Interesuje nas przede wszystkim, czy model:

- potrafi przełożyć opis firmy na konkretne wymagania techniczne,

- poprawnie dobiera parametry urządzeń do skali sieci,

- uwzględnia ograniczenia fizyczne i organizacyjne,

- rozpoznaje zależności pomiędzy poszczególnymi elementami infrastruktury,

- uwzględnia redundancję, bezpieczeństwo i możliwość rozbudowy,

- poprawnie wykonuje podstawowe obliczenia, np. dotyczące przepustowości lub zasilania,

- potrafi wykryć i poprawić błędy we własnym projekcie po zwróceniu na nie uwagi.

Szczególnie interesujące będą przypadki, w których projekt na pierwszy rzut oka wygląda poprawnie, ale zawiera istotne błędy, np. niewystarczającą przepustowość, zbyt małą liczbę portów, brak odpowiedniego zapasu lub niewystarczające zasilanie awaryjne.

# Porównanie modeli

Eksperymenty wykonamy na kilku modelach, w miarę możliwości zarówno darmowych, jak i komercyjnych.

Te same scenariusze i wymagania będziemy przekazywać różnym modelom. Zachowamy prompty oraz wygenerowane projekty, aby można było porównać nie tylko ich wygląd, ale przede wszystkim poprawność techniczną i liczbę popełnionych błędów.

# Wynik

Chcemy odpowiedzieć na pytanie, czy współczesne modele AI są już w stanie przygotować sensowny projekt złożonej sieci teleinformatycznej, uwzględniający rzeczywiste wymagania i ograniczenia, czy też nadal dobrze radzą sobie głównie z przygotowaniem ogólnej koncepcji, która wymaga szczegółowej weryfikacji przez człowieka.

---

## [opened] Czy AI może być bronią do walki z code rot? (#5)
**Author:** Piotr Róg
**Assignees:** Piotr Róg
**Created At:** 2026-10-06T11:31:53.221+02:00

### Description
grupa:group_Radio17

# Cel

Wraz z upływem czasu starsze oprogramowanie może przestać się kompilować na współczesnych systemach, nawet jeżeli jego kod źródłowy pozostaje niezmieniony - zjawisko znane między innymi jako `code rot`. Przyczyną mogą być zmiany w bibliotekach, nagłówkach systemowych, API czy bardziej restrykcyjne sprawdzanie błędów przez nowe wersje kompilatorów. Problem ten jest szczególnie widoczny w przypadku starszych narzędzi systemowych, sterowników czy modułów kernela.

Chcemy sprawdzić, na ile współczesne modele AI są w stanie pomóc w przywróceniu możliwości kompilowania starego oprogramowania na współczesnych systemach. Jako przykłady można wykorzystać programy lub moduły przygotowane kilkanaście lat temu dla starszych dystrybucji Linuksa, np. Ubuntu 8.04, które obecnie nie kompilują się na Ubuntu 22.04 lub nowszym.

Interesuje nas nie tylko poprawienie pojedynczych błędów kompilatora, ale również sprawdzenie, czy AI potrafi rozpoznać przyczynę problemu i dobrać odpowiedni sposób jego naprawy. W wielu przypadkach może to być zmiana składni, zastąpienie usuniętej funkcji, dostosowanie kodu do nowego API albo zmiana sposobu korzystania z bibliotek systemowych.

# Eksperymenty

Sprawdzić między innymi:
- kompilowanie starego kodu na współczesnym GCC i analiza błędów,
- przekazanie kodu oraz komunikatów kompilatora do AI i sprawdzenie, czy potrafi zaproponować poprawki,
- naprawianie zmian wynikających z bardziej restrykcyjnego działania współczesnych kompilatorów,
- dostosowanie kodu do zmienionych nagłówków, funkcji i API,
- próby aktualizacji starszych narzędzi i programów użytkowych,
- w miarę możliwości dostosowanie starych modułów kernela do współczesnej wersji kernela.

Można wykorzystać kod przeznaczony pierwotnie dla starszych wersji Ubuntu, FreeBSD lub innych systemów, dla których dostępny jest kod źródłowy i możliwe jest odtworzenie pierwotnego środowiska.

# Co chcemy sprawdzić

Interesuje nas przede wszystkim, czy model:

- potrafi poprawnie interpretować błędy współczesnego kompilatora,
- potrafi znaleźć przyczynę problemu zamiast jedynie usuwać kolejne komunikaty błędów,
- rozpoznaje różnice pomiędzy starymi i nowymi wersjami API,
- potrafi dobrać poprawną zamianę usuniętej lub zmienionej funkcji,
- potrafi iteracyjnie poprawiać kod na podstawie kolejnych błędów kompilacji,
- zachowuje oryginalne działanie programu po wprowadzonych zmianach.

Będziemy również zwracać uwagę na przypadki, w których AI generuje poprawki pozwalające na kompilację, ale zmieniające działanie programu albo maskujące rzeczywisty problem.

# Porównanie modeli

Eksperymenty wykonamy na kilku modelach, w miarę możliwości zarówno darmowych, jak i komercyjnych.

Dla każdego przypadku zachowamy oryginalny kod, komunikaty kompilatora, wykorzystane prompty oraz kolejne wersje kodu wygenerowane przez AI. Ten sam problem będziemy w miarę możliwości uruchamiać na kilku modelach i wielokrotnie, aby sprawdzić różnice oraz powtarzalność wyników.

# Wynik

Chcemy odpowiedzieć na pytanie, czy współczesne modele AI mogą być praktycznym narzędziem do walki z code rot, pozwalającym przywracać do życia stare oprogramowanie bez konieczności ręcznego analizowania całego kodu przez programistę.

Szczególnie interesujące będzie sprawdzenie, czy AI radzi sobie jedynie z prostymi zmianami wynikającymi z ewolucji składni i API, czy również potrafi poradzić sobie z bardziej złożonymi zmianami wymagającymi zrozumienia działania programu i środowiska, dla którego został pierwotnie napisany.

---

## [opened] Inżynieria wsteczna (własnościowych) protokołów sieciowych z wykorzystaniem AI (#4)
**Author:** Piotr Róg
**Assignees:** Piotr Róg
**Created At:** 2026-10-06T11:21:00.657+02:00

### Description
grupa:group_Radio17

# Cel

Wiele aplikacji, gier i urządzeń wykorzystuje własnościowe protokoły sieciowe, dla których nie istnieje publiczna dokumentacja albo jest ona niepełna. Zrozumienie takiego protokołu często wymaga obserwowania komunikacji pomiędzy klientem i serwerem oraz analizowania przechwyconych pakietów. W przypadku protokołów binarnych dodatkowym problemem jest ustalenie znaczenia poszczególnych bajtów, pól oraz zależności pomiędzy kolejnymi komunikatami.

Chcemy sprawdzić, na ile współczesne modele AI są w stanie pomagać w takim procesie. Model otrzyma dostęp do dumpów z Wiresharka, a w najprostszym wariancie również informację, jaka akcja została wykonana w aplikacji podczas ich tworzenia. Przykładowo możemy wykonać kilka różnych operacji w kliencie i sprawdzić, czy AI potrafi wskazać, które fragmenty komunikacji odpowiadają za poszczególne działania.

Nie zakładamy, że model będzie w stanie całkowicie odtworzyć badany protokół – interesuje nas przede wszystkim, jak dużo informacji jest w stanie z niego wyciągnąć i jak dobrze potrafi je uporządkować.

# Eksperymenty

Sprawdzić między innymi:

- analizę przygotowanych dumpów Wiresharka z informacją o wykonanej akcji,

- rozpoznawanie powtarzających się komunikatów i pól,

- identyfikowanie pól stałych i zmiennych oraz próby określenia ich znaczenia,

- porównywanie komunikatów powstałych w wyniku podobnych operacji,

- próby określenia kolejności i zależności pomiędzy komunikatami,

- stopniowe przekazywanie modelowi kolejnych danych i sprawdzanie, czy potrafi poprawiać wcześniejsze hipotezy.

Do testów można wykorzystać zarówno specjalnie przygotowany prosty protokół, którego strukturę znamy, jak i bardziej realistyczny przykład. Własny protokół pozwoli łatwiej ocenić, które informacje model rzeczywiście poprawnie odtworzył.

Jako wynik eksperymentu spróbujemy uzyskać uporządkowaną dokumentację protokołu, np. w postaci opisu komunikatów i ich pól lub, jeśli będzie to odpowiednie dla badanego protokołu, definicji w formacie Protocol Buffers (.proto).

# Co chcemy sprawdzić

Interesuje nas przede wszystkim, czy model:

- potrafi znaleźć strukturę komunikatów w surowych danych,

- potrafi powiązać zmiany w pakietach z konkretnymi akcjami użytkownika,

- poprawnie rozpoznaje pola stałe i zmienne,

- potrafi formułować hipotezy dotyczące znaczenia poszczególnych pól,

- potrafi stworzyć sensowną dokumentację badanego protokołu,

- potrafi rozpoznać, kiedy nie ma wystarczających danych do wyciągnięcia jednoznacznego wniosku.

Będziemy również rejestrować przypadki, w których model błędnie interpretuje dane lub tworzy pozornie sensowną dokumentację niezgodną z rzeczywistym działaniem protokołu.

# Porównanie modeli

Eksperymenty wykonamy na kilku modelach, w miarę możliwości zarówno darmowych, jak i komercyjnych.

Ten sam prompt i dane będziemy w miarę możliwości uruchamiać wielokrotnie, aby sprawdzić powtarzalność wyników. Dla każdego eksperymentu zapiszemy nazwę i wersję modelu, jego parametry (w przypadku modeli lokalnych również sposób kwantyzacji), prompt oraz wykorzystane dane.

# Wynik

Chcemy odpowiedzieć na pytanie, czy współczesne modele AI mogą być praktycznym wsparciem w reverse engineeringu nieznanych protokołów sieciowych, czy też potrafią głównie znajdować proste wzorce w przechwyconych danych, a właściwe zrozumienie protokołu nadal wymaga pracy człowieka.

---

## [opened] AI a portowanie starego kodu między platformami (#3)
**Author:** Piotr Róg
**Assignees:** Piotr Róg
**Created At:** 2026-10-05T17:26:08.080+02:00

### Description
grupa:group_Radio17

# Cel

Wiele starszych programów i gier zostało napisanych z wykorzystaniem specyficznych assemblerów, kompilatorów, na konkretne systemy operacyjne oraz najczęściej operowały bezpośrednio na sprzęcie. Ich przeniesienie na współczesne platformy często wymaga nie tylko zmiany składni, ale również zrozumienia, co faktycznie robi kod i jak zastąpić zależności od starego środowiska. Trzeba również wziąć pod uwagę specyfiki starych kompilatorów, które pozwalały na nieco większą swobodę w pisaniu i przez co dla współczesnych programistów (a tym samym potencjalnie dla AI) kod napisany pod nie może być niezrozumiały.

Dla przykładu stary Watcom 10 pozwala na taką składnię:
```
for(int i=0;i<10;i++) {}
for(i=0;i<10;i++) {}
```
a współczesny GCC wyrzuci, że zmienna i w drugim przypadku nie jest zadeklarowana.

Chcemy sprawdzić, na ile współczesne modele AI potrafią samodzielnie wykonać takie zadanie. Jest to ciekawy przypadek użycia, ponieważ prosta translacja składni może być stosunkowo łatwa dla LLM, natomiast prawdziwe portowanie wymaga rozumienia architektury programu, sprzętu, API i różnic pomiędzy platformami.

Dodatkowo pozwoli to sprawdzić, czy AI jest w stanie pomagać przy modernizacji starego oprogramowania, dla którego dokumentacja może być niepełna, kod może być trudny do zrozumienia, a część wiedzy potrzebnej do portowania jest związana z historycznymi platformami.

# Eksperymenty

Sprawdzić między innymi:

- translację assemblera MASM -> NASM, np. na fragmentach historycznego kodu BIOS/bootloaderów - najprostsze, kod w NASM powinien dawać takiego samego bloba jak w MASM,

- portowanie kodu DOS wykorzystującego bezpośrednio sprzęt do współczesnego środowiska SDL,

- portowanie współczesnego kodu tworzonego pod DOS,

- w miarę możliwości portowanie kodu pomiędzy innymi platformami, np. Amiga, Commodore 64, NES itp.

Do testowania modeli można wykorzystać dostępny kod źródłowy starszych gier, np. Doom, Hexen, Quake, Polanie, a także kod otwartoźródłowych narzędzi przygotowywanych dla projektu FreeDOS.

# Co chcemy sprawdzić

Interesuje nas przede wszystkim, czy model:

- rzeczywiście rozumie działanie kodu, czy tylko dokonuje translacji składni,

- poprawnie rozpoznaje zależności od konkretnej platformy i sprzętu,

- potrafi dobrać sposób portowania,

- wybiera bezpośrednie przepisanie kodu, shimming, wrappery czy inną strategię,

- generuje kod, który się kompiluje i uruchamia,

- zachowuje funkcjonalność oryginalnego programu,

- potrafi samodzielnie poprawiać błędy po otrzymaniu informacji z kompilatora.

Będziemy również rejestrować przypadki, w których model wymyśla nieistniejące API, błędnie interpretuje działanie sprzętu lub generuje kod pozornie poprawny, ale niezgodny z działaniem oryginału.

# Porównanie modeli

Eksperymenty wykonamy na kilku modelach, w miarę możliwości zarówno darmowych, jak i komercyjnych.

Ten sam prompt będziemy w miarę możliwości uruchamiać wielokrotnie, aby sprawdzić powtarzalność wyników.

# Wynik

Chcemy odpowiedzieć na pytanie, czy współczesne LLM są już w stanie być praktycznym narzędziem do migracji starego oprogramowania, czy też dobrze radzą sobie jedynie z mechaniczną translacją kodu, podczas gdy właściwe portowanie nadal wymaga wiedzy i kontroli programisty.

---

## [opened] oceny (#2)
**Author:** Jarosław Bułat
**Created At:** 2026-09-25T19:32:53.366+02:00

### Description
~sprint_00 oceny

stan na 29.01.2026 16:00

|group | name/surname | ~sprint_01 | ~sprint_02 | ~sprint_03 | ~sprint_04 | ~sprint_05 | ~sprint_06 | ~sprint_07 | ~sprint_08 | ~sprint_09 | ~sprint_10 | ~sprint_11 | ~sprint_12 | ~sprint_13 | ~sprint_14 | SUM|
|-------|------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------------|
|-------|------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------------|

---

## [opened] grupy (#1)
**Author:** Jarosław Bułat
**Assignees:** Jarosław Bułat
**Created At:** 2026-09-25T19:30:09.492+02:00

### Description
~sprint_00 groups

W activity poniżej zróbcie podział na grupy. Jedno activity == jedna grupa w formacie:

**group_nazwa_grupy: Imię Nazwisko, Imię2 Nazwisko2, ...**

Wpisujcie realne imiona/nazwiska a nie login z gitlaba/agh.

Jeżeli chcecie się "rozstać" zrobić inny projekt w innym składzie to zróbcie kolejną grupę (kolejne issue).

Proszę bardzo dokładnie przestrzegać formatowania - podkreślenie, małe/duże litery, przecinki, spacje, etc... Inaczej automatyka wypełniająca tabelki nie będzie działać. Prefiks **group_** jest obowiązkowo i musi być literalnie tak wpisane.

### Comments
**Jeremiasz Moroz** (2026-10-06T23:46:38.211+02:00):
group_SOK: Jeremiasz Moroz, Maciej Gumiela, Szymon Kasperek

**Łukasz Skrzypek** (2026-10-06T23:11:52.421+02:00):
group_TeleTele: Łukasz Skrzypek, Arkadiusz Kępa, Daniel Kędziora

**Adrian Sotomski** (2026-10-06T22:43:11.801+02:00):
group_Archmagosi_Omnisjasza: Krzysztof Ptaszyński, Bartosz Pieczek, Adrian Sotomski, Radosław Chruściński

**Filip Trzciński** (2026-10-06T21:49:24.787+02:00):
group_telezubry: Antoni Janek, Artur Kupiec, Filip Trzcinski, Kamil Pawelczak

**Wojciech Pietras** (2026-10-06T21:48:14.575+02:00):
group_ZyblikiSlowiki: Wojciech Pietras, Michał Sałapat, Filip Zając, Kacper Taborski

**Mateusz Zawieracz** (2026-10-06T21:30:51.692+02:00):
group_daniel: Mikołaj Mierzwa, Wojciech Śliwa, Kacper Rothkegel, Mateusz Zawieracz

**Jakub Dusza** (2026-10-06T21:04:33.767+02:00):
group_hazard: Franciszek Hajduk, Maciek Antosz, Jakub Dusza

**Karol Brodowicz** (2026-10-06T19:17:26.251+02:00):
group_motor: Karol Brodowicz, Mikołaj Mazur

**Jakub Szymczak** (2026-10-06T11:50:00.647+02:00):
group_SuperInteligencja: Jakub Szymczak, Tymoteusz Kruk, Nikodem Bednarski

**Mateusz Żelasko** (2026-10-06T11:37:55.020+02:00):
group_Strawberry: Paweł Pasternak, Tyberiusz Bobrek, Borys Jarnot-Bałuszek, Mateusz Żelasko

**Krzysztof Dudzik** (2026-10-05T23:15:42.456+02:00):
group_zolc: Krzysztof Dudzik, Adam Minior, Antoni Pietraszewski, Piotr Kurbiel

**Marcin Węgrzyn** (2026-10-05T23:00:29.210+02:00):
group_BezKontekstu: Adam Jabłoński, Marcin Węgrzyn

**Krzysztof Słowikowski** (2026-10-05T21:57:32.549+02:00):
group_Cokolwiek: Mikołaj Dorosz, Amelia Szymańska, Krzysztof Słowikowski

**Wiktoria Gajos** (2026-10-05T12:28:39.152+02:00):
group_TajnAIcy: Wiktoria Gajos, Bartosz Łukasik, Mikołaj Mitoń

**Kacper Tomczyk** (2026-10-04T20:49:13.818+02:00):
group_ZbikiDzikiIGoaciki: Kacper Tomczyk, Jakub Bogunia, Michał Kania, Maciej Miłek

**Arkadiusz Baran** (2026-10-04T17:29:04.823+02:00):
group_RNG: Joanna Żupnik, Arkadiusz Baran

**Kamil Szkarłat** (2026-10-02T17:50:23.965+02:00):
group_BlueMoon: Kamil Szkarłat, Jakub Szkaradek, Bartłomiej Ząbek

**Piotr Róg** (2026-10-02T14:04:22.964+02:00):
group_Radio17: Patryk Ordon, Piotr Róg

---

