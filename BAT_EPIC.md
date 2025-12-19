# 🏗️ EPIC: Blender Addon Template (Production-ready)

## 📌 Kontext

Plánujeme dlouhodobě vyvíjet **více Blender addonů** (pro Blender 4.5+), které:
- nejsou jednorázové skripty,
- mají vlastní robustní core logiku,
- využívají externí Python závislosti (např. `websocket-client`),
- disponují vlastními testy a dokumentací,
- jsou stabilní při reloadu i při běhu mimo Blender (CI, pdoc).

### Ponaučení z minulosti
Dosavadní pokusy ukázaly kritická místa:
- **Vendoring chaos:** Přímé vkládání závislostí vede k importním konfliktům.
- **Propletené testy:** Testy uvnitř addonu komplikují distribuci i importy.
- **Nestabilita:** Nesprávný reload addonu často způsobuje pád celého Blenderu.
- **Fragmentace:** Bez jednotné struktury se chyby opakují u každého nového projektu.

### Cíl
Vytvořit **jedno centrální template repo** (`lebduska/blender-addon-template`), které:
- Bude sloužit jako standardizovaný základ pro všechny budoucí addony.
- Bude využívat best-practices z osvědčených open-source projektů.
- Odstraní opakující se technické problémy (importy, reload, testy, závislosti).
- Bude nastaveno jako **GitHub Template repository**.

---

## 🎯 Cíle EPICu

Vytvořit **produkčně použitelnou šablonu**, která:
1. **Separuje zájmy:** Striktní oddělení core logiky od Blender API (`bpy`).
2. **Spravuje závislosti:** Možnost používat externí knihovny bez konfliktů.
3. **Definuje testování:** Jasná pravidla pro unit, integration a headless Blender testy.
4. **Zajišťuje stabilitu:** Bezpečný reload mechanismus (žádné pády).
5. **Je agnostická k prostředí:** Importovatelná i mimo Blender (pro CI/CD a dokumentaci).
6. **Je snadno použitelná:** Rychlý start nového projektu přes „Use this template“.

---

## 🏛️ Architektonické principy (Principles)

### P1 – Core ≠ Blender
- Veškerá aplikační logika MUSÍ být v adresáři `core/`.
- `core/` nesmí importovat `bpy` ani jiné moduly závislé na Blenderu.
- Blender kód slouží pouze jako adaptér (thin glue).

### P2 – Blender je runtime, ne testovací prostředí
- Unit testy běží standardně v OS, nikoliv uvnitř Blenderu.
- Blender-specifické funkce se testují buď mockováním, nebo cíleným headless testem.

### P3 – Žádné testy uvnitř distribučního balíčku
- Finální addon neobsahuje složku `tests/`.
- Testy jsou vždy umístěny v kořenovém adresáři mimo balík addonu.

### P4 – Inteligentní správa závislostí
- Externí závislosti se instalují do `_deps/` (např. pomocí `pip`).
- Addon musí být schopen se zaregistrovat i bez závislostí (např. zobrazit UI výzvu k instalaci).

### P5 – Bezpečný a odložený reload
- Reload se provádí asynchronně přes `bpy.app.timers.register`.
- Je zakázáno joinovat thready přímo v UI threadu (prevence zamrzání).

### P6 – Import-safe kód
- Samotný import modulu nesmí spouštět žádnou runtime logiku.
- Veškerá inicializace patří do funkcí `register()` / `unregister()`.

---

## 📂 Navržená struktura repozitáře

```text
blender-addon-template/
├── addon/
│   └── my_addon/
│       ├── __init__.py      # Registrace a vstupní bod
│       ├── blender/         # UI, Operátory, Handlery (Blender glue)
│       │   ├── registration.py
│       │   ├── panels.py
│       │   ├── operators.py
│       │   └── handlers.py
│       ├── core/            # Čistá logika (bez bpy)
│       │   ├── client.py
│       │   ├── protocol.py
│       │   ├── state.py
│       │   └── serialize.py
│       └── deps/            # Logika pro načítání závislostí
│           └── deps.py
├── tests/                   # Testy (mimo addon balík)
│   ├── unit/                # Core logika (rychlé)
│   ├── integration/         # Komunikace a flow
│   └── blender/             # Headless Blender testy
├── tools/                   # Pomocné skripty
│   ├── run_blender_tests.py
│   └── build_zip.py
├── pyproject.toml           # Konfigurace buildu a toolingu
├── pytest.ini               # Konfigurace testů
├── README.md
├── TESTING.md
└── LICENSE (GPL v3)
```

---

## 🧪 Testovací strategie

| Typ testu | Umístění | Prostředí | Zaměření |
| :--- | :--- | :--- | :--- |
| **Unit** | `tests/unit` | Standard Python | Logika v `core/` |
| **Integration** | `tests/integration` | Standard Python | Komunikační protokoly |
| **Blender** | `tests/blender` | Headless Blender | Integrace s `bpy` |

---

## ✅ Definition of Done (DoD)

- [ ] Repo je nakonfigurováno jako GitHub Template.
- [ ] Nový addon lze vytvořit jedním kliknutím („Use this template“).
- [ ] Unit testy lze spustit v CI bez instalace Blenderu.
- [ ] Ukázkový Headless Blender test úspěšně projde.
- [ ] Reload addonu nevyvolá pád Blenderu.
- [ ] Dokumentace (`README.md`, `TESTING.md`) obsahuje jasné instrukce pro vývoj.

---

## 💡 AI Notes (Pokyny pro vývoj)

- Implementuj pouze **skeleton** (kostru) bez zbytečné business logiky.
- Preferuj **čitelnost** a dodržování Python standardů (PEP8).
- Cílová verze: **Blender 4.5+**.
- Všechny moduly v `blender/` musí být snadno rozšiřitelné.
