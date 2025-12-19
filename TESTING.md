# 🧪 Testování Blender Addonu

Tento projekt využívá rozdělenou testovací strategii pro zajištění stability a rychlosti vývoje.

## 1. Unit Testy (Standardní Python)
Testují logiku v adresáři `addon/my_addon/core/`. Jsou nezávislé na Blenderu a běží velmi rychle.

**Spuštění:**
```bash
python3 -m unittest discover tests/unit
# nebo pokud máte nainstalovaný pytest:
pytest tests/unit
```

## 2. Blender Testy (Headless Blender)
Testují integraci s Blender API (`bpy`). Vyžadují nainstalovaný Blender.

**Spuštění:**
```bash
python3 tools/run_blender_tests.py
```
*Poznámka: Můžete nastavit cestu k Blenderu pomocí proměnné prostředí `BLENDER_PATH`.*

## 3. Integrační Testy
Testují flow celého systému, např. simulaci síťové komunikace.

**Spuštění:**
```bash
pytest tests/integration
```

## Proč takto?
- **Rychlost:** Unit testy běží v milisekundách.
- **CI/CD:** Testy v `core/` lze snadno spouštět v GitHub Actions bez nutnosti instalovat Blender.
- **Stabilita:** Headless testy v Blenderu odhalí chyby v registraci nebo UI dříve, než addon otevřete ručně.
