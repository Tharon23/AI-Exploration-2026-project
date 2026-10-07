# Project: AI Exploration 2026

**Description**: null

## File Tree
- README.md (blob)

## Key Files Content
### README.md
```
null
```

## Issues
### #17: AI jako asystent zaawansowanej konfiguracji i diagnostyki GNU/Linux
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

### #16: Udźwiękowienie niemego klipu - AI jako dźwiękowiec (video-to-audio)
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

### #15: LLM Paragrafy i Role, czyli Gry Paragrafowe i AI
grupa:group_Archmagosi_Omnisjasza

### #14: Generowanie gier przez LLM: porównanie komercyjnych modeli
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

### #13: Chatbot AI jako algorytm mediów społecznościowych – rekomendacja treści
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

### #12: AI Crime Benchmark
**Cel projektu**

Projekt zakłada zbadanie, jak modele AI radzą sobie z rozwiązywaniem fikcyjnych spraw kryminalnych na podstawie kontrolowanego zestawu dowodów, opartego na prawdziwych historiach. Jego celem jest sprawdzenie, czy model potrafi analizować informacje, łączyć fakty, wykrywać sprzeczności, odrzucać fałszywe tropy oraz wskazywać najbardziej logiczne rozwiązanie sprawy.

**Tryby eksperymentu**

- Pełna sprawa: model otrzymuje wszystkie materiały od razu.
- Sprawa etapowa: model otrzymuje informacje stopniowo 
- Sprawa z fałszywym tropem: do materiałów dodawany jest mylący dowód
- Sprawa ze sprzecznością: część dokumentów zawiera informacje niepasujące do reszty akt.
- Sprawa z ograniczonym kontekstem: model dostaje tylko część danych

### #11: LLM zawód typer
grupa_hazard

### #10: Ewaluacja modeli decyzyjnych: komercyjny Jev vs otwartoźródłowe Laya, Kev i NanoJev
grupa:group_motor

### #8: Analiza cenzury, wariancji geolokalizacyjnej i oceny moralnej LLM w kontekście faktów historycznych
## Cel projektu

Zbadanie, w jaki sposób pochodzenie modelu (kraj powstania/twórca) oraz lokalizacja zapytania (IP/VPN) wpływają na prezentację, pomijanie lub wartościowanie kontrowersyjnych i tragicznych wydarzeń z historii nowożytnej i współczesnej.

## Zakres eksperymentów

**Eksperyment 1: Zatajanie i cenzura faktów historycznych w zależności od pochodzenia modelu**

Sprawdzenie, czy modele wykazują tzw. alignment bias zgodny z linią polityczną kraju pochodzenia lub regulacjami prawnymi danego regionu.

**Eksperyment 2: Wpływ geolokalizacji (VPN) na odpowiedzi systemów chatbotowych**

Weryfikacja hipotezy, czy platformy webowe/serwisy modeli dynamicznie zmieniają poziom filtracji i ton odpowiedzi w zależności od adresu IP użytkownika (geofencing system prompts / localized safety guardrails).

**Eksperyment 3: „Moralność” i symetria etyczna modeli wobec wydarzeń historycznych**

Zbadanie, czy modele zachowują neutralność encyklopedyczną, czy dokonują bezpośredniej oceny moralnej (relatywizm) oraz czy oceniają zbrodnie symetrycznie.

### #7: Wirtualny radiowiec, czyli "alter AI ego" na antenie
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

### #6: AI jako projektant sieci teleinformatycznych dla firm
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

### #5: Czy AI może być bronią do walki z code rot?
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

### #4: Inżynieria wsteczna (własnościowych) protokołów sieciowych z wykorzystaniem AI
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

### #3: AI a portowanie starego kodu między platformami
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

### #2: oceny
~sprint_00 oceny

stan na 29.01.2026 16:00

|group | name/surname | ~sprint_01 | ~sprint_02 | ~sprint_03 | ~sprint_04 | ~sprint_05 | ~sprint_06 | ~sprint_07 | ~sprint_08 | ~sprint_09 | ~sprint_10 | ~sprint_11 | ~sprint_12 | ~sprint_13 | ~sprint_14 | SUM|
|-------|------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------------|
|-------|------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------------|

### #1: grupy
~sprint_00 groups

W activity poniżej zróbcie podział na grupy. Jedno activity == jedna grupa w formacie:

**group_nazwa_grupy: Imię Nazwisko, Imię2 Nazwisko2, ...**

Wpisujcie realne imiona/nazwiska a nie login z gitlaba/agh.

Jeżeli chcecie się "rozstać" zrobić inny projekt w innym składzie to zróbcie kolejną grupę (kolejne issue).

Proszę bardzo dokładnie przestrzegać formatowania - podkreślenie, małe/duże litery, przecinki, spacje, etc... Inaczej automatyka wypełniająca tabelki nie będzie działać. Prefiks **group_** jest obowiązkowo i musi być literalnie tak wpisane.

## Wiki Pages
### Wiki: home
```
# AI Exploration

Przykładowe projekty z 2025: [wiki](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/home). Uwaga nie wszystkie projekty są podlinkowane na stronę główną. Warto przyjrzeć się objętości i formie, będę wymagał podobnego sposobu raportowania.

Celem zajęć jest poznanie obecnych możliwości szeroko rozumianej **sztucznej inteligencji** (głównie modeli generatywnych) w dziedzinach takich jak programowanie, tworzenie obrazów/filmów/audio, zarządzanie (projektami, procesami, pracami administracyjnymi), przekształcaniem mediów (różnego rodzaju deep-fake), Bezpieczeństwo (prompt injection). Chcemy zobaczyć jaki jest stan obecny (2026/2027) i jaki jest postęp od ostatniego roku.

## rules

Zajęcia będą miały charakter zespołowy. Podzielcie się w grupy 2-4 osobowe. Będziemy pracować w sprintach tygodniowych, wyjątkowo 2-tygodniowych.

Każdy sprint będzie oceniany (ta sama ocena na grupę chyba że wewnętrznie ustalicie inaczej). Oceny za sprint: 0 (nic), 1 (tak sobie), 2 (wszystko zrobione), 3 (byłem pod wrażeniem pracy). Ocena końcowa:
- **lab**: suma punktów ze sprintów = 70% oceny, jeżeli w każdym sprincie otrzymacie 2 pkt to za wszystkie będzie 70% oceny (ocena 4.0). Dodatkowe 30% punktów to działający projekt w takiej formie żeby dało się go uruchomić i zaprezentować w następnym roku (binarka, kontener, deploy przez ansibla, docker-file, etc...). Więcej na zajęciach, forma do uzgodnienia.
- **projekt**: ocena wystawiana podczas prezentacji (średnia ze wszystkich prezentacji).

**Zajęcia projektowe** zrobimy co najmniej 3x w semestrze (dla wszystkich na raz, daty tych spotkań TBD). Wtedy grupy zaprezentują swoje wyniki - pokażecie innym co udało Wam się uzyskać. Prezentacje w sali wykładowej on-site (nie zdalnie). To mogą być prezentacje nieskończonych projektów.

**Zajęcia labowe** to konsultacja z każdą grupą indywidualnie (\~15minut). Omawiamy wtedy progres z poprzedniego sprintu i planujemy kolejny sprint. Harmonogram spotkań dowolny.

Cały workflow oprzemy o [issue](https://gitlab.tele.agh.edu.pl/kwant/ai-exploration-2026/-/boards). Jeden temat to jedno issue z wieloma aktywnościami (Activity). Tam raportujecie całą swoją pracę a ja oceniam sprint po aktywności.

Macie pomysł na temat/projekt, wpiszcie go w `Open`. Jeżeli to jest temat którym chcecie się później zająć to zróbcie `assign` do siebie, jeżeli nie to zostawcie wolny - może kogoś innego zainspiruje. Jak pracujecie nad tematem to ma być w `Doing`, przed ewaluacją, gotowy i kompletny sprint przesuwacie do `Review`. Tematy do oceny mają znaleźć się w `Review` dzień wcześniej.

Po zakończeniu tematu/projektu należy utworzyć wiki z opisem - przenieść wpisy z issue do utworzonego tematu na wiki, uporządkować, umieścić w hierarchii, upewnić się że są widoczne na stronie głównej i issue zamknąć (przenieść do `Closed`). Wtedy można rozpocząć nowy projekt. Wszystkie projekty mają się zakończyć prezentacjami.

Format `issue`:

- w opisie (edit issue) ma być opis zadania, można go uzupełniać/modyfikować (ma być aktualny), w opisie musi znaleźć się linijka identyfikująca grupę w formacie: `grupa:group_nazwa_grupy` (krytycznie ważne bo skrypt oceniający się pogubi),
- w "Activity" wypełniacie pracę którą raportujecie z bieżącego sprintu - to oceniam, w tekście musi się znaleźć etykieta aktualnego sprintu (np: ~sprint_01) albo aktualnych sprintów jeżeli 2-tygodniowy sprint (np: ~sprint_01 ~sprint_02), może być wiele "Activity" dla jednego sprintu - np. każda osoba oddzielny wpis, formatujcie activity od razu tak, żeby potem było prosto zrobić z tego raport

Specjalne 'issue':

- #1 podział na grupy
- #2 aktualne punkty

Harmonogram podziału zajęć w czwartki: [google doc](https://docs.google.com/spreadsheets/d/1018lKCmXuuG4wCYo06VUlAUwqygWA7kC5j7hI4rYx0A/edit), wpisz/zarezerwuj termin dla grupy - wpisz nazwę grupy w uzgodnionym (powyżej) formacie.

## inspiracje/przykładowe tematy

* generowanie gier
* read team - blue team dla usług LLM (minimum 2 zespoły). Nie atakujemy inaczej, niż przez prompt lub źródło danych 
* Rozpoznawanie małych zwierząt z kamer w lesie
* UI/UX
* test Turinga
* LLM lokalnie (małe 7-14B, na GPU albo CPU, kwantyzacja, telefon komórkowy?) - zainstalować/przetestować
* LLM rozproszone (w Instytucie mamy 4xGTX4090 24GB, możemy przetestować większy model) - zainstalować/przetestować
* generowanie mediów (myzka/film/obrazki), sprawdzić dokładność - np. które modele generują poprawną liczbę rąk/palców
* wziąć którąś z pracy z [2023](https://gitlab.tele.agh.edu.pl/wh_vr_2022/ai_exploration/-/wikis/home) powtórzyć ten sam eksperyment tylko na nowszych narzędziach, sprawdzić co się zmieniło
* coś z bardzo długim kontekstem (gogle gemini ma \~1M context window), wrzucić do takiego modelu duży kod źródłowy/książkę i sprawdzić jak to działa? ile informacji można z tego wydobyć?
* **Wasz pomysł** - liczymy na kreatywność :-) pomysły/zakres mają być ze mną uzgodnione

Do wszystkich wyników podawajcie rodzaj użytych modeli (nazwy, wersje, parametry - w tym sposoby kwantyzacji). We wszystkich eksperymentach podajcie prompt (ale nie screenshot), tak żeby w przyszłym roku można było sprawdzić na nowych modelach i sprawdzić jaki progres.

Tips&Tricks:

* spróbujcie wielokrotnie zapytać o to samo (ten sam prompt) i zobaczcie jak różne są wyniki,
* używajcie zarówno darmowych modeli jak i spróbujcie czegoś komercyjnego (będzie trzeba poświecić ze 2 piwa), najpierw za free żeby sprawdzić jakie są granice a potem zobaczcie jaka jest różnica pomiędzy Fable, Opus a Sonnet.

Zeszły rok (2025):
* [Mistrz Gry](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/Mistrz-Gry) 
* [Promptografia](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/Promptografia---Jak-zrobi%C4%87-zdj%C4%99cie-nie-maj%C4%85c-aparatu%3F)
* [AI jako asystent medyczny](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/-AI-jako-asystent-medyczny)
* [Poker LLM](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/Poker-LLM)
* [DeObfuskacja kod](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/Large-Language-Malware---Jak-dobrze-modele-j%C4%99zykowe-analizuj%C4%85-zaciemniony-kod)
* [deep-fake-video](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/DeepSzpont:-Badanie-postrzegalno%C5%9Bci-wideo-generowanego-przez-AI)
* [generowanie komiksów](https://gitlab.tele.agh.edu.pl/kwant/AI_Exploration_2024/-/wikis/Modele-vs-generowanie-komiks%C3%B3w)


## Pokazy

Na koniec przedmiotu IoT będą pokazy piątek 11.12.2026 o godzinie 12:00 do 15:00 w budynku B9 drugie piętro. Zachęcamy, żeby na ten termin mieć coś gotowego i pokazać. Ma być kilka osób nie tylko od nas z instytutu, więc można kogoś poznać. Zawsze dobrze jest wystawić swój pomysł jako demo. To dużo uczy. Oczywiście coś musi już działać, bo inaczej szkoda to robić. 

## Prezentacje 2025  -> TBD 2026

Format: Slot \[datatime\] Temat: XXX (grupa YYY) 

## projekty 2026

Tutaj powinny zostać dołączone raporty z Waszej pracy. Na tej stronie proszę wstawiać tylko linki do podstron wiki. Wszystkie materiały mają być w całości umieszczone w tym repozytorium (tekst, obrazki, audio, filmy). Proszę nie przesadzać z wielkością plików.

* **Tekst**:
  * projekt 1 temat opis, link
  * następny projekt związany z tekstem
* **Prompt injection**:
  * projekt 1 związany z w prompt injectino
  * ....
```


